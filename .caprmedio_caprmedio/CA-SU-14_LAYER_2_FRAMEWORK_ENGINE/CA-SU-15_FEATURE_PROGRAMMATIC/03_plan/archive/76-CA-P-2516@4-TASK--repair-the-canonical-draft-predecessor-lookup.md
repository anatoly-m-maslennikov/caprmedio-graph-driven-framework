---
atom_id: CA-P-2516@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 76
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 4
updated_at: '2026-10-21T01:18:09Z'
---
# Summary

Repair the canonical Draft predecessor lookup

## Objective

Close the bounded C557 full-release fixture gap without changing production semantics.

## Details

At most15 minutes own work; split before extending. Depends on the current failed full suite finishing and independent diagnosis. Superseding scope: own the confirmed shared Draft-demotion predecessor lookup defect in201_TOOLS/lifecycle_intents.py and one minimal regression in201_TOOLS/tests or existing W04 fixture checks. The failure is production logic, not a fixture migration; do not change fixture expected paths to hide it. Diagnose the nonexistent old Plan archive target and Plan Draft preview declared-versus-observed selected-binding mismatch before changing the fixture. Use canonical actual Plan paths and fresh fixture source bindings after setup mutations. Preserve matrix totals29 applied/eight no-ops/eight refusals; never change production currentness guards, counts or success criteria merely to pass. No production/test source edits while that suite collects results. Acceptance: W04 fixture and complete29/8/8 matrix plus one adjacent selected-workflow check pass; independent review confirms source-currentness refusal and non-Plan paths remain protected. After completion review and update dependent P2513 before a fresh complete normal local release; no waived checks, live corpus fallback, production mutation testing or held/uncertain replay.

### Complete gate result and execution review

The full run local-20261021-mcp-health-verified-env has finished:424 modules,3796 tests,zero skips,six failed modules; launcher integration passed. No install/startup phase ran. Source repair may now begin under the exclusive scope below, followed by independent diff review and fresh focused/full checks. No failed receipt is reused as acceptance.

Read-only diagnosis confirms _publish_status_change hardcodes local/archive after demote_atom_to_draft has already published a Plan predecessor to the canonical shared archived directory. Use the existing canonical predecessor owner where equivalent; avoid unnecessary public API changes or new status modes. Audit all callers of the changed helper and preserve non-Plan paths, exact predecessor bytes, no-op and recovery semantics. The separately masked Plan preview refusal is NOT diagnosed by this Task; new P2517 owns it before any second production change. The earlier fixture-only/rebinding wording is superseded for this confirmed defect. No weakening of currentness guards or29/8/8 totals.

### Source ownership and Problem binding

Active C558 owns this confirmed production caller defect; source implementation reuses the exact _status_predecessor_destination owner already used by publication and binds its result before the effect. The separate masked Plan preview concern is C559/P2517. Old fixture-only task naming is replaced, preserving identityP2516 and the exact predecessor. Await focused regression/W04 fixture/golden receipts and independent source review before Done.

### Verified source completion and next dependency review

The shared caller now obtains the exact publisher-owned predecessor destination before demotion and loads that retained carrier afterward. No public API, non-Plan local history or publication/recovery guard changes. A nested Plan regression asserts the exact independent owning03_plan/archived path and byte-exact predecessor. Independent source/final-test review APPROVE. Worker bounded9 checks pass in37.9s; root fresh broader model-driven lifecycle20/20 passes in38.153s in the actual release virtualenv. The earlier worker interruption is not acceptance evidence; the fresh root run closes that uncertainty. Frozen lifecycle hash8beb32798fdc3f566e0d24382c4dcf7a592e0095e968e1a1d15f1f14caa4865d and regression28813dcbc5ef4f37093afc42066b3cde150ab0e9bc6f948578ad31ee1be1b892. C558 can resolve this bounded source defect. P2513 is reviewed to retain C559/P2517 plus final frozen/full gates as remaining dependencies; no deployed acceptance is claimed.
