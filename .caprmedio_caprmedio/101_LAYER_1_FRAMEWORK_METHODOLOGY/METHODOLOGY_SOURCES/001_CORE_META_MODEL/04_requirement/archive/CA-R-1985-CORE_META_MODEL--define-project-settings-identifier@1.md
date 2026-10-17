---
atom_id: CA-R-1985
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Continuant/Project.Settings.Identifier
relations:
  child_of:
  - CA-R-1174
version: 1
updated_at: "2026-10-17 17:51:06 +0400"
---
# Summary

Define Project.Settings.Identifier

## Scope

the identifier of a Project's authoritative Settings configuration.

## Claim

Project Settings Identifier identifies the Project's authoritative Settings configuration, **not** an Atom.

## Details

Evidence: CA-R-1738 defines Project Settings, CA-R-1401 keeps it outside the Atom type, and CA-D-362 supplies concrete identification. Candidate #6 decisions 11 and 18 preserve the Project path and distinguish Project identity from the delivered framework's name. This generic definition adds no filename, identifier spelling or duplicate Project Name setting.
