---
atom_id: CA-P-2436@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 25
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 2
updated_at: '2026-10-20T12:55:50.000Z'
---
# Summary

Reconcile Plan Draft placement authority

## Objective

Complete one bounded Epic CA-P-2401 responsibility with truthful source, fixture and runtime evidence.

## Details

Align only D461 production locator/version/hash and exact frozen validator bytes to current v13 after Claim comparison; ensure Plan Draft placement under draft is supported and wrong/unknown placement is diagnosed, not a KeyError. No new strict manifest gate. Add focused frozen positive and negative checks; preserve unchanged status behavior.

Use the PROGRAMMATIC M projection. At most15minutes own work; split dependent Tasks before extending. Preserve concurrent edits, exact predecessors and selected uv-managed environment. Review/update dependent Task before execution.

### Definition of Done

Bounded deliverable and reproducible checks are recorded, with runtime effects and limitations explicit.

### Completion checkpoint

Accepted source/test deliverable completed: the D461 pin and exact frozen v13 payload are bound to SHA-256 `d0d938144a99f273b96c53afd630b12480a6b2af5f05e2396ba03d91156a7f1d`; Draft maps to `draft`, and unknown placement is diagnosed without `KeyError`. Frozen R1539 graph v9 and captured R1947/status index align direct consumers; the deliberate legacy v6 fixture is retained. Checks covered affected modules12+3+15, inherited5, structure33, graph29, current semantics5, integration6, plus compile/JSON/exact-source comparisons. Existing E402/Ruff is baseline only. No Docker/MCP/full-final-suite claim is made.
