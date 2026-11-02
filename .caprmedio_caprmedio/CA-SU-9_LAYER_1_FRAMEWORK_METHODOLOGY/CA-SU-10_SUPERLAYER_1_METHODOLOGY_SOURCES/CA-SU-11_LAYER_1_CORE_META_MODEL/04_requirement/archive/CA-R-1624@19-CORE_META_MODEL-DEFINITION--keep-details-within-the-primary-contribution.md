---
atom_id: CA-R-1624@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content.Details
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Content
relations: {}
version: 19
updated_at: 2026-10-29 10:13:49 +0400
tier: 1
type: Entity Definition
---
## Summary

Keep Details within the primary contribution

## Claim scope

supporting Details **in** an Atom's Content.

## Claim

an Atom's Details **means** supporting information that expands its primary contribution **without** changing its intent, applicability, **or** required outcome. Details **must not** contradict that contribution **or** introduce another independently replaceable contribution. for RMED, the primary contribution is the Claim read within its Scope; Details **must not** introduce an additional obligation **or** alter those applicability restrictions.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom.Content.Details[string]{0..1}
```
