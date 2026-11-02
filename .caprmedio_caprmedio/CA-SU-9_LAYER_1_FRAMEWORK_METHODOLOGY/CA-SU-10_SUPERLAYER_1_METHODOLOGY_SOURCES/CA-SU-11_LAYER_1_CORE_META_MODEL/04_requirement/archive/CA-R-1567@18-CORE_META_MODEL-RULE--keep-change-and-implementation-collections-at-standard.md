---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Projection
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
version: 18
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-R-1378
  - CA-R-1578
atom_id: CA-R-1567@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Keep Change and Implementation collections at Standard

## Scope

Atom Collections and decomposition views grouping CAPO or I content.

## Claim

an Atom Collection **or** decomposition view grouping CAPO **or** I content **must** remain a derived grouping and **must not** acquire an Atom Tier or imply a Tier from its grouped Content Roles or Types. When a view displays a source Atom, it preserves that source Atom's numeric Tier; the grouping itself has no independent Tier.

nesting expresses composition, **not** Core **or** General authority; a Plan Directory Carrier remains a Carrier of its existing Atom under CA-D-460-CORE_META_MODEL-ENG_DECISION--serialize-plan-atom-carrier-bundles, **not** an independently tiered collection **or** second Atom.

## Details
