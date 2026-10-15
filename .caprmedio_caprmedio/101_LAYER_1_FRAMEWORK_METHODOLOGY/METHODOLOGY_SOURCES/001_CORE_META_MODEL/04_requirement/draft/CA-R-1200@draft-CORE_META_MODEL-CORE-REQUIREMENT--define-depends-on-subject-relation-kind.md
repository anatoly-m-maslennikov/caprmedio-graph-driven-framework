---
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    ["Relation Kind", "Atom", "Subject", "Atom/Content Role: Plan/Type: Plan", "Entity", "Atom.Substance", "Workflow"]
version: 17
updated_at: "2026-10-15 12:10:45 +0000"
relations: {}
atom_id: "CA-R-1200@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define DEPENDS_ON Subject Relation Kind

## Scope

the DEPENDS_ON Subject Relation Kind of an Atom.

## Claim

DEPENDS_ON **means** the direct Subject Relation Kind from an Atom **to** a canonical Entity mentioned **in** its Markdown Main Content other than its GOVERNS target. this reference does **not** make the Claim authoritative about that Entity.

## Details

mentions **in** Summary, Scope, Claim, Details, other registered body sections, tables, **and** examples count. this Relation does **not** establish Workflow control flow **or** execution order; Plan start prerequisites remain separately governed by `BLOCKS` under CA-R-1580-CORE_META_MODEL-CORE-REQUIREMENT--define-plan-blocking.
