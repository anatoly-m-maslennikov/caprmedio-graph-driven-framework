---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/State Ownership
  depends_on: []
version: 16
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-M-408
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-358
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
tier: 5
type: Eval Case
---
# Reject I/O during object construction

## Claim checked

one PROGRAMMATIC object is constructed **without** acquiring resources **or** applying
external effects.

## Test case

construct one object while its declared resource boundary is unavailable **and**
observe whether construction attempts filesystem, process, network,
persistence, **or** logging-export I/O.

## Acceptance criteria

pass **only** **when** construction completes **without** I/O **and** acquisition begins **only**
through a specifically named explicit method.

## Failure disposition

reject the object lifecycle **until** acquisition is removed from construction.

## Sources

- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-STANDARD-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)
