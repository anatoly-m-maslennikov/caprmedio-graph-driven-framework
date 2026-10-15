---
subjects:
  governs: "Atom/Revision/Status: Draft/Filename"
  depends_on:
    - "Atom/Identifier"
version: 13
updated_at: "2026-10-15 10:01:40 +0000"
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
  source_atom_revision: 13
  source_sha256: e87fe9790b230fbc372d14306132455a52ab51b8a895ab9ecefe821d38162ada
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

CA-D-446's explicit source-pinned Subjects-only edit draft is a derived proposed next Revision of an existing Atom, not a new Atom Draft or another canonical original. It may carry the temporary `atom_id: <canonical-ID>@draft`, `status: Draft`, and matching temporary-ID filename in the owning role's `draft/` folder while the exact canonical source remains untouched. The reviewed packet retains the canonical target/source pin and exact draft path/digest; this is the narrow provenance basis for this proposal, not ordinary Draft identity allocation or retained-head promotion. No additional `revision_lineage` or demotion history is created just to stage it. Approval restores the canonical ID and original Status, independently validates normalized Subjects-only materialization, and uses the existing exact predecessor archive plus N+1/actual-time update. New-Atom Drafts and ordinary lifecycle Drafts remain ID-free and subject to their existing lineage rules; canonical ID grammar is unchanged.
