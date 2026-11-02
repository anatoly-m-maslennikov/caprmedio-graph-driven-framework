---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan.Status: Done"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Node/Continuant/Atom/Content Role: Plan.Definition of Done", "Entity/Carrier/File Carrier"]
version: 10
updated_at: "2026-10-19 15:53:36 +0400"
relations: {"relates_to": ["CA-R-1575", "CA-R-1579", "CA-R-1599", "CA-R-1539"]}
atom_id: "CA-R-1583"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1583-CORE_META_MODEL-CORE-REQUIREMENT--define-plan-completion.md
  source_atom_id: CA-R-1583
  source_atom_revision: 10
  source_sha256: c94e1b69e37d1f6556a4f66ecf6c078dd77acd7490bbc9d120fa3392d047486e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Plan completion

## Scope

Plan completion.

## Claim

Plan Status Done **means** that **all** applicable completion conditions hold:

- the Plan satisfies CA-R-1575; absence of work **and** decomposition **must not** count as completion.
- its own work, **if** present, is complete.
- **every** directly decomposed Plan is Done.
- its Definition of Done falsifying Condition Expression evaluates **to** false.

a Hub requires its own Definition of Done **and** completion of its decomposed Plans; Canceled **or** Archived work does **not** satisfy Done.

## Details
