"""
Builds a high-impact, professional, 10-slide PowerPoint presentation (.pptx)
for the Hallucination Detection study by Prachi Chauhan & Aditi Verma (Manipal University Jaipur).
Uses 16:9 widescreen layout, modern visual cards, tables, KPI callouts, and embedded speaker notes.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def build_10_slide_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    DARK_NAVY = RGBColor(15, 23, 42)       # #0F172A
    CARD_BG = RGBColor(255, 255, 255)      # #FFFFFF
    BG_LIGHT = RGBColor(248, 250, 252)     # #F8FAFC
    PRIMARY_BLUE = RGBColor(37, 99, 235)   # #2563EB
    TEXT_MAIN = RGBColor(15, 23, 42)       # #0F172A
    TEXT_MUTED = RGBColor(100, 116, 139)   # #64748B
    BORDER_COLOR = RGBColor(226, 232, 240) # #E2E8F0
    ACCENT_GREEN = RGBColor(16, 185, 129)  # #10B981
    ACCENT_RED = RGBColor(225, 29, 72)     # #E11D48
    ACCENT_AMBER = RGBColor(217, 119, 6)   # #D97706
    ACCENT_PURPLE = RGBColor(124, 58, 237) # #7C3AED

    def add_bg(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category_text="RESEARCH PROJECT PRESENTATION"):
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

    def set_notes(slide, notes_text):
        notes_slide = slide.notes_slide
        tf = notes_slide.notes_text_frame
        tf.text = notes_text

    # ==============================================================================
    # SLIDE 1: TITLE SLIDE (Dark Navy Theme)
    # ==============================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_bg(slide1, DARK_NAVY)

    bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(1.3), Inches(1.2), Inches(0.08))
    bar.fill.solid()
    bar.fill.fore_color.rgb = PRIMARY_BLUE
    bar.line.fill.background()

    tb_badge = slide1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.3), Inches(0.4))
    p_b = tb_badge.text_frame.paragraphs[0]
    p_b.text = "RESEARCH PROJECT PRESENTATION  •  AI & NLP"
    p_b.font.size = Pt(12)
    p_b.font.bold = True
    p_b.font.color.rgb = PRIMARY_BLUE

    tb_title = slide1.shapes.add_textbox(Inches(1.0), Inches(1.9), Inches(11.3), Inches(1.6))
    tf_t = tb_title.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Hallucination Detection in Large Language Models"
    p_t.font.size = Pt(36)
    p_t.font.bold = True
    p_t.font.color.rgb = RGBColor(255, 255, 255)

    tb_sub = slide1.shapes.add_textbox(Inches(1.0), Inches(3.4), Inches(11.3), Inches(0.8))
    tf_s = tb_sub.text_frame
    tf_s.word_wrap = True
    p_s = tf_s.paragraphs[0]
    p_s.text = "An Empirical Study Comparing Lexical Baselines vs. Deep NLI Cross-Encoders on HaluEval"
    p_s.font.size = Pt(18)
    p_s.font.color.rgb = RGBColor(203, 213, 225)

    add_card(slide1, Inches(1.0), Inches(4.5), Inches(11.333), Inches(2.0), bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))
    tb_auth = slide1.shapes.add_textbox(Inches(1.3), Inches(4.7), Inches(10.7), Inches(1.6))
    tf_a = tb_auth.text_frame
    tf_a.word_wrap = True

    p_a1 = tf_a.paragraphs[0]
    p_a1.text = "Project Team & Affiliation:"
    p_a1.font.size = Pt(13)
    p_a1.font.bold = True
    p_a1.font.color.rgb = PRIMARY_BLUE

    p_a2 = tf_a.add_paragraph()
    p_a2.text = "Prachi Chauhan & Aditi Verma"
    p_a2.font.size = Pt(17)
    p_a2.font.bold = True
    p_a2.font.color.rgb = RGBColor(255, 255, 255)

    p_a3 = tf_a.add_paragraph()
    p_a3.text = "Department of Computer Science and Engineering  |  Manipal University Jaipur"
    p_a3.font.size = Pt(13)
    p_a3.font.color.rgb = RGBColor(148, 163, 184)

    p_a4 = tf_a.add_paragraph()
    p_a4.text = "HaluEval QA Benchmark  •  Leakage-Resistant Split  •  TF-IDF vs. DeBERTa-v3 Cross-Encoder"
    p_a4.font.size = Pt(12)
    p_a4.font.color.rgb = RGBColor(203, 213, 225)

    set_notes(slide1, "Good morning respected teachers and panel members. Today, Prachi and I are presenting our research project on Hallucination Detection in Large Language Models. We evaluate two distinct approaches on the HaluEval QA benchmark using a scientifically rigorous, leakage-resistant split.")

    # ==============================================================================
    # SLIDE 2: THE PROBLEM (The Hallucination Dilemma)
    # ==============================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_bg(slide2, BG_LIGHT)
    add_header(slide2, "The Problem: Why AI Hallucinations Matter", "MOTIVATION & BACKGROUND")

    cards_data = [
        ("The Fluency Trap", ACCENT_AMBER, [
            "LLMs generate grammatically perfect, confident answers.",
            "Fluency creates a psychological illusion of factual truth.",
            "Standard models predict tokens by probability, not truth.",
            "Users cannot intuitively tell facts from plausible fiction."
        ]),
        ("High Real-World Stakes", ACCENT_RED, [
            "Healthcare: Making up drug interactions or wrong dosages.",
            "Legal Informatics: Fabricating non-existent case precedents.",
            "Finance & News: Misquoting revenues, dates, and names.",
            "Enterprise Search: Contradicting internal company PDFs."
        ]),
        ("The Detection Challenge", PRIMARY_BLUE, [
            "Detectors must spot fabrications without known answers at runtime.",
            "Word matching fails on paraphrases and synonyms.",
            "Deep models are computationally heavy and uncalibrated.",
            "The Trade-off: Catching errors vs. blocking correct answers."
        ])
    ]

    for idx, (title, color, bullets) in enumerate(cards_data):
        left = Inches(0.8 + idx * 3.95)
        add_card(slide2, left, Inches(1.5), Inches(3.8), Inches(5.3))
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

    set_notes(slide2, "Why does this matter? Large Language Models predict words based on statistics, not truth. They sound completely confident even when they make things up. In casual writing this is harmless, but in medicine, law, or business, hallucinations are dangerous. The real challenge is catching these errors automatically.")

    # ==============================================================================
    # SLIDE 3: OBJECTIVE & SETUP
    # ==============================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_bg(slide3, BG_LIGHT)
    add_header(slide3, "Project Objective & Grounded QA Formulation", "GOAL & SETUP")

    add_card(slide3, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_o = slide3.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_o = tb_o.text_frame
    tf_o.word_wrap = True

    p = tf_o.paragraphs[0]
    p.text = "The Goal: Building an AI Lie Detector"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    o_pts = [
        "Core Mission: Create an automated system that checks if an LLM-generated answer is genuinely supported by reference facts.",
        "Input Triplet: The detector receives three pieces of text:\n  1. Knowledge Passage (Ground truth reference text)\n  2. Question (The user query)\n  3. Candidate Answer (The LLM's generated response)",
        "Binary Output Decision:\n  • Label 0: Supported (Faithful to the facts)\n  • Label 1: Hallucination Risk (Unsupported or fake)"
    ]
    for pt in o_pts:
        p_b = tf_o.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(10)

    add_card(slide3, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_rq = slide3.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_rq = tb_rq.text_frame
    tf_rq.word_wrap = True

    p = tf_rq.paragraphs[0]
    p.text = "Our 3 Research Questions"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE

    rq_pts = [
        "RQ1 (Lexical Baseline): How well can a fast, statistical word-frequency model (TF-IDF) identify hallucinations without deep neural networks?",
        "RQ2 (Semantic Reasoning): Does a pretrained Natural Language Inference (NLI) cross-encoder perform better when given the same factual context?",
        "RQ3 (Operational Trade-off): What happens when we tune decision thresholds? Does requiring high confidence create unbearable false alarms?"
    ]
    for pt in rq_pts:
        p_b = tf_rq.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(12)

    set_notes(slide3, "Our objective was to build an automated lie detector for AI. Given a reference text, a question, and an answer, the model must flag whether the answer is supported or hallucinated. We framed three core research questions comparing simple statistical methods against deep language inference.")

    # ==============================================================================
    # SLIDE 4: TAXONOMY
    # ==============================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_bg(slide4, BG_LIGHT)
    add_header(slide4, "How Hallucinations Are Detected: 6 Methods", "LITERATURE TAXONOMY")

    tech_families = [
        ("1. Lexical Classifiers", "TF-IDF & n-gram frequencies paired with logistic regression. Fast and lightweight baseline (Our Model A).", PRIMARY_BLUE),
        ("2. Natural Language Inference", "Cross-encoders checking premise-hypothesis entailment. Directly measures evidence support (Our Model B).", ACCENT_PURPLE),
        ("3. External Retrieval", "Queries Google or vector databases to fetch verified documents before auditing generated claims.", ACCENT_GREEN),
        ("4. Consistency (SelfCheckGPT)", "Samples the LLM multiple times. If answers disagree wildly across runs, the model is likely hallucinating.", ACCENT_AMBER),
        ("5. Predictive Uncertainty", "Inspects token probabilities, logits, and entropy. Low internal confidence flags hallucinations.", ACCENT_RED),
        ("6. Atomic Claim Decomposition", "Splits complex paragraphs into single factual statements and verifies each claim independently.", PRIMARY_BLUE)
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

    set_notes(slide4, "In our literature review, we categorized detection techniques into six families. In our study, we specifically implemented Family 1—a lexical classifier—and Family 2—an NLI cross-encoder—to directly compare surface-level word matching against deep semantic reasoning.")

    # ==============================================================================
    # SLIDE 5: METHODOLOGY & LEAKAGE-RESISTANT SPLIT (Our Novelty)
    # ==============================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_bg(slide5, BG_LIGHT)
    add_header(slide5, "Our Scientific Safeguard: Leakage-Resistant Split", "METHODOLOGY & NOVELTY")

    add_card(slide5, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_b = slide5.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_b = tb_b.text_frame
    tf_b.word_wrap = True

    p = tf_b.paragraphs[0]
    p.text = "The Data Leakage Trap in HaluEval"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED

    b_pts = [
        "Benchmark: HaluEval Question-Answering (10,000 Wikipedia QA records).",
        "Paired Records: Each question has TWO answers:\n  • One supported correct answer (0)\n  • One ChatGPT hallucinated answer (1)",
        "The Common Mistake: Randomly splitting the 20,000 answers into train and test.",
        "Why It's Dangerous: The right answer for Question #42 ends up in Train, and the fake answer ends up in Test! The model just memorizes the topic entities instead of learning factual consistency."
    ]
    for pt in b_pts:
        p_b = tf_b.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    add_card(slide5, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_s = slide5.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True

    p = tf_s.paragraphs[0]
    p.text = "Our Solution: Question-Level Partitioning"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    s_pts = [
        "The Fix: Split by UNIQUE QUESTION IDs before expanding answer pairs.",
        "Guaranteed Disjointness: All answer variants of a question remain in the exact same partition.",
        "Our Partition Sizes:\n  • Train: 7,000 questions (14,000 answers)\n  • Validation: 1,000 questions (2,000 answers)\n  • Held-out Test: 2,000 questions (4,000 answers)",
        "Mathematical Proof: An automated assertion test in code verifies 0 overlapping question IDs across partitions!"
    ]
    for pt in s_pts:
        p_b = tf_s.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    set_notes(slide5, "This slide represents a key scientific contribution of our work: preventing data leakage. In HaluEval, each question has both a right and a fake answer. If you split randomly, answers from the same question cross between train and test, causing the model to cheat by memorizing topics. We split unique questions first, guaranteeing zero data leakage.")

    # ==============================================================================
    # SLIDE 6: THE TWO COMPETING MODELS
    # ==============================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_bg(slide6, BG_LIGHT)
    add_header(slide6, "The Two Models: Lexical vs. Semantic Logic", "MODEL ARCHITECTURES")

    add_card(slide6, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_m1 = slide6.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_m1 = tb_m1.text_frame
    tf_m1.word_wrap = True

    p = tf_m1.paragraphs[0]
    p.text = "Model A: TF-IDF + Logistic Regression"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    m1_pts = [
        "Nature: Fast statistical machine learning baseline.",
        "Features: Unigrams + Bigrams (ngram_range=(1, 2)) to capture compound entities.",
        "Vocabulary Cap: 50,000 max features.",
        "Sublinear TF: Applies 1 + log(tf) so frequent words don't overpower the model.",
        "Classifier: Logistic Regression with balanced class weights and max_iter=1000.",
        "Advantage: Inexpensive, trains in seconds, runs on CPU."
    ]
    for pt in m1_pts:
        p_b = tf_m1.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    add_card(slide6, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_m2 = slide6.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_m2 = tb_m2.text_frame
    tf_m2.word_wrap = True

    p = tf_m2.paragraphs[0]
    p.text = "Model B: DeBERTa-v3 NLI Cross-Encoder"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_PURPLE

    m2_pts = [
        "Nature: Pretrained deep transformer (cross-encoder/nli-deberta-v3-small).",
        "Premise: Factual Knowledge passage.",
        "Hypothesis: Candidate Answer alone (isolates the factual claim from question phrasing).",
        "Full Cross-Attention: Compares all premise and hypothesis tokens simultaneously.",
        "Logits: Contradiction (0), Entailment (1), Neutral (2).",
        "Rule 1 (Argmax): Entailment → 0 (Supported); Contradiction & Neutral → 1 (Hallucination Risk)."
    ]
    for pt in m2_pts:
        p_b = tf_m2.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    set_notes(slide6, "Here are the two models we built. Model A is TF-IDF with 50,000 features and Logistic Regression—lightweight, fast, and simple. Model B is a DeBERTa-v3 cross-encoder that evaluates logical entailment between the reference passage and the candidate answer.")

    # ==============================================================================
    # SLIDE 7: RESULTS (Head-to-Head Comparison)
    # ==============================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_bg(slide7, BG_LIGHT)
    add_header(slide7, "Head-to-Head Results on 300 Comparison Examples", "EMPIRICAL FINDINGS (TABLE I)")

    table_shape = slide7.shapes.add_table(5, 4, Inches(0.8), Inches(1.5), Inches(11.7), Inches(2.6))
    table = table_shape.table

    table.columns[0].width = Inches(3.0)
    table.columns[1].width = Inches(2.7)
    table.columns[2].width = Inches(2.7)
    table.columns[3].width = Inches(3.3)

    table_data = [
        ["Evaluation Metric", "TF-IDF Baseline", "NLI Detector (Argmax)", "Winner & Practical Meaning"],
        ["Accuracy", "69.33%", "45.33%", "TF-IDF achieves higher overall score"],
        ["Precision (Hallucinations)", "75.89%", "47.15%", "TF-IDF has far fewer false alarms"],
        ["Recall (Safety Catch)", "56.67%", "77.33% (+20.7%)", "NLI catches 20% more hallucinations!"],
        ["F1-Score", "64.89%", "58.59%", "TF-IDF maintains better overall balance"]
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

    add_card(slide7, Inches(0.8), Inches(4.4), Inches(11.7), Inches(2.4))
    tb_exp = slide7.shapes.add_textbox(Inches(1.1), Inches(4.55), Inches(11.1), Inches(2.1))
    tf_e = tb_exp.text_frame
    tf_e.word_wrap = True

    p = tf_e.paragraphs[0]
    p.text = "Why Did TF-IDF Get Higher Accuracy Than Deep NLI? (The Paradox Explained)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    e_pts = [
        "Dataset Artifacts: TF-IDF was trained directly on 14,000 HaluEval QA examples, picking up ChatGPT's stylistic perturbation patterns.",
        "Zero-Shot Evaluation: DeBERTa was used off-the-shelf without fine-tuning on HaluEval QA.",
        "Elliptical Short Answers: Many correct answers in HaluEval are concise noun phrases (e.g. 'Arthur's Magazine'). Because they lack a full verb sentence, DeBERTa gave them NEUTRAL scores.",
        "Conservative Penalty: Our rule maps Neutral to Hallucination Risk, dropping accuracy while boosting safety recall."
    ]
    for pt in e_pts:
        p_b = tf_e.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(12)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(4)

    set_notes(slide7, "Here are our head-to-head results on the 300 test sample. At first glance, TF-IDF won on accuracy with 69% versus 45%. But look at recall: NLI achieved 77% versus 56%. That means NLI caught 20% more hallucinations! TF-IDF got higher accuracy because it learned ChatGPT vocabulary patterns, while NLI was penalized on short noun phrases.")

    # ==============================================================================
    # SLIDE 8: THRESHOLD DILEMMA (Safety vs Usability)
    # ==============================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_bg(slide8, BG_LIGHT)
    add_header(slide8, "The Threshold Dilemma: Safety vs. Usability", "THRESHOLD EXPERIMENT (SECTION V-C)")

    add_card(slide8, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_th1 = slide8.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_th1 = tb_th1.text_frame
    tf_th1.word_wrap = True

    p = tf_th1.paragraphs[0]
    p.text = "Rule 2 Strategy: Requiring High Confidence"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_BLUE

    th1_pts = [
        "Rule 2 Logic: Mark answer as Supported ONLY IF P(entailment) >= tau; otherwise flag as Hallucination Risk.",
        "Validation Sweep: Evaluated tau in [0.50, 0.95] with step 0.05 on 2,000 validation answers.",
        "Optimal Threshold: tau* = 0.95 maximized validation F1 (59.61%).",
        "Diagnostic Test on 300 Sample at tau = 0.95:\n  • Hallucination Recall: 84.67% (Catches 127 of 150 fake answers!)\n  • Precision: 47.04% | F1-Score: 60.48%"
    ]
    for pt in th1_pts:
        p_b = tf_th1.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    add_card(slide8, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_th2 = slide8.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_th2 = tb_th2.text_frame
    tf_th2.word_wrap = True

    p = tf_th2.paragraphs[0]
    p.text = "The Usability Penalty (Confusion Matrix)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_RED

    th2_pts = [
        "The Catastrophic Cost: False Positive Rate = 95.33%!",
        "Audit of 150 Supported Answers:\n  • Accepted as Supported (TN): ONLY 7 answers!\n  • Falsely Rejected as Fake (FP): 143 out of 150 answers!",
        "Audit of 150 Hallucinated Answers:\n  • Correctly Caught (TP): 127 answers\n  • Missed (FN): 23 answers",
        "Core Finding: Pushing recall to 85% turns the model into a 'brick wall'—it stops false info only by rejecting almost all valid outputs!"
    ]
    for pt in th2_pts:
        p_b = tf_th2.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    set_notes(slide8, "What happens when you demand 95% confidence before trusting an answer? Hallucination recall jumps to 85%, which sounds great. But look at the false positive rate: 95.3%! Out of 150 correct answers, it rejected 143 of them. It acts like a brick wall that blocks almost all real information.")

    # ==============================================================================
    # SLIDE 9: STATISTICAL RIGOR & LIMITATIONS
    # ==============================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_bg(slide9, BG_LIGHT)
    add_header(slide9, "Statistical Rigor & Study Limitations", "UNCERTAINTY & CONSTRAINTS")

    add_card(slide9, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_st = slide9.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_st = tb_st.text_frame
    tf_st.word_wrap = True

    p = tf_st.paragraphs[0]
    p.text = "Bootstrap 95% Confidence Intervals"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GREEN

    st_pts = [
        "Method: B = 2,000 bootstrap resampling iterations to calculate true empirical percentile bounds.",
        "TF-IDF (4,000 test set): 70.57% [69.15%, 72.00%] (Margin: ±1.42%)",
        "TF-IDF (300 sample): 69.33% [64.00%, 74.33%] (Margin: ±5.17%)",
        "NLI Argmax (300 sample): 45.33% [39.67%, 51.00%] (Margin: ±5.67%)",
        "Why It Matters: On 300 samples, the error margin is ±5.7%. Reporting confidence intervals prevents claiming superiority over random sampling noise!"
    ]
    for pt in st_pts:
        p_b = tf_st.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(8)

    add_card(slide9, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3))
    tb_lm = slide9.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.1), Inches(4.7))
    tf_lm = tb_lm.text_frame
    tf_lm.word_wrap = True

    p = tf_lm.paragraphs[0]
    p.text = "3 Critical Study Limitations"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_AMBER

    lm_pts = [
        "1. Evaluation Sample Size (300): Head-to-head NLI comparison was restricted to 300 answers due to interactive Colab compute constraints.",
        "2. Synthetic Benchmark Domain: HaluEval was generated using ChatGPT perturbations on Wikipedia; results may not fully generalize to open dialogue or coding.",
        "3. Elliptical QA Answers: Short entity answers (e.g. 'Arthur's Magazine') lack full sentence grammar, causing NLI models to predict neutral rather than entailment."
    ]
    for pt in lm_pts:
        p_b = tf_lm.add_paragraph()
        p_b.text = f"•  {pt}"
        p_b.font.size = Pt(13)
        p_b.font.color.rgb = TEXT_MAIN
        p_b.space_before = Pt(10)

    set_notes(slide9, "We computed 95% bootstrap confidence intervals over 2,000 iterations. On 300 samples, the margin of error is plus-or-minus 5.7%. This statistical rigor proves that small differences can be random noise. We also candidly acknowledge our limitations: synthetic benchmark text and small comparison sample.")

    # ==============================================================================
    # SLIDE 10: CONCLUSION & VIVA DEFENSE CHEAT SHEET (Dark Theme)
    # ==============================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_bg(slide10, DARK_NAVY)

    tb_c_title = slide10.shapes.add_textbox(Inches(1.0), Inches(0.6), Inches(11.3), Inches(0.8))
    tf_ct = tb_c_title.text_frame
    p = tf_ct.paragraphs[0]
    p.text = "Conclusion & Viva Defense Cheat Sheet"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)

    viva_cards = [
        ("Key Conclusion 1: Leakage Prevention", "Splitting by question IDs before answer creation is mandatory to stop models from memorizing topic words.", PRIMARY_BLUE),
        ("Key Conclusion 2: The Safety Paradox", "TF-IDF had higher accuracy (~70%), but NLI was much safer (+20% recall). Fast models miss subtle falsehoods.", ACCENT_PURPLE),
        ("Viva Q: Why did tau = 0.95 fail?", "Requiring 95% confidence caught 85% of hallucinations, but created a 95% false alarm rate, rejecting 143/150 valid answers.", ACCENT_RED),
        ("Viva Q: How to fix this in production?", "Use hybrid pipelines: break answers into atomic claims, fetch live retrieval evidence, and route borderline cases to humans.", ACCENT_GREEN)
    ]

    for idx, (q, a, color) in enumerate(viva_cards):
        col = idx % 2
        row = idx // 2
        left = Inches(1.0 + col * 5.8)
        top = Inches(1.6 + row * 2.6)
        add_card(slide10, left, top, Inches(5.5), Inches(2.35), bg_color=RGBColor(30, 41, 59), border_color=RGBColor(51, 65, 85))

        tb = slide10.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), Inches(5.0), Inches(1.95))
        tf = tb.text_frame
        tf.word_wrap = True
        p_t = tf.paragraphs[0]
        p_t.text = q
        p_t.font.size = Pt(16)
        p_t.font.bold = True
        p_t.font.color.rgb = color

        p_d = tf.add_paragraph()
        p_d.text = a
        p_d.font.size = Pt(13)
        p_d.font.color.rgb = RGBColor(226, 232, 240)
        p_d.space_before = Pt(8)

    set_notes(slide10, "In conclusion: Hallucination detection is an engineering trade-off problem, not just picking the biggest model. Question-level splitting is essential. Fast models are accurate but miss hallucinations, while deep models catch errors but trigger false alarms. Thank you, and we are ready for your questions!")

    # Save to standard locations
    output_paths = [
        "/Users/aditi/Downloads/Hallucination_Detection_10_Slides.pptx",
        "/Users/aditi/Desktop/Hallucination_Detection_10_Slides.pptx",
        "/Users/aditi/.gemini/antigravity/scratch/hallucination-detection-study/Hallucination_Detection_10_Slides.pptx"
    ]

    for path in output_paths:
        prs.save(path)
        print(f"Saved 10-slide PowerPoint presentation to: {path}")

build_10_slide_presentation()
