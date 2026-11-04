---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Form
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
version: 37
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-923
atom_id: CA-R-924
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Requirement
form: Rule
---
## Summary
Register Core Relational Atom Classifications

## Claim

### Prose Claim


Allowed qualified Types of Relational Atom.


the Core contribution **to** allowed qualified Types of Relational Atom **must** be (`Atom/(.Header.Role := Requirement)/(.Header.Form := Goal)`, `Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)`, `Atom/(.Header.Role := Plan)/(.Header.Form := Plan)`); a Plan is relational **only** **when** its actual Claim target differs under the Relational Atom definition, **not** merely because it has decomposition, blocking, **or** a particular Label.
