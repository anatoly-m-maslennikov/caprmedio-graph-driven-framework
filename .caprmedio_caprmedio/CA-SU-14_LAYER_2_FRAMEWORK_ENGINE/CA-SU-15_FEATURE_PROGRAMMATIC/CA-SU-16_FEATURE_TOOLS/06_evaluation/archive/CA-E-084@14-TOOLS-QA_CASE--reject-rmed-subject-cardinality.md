---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
version: 14
updated_at: 2026-10-24 08:53:16 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1136
  - CA-R-1201
  - CA-R-1202
  - CA-D-269
atom_id: CA-E-084@14
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject RMED subject cardinality

## Test case

- give an RMED Atom **`=0`** GOVERNS targets.
- give another RMED Atom **`>=2`** distinct GOVERNS targets.
- give a valid RMED Atom **`=1`** GOVERNS target **and** **`>=0`** unique DEPENDS_ON targets; include a case with **`>=2`** DEPENDS_ON targets.

## Expected result

reject the first two fixtures with the stable RMED-subject-cardinality diagnostic **and** a non-zero exit. accept the third fixture with respect **to** Subject cardinality. count **only** GOVERNS targets toward the **`=1`** governed-target constraint; DEPENDS_ON targets **must not** be counted as additional GOVERNS targets.
