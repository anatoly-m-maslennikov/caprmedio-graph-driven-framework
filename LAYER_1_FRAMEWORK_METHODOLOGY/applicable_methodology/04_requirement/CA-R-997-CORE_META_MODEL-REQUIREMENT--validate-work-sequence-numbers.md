---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan.Work Sequence Number"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Node/Continuant/Atom/Content Role: Plan.Work Sequence Number"]
version: 22
updated_at: "2026-10-19 15:54:39 +0400"
relations:
  child_of:
    - CA-R-991
    - CA-R-992
atom_id: "CA-R-997"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-997-CORE_META_MODEL-REQUIREMENT--validate-work-sequence-numbers.md
  source_atom_id: CA-R-997
  source_atom_revision: 22
  source_sha256: bc6753e82ac06c07423e9d20b7ad30fb498b86c4a83f99e0f2b948d99940711e
  original_relations_sha256: 84d32a87616b0ba20eb7e61228c75eef35f9218c63f3b6b448b4cf6624bb5430
---
# Summary

Validate Work Sequence Numbers

## Scope

supplied Work Sequence Numbers for direct Plans decomposing the same Hub or sharing the same top-level Plan container.

## Claim

**every** supplied Work Sequence Number **must** be a unique positive ordinal among direct Plans decomposing the same Hub **or** sharing the same top-level Plan container.

## Details
