"""
models/project.py
Model layer — plain data objects describing each project.
No persistence layer is needed for a static showcase, so project
data lives here as in-memory Python objects, following the same
role a database model would play in a larger MVC app.
"""


class Project:
    def __init__(self, slug, name, tagline, status, stack, summary,
                 highlights, stats, limitations, timeline, accent,
                 screenshots=None):
        self.slug = slug
        self.name = name
        self.tagline = tagline
        self.status = status
        self.stack = stack
        self.summary = summary
        self.highlights = highlights
        self.stats = stats
        self.limitations = limitations
        self.timeline = timeline
        self.accent = accent  # "amber" or "cyan" — maps to a CSS accent class
        self.screenshots = screenshots or []  # list of {"file": ..., "caption": ...}


PROJECTS = {
    "wedgetail": Project(
        slug="wedgetail",
        name="WedgeTail",
        tagline="Malware lineage & evolutionary intelligence",
        status="Alpha 0.1.3 — active research",
        stack=["Python", "PyTorch", "LSTM", "PE Analysis", "Semantic Embeddings"],
        summary=(
            "WedgeTail investigates how malware strains evolve — treating "
            "malicious binaries the way a biologist treats a species tree. "
            "Instead of asking \u201cwhat family is this?\u201d in isolation, it "
            "asks \u201cwhat did this evolve from, and what is it becoming?\u201d "
            "by analysing opcode sequences, API call behaviour, PE metadata, "
            "and embedded strings, then computing semantic similarity across "
            "a corpus of samples to reconstruct inheritance graphs."
        ),
        highlights=[
            {
                "title": "Lineage graphs, not just labels",
                "body": (
                    "Directed graph edges represent code inheritance between "
                    "samples, ordered by timestamp, so the system can surface "
                    "which strains borrowed from which — not just a family name."
                ),
            },
            {
                "title": "Behavioural fingerprinting",
                "body": (
                    "Uses opcode + API call embeddings rather than binary-to-image "
                    "visualisation, because behavioural signal stays stable across "
                    "packed and re-obfuscated variants where pixel patterns don't."
                ),
            },
            {
                "title": "Trend forecasting",
                "body": (
                    "An LSTM tracks weekly prevalence of specific capabilities "
                    "(evasion techniques, API patterns) across families to project "
                    "which behaviours are gaining adoption."
                ),
            },
            {
                "title": "Honest about static analysis limits",
                "body": (
                    "Packed, encrypted, or installer-wrapped payloads (e.g. NSIS "
                    "installers) are explicitly flagged rather than silently "
                    "misclassified — the system reports low confidence instead "
                    "of guessing."
                ),
            },
        ],
        stats=[
            {"value": "2,026", "label": "training samples"},
            {"value": "20", "label": "malware families"},
            {"value": "~70%", "label": "test accuracy"},
            {"value": "17/17", "label": "ancestor-matching, demo corpus"},
        ],
        limitations=[
            "Static analysis can't see inside packed or encrypted payloads — "
            "flagged explicitly rather than hidden.",
            "Trend Forecast module is architecturally complete but validated "
            "only on synthetic data so far; no live feed yet.",
            "Lineage Tree currently runs on a fixed demo corpus and doesn't "
            "yet grow from new uploads.",
        ],
        timeline=[
            "Built a real trained classifier across 20 malware families, "
            "replacing an early prototype's fictional label set.",
            "Diagnosed and fixed a chain of feature-extraction bugs: API "
            "suffix mismatches silently dropping ~1/3 of tracked calls, "
            "unnormalised entropy values dominating similarity scores, and "
            "ordinal imports being silently discarded.",
            "Added installer-wrapper detection after discovering a "
            "persistently-misclassified sample was actually an NSIS-wrapped "
            "payload, not a raw binary.",
            "Currently retraining and validating ahead of a Young ICT "
            "Explorers presentation.",
        ],
        accent="amber",
        screenshots=[
            {
                "file": "wedgetail/lineage-tree.png",
                "caption": "Lineage Tree — phylogenetic graph of code-reuse relationships across the demo corpus.",
            },
            {
                "file": "wedgetail/trend-forecast.png",
                "caption": "Trend Forecast — LSTM-driven capability momentum, current vs. predicted next-week prevalence.",
            },
            {
                "file": "wedgetail/analyse-sample.png",
                "caption": "Analyse Sample — live classification of a real AgentTesla sample with ancestor matches.",
            },
            {
                "file": "wedgetail/corpus.png",
                "caption": "Corpus — overview of the current sample set by family and threat actor.",
            },
        ],
    ),
    "lungvision": Project(
        slug="lungvision",
        name="LungVision",
        tagline="Chest X-ray triage across six respiratory conditions",
        status="Archived — no longer active",
        stack=["Python", "fastai", "PyTorch", "ResNet-152", "Jupyter"],
        summary=(
            "LungVision is a computer vision model trained to classify chest "
            "X-rays across six categories \u2014 healthy, viral pneumonia, "
            "bacterial pneumonia, lung cancer, tuberculosis, and chronic "
            "obstructive pulmonary disease (COPD). Built with fastai on top "
            "of a ResNet-152 backbone, the project explores how far transfer "
            "learning can go on a modest, self-curated image dataset for a "
            "diagnostic support task."
        ),
        highlights=[
            {
                "title": "Six-way classification",
                "body": (
                    "Distinguishes between healthy scans and five distinct "
                    "respiratory conditions, rather than a simpler binary "
                    "healthy/unhealthy split."
                ),
            },
            {
                "title": "Transfer learning on ResNet-152",
                "body": (
                    "Fine-tunes a deep, pretrained convolutional backbone "
                    "on the curated chest X-ray dataset using fastai's "
                    "vision_learner pipeline."
                ),
            },
            {
                "title": "Dataset curation pipeline",
                "body": (
                    "Sources and validates images per class, removes "
                    "corrupted files, and uses fastai's classifier cleaner "
                    "workflow to catch mislabelled samples before training."
                ),
            },
            {
                "title": "Confusion-matrix driven iteration",
                "body": (
                    "Uses classification interpretation tools \u2014 confusion "
                    "matrices and top-loss inspection \u2014 to identify which "
                    "conditions the model confuses and where the dataset "
                    "needs more examples."
                ),
            },
        ],
        stats=[
            {"value": "6", "label": "diagnostic classes"},
            {"value": "ResNet-152", "label": "backbone"},
            {"value": "128px", "label": "input resolution"},
            {"value": "fastai", "label": "training framework"},
        ],
        limitations=[
            "Trained on a self-curated, modest-sized dataset — not a "
            "clinical-grade, hospital-scale corpus.",
            "A research prototype for exploring the approach, not a "
            "validated diagnostic tool.",
            "Image sourcing pipeline relies on web image search, so label "
            "noise is mitigated by manual cleaning rather than eliminated.",
        ],
        timeline=[
            "Defined six target classes and sourced candidate images per "
            "class via automated image search.",
            "Built a verification pass to strip corrupted or unreadable "
            "images before training.",
            "Trained a ResNet-152 vision learner with fastai, fine-tuning "
            "over multiple epochs.",
            "Used confusion-matrix and top-loss analysis plus an interactive "
            "classifier cleaner to refine the dataset.",
            "Exported the trained model for inference on new scans.",
        ],
        accent="cyan",
    ),
}


def get_all_projects():
    return list(PROJECTS.values())


def get_project(slug):
    return PROJECTS.get(slug)
