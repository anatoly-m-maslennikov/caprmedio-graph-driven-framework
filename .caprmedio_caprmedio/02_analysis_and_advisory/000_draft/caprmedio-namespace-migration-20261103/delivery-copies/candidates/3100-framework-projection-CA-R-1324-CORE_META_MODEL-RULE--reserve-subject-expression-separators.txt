---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Term.Name
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1324
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1324-CORE_META_MODEL-RULE--reserve-subject-expression-separators.md
  source_atom_id: CA-R-1324
  source_atom_revision: 27
  source_sha256: 573c277c2ccbe80eff71a8bbe80742e4b87708d9586f4db2cd2e32300bb0e941
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Reserve Subject Expression Separators

## Claim scope

Term names in Subject Expressions.

## Claim

a Term name **must not** contain unescaped `/`, `//`, `.`, `:`, `+>`, `<+`, `>|`, `|<`, `((`, `))`, `@`, `(`, `)`, `[`, `]`, `{`, or `}`. These are reserved Subject Expression syntax for specialization or instances, Property and allowed-value qualification, containment, classification, named Relations, calls to already declared Entities, logical grouping, direct-value Format, or cardinality. A backslash escapes a literal operator character in a name; this Rule does not ban such escaped literal name characters or invent a quote DSL. This Term-name rule does not make the RHS name after `//` a Term; that operand identifies an instance that already exists or is explicitly introduced by applicable defining authority under its separate naming/source authority. Syntax alone neither creates nor admits the instance. The lowercase `atom` keyword and its selector punctuation remain registered initial-selector syntax under CA-R-1321, not a broadened Term-name policy.
