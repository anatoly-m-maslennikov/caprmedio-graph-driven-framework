---
cce_version: cce_1
cce_form: evaluation
version: 20
updated_at: 2026-10-27 19:59:35 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-261
  - CA-M-262
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-435
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Policy
tier: 3
---
# Evaluate reconstruction readiness

the reconstruction readiness Evaluation **must** return `fail` **if** rebuilding required behavior **or** evaluating the rebuilt result needs authority recovered from the previous Implementation **or** specification work **before** reconstruction; **if** a language change is selected, **then** evaluate readiness against the current RMED **after** its affected Method **and** Delivery updates. absence of a prebuilt alternative **must not** by itself cause failure.

the Evaluation **must not** report runtime equivalence **if** equal complete runtime inputs under unchanged RMED produce different outputs, relevant starting state **or** configuration **or** time **or** randomness **or** external-service responses are omitted from the comparison, applicable Method **or** Delivery constraints are violated, **or** an authorized RMED change is hidden inside the unchanged baseline. source-code differences alone **must not** cause failure. a fixed task order **or** readiness review **without** runtime evidence **must not** be reported as proof of equivalent reconstruction.
