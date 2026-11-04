---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 37
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-1051
atom_id: CA-R-1676
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Keep RMED-to-RMED Relations within Active Authority

## Claim

### Prose Claim


direct relations authored by Current RMED Atoms that target RMED Atoms.


**if** a direct relation is authored by a Current Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery) **and** targets an Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery), **then** the target Atom **must** be Current.
