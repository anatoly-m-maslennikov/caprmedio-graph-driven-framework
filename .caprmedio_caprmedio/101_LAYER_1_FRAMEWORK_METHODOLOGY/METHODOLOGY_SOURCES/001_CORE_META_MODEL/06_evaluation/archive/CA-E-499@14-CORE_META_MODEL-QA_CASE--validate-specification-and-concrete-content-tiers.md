---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Tier
  depends_on:
  - Spec Content Roles
  - Change Content Roles
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Subject/Domain/Node/Continuant/Atom.Tier
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - Implementation
  - Container Atom
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom.Tier: 3 / Standard'
version: 14
updated_at: 2026-10-24 00:38:25 +0400
relations:
  evaluation_for:
  - CA-R-2127
  - CA-R-2128
  - CA-R-1567
  - CA-R-1568
  - CA-R-1571
  - CA-M-437
  - CA-D-652
atom_id: CA-E-499@14
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: QA Case
tier: 3
---
# Summary

Validate Specification **and** concrete content tiers

## Scope

classification of specification authority and concrete content tiers.

## Claim

the tier Evaluation **must** reject classification that confuses specification authority with the content it governs.

### Numeric tier fixtures

- classify an Atom from its complete Claim, owner Scope Unit, and the applicable definition; use numeric Tier `0` for an admitted Project Principle, Tier `1` for Core, Tier `2` for General, Tier `3` for Standard, and `-1` only for a Project-owned Goal.
- permit ordinary Project Atoms at Tier `0` or higher and non-Project Atoms at Tier `1` or higher; do not infer a tier from reuse, nesting, importance, filename labels, Content Role, or Type.
- preserve the source Atom's numeric Tier in a Projection or other derived carrier; the derived carrier does not acquire an independent Atom Tier.
- evaluate every stored governing RMED relation occurrence under CA-R-2149: a same-Scope target has a strictly lower Tier, while a strict-ancestor target is governed without comparing Tiers; descendant and sibling targets fail. Stored source-to-target direction is authoritative and derived inverses are excluded.
- unresolved owner, Scope ancestry, endpoint Tier, or registered relation membership remains unresolved and is not treated as a pass; no default Tier is applicable.
- no Content Role or Type restriction authorizes or forbids a numeric Tier; any role/type classification must still follow the complete Claim and the applicable definition.

## Details
