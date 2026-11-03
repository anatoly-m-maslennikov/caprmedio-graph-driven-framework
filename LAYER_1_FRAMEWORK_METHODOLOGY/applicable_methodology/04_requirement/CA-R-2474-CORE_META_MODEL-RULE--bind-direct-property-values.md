---
atom_id: CA-R-2474
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Node
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2474-CORE_META_MODEL-RULE--bind-direct-property-values.md
  source_atom_id: CA-R-2474
  source_atom_revision: 2
  source_sha256: 1df9594a5a58dfda43b824f7862005b04b6b0da81d7aa13d4ffe6a8329c21efb
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Bind direct Property values on instances

## Claim

HAS_VALUE binds a Property on an instance to its admitted literal value. For example, the version Property of Atom instance CA-P-123 has value 1. The Property declaration supplies its value format, admitted domain and cardinality; the literal 1 is not a separately declared graph Node and requires no Declaration Atom.

HAS_VALUE is a value binding rather than an ordinary Node-to-Node graph Relation. It must not create graph endpoints or independently authored inverse facts for literals. A Primary Node has no direct value. A Property on a Primary Node instance may hold direct values where its effective declaration permits them, including inherited Property declarations. Applying a declared Property to an instance does not instantiate that Property through HAS_INSTANCE or give its declaration another bearer.
