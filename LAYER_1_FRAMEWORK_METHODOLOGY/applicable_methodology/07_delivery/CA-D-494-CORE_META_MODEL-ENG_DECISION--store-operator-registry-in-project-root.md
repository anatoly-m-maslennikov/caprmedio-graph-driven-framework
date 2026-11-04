---
atom_id: CA-D-494
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 17
updated_at: 2026-11-02 00:18:22 +0400
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Operator Registry
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Journal
relations: {}
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-494-CORE_META_MODEL-ENG_DECISION--store-operator-registry-in-project-root.md
  source_atom_id: CA-D-494
  source_atom_revision: 17
  source_sha256: aa3aca414d163ac7ead82f39827362a2cb7fd1315f33c9a9f1e35047231c9cc1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Store Operator Registry in Project Root

## Claim

### Prose Claim


the authoritative Operator registry of a Project.


the authoritative Operator registry **must** use **`=1`** `operators_registry.toml` file **in** the Project authority root, alongside Project Settings.

- the root has **`=1`** key, `operators`, containing **`>=1`** `[[operators]]` table.
- **every** table has **`=1`** `name` **and** **`=1`** `role`, both nonempty strings. names are unique. a table may also carry **<=1** `journal_author`, an explicitly registered Journal account name using the Journal's Author format. provided Journal account names are unique; **other** additional keys **or** duplicate identities make the registry invalid.
- Author membership compares the carried `author` string with registered `name` values exactly, **without** aliases, case folding, trimming, **or** inference from filenames. `role` describes the Operator; it does **not** replace the name **or** independently grant execution permission.
- concrete Operator names **and** roles belong **only** **in** the Project's registry, **not** **in** reusable methodology **or** Tool code. a missing, unreadable, malformed, **or** stale registry leaves membership unresolved; it is **not** an empty valid registry.

## Details

The optional `journal_author` binds the Operator's registered display name to the account carried by Journal events. It does not change Atom Author membership or grant permission. An event account resolves only by an explicit `journal_author` match, or by a literal match with the registered `name` when no mapping is needed. Missing, duplicate or changed mappings leave command identity unresolved; Tools do not derive an account from a display name. Concrete mappings belong in the Project registry, not reusable Tool code.
