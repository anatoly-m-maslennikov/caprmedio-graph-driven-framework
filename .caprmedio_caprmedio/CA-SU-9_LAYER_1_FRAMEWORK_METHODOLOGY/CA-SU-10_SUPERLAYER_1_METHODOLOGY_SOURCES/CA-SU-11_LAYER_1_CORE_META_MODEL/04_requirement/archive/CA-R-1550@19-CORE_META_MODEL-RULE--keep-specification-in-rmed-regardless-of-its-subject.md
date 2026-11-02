---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom/Content Role
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Selection
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Domain/Continuant/Atom.Subjects
version: 19
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-R-1531
  - CA-R-1548
  - CA-R-1549
atom_id: CA-R-1550@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
