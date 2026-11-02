---
atom_id: CA-R-2423@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Obsolete Names
relations: {}
version: 1
updated_at: 2026-10-29 14:16:32 +0400
---
## Summary

Define Project Settings Obsolete Names

## Claim

Project Settings Obsolete Names is the optional collection of registered prior Project names. Each name is a nonempty string. A present empty collection contains no prior names; absence and an explicitly empty collection remain distinct. Exact values and ordering are preserved under CA-D-366, which specifies their TOML representation. This property does not replace the current Project Name or infer additional prior names.

### Formal claim

```text
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Obsolete Names[string]{0+}
```
