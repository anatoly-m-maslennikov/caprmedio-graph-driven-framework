---
atom_id: CA-P-2613@18
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
version: 18
updated_at: 2026-10-23T13:38:56+0400
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2582
  depends_on:
  - CA-P-2611
  - CA-P-2612
  relates_to:
  - CA-O-016
  - CA-A-1142
  - CA-W-09
  - CA-C-583
  - CA-C-584
  - CA-C-585
  - CA-C-586
  - CA-C-587
  - CA-P-2629
  - CA-P-2630
  - CA-P-2631
  - CA-P-2632
  - CA-P-2633
  - CA-P-2634
  - CA-P-2635
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

## Bounded repair planning queue — 23 October 2026

The following records are bounded read-only planning lanes. They do not emit
or admit a candidate and do not alter source, code, binding or runtime state.

| Plan | Owner lane | Exclusive scope | Depends on | Status |
| --- | --- | --- | --- | --- |
| CA-P-2622 | source-proposal lane | generic-six C583 clause-to-Core review | CA-C-583 | Done |
| CA-P-2623 | compiler-preparation lane | compiler/refactor boundary and compatibility map | CA-P-2622, CA-C-583 | Active |
| CA-P-2624 | compiler-regression lane | separate focused regression plan | CA-P-2623, CA-C-583 | Backlog |
| CA-P-2625 | fresh-inventory lane | public MCP versus Project/code frontier inventory | CA-C-584 | Active |
| CA-P-2626 | frontier-review lane | C584 reconciliation proposal | CA-P-2625, CA-C-584 | Active |

CA-P-2620 and CA-P-2621 remain Backlog and conditional on actual CA-C-583 and
CA-C-584 disposition. The protected R1847, R1848, D547, E567, E568 and A1142
carriers, the visible Project binding and O188 remain untouched.

## Current O016@20 compatibility checkpoint — 23 October 2026

The fresh inventory reports current O016@20 with body bytes unchanged from the
exact O016@18 archive. Add two bounded lanes without broadening the frontier:
CA-P-2627 is Done for candidate-only current-20 compatibility/admission
preparation, and CA-P-2628 is Done for focused isolated current-20 tests.
Both are owned by the journal_compiler_repair lane, depend on verified body
equivalence, and preserve exact legacy-17/direct-18 implementation support.
They must not imply support for every version greater than 18, change the
public 15-operation route, or mutate the live Project manifest or binding.

## Current O016@20 compatibility lanes — 23 October 2026

CA-P-2627 and CA-P-2628 are Done under the journal_compiler_repair lane.
They depend on verified O016@20 body equivalence with the exact @18 archive,
preserve exact legacy-17/direct-18 implementation support and must not broaden
the frontier to every version greater than 18. CA-P-2627 owns candidate-only
compatibility/admission preparation; CA-P-2628 owns focused isolated tests.
Neither lane changes the public 15-operation route, live 16-operation Project
manifest, visible binding, runtime or publication state.

## R1317 Journal-boundary decision and follow-up lanes — 23 October 2026

The Operator resolved CA-C-585: Journal recording is non-blocking for
methodology approvals and recovery; actual OperatorDecision and independent
Run/effect evidence remain required. CA-P-2629 is Done for the bounded
source alignment of R1317, O007, O155 and O156. CA-P-2630 is Backlog for the
dependent compiler admitted-evidence contract; it must consume existing
source-bound evidence and must not accept an authoritative caller approval
flag. CA-P-2623 is updated with this decision, while CA-C-583 remains Active
for the remaining R1317/O007/O155/O156 source alignment and compiler
implementation gap. No runtime, binding,
publication, release or deployment state changes follow from this checkpoint.

CA-P-2631 is Done for the separate compiler_rmed_reconciliation lane over
R1840, R1841, R1842, E561, E562, D541 and D542. CA-P-2630 remains Backlog
although CA-P-2629 and CA-P-2631 are independently reviewed; its contract
must consume existing admitted evidence and must not accept a caller-
authoritative approval flag.

The bounded generic-six review in CA-P-2622 passed at 99% or higher for
O130@9, O131@9, O133@9, O134@9, O136@9 and O137@9, with exact source hashes
retained in that Task. It found no generic Journal gate, duplicate or
graph-alias issue. This closes only that review sub-deliverable; CA-C-583
remains Active for the R1317/O007/O155/O156 source alignment and the compiler
implementation gap.

## O011 decision hold — 23 October 2026

