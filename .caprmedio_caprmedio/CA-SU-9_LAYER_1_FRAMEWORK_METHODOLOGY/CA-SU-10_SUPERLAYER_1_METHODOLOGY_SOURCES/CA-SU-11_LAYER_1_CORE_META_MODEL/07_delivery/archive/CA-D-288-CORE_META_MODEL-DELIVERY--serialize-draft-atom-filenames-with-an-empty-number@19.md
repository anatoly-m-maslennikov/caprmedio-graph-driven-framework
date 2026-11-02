---
subjects:
  governs: "Entity/Carrier/File Carrier.Filename"
  depends_on:
    ["Entity/Node/Continuant/Atom.ID"]
version: 19
updated_at: "2026-10-19 15:55:23 +0400"
relations: {}
atom_id: "CA-D-288"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
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
