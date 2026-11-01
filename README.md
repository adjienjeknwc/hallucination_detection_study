# Hallucination Detection in Large Language Models: An Empirical Study on HaluEval

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/adjienjeknwc/hallucination_detection_study/blob/main/hallucination_detection_study.ipynb)

An end-to-end empirical study and reproducible Google Colab notebook comparing lexical and semantic hallucination detectors on the **HaluEval Question-Answering (QA)** benchmark.

---

## 📌 Study Overview

Large Language Models (LLMs) frequently generate answers that appear fluent and authoritative yet contradict or remain unsubstantiated by reference knowledge—a vulnerability known as **hallucination**. Reliable detection of factual inconsistency is essential for real-world question answering and Retrieval-Augmented Generation (RAG) pipelines.

This study implements an empirical evaluation comparing two distinct paradigms:
1. **Model A (Lexical Baseline):** TF-IDF Vectorizer (unigrams + bigrams, sublinear TF) + balanced Logistic Regression.
2. **Model B (Semantic NLI Cross-Encoder):** Pretrained `cross-encoder/nli-deberta-v3-small` evaluating premise–hypothesis entailment.

---

## 🚀 How to Run in Google Colab

1. **Upload Notebook:** Upload [`hallucination_detection_study.ipynb`](./hallucination_detection_study.ipynb) to [Google Colab](https://colab.research.google.com/).
2. **Select GPU Runtime:**
   - In Colab menu: **Runtime** $\rightarrow$ **Change runtime type**
   - Hardware accelerator: **T4 GPU** (free tier)
3. **Execute Top-to-Bottom:**
   - In Colab menu: **Runtime** $\rightarrow$ **Run all** (`Ctrl+F9` / `Cmd+F9`)
   - **Zero manual edits required**: All dependencies (`datasets`, `transformers`, `torch`, `scikit-learn`, etc.) install automatically in Cell 1.
   - Total execution time: **~60–90 seconds** on a T4 GPU.

---

## 🧪 Pipeline & Methodology Breakdown

```
Raw HaluEval QA Records (10,000 Questions)
               │
               ▼
┌────────────────────────────────────────────────────────┐
│  STEP 3: Leakage-Resistant Question-Level Split         │
│  (Split questions before expanding into answer pairs)  │
└──────────────────────┬─────────────────────────────────┘
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
   Train Set       Validation Set    Held-Out Test Set
  7,000 Qs         1,000 Qs          2,000 Qs
  (14,000 answers) (2,000 answers)   (4,000 answers)
       │               │               │
       ▼               │               ├────────────────────────┐
┌──────────────┐       │               ▼                        ▼
│ STEP 4:      │       │      Full 4,000 Answers       Fixed 300 Sample
│ Train TF-IDF │       │      (TF-IDF Evaluation)      (150 Supp, 150 Halluc)
│ + LogReg     │       │               │                        │
└──────────────┘       │               │                        ▼
                       │               │               ┌───────────────────┐
                       │               │               │ STEP 5 & 6:       │
                       ▼               │               │ TF-IDF vs NLI     │
               ┌───────────────┐       │               │ - Rule 1 (Argmax) │
               │ STEP 6:       │       │               │ - Rule 2 (τ*)     │
               │ NLI Threshold │───────┼───────────────┤ - Bootstrap 95% CI│
               │ Sweep (τ)     │       │               └───────────────────┘
               └───────────────┘       │                        │
                                       ▼                        ▼
                       ┌───────────────────────────────────────────────────┐
                       │ STEP 7: Export results.csv & High-Resolution PNGs │
                       └───────────────────────────────────────────────────┘
```

### Step 1: Environment Setup & Reproducibility
- Automated installation of `datasets`, `scikit-learn`, `transformers`, `torch`, `pandas`, `matplotlib`, and `seaborn`.
- Global deterministic random seed `SEED = 42` set for Python, NumPy, PyTorch CPU, and PyTorch CUDA.
- Dynamic GPU/CUDA verification (`torch.cuda.is_available()`).

### Step 2: Data Loading & Preparation
- Loads `pminervini/HaluEval` (`qa` config, `data` split) from Hugging Face (10,000 records).
- Converts each record into **two binary classification examples**:
  - `right_answer` $\rightarrow$ **Label 0 (Supported)**
  - `hallucinated_answer` $\rightarrow$ **Label 1 (Hallucinated)**
- Formats model input text:
  $$\text{input\_text} = \text{"Knowledge: "} + \text{knowledge} + \text{" Question: "} + \text{question} + \text{" Answer: "} + \text{candidate\_answer}$$

### Step 3: Leakage-Resistant Split
- **Why question-level splitting matters:** Splitting after answer expansion causes reference and hallucinated answers from the same question to cross partitions. Classifiers memorize entities and question topics instead of learning factual consistency.
- Questions are assigned a persistent `original_question_id`, deterministically shuffled, and partitioned:
  - **Train partition:** 7,000 questions (14,000 answer examples, 50/50 balance).
  - **Validation partition:** 1,000 questions (2,000 answer examples, 50/50 balance).
  - **Held-out test partition:** 2,000 questions (4,000 answer examples, 50/50 balance).
- An automated assertion test mathematically verifies zero question overlap across partitions.

### Step 4: TF-IDF Baseline
- `TfidfVectorizer`: `ngram_range=(1, 2)` (unigrams + bigrams), `max_features=50000`, `sublinear_tf=True`.
- `LogisticRegression`: `max_iter=1000`, `class_weight='balanced'`, `random_state=42`.
- Fitted on `train_df` (14,000 answers) and evaluated on the full held-out `test_df` (4,000 answers).
- Reports accuracy, per-class classification report (precision, recall, F1), and confusion matrix.

### Step 5: NLI Detector (`cross-encoder/nli-deberta-v3-small`)
- Pretrained cross-encoder on SNLI and MultiNLI.
- **Premise:** Knowledge passage (ground truth evidence).
- **Hypothesis:** Candidate answer (isolated claim to verify; omitting question syntax avoids confounding the entailment classifier).
- **GPU Batched Inference:** Softmax probabilities over `[contradiction (0), entailment (1), neutral (2)]`.
- **Rule 1 (Argmax Decision Rule):**
  - $\text{argmax} = \text{entailment (1)} \implies \text{Label 0 (Supported)}$
  - $\text{argmax} = \text{contradiction (0)} \implies \text{Label 1 (Hallucination Risk)}$
  - $\text{argmax} = \text{neutral (2)} \implies \text{Label 1 (Hallucination Risk, conservative mapping)}$
- Evaluated on a fixed, class-balanced sample of **300 test examples** (150 supported, 150 hallucinated).
- Generates a side-by-side comparison table with TF-IDF on the identical sample.

### Step 6: Validation-Tuned Threshold Analysis
- **Rule 2:** Mark an answer as **Supported (0)** if and only if $P(\text{entailment}) \ge \tau$; otherwise, flag as **Hallucination Risk (1)**.
- Sweeps $\tau \in [0.50, 0.95]$ in increments of $0.05$ on the **validation partition only** ($2,000$ answers).
- Selects optimal $\tau^*$ that maximizes validation F1 for hallucination detection.
- Applies $\tau^*$ once to the 300-example sample and reports metrics, confusion matrix, false-positive rate (FPR), and specificity.
- Includes clear documentation that the 300-sample reuse is diagnostic, not an independent test.

### Step 7: Plots & Output Artifacts
Generates and saves:
1. `metrics_comparison.png`: High-resolution bar chart comparing TF-IDF, NLI Rule 1, and NLI Rule 2.
2. `confusion_matrices.png`: 4-panel annotated heatmap grid of all confusion matrices.
3. `threshold_sweep.png`: Precision, recall, and F1 dynamics across thresholds $\tau \in [0.50, 0.95]$.
4. `results.csv`: Comprehensive CSV export of all models, subsets, and metrics.

### Step 8: Statistical Rigor & Wrap-up
- **Bootstrap 95% Confidence Intervals:** $B = 2,000$ iterations to compute empirical percentile confidence intervals for accuracy across all models and sample sizes.
- **Dynamic Findings Summary:** Code cell that renders findings dynamically using live computed variables—guaranteeing every number comes from real code output.
- **Limitations Discussion:** In-depth analysis of sample size constraints, benchmark domain specificity, threshold diagnostic reuse, and elliptical QA hypotheses.

---

## 📁 Repository Structure

```
hallucination-detection-study/
├── hallucination_detection_study.ipynb   # Main Google Colab notebook
├── build_notebook.py                    # Programmatic notebook builder
├── generate_notebook.py                 # Notebook generator script
├── test_pipeline_logic.py               # Unit tests for core pipeline logic
└── README.md                            # Complete documentation & study guide
```

---

## 📊 Summary of Generated Output Files

When executed in Google Colab, the notebook automatically saves the following files in the runtime workspace:
- `results.csv`: Table containing Model Name, Partition, Accuracy, Precision, Recall, F1, FPR, Specificity, and Confusion Matrix elements.
- `metrics_comparison.png`: Visual bar chart comparing model performances on the 300-example sample.
- `confusion_matrices.png`: 4-panel confusion matrix heatmap grid.
- `threshold_sweep.png`: Validation threshold curve illustrating the precision–recall trade-off.
