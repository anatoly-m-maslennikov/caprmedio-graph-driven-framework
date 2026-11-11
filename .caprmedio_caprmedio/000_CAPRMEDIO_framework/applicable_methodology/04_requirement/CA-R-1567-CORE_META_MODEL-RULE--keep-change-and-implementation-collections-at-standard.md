---
atom_id: CA-R-1567
ref_id: CA-R-1567
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
  dependencies:
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Package/Project Package
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)
tier: 2
status: Active
version: 26
updated_at: 2026-11-10 14:38:45 +0400
carrier_destination:
  file:
    name: CA-R-1567-CORE_META_MODEL-RULE--keep-change-and-implementation-collections-at-standard.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1567-CORE_META_MODEL-RULE--keep-change-and-implementation-collections-at-standard.md
  source_atom_id: CA-R-1567
  source_atom_revision: 26
  source_sha256: 170ca8acc4c5c7548f2ffa04f8c14dc2f1b9f7994e509e7c0456f6957e0a0c6e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Change and Implementation collections at Standard

## Claim

### Prose Claim


Atom Collections and decomposition views grouping CAPO or I content.


an Atom Collection **or** decomposition view grouping CAPO **or** I content **must** remain a derived grouping and **must not** acquire an Atom Tier or imply a Tier from its grouped Content Roles or Types. When a view displays a source Atom, it preserves that source Atom's numeric Tier; the grouping itself has no independent Tier.

nesting expresses composition, **not** Core **or** General authority; a Plan Directory Carrier remains a Carrier of its existing Atom under CA-D-460-CORE_META_MODEL-ENG_DECISION--serialize-plan-atom-carrier-bundles, **not** an independently tiered collection **or** second Atom.
