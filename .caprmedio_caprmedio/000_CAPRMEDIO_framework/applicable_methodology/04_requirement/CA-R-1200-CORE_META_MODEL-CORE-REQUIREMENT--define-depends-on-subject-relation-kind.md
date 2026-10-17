---
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    ["Relation Kind", "Entity/Continuant/Object/Atom", "Subject", "Atom/Content Role: Plan/Type: Plan", "Entity", "Entity/Continuant/Object/Atom.Substance", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow"]
version: 18
updated_at: "2026-10-15 18:41:10 +0000"
relations: {}
atom_id: "CA-R-1200"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1200-CORE_META_MODEL-CORE-REQUIREMENT--define-depends-on-subject-relation-kind.md
  source_atom_id: CA-R-1200
  source_atom_revision: 18
  source_sha256: bf69dc257dbacf4cc18dad33aa4ad966c0113c5c7cf720dcb032038795e2350d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define DEPENDS_ON Subject Relation Kind

## Scope

the DEPENDS_ON Subject Relation Kind of an Atom.

## Claim

DEPENDS_ON **means** the direct Subject Relation Kind from an Atom **to** a canonical Entity mentioned **in** its Markdown Main Content other than its GOVERNS target. this reference does **not** make the Claim authoritative about that Entity.

## Details

mentions **in** Summary, Scope, Claim, Details, other registered body sections, tables, **and** examples count. this Relation does **not** establish Workflow control flow **or** execution order; Plan start prerequisites remain separately governed by `BLOCKS` under CA-R-1580-CORE_META_MODEL-CORE-REQUIREMENT--define-plan-blocking.
