---
atom_id: CA-P-2350
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project.Settings
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Continuant/Projection
version: 7
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2295
tier: 3
---
# Summary

Read observed Settings Journal bindings

## Objective

After P2348/P2349 source acceptance, update the existing graph Settings receipt reader to accept the admitted recovered-state observation alongside completed change receipts. Reuse registered Journal validation and preserve exact selected Project, path, digest, positive logical Revision, duplicate/ambiguity and zero-write behavior. Update existing fixtures to canonical records rather than bypass validation. No live registration, Settings edits, new Journal schema or claims of complete Settings schema admission.

## Details

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git. Existing blocked live operations stay blocked; this Task covers implementation and isolated tests only.

### Definition of Done

Exact source/code/test evidence and independent review prove this bounded outcome. Settings values and live Journal bytes remain unchanged. Preparation alone is not completion.


### Accepted outcome — 2026-10-13

Final graph-reader hash 3641ce9ae898fb5d9878e2a54908ce40af3a6f6832a684db811e05e8aca72c44 passed all 46 generator tests, including 9 independent methods with 195 subtests. Independent review exposed and verified the direct stale-digest fix. Canonical completed/recovered evidence, exact Project/path/digest/identity, tampering, ambiguity and absent current Carrier checks passed with no reader writes. Live registration and complete Settings schema admission remain separate.

