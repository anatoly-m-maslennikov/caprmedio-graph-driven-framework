---
atom_id: CA-R-2689
ref_id: CA-R-2689
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.Path
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Children
tier: 2
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2689-CORE_META_MODEL-RULE--derive-scope-unit-ancestry-from-declarations.md
  source_atom_id: CA-R-2689
  source_atom_revision: 1
  source_sha256: c4ffd5d59a3b0ab0f1d615be63c15983280b36816d2758c9b78f11b23df2b326
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Derive Scope Unit ancestry from Declarations

## Claim

Scope Unit ancestry is derived from Scope Unit Declarations and their direct parent relations. CAPRMEDIO does not author or persist a Structural Level property for a Scope Unit. A displayed path or depth is derived from that parent chain only. It does not establish or override parentage, ownership, or authority. Conflicting or unresolved parent inputs remain unresolved.
