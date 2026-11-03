---
subjects:
  active: CFEL
  passive:
  - Entity
  - CFEL <+ Relation
  - Term
version: 32
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1194
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1194-CORE_META_MODEL-DEFINITION--define-subject-path.md
  source_atom_id: CA-R-1194
  source_atom_revision: 32
  source_sha256: 39c4f4e45cc91213806ee0c4caf9000695358f16e96f5d464ef3e8dff58c76c8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Subject Path

## Claim scope

A canonical Subject path identifying a governed or dependency target.

## Claim



The following interpretation is required when this governed concept is used:

A Subject Path is a full canonical expression identifying one thing or topic addressed by GOVERNS or DEPENDS_ON. Entity is the canonical expression root under CA-R-2462; this Definition does not enumerate a closed root-branch set. A source path retains the declared operators and full qualification; a short display label is not another identity or alias.

The target is selected by the meaning addressed, not by the Atom's Local Scope Unit, Content Role, folder or Carrier. The path names a target; it is not itself the Subject Relation. A defining Atom may introduce that target, so format checks do not require prior target existence.

## Semantics

A path may address classification without declaring an Entity kind. `Atom.Content Role` addresses the relative Property, while `Atom/(.Content Role: Plan)` identifies a qualified Atom inheriting applicable Atom features and constraints. Neither form invents an intermediate Entity kind. The root and operators follow the adopted Entity syntax under CA-R-1931; no Project-name namespace layer is introduced.
