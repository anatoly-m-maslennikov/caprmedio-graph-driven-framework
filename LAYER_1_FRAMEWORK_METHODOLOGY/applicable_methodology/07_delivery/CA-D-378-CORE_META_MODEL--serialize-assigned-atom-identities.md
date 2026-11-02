---
subjects:
  governs: "Entity/Node/Continuant/Atom.ID"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role", "Entity/Node/Continuant/Project", "Entity/Node/Continuant/Atom/Content Role: Plan.ID"]
version: 16
updated_at: "2026-10-20 21:17:20 +0400"
relations: {}
atom_id: "CA-D-378"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-378-CORE_META_MODEL--serialize-assigned-atom-identities.md
  source_atom_id: CA-D-378
  source_atom_revision: 16
  source_sha256: d4e6f0569f81a54f434d060ea6e2a271dea51611a66a1afd0f6a10ca127c7562
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Assigned Atom Identities

## Scope

assigned Atom IDs.

## Claim

**every** assigned Current or Archived Atom ID **must** begin with the registered uppercase Project identity prefix. the canonical Project-owned Atom ID encoding **must** match `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>`. For a Draft, `atom_id` **may** be omitted or use a Draft-only marker: `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-draft` for a new Atom, `<canonical-ID>@<proposed-version>-draft` for a new version of an existing Atom, or the compatible `<canonical-ID>@draft` form. These markers are permitted on a carried Draft source, not a Current source. Exact archived predecessor bytes remain governed by actual-history preservation and are not normalized by this rule. The role-only new-Atom marker allocates no canonical number. the Atom Content Role Identity Letter **must** be **in** (Concern: C, Analysis: A, Plan: P, Requirement: R, Method: M, Evaluation: E, Delivery: D, Implementation: I, Operations: O). a `<PROJECT_PREFIX>-P` Identifier **must** identify a Plan Atom, including one labeled Epic, **and** **must not** identify a separate non-Atom collection.

## Details
