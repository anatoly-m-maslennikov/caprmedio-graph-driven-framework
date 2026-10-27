---
atom_id: CA-P-2351@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Settings
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/Projection
version: 6
updated_at: 2026-10-24 11:10:31 +0400
relations:
  is_decomposition_of:
  - CA-P-2295
tier: 3
---
# Summary

Verify observed Settings Journal bindings

## Objective

Independently test the actual graph Settings receipt reader for both admitted forms, exact identity/evidence, malformed or tampered records, mismatched Project/path/digest, invalid versions, duplicates and unchanged Settings. Wait for P2348/P2349 authority and P2350 code freeze for final verdict. No production/source/Plan/Git changes; no live registration or whole-runtime completion claim.

## Details

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git. Existing blocked live operations stay blocked; this Task covers implementation and isolated tests only.

### Definition of Done

Exact source/code/test evidence and independent review prove this bounded outcome. Settings values and live Journal bytes remain unchanged. Preparation alone is not completion.


### Accepted outcome — 2026-10-13

Final graph-reader hash 3641ce9ae898fb5d9878e2a54908ce40af3a6f6832a684db811e05e8aca72c44 passed all 46 generator tests, including 9 independent methods with 195 subtests. Independent review exposed and verified the direct stale-digest fix. Canonical completed/recovered evidence, exact Project/path/digest/identity, tampering, ambiguity and absent current Carrier checks passed with no reader writes. Live registration and complete Settings schema admission remain separate.

