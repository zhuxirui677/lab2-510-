# Component D: Testing & Validation

---

## Validation Exercise: Prompt Regression Test

### What Was Tested

Three prompts used during Level 2 and Level 3 of Component B were re-run with and without `.cursorrules` / `CLAUDE.md` to measure the impact of the configuration files on AI output quality.

---

### Step 2: Prompts Run WITHOUT Config Files

Config files were temporarily renamed:

```bash
mv .cursorrules .cursorrules.bak
mv CLAUDE.md CLAUDE.md.bak
```

Cursor was closed and reopened so no cached config remained.

---

### Step 3: Prompts Run WITH Config Files

Config files restored:

```bash
mv .cursorrules.bak .cursorrules
mv CLAUDE.md.bak CLAUDE.md
```

Cursor was restarted again before running.

---

### Step 4: Results

| # | Prompt Used | Without Config (Before) | With Config (After) | What Changed | Better / Worse / Same |
|---|-------------|------------------------|---------------------|--------------|----------------------|
| 1 | `"Add a helper function to utils.py that takes a list of numbers and returns mean, median, and std deviation as a dictionary."` | Generated function with no type hints, no docstring, used `numpy` (not in requirements.txt), single-letter variable `n` for the list | Generated function with `list[float]` type hint on input and `dict[str, float]` on output, full Google-style docstring with Args/Returns/Raises, used `statistics` module (stdlib), descriptive variable name `values` | Added type hints, docstring, switched from numpy to stdlib, renamed variable — all per `.cursorrules` | **Better** |
| 2 | `"Explain the st.session_state pattern used in this app."` | Generic explanation: "st.session_state is a dictionary-like object that persists values between reruns. It is useful for maintaining state in Streamlit apps." No project context. | Explanation referenced the specific variables in the app (`bill_amount`, `tip_rate`, `num_people`) and connected them to the tip calculator workflow: "In your Tip Calculator, session_state prevents the receipt summary from resetting when the user adjusts the number of people." | Used project context from `CLAUDE.md` to ground the explanation in the actual app | **Better** |
| 3 | `"Add error handling so the app doesn't crash if the user enters a negative bill amount."` | Added a bare `if bill_amount < 0: st.write("Invalid input")` with no styling, no early return, placed after the calculation (too late to prevent the error) | Added `if bill_amount < 0: st.error("Bill amount cannot be negative. Please enter a positive value."); st.stop()` placed before the calculation, using `st.error()` per Streamlit conventions in `.cursorrules` and `st.stop()` to halt the rerun cleanly | Used `st.error()` instead of `st.write()`, added `st.stop()`, moved validation before computation — all per `.cursorrules` Streamlit conventions | **Better** |

---

## Smoke Test Results

For each configuration-adjusted output, I confirmed:

| # | Runs without error | Core path works | Invalid input handled |
|---|--------------------|-----------------|-----------------------|
| 1 (`compute_stats`) | Yes — `streamlit run app.py` passed | Yes — `compute_stats([10, 20, 30])` returned `{'mean': 20.0, 'median': 20.0, 'std_dev': 8.16}` | Yes — `compute_stats([])` raises `ValueError: Cannot compute statistics on an empty list.` |
| 2 (explanation) | N/A — explanation only | N/A | N/A |
| 3 (error handling) | Yes — no crash on negative input | Yes — positive bill works normally | Yes — `-5` shows red `st.error()` and halts; `0` shows info message from chart section |

---

## Quality Gate Checklist

- [x] **Smoke test completed**: Each generated function runs, core behavior works once, and invalid input is handled without crashing
- [x] **3 prompts tested**: Recording table has 3 complete rows with before/after observations
- [x] **Differences are specific**: Each "What Changed" entry describes a concrete observable change (e.g., "added type hints" not "output improved")
- [x] **Config files restored**: `.cursorrules` and `CLAUDE.md` are back in place; re-ran Prompt 1 to verify (same good output as "with config" run)
- [x] **Honest assessment**: All 3 prompts showed improvement. No "Same" results, but I note that Prompt 2 (explanation quality) is harder to measure objectively — the improvement is real but relies on judgment, not a passing/failing test
- [x] **Prompts are documented**: Exact prompt text recorded in the table above; reproducible by anyone in the same project directory

---

## Testing Concept: Regression Testing

### Key Insight from This Exercise

Configuration files are inputs to the AI, not just documentation. Changing `.cursorrules` or `CLAUDE.md` is functionally equivalent to changing a parameter in a function — it changes outputs. This means:

1. Config files should be version-controlled (committed to git) so changes are tracked
2. If AI output quality suddenly drops on a prompt that used to work, check whether a config file changed
3. In a team setting, config file changes should be reviewed like code changes — they affect every AI-generated output going forward

The most surprising finding: the biggest quality gain was not from style rules (type hints, docstrings) but from **project-grounded explanations**. When `CLAUDE.md` gave Claude Code the app's purpose and user context, its explanations became actionable rather than generic. This suggests that project context (what the app is for, who uses it) is as valuable in config files as coding standards.
