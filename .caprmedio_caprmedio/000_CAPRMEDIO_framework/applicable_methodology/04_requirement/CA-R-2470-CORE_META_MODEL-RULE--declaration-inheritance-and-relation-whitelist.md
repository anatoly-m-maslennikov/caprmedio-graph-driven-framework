---
atom_id: CA-R-2470
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: (Node, Node/**, .**)
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2470-CORE_META_MODEL-RULE--declaration-inheritance-and-relation-whitelist.md
  source_atom_id: CA-R-2470
  source_atom_revision: 2
  source_sha256: f745229e672dd0effaa6d9926f0a48aa7dd2d5a41a7144649863de2970a43d9a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Inherit Declaration constraints and enforce Relation whitelists

## Claim

For Node1/Node2, Node2's instances receive Node1's applicable:

- Relation cardinalities.
- Declared Properties.
- Property Formats and value domains.
- Direct-value and nested-Property cardinalities.

Applicable local Node constraints also apply. Inheritance does not copy actual values or Relation facts. Reuse an inherited Property's Declaration; an inherited lookup creates no new Property or bearer.

Each Node's effective Declaration resolves its complete Relation whitelist, including permissions, directions, endpoints and cardinalities. A Relation absent from that effective whitelist is forbidden. An unresolved whitelist does not grant permission.

