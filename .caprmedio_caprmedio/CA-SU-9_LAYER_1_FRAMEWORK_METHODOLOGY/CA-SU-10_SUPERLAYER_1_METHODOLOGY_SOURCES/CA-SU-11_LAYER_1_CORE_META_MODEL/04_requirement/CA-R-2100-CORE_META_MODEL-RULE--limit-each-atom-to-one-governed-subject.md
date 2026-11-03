---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation//GOVERNS
atom_id: CA-R-2100
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 8
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 1
role: Requirement
form: Rule
---
## Summary

Limit each Atom to one governed Subject

## Claim

### Prose Claim


The direct GOVERNS Subject Relations recorded in an Atom's Subjects.


An Atom **may** have zero or one direct GOVERNS Subject Relation. No Atom's Subjects **may** contain more than one direct GOVERNS Subject Relation.

## Details

This Rule limits cardinality only. It does not require an Atom to have a GOVERNS Subject. The Subjects collection is optional, and DEPENDS_ON relations are not limited by this Rule.
