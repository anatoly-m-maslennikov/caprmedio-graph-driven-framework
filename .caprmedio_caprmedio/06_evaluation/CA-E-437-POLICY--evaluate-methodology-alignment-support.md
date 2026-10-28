---
cce_version: cce_1
cce_form: evaluation
version: 21
updated_at: 2026-10-27 19:59:35 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-R-1424
subjects:
  governs: 'Subject/caprmedio/Product: CAPRMEDIO Framework'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-437
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Policy
tier: 5
---
# Evaluate methodology alignment support

the methodology alignment support Evaluation **must** return `fail` **if** the available Tools cannot assess the governed instance against the current Applicable Methodology, omit known nonconformance, cannot support an authorized repair, **or** mutate authority **without** Operator permission; a targeted check **may** use a bounded affected Scope **and** its dependencies. an unresolved finding **or** Operator-created orphan **must not** by itself establish failure of the required support capability **or** be reported as conformance.
