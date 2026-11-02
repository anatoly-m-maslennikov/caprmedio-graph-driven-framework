---
cce_version: cce_1
cce_form: evaluation
version: 27
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-R-1424
subjects:
  active: Aspects <+ Product
  passive:
  - 'Entity/Object/Continuant/Projection/Type: Applicable Methodology'
  - Entity/Object/Continuant/Actor/Operator
  - Package
  - Entity/Object/Continuant/Term//Artifact
  - Atom/(.Role := Evaluation)
  - Entity/Object/Continuant/Selection
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-437
status: Active
current_scope_unit: caprmedio
tier: 5
role: Evaluation
form: Eval Policy
---
## Summary
Evaluate methodology alignment support

## Claim

the methodology alignment support Evaluation **must** return `fail` **if** the available Tools cannot assess the governed instance against the current Applicable Methodology, omit known nonconformance, cannot support an authorized repair, **or** mutate authority **without** Operator permission; a targeted check **may** use a bounded affected Scope **and** its dependencies. an unresolved finding **or** Operator-created orphan **must not** by itself establish failure of the required support capability **or** be reported as conformance.
