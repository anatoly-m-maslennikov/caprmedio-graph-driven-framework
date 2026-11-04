---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Goal)
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Active
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
version: 11
updated_at: 2026-11-04 09:19:08 +0400
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
  source_atom_revision: 11
  source_sha256: f87bc5460022a12f85e8e3e6f2ed0b5726058b671f195be4d5035144cc937ba0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary
Give Every Non-Project-Goal Atom One Numeric Tier

## Claim

### Prose Claim

Atom other than an Atom of Form Goal whose active Subject resolves to the Project Scope Unit root.


**every** Atom other than an Atom of Form Goal whose active Subject resolves to the Project Scope Unit root **must** carry exactly one integer Tier. An ordinary Atom owned by a Scope Unit uses an integer Tier **>=0**, except for that exact Project-root Goal predicate. An Atom of Form Goal whose active Subject resolves to the Project Scope Unit root carries exactly Tier `-1` under CA-R-2132, regardless of its Container or owner.

This rule defines owner-relative ranges, not a finite set of values. Higher integers remain admissible and may be assigned or raised when required by the approved governing-relation ordering. No Content-Role or Type-to-Tier restriction is imposed.
