---
atom_id: CA-P-2365
content_role: Plan
type: Plan
label: Task
work_sequence_number: 43
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
updated_at: "2026-10-14 00:31:50 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Replace native Subject dependencies by value

## Objective

Remove the Subjects-only migration blocker: native depends_on replacement selects the exact supplied old Subject value and rejects caller-supplied index selectors, as required by accepted O030 v15/D425.

## Details

Own only atom_subject_patch.py, atom_operations.py's Describe path and affected Subject author fixtures, under Root-assigned exclusive ownership. Replace the native _plan_patch dependency-selection requirement for a caller index with exact old-value selection. Refuse absent or ambiguous old values and every caller-supplied index rather than silently accepting or ignoring it. Preserve privately computed index/node spans for precise carrier edits and keep Describe/request guidance consistent with the by-value public boundary. Preserve existing governs replacement, exact expected-old-value checks, notation/schema validation, sealed preview/currentness, authorization, publication/history/effect and rollback gates. Reuse the existing Subject publication path; no second writer or semantic policy change.

Estimated own work: up to 15 minutes; split before exceeding this bound. Root owns Plans/Git and assigns disjoint production/author-test and independent-test ownership. You are not alone; preserve unrelated edits. This is only necessary Subject-migration support. New add/remove/full-set capabilities, ordinary content edits, YAML Type catalog, broader connector rebuild, Draft work, new routes and live migration are excluded; expand only if Root binds a necessary already-approved migration packet.

### Definition of Done

Actual native fixtures prove unique exact-old-value depends_on replacement without a caller index, precise intended-span changes and preserved unrelated carrier bytes. Caller index, missing/ambiguous old value, stale expected state and invalid Subject input refuse safely; exact no-op remains unchanged. Describe no longer instructs callers to select Subject list entries by index. Existing Subjects-only preview/admission/publication/currentness/authorization/history/recovery gates and affected Subject regressions remain intact. Deliver exact final source/code/test pins and executed checks for independent P2366 acceptance; preparation or mock-only success is insufficient. No live Subject effect or broader capability is accepted by this bounded fix.
