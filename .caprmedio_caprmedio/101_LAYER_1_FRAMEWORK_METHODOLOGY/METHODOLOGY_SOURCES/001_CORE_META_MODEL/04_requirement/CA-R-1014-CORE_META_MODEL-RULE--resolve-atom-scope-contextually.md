---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Local Scope Unit
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Author
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Scope
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Governed Subject
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
version: 32
updated_at: 2026-10-27 19:59:49 +0400
relations:
  child_of:
  - CA-R-1596
atom_id: CA-R-1014
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Resolve Atom Scope Contextually

## Scope

Atom Scope.

## Claim

an Atom Scope **must** include its current Scope Unit Scope **or** its Author's registered Operator fallback under CA-D-276-CORE_META_MODEL-DELIVERY--use-economical-yaml-frontmatter, its **`=1`** Atom Governed Subject, **and** **any** explicit Scope constraints **in** its Claim.

## Details
