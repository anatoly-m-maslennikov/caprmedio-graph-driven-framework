---
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Canonical Scope Signature"
  depends_on:
    ["Entity/Node/Continuant/Projection/Type: Canonical Scope Signature", "Entity/Carrier"]
version: 16
updated_at: "2026-10-19 15:55:32 +0400"
relations:
  child_of:
    - CA-D-266
atom_id: CA-D-347@16
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Deliver Canonical Scope Signatures as External Report Projections

## Scope

external report Projections that deliver Canonical Scope Signatures.

## Claim

**every** Canonical Scope Signature Projection **must** be delivered as **`=1`** non-authoritative JSON report under its Project's `.caprmedio_<project_name>/_projection/` Directory Carrier with the selected source frontier digest, **every** source Atom identity **and** revision, source Carrier digest, source Scope Expression occurrence, Canonical Scope Signature, **and** exclusion diagnostic; the Projection **must not** become an Atom Carrier, modify a selected source Carrier, establish Claim equivalence, **or** create a dependency relation.

## Details
