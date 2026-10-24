---
subjects:
  governs: Work Journal/Event/Carrier Serialization
  depends_on:
  - Work Journal/Event
  - Atom/Identifier
  - Atom/Revision
  - Subject/Engineering/Carrier
version: 13
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-D-435@13
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 3
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
