---
atom_id: CA-P-2516
content_role: Plan
type: Plan
label: Task
work_sequence_number: 76
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 3
updated_at: "2026-10-21T01:11:01Z"
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
