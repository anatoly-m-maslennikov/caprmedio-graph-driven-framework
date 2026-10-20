---
subjects:
  governs: "Concern About Relation"
  depends_on:
    - "atom-boundary"
    - "relation-model"
version: 16
updated_at: "2026-10-20 16:28:10 +0400"
relations: {}
atom_id: "CA-R-1022"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Register concern_about relation

## Scope

`concern_about` relations.

## Claim

`concern_about` **must** be registered as a direct relation owned by a Concern Atom **and** directed **to** one Observation **or** other directly affected governed entity.

for mechanical Atom-target admission, **any** valid Atom Content Role **must** be eligible **when** the admitted reference context uniquely resolves the target as a valid canonical Atom Revision. an Atom ID string alone **must not** establish target validity. whether the target is genuinely affected remains a semantic judgment outside mechanical validation.

## Details

This mechanical admission preserves identity, carried Content Role, Revision, reference uniqueness and canonical-representation checks. It does not limit eligible Atom targets to an Observation Type, assert actual affectedness, or define admission for unresolved non-Atom entity representations.
