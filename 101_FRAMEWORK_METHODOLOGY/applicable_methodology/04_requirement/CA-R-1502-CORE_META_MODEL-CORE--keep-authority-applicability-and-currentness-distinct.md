---
subjects:
  governs: "Artifact"
  depends_on:
    ["Artifact/Authority", "Artifact/Applicability", "Artifact/Currentness", "Artifact/Revision", "Entity/Continuant/Projection", "Provenance", "Atom/Content Role: Implementation", "Entity/Continuant/Object/Atom/Content Role: Evaluation", "Property", "Atom/Claim", "Entity/Continuant/Object/Atom/Content Role: Requirement", "Entity/Continuant/Object/Atom/Content Role: Method", "Entity/Continuant/Object/Atom/Content Role: Delivery", "Entity/Continuant/Object/Atom/Content Role: Operations"]
version: 6
updated_at: "2026-10-15 18:43:44 +0000"
relations: {child_of: [CA-M-001]}
atom_id: "CA-R-1502"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1502-CORE_META_MODEL-CORE--keep-authority-applicability-and-currentness-distinct.md
  source_atom_id: CA-R-1502
  source_atom_revision: 6
  source_sha256: 9320d383dd9208db76c1928a557c024b46ce0479f8d54fe6041c6161a0651a09
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
