---
subjects:
  governs: "Projection/Type: Canonical Scope Signature"
  depends_on:
    ["Canonical Scope Signature", "Carrier"]
version: 13
updated_at: "2026-10-15 12:05:43 +0000"
relations:
  child_of:
    - CA-D-266
atom_id: "CA-D-347@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
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
