---
atom_id: CA-R-2377@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains'
relations: {}
version: 1
updated_at: 2026-10-29 17:09:47 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Step Enabled Relations Contains

## Claim scope

Containment capability on the stated nested Step path.

## Claim

For a Step Atom nested under a Workflow by the stated >{1+} path, Enabled Relations.Contains is a Boolean containment capability that is True; a Step may contain Step Atoms. A containing Step launches no Action of its own, while a leaf Step launches exactly one referenced Action with its parameters and input bindings.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step.Enabled Relations.Contains[bool]{1}
```

## Details

Source meaning: CA-R-1945, CA-R-1992. Scope-specific constraints remain in their governing Rs.
