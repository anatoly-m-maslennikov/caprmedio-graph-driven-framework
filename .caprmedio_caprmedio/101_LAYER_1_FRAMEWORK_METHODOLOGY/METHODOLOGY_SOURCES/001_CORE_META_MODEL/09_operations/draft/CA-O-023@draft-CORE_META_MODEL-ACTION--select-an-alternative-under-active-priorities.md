---
version: 8
updated_at: "2026-10-15 18:33:28 +0000"
relations:
  child_of:
    - CA-R-1487
  relates_to:
    - CA-O-022
    - CA-M-297
subjects:
  governs: "Select Priority-Governed Alternative"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Actor/Type: Operator", "Resolve Operator Priorities", "Project Priority Model Application", "Project Lexicographic Selection"]
atom_id: "CA-O-023@draft"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
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
