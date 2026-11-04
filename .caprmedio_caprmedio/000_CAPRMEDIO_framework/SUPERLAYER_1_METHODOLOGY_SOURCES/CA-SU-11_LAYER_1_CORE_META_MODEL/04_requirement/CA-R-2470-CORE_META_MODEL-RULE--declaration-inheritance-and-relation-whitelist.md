---
atom_id: CA-R-2470
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ (Node, Node.**)
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---

## Summary

Inherit Declaration constraints and enforce Relation whitelists

## Claim

### Prose Claim


For Node1/Node2, Node2's instances receive Node1's applicable:

- Relation cardinalities.
- Declared Properties.
- Property Formats and value domains.
- Direct-value and nested-Property cardinalities.

Applicable local Node constraints also apply. Inheritance does not copy actual values or Relation facts. Reuse an inherited Property's Declaration; an inherited lookup creates no new Property or bearer.

Each Node's effective Declaration resolves its complete Relation whitelist, including permissions, directions, endpoints and cardinalities. A Relation absent from that effective whitelist is forbidden. An unresolved whitelist does not grant permission.

