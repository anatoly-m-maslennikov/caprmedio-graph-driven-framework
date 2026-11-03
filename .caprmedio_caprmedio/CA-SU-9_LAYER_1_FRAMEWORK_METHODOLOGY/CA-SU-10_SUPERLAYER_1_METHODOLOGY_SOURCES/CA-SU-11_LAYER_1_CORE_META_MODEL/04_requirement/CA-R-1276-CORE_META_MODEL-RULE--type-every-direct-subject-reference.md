---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Subjects
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation
  - CAPRMEDIO_MODEL <+ CFEL > Relation//GOVERNS
  - CAPRMEDIO_MODEL <+ CFEL > Relation//DEPENDS_ON
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1276
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Type Every Direct Subject Reference

## Claim scope

direct references in an Atom's Subjects Property.

## Claim

**every** direct reference **in** an Atom's Subjects Property **must** use **`=1`** Relation Kind **in** (GOVERNS, DEPENDS_ON). the relation entry supplies this kind **without** an additional kind Property on a Subject object.
