---
atom_id: CA-R-1612
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection/(.Form:=Realization Graph)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Verification
version: 26
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1612-PROJECT_CONFIGURATION-RULE--allow-pre-runtime-pass-only-with-sufficient-evidence.md
  source_atom_id: CA-R-1612
  source_atom_revision: 26
  source_sha256: da9e1108ca7cdc743f76edffd6425fa1a646b760f3b20229337779a59233de62
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Allow pre-runtime pass only with sufficient evidence

## Claim scope

Evaluations using a Realization Graph before runtime, for their declared input boundary.

## Claim

an Evaluation using a Realization Graph **may** return `pass` **before** runtime **only** **when** sufficient evidence establishes the checked Claim for the declared input boundary.

- **if** the Claim requires complete coverage of particular Relation mechanisms, the evidence **must** establish that coverage; a completeness declaration alone is insufficient.
- the evidence **must** establish the actual acceptance condition. complete provenance **or** graph coverage does **not** itself establish that condition.
- a possible inferred Relation is **not** an observed occurrence. **when** required runtime evidence is unavailable **or** a material condition remains unresolved, the Evaluation **must not** return a pre-runtime `pass`.

this Claim constrains permission **to** report a result; the applicable E Atoms supply the checks. it does **not** require complete graph coverage for a Claim that needs **only** bounded evidence.
