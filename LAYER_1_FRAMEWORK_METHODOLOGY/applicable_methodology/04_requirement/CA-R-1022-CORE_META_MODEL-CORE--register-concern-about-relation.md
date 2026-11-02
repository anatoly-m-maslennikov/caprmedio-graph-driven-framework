---
subjects:
  governs: "Concern About Relation"
  depends_on:
    - "atom-boundary"
    - "relation-model"
version: 17
updated_at: "2026-10-20T12:49:16.615Z"
relations: {}
atom_id: "CA-R-1022"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1022-CORE_META_MODEL-CORE--register-concern-about-relation.md
  source_atom_id: CA-R-1022
  source_atom_revision: 17
  source_sha256: 1db2ca7916410f89d2cfda9c5defd8c641257c4585ca89233b4361da02586207
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Register concern_about relation

## Scope

`concern_about` relations.

## Claim

`concern_about` **must** be registered as a direct relation owned by a Concern Atom **and** directed **to** one Observation **or** other directly affected governed entity.

for mechanical Atom-target admission, **any** valid Atom Content Role **must** be eligible **when** the admitted reference context uniquely resolves the target as a valid canonical Current Atom. Current is the non-Draft, non-Archived lifecycle group and includes all admitted Current statuses, not only Active. Draft and Archived targets **must not** be admitted as Current relation targets. an Atom ID string alone **must not** establish target validity. whether the target is genuinely affected remains a semantic judgment outside mechanical validation.

## Details

This mechanical admission preserves identity, carried Content Role, Version, admitted Current Status, reference uniqueness and canonical-representation checks. It does not limit eligible Atom targets to an Observation Type, assert actual affectedness, or define admission for unresolved non-Atom entity representations.
