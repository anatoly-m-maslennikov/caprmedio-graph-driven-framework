---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Tier
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Goal'
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ MODEL <+ Atom.Tier
version: 10
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-2125
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Active
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2125-CORE_META_MODEL-RULE--give-every-non-project-goal-atom-one-numeric-tier.md
  source_atom_id: CA-R-2125
  source_atom_revision: 10
  source_sha256: e705a6d6eddaa549187ed543681819c37e46537c40aee33e17b23644adf998c1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary
Give Every Non-Project-Goal Atom One Numeric Tier

## Claim scope
Atom other than a Project Goal Atom.

## Claim

**every** non-Project-Goal Atom **must** carry exactly one integer Tier. An ordinary Atom owned by a Scope Unit uses an integer Tier **>=0**. Project Goal is the separate explicit Tier `-1` case under CA-R-2132.

This rule defines owner-relative ranges, not a finite set of values. Higher integers remain admissible and may be assigned or raised when required by the approved governing-relation ordering. No Content-Role or Type-to-Tier restriction is imposed.
