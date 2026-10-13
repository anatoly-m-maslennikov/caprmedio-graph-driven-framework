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
status: Done
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Plan]
version: 2
updated_at: "2026-10-14 00:40:32 +0400"
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

### Accepted bounded outcome

The bounded native by-value replacement and Describe correction is accepted on frozen code. Exact unique old values select dependencies; caller indices, missing/ambiguous old values and invalid/stale input refuse. Private computed index/spans, intended-byte changes, unrelated carrier bytes and no-op behavior are retained. Accepted source pins are O030 v15 SHA-256 `a53bf60a93f9afff6da80f9d657009bb294420d8b2bf98eb6ab36c6895fb0dd1` and D425 v15 `2f332c1d1c1dc9e6d41d81b739eb3ee7f5fd20ca7ffdd46a6d7cf6f01fdcf7d4`.

Received final evidence: 87 author native/dispatch checks PASS; 9 independent tests/37 subtests PASS; independent frozen-code review PASS. Reopened production SHA-256 pins match acceptance: atom_subject_patch.py `272c174c4e66c679a6a1c059d710b0b368094330b9bd9478d2d44a588629369c`; atom_operations.py `0f38c6a27646af6003d3984c330763f83bd0c40360b2ffb955069ed6134b3315`. Independent test_subject_patch_by_value_independent.py SHA-256: `c76e2e7d6ae1a37c042bfe42f82cb5f7677dfa2196c03497e006ff49c3be89a2`. Native preparation/materialization/staging and dispatch checks plus code review establish this selector correction without weakening existing Subjects-only gates.

The selected suite has 39 setup errors from stale O127 fixture pins and is explicitly excluded, not counted as a pass or live readiness. This closure accepts only the bounded native migration blocker; broader Subject migration/Epic, selected execution/runtime readiness and other unfinished descendants remain Active. No live Subject effect, source policy, new add/remove/full-set capability, Draft or catalog work is accepted here.
