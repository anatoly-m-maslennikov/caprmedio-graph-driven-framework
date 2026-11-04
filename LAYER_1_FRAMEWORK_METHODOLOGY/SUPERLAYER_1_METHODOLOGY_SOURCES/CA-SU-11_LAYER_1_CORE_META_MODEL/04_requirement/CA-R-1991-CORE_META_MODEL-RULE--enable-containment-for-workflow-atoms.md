---
atom_id: CA-R-1991
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow).Enabled Relations.Contains'
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Enabled Relations.Contains
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
relations:
  child_of:
  - CA-R-2478
version: 13
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Rule
---
## Summary

Enable containment for Workflow Atoms

## Claim

### Prose Claim


Containment capability of Workflow Atoms.


`Atom/(.Header.Role := Operations)/(.Header.Form := Workflow).Enabled Relations.Contains` **must** be True. a Workflow Atom **may** contain Step Atoms.

## Details

The Workflow remains an Atom. Its Steps retain their own definitions and Action references. This permission does not copy shared Actions into a Workflow or replace its declared control flow with folder order.
