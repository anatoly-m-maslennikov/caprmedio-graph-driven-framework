---
subjects:
  governs: "Entity/Carrier/File Carrier.Filename"
  depends_on:
    ["Entity/Continuant/Object/Atom.ID"]
version: 17
updated_at: "2026-10-16 12:09:13 +0000"
relations: {}
atom_id: "CA-D-288"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-288-CORE_META_MODEL-DELIVERY--serialize-draft-atom-filenames-with-an-empty-number.md
  source_atom_id: CA-D-288
  source_atom_revision: 17
  source_sha256: 04cd139d94ed3c25f78053d70f2a8ae2451e0ead4ea6cb3d321b3fbf570e9306
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Serialize Draft Atom Filenames with an Empty Number

## Scope
Project-owned Draft Atom filenames.

## Claim

Outside the explicit Subjects-only edit-draft exception below, **every** Project-owned Draft Atom filename **must** use `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>--` **before** its mutable components **and** **must not** carry an assigned Atom ID.

## Details

### Subjects-only edit-draft exception

CA-D-446's explicit source-pinned Subjects-only edit draft is a derived proposed next Revision of an existing Atom, not a new Atom Draft or another canonical original. It may carry the temporary `atom_id: <canonical-ID>@draft`, `status: Draft`, and matching temporary-ID filename in the owning role's `draft/` folder while the exact canonical source remains untouched. The reviewed packet retains the canonical target/source pin and exact draft path/digest for that specific proposed edit. Approval restores the canonical ID and original Status, independently validates normalized Subjects-only materialization, and uses the existing exact predecessor archive plus N+1/actual-time update. Staging and publication require no retained Draft-history entry, `revision_lineage`, unique Draft head, origin chain or consuming successor. New-Atom Drafts and ordinary lifecycle Drafts remain ID-free; canonical ID grammar and the normal source, schema, identity/collision, permission and exact actual-history safeguards are unchanged.
