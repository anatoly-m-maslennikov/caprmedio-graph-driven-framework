---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action"
  depends_on:
    ["Entity/Node/Continuant/Actor", "Tool", "Atom/Content Role: Plan/Type: Plan", "Entity/Node/Continuant/History/Journal.Record", "Entity/Carrier", "Atom/Content Role: Operations/Type: Action/Execution Kind", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom.Substance"]
version: 13
updated_at: "2026-10-19 15:53:08 +0400"
relations: {}
atom_id: "CA-R-1452"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1452-CORE_META_MODEL-CORE--define-action.md
  source_atom_id: CA-R-1452
  source_atom_revision: 13
  source_sha256: c7e1900c89f21167c58d7169c51968bffa7bc8d7a1fc87d6de39c0afff00cd70
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Action

## Scope

the definition of an Action.

## Claim

an Action **means** an Atom with Content Role Operations **and** Type Action whose Claim specifies one reusable operational building block with an explicit operational contribution **and** a justified boundary at the modeled responsibility **and** granularity **where** further division has no useful independently governed meaning. this atomic boundary is **not** a count of machine instructions **or** Tool calls; an arbitrary large procedure **without** that justified boundary is **not** an Action. the Action is distinct from an Actor, a Tool, a Task, a particular execution, a Journal Record, **and** a Carrier. its execution kind is defined under CA-R-1526; an Agentic Action **may** use Tools **without** making **every** call another Action **or** Step.

## Details
