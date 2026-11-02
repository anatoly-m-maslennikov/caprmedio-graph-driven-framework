---
atom_id: CA-R-2227@3
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Entity Definition'
version: 3
relations: {}
tier: 1
updated_at: 2026-10-29 17:09:47 +0400
---
## Summary

Define Requirement Type Entity Definition

## Claim

Entity Definition is a Requirement Type defining one named primary Entity or dependent property with one canonical governed Subject: its meaning, structure and applicable constraints. It has required direct prose Claim; an optional R-only Formal claim complements that same scoped definition. Structural/property cardinalities and value formats belong in its formal part when applicable; other conditions stay in prose. Semantics and Details explain/support rather than add hidden operative requirements.

Each Entity has one canonical defining R across Scope Units. Other scoped Rs may constrain that Entity, but do not become additional Entity Definitions. The Relation Definition template qualifies without introducing a subtype hierarchy. A Definition includes its coherent characteristics; do not invent a new Entity for each nuance or condition.

For / specialization, reuse the broader Definition and state only the narrower entity's distinctions. For // instantiation, reuse the kind Definition and state only the instance-specific facts. Both inherit applicable structure, properties and constraints; neither copies the base Definition. Containment > does not supply this inheritance. A Method Atom is an Atom with Content Role Method, so its Definition states the Method contribution rather than repeating Atom's full schema.

## Details

This is the general Type meaning, not the old Model-specific Graph Rule arrangement. It supersedes the older generic Definition Type. Advanced expression work remains a separate proposal.
