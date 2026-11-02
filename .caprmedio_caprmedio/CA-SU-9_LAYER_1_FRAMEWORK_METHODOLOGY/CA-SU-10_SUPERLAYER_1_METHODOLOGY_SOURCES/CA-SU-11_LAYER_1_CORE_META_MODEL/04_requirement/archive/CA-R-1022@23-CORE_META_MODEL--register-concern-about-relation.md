---
subjects:
  governs: 'Subject/Graph Relation/Type: concern_about'
  depends_on:
  - Subject/Graph Relation
version: 23
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1022@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
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
