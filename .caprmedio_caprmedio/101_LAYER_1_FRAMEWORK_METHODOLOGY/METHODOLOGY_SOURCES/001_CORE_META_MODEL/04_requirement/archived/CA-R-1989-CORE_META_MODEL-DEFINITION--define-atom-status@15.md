---
atom_id: CA-R-1989
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Status
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
relations:
  child_of:
  - CA-R-1174
version: 15
updated_at: 2026-10-29 14:16:32 +0400
tier: 1
type: Entity Definition
---
## Summary

Define Atom Status

## Claim scope

Status borne by an Atom, including the lifecycle value carried by an archived representation.

## Claim

Atom.Status **means** the Atom's lifecycle classification under its applicable Status model. Status is a dependent property of the Atom; its allowed values resolve under the applicable Atom, Content Role and Type rules. An archived representation carries `Archived` as its status, while retaining the predecessor's Version and Updated At; archiving alone does not create a new version.

The base allowed Status values are Draft, Active and Archived under CA-R-1947. Narrower Atom kinds inherit these values and may add their own governed values.

### Formal claim

```text
Atom.Status[string]{1}
Atom.Status: Draft
Atom.Status: Active
Atom.Status: Archived
```

## Details

IS_BORNE_BY expresses the property-to-Atom relation. A Current Atom is not historical merely because it has a Version Number. Archive conversion changes the representation status to `Archived` without changing the governed content, Version or Updated At. CA-R-1412 supplies the one-Status requirement. The separate allowed-value rules define inherited and additional values; this definition repeats that existing base domain without adding a transition procedure or mandatory history record. Shared Status meanings are derived in the Terms graph from source usage, not independently authored here for every owner.
