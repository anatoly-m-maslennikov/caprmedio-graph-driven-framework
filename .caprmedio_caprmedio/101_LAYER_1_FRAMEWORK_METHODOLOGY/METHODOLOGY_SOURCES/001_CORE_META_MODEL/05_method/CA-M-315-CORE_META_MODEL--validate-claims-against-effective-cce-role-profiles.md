---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Controlled English
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Type
version: 20
updated_at: 2026-10-27 19:59:42 +0400
relations:
  child_of:
  - CA-M-307
  - CA-M-308
atom_id: CA-M-315
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 7
type: Implementation Method
---
# Summary

Validate Claims against Effective CCE Role Profiles

## Scope

Atom Claims against effective CCE Role Profiles.

## Claim

**to** validate one Atom Claim against its effective CCE Role Profile, the Validator **must** perform **all** of:

1. resolve the effective profile under CA-M-308 **without** inferring a different Content Role from the wording under review.
2. identify the Claim's primary contribution, every subordinate content slot, **and** every registered CCE Operator occurrence.
3. verify that the primary contribution matches the resolved role profile **and** that every narrower Type **or** content-slot contribution remains within its admitted boundary.
4. verify that every CCE Operator use is permitted for its exact primary **or** subordinate context **and** has explicit logical scope.
5. reject a primary contribution owned by another Content Role even **when** every individual CCE Operator is present **in** the global registry.
6. for Concern **or** Analysis, validate shared CCE **and** their governed Content Role meaning **without** requiring a role-specific profile.
7. for Implementation content, report that no CCE Role Profile is registered; do **not** apply another role's profile **or** report role-profile conformance.
8. report every mismatch by Content Role, Type, content slot, primary contribution, **and** Operator occurrence. do **not** rewrite the source Claim **or** report conformance while one required classification remains unresolved.

## Details

global CCE Operator registration is necessary but insufficient for role-profile conformance.
