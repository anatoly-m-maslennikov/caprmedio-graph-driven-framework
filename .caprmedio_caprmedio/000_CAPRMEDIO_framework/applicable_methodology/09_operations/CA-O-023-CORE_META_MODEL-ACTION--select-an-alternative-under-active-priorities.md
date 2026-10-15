---
version: 6
updated_at: "2026-10-14 13:43:24 +0400"
relations:
  child_of:
    - CA-R-1487
  relates_to:
    - CA-O-022
    - CA-M-297
subjects:
  governs: "Select Priority-Governed Alternative"
  depends_on:
    - "Action"
    - "Operator"
    - "Resolve Operator Priorities"
    - "Project/priority model application"
    - "Project/lexicographic selection"
atom_id: "CA-O-023"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-023-CORE_META_MODEL-ACTION--select-an-alternative-under-active-priorities.md
  source_atom_id: CA-O-023
  source_atom_revision: 6
  source_sha256: 99a2b34eaefb887afa8b62daefb52e559a0992d2b73e7448388cc50cfe74e099
  original_relations_sha256: 047cd938435fe8ff2d4107ef1a67b8ae794bce6978dda89e63efeacb3951c6b3
---
# Summary

Select an alternative under active priorities

## Operation

Select Priority-Governed Alternative **means** the Action that applies resolved Operator priorities **to** candidate alternatives **and** returns a justified selection **or** an unresolved comparison.

### execution

1. obtain the effective priorities resolved under CA-O-022 for the affected context. unresolved priorities do **not** authorize selection.
2. reject **every** candidate that violates applicable authority **or** a non-negotiable constraint.
3. apply the selected model **to** the remaining alternatives using the available evidence. use CA-M-297 **only** for Operator-selected comparison by priority order; use the selected technique for another model.
4. return a selected alternative **only** **when** that model justifies the choice. retain the constraints, criterion evidence, **and** comparison result that justify it.

### unresolved comparison

**if** no admissible alternative remains **or** the model does **not** determine a selection:

- report the alternatives, constraints, evidence, **and** unresolved comparison **to** the Operator.
- identify incomplete criterion order, unresolved ties, **or** incomparable results **when** applicable.
- do **not** invent a tie-break, substitute an algorithm, **or** return an unsupported winner.

**if** the Operator changes the applicable priorities, use the newly resolved result under CA-O-022 **before** comparing again.

## Details
