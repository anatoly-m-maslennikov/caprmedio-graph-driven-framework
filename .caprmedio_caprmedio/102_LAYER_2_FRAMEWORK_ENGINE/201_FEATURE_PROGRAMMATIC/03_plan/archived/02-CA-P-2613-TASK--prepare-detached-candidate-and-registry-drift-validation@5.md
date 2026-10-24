---
atom_id: CA-P-2613
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
version: 5
updated_at: "2026-10-23T00:44:56+0400"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2582]
  depends_on: [CA-P-2611, CA-P-2612]
  relates_to: [CA-O-016, CA-A-1142, CA-W-09, CA-C-583, CA-C-584]
---
# Summary

Prepare the detached candidate and registry-drift validation

## Objective

Build a detached candidate from the reviewed source package and validate its
registry/frontier drift before any publication decision. Explicitly account
for A1142 and the W09 old-frontier registry entry; keep the candidate separate
from the actual Project binding.

## Details

At most 15 minutes of own work; one Task per file. Start only after CA-P-2611
is accepted and CA-P-2612 supplies the reviewed source pins. Preserve the
frozen oracle, installed O016@13/CA-O-091 binding, candidate hashes and
current Project identity. Validate candidate graph/source consistency,
connected exceptions and registry drift; report conflicts instead of
repointing the live projection. No actual Project binding write, production
MCP traffic, runtime admission, release, deployment, replay or full-suite
run.

## Definition of Done

Produce a detached candidate plus a bounded validation report showing whether
the reviewed source package can replace the old frontier, including the A1142
/ W09 registry issue. Publication remains a separate reviewed gate and the
visible Project binding stays unchanged.

### Deferred leaf checkpoint — 22 October 2026

Keep this detached-candidate and registry-drift leaf Backlog until CA-P-2612's source package is reviewed. Preserve A1142/W09 as candidate validation concerns and do not repoint the actual Project binding.

### Review-scope decision checkpoint — 23 October 2026

Keep this detached-candidate and registry-drift leaf Backlog. The source package is accepted, but execution awaits the Operator's choice between reviewing all 15 non-target route pins plus both query admissions and retaining the focused hold. Preserve the existing mechanical report, A1142/W09 historical distinction and visible Project binding; do not emit or admit a candidate.

### Human review-scope authorization — 23 October 2026

The Operator authorized review of all 15 non-target route pins plus both query admissions before any publication decision. This remains a zero-own-work review container: six read-only leaves CA-P-2614 through CA-P-2619 are Active and mapped to the authorized lanes below. They record mechanical drift only; they do not emit or admit a candidate, alter A1142, mutate the visible Project binding or start implementation. Keep this container Active until the root receives all lane results and explicitly activates closure.

Lane allocation: lifecycle 5 route pins; Scope Units 4; graph builders 2; applicable methodology 1; revert 1; query routes 2 plus both query-admission definitions. The route-pin total is 15; query-admission leaf counts remain a separate mechanical inventory. Scope Unit implementation remains deferred to Stage 2.

## Semantic binding-review checkpoint — 23 October 2026

All six authorized read-only review lanes are complete. CA-P-2614 through
CA-P-2619 are Done as review-complete records, not implementation or admission
claims. The aggregate result is 8 route/contract PASS findings and 7
binding-closure HOLD findings.

CA-P-2614 records create/update PASS, replace/status HOLD for the declared
O031/O029 Journal receipt qualifiers, lifecycle-graph PASS and optional
move_atom admission HOLD. CA-P-2615 records current Project O015@12 authority
and graph PASS; Scope Unit implementation remains Stage 2. CA-P-2616 records
graph-structure PASS but a Journal-receipt semantic HOLD for O133/O138 and
related routes. CA-P-2617 records the compiler/approval Journal semantic HOLD.
CA-P-2618 records the O130/O131 Journal/start-terminal semantic HOLD.
CA-P-2619 records current query/admission PASS while the optional move contract
remains open.

The findings are represented by new Active Problems CA-C-583 (Journal
receipt/completion semantics against R1525@11, R1720@22 and D340@17) and
CA-C-584 (the exact 15-operation MCP contract versus optional move_atom).
The two remaining candidate-only leaves CA-P-2620 and CA-P-2621 are Backlog,
each bounded to 15 minutes and conditional on those Problems being resolved or
explicitly accepted. P2613 remains Active; no candidate emission, A1142 edit,
live binding mutation, runtime admission, Scope Unit implementation, replay,
release or deployment occurred.
