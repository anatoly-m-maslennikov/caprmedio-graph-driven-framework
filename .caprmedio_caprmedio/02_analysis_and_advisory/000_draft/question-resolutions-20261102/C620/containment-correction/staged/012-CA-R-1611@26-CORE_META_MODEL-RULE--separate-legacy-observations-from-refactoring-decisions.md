---
atom_id: CA-R-1611@26
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
subjects:
  active: Entity/Aspect/Engineering/Traceability
  passive:
  - Atom/(.Role := "Analysis & Advisory")
  - Atom.Content
  - Atom/(.Role := Evaluation)
  - Projection
version: 26
updated_at: 2026-11-02 15:49:28 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Separate legacy observations from refactoring decisions

## Claim scope

Reverse-engineering results, including observed Implementation facts and proposed decisions about the intended refactored result.

## Claim

reverse-engineering results **must** distinguish observed Implementation facts from proposed decisions about the intended refactored result.

- behavior **or** constraints proposed for preservation **must** be identified as proposed decisions.
- behavior **or** constraints proposed for change **must** be identified as proposed decisions.
- unresolved behavior, missing evidence, **and** uncertain interpretations **must** remain explicit.

an observed behavior **or** defect **must not** become a Requirement merely because it exists **in** the legacy Implementation. supporting evidence **must** remain recoverable **without** a proposed disposition **or** uncertainty being presented as an observed fact.
