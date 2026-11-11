---
atom_id: CA-M-273
ref_id: CA-M-273
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
  - CAPRMEDIO_MODEL <+ Carrier/Directory
tier: 3
status: Active
version: 38
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-M-273-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-ownership-and-claim-target-atom-sets.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Derive Ownership **and** Claim-target Atom Sets

## Claim

### Prose Claim


selection of Owned Atoms, Targeting Atoms, Subtree-owned Atoms, **and** Subtree-targeting Atoms for a Scope Unit.


**to** derive the four Atom sets for a selected Scope Unit, the resolver **must** perform **all** of:

1. establish the complete authoritative source frontier, including Atoms outside the selected subtree that can target a Scope Unit inside it; scanning **only** locally stored Atoms is insufficient for Targeting Atoms **or** Subtree-targeting Atoms.
2. read **every** candidate Atom's carried current Scope Unit **and** check it against its nearest containing Scope Unit, passing through Atom Collections **and** Plan Hub Carriers **without** treating their nesting as additional Scope Unit ownership. preserve the carried external-Atom Author fallback under CA-D-657-CORE_META_MODEL-ENG_DECISION--use-economical-yaml-frontmatter **when** no containing Scope Unit exists; do **not** invent a Scope Unit owner.
3. resolve **every** candidate's Claim Target Scope Unit independently of ownership. read the internally carried target; absence of a required value is invalid, **not** permission **to** infer it from placement; apply CA-R-1588-CORE_META_MODEL-RULE--default-plan-target-to-the-enclosing-scope-unit for Plans within Plan containment. an unresolved required target remains unresolved. a reference **to** another Scope Unit **must not** transfer ownership, **and** the target **must** resolve **to** a Scope Unit, **not** a Hub Atom **or** another non-Scope-Unit object. Claim Scope restrictions remain **in** the body sections registered by CA-D-495, including Scope for RMED, **and** do **not** create extra targets.
4. derive Owned Atoms, Targeting Atoms, Subtree-owned Atoms, **and** Subtree-targeting Atoms under CA-R-1447-CORE_META_MODEL-GENERAL-REQUIREMENT--define-owned-atoms, CA-R-1448-CORE_META_MODEL-GENERAL-REQUIREMENT--define-targeting-atoms, CA-R-942-CORE_META_MODEL-DEFINITION--define-subtree-owned-atoms, **and** CA-R-1449-CORE_META_MODEL-GENERAL-REQUIREMENT--define-subtree-targeting-atoms respectively. use the Scope Unit tree for descendant coverage; do **not** substitute physical subtree membership for Claim targeting **or** inferred inherited applicability for an explicit **or** default Claim target.
5. retain source Atom **and** Revision references **without** creating additional authoritative Atom copies. apply Content Role, Status, **and** other requested filters **after** resolving the selected set; the alias `spec` selects the Active RMED subset under CA-M-288-CORE_META_MODEL-IMPLEMENTATION_METHOD--use-spec-as-an-alias-for-active-rmed-subtree-targeting-atoms, independently of numeric Tier.
6. report the exact missing source, owner, target, ancestry, **or** required filter value **and** withhold a complete affected result **when** it is unresolved **or** contradictory. a complete empty set remains empty; an incomplete frontier **must not** be reported as a complete empty set.
