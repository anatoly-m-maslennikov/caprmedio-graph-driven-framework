---
atom_id: CA-P-2630@8
content_role: Plan
type: Plan
label: Task
work_sequence_number: 17
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
version: 8
updated_at: 2026-10-24 13:39:34 +0400
subjects:
  governs: Subject/Engineering/Journal Operations
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2613
  depends_on:
  - CA-P-2623
  - CA-P-2629
  - CA-P-2631
  - CA-C-585
  - CA-C-586
  relates_to:
  - CA-O-016
  - CA-O-011
  - CA-R-1317
  - CA-O-007
  - CA-O-155
  - CA-O-156
  - CA-C-583
  - CA-R-1840
  - CA-R-1841
  - CA-R-1842
  - CA-E-561
  - CA-E-562
  - CA-D-541
  - CA-D-542
tier: 3
---
# Summary

Define the compiler admitted-evidence contract

## Objective

Define the smallest compiler implementation contract that consumes existing
admitted OperatorDecision, Run and effect evidence, while treating Journal
recording as non-blocking for methodology approvals and recovery. The contract
must not accept an authoritative approval flag supplied by the caller.

## Details

This is one bounded contract-design Task with at most 15 minutes of own work,
to activate after CA-P-2629's R1317 source alignment and CA-P-2631's seven
contract reconciliation are independently reviewed. CA-C-586 is an explicit
design hold: the Operator must decide whether O011 obtains the actual
OperatorDecision through the existing interactive MCP loop or whether the
integration gap is deferred and reported. Identify the existing evidence
carriers and current compiler callers only after that decision, preserve result
shapes, partial results, retry accounting, recording_error handling and
no-replay behavior, and separate business Journal append from technical
diagnostics. Do not invent a new input schema, authoritative caller flag,
trusted-evidence contract or runtime behavior in this planning record.
Failed-publication recovery evidence remains separately unresolved until its
current source is adjudicated.

## Definition of Done

Return a source-bound contract proposal naming the admitted evidence fields,
their owner and freshness checks, the caller-visible failure/partial-result
behavior and focused regression boundaries. The proposal must reject a
caller-authoritative approval flag and must not claim CA-C-583 resolved or
runtime/compiler implementation complete. Activate only after CA-C-586 is
answered and CA-P-2629 and CA-P-2631 are reviewed.

## Dependency checkpoint — 23 October 2026

CA-P-2629's four-carrier methodology source package and CA-P-2631's
compiler/shared-run RMED source package are independently reviewed and Done at
99% or higher; CA-P-2632 records the completed identity-safe source
replacement and consumer rebind. This Task remains Backlog because the
Operator's CA-C-586 decision about O011 interactive OperatorDecision
acquisition remains open and compiler implementation has not started. No
compiler contract, caller-authoritative approval flag, source mutation,
binding change or runtime admission is implied.
