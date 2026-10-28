---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Controlled English
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Type
version: 20
updated_at: 2026-10-27 19:59:41 +0400
relations:
  child_of:
  - CA-M-113
  - CA-M-230
  - CA-M-234
atom_id: CA-M-307
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 5
type: Implementation Method
---
# Summary

Define Content-role-specific CCE Profiles

## Scope

CCE Role Profiles.

## Claim

a CCE Role Profile **means** one restriction of shared CCE that identifies the permitted primary Claim contribution, permitted CCE Operator uses, permitted subordinate content slots, **and** prohibited primary contributions for one Content Role **or** one narrower Type **or** content slot.

the current role-specific profiles apply **only** **to** Plan, Requirement, Method, Evaluation, Delivery, **and** Operations Atoms.

Concern **and** Analysis Claims remain subject **to** shared CCE **without** an additional CCE Role Profile. this absence does **not** exempt them from shared CCE **or** authorize normative authority outside their Content Role meanings.

no CCE Role Profile is currently registered for Implementation because the current source set contains no Implementation Atoms. an absent Implementation profile **must not** be replaced by another role's profile **or** treated as role-profile conformance.

a narrower Type **or** content-slot profile **may** restrict its parent role profile **and** define permitted subordinate operator use, but it **must not** change the primary contribution of the Content Role.

## Details
