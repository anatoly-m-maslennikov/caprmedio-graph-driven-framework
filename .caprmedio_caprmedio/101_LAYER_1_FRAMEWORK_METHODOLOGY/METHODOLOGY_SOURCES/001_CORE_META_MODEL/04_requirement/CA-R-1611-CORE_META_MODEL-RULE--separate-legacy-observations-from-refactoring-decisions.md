---
atom_id: CA-R-1611
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Traceability
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Analysis'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
version: 21
updated_at: 2026-10-27 19:59:59 +0400
relations: {}
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
