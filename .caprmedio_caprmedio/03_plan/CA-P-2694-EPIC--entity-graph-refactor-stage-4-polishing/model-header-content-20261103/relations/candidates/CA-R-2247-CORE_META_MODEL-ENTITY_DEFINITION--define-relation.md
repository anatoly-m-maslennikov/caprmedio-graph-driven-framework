---
atom_id: CA-R-2247
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 5
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Relation

## Claim

### Formal Claim

```CFEL
Relation.Name{:1}: [string]{:1};
Relation.Name.*[]{:0};
Relation.Meaning{:1}: [string]{:1};
Relation.Meaning.*[]{:0}
```

### Prose Claim

Relation defines a reusable directed graph Relation Type with a Name and Meaning. Each actual link is a tuple (Host, Relation Type, Target); persist each direct fact once. Endpoints are declared model Entities or instances, including Carrier and CFEL descriptors, and exclude literal values and glyphs. An operator is distinct from a graph Relation even when its notation spells a Relation traversal. Its declared descriptor may be an endpoint.

A direct Relation Declaration owns shared meaning, endpoint signature and any counterpart binding. A derived counterpart remains a distinct Relation with its own Declaration; its meaning and endpoints are inferred through that binding. An alias supplies lexical notation for one Relation; it does not create a new Relation, a Node or a separate Relation ID.
