"""
Builds a high-impact, professional 16:9 widescreen PowerPoint presentation (.pptx)
and an interactive HTML presentation deck for the Hallucination Detection research project.
Authors: Prachi Chauhan & Aditi Verma (Manipal University Jaipur)
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    DARK_NAVY = RGBColor(15, 23, 42)      # #0F172A
    CARD_BG = RGBColor(255, 255, 255)     # #FFFFFF
    BG_LIGHT = RGBColor(248, 250, 252)    # #F8FAFC
    PRIMARY_BLUE = RGBColor(37, 99, 235)  # #2563EB
    TEXT_MAIN = RGBColor(15, 23, 42)      # #0F172A
    TEXT_MUTED = RGBColor(100, 116, 139)  # #64748B
    BORDER_COLOR = RGBColor(226, 232, 240)# #E2E8F0
    ACCENT_GREEN = RGBColor(16, 185, 129) # #10B981
    ACCENT_RED = RGBColor(225, 29, 72)    # #E11D48
    ACCENT_AMBER = RGBColor(217, 119, 6)  # #D97706
    ACCENT_PURPLE = RGBColor(124, 58, 237)# #7C3AED

    def add_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="EMPIRICAL RESEARCH STUDY"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = PRIMARY_BLUE

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.65))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_MAIN

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=BORDER_COLOR):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        return card

    # ==============================================================================
    # SLIDE 1: TITLE SLIDE (Dark Navy Theme)
    # ==============================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_bg(slide1, DARK_NAVY)

    # Accent decorative bar
    bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(1.3), Inches(1.2), Inches(0.08))
    bar.fill.solid()
    bar.fill.fore_color.rgb = PRIMARY_BLUE
    bar.line.fill.background()

    # Category badge
    tb_badge = slide1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(0.4))
    p_b = tb_badge.text_frame.paragraphs[0]
    p_b.text = "RESEARCH PAPER & EMPIRICAL BENCHMARK EVALUATION"
    p_b.font.size = Pt(12)
    p_b.font.bold = True
    p_b.font.color.rgb = PRIMARY_BLUE

    # Main Title
    tb_title = slide1.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(11.3), Inches(1.6))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Hallucination Detection in Large Language Models"
    p_t.font.size = Pt(36)
    p_t.font.bold = True
    p_t.font.color.rgb = RGBColor(255, 255, 255)

    # Subtitle
    tb_sub = slide1.shapes.add_textbox(Inches(1.0), Inches(3.4), Inches(11.3), Inches(0.8))
    tf_s = tb_sub.text_frame
    tf_s.word_wrap = True
    p_s = tf_s.paragraphs[0]
    p_s.text = "A Review of Techniques, Leakage-Resistant Benchmarking, and Operational Trade-Offs"
    p_s.font.size = Pt(18)
    p_s.font.color.rgb = RGBColor(203, 213, 225)

    # Authors Card
    c_author = add_card(slide1, Inches(1.0), Inches(4.5), Inches(11.333), Inches(2.0), bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
    tb_auth = slide1.shapes.add_textbox(Inches(1.3), Inches(4.7), Inches(10.7), Inches(1.6))
    tf_a = tb_auth.text_frame
    tf_a.word_wrap = True

    p_a1 = tf_a.paragraphs[0]
    p_a1.text = "Authors & Researchers:"
    p_a1.font.size = Pt(13)
    p_a1.font.bold = True
    p_a1.font.color.rgb = PRIMARY_BLUE

    p_a2 = tf_a.add_paragraph()
    p_a2.text = "Prachi Chauhan  (prachi.23fe10cii00015@muj.manipal.edu)   •   Aditi Verma  (aditi.23fe10cii00093@muj.manipal.edu)"
    p_a2.font.size = Pt(15)
    p_a2.font.bold = True
    p_a2.font.color.rgb = RGBColor(255, 255, 255)

    p_a3 = tf_a.add_paragraph()
    p_a3.text = "Department of Computer Science and Engineering  |  Manipal University Jaipur"
    p_a3.font.size = Pt(13)
    p_a3.font.color.rgb = RGBColor(148, 163, 184)

    p_a4 = tf_a.add_paragraph()
    p_a4.text = "Benchmark: HaluEval Question-Answering Subset   •   Models: TF-IDF vs. DeBERTa-v3 NLI Cross-Encoder"
    p_a4.font.size = Pt(12)
    p_a4.font.color.rgb = RGBColor(203, 213, 225)

    # ==============================================================================
    # SLIDE 2: THE PROBLEM (The Hallucination Dilemma)
    # ==============================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_bg(slide2, BG_LIGHT)
    add_header(slide2, "The Hallucination Dilemma in Generative AI", "MOTIVATION & BACKGROUND")

    # 3 Cards
    cards_data = [
        ("The Fluency Trap", ACCENT_AMBER, [
            "LLMs generate coherent, grammatically flawless, authoritative responses.",
            "Fluency creates a dangerous illusion of factual correctness.",
            "Standard decoding maximizes token likelihood, not empirical truth.",
            "Users and downstream systems cannot intuitively tell truth from fiction."
        ]),
        ("High Real-World Stakes", ACCENT_RED, [
            "Medical Diagnosis: Fabricating drug interactions or false symptoms.",
            "Legal Informatics: Citing fictitious judicial precedents and statutes.",
            "Finance & News: Hallucinating earnings figures or historical events.",
            "Enterprise RAG: Contradicting private company reference documents."
        ]),
        ("The Detection Challenge", PRIMARY_BLUE, [
            "Detectors must identify fabrications without ground truth during inference.",
            "Lexical matching fails on semantically equivalent paraphrases.",
            "Deep semantic reasoning models are computationally heavy and uncalibrated.",
            "Extreme trade-off: Catching errors vs. blocking correct answers."
        ])
    ]

    for idx, (title, color, bullets) in enumerate(cards_data):
        left = Inches(0.8 + idx * 3.95)
        add_card(slide2, left, Inches(1.5), Inches(3.8), Inches(5.3))
        
        # Header banner
        hbar = slide2.shapes.add_shape(MSO_SHAPE.RECTANGLE, left + Inches(0.3), Inches(1.8), Inches(3.2), Inches(0.06))
        hbar.fill.solid()
        hbar.fill.fore_color.rgb = color
        hbar.line.fill.background()

        tb = slide2.shapes.add_textbox(left + Inches(0.3), Inches(2.0), Inches(3.2), Inches(4.5))
        tf = tb.text_frame
        tf.word_wrap = True
        p_h = tf.paragraphs[0]
        p_h.text = title
        p_h.font.size = Pt(18)
        p_h.font.bold = True
        p_h.font.color.rgb = color

        for b in bullets:
            p_b = tf.add_paragraph()
            p_b.text = f"•  {b}"
            p_b.font.size = Pt(13)
            p_b.font.color.rgb = TEXT_MAIN
            p_b.space_before = Pt(10)

    # ==============================================================================
    # SLIDE 3: CONCEPTUAL NUANCE (False vs. Unsupported)
    # ==============================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_bg(slide3, BG_LIGHT)
    add_header(slide3, "Factual Falsity vs. Unsupported Claims: A Critical Distinction", "CORE CONCEPTUAL DEFINITION")

    # Left card: Direct Contradiction
    add_card(slide3, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_c1 = slide3.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf1 = tb_c1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "Type A: Factually Contradicted (Conflict)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED

    points_1 = [
        "Definition: The generated statement directly clashes with explicit evidence in the reference text.",
        "Grounding Evidence: 'Water boils at 100°C at standard atmospheric pressure.'",
        "LLM Output: 'Water boils at 50°C under normal sea-level conditions.'",
        "NLI Label: CONTRADICTION (Logit Class 0).",
        "Diagnostic Impact: Clear, objective falsehood; relatively straightforward for attention mechanisms to detect."
    ]
    for pt in points_1:
        p_b = tf1.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    # Right card: Unsupported / Unverifiable
    add_card(slide3, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_c2 = slide3.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf2 = tb_c2.text_frame
    tf2.word_wrap = True

    p2 = tf2.paragraphs[0]
    p2.text = "Type B: Unsupported / Unverifiable (Extrapolation)"
    p2.font.size = Pt(18)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_AMBER

    points_2 = [
        "Definition: The statement may or may not be true in the real world, but cannot be verified by the provided passage.",
        "Grounding Evidence: 'Arthur’s Magazine was an American literary periodical published in Philadelphia.'",
        "LLM Output: 'Arthur’s Magazine was the most widely read publication in Pennsylvania history.'",
        "NLI Label: NEUTRAL (Logit Class 2).",
        "Crucial Insight: In evidence-grounded systems, unsupported claims represent hallucination risk and cannot be trusted!"
    ]
    for pt in points_2:
        p_b = tf2.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    # ==============================================================================
    # SLIDE 4: TAXONOMY (The 6 Detection Families)
    # ==============================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_bg(slide4, BG_LIGHT)
    add_header(slide4, "Taxonomy of Hallucination Detection Techniques", "LITERATURE TAXONOMY (SECTION III)")

    tech_families = [
        ("1. Lexical Classifiers", "TF-IDF, n-grams, word frequency counters paired with linear models. Fast & interpretable but easily fooled by synonyms.", PRIMARY_BLUE),
        ("2. Natural Language Inference", "Premise-hypothesis cross-encoders classifying entailment, contradiction, and neutral. Directly evaluates evidence grounding.", ACCENT_PURPLE),
        ("3. Retrieval Verification", "Queries external live knowledge (Wikipedia, search APIs, vector DBs) to fetch corroborating evidence.", ACCENT_GREEN),
        ("4. Consistency (SelfCheckGPT)", "Samples response multiple times with temperature > 0. High semantic divergence across outputs signals hallucination.", ACCENT_AMBER),
        ("5. Predictive Uncertainty", "Inspects model token logits, entropy, and softmax probability distributions. Low confidence flags potential errors.", ACCENT_RED),
        ("6. Atomic Claim Decomposition", "Deconstructs complex paragraphs into atomic factual propositions and audits each claim independently.", PRIMARY_BLUE)
    ]

    for idx, (title, desc, color) in enumerate(tech_families):
        col = idx % 3
        row = idx // 3
        left = Inches(0.8 + col * 3.95)
        top = Inches(1.5 + row * 2.7)
        add_card(slide4, left, top, Inches(3.8), Inches(2.45))

        tb = slide4.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), Inches(3.3), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(15)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MAIN
        p_d.space_before = Pt(6)

    # ==============================================================================
    # SLIDE 5: METHODOLOGY & LEAKAGE-RESISTANT SPLIT
    # ==============================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_bg(slide5, BG_LIGHT)
    add_header(slide5, "The HaluEval Benchmark & Leakage-Resistant Splitting", "METHODOLOGY & EXPERIMENTAL SETUP")

    # Left: The Benchmark
    add_card(slide5, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_b = slide5.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True

    p = tf_b.paragraphs[0]
    p.text = "Benchmark: HaluEval Question-Answering"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    b_points = [
        "Dataset Source: Hugging Face (pminervini/HaluEval, 'qa' configuration, 'data' split).",
        "Volume: 10,000 raw question-answering records based on HotpotQA context passages.",
        "Paired Records: Each entry contains a reference Knowledge passage, a Question, a Ground Truth Right Answer (Label 0), and a ChatGPT-generated Hallucinated Answer (Label 1).",
        "Expansion: Expanding each record produces exactly 20,000 balanced binary examples (50% Supported, 50% Hallucinated)."
    ]
    for pt in b_points:
        p_b = tf_b.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(10)

    # Right: The Leakage Trap & Solution
    add_card(slide5, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_l = slide5.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True

    p = tf_l.paragraphs[0]
    p.text = "Leakage-Resistant Question Partitioning"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    l_points = [
        "The Data Leakage Risk: Splitting answers after expansion allows right and fake answers from the same question into train & test. The model memorizes topic words rather than learning factual support.",
        "The Solution: Split by Original Question IDs BEFORE expanding answer pairs.",
        "Train Set: 7,000 questions  →  14,000 answer pairs",
        "Validation Set: 1,000 questions  →  2,000 answer pairs",
        "Held-Out Test Set: 2,000 questions  →  4,000 answer pairs",
        "Mathematical Verification: Assertion check in code confirms ZERO question ID overlap across partitions!"
    ]
    for pt in l_points:
        p_b = tf_l.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    # ==============================================================================
    # SLIDE 6: MODEL COMPARISON ARCHITECTURE
    # ==============================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_bg(slide6, BG_LIGHT)
    add_header(slide6, "Architectural Design: Lexical vs. Semantic Detectors", "DETECTION MODELS")

    # Model 1 Card
    add_card(slide6, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_m1 = slide6.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_m1 = tb_m1.text_frame
    tf_m1.word_wrap = True

    p = tf_m1.paragraphs[0]
    p.text = "Model A: TF-IDF + Logistic Regression"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    m1_points = [
        "Approach: Supervised statistical lexical frequency baseline.",
        "N-Gram Features: Unigrams + Bigrams (ngram_range=(1, 2)) to capture compound entities.",
        "Vocabulary Cap: max_features = 50,000 tokens.",
        "Sublinear TF: Applies 1 + log(tf) to prevent high-frequency words from dominating decision boundaries.",
        "Classifier: Logistic Regression with balanced class weights and max_iter=1000.",
        "Input Format: Full concatenated string: Knowledge + Question + Candidate Answer."
    ]
    for pt in m1_points:
        p_b = tf_m1.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    # Model 2 Card
    add_card(slide6, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_m2 = slide6.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_m2 = tb_m2.text_frame
    tf_m2.word_wrap = True

    p = tf_m2.paragraphs[0]
    p.text = "Model B: Pretrained NLI Cross-Encoder"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE

    m2_points = [
        "Architecture: cross-encoder/nli-deberta-v3-small (DeBERTa-v3 fine-tuned on SNLI & MultiNLI).",
        "Premise: Ground truth Knowledge passage.",
        "Hypothesis: Candidate Answer alone (Design Choice: isolates factual claim without question syntax noise).",
        "Full Cross-Attention: Simultaneously computes attention between all premise and hypothesis tokens.",
        "Output Classes: [0: Contradiction, 1: Entailment, 2: Neutral].",
        "Rule 1 (Argmax): Entailment → 0 (Supported); Contradiction & Neutral → 1 (Hallucination Risk)."
    ]
    for pt in m2_points:
        p_b = tf_m2.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    # ==============================================================================
    # SLIDE 7: RESULTS: 4,000 HELD-OUT TEST EVALUATION
    # ==============================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_bg(slide7, BG_LIGHT)
    add_header(slide7, "Lexical Baseline Results on 4,000 Held-Out Answers", "EMPIRICAL FINDINGS (SECTION V-A)")

    # KPI Stat Card
    add_card(slide7, Inches(0.8), Inches(1.5), Inches(3.6), Inches(5.3), bg_color=DARK_NAVY)
    tb_kpi = slide7.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(3.2), Inches(4.7))
    tf_k = tb_kpi.text_frame
    tf_k.word_wrap = True

    p = tf_k.paragraphs[0]
    p.text = "TEST ACCURACY"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    p2 = tf_k.add_paragraph()
    p2.text = "70.57%"
    p2.font.size = Pt(44)
    p2.font.bold = True
    p2.font.color.rgb = RGBColor(255, 255, 255)

    p3 = tf_k.add_paragraph()
    p3.text = "Evaluated on 4,000 leakage-resistant answer examples (2,000 supported, 2,000 hallucinated)."
    p3.font.size = Pt(13)
    p3.font.color.rgb = RGBColor(203, 213, 225)
    p3.space_before = Pt(15)

    p4 = tf_k.add_paragraph()
    p4.text = "95% Bootstrap CI:\n[69.15%, 72.00%]\nError Margin: ±1.42%"
    p4.font.size = Pt(13)
    p4.font.bold = True
    p4.font.color.rgb = ACCENT_GREEN
    p4.space_before = Pt(20)

    # Table & Breakdown Card
    add_card(slide7, Inches(4.7), Inches(1.5), Inches(7.8), Inches(5.3))
    tb_tbl = slide7.shapes.add_textbox(Inches(5.0), Inches(1.8), Inches(7.2), Inches(4.7))
    tf_t = tb_tbl.text_frame
    tf_t.word_wrap = True

    p = tf_t.paragraphs[0]
    p.text = "Per-Class Performance Metrics (Classification Report)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_MAIN

    pts = [
        "Supported Answers (Class 0): Precision: 0.67  |  Recall: 0.82  |  F1: 0.74",
        "Hallucinated Answers (Class 1): Precision: 0.77  |  Recall: 0.59  |  F1: 0.67",
        "Macro Average: Precision: 0.72  |  Recall: 0.71  |  F1: 0.70",
        "Confusion Matrix Analysis (4,000 answers):",
        "  • True Negatives (Supported correctly accepted): 1,643",
        "  • False Positives (Supported incorrectly flagged): 357",
        "  • False Negatives (Hallucinations missed): 820  (41% missed!)",
        "  • True Positives (Hallucinations caught): 1,180",
        "Takeaway: The baseline detects supported text reliably (82% recall), but allows over 40% of hallucinations to slip through undetected."
    ]
    for pt in pts:
        p_b = tf_t.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(6)

    # ==============================================================================
    # SLIDE 8: HEAD-TO-HEAD COMPARISON (Table V-B / Table I)
    # ==============================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_bg(slide8, BG_LIGHT)
    add_header(slide8, "Comparative Evaluation on 300 Examples (Table I)", "HEAD-TO-HEAD MODEL COMPARISON")

    # Add Table
    table_shape = slide8.shapes.add_table(5, 4, Inches(0.8), Inches(1.5), Inches(11.7), Inches(2.6))
    table = table_shape.table

    # Column widths
    table.columns[0].width = Inches(3.0)
    table.columns[1].width = Inches(2.7)
    table.columns[2].width = Inches(2.7)
    table.columns[3].width = Inches(3.3)

    table_data = [
        ["Evaluation Metric", "TF-IDF Baseline", "NLI Detector (Argmax)", "Operational Implication"],
        ["Accuracy", "69.33%", "45.33%", "TF-IDF achieves higher overall accuracy"],
        ["Precision (Hallucinations)", "75.89%", "47.15%", "TF-IDF has far fewer false alarms"],
        ["Recall (Safety Catch)", "56.67%", "77.33% (+20.7%)", "NLI catches significantly more hallucinations!"],
        ["F1-Score", "64.89%", "58.59%", "TF-IDF balances precision and recall better"]
    ]

    for r_idx, row in enumerate(table_data):
        for c_idx, cell_value in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = cell_value
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER if c_idx > 0 else PP_ALIGN.LEFT
            if r_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = DARK_NAVY
                p.font.bold = True
                p.font.color.rgb = RGBColor(255, 255, 255)
                p.font.size = Pt(13)
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = CARD_BG
                p.font.size = Pt(12)
                p.font.color.rgb = TEXT_MAIN
                if c_idx == 2 and r_idx == 3:
                    p.font.bold = True
                    p.font.color.rgb = ACCENT_GREEN

    # Explanatory card below table
    add_card(slide8, Inches(0.8), Inches(4.4), Inches(11.7), Inches(2.4))
    tb_exp = slide8.shapes.add_textbox(Inches(1.1), Inches(4.55), Inches(11.1), Inches(2.1))
    tf_e = tb_exp.text_frame
    tf_e.word_wrap = True

    p = tf_e.paragraphs[0]
    p.text = "Why Did TF-IDF Outperform Deep NLI in Accuracy? (The Paradox Explained)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    e_pts = [
        "Dataset Artifacts: TF-IDF was trained directly on 14,000 HaluEval QA examples, allowing it to exploit subtle ChatGPT lexical markers and vocabulary distributions.",
        "Zero-Shot NLI Bias: The NLI model was evaluated off-the-shelf without task-specific fine-tuning.",
        "Elliptical QA Answers: Many correct answers in HaluEval are concise noun phrases (e.g. 'Arthur’s Magazine'). Because they lack full subject-verb-object syntax, the NLI model assigned them NEUTRAL scores.",
        "Conservative Rule Penalty: Rule 1 maps Neutral to Hallucination Risk, generating numerous false alarms on valid short answers."
    ]
    for pt in e_pts:
        p_b = tf_e.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(4)

    # ==============================================================================
    # SLIDE 9: THRESHOLD ANALYSIS (Rule 2)
    # ==============================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_bg(slide9, BG_LIGHT)
    add_header(slide9, "Validation-Tuned Entailment Thresholding (Rule 2)", "THRESHOLD OPTIMIZATION (SECTION V-C)")

    # Left: Tuning Strategy
    add_card(slide9, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_t1 = slide9.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_t1 = tb_t1.text_frame
    tf_t1.word_wrap = True

    p = tf_t1.paragraphs[0]
    p.text = "Rule 2 Strategy & Validation Sweep"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    t1_pts = [
        "Rule 2 Definition: Mark candidate answer as Supported (0) IF AND ONLY IF P(entailment) >= tau; otherwise flag as Hallucination Risk (1).",
        "Threshold Grid: Swept tau in [0.50, 0.95] with step 0.05 strictly on the 2,000 validation answers.",
        "Optimal Threshold Selection: tau* = 0.95 maximized validation F1 (59.61%).",
        "Validation Metrics at tau = 0.95:",
        "  • Validation Accuracy: 44.06%",
        "  • Validation Precision: 46.65%",
        "  • Validation Recall: 82.56%",
        "Diagnostic Protocol Note: The 300-sample was reused to inspect behavioral shift; this is diagnostic, not an independent final test."
    ]
    for pt in t1_pts:
        p_b = tf_t1.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    # Right: Diagnostic Test Results on 300 Sample
    add_card(slide9, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_t2 = slide9.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_t2 = tb_t2.text_frame
    tf_t2.word_wrap = True

    p = tf_t2.paragraphs[0]
    p.text = "Diagnostic Test on 300 Sample (tau = 0.95)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER

    t2_pts = [
        "Accuracy: 44.67%",
        "Precision (Hallucinations): 47.04%",
        "Recall (Hallucinations): 84.67%  (Catches 127 of 150 fake answers!)",
        "F1-Score: 60.48%",
        "False Positive Rate (FPR): 95.33%  (Catastrophic false alarms!)",
        "Specificity (TNR): 4.67%  (Only 7 of 150 supported answers accepted!)",
        "Critical Finding: Demanding 95% entailment confidence catches almost all hallucinations, but rejects nearly every legitimate answer."
    ]
    for pt in t2_pts:
        p_b = tf_t2.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    # ==============================================================================
    # SLIDE 10: CONFUSION MATRIX DEEP DIVE (The Usability Penalty)
    # ==============================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_bg(slide10, BG_LIGHT)
    add_header(slide10, "The Safety vs. Usability Penalty: Confusion Matrix Audit", "ERROR AUDIT & TRADEOFF ANALYSIS")

    # 2 Comparison Cards (Rule 1 vs Rule 2)
    # Card 1: Rule 1
    add_card(slide10, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_cm1 = slide10.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_cm1 = tb_cm1.text_frame
    tf_cm1.word_wrap = True

    p = tf_cm1.paragraphs[0]
    p.text = "Rule 1: Argmax Decision Rule"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE

    cm1_pts = [
        "Decision Logic: Highest score among [contradiction, entailment, neutral].",
        "True Negatives (Supported Correct): 20 / 150 (13.3%)",
        "False Positives (Supported Rejected): 130 / 150 (86.7%)",
        "False Negatives (Hallucinations Missed): 34 / 150 (22.7%)",
        "True Positives (Hallucinations Caught): 116 / 150 (77.3%)",
        "Summary: High recall (77.3%), but neutral mapping already causes substantial false rejection of valid text."
    ]
    for pt in cm1_pts:
        p_b = tf_cm1.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    # Card 2: Rule 2
    add_card(slide10, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_cm2 = slide10.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_cm2 = tb_cm2.text_frame
    tf_cm2.word_wrap = True

    p = tf_cm2.paragraphs[0]
    p.text = "Rule 2: High Confidence Threshold (tau = 0.95)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED

    cm2_pts = [
        "Decision Logic: Require P(entailment) >= 0.95 for supported classification.",
        "True Negatives (Supported Correct): ONLY 7 / 150 (4.7%)",
        "False Positives (Supported Rejected): 143 / 150 (95.3%!)",
        "False Negatives (Hallucinations Missed): 23 / 150 (15.3%)",
        "True Positives (Hallucinations Caught): 127 / 150 (84.7%)",
        "The Lesson: A detector with 95% FPR acts as a 'brick wall'—it stops false information only by shutting down genuine utility."
    ]
    for pt in cm2_pts:
        p_b = tf_cm2.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    # ==============================================================================
    # SLIDE 11: STATISTICAL RIGOR (Bootstrap Confidence Intervals)
    # ==============================================================================
    slide11 = prs.slides.add_slide(blank_layout)
    add_bg(slide11, BG_LIGHT)
    add_header(slide11, "Statistical Rigor: Bootstrap 95% Confidence Intervals", "STATISTICAL ANALYSIS (B = 2,000 ITERATIONS)")

    # Table for CIs
    ci_table_shape = slide11.shapes.add_table(5, 5, Inches(0.8), Inches(1.5), Inches(11.7), Inches(2.6))
    ci_table = ci_table_shape.table

    ci_table.columns[0].width = Inches(3.6)
    ci_table.columns[1].width = Inches(1.8)
    ci_table.columns[2].width = Inches(2.1)
    ci_table.columns[3].width = Inches(2.4)
    ci_table.columns[4].width = Inches(1.8)

    ci_data = [
        ["Model & Partition", "Sample Size", "Observed Acc", "95% Bootstrap CI", "Error Margin"],
        ["TF-IDF Baseline (Held-out Test)", "4,000", "70.57%", "[69.15%, 72.00%]", "±1.42%"],
        ["TF-IDF Baseline (Comparison Sample)", "300", "69.33%", "[64.00%, 74.33%]", "±5.17%"],
        ["NLI DeBERTa (Rule 1: Argmax)", "300", "45.33%", "[39.67%, 51.00%]", "±5.67%"],
        ["NLI DeBERTa (Rule 2: tau=0.95)", "300", "44.67%", "[39.00%, 50.33%]", "±5.67%"]
    ]

    for r_idx, row in enumerate(ci_data):
        for c_idx, cell_value in enumerate(row):
            cell = ci_table.cell(r_idx, c_idx)
            cell.text = cell_value
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER if c_idx > 0 else PP_ALIGN.LEFT
            if r_idx == 0:
                cell.fill.solid()
                cell.fill.fore_color.rgb = DARK_NAVY
                p.font.bold = True
                p.font.color.rgb = RGBColor(255, 255, 255)
                p.font.size = Pt(13)
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = CARD_BG
                p.font.size = Pt(12)
                p.font.color.rgb = TEXT_MAIN

    # Explanatory card
    add_card(slide11, Inches(0.8), Inches(4.4), Inches(11.7), Inches(2.4))
    tb_ci_exp = slide11.shapes.add_textbox(Inches(1.1), Inches(4.55), Inches(11.1), Inches(2.1))
    tf_ce = tb_ci_exp.text_frame
    tf_ce.word_wrap = True

    p = tf_ce.paragraphs[0]
    p.text = "Why Confidence Intervals are Essential for AI Benchmarking"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    ci_pts = [
        "Sample Size Effect: Evaluating on 300 examples produces an error margin of ~±5.5%, whereas evaluating on 4,000 examples reduces uncertainty to ±1.4%.",
        "Preventing False Superiority Claims: A 3% difference on a 300-example benchmark is often statistical noise, not true model superiority.",
        "Overcoming Literature Flaws: Early hallucination papers reported single point estimates without significance tests; our bootstrap protocol provides statistical bounds."
    ]
    for pt in ci_pts:
        p_b = tf_ce.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(5)

    # ==============================================================================
    # SLIDE 12: LIMITATIONS OF THE STUDY
    # ==============================================================================
    slide12 = prs.slides.add_slide(blank_layout)
    add_bg(slide12, BG_LIGHT)
    add_header(slide12, "Critical Limitations & Methodological Constraints", "STUDY LIMITATIONS (SECTION VII)")

    limitations = [
        ("1. Evaluation Sample Size (300 Examples)", "The head-to-head TF-IDF vs NLI test was conducted on 300 examples due to interactive compute limits. While diagnostic, scaling to all 4,000 answers is needed for definitive enterprise ranking.", ACCENT_AMBER),
        ("2. Synthetic Benchmark Domain (HaluEval)", "HaluEval was generated by ChatGPT perturbing Wikipedia text. It reflects specific synthetic perturbation patterns (negation, entity replacement) that may not generalize to open-ended dialogue.", PRIMARY_BLUE),
        ("3. Diagnostic Threshold Sample Reuse", "The 300 sample was examined under Rule 1 and reused to observe Rule 2. Although threshold selection used validation data, applying it to the same 300 examples is diagnostic, not an isolated holdout test.", ACCENT_RED),
        ("4. Elliptical QA Hypotheses", "Short noun-phrase answers (e.g. 'Arthur’s Magazine') lack full declarative grammar, leading NLI models to assign Neutral rather than Entailment, penalizing accuracy.", ACCENT_PURPLE)
    ]

    for idx, (title, desc, color) in enumerate(limitations):
        col = idx % 2
        row = idx // 2
        left = Inches(0.8 + col * 5.95)
        top = Inches(1.5 + row * 2.7)
        add_card(slide12, left, top, Inches(5.8), Inches(2.45))

        tb = slide12.shapes.add_textbox(left + Inches(0.3), top + Inches(0.2), Inches(5.2), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(16)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MAIN
        p_d.space_before = Pt(6)

    # ==============================================================================
    # SLIDE 13: FUTURE ROADMAP & PRODUCTION SYSTEM
    # ==============================================================================
    slide13 = prs.slides.add_slide(blank_layout)
    add_bg(slide13, BG_LIGHT)
    add_header(slide13, "Production Architecture: The Hybrid Detection Pipeline", "FUTURE RESEARCH & SYSTEM DESIGN")

    stages = [
        ("STAGE 1: Atomic Claim Extraction", "Deconstruct long generative paragraphs into isolated atomic propositions using dependency parsing or LLM prompt extraction.", PRIMARY_BLUE),
        ("STAGE 2: Multi-Source Evidence Retrieval", "Fetch verified grounding documents from internal vector databases, trusted knowledge graphs, and live search indexes.", ACCENT_GREEN),
        ("STAGE 3: Fine-Tuned Domain NLI", "Run specialized, task-fine-tuned cross-encoders comparing each atomic claim against retrieved evidence passages.", ACCENT_PURPLE),
        ("STAGE 4: Calibrated Risk Triage", "Apply calibrated threshold gating. Low-risk responses auto-pass; borderline cases route to human expert review.", ACCENT_AMBER)
    ]

    for idx, (title, desc, color) in enumerate(stages):
        top = Inches(1.5 + idx * 1.35)
        add_card(slide13, Inches(0.8), top, Inches(11.7), Inches(1.2))

        tb = slide13.shapes.add_textbox(Inches(1.1), top + Inches(0.15), Inches(11.1), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(15)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = TEXT_MAIN
        p_d.space_before = Pt(2)

    # ==============================================================================
    # SLIDE 14: CONCLUSION (Dark Navy Theme)
    # ==============================================================================
    slide14 = prs.slides.add_slide(blank_layout)
    add_bg(slide14, DARK_NAVY)

    # Title
    tb_c_title = slide14.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.3), Inches(0.8))
    tf_ct = tb_c_title.text_frame
    p = tf_ct.paragraphs[0]
    p.text = "Conclusion & Key Takeaways"
    p.font.size = Pt(30)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)

    takeaways = [
        ("1. Leakage-Resistant Evaluation is Mandatory", "Random answer-level shuffling introduces subtle lexical data leakage. Question-level partitioning is essential for rigorous factual consistency research."),
        ("2. Lexical Baselines are Strong but Surface-Level", "TF-IDF achieved 70.57% test accuracy by capturing benchmark vocabulary artifacts, but missed over 40% of hallucinations."),
        ("3. Deep Semantic NLI Catches More Hallucinations", "The DeBERTa-v3 cross-encoder boosted hallucination recall to 77.3% (and 84.7% with thresholding), serving as a stronger safety net."),
        ("4. Usability Penalty Must Be Measured", "Maximizing recall via strict thresholding created a 95.3% false-positive rate. Production systems must balance safety against false rejection rates.")
    ]

    for idx, (title, desc) in enumerate(takeaways):
        top = Inches(1.8 + idx * 1.3)
        add_card(slide14, Inches(1.0), top, Inches(11.333), Inches(1.15), bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))

        tb = slide14.shapes.add_textbox(Inches(1.3), top + Inches(0.12), Inches(10.7), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True

        p_t = tf.paragraphs[0]
        p_t.text = title
        p_t.font.size = Pt(15)
        p_t.font.bold = True
        p_t.font.color.rgb = PRIMARY_BLUE

        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(12)
        p_d.font.color.rgb = RGBColor(226, 232, 240)
        p_d.space_before = Pt(3)

    # ==============================================================================
    # SLIDE 15: Q&A / VIVA CHEAT SHEET
    # ==============================================================================
    slide15 = prs.slides.add_slide(blank_layout)
    add_bg(slide15, BG_LIGHT)
    add_header(slide15, "Thank You! Questions & Discussion", "PRESENTATION WRAP-UP & Q&A")

    viva_cards = [
        ("Why question-level split?", "Prevents identical question entities from appearing in train and test, stopping lexical memorization.", PRIMARY_BLUE),
        ("Why did TF-IDF beat NLI in acc?", "TF-IDF trained directly on 14k in-domain answers; NLI was zero-shot and penalized on short noun phrases.", ACCENT_PURPLE),
        ("What does tau = 0.95 show?", "Extreme recall (84.7%) causes an unbearable false-positive penalty (95.3%), rejecting 143/150 valid answers.", ACCENT_RED),
        ("Why bootstrap CIs?", "Quantifies error margin (±5.5% on 300 sample vs ±1.4% on 4k), ensuring claims of superiority are statistically sound.", ACCENT_GREEN)
    ]

    for idx, (q, a, color) in enumerate(viva_cards):
        col = idx % 2
        row = idx // 2
        left = Inches(0.8 + col * 5.95)
        top = Inches(1.5 + row * 2.7)
        add_card(slide15, left, top, Inches(5.8), Inches(2.45))

        tb = slide15.shapes.add_textbox(left + Inches(0.3), top + Inches(0.2), Inches(5.2), Inches(2.0))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = f"Q: {q}"
        p_t.font.size = Pt(16)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_d = tf.add_paragraph()
        p_d.text = f"A: {a}"
        p_d.font.size = Pt(13)
        p_d.font.color.rgb = TEXT_MAIN
        p_d.space_before = Pt(8)

    # Save PowerPoint deck in multiple locations
    output_paths = [
        "/Users/aditi/Downloads/Hallucination_Detection_Study_Presentation.pptx",
        "/Users/aditi/Desktop/Hallucination_Detection_Study_Presentation.pptx",
        "/Users/aditi/.gemini/antigravity/scratch/hallucination-detection-study/Hallucination_Detection_Study_Presentation.pptx"
    ]

    for path in output_paths:
        prs.save(path)
        print(f"Saved PPTX presentation to: {path}")

create_deck()
