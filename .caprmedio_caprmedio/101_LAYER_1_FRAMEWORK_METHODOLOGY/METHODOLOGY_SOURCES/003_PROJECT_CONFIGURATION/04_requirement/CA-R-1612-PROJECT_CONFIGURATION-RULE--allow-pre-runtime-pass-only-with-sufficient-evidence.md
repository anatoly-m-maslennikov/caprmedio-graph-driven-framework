---
atom_id: CA-R-1612
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Realization Graph'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
version: 18
updated_at: 2026-10-27 19:59:59 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Allow pre-runtime pass only with sufficient evidence

## Scope

Evaluations using a Realization Graph before runtime, for their declared input boundary.

## Claim

an Evaluation using a Realization Graph **may** return `pass` **before** runtime **only** **when** sufficient evidence establishes the checked Claim for the declared input boundary.

- **if** the Claim requires complete coverage of particular Relation mechanisms, the evidence **must** establish that coverage; a completeness declaration alone is insufficient.
- the evidence **must** establish the actual acceptance condition. complete provenance **or** graph coverage does **not** itself establish that condition.
- a possible inferred Relation is **not** an observed occurrence. **when** required runtime evidence is unavailable **or** a material condition remains unresolved, the Evaluation **must not** return a pre-runtime `pass`.

this Claim constrains permission **to** report a result; the applicable E Atoms supply the checks. it does **not** require complete graph coverage for a Claim that needs **only** bounded evidence.

## Details
