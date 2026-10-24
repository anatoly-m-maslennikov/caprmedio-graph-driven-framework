# Semantic binding review — P2613

Generated: 2026-10-23T00:51:57+0400
Scope: CA-P-2613 all-route binding and query-admission review
Authority: CA-C-576, CA-R-1525@11, CA-R-1720@22, CA-D-340@17
Disposition: review evidence only; no publication or live binding mutation

## Result

The six authorized lanes are complete as review records. The aggregate is 8
PASS findings and 7 binding-closure HOLD findings. PASS/HOLD describes the
reviewed route or contract semantics; it is not runtime admission, deployment
readiness or a release result.

| Task | Scope | Verdict | Review-complete status |
| --- | --- | --- | --- |
| CA-P-2614 | lifecycle, 5 pins | create/update PASS; replace/status semantic HOLD; lifecycle graph PASS; public move contract HOLD | Done |
| CA-P-2615 | Scope Units, 4 pins | current Project authority/graph PASS; Stage 2 implementation deferred | Done |
| CA-P-2616 | graph builders, 2 pins | graph structure PASS; Journal receipt/completion semantic HOLD | Done |
| CA-P-2617 | applicable methodology, 1 pin | graph compatibility PASS; Journal approval/recovery semantic HOLD | Done |
| CA-P-2618 | revert, 1 pin | exact old pins recovered; Journal start/terminal semantic HOLD | Done |
| CA-P-2619 | query routes, 2 pins + both admissions | current source and query admissions PASS; public move contract remains open | Done |

## Confirmed semantic findings

### CA-C-583 — Journal receipt/completion reconciliation

The current source contains definite clauses requiring reconciliation, not merely a
generic question. O130 line 44 treats an unconfirmed Workflow Journal start
as blocking dispatch; O131 line 55 applies a Journal-confirmation gate; O133
and O136 line 39 make an absent receipt prevent a Run from completing; and
O134/O137 lines 40, 42 and 46-48 contain recording blockers or completion
gates. compile_applicable_methodology.py lines 1235-1275 constructs Approval
from a Journal row and digest, while lines 1177-1180 and 1211-1232 use a
failed Publication Journal record for recovery.

R1525@11, R1720@22 and D340@17 explicitly provide no Journal permission,
proof, recording, completion or recovery gate. The actual business Journal
append obligation remains valid, including O051, which is not part of this
Problem's gate claim. O007/O155/O156 provide affected approval-source
context; mandatory logging alone is not a proof gate. Independently admitted
Run-state and Operator-Decision evidence remain distinct from Journal
receipts. O029/O031 are declared helper contracts, not proof that generic
status implementation is actually blocked. No deployed runtime outage is
claimed.

### CA-C-584 — Public MCP declarations versus Project/code frontier

R1847@16 lines 37-42 defines the exact 15-operation MCP route set and omits
move_atom. E567@7 lines 25, 36 and 40 also expects 15. The canonical Project
manifest contains 16 operations including move_atom; selected_route_spec.py
line 33 permits OPTIONAL_SELECTED_ROUTE_NAMES; and O127 supports Move.
The mismatch is between public MCP declarations and the canonical
Project/implementation frontier. It is not correct to say that R1847@16
includes move_atom, and the 15-operation source must not be relabeled as a
16-operation contract.

## Mechanical and authority evidence

- Root source revalidation: 50/50 pins, changed = none.
- Project/Engine/A1142/R1525/R1720/D340 baseline hashes remained unchanged.
- In-memory O016@18 candidate remains separate from the visible binding.
- The raw Project manifest does not resolve the retired O091 locator to exactly
  one current Carrier; this is not evidence of two active O091 carriers.
- The earlier graph finding about accepting tampered old pins was withdrawn.
- O051 cardinality and the native Archive-helper observations were retracted as
  capability contradictions; no Problem was created for them.
- Scope Unit implementation remains deferred to Stage 2.

## Remaining candidate-only work

CA-P-2613 remains Active. CA-P-2620 (registry/authority requalification) and
CA-P-2621 (detached candidate compilation) are Backlog, each bounded to 15
minutes and conditional on CA-C-583 and CA-C-584 being resolved or explicitly
accepted. No source fix, A1142 edit, candidate emission, live binding write,
runtime admission, release, deployment, replay or full-suite run is claimed.

### Candidate-direction checkpoint — 23 October 2026

The detached candidate direction is to omit optional move_atom while
preserving the optional implementation capability. O127's internal Move does
not admit a public MCP route. The live Project manifest remains at 16
operations and is untouched; CA-C-584 remains Active until this direction is
validated by a later correction. This checkpoint does not retire Move, repair
the manifest, publish a candidate or claim runtime admission.
