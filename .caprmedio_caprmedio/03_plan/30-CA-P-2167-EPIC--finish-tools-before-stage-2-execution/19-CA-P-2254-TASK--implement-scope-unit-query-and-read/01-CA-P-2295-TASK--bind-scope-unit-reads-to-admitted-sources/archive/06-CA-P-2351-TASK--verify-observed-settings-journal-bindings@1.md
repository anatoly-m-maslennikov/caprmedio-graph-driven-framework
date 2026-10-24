---
atom_id: CA-P-2351
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Configuration, Journal, Projection]
version: 1
updated_at: "2026-10-13 21:23:34 +0400"
relations:
  is_decomposition_of: [CA-P-2295]
---
# Summary

Verify observed Settings Journal bindings

## Objective

Independently test the actual graph Settings receipt reader for both admitted forms, exact identity/evidence, malformed or tampered records, mismatched Project/path/digest, invalid versions, duplicates and unchanged Settings. Wait for P2348/P2349 authority and P2350 code freeze for final verdict. No production/source/Plan/Git changes; no live registration or whole-runtime completion claim.

## Details

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git. Existing blocked live operations stay blocked; this Task covers implementation and isolated tests only.

### Definition of Done

Exact source/code/test evidence and independent review prove this bounded outcome. Settings values and live Journal bytes remain unchanged. Preparation alone is not completion.

