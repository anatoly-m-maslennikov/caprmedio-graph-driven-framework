---
atom_id: CA-P-2175
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Plan]
version: 1
updated_at: "2026-10-12 04:02:18 +0400"
relations:
  is_decomposition_of: [CA-P-2172]
  blocks: [CA-P-2174]
---
# Summary

Select current originals in Subject preview

## Objective

The existing Subject preview selects eligible current non-archived originals and preserves intended Status.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisites: CA-P-2168 and its actual current preview contract packet independently accepted under CA-P-2171. Other contract packets need not be complete. Reopen all callers of the preview's shared eligibility check and bind their exact affected files/tests before editing. Own only preview eligibility and its focused fixtures; coordinate shared parser/writer changes with integration.

Apply the smallest contract-aligned change. Preserve existing role/owner/currentness checks, exact source sealing, unrelated bytes, Version/time/history handling and standalone apply rejection. Check valid non-Active current, Active current, archived, duplicate-current and ineligible cases. Deliver implementation/test pins and actual results to CA-P-2174. Split before execution if more than 15 minutes is required; no original Core write occurs.

### Definition of Done

The Plan is **not** Done if independent contract acceptance is missing/stale, a caller remains inconsistent, currentness still requires literal Active, unrelated bytes/Status/guards regress, focused checks fail, or own work exceeds 15 minutes without decomposition.