CA-C-586 records the still-open Operator question whether O011 should reuse
the interactive MCP loop to obtain the actual OperatorDecision while retaining
independent Run/effect evidence, or defer and report that integration gap.
CA-P-2630 remains Backlog until this question is answered; no trusted-evidence
or public decision-reference contract is admitted by this plan. The
Journal-boundary resolution in CA-C-585 remains unchanged and does not create
a generic Journal gate.
## Methodology review and Engine identity-safe planning — 23 October 2026

CA-P-2629 is Done after independent review of the current CA-R-1317@18,
CA-O-007@14, CA-O-155@10 and CA-O-156@11 carriers at 99% or higher. The
accepted hashes and non-blocking Journal boundary are retained in that Task;
actual OperatorDecision and independent Run/effect evidence remain required.

CA-P-2630 remains Backlog because compiler implementation is not started and
CA-C-586 remains an open Operator choice about O011 interactive OperatorDecision
acquisition.

CA-P-2632 is Done as a bounded child of CA-P-2631: the writer archived
CA-R-1841@2, created collision-checked CA-R-2118@1 and rebound the reviewed
Engine consumers. The exact mapping and hashes are in CA-P-2632 and its
business Journal event; no formal replacement relation, runtime admission,
binding publication, release or deployment is claimed.

## Superseding source and test checkpoint — 23 October 2026

CA-P-2627 and CA-P-2628 are Done: independent Terra review found no findings,
34 code-admission/focused checks passed with Ruff and strict Mypy, and two
separate Root registration checks passed in 6.649 seconds. The current O016@20
candidate remained detached from the live binding. CA-P-2629, CA-P-2631 and
CA-P-2632 are Done for their reviewed source packages and the identity-safe
R1841-to-R2118 source replacement. CA-P-2630 remains Backlog because the
compiler contract/implementation is still held by CA-C-586; CA-C-583's final
O029/O031 helper-contract source reconciliation is complete and its remaining
implementation gap is tracked separately.

CA-C-587 is Active for the measured cold-start test-budget mismatch: the
legacy fixture/discovery budget is 30 seconds, Gateway readiness is 90
seconds, and the disposable bounded harness is 120 seconds. CA-P-2633 is
Active execution: the worker reduced the observed 305 source lines to 200
and added a 200-line support helper; focused checks and independent review
remain pending. CA-P-2634 is Active execution: the worker aligned the
bounded test startup/readiness boundary to 120 seconds while leaving
production Gateway90 unchanged; focused checks remain pending and final
acceptance follows CA-P-2633 review. CA-P-2635 is Done for the final
O029@13/O031@9 successor review, with exact source pins retained there. The
compiler implementation gap remains separate.

The final current-source inventory is now verified 50/50 with stable reads at
09:25:19Z and 09:25:22Z. The retained evidence artifacts are:

- execution_evidence/p2613/current-source-pins.post-reconciliation-20261023.json
  — SHA-256 f0acd20b450b056f61312eb560cd1c742d6fd0cf9a8972de8dfd41db7bf6ed8f.
- execution_evidence/p2613/source-review-verification.post-reconciliation-20261023.json
  — SHA-256 b7a98738e69ea2e982eae089fd965acf5fba2eb12c95ab7e8e4a9cabd938a348.
- execution_evidence/p2613/binding-drift-report.post-reconciliation-20261023.md
  — SHA-256 871ee20e4b9e79398590f7652973a9543764b76f366154c53f34a39b0ae27b19.

This is a source/inventory checkpoint, not live binding publication, runtime
admission, release, deployment or full-suite evidence. CA-P-2633 and
CA-P-2634 are now Done for their bounded working-tree changes, focused checks
and independent review. CA-C-587 is Resolved only for the finite disposable
test-harness readiness mismatch. The sanitized ValueError/source-drift
hypothesis remains separate and unproven.

## Bounded stdio harness closure — 23 October 2026

CA-P-2633 completed the refactor from the observed 305 source lines to 200
and added a 199-line support helper. Twelve focused stdio/telemetry checks
passed in 117.937 seconds. CA-P-2634 then aligned disposable startup/readiness
to 120 seconds; five focused hot-reload readiness/telemetry checks passed in
20.556 seconds. Ruff, strict Mypy, AST-diff verification and independent
review passed after the RMED ownership-header correction. Production Gateway
readiness remains 90 seconds, CA-C-586 remains open, and no compiler behavior,
live binding, runtime admission, release, deployment or full-suite state
changed.
