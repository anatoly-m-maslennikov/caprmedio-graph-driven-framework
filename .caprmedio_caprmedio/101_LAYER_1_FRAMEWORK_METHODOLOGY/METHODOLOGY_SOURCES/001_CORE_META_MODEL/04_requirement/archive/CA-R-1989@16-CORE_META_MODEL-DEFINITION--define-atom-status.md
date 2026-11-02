---
atom_id: CA-R-1989@16
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Status
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Content Role
relations:
  child_of:
  - CA-R-1174
version: 16
updated_at: 2026-10-30 17:16:27 +0400
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

IS_PROPERTY_OF expresses the property-to-Atom relation. A Current Atom is not historical merely because it has a Version Number. Archive conversion changes the representation status to `Archived` without changing the governed content, Version or Updated At. CA-R-1412 supplies the one-Status requirement. The separate allowed-value rules define inherited and additional values; this definition repeats that existing base domain without adding a transition procedure or mandatory history record. Shared Status meanings follow their dedicated governing Term Definitions; an optional Terms Graph can project those sources without independently authoring another meaning for each owner.

### Current source pin and pending adoption

Proposed N+1 successor of `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1989-CORE_META_MODEL-DEFINITION--define-atom-status.md`, Version 15, SHA-256 `e23edf67d8eccbc842c3b423b24fbb9f13068e53f95a9335510839079a72c51e`. Current bytes remain unchanged. The new Relation names depend on the pending IS_PROPERTY_OF / HAS_PROPERTY Relation Definition Drafts; this source does not admit them through a renamed token alone. This preparation performs no runtime change, generated-view refresh or promotion.
