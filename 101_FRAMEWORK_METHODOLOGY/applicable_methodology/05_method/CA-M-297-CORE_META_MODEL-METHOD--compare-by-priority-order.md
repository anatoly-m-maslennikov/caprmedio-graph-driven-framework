---
version: 5
updated_at: "2026-10-14 13:43:24 +0400"
relations:
  child_of:
    - CA-R-1487
  method_for:
    - CA-R-1487
subjects:
  governs: "Project/lexicographic selection"
  depends_on:
    - "Operator"
    - "Project/priority model application"
    - "Atom/Content Role: Method"
atom_id: "CA-M-297"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-297-CORE_META_MODEL-METHOD--compare-by-priority-order.md
  source_atom_id: CA-M-297
  source_atom_revision: 5
  source_sha256: d0876b921ff057c06f8afa643c9a9480752c88bb9d0b87f97ace55f704971518
  original_relations_sha256: 281ec85f44ff131b99377546943617cbfcfbf23e636c242eb0d23f43d42db629
---
# Summary

Compare by priority order

## Scope

priority-order comparison of admissible alternatives.

## Claim

**when** the Operator selects comparison by priority order, the comparison of admissible alternatives **must** use the resolved order of active, applicable criteria as follows:

- an earlier criterion takes precedence over a later criterion.
- for alternatives tied on **all** earlier criteria, the first criterion that distinguishes them determines their relative preference.
- later criteria **must not** override a preference established by an earlier criterion.
- alternatives tied on **all** applicable criteria remain tied.
- an incomplete criterion order **or** an incomparable result at the current deciding criterion leaves the comparison unresolved; a later criterion **must not** bypass that gap.

this Method defines the comparison technique, **not** priority activation, alternative-selection execution, **or** escalation.

## Details
