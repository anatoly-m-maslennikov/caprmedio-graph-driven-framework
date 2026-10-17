---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Plan"]
version: 8
updated_at: "2026-10-16 12:08:30 +0000"
relations: {"relates_to": ["CA-R-1536", "CA-R-1579"]}
atom_id: "CA-R-1537"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1537-CORE_META_MODEL-CORE-REQUIREMENT--derive-recursive-plan-decomposition-by-transitive-closure.md
  source_atom_id: CA-R-1537
  source_atom_revision: 8
  source_sha256: 4a16ad8e315d878ae03c2a33633e7d39035a96cb8f486ee6d2d48fecb841fd07
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Recursive Plan Decomposition by Transitive Closure

## Scope

recursive Plan work decomposition derived from direct `DECOMPOSES_INTO` Relations.

## Claim

recursive Plan work decomposition **means** the transitive closure of direct `DECOMPOSES_INTO` Relations; it **must not** be authored as a second direct relation set.

## Details
