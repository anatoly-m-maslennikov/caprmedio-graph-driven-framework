---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Local Scope Unit
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Author
  - Subject/Domain/Node/Continuant/Scope Unit.Scope
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Atom.Governed Subject
  - Subject/Domain/Node/Continuant/Atom.Substance
version: 27
updated_at: 2026-10-24 02:14:24 +0400
relations:
  child_of:
  - CA-R-1596
atom_id: CA-R-1014@27
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
