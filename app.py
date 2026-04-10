"""Tip Calculator — TECHIN 510 Week 1/2 Streamlit App."""

import streamlit as st
from datetime import date

import utils

st.set_page_config(page_title="Tip Calculator", page_icon="🧾", layout="centered")

# ── Session state initialization ──────────────────────────────────────────────
if "bill_amount" not in st.session_state:
    st.session_state["bill_amount"] = 0.0
if "tip_rate" not in st.session_state:
    st.session_state["tip_rate"] = 0.18
if "num_people" not in st.session_state:
    st.session_state["num_people"] = 1

# ── Title ─────────────────────────────────────────────────────────────────────
st.title("Tip Calculator")
st.caption("Split the bill, stress-free.")

# ── Results (above the fold) ──────────────────────────────────────────────────
bill = st.session_state["bill_amount"]
rate = st.session_state["tip_rate"]
people = st.session_state["num_people"]

tip_amount, total, per_person = utils.compute_tip(bill, rate, people)

col1, col2, col3 = st.columns(3)
col1.metric("Tip Amount", f"${tip_amount:.2f}")
col2.metric("Total", f"${total:.2f}")
col3.metric("Per Person", f"${per_person:.2f}")

st.divider()

# ── Inputs ────────────────────────────────────────────────────────────────────
st.subheader("Bill Details")

bill_input = st.number_input(
    "Bill Amount ($)",
    min_value=0.0,
    step=0.01,
    format="%.2f",
    value=st.session_state["bill_amount"],
)

if bill_input < 0:
    st.error("Bill amount cannot be negative. Please enter a positive value.")
    st.stop()

st.session_state["bill_amount"] = bill_input

TIP_RATE_MAP = {
    "10%": 0.10,
    "15%": 0.15,
    "18%": 0.18,
    "20%": 0.20,
    "Custom": None,
}

tip_option = st.selectbox("Tip Percentage", list(TIP_RATE_MAP.keys()), index=2)

if tip_option == "Custom":
    custom_pct = st.slider("Custom tip (%)", min_value=0, max_value=50, value=18)
    st.session_state["tip_rate"] = custom_pct / 100
else:
    st.session_state["tip_rate"] = TIP_RATE_MAP[tip_option]

num_people = st.number_input(
    "Number of People",
    min_value=1,
    max_value=50,
    step=1,
    value=st.session_state["num_people"],
)
st.session_state["num_people"] = num_people

st.divider()

# ── Receipt Summary ───────────────────────────────────────────────────────────
st.subheader("Receipt Summary")

receipt_text = utils.format_receipt(
    bill_amount=st.session_state["bill_amount"],
    tip_rate=st.session_state["tip_rate"],
    tip_amount=tip_amount,
    total=total,
    per_person=per_person,
    num_people=st.session_state["num_people"],
    today=date.today(),
)

st.code(receipt_text, language=None)

st.divider()

# ── Payment Breakdown Chart ───────────────────────────────────────────────────
st.subheader("Payment Breakdown")

if st.session_state["bill_amount"] == 0:
    st.info("Enter a bill amount to see the chart.")
else:
    fig = utils.build_breakdown_chart(
        bill_amount=st.session_state["bill_amount"],
        tip_amount=tip_amount,
        per_person=per_person,
    )
    st.plotly_chart(fig, use_container_width=True)
