---
atom_id: CA-R-1194
ref_id: CA-R-1194
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Term
tier: 1
status: Active
version: 32
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1194-CORE_META_MODEL-RULE--define-subject-path.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Subject Path

## Claim

### Prose Claim


A canonical Subject path identifying a governed or dependency target.




The following interpretation is required when this governed concept is used:

A Subject Path is a full canonical expression identifying one thing or topic addressed by GOVERNS or DEPENDS_ON. Entity is the canonical expression root under CA-R-2462; this Definition does not enumerate a closed root-branch set. A source path retains the declared operators and full qualification; a short display label is not another identity or alias.

The target is selected by the meaning addressed, not by the Atom's Local Scope Unit, Content Role, folder or Carrier. The path names a target; it is not itself the Subject Relation. A defining Atom may introduce that target, so format checks do not require prior target existence.

## Semantics

A path may address classification without declaring an Entity kind. `Atom.Header.Role` addresses the relative Property, while `Atom/(.Header.Role: Plan)` identifies a qualified Atom inheriting applicable Atom features and constraints. Neither form invents an intermediate Entity kind. The root and operators follow the adopted Entity syntax under CA-R-1931; no Project-name namespace layer is introduced.
