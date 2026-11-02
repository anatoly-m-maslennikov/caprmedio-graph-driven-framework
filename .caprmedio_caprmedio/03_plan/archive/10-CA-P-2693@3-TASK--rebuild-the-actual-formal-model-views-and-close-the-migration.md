---
atom_id: CA-P-2693@3
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Model
version: 3
updated_at: 2026-10-29 04:56:21 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

Rebuild the actual Formal Model views and close the migration

## Objective

Rebuild the Subject graph from the migrated Current sources, review it and close only after required corrections are complete.

## Details

Stages 4 and 5, after Definition coverage and relevant cleanup. Rebuild from the exact declared Current source set, never from A1239 or unadopted Drafts. Record source IDs/Versions, selected Scope Units/branches and statuses. Keep graph views derived and identify defining R Atom IDs rather than copying Definition text into them.

Use the selected primary-kind view, independent property views with inheritance marks, and only the requested Relation/graph-definition instance views. Preserve the chosen relation notation and declared containment-versus-inheritance meaning. Do not implement deferred Terms Graph or advanced expression evaluation.

Then perform a read-only review of the actual rebuilt graph together with the adopted defining Rs. Check the new roots/notation, Governs coverage first and dependencies second, Definition coverage, inheritance, direct-value counts/formats, actual typed relations and repaired superseded references. Verify that no Current source was silently excluded to manufacture a clean tree.

Resolve review findings using existing decisions, ask only concrete new meaning questions below 95% confidence, apply the bounded corrections and rebuild again. Re-review affected parts before closure. A generator run is not a completed review.

Use an existing suitable local generator. If a required notation is unsupported, record the concrete capability gap for the separate Engine work; do not modify tools/runtime in this Epic. Do not mark Done until the actual graph and adopted sources agree and all required held cases are resolved.

## Definition of Done

The actual-source graph is rebuilt and reviewed; required findings have been corrected and affected views rebuilt/rechecked. All selected entities have adopted R Definitions and no required mapping or consumer gap is hidden. Advanced work and remaining Engine work are explicitly separate before this Epic closes.

## Progress

Not executed. The proposal and repaired Draft review are preparation evidence, not a rebuilt Current graph or adoption proof.
