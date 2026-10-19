---
subjects:
  governs: "Entity/Node/Continuant/Scope Unit.Path"
  depends_on: []
version: 27
updated_at: "2026-10-19 11:42:05 +0000"
relations:
  child_of:
    - CA-M-001
    - CA-R-1776
atom_id: "CA-R-1688@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Scope path does not change semantic coordinates

## Scope

Scope paths in the current project.

## Claim

Scope path is a project-relative address containing **`>=0`** operator-labeled structural scopes ordered from broader parent **to** narrower child.

the current project is ambient. Scope **may** govern ownership, applicability, **and** inheritance, but it never changes stable Artifact identity, Artifact form, Content Role, **or** Governance locus.

## Details
