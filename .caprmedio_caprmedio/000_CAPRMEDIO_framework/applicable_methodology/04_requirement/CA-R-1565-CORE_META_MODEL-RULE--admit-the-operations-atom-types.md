---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations).Header.Form'
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1565
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1565-CORE_META_MODEL-RULE--admit-the-operations-atom-types.md
  source_atom_id: CA-R-1565
  source_atom_revision: 21
  source_sha256: 94f3844bd8305bcafb46b2dee619b5ee4e69c76f641814a5985dcf0f27b22214
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Admit the Operations Atom Types

## Claim

### Prose Claim


internal Type values of Operations Atoms.


the admitted internal values of `Atom/(.Header.Role := Operations).Header.Form` **must** include (Action, Workflow, Step).

## Details

Branch, Fork, and Decision are not admitted internal Type values. Linear and Conditional are Step forms carried by Step definitions, not additional Operations Atom Types.
