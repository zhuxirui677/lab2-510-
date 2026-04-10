# Component C: System Architecture & Design

---

## C.1 Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER (Browser)                           │
│                   Interacts via Streamlit UI                    │
└───────────────────────────┬─────────────────────────────────────┘
                            │ HTTP (localhost:8501)
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                     app.py  (YOUR CODE)                         │
│  - st.set_page_config()                                         │
│  - UI layout: inputs, metrics, receipt, chart                   │
│  - st.session_state for persistent values                       │
│  - calls utils.py functions for computation                     │
└──────────┬────────────────┬────────────────────────────────────-┘
           │                │
           ▼                ▼
┌─────────────────┐  ┌──────────────────────────────────────────┐
│   utils.py      │  │         External Libraries               │
│  (YOUR CODE)    │  │  Streamlit  │  Plotly  │  Pandas         │
│  - compute_tip()│  │  (UI fwk)   │  (charts)│  (data tables)  │
│  - compute_stats│  │  You call   │  You call│  You call them  │
│  - format_receipt│  │  them; you  │  them;   │  but don't own  │
└─────────────────┘  │  don't own  │  don't   │  them           │
                     │  Streamlit  │  own it  │                 │
                     └──────────────────────────────────────────┘
           │
           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  AI Tools (Boundary Layer)                      │
│                                                                 │
│  ┌──────────────────────┐    ┌──────────────────────────────┐  │
│  │  Cursor (IDE)        │    │  Claude Code (Terminal)      │  │
│  │  Reads: .cursorrules │    │  Reads: CLAUDE.md            │  │
│  │  Modes:              │    │  Commands: read/write files  │  │
│  │   Composer (Cmd+I)   │    │  Scope: whole project        │  │
│  │   Chat (Cmd+L)       │    │                              │  │
│  │   Inline (Cmd+K)     │    │                              │  │
│  └──────────────────────┘    └──────────────────────────────┘  │
│                                                                 │
│  Boundary: AI tools PROPOSE changes. YOU accept or reject.     │
│  They cannot push to GitHub or run your app on their own.      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                        GitHub                                   │
│  - Remote code storage                                          │
│  - Version history (git log, git blame)                         │
│  - You push; GitHub handles storage, access, versioning         │
│  - Boundary: you control what gets pushed via git add/commit    │
└─────────────────────────────────────────────────────────────────┘
```

**Component Ownership Summary:**

| Component | Who owns it | What the boundary looks like |
|-----------|-------------|------------------------------|
| `app.py` | You | You write it; AI proposes, you accept |
| `utils.py` | You | Pure Python logic; no UI dependency |
| Streamlit | Third party | You call `st.*` functions; Streamlit handles rendering |
| Plotly | Third party | You build `fig` objects; Plotly handles SVG/JS output |
| `.cursorrules` / `CLAUDE.md` | You | Your instructions to AI tools; they read but cannot modify |
| Cursor / Claude Code | Third party (AI tools) | They read your files and propose changes |
| GitHub | Third party | Stores your git objects; you control what is pushed |

---

## C.2 Design Decision Log

### This Week's Decision: Where Should Project Context Live?

> "Where should project context live — in `.cursorrules`, in `CLAUDE.md`, in your prompts, or in all three?"

---

| Field | Entry |
|-------|-------|
| **Decision** | Store coding standards and Streamlit conventions in `.cursorrules`; store project description, tech stack, and run commands in `CLAUDE.md`; reserve prompts for task-specific, one-time instructions only |
| **Alternatives considered** | (1) Put everything in `.cursorrules` only; (2) Put everything in every prompt; (3) Use neither file and rely on prompt context each time |
| **Why I chose this** | `.cursorrules` is Cursor-specific and code-focused; `CLAUDE.md` is Claude Code-specific and project-context-focused. Mixing them creates confusion about which tool reads what. Prompts are ephemeral — they disappear after each session, so they cannot carry conventions across sessions |
| **Trade-off** | Maintaining two separate context files means they can drift out of sync. If I update the tech stack in `CLAUDE.md` but forget to update `.cursorrules`, one tool has stale context. Single-file is easier to maintain but loses tool-specific optimization |
| **When I would choose differently** | For a one-day project or throwaway prototype, I would skip both files and just prompt — the overhead of maintaining config files is not worth it. For a team project, I would add a third file (`AI_CONTEXT.md`) that both tools read, so standards only live in one place |

---

### Conflict Resolution: What Wins When Files Contradict?

During testing, I found that when `.cursorrules` said "use Plotly" but a prompt said "use Matplotlib," Cursor followed the **prompt** over the rules file. This makes sense: prompts are explicit, immediate instructions while rules are defaults. The hierarchy is:

```
Explicit prompt instruction  >  .cursorrules  >  model's default behavior
```

**Implication for design:** Put non-negotiables in config files (security practices, project structure, style). Put task-specific choices in the prompt. Never contradict yourself between the two — resolve conflicts in the config file first.

---

### Information That Belongs in One File, Not the Other

| Information | Right place | Wrong place | Why |
|-------------|-------------|-------------|-----|
| Coding style (type hints, docstrings) | `.cursorrules` | Prompt | Applies to every generated function — should be automatic, not re-stated each time |
| "Run with `streamlit run app.py`" | `CLAUDE.md` | `.cursorrules` | This is operational context for Claude Code (terminal agent), not a coding convention |
| Target audience ("students at UW GIX") | `CLAUDE.md` | `.cursorrules` | Project context, not code style |
| Color palette | `.cursorrules` | `CLAUDE.md` | Code-level styling standard; Cursor needs it; Claude Code rarely generates charts |
| API keys / secrets | Neither | Both | Never in any AI-readable context file |
