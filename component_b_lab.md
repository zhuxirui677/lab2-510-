# Component B: Lab

---

## Recall Prompt

Before writing my first prompt today, I reflected on the problem statement from Component A:

> *"When Jason needs to review course petition syllabi for equivalency, he currently manually merges documents, emails each student individually across multiple unreliable systems, and hand-checks credit caps — which leads to repeated administrative effort, inconsistent tracking, and delayed outcomes for students."*

Using the same format to describe what I want AI to build:

> *"When a developer needs to build a course petition review tool, they currently spend time manually wiring up UI, data handling, and workflow logic, which leads to slow prototyping and inconsistent code structure. I want the AI to scaffold a Streamlit app that handles document upload, keyword comparison, and status tracking."*

---

## Warm-Up — Level 2: Model Comparison

### Test Prompt Used

```
Write a Python function that takes a list of student records (dictionaries with
"name", "program", and "gpa" keys) and returns only the students in a given
program with a GPA above a given threshold. Include error handling.
```

---

### Model A: Claude (in Cursor)

```python
def filter_students(
    students: list[dict],
    program: str,
    gpa_threshold: float
) -> list[dict]:
    """
    Filter students by program and minimum GPA.

    Args:
        students: List of student record dicts with 'name', 'program', 'gpa'
        program: Program name to filter by
        gpa_threshold: Minimum GPA (inclusive)

    Returns:
        List of matching student records

    Raises:
        TypeError: If students is not a list
        ValueError: If gpa_threshold is not a valid number
    """
    if not isinstance(students, list):
        raise TypeError(f"Expected a list, got {type(students).__name__}")
    if not isinstance(gpa_threshold, (int, float)):
        raise ValueError(f"gpa_threshold must be a number, got {type(gpa_threshold).__name__}")

    result = []
    for i, student in enumerate(students):
        if not isinstance(student, dict):
            raise TypeError(f"Record at index {i} is not a dict: {student}")
        missing = [key for key in ("name", "program", "gpa") if key not in student]
        if missing:
            raise KeyError(f"Record at index {i} is missing keys: {missing}")
        if student["program"] == program and student["gpa"] >= gpa_threshold:
            result.append(student)
    return result
```

**Explanation provided by Claude:**
- Explained each parameter with types
- Described the logic of the loop step by step
- Explicitly listed what exceptions are raised and when
- Mentioned that the comparison is inclusive (`>=`)

---

### Model B: ChatGPT (GPT-4o)

```python
def filter_students(students, program, gpa_threshold):
    """
    Returns students in the specified program with GPA above the threshold.
    """
    if not isinstance(students, list):
        raise TypeError("students must be a list")

    filtered = []
    for student in students:
        try:
            if student.get("program") == program and student.get("gpa", 0) >= gpa_threshold:
                filtered.append(student)
        except Exception as e:
            print(f"Skipping invalid record: {e}")

    return filtered
```

**Explanation provided by ChatGPT:**
- Gave a brief paragraph summary
- Mentioned `.get()` is used to avoid KeyError
- Did not explain individual lines in detail
- Suggested adding unit tests as a follow-up

---

### Observations

1. **Code Style:** Claude used type annotations (`list[dict]`, `float`) and a detailed docstring with `Args`, `Returns`, and `Raises` sections — closer to production-level style. ChatGPT produced cleaner, more readable code without annotations, which is easier to understand for beginners but less self-documenting.

2. **Error Handling Strategy:** Claude raises explicit, descriptive exceptions (e.g., `KeyError` listing which keys are missing, with the record index). ChatGPT uses a broad `try/except` inside the loop that silently skips bad records with a `print` — this avoids crashes but hides data quality problems, which could be dangerous in a real application.

3. **Explanation Quality:** Claude's explanation was more granular — it walked through each edge case and why a particular decision was made. ChatGPT's explanation was higher-level and more conversational, better suited for understanding the big picture quickly but less useful for debugging or code review.

---

## Level 1: Claude Code Setup

### Step 1.1 — Verify Week 1 Tools

```bash
$ git --version
git version 2.46.0

$ python3 --version
Python 3.12.3

$ streamlit --version
Streamlit, version 1.35.0

$ node --version
v20.14.0
```

All tools confirmed working. Node.js is v20 (LTS), meeting the requirement.

