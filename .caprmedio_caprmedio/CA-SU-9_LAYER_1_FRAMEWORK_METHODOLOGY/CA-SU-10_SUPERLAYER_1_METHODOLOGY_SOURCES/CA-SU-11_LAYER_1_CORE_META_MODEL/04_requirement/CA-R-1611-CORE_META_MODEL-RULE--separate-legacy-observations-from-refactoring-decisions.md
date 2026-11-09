---
atom_id: CA-R-1611
ref_id: CA-R-1611
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Traceability"
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Projection
tier: 3
status: Active
version: 28
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1611-CORE_META_MODEL-RULE--separate-legacy-observations-from-refactoring-decisions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Separate legacy observations from refactoring decisions

## Claim

### Prose Claim


Reverse-engineering results, including observed Implementation facts and proposed decisions about the intended refactored result.


reverse-engineering results **must** distinguish observed Implementation facts from proposed decisions about the intended refactored result.

- behavior **or** constraints proposed for preservation **must** be identified as proposed decisions.
- behavior **or** constraints proposed for change **must** be identified as proposed decisions.
- unresolved behavior, missing evidence, **and** uncertain interpretations **must** remain explicit.

an observed behavior **or** defect **must not** become a Requirement merely because it exists **in** the legacy Implementation. supporting evidence **must** remain recoverable **without** a proposed disposition **or** uncertainty being presented as an observed fact.
