---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Continuant
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
version: 20
updated_at: 2026-10-27 19:59:56 +0400
relations:
  child_of:
  - CA-M-001
atom_id: CA-R-1502
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Keep Authority, Applicability, and Currentness distinct

## Scope

an Artifact's Authority, Applicability, and Currentness Properties.

## Claim

an Artifact's Authority, Applicability, **and** Currentness **must** remain distinct Properties under CA-R-1499, CA-R-1500, **and** CA-R-1501.

- an authoritative Artifact **may** be inapplicable **to** a given context.
- an applicable historical Revision **may** no longer be current.
- a current Projection **may** accurately report state **without** possessing semantic authority.

## Details

acceptance, provenance, Implementation, evidence, **and** Evaluation do **not** silently establish **any** of these Properties. precedence **and** conflict resolution select among **otherwise** authoritative **and** applicable Claims; they do **not** merge these Properties. the owning Requirement, Method, Evaluation, Delivery, **and** Operations Atoms govern how these Properties are resolved **and** reported through derived views.
