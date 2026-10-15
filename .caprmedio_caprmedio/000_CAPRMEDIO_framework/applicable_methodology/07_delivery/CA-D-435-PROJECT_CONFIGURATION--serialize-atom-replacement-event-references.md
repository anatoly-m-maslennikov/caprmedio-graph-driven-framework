---
subjects:
  governs: "Work Journal/Event/Carrier Serialization"
  depends_on:
    - "Work Journal/Event"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Carrier"
version: 10
updated_at: "2026-10-14 18:37:38 +0400"
relations: {}
atom_id: "CA-D-435"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-435-PROJECT_CONFIGURATION--serialize-atom-replacement-event-references.md
  source_atom_id: CA-D-435
  source_atom_revision: 10
  source_sha256: 470e466c21c59bebf0a2a5abd431a8abcdaeedde4785176c86360164a2f736da
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Atom replacement event references

## Scope

Actual Atom replacement references supplied for Journal recording.

## Claim

Journal serialization **must** preserve the actually supplied predecessor **and** successor Atom references of a replacement observation, including `predecessor_atom_id` **and** `successor_atom_ids` **when** supplied.

- preserve reference values **and** array order as data through safe encoding. array order does **not** establish priority **or** execution order.
- do **not** look up an earlier Journal record, require a predecessor chain, compute a digest, validate the replacement **or** fabricate a baseline **to** append these observations.
- absence of replacement references does **not** establish whether the action was a replacement. do **not** infer missing identities, successors **or** historical facts.
- existing records remain readable **without** rewriting their fields, selected representation **or** observed values. legacy **or** nonconforming values remain observations, **not** certified replacements.
- actual source replacement, exact predecessor history **and** successor correctness remain independently governed by CA-R-807 **and** CA-E-462. Journal append **or** read grants no source-effect permission **and** proves none of those conditions.

## Details
