---
atom_id: CA-R-1990
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Enabled Relations.Contains'
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Enabled Relations.Contains
relations:
  child_of:
  - CA-R-2478
version: 12
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Rule
---
## Summary

Enable containment for Plan Atoms

## Claim

### Prose Claim


Containment capability of Plan Atoms.


`Atom/(.Header.Role := Plan).Enabled Relations.Contains` **must** be True. a Plan Atom **may** contain other Plan Atoms.

## Details

Plan labels such as Epic, Task and Version do not create different containment Types. Containment is optional and can nest. This permission does not implement a Plan projection or replace other typed relations between Plans.
