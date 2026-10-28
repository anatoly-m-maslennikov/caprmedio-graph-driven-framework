---
subjects:
  governs: Subject/Graph Rule/CCE Role Profile
  depends_on:
  - Subject/Graph Rule/CCE Role Profile
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - Subject/Graph Node/Domain/Continuant/Atom.Type
  - Subject/Graph Node/Domain/Continuant/Atom.Content
version: 18
updated_at: 2026-10-26 05:59:45 +0400
relations:
  child_of:
  - CA-M-307
atom_id: CA-M-308@18
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 6
type: Implementation Method
---
# Summary

Resolve the Effective CCE Role Profile

## Scope

effective CCE Role Profiles for Atom Claims.

## Claim

**to** resolve one effective CCE Role Profile for one Atom Claim, the Author **must** perform **all** of:

1. resolve the Atom's Content Role **before** selecting a profile.
2. **if** the Content Role is Plan, Requirement, Method, Evaluation, Delivery, **or** Operations, select the corresponding profile under CA-M-309 through CA-M-314.
3. apply an admitted Type profile **and** content-slot profile **after** the role profile; treat each narrower profile as a restriction **or** declared subordinate use, **not** as permission **to** change the role's primary contribution.
4. distinguish operators that express the primary Claim contribution from operators inside a condition, Definition of Done, input, result, failure, transition, representation, **or** another governed subordinate slot.
5. **if** the Content Role is Concern **or** Analysis, apply shared CCE **without** a role-specific profile.
6. **if** the Content Role is Implementation, return no registered CCE Role Profile **without** selecting a fallback profile **or** reporting role-profile conformance.
7. **if** the Content Role, Type, content slot, **or** applicable profile is unresolved, report the exact unresolved selection **and** do **not** report role-profile conformance.

## Details

the effective profile is derived from governed content classification. it is **not** another required Atom property.
