---
atom_id: CA-D-494
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
version: 3
updated_at: "2026-10-10 03:33:44 +0400"
subjects:
  governs: "Project/Operator Registry/Carrier"
  depends_on:
    - "Project"
    - "Operator"
    - "Atom/Revision/Author"
    - "Journal"
relations:
  relates_to:
    - CA-D-274
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-494-CORE_META_MODEL-DELIVERY--store-operator-registry-in-project-root.md
  source_atom_id: CA-D-494
  source_atom_revision: 3
  source_sha256: 98f80305941f3f19636e2807a2e8b5bcf5b240f5e065182e3a4f8174035424f8
  original_relations_sha256: a65eca1addd76091855e72e01ea52ce14489f7951301cdf17bf615f34767c318
---
# Summary

Store Operator Registry in Project Root

## Scope

the authoritative Operator registry of a Project.

## Claim

the authoritative Operator registry **must** use **`=1`** `operators_registry.toml` file **in** the Project authority root, alongside Project Settings.

- the root has **`=1`** key, `operators`, containing **`>=1`** `[[operators]]` table.
- **every** table has **`=1`** `name` **and** **`=1`** `role`, both nonempty strings. names are unique. a table may also carry **<=1** `journal_author`, an explicitly registered Journal account name using the Journal's Author format. provided Journal account names are unique; **other** additional keys **or** duplicate identities make the registry invalid.
- Author membership compares the carried `author` string with registered `name` values exactly, **without** aliases, case folding, trimming, **or** inference from filenames. `role` describes the Operator; it does **not** replace the name **or** independently grant execution permission.
- concrete Operator names **and** roles belong **only** **in** the Project's registry, **not** **in** reusable methodology **or** Tool code. a missing, unreadable, malformed, **or** stale registry leaves membership unresolved; it is **not** an empty valid registry.

## Details

The optional `journal_author` binds the Operator's registered display name to the account carried by Journal events. It does not change Atom Author membership or grant permission. An event account resolves only by an explicit `journal_author` match, or by a literal match with the registered `name` when no mapping is needed. Missing, duplicate or changed mappings leave command identity unresolved; Tools do not derive an account from a display name. Concrete mappings belong in the Project registry, not reusable Tool code.
