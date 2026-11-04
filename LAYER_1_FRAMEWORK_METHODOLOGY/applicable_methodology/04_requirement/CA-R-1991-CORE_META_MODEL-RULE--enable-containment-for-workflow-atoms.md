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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1991-CORE_META_MODEL-RULE--enable-containment-for-workflow-atoms.md
  source_atom_id: CA-R-1991
  source_atom_revision: 13
  source_sha256: 2ba90e621c5cd394a4e930cab335d13bc781f6b313f2c6c3ae455b9dcbb2d387
  original_relations_sha256: 4fde62f0627e52833e954bbd64d451c404b9f9d66585c52603ef12fa5886adfa
---
## Summary

Enable containment for Workflow Atoms

## Claim

### Prose Claim


Containment capability of Workflow Atoms.


`Atom/(.Header.Role := Operations)/(.Header.Form := Workflow).Enabled Relations.Contains` **must** be True. a Workflow Atom **may** contain Step Atoms.

## Details

The Workflow remains an Atom. Its Steps retain their own definitions and Action references. This permission does not copy shared Actions into a Workflow or replace its declared control flow with folder order.
