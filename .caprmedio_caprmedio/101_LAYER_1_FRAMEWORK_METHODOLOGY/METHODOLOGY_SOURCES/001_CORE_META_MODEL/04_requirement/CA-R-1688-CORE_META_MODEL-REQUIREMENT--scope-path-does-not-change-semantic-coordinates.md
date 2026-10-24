---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit.Path
  depends_on: []
version: 30
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-M-001
  - CA-R-1776
atom_id: CA-R-1688
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Scope path does not change semantic coordinates

## Scope

Scope paths in the current project.

## Claim

Scope path is a project-relative address containing **`>=0`** operator-labeled structural scopes ordered from broader parent **to** narrower child.

the current project is ambient. Scope **may** govern ownership, applicability, **and** inheritance, but it never changes stable Artifact identity, Artifact form, Content Role, **or** Governance locus.

## Details
