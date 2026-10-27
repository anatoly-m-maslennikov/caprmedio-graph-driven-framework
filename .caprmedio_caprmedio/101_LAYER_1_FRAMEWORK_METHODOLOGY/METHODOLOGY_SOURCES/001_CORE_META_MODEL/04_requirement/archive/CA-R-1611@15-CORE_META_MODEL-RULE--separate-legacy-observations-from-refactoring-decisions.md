---
atom_id: CA-R-1611@15
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Implementation Reconstructability
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Analysis'
  - Subject/Domain/Node/Continuant/Atom.Substance
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - Evidence
  - Subject/Domain/Node/Continuant/Projection
version: 15
updated_at: 2026-10-24 11:58:20 +0400
relations:
  relates_to:
  - CA-R-1470
  - CA-R-1687
  - CA-R-1746
tier: 3
type: Rule
---
# Summary

Separate legacy observations from refactoring decisions

## Scope

Reverse-engineering results, including observed Implementation facts and proposed decisions about the intended refactored result.

## Claim

reverse-engineering results **must** distinguish observed Implementation facts from proposed decisions about the intended refactored result.

- behavior **or** constraints proposed for preservation **must** be identified as proposed decisions.
- behavior **or** constraints proposed for change **must** be identified as proposed decisions.
- unresolved behavior, missing evidence, **and** uncertain interpretations **must** remain explicit.

an observed behavior **or** defect **must not** become a Requirement merely because it exists **in** the legacy Implementation. supporting evidence **must** remain recoverable **without** a proposed disposition **or** uncertainty being presented as an observed fact.

## Details
