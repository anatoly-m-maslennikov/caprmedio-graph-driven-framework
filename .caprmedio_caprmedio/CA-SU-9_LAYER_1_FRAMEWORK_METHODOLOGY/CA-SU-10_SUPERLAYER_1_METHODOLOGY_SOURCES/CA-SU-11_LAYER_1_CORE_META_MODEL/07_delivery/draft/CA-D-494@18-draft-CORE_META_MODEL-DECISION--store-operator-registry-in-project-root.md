---
atom_id: CA-D-494
ref_id: CA-D-494@18-draft
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Operator Registry
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Journal
tier: 3
status: Draft
version: 18
updated_at: 2026-11-05 13:47:13 +0400
carrier_destination:
  file:
    name: CA-D-494@18-draft-DECISION--store-operator-registry-in-project-root.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft
---
## Summary

Store Operator Registry in Project Root

## Claim

### Prose Claim


the authoritative Operator registry of a Project.


the authoritative Operator registry **must** use **`=1`** `operators_registry.toml` file **in** the Project authority root, alongside Project Settings.

- the root has **`=1`** key, `operators`, containing **`>=1`** `[[operators]]` table.
- **every** table has **`=1`** `name` **and** **`=1`** `role`, both nonempty strings. names are unique. additional keys **or** duplicate identities make the registry invalid.
- `role` describes the Operator; it does **not** replace the name **or** independently grant execution permission.
- concrete Operator names **and** roles belong **only** **in** the Project's registry, **not** **in** reusable methodology **or** Tool code. a missing, unreadable, malformed, **or** stale registry leaves membership unresolved; it is **not** an empty valid registry.

