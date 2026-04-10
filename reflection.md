# Reflection

**Week 2 Lab — Anatomy of Coding Agents**

---

**1. Tool Comparison**

When I tested the same Python function prompt across Claude (in Cursor) and ChatGPT (GPT-4o), the most notable difference was in error handling strategy: Claude raised precise, descriptive exceptions with the record index and missing key names, while ChatGPT used a broad `try/except` inside the loop that silently skipped invalid records with a `print` statement. Claude gave better code for a production context, because silent failures hide data quality bugs; ChatGPT gave a better first-read explanation — its paragraph summary was cleaner and easier to follow for someone learning. Neither tool was strictly "better" — they optimized for different things, and the right choice depends on whether you need code you can trust in production or code you can understand quickly as a beginner.

**2. Prompt Quality**

Looking at my prompt log, the shift from vague ("Add a chart to my app") to constrained ("Add a Plotly bar chart, always visible, not inside a button, using these exact variables and this color palette, with this edge case behavior") reduced the number of AI assumptions from roughly 90% to about 20% of the final output. The single most impactful type of constraint was **behavioral** — "always visible, not inside a button" — rather than styling or data source. I learned that AI tools fill gaps with plausible-but-wrong defaults: Matplotlib instead of Plotly, hidden behind a button, with hardcoded data. Being specific about what I do *not* want (negation constraints) was as important as specifying what I do want.

**3. Configuration Impact**

After creating `.cursorrules` and `CLAUDE.md`, the most measurable change was not in code style (type hints, docstrings) but in **explanation grounding**: with `CLAUDE.md` present, Claude Code's answers referenced the actual app's variables and use case instead of giving generic Streamlit tutorials. For configuration files going forward, I would add a section describing the target user (who actually uses the app), a list of things the AI should never do (e.g., "never use Matplotlib, never hardcode data, never put results behind a button"), and an explicit note about which libraries are already in `requirements.txt` — so the AI doesn't generate code that imports something the project doesn't have installed.
