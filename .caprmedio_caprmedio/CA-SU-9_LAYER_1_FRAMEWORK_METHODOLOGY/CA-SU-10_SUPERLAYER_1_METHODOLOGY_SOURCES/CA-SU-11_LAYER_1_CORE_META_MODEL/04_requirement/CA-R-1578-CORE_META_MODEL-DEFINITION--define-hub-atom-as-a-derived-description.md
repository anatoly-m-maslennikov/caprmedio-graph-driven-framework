---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Label'
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1578
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Define Hub Atom as a derived description

## Claim

### Prose Claim


Hub Atom descriptions.


Hub Atom **means** a derived description of a Plan Atom with **`>0`** outgoing derived `CONTAINS` links to Plan Atoms; it does **not** introduce another Type, Subtype, stored classification, identity, **or** authority tier. contained Atoms retain their own Claims rather than becoming parts of the Hub Claim.
