# Component A: Staff Interview
## Interviewee: Jason Evans, Academic Student Counselor (ASC)
## Topic: Course Petition Syllabus Review Workflow

---

## Interview Script & Notes

### Background

Jason Evans is the Academic Student Counselor responsible for reviewing course petitions. When a student wants to transfer external course credits toward a TECHIN program requirement, they must submit a petition. Jason's job is to evaluate whether the external course syllabus is equivalent to the required TECHIN course.

---

### Interview Notes

**Q: Can you walk me through what happens when a student submits a course petition?**

> Students upload their documents themselves — usually one document per petition form. They submit their external course syllabus so I can compare it against the TECHIN course syllabus.

*Note: Upload process relies entirely on students — format and completeness vary.*

**Q: What are you actually looking for when you compare the two syllabi?**

> I'm checking whether they're roughly the same — I'd say the threshold is about 90% match. I look at four main things: learning outcomes, the institution offering the course, the topics covered, and whether the course has similar projects or exams as the basis for assessment.

*Note: Clear mental model of equivalence criteria — 4 keywords.*

**Q: What happens when one course covers multiple TECHIN equivalencies?**

> If a student is claiming one external course covers multiple TECHIN courses, I combine all the equivalencies into one file for review. There's a maximum of three equivalencies allowed per course.

*Note: Manual file-merging step — no dedicated tool for this.*

**Q: How do you communicate with students during this process?**

> I email each student individually. It's not a group email — every case is different. And not all students write in English, so sometimes the communication gets complicated. I use multiple systems and I get different responses from different students, which makes it hard to track where each petition is.

*Note: One-on-one email communication across language barriers, no centralized tracking.*

**Q: Is there anything that slows you down the most?**

> Honestly, the reliability issue. The emails aren't always reliable — I send something and I don't know if the student received it. And I have to double-check that each student doesn't exceed 9 transfer credits total. That's a hard cap, but there's no automatic check — I have to verify it manually every time.

*Note: No automated credit cap validation; manual verification burden.*

**Q: What does the approval process look like after your review?**

> After I complete my review, I send my recommendation to the instructor for approval. Then it goes to equivalence faculty review. Once everything is approved, the course gets highlighted in the student's transcript, and I send a result email to the student.

*Note: Multi-stakeholder approval chain — instructor → faculty → transcript update → student notification.*

---

## Emotional Journey Map

**Color Legend:**
- 🔴 **RED — Frustration Peak**: irritation, resignation, repeated manual effort
- 🟢 **GREEN — Delight Moment**: satisfaction, confidence, clarity
- 🟡 **YELLOW — Uncertainty Zone**: hesitation, "it depends," inconsistency

| Step | Action | Emotion |
|------|--------|---------|
| 1 | Student uploads documents (one doc per form) | 🟡 YELLOW — format and completeness are unpredictable |
| 2 | Jason opens and checks the submitted syllabus | 🟢 GREEN — clear starting point when documents are complete |
| 3 | Compare student syllabus vs. TECHIN syllabus on 4 keywords | 🟢 GREEN — 90% match rule gives clear decision criteria |
| 4 | If multiple courses → merge into one combined file (max 3) | 🔴 RED — manual merging with no dedicated tool, tedious and error-prone |
| 5 | Check student's email domain (.edu or other) | 🟡 YELLOW — inconsistent; non-.edu accounts sometimes unreachable |
| 6 | Email student individually (not in group) | 🔴 RED — time-consuming, repeated one-on-one work; some students reply in other languages |
| 7 | Track petition status across multiple systems | 🔴 RED — different systems give different responses; no single source of truth |
| 8 | Manually verify 9-credit cap for each student | 🔴 RED — no automation; must cross-reference manually every time |
| 9 | Send recommendation to instructor for approval | 🟡 YELLOW — outcome depends on instructor availability and response time |
| 10 | Equivalence faculty review | 🟡 YELLOW — timeline and criteria can vary by faculty |
| 11 | Highlight course in transcript upon approval | 🟢 GREEN — clear, satisfying closure when everything is in order |
| 12 | Send result email to student | 🟢 GREEN — closing the loop; student gets their answer |

---

## Problem Statement

> **"When Jason needs to review course petition syllabi for equivalency, he currently manually merges documents, emails each student individually across multiple unreliable systems, and hand-checks credit caps — which leads to repeated administrative effort, inconsistent tracking, and delayed outcomes for students."**

---

## If-Then Flowchart

```
[Student Submits Petition + Syllabus]
        |
        v
[Is document complete and in correct format?]
   |                        |
  YES                       NO
   |                        |
   v                        v
[Proceed to Review]   🟡 [Email student to resubmit]
        |                   (individual email — unreliable)
        v
[Compare: Student Syllabus vs. TECHIN Course Syllabus]
  Check: Learning Outcomes / Institution / Topics / Exam-Project Basis
        |
        v
[Is match >= 90%?]
   |                        |
  YES                       NO
   |                        |
   v                        v
[Is this a multi-course     🟢 [Mark as Not Equivalent]
 equivalency claim?]              → Email student result
   |          |
  YES         NO
   |          |
   v          v
🔴 [Manually merge    [Single equivalency file ready]
 syllabi into one         |
 file (max 3)]            |
        |_________________|
                |
                v
🔴 [Manually verify student has not exceeded 9-credit cap]
                |
                v
[Does student exceed credit cap?]
   |                        |
  YES                       NO
   |                        |
   v                        v
🟡 [Flag for discussion] [Send to Instructor for Approval]
                                |
                                v
                    [Instructor approves?]
                       |              |
                      YES             NO
                       |              |
                       v              v
              [Send to Faculty    🟡 [Revise or escalate]
               Equivalency Review]
                       |
                       v
              [Faculty approves?]
                 |           |
                YES           NO
                 |             |
                 v             v
      🟢 [Highlight course  🟡 [Notify student
        in transcript]        of denial + reason]
                 |
                 v
      🟢 [Send result email to student]
                 |
                 v
            [COMPLETE]
```

**Flowchart Color Key:**
- 🔴 RED = Frustration Peak — manual, repetitive, error-prone steps
- 🟢 GREEN = Delight Moment — clear decisions, satisfying closure
- 🟡 YELLOW = Uncertainty Zone — outcome depends on external factors or inconsistent inputs

---

## Design Implications

**Reduce Frustration Peaks:**
- Automate credit cap validation (flag when student approaches 9-credit limit)
- Provide a structured document upload template so submissions arrive in a consistent format
- Centralize petition tracking in a single dashboard instead of scattered email threads
- Support multi-language communication with translation assistance

**Preserve Delight Moments:**
- Keep the human decision on equivalency — the 4-keyword framework Jason uses is a professional judgment, not a formula
- Maintain personal result communication but reduce the overhead (e.g., pre-filled email templates)

**Resolve Uncertainty Zones:**
- Standardize the multi-course merging workflow with a tool that handles the max-3 rule automatically
- Provide status visibility so both Jason and students know where a petition stands at any point
```
