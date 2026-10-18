---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Plan.Assignee"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Plan", "Entity/Continuant/Node/Actor/Type: AI Agent"]
version: 8
updated_at: "2026-10-18 03:33:42 +0400"
relations: {"relates_to": ["CA-R-1584"]}
atom_id: "CA-R-1585"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1585-CORE_META_MODEL-GENERAL-REQUIREMENT--default-plan-work-assignment-to-an-ai-agent.md
  source_atom_id: CA-R-1585
  source_atom_revision: 8
  source_sha256: ad257a040796137cf27c1c785d35b28493f8be9660a946a616ba771a46f0ab6a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Default Plan work assignment to an AI Agent

## Scope

a Plan Atom with its own work and no explicit Assignee.

## Claim

**if** a Plan Atom has its own work **and** no explicit Assignee, **then** its effective Assignee **must** be **=1** AI Agent selected **to** execute that work.

## Details
