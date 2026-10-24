---
subjects:
  governs: Subject/Domain/Node/Continuant/Term//Artifact
  depends_on:
  - Artifact/Authority
  - Artifact/Applicability
  - Artifact/Currentness
  - Artifact/Revision
  - Subject/Domain/Node/Continuant/Projection
  - Provenance
  - 'Atom/Content Role: Implementation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Domain/Node/Continuant/Atom.Substance
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations'
version: 13
updated_at: 2026-10-24 01:37:42 +0400
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
