---
atom_id: CA-P-2707
role: Plan
form: Plan
label: Task
status: Active
version: 5
updated_at: 2026-11-04 14:56:07 +0400
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit
relations:
  IS_CONTAINED_BY:
    atom: CA-P-2694
carrier_destination:
  file:
    name: 12-CA-P-2707-TASK--verify-declaration-source-cutover.md
    path: .caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing
---
## Summary

Verify the Declaration source cutover

## Objective

Verify the final Current Declaration sources and their source consumers. Reconcile source-side authority and identity before carrier admission. CA #3 owns engine implementation/runtime changes, fixtures, regression work and execution of carrier-admission, complete-suite, launcher, Docker and lifecycle checks. Those remain required external dependencies before P2707 or the Epic can be Done.

## Recorded evidence

- Earlier cutover evidence reported 44 Scope Unit Declarations, 43 non-root IDs and nine Ordered units. Recheck those counts and identities on the final candidate.
- The live project_structure.toml was retired. Recheck production, bindings, fixtures and documentation for executable dependencies.
- Current D657 replaces retired D274 as live carrier-encoding authority. Its reviewed Claim digest, registry closure and 588 validator tests are recorded in the completion packet.
- The latest reader passed 426 graph tests. Seven MODEL views use Project root ownership and Form + Scope Unit identity.
- Connector and moved-default fixture corrections passed 48 focused tests.
- Earlier whole-suite runs contained concurrent edits and failures. They do not establish a final pass.

## Remaining checks

1. The source lane verifies final Declaration counts, identities, derived paths and source hashes. Explain every digest change from preserved source evidence.
2. Reconcile the legacy scope-field disposition from Current authority and identify a valid Current execution binding for every required operation. CA #3 owns matching implementation, registry/fixture changes and tests; a retired or archived carrier is not a Current replacement. The missing actual CA-O-104 Review Workflow remains a distinct source-authority issue and cannot be filled by a projection or installed copy.
3. CA #3 verifies live Project admission and fresh Docker query/status and lifecycle checks, including the W10 result/timestamp comparison, on the stable candidate.
4. CA #3 runs the complete current-source suite and launcher on that same stable candidate. Record exact implementation, source and image identities, results and cleanup. These checks remain pending until an actual terminal result is recorded; focused or mixed-state runs do not satisfy them.
5. Preserve the explicit O016 expected-failure disposition under P2708. It does not waive unrelated failures. Actual Workflow-instance migration remains separately deferred; do not conflate it with the missing CA-O-104 source or with the settled Occurrent kind decisions.

## Status

Active. Focused tests and source adoption receipts do not close this gate. No release is required.

## Evidence

- [Integration packet](../../02_analysis/draft/epic-completion-20261104/integration/REPORT.md).
- [Full acceptance matrix](../../02_analysis/draft/epic-completion-20261104/acceptance/matrix.json).
- [Earlier cutover verification](scope-unit-governance-20261031/verification/final-cutover-verification.json).
