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
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  - CAPRMEDIO_MODEL <+ Package/Project Package
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Tier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form := Plan)
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
---
## Summary

Keep Change and Implementation collections at Standard

## Claim

### Prose Claim


Atom Collections and decomposition views grouping CAPO or I content.


an Atom Collection **or** decomposition view grouping CAPO **or** I content **must** remain a derived grouping and **must not** acquire an Atom Tier or imply a Tier from its grouped Content Roles or Types. When a view displays a source Atom, it preserves that source Atom's numeric Tier; the grouping itself has no independent Tier.

nesting expresses composition, **not** Core **or** General authority; a Plan Directory Carrier remains a Carrier of its existing Atom under CA-D-460-CORE_META_MODEL-ENG_DECISION--serialize-plan-atom-carrier-bundles, **not** an independently tiered collection **or** second Atom.
