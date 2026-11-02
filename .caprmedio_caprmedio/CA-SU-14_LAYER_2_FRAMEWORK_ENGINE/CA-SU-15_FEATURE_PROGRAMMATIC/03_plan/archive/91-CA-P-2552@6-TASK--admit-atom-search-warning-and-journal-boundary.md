---
atom_id: CA-P-2552@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 91
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Runtime Failure Classification
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 6
updated_at: 2026-10-24 10:35:14 +0400
tier: 3
---
# Summary

Admit the AtomSearch warning and Journal boundary

## Objective

Reconcile the Operator's warning disposition for individual schema-invalid Atoms
with the active ATOM_SEARCH, diagnostic-logging, and query-Journal authorities,
then obtain bounded implementation and focused proof without claiming deployment
or release conformance. The technical sink decision is now resolved: Docker
`stderr`, a validated Project prefix from settings, and Docker local rotation
`max-size=10m`/`max-file=3`; the business Journal remains business-only.

## Details

At most 15 minutes own work per child; split before extending. CA-C-572 remains the
active source problem. An isolated schema-invalid Atom may be skipped with a
technical warning containing path and reason while a bounded scan continues with
`complete: false`; fatal I/O, security, duplicate-identity, stale, ambiguous, or
incomplete-frontier conditions remain refusal/error. Technical warnings go to
Docker `stderr` as structured records with the validated Project prefix from the
existing bound Project selection and canonical prefix-field validation, and are not
business Journal records. Reuse CA-M-163, CA-D-396, CA-D-504 and CA-D-559 as
logger authorities; do not create `.caprmedio_runtime/logs/`. Docker local
rotation is bounded to `max-size=10m` and `max-file=3`, with
`mode=non-blocking` and `max-buffer-size=1m`; new technical messages may be
dropped when full so the primary operation cannot stall. Docker logs are removed
with the container. This uses the selected immutable settings view and does not
claim full SettingsReader conformance or add a settings carrier. Preserve
historical Journal bytes and the existing actual-query Run/Journal route. Root
owns code, tests, Git, Docker, runtime, and any release or deployment effect.

### Bounded decomposition

- CA-P-2553 is Done for the implementation/contract increment after the focused
  AtomSearch check (94 tests, no skips).
- CA-P-2554 is Done for the dependent focused proof; it preserves the
  source/test-only and no-deployment boundary.
- CA-P-2555 is Done at the source/configuration/focused-evidence boundary and
  remains explicitly separate from new-image and deployment acceptance.

This plan does not modify the frozen local-release carriers CA-R-1878, CA-M-332 or
CA-E-573, does not close CA-P-2536 or CA-P-2401, and does not claim the focused
tests as installed-runtime or deployment proof.

### Definition of Done

The children provide exact source/test evidence for warning path/reason,
`complete: false`, no mutation, preserved Journal history, and fatal-class
refusal. The logger boundary is reconciled by the selected Docker policy. The
completed children record 94 AtomSearch tests with no skips, ten MCP protocol
tests in 3.990 seconds, four Docker logging checks plus 21 related checks, and an
isolated source-mounted Docker inspection covering two Project prefixes,
redaction, non-blocking rotation and no Atom contents. This Task remains Active
for the new-image/deployment/readiness boundary; its children are Done for the
bounded source/configuration/evidence scope, while CA-C-572 remains visible and
active.
