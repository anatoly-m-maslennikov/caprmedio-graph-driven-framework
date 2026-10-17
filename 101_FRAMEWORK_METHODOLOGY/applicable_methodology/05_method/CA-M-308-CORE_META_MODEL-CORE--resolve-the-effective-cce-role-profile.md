---
subjects:
  governs: "CCE Role Profile"
  depends_on:
    ["CCE Role Profile", "Atom/Content Role", "Type", "Entity/Continuant/Object/Atom.Substance"]
version: 6
updated_at: "2026-10-15 18:48:35 +0000"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-M-309
    - CA-M-310
    - CA-M-311
    - CA-M-312
    - CA-M-313
    - CA-M-314
atom_id: "CA-M-308"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-308-CORE_META_MODEL-CORE--resolve-the-effective-cce-role-profile.md
  source_atom_id: CA-M-308
  source_atom_revision: 6
  source_sha256: 9fcf6afd0bf38b1034abdda663088f503ec1d0aea63413b9bd16caf65ffd68dd
  original_relations_sha256: ecf15d66e52790b11397217f00000f28e01dedab7a7136802d07e978204bdbb7
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
