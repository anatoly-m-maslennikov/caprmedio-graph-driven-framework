---
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  governs: "Projection/Type: Entities Graph"
updated_at: "2026-10-15 18:56:34 +0400"
---
# Summary

Evaluation for the deferred Entities Graph Construction tree

## Scope

Construction/CONTAINS projection only. Deferred by the Operator on 2026-10-15; this draft is not Active authority.

## Claim

When Construction projection is adopted, check that:

- the Inherency view precedes the Construction view and their relation families are not mixed;
- the Construction tree follows explicit CONTAINS facts or inverse-derived IS_CONTAINED_BY facts, preserves declared cardinalities, and distinguishes allowed kind composition from actual instances;
- a valid declared Plan-in-Plan, Workflow/Step/one-Action and Scope Unit containment fixture renders correctly; missing declarations do not cause guessed edges;

Use controlled generator fixtures. Missing construction facts do not block the active Inherency-only view.

## Origin

Separated from CA-E-449@14. The active successor retains the Inherency projection. No canonical Atom ID is assigned to this draft.
