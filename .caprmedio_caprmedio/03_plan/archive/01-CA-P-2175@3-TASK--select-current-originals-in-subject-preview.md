---
atom_id: CA-P-2175@3
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
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Subject
  - Plan
version: 3
updated_at: 2026-10-23 23:03:23 +0400
relations:
  is_decomposition_of:
  - CA-P-2172
  blocks:
  - CA-P-2174
---
# Summary

Select current originals in Subject preview

## Objective

The existing Subject preview selects eligible current non-archived originals and preserves intended Status.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisites: CA-P-2168 and its actual current preview contract packet independently accepted under CA-P-2171. Other contract packets need not be complete. Reopen all callers of the preview's shared eligibility check and bind their exact affected files/tests before editing. Own only preview eligibility and its focused fixtures; coordinate shared parser/writer changes with integration.

Apply the smallest contract-aligned change. Preserve existing role/owner/currentness checks, exact source sealing, unrelated bytes, Version/time/history handling and standalone apply rejection. Check valid non-Active current, Active current, archived, duplicate-current and ineligible cases. Deliver implementation/test pins and actual results to CA-P-2174. Split before execution if more than 15 minutes is required; no original Core write occurs.

### Completion receipt

[Final independent verification](../../../../_projection/core-entity-review/stage2/tools-first/preview-graph-verification.md), committed at `980ab9371`, passed after duplicate-original and same-path currentness gaps were fixed. Accepted production SHA-256 is `cc67263b7e91650c42e95a7bd933b8af45b03f072176bdfd0e81e7f8391c01e4`; independent fixture SHA-256 is `089c2015dc678f14b036f0eb8cd4a94c749c497604ba2c248f72e30617306a0e`. Concurrent commit `9a40b76e3` captured those exact changes; unrelated release changes are outside this Task's receipt.

Root's complete UPDATE directory passed 49 checks, including 14 new real-validator cases for non-Active originals, unchanged Status/bytes, no-op, archive/Draft/invalid-placement rejection, stale pins, competing/duplicate identities, predecessors, directory symlinks, insertion and same-path identity drift. Lookup still defaults to Active; full source/result validation and the standalone apply guard remain intact. This closes the tested preview increment only. Later intent/materialization changes need fresh verification, and application/combined Tool/live migration gates remain pending.

### Definition of Done

The Plan is **not** Done if independent contract acceptance is missing/stale, a caller remains inconsistent, currentness still requires literal Active, unrelated bytes/Status/guards regress, focused checks fail, or own work exceeds 15 minutes without decomposition.
