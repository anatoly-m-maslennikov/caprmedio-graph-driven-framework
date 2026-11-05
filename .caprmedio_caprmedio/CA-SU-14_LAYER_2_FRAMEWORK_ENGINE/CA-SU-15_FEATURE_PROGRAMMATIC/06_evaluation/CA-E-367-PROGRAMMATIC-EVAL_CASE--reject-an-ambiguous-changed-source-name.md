---
atom_id: CA-E-367
ref_id: CA-E-367
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring
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
# Reject an ambiguous changed source name

## Claim checked

one new **or** materially changed source unit has a specific,
intention-revealing name that states one responsibility.

## Test case

evaluate one changed class named `Manager` **without** a qualifying project term **or**
owned responsibility.

## Acceptance criteria

pass **only** **when** the class is rejected **until** its name identifies the exact
responsibility it owns.

## Failure disposition

block the changed unit from claiming naming conformance.

## Sources

- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)
