#!/usr/bin/env bash
# Build LAB2_Submission.docx from the same Markdown sources as the PDF bundle.
# Passes optional flags through to build_lab2_full_report.sh (e.g. --include-lab-manual).

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

"$ROOT/scripts/build_lab2_full_report.sh" "$@"

PYTHON="$ROOT/.venv/bin/python"
if [[ ! -x "$PYTHON" ]]; then
  PYTHON="python3"
fi

if ! "$PYTHON" "$ROOT/scripts/md_to_docx.py" --input "$ROOT/LAB2_FULL_REPORT.md" --output "$ROOT/LAB2_Submission.docx"; then
  echo "DOCX build failed. Create a venv and install docx deps, for example:" >&2
  echo "  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt -r requirements-docx.txt" >&2
  exit 1
fi

echo "Wrote $ROOT/LAB2_Submission.docx"
