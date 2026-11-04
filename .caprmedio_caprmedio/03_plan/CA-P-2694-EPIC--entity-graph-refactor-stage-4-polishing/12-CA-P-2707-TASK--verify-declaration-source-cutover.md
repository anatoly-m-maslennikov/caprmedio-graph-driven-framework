---
atom_id: CA-P-2707
role: Plan
form: Plan
label: Task
status: Active
version: 4
updated_at: 2026-11-04 09:32:27 +0400
tier: 4
current_scope_unit: caprmedio
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit
relations:
  IS_CONTAINED_BY:
  - CA-P-2694
author: Anatoly Maslennikov
---
## Summary

Verify the Declaration source cutover

## Objective

Verify the final Current Declaration sources, their consumers and carrier admission. Pass the complete suite, launcher and required Docker checks before Epic completion.

## Recorded evidence

- Earlier cutover evidence reported 44 Scope Unit Declarations, 43 non-root IDs and nine Ordered units. Recheck those counts and identities on the final candidate.
- The live project_structure.toml was retired. Recheck production, bindings, fixtures and documentation for executable dependencies.
- Current D657 replaces retired D274 as live carrier-encoding authority. Its reviewed Claim digest, registry closure and 588 validator tests are recorded in the completion packet.
- The latest reader passed 426 graph tests. Seven MODEL views use Project root ownership and Form + Scope Unit identity.
- Connector and moved-default fixture corrections passed 48 focused tests.
- Earlier whole-suite runs contained concurrent edits and failures. They do not establish a final pass.

## Remaining checks

1. Verify final Declaration counts, identities, derived paths and source hashes. Explain each digest change from preserved source evidence.
2. Close the legacy scope-field disposition and any missing Current execution bindings. A retired carrier is not a Current replacement.
3. Verify live Project admission and fresh Docker query/status and lifecycle checks, including the W10 result/timestamp comparison.
4. Run the complete current-source suite and launcher on a stable candidate. Record the exact implementation, source and image identities, results and cleanup.
5. Preserve the explicit O016 expected-failure disposition under P2708. It does not waive unrelated failures.

## Status

Active. Focused tests and source adoption receipts do not close this gate. No release is required.

## Evidence

- [Integration packet](../../02_analysis/draft/epic-completion-20261104/integration/REPORT.md).
- [Full acceptance matrix](../../02_analysis/draft/epic-completion-20261104/acceptance/matrix.json).
- [Earlier cutover verification](scope-unit-governance-20261031/verification/final-cutover-verification.json).
