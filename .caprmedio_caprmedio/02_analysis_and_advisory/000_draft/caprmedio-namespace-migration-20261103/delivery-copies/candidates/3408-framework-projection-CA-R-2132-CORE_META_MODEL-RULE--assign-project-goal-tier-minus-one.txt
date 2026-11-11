---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Tier
  passive:
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Project Goal'
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ MODEL <+ Atom.Tier
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
version: 12
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-2132
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Active
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2132-CORE_META_MODEL-RULE--assign-project-goal-tier-minus-one.md
  source_atom_id: CA-R-2132
  source_atom_revision: 12
  source_sha256: 3e569022592f6035913df186081fb2867087d31d8e8ea2b936fbce5473988386
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Assign Project Goal Tier Minus One

## Claim scope

Project Goal Atoms.

## Claim

Every Requirement Atom of Type Project Goal **must** target the Project, be owned by its Operator Actor instead of a Local Scope Unit, and carry exactly one numeric Tier `-1`. Tier `-1` is explicit, is not omitted, and is outside the ordinary nonnegative Tier range. This Rule does not impose an arbitrary Type-to-Tier restriction beyond verified Project Goal identity and ownership.

## Details

The Project Goal retains its Operator Actor owner. CA-R-2149 uses its Target Project only as the derived ordering context; ordinary Goal ownership and Scope ordering are unchanged.
