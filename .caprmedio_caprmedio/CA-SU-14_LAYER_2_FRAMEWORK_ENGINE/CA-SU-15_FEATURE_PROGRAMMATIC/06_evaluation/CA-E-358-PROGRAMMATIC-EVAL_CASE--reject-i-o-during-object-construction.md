---
atom_id: CA-E-358
ref_id: CA-E-358
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component Structure"
tier: 5
relations:
  evaluation_for:
  - CA-M-408
  derived_from:
  - CA-A-053
status: Active
version: 23
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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

- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)
