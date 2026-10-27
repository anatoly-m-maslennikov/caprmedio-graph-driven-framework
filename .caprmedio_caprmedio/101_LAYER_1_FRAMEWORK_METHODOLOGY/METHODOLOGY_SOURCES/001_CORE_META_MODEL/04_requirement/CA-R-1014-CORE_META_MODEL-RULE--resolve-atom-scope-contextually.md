---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Local Scope Unit
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Author
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Scope
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Atom.Governed Subject
  - Subject/Graph Node/Domain/Continuant/Atom.Content
version: 31
updated_at: 2026-10-25 17:32:27 +0400
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
