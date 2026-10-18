---
subjects:
  governs: "Entity/Continuant/Actor/Type: AI Agent"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Actor/Type: AI Agent", "Scripted Migration", "Target Set"]
version: 6
updated_at: "2026-10-15 18:44:18 +0000"
relations: {}
atom_id: "CA-R-1554"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1554-CORE_META_MODEL-GENERAL-REQUIREMENT--bound-scripted-migrations.md
  source_atom_id: CA-R-1554
  source_atom_revision: 6
  source_sha256: 0159873839aaf55b5601768b4192cf26528293272a216b5220161ae7d2510ca4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Bound Scripted Migrations

## Scope

AI Agent participation in Scripted Migrations.

## Claim

an AI Agent that performs a Scripted Migration **must** satisfy **all** of these participation conditions:

- bind the migration **to** an exact governed Target Set;
- fail **when** an expected target is absent;
- produce a reviewable change set.

these conditions constrain the AI Agent's participation; they do **not** define the migration's Steps **or** Workflow control flow **or** grant additional mutation authority.

## Details
