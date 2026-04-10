# Project Context

## What This Project Is

A Streamlit web app called "Tip Calculator" — a course project for TECHIN 510 at UW GIX. It calculates tip amounts, bill totals, and per-person splits for restaurant bills, and displays a formatted receipt summary and a Plotly payment breakdown chart.

## Target Users

Students and diners who want a quick, formatted receipt breakdown for splitting a restaurant bill. The audience is non-technical — error messages must be friendly and clear.

## Tech Stack

- Python 3.11+
- Streamlit for the web interface
- Plotly for interactive charts
- Pandas for data tables (used in the eligibility checker)
- No numpy, no matplotlib

## Project Structure

- `app.py` — Main Streamlit application (UI only)
- `utils.py` — Utility functions: compute_tip, format_receipt, build_breakdown_chart, compute_stats
- `eligibility_cursor.py` — GIX Career Event Eligibility Checker (Component E, Cursor version)
- `eligibility_chatgpt.py` — GIX Career Event Eligibility Checker (Component E, ChatGPT version)
- `.cursorrules` — Cursor AI configuration
- `requirements.txt` — Python dependencies

## Development Commands

- Run the tip calculator: `streamlit run app.py`
- Run the eligibility checker: `streamlit run eligibility_cursor.py`
- Install dependencies: `pip install -r requirements.txt`
- Activate virtual environment: `source .venv/bin/activate`

## Coding Standards

- Follow PEP 8 style guidelines
- Use type hints on all function signatures
- Write Google-style docstrings for all functions (Args, Returns, Raises)
- Handle errors gracefully — never let the app crash on user input
- Use st.error() + st.stop() for unrecoverable input errors
- Never hardcode sensitive data (API keys, passwords)

## Important Notes

- This is a course project for TECHIN 510 at UW GIX
- When making changes, always verify the app still runs: `streamlit run app.py`
- All chart code uses Plotly — do not introduce Matplotlib
- The color palette is: ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
