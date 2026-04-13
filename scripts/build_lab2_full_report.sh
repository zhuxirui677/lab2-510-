#!/usr/bin/env bash
# Build LAB2_FULL_REPORT.md at the repository root.
#
# Usage:
#   ./scripts/build_lab2_full_report.sh
#       Default: student submission bundle (cover + Components A–E + reflection + README appendix).
#       Does NOT include lab-manual.md (long instructor text; keeps PDF focused on your work).
#
#   ./scripts/build_lab2_full_report.sh --include-lab-manual
#       Same as default, but inserts the full English lab-manual.md immediately after the cover
#       under the heading "Course Lab Manual (reference)".
#
#   ./scripts/build_lab2_full_report.sh --help
#       Show this help.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

INCLUDE_LAB_MANUAL=0

for arg in "$@"; do
  case "$arg" in
    --include-lab-manual)
      INCLUDE_LAB_MANUAL=1
      ;;
    -h|--help)
      cat <<'HELP'
Usage: ./scripts/build_lab2_full_report.sh [--include-lab-manual]

  (no flags)              Build LAB2_FULL_REPORT.md from cover + Components A–E +
                          reflection + README appendix. Does NOT embed lab-manual.md.

  --include-lab-manual    Also insert lab-manual.md (full English instructor manual)
                          right after the cover, under "Course Lab Manual (reference)".

  -h, --help              Show this message.
HELP
      exit 0
      ;;
    *)
      echo "Unknown option: $arg" >&2
      echo "Use: $0 [--include-lab-manual] | --help" >&2
      exit 2
      ;;
  esac
done

{
  cat reports/SUBMISSION_COVER.md

  if [[ "$INCLUDE_LAB_MANUAL" -eq 1 ]]; then
    printf '\n---\n\n## Course Lab Manual (reference)\n\n'
    printf '_The following section is the full Week 2 instructor lab manual (`lab-manual.md`)._\n\n'
    cat lab-manual.md
    printf '\n---\n\n'
  fi

  cat component_a_interview.md
  cat component_b_lab.md
  cat component_c_architecture.md
  cat component_d_testing.md
  cat component_e_challenge.md
  printf '\n---\n\n'
  cat reflection.md
  printf '\n---\n\n## Appendix — Run & Reproduce\n\n'
  cat README.md
} > LAB2_FULL_REPORT.md

if [[ "$INCLUDE_LAB_MANUAL" -eq 1 ]]; then
  echo "Wrote LAB2_FULL_REPORT.md (with lab-manual.md included after cover)."
else
  echo "Wrote LAB2_FULL_REPORT.md (lab-manual.md excluded; use --include-lab-manual to add it)."
fi
