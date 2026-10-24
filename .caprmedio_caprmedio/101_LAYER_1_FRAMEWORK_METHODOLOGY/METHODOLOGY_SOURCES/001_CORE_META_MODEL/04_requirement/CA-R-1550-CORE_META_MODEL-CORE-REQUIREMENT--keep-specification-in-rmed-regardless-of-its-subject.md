---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom/Content Role
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/Selection
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Implementation
  - Subject/Domain/Node/Continuant/Atom.Subjects
version: 13
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-R-1531
  - CA-R-1548
  - CA-R-1549
  - CA-R-1343
atom_id: CA-R-1550
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Keep specification in RMED regardless of its Subject

## Scope

specification Claims about Change **or** Implementation content.

## Claim

a specification Claim about Change **or** Implementation content **must** remain **in** Spec Content Roles according **to** its own contribution rather than inherit the Content Role of the content it specifies.

## Details
