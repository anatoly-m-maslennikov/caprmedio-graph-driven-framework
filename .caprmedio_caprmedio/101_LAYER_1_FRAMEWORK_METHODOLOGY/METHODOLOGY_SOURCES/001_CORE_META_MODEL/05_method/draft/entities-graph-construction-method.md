---
content_role: Method
current_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  governs: "Projection/Type: Entities Graph"
updated_at: "2026-10-15 18:56:34 +0400"
---
# Summary

Method for the deferred Entities Graph Construction tree

## Scope

Construction/CONTAINS projection only. Deferred by the Operator on 2026-10-15; this draft is not Active authority.

## Claim

Generate the Construction tree programmatically from explicit source containment declarations, separately from Inherency.

## Details

Render Construction separately, container before contained entity. Preserve source-declared multiplicity and distinguish kind-level allowed composition from instance facts. Inverse declarations describe the same edge, not a second edge.

Use declared order or alphabetical fallback, preserve source evidence, and report missing facts and cycles without guessing or endless expansion.

## Origin

Separated from CA-M-385@1. The active successor retains the Inherency projection. No canonical Atom ID is assigned to this draft.
