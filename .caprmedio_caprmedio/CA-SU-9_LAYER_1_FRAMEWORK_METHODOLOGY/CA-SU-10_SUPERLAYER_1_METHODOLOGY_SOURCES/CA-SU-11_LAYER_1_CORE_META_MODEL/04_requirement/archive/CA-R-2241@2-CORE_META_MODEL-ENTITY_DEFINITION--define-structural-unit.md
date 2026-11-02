---
atom_id: CA-R-2241@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Structural Unit
version: 2
updated_at: 2026-10-29 09:46:50 +0400
relations: {}
tier: 1
---
## Summary

Define Structural Unit

## Claim

Structural Unit classifies the organizational Scope Unit kind. Project specializes Scope Unit as its parentless root; structural containment remains separate from this classification and adds no numeric structural level.

### Formal claim

```text
Continuant/Structural Unit
Structural Unit/Scope Unit
Scope Unit/Project
```

## Semantics

Scope Unit specializes Structural Unit; Project specializes Scope Unit as its parentless root. Project containment and recursive Scope Unit structure are separate from this classification. This classification does not add a numeric structural-level property. CA-A-1258 supersedes the earlier sibling Project/Scope Unit layout.

## Details

Review Draft from A1247–A1249; Current authority is this defining Atom; the review references are supporting provenance.
