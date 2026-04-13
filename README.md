# TECHIN 510 — Lab 2: Anatomy of Coding Agents

GitHub: https://github.com/GIX-Luyao/lab-2-zhuxirui677

This repository contains the Week 2 Streamlit lab work: an enhanced **Tip Calculator**, AI configuration files (`.cursorrules`, `CLAUDE.md`), written lab deliverables (Components A–E), and two implementations of the **GIX Career Event Eligibility Checker** (Component E).

---

## Prerequisites

- Python **3.11+**
- A virtual environment (recommended)
- Git

Optional (for Claude Code, if you reproduce Level 1 outside Cursor):

- Node.js **v20+**
- An Anthropic API key (never commit keys to the repository)

---

## Install

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Optional — only if you will build the Word submission bundle:
pip install -r requirements-docx.txt
```

On Windows, activate with `.venv\Scripts\activate`.

---

## Run the applications

### 1) Tip Calculator (main Week 1/2 app)

```bash
streamlit run app.py
```

**Smoke test (happy path):** enter a positive bill amount, pick a tip option, set number of people ≥ 1 — metrics, receipt, and Plotly chart should update.

**Smoke test (invalid input):** enter a negative bill amount — the app should show `st.error()` and stop without crashing.

### 2) Eligibility Checker — Cursor-style (`eligibility_cursor.py`)

```bash
streamlit run eligibility_cursor.py
```

**Smoke test (happy path):** choose a recognized program (not **Other**), enter a quarter like `Spr 2026`, pick CPT status — a styled dataframe of five events should appear.

**Smoke test (invalid / edge):** choose **Other** — you should see a warning and no results table; enter an unparsable quarter with a recognized program — warning and no table.

### 3) Eligibility Checker — ChatGPT-style (`eligibility_chatgpt.py`)

```bash
streamlit run eligibility_chatgpt.py
```

**Smoke test (happy path):** fill inputs, click **Check Eligibility** — static `st.table()` results.

**Smoke test (invalid):** leave the quarter blank and click **Check Eligibility** — warning, no crash; choose **Other** — warning, no table.

---

## Reproduce written deliverables & PDF

| Artifact | File |
|----------|------|
| Single bundled report (export to PDF for Canvas) | `LAB2_FULL_REPORT.md` (run `./scripts/build_lab2_full_report.sh`) |
| **Word bundle (all written deliverables in one .docx)** | `LAB2_Submission.docx` (run `./scripts/build_lab2_submission_docx.sh`) |
| Instructor lab manual (English; optional in PDF/DOCX) | `lab-manual.md` (excluded by default; pass `--include-lab-manual` to both build scripts) |
| PDF export options | `reports/PDF_EXPORT_INSTRUCTIONS.md` |
| Component A | `component_a_interview.md` |
| Component B (includes AI + prompt log) | `component_b_lab.md` |
| Component C | `component_c_architecture.md` |
| Component D | `component_d_testing.md` |
| Component E | `component_e_challenge.md` |
| Reflection (3–5 sentences) | `reflection.md` |
| Cursor rules | `.cursorrules` |
| Claude Code context | `CLAUDE.md` |

### Build `LAB2_FULL_REPORT.md` (concatenates all sections)

From the repository root:

```bash
# Default: cover + Components A–E + reflection + this README (does NOT embed lab-manual.md)
./scripts/build_lab2_full_report.sh

# Optional: also embed the full instructor lab manual (English) after the cover
./scripts/build_lab2_full_report.sh --include-lab-manual

./scripts/build_lab2_full_report.sh --help
```

The script is the source of truth; it writes `LAB2_FULL_REPORT.md` in one step.

Then add screenshots under `docs/screenshots/` and uncomment the image lines in `reports/SUBMISSION_COVER.md`, re-run the build script, and export to PDF per `reports/PDF_EXPORT_INSTRUCTIONS.md`.

### Build `LAB2_Submission.docx` (Word — same content as the Markdown bundle)

This regenerates `LAB2_FULL_REPORT.md` and converts it to **`LAB2_Submission.docx`** at the repository root (cover, Components A–E, reflection, and this README as appendix). Optional flags match the Markdown builder.

```bash
# Default bundle (no embedded lab-manual.md)
./scripts/build_lab2_submission_docx.sh

# Optional: include the full instructor lab manual after the cover
./scripts/build_lab2_submission_docx.sh --include-lab-manual
```

**Dependencies:** `pip install -r requirements-docx.txt` (adds `python-docx`). If [Pandoc](https://pandoc.org/) is installed, the converter uses it automatically for higher fidelity; otherwise it uses `python-docx` with a lightweight Markdown parser (headings, lists, tables, code blocks).

---

## Project structure

- `app.py` — Tip Calculator UI (calls `utils.py`)
- `utils.py` — Calculations, receipt formatting, Plotly chart builder, `compute_stats`
- `eligibility_cursor.py` — Component E implementation (structured, typed, with `st.set_page_config`)
- `eligibility_chatgpt.py` — Component E comparison implementation (flat script style)
- `data/` — Reserved for CSV/JSON if you extend the project
- `docs/screenshots/` — Place PNG screenshots here for the PDF/DOCX report
- `scripts/md_to_docx.py` — Markdown → DOCX helper used by `build_lab2_submission_docx.sh`

---

## Course notes

- This is a **TECHIN 510** project at **UW GIX**.
- Do **not** commit API keys, tokens, or secrets.
