---
version: 15
updated_at: 2026-10-24 11:58:20 +0400
relations:
  child_of:
  - CA-R-1487
  method_for:
  - CA-R-1487
subjects:
  governs: Subject/Domain/Node/Continuant/Selection//PROJECT_LEXICOGRAPHIC
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Selection//PROJECT_PRIORITY_MODEL
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
atom_id: CA-M-297@15
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 4
type: Implementation Method
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
