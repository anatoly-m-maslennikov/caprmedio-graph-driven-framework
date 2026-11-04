---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)'
  passive:
  - CAPRMEDIO_MODEL <+ Atom
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-932@37
atom_id: CA-R-933
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Requirement
form: Rule
---
## Summary
Restrict Demand to one depended-on result

## Claim

### Prose Claim


Demand Atoms.


**every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Goal depends.
