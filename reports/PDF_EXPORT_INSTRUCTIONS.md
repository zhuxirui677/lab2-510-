# Export `LAB2_FULL_REPORT.md` to PDF

Generate or refresh the report first (from the project root):

```bash
./scripts/build_lab2_full_report.sh
# or, to append the full instructor manual after the cover:
./scripts/build_lab2_full_report.sh --include-lab-manual
```

**Word (.docx):** from the project root, run `./scripts/build_lab2_submission_docx.sh` (same optional `--include-lab-manual`). Install `python-docx` with `pip install -r requirements-docx.txt` first.

## Option A — VS Code / Cursor

1. Open `LAB2_FULL_REPORT.md` at the repository root.
2. Use a Markdown PDF extension (for example **Markdown PDF**) and run **Export (pdf)**.
3. Ensure images under `docs/screenshots/` exist if you uncommented image lines in the cover section.

## Option B — Pandoc (terminal)

Install [Pandoc](https://pandoc.org/) and a LaTeX engine if needed, then from the project root:

```bash
pandoc LAB2_FULL_REPORT.md -o LAB2_Submission_Report.pdf --pdf-engine=xelatex -V geometry:margin=1in
```

If you only need HTML first:

```bash
pandoc LAB2_FULL_REPORT.md -o LAB2_Submission_Report.html --standalone
```

Then print the HTML to PDF from your browser.