---

### Step 1.2 — Create Anthropic API Key

1. Went to [https://console.anthropic.com](https://console.anthropic.com) and logged in.
2. Navigated to **Settings > API Keys**.
3. Clicked **Create Key**, named it `techin510`.
4. Copied the key immediately and saved it to a local password manager.
5. Key is **not** stored in any project file or pushed to GitHub.

---

### Step 1.3 — Install Claude Code

Followed the official Claude Code documentation:

```bash
npm install -g @anthropic-ai/claude-code
```

Verified installation:

```bash
$ claude --version
1.0.3 (claude-sonnet-4-5)
```

---

### Step 1.4 — Launch Claude Code in Project

Navigated to my Week 1 app folder and launched Claude Code:

```bash
cd ~/Documents/techin510/my-first-app
source .venv/bin/activate
claude
```

On first launch, authenticated via browser redirect. After authentication, tested with:

```
What files are in this project? Give me a brief summary.
```

**Claude Code's response:**

> Your project contains: `app.py` (main Streamlit app — a tip calculator with bill input, tip percentage slider, and per-person split), `requirements.txt` (lists streamlit and pandas), `.venv/` (virtual environment directory). The app currently runs a single-page layout with no persistent state.

Typed `/exit` to end the session.

**Checkpoint confirmed:**
- [x] All Week 1 tools working
- [x] Node.js v20+ installed
- [x] Anthropic API key stored securely (not in repo)
- [x] `claude --version` returns version number
- [x] Successfully launched Claude Code in project folder and received a response

---

## Level 2: Three Cursor Modes

### Step 2.1 — Open Project in Cursor

Opened the Week 1 Streamlit app in Cursor via **File > Open Folder**.

```bash
cd ~/Documents/techin510/my-first-app
source .venv/bin/activate
```

Virtual environment activated before opening.

---

### Step 2.2 — Composer (Cmd+I): Add a New Feature

**Prompt used in Cursor Composer:**

```
Add a new "Receipt Summary" section below the existing tip calculator.
It should display a formatted receipt that shows: the date, bill amount,
tip percentage, tip amount, total amount, and per-person amount.
Style it to look like a printed receipt using a monospaced font.
Add a "Copy to Clipboard" button using st.code() or pyperclip.
```

**Generated code review:**
- New section appeared below the calculator with correct layout
- Used `st.code()` to simulate monospaced receipt formatting
- `datetime.today()` imported automatically for the date field
- Copy button implemented with `st.button()` + `st.code()` block (clipboard API not directly available in Streamlit without JS)

**Checked before accepting:**
- No missing imports (datetime was added at the top)
- Indentation was clean
- Receipt values referenced the same session state variables as the calculator

**Accepted the changes. App ran successfully:**

```bash
streamlit run app.py
```

No errors on first run.

---

### Step 2.3 — Chat (Cmd+L): Understand Code

Selected the following block from `app.py`:

```python
if "history" not in st.session_state:
    st.session_state["history"] = []
```

Opened Cursor Chat (`Cmd+L`) and typed:

```
Explain this code to me step by step. I am a graduate student learning
to code. What does each line do, and why is it written this way?
```

**Claude's explanation (summarized):**

> `st.session_state` is Streamlit's way of persisting data between reruns. Every time the user interacts with the app (e.g., moves a slider), Streamlit re-executes the entire script from top to bottom. Without session state, variables would reset on every interaction. This `if` check ensures the history list is only initialized once — the first time the app loads. After that, existing data is preserved.

**Follow-up I asked:**

```
What would happen if I removed the if check and just wrote:
st.session_state["history"] = []
```

**Claude's answer:**

> The history list would be wiped clean on every rerun. Any tip calculation the user added would disappear the moment they adjusted a slider or clicked a button. The `if` guard is what makes the state persistent.

This clarified something I had been unsure about — why the pattern always uses `if "key" not in st.session_state`.

---

### Step 2.4 — Inline Edit (Cmd+K): Refactor Code

Selected the following tip calculation block:

```python
if tip_option == "10%":
    tip_rate = 0.10
elif tip_option == "15%":
    tip_rate = 0.15
elif tip_option == "18%":
    tip_rate = 0.18
elif tip_option == "20%":
    tip_rate = 0.20
elif tip_option == "Custom":
    tip_rate = custom_tip / 100
```

Pressed `Cmd+K` and typed:

```
Refactor this to use a dictionary instead of multiple if/elif statements.
Rename variables to be more descriptive and add a short comment.
```

**Refactored result:**

```python
# Map tip label to decimal rate; fall back to custom input if "Custom" selected
TIP_RATE_MAP = {
    "10%": 0.10,
    "15%": 0.15,
    "18%": 0.18,
    "20%": 0.20,
}
tip_rate = TIP_RATE_MAP.get(tip_option, custom_tip / 100)
```

**Reviewed and accepted.** The logic is identical but:
- Easier to extend (just add a new key to the dict)
- Eliminates repeated `elif` branches
- `dict.get()` handles the "Custom" fallback cleanly

App still ran without errors after the refactor.

---

### Level 2 Checkpoint

- [x] Used Cursor Composer (`Cmd+I`) to add a Receipt Summary feature
- [x] Used Cursor Chat (`Cmd+L`) to understand `st.session_state`
- [x] Used Inline Edit (`Cmd+K`) to refactor if/elif into a dictionary
- [x] App runs without errors after all three changes

---

## Information Hierarchy Review

### Step 1: The Squint Test

Opened the app in the browser, leaned back, and squinted until text blurred.

**Top 3 elements that still stood out:**
1. The large `st.title()` header — "Tip Calculator"
2. The number input box for bill amount (high contrast border)
3. The green total amount displayed in `st.metric()`

### Step 2: Evaluate Hierarchy

| Question | Answer |
|----------|--------|
| What is the most important piece of information? | The total amount and per-person split |
| Is that information the most visually prominent? | No — the bill input drew more attention than the result |
| Can a first-time user understand what this app does at a glance? | Yes |
| Are related items visually grouped together? | Partially — controls and results were mixed on one page |
| Is there any element that draws attention but is not important? | Yes — the "Receipt Summary" section header was visually heavy but secondary |

### Step 3: One Hierarchy Fix

**Change made:** Moved the total amount `st.metric()` display above the tip controls, and added `st.divider()` between the input section and the results section.

**Why:** The user's primary need is to see the result — not to watch the inputs. Moving the result above the fold keeps the most important information at the top, consistent with how a physical receipt works.

**Prompt used in Cursor Composer to implement the fix:**

```
Move the st.metric() result cards above the input controls section.
Add st.divider() between the results and the input area.
Keep all functionality the same — only reorder the visual layout.
```

---

## Level 3: Prompt Engineering Workshop

### Step 3.1: Spec First

Before writing any prompt, I wrote a 3-sentence spec:

> **What it should do:** Display a bar chart showing the tip amount, base amount, and per-person share as three side-by-side bars, updating live as the user adjusts inputs.
> **Inputs:** Bill amount (float), tip percentage (float), number of people (int) — all already in `st.session_state`.
> **Output:** A Plotly bar chart with labeled axes, a legend, and hover tooltips showing exact dollar values. Chart appears below the receipt summary section.

---

### Attempt 1 — Vague Prompt

**Prompt:**
```
Add a chart to my app
```

**Result:**
Cursor generated a Matplotlib bar chart with hardcoded sample data (`[10, 20, 30]`) and no connection to the actual bill/tip values. It imported `matplotlib.pyplot` at the top and used `st.pyplot()`. The chart appeared at the bottom of the page with no title, no axis labels, and no interactivity. It also added a `fig.clf()` call that was unnecessary.

**What the AI assumed:**
- Matplotlib (not Plotly)
- Hardcoded data instead of dynamic session state values
- No context about what data existed in the app

**What was missing:** Data source, chart type rationale, axis labels, interactivity, positioning.

---

### Attempt 2 — Specific Prompt

**Prompt:**
```
Add a bar chart below the receipt summary using Plotly. Show three bars:
"Base Amount", "Tip Amount", and "Per-Person Share". Pull the values from
the bill_amount, tip_amount, and per_person variables already calculated
in the app. Include a title "Payment Breakdown", label both axes, and add
hover tooltips showing exact dollar amounts.
```

**Result:**
Cursor generated a proper Plotly bar chart using `px.bar()`. It correctly referenced the existing variables, added axis labels (`st.plotly_chart(fig)`), and included hover data. The chart title was "Payment Breakdown" as specified. Colors were Plotly defaults (blue). One issue: it placed the chart inside an `if st.button("Show Chart"):` block, making it hidden by default — not what I wanted.

**Improvement over Attempt 1:** Data was live and connected. Labels and interactivity worked. Still one assumption error (button gating).

---

### Attempt 3 — Constrained Prompt

**Prompt:**
```
Add a Plotly bar chart (not Matplotlib) directly below the receipt summary
section — always visible, not inside a button. Show three bars: "Base Amount",
"Tip Amount", and "Per-Person Share", using the variables bill_amount,
tip_amount, and per_person that are already calculated. Use the color palette
["#1f77b4", "#ff7f0e", "#2ca02c"]. Title: "Payment Breakdown". X-axis label:
"Category". Y-axis label: "Amount (USD)". Add hover tooltips with exact values
formatted as "$X.XX". If bill_amount is 0, display st.info("Enter a bill
amount to see the chart.") instead of an empty chart. Follow .cursorrules.
```

**Result:**
Output matched the spec exactly. Chart was always visible, used the correct color palette, had properly formatted tooltips (`$12.50`), and showed the `st.info()` message when bill was zero. The function had a type hint and a docstring (because `.cursorrules` was active). No unnecessary `st.button()` wrapper.

**What constrained prompts added:**
- "not Matplotlib" eliminated the wrong tool assumption
- "always visible, not inside a button" fixed the hidden chart issue
- `"$X.XX"` format string eliminated ambiguity about tooltip format
- Edge case instruction for zero bill prevented a silent empty chart

---

### Step 3.5: Reflection on Progression

1. **Biggest difference:** Vague → Specific removed the hardcoded data problem. Specific → Constrained removed the button-gating assumption. The AI made one major error at each level that only the next level of specificity fixed.

2. **What mattered most:** Behavior constraints ("always visible, not inside a button") had the most impact. Layout and data source were also critical. Styling mattered least — Plotly defaults were acceptable.

3. **AI vs. my instructions:** In the vague prompt, roughly 90% of decisions came from the AI's assumptions. In the constrained prompt, roughly 80% came from my instructions. The AI still chose chart sizing and animation settings — but those were reasonable defaults I was comfortable accepting.

---

## Level 4: Configuration Files

### Step 4.1: `.cursorrules`

Created `.cursorrules` in the project root. See [`.cursorrules`](.cursorrules) for the full file.

**Key sections added:**
- Python 3.11+ with type hints required
- Google-style docstrings on all functions
- Streamlit conventions (no hardcoded data, use `st.cache_data`, errors via `st.error()`)
- Plotly preferred for charts; specific color palette `["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]`
- Project structure: `app.py` for UI, `utils.py` for logic

**Test prompt used after saving:**
```
Add a new helper function to utils.py that takes a list of numbers and
returns the mean, median, and standard deviation as a dictionary.
```

**Result with `.cursorrules` active:**
```python
import statistics
from typing import Union

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
```

Type hints, Google docstring, descriptive variable names — all consistent with `.cursorrules`.

---

### Step 4.2: `CLAUDE.md`

Created `CLAUDE.md` in the project root. See [`CLAUDE.md`](CLAUDE.md) for the full file.

**Test in Claude Code:**

```bash
cd ~/Documents/techin510/my-first-app
claude
```

Prompt:
```
What is this project? What tech stack does it use?
```

**Claude Code's response (with CLAUDE.md present):**

> This is a Streamlit web app called "Tip Calculator" — a course project for TECHIN 510 at UW GIX. It calculates tip amounts, totals, and per-person splits for restaurant bills. The tech stack is: Python 3.11+, Streamlit for the web interface, Plotly for interactive charts, and Pandas for any data manipulation. The target users are students and diners who want a quick, formatted receipt breakdown. Run with `streamlit run app.py`.

Claude Code answered accurately from `CLAUDE.md` without reading every source file.

---

### Level 4 Checkpoint

- [x] `.cursorrules` created and tested — AI output now includes type hints, docstrings, and Streamlit conventions
- [x] `CLAUDE.md` created and tested — Claude Code correctly described the project from context file
- [x] Prompt log contains 3 prompts (vague → specific → constrained) with before/after results
- [x] All changes committed and pushed to GitHub
