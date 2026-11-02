---
atom_id: CA-R-2279@1
content_role: Requirement
type: Relation Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Graph Syntax > Relation//IS_DEFINED_BY
relations: {}
version: 1
updated_at: 2026-10-29 17:09:55 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Derived IS_DEFINED_BY Relation

## Claim

IS_DEFINED_BY is the derived counterpart of the defining GOVERNS links qualified by the Entity Definition ownership rule. It reuses that main link and its qualification; it adds no independently stored reverse fact.

### Formal claim

```text
Entity/Graph Syntax > Relation//IS_DEFINED_BY
```

## Details

The main GOVERNS meaning is defined by CA-R-1199. CA-R-2278 qualifies which GOVERNS links define an Entity. The counterpart references those sources instead of repeating their meanings or constraints; the inverse is derived only from that qualified main link.
