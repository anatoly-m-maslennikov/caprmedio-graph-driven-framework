---
atom_id: CA-R-1612@13
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Realization Graph'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Content
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - Subject/Engineering/Outcome Evidence
  - Subject/Graph/Relation.Derivation Class
version: 13
updated_at: 2026-10-25 01:04:58 +0400
relations:
  relates_to:
  - CA-M-312
  - CA-R-1494
  - CA-R-1616
  - CA-R-1617
  - CA-R-1687
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
