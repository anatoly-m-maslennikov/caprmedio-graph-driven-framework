---
subjects:
  active: CFEL <+ Relation
  passive:
  - Entity
  - Projection
  - Atom
  - Journal
  - CFEL <+ Relation
version: 28
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1472
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1472-CORE_META_MODEL-RULE--admit-typed-secondary-graph-connections.md
  source_atom_id: CA-R-1472
  source_atom_revision: 28
  source_sha256: 999c0704da99a68e1c8143d3bed3851c745e2daee9b14eeaebd0b9bbf1afe2ad
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Admit typed secondary graph connections

## Claim scope

connections represented by a secondary CAPRMEDIO Graph.

## Claim

a secondary CAPRMEDIO Graph **may** represent typed Relations between its own nodes, **to** another secondary graph **or** its nodes, **and** **to** source Atoms **or** other admitted authoritative sources.

**every** connection **must** identify **`=1`** shared project-unique Relation Type under its defining authority, with its declared direction preserved, **and** must conform to any applicable governing Entity Definition endpoint-class, endpoint-graph-context, **and** cardinality constraints. a graph-qualified reference **or** context may qualify that connection without creating graph-owned Type identity. crossing a graph boundary **must not** create a graph-specific Type identity, import a foreign Relation Type as native, **or** make a referenced external endpoint a native node of the receiving graph. a cross-graph reference preserves the referenced endpoint identity **and** source traceability **without** copying its source fact into independent authority. these permissions do **not** create a Relation Type definition **or** authorize inference beyond the defining authority and applicable Rules.
