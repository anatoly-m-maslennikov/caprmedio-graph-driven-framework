---
atom_id: CA-R-1324
ref_id: CA-R-1324
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Term.Name
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
tier: 3
status: Active
version: 27
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1324-CORE_META_MODEL-RULE--reserve-subject-expression-separators.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1324-CORE_META_MODEL-RULE--reserve-subject-expression-separators.md
  source_atom_id: CA-R-1324
  source_atom_revision: 27
  source_sha256: 6de46ae1454cd7d78104cc83ad05ee2a89120ea57d8174eb21767390e96e836b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Reserve Subject Expression Separators

## Claim

### Prose Claim


Term names in Subject Expressions.


a Term name **must not** contain unescaped `/`, `//`, `.`, `:`, `+>`, `<+`, `>|`, `|<`, `((`, `))`, `(`, `)`, `[`, `]`, `{`, or `}`. These are reserved Subject Expression syntax for specialization or instances, Property and allowed-value qualification, containment, classification, named Relations, logical grouping, direct-value Format, or cardinality. A backslash escapes a literal operator character in a name; this Rule does not ban such escaped literal name characters or invent a quote DSL. This Term-name rule does not make the RHS name after `//` a Term; that operand identifies an instance that already exists or is explicitly introduced by applicable defining authority under its separate naming/source authority. Syntax alone neither creates nor admits the instance. The lowercase `atom` keyword and its selector punctuation remain registered initial-selector syntax under CA-R-1321, not a broadened Term-name policy.
