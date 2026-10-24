---
atom_id: CA-P-2350
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
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

Read observed Settings Journal bindings

## Objective

After P2348/P2349 source acceptance, update the existing graph Settings receipt reader to accept the admitted recovered-state observation alongside completed change receipts. Reuse registered Journal validation and preserve exact selected Project, path, digest, positive logical Revision, duplicate/ambiguity and zero-write behavior. Update existing fixtures to canonical records rather than bypass validation. No live registration, Settings edits, new Journal schema or claims of complete Settings schema admission.

## Details

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git. Existing blocked live operations stay blocked; this Task covers implementation and isolated tests only.

### Definition of Done

Exact source/code/test evidence and independent review prove this bounded outcome. Settings values and live Journal bytes remain unchanged. Preparation alone is not completion.

