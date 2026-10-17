---
subjects:
  governs: "Entity/Continuant/Node/Atom.Summary"
  depends_on:
    ["Entity/Continuant/Node/Atom", "Entity/Continuant/Node/Atom.ID", "Entity/Continuant/Node/Atom.Substance"]
version: 8
updated_at: "2026-10-17 23:23:05 +0000"
relations: {}
atom_id: "CA-R-1464@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Keep Summary fixed for Atom identity

## Scope

the Summary of an Atom across its Revisions.

## Claim

an Atom **must** keep the Summary created with it across **all** of its Revisions. **if** its Summary needs a change, **then** it **must** be replaced by a new Atom with a new Atom ID, even **if** its Claim is unchanged.

## Details
