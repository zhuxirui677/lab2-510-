"""Utility functions for the Tip Calculator Streamlit app."""

import statistics
from datetime import date

import plotly.express as px
import plotly.graph_objects as go


def compute_tip(
    bill_amount: float,
    tip_rate: float,
    num_people: int,
) -> tuple[float, float, float]:
    """Compute tip amount, total, and per-person share.

    Args:
        bill_amount: Pre-tip bill total in USD.
        tip_rate: Tip as a decimal fraction (e.g., 0.18 for 18%).
        num_people: Number of people splitting the bill.

    Returns:
        A tuple of (tip_amount, total, per_person), all in USD.

    Raises:
        ValueError: If num_people is less than 1.
    """
    if num_people < 1:
        raise ValueError(f"num_people must be at least 1, got {num_people}")
    tip_amount = round(bill_amount * tip_rate, 2)
    total = round(bill_amount + tip_amount, 2)
    per_person = round(total / num_people, 2)
    return tip_amount, total, per_person


def format_receipt(
    bill_amount: float,
    tip_rate: float,
    tip_amount: float,
    total: float,
    per_person: float,
    num_people: int,
    today: date,
) -> str:
    """Format a printed-receipt-style summary string.

    Args:
        bill_amount: Pre-tip bill total in USD.
        tip_rate: Tip as a decimal fraction.
        tip_amount: Calculated tip in USD.
        total: Bill plus tip in USD.
        per_person: Per-person share in USD.
        num_people: Number of people splitting.
        today: Date to print on the receipt.

    Returns:
        A monospaced receipt string ready for st.code().
    """
    width = 32
    divider = "-" * width
    lines = [
        divider,
        "         RECEIPT          ",
        divider,
        f"Date:        {today.strftime('%b %d, %Y')}",
        f"Bill:              ${bill_amount:>7.2f}",
        f"Tip ({tip_rate * 100:.0f}%):         ${tip_amount:>7.2f}",
        divider,
        f"TOTAL:             ${total:>7.2f}",
        f"Split ({num_people} people):   ${per_person:>7.2f}",
        divider,
        "      Thank you!          ",
        divider,
    ]
    return "\n".join(lines)


def build_breakdown_chart(
    bill_amount: float,
    tip_amount: float,
    per_person: float,
) -> go.Figure:
    """Build a Plotly bar chart showing payment breakdown.

    Args:
        bill_amount: Pre-tip bill total in USD.
        tip_amount: Calculated tip in USD.
        per_person: Per-person share in USD.

    Returns:
        A Plotly Figure object ready for st.plotly_chart().
    """
    categories = ["Base Amount", "Tip Amount", "Per-Person Share"]
    values = [bill_amount, tip_amount, per_person]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

    fig = px.bar(
        x=categories,
        y=values,
        color=categories,
        color_discrete_sequence=colors,
        title="Payment Breakdown",
        labels={"x": "Category", "y": "Amount (USD)"},
        text=[f"${v:.2f}" for v in values],
    )
    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>$%{y:.2f}<extra></extra>",
        textposition="outside",
    )
    fig.update_layout(showlegend=False)
    return fig


def compute_stats(values: list[float]) -> dict[str, float]:
    """Compute descriptive statistics for a list of numbers.

    Args:
        values: A list of numeric values to analyze.

    Returns:
        A dictionary with keys 'mean', 'median', and 'std_dev'.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError("Cannot compute statistics on an empty list.")
    return {
        "mean": statistics.mean(values),
        "median": statistics.median(values),
        "std_dev": statistics.pstdev(values),
    }
