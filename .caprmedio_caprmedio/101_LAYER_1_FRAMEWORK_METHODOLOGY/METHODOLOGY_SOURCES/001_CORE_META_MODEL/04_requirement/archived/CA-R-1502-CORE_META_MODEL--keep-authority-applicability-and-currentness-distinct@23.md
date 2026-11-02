---
subjects:
  governs: Entity/Object/Continuant
  depends_on:
  - Entity
  - Entity/Object/Continuant/Projection
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - Entity/Object/Continuant/Term//Property
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations'
version: 23
updated_at: 2026-10-30 01:32:01 +0400
relations:
  child_of:
  - CA-M-447
atom_id: CA-R-1502
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary
Keep Authority, Applicability, and Currentness distinct

## Claim scope

an Artifact's Authority, Applicability, and Currentness Properties.

## Claim

an Artifact's Authority, Applicability, **and** Currentness **must** remain distinct Properties under CA-R-1499, CA-R-1500, **and** CA-R-1501.

- an authoritative Artifact **may** be inapplicable **to** a given context.
- an applicable historical Revision **may** no longer be current.
- a current Projection **may** accurately report state **without** possessing semantic authority.

## Details

acceptance, provenance, Implementation, evidence, **and** Evaluation do **not** silently establish **any** of these Properties. precedence **and** conflict resolution select among **otherwise** authoritative **and** applicable Claims; they do **not** merge these Properties. the owning Requirement, Method, Evaluation, Delivery, **and** Operations Atoms govern how these Properties are resolved **and** reported through derived views.
