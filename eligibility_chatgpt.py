"""GIX Career Event Eligibility Checker — ChatGPT-style single-file implementation (no .cursorrules)."""

from datetime import date

import streamlit as st

st.set_page_config(page_title="GIX Eligibility Checker", page_icon="🎓", layout="centered")

st.title("GIX Career Event Eligibility Checker")

RECOGNIZED_PROGRAMS = ["MSTI", "MDE", "MBA", "EMBA"]

QUARTER_MAP = {"Win": 1, "Spr": 4, "Sum": 7, "Aut": 10}

program = st.selectbox("Program", ["MSTI", "MDE", "MBA", "EMBA", "Other"])
graduation_quarter = st.text_input("Graduation Quarter (e.g. Spr 2025)")
cpt_status = st.radio("CPT Status", ["Active", "Inactive", "Not Applicable"])

if st.button("Check Eligibility"):
    if program == "Other":
        st.warning("Your situation may require advisor review. Contact GIX Career Services.")
    elif not graduation_quarter.strip():
        st.warning("Please enter a graduation quarter (for example: Spr 2026).")
    else:
        parts = graduation_quarter.split()
        if len(parts) != 2:
            st.error('Use the format "Spr 2026" (season abbreviation + year).')
        else:
            season, year_str = parts[0], parts[1]
            if season not in QUARTER_MAP:
                st.error(f"Unknown season: {season}. Use Win, Spr, Sum, or Aut.")
            else:
                try:
                    year = int(year_str)
                except ValueError:
                    st.error("Year must be a number (for example: Spr 2026).")
                else:
                    month = QUARTER_MAP[season]
                    grad_date = date(year, month, 1)
                    today = date.today()
                    months_away = (grad_date.year - today.year) * 12 + (grad_date.month - today.month)
                    within_4q = 0 <= months_away <= 12

                    results = [
                        {"Event": "Mock Interviews", "Eligible": "Yes", "Reason": "Open to recognized programs"},
                        {"Event": "Resume Reviews", "Eligible": "Yes", "Reason": "Open to recognized programs"},
                        {
                            "Event": "Employer Panels",
                            "Eligible": "Yes" if within_4q else "No",
                            "Reason": "Within 4 quarters of graduation" if within_4q else "Not within 4 quarters of graduation",
                        },
                        {"Event": "Networking Nights", "Eligible": "Yes", "Reason": "Open to all students"},
                        {
                            "Event": "CPT Info Sessions",
                            "Eligible": "Yes" if cpt_status == "Active" else "No",
                            "Reason": "Requires Active CPT" if cpt_status == "Active" else "CPT not active",
                        },
                    ]

                    st.table(results)
