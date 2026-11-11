---
atom_id: CA-P-2693
ref_id: CA-P-2693
container:
  atom: CA-P-2683
role: Plan
form: Plan
label: Task
topics:
  main_subject: Entity
tier: 4
status: Done
version: 5
updated_at: 2026-10-29 11:48:33 +0400
current_scope_unit: caprmedio
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: 10-CA-P-2693-TASK--rebuild-the-actual-formal-model-views-and-close-the-migration.md
    path: .caprmedio_caprmedio/03_plan/020_done/CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims/020_done
---
## Summary

Rebuild the actual Formal Model views and close the migration

## Objective

Rebuild the Subject graph from the migrated Current sources, review it and close only after required corrections are complete.

## Details

Stages 4 and 5, after Definition coverage and relevant cleanup. Rebuild from the exact declared Current source set, never from A1239 or unadopted Drafts. Record source IDs/Versions, selected Scope Units/branches and statuses. Keep graph views derived and identify defining R Atom IDs rather than copying Definition text into them.

Use the selected primary-kind view, independent property views with inheritance marks, and only the requested named Relation Type instance view. Preserve the chosen relation notation and declared containment-versus-inheritance meaning. Do not implement deferred Terms Graph or advanced expression evaluation.

Then perform a read-only review of the actual rebuilt graph together with the adopted defining Rs. Check the new roots/notation, Governs coverage first and dependencies second, Definition coverage, inheritance, direct-value counts/formats, actual typed relations and repaired superseded references. Verify that no Current source was silently excluded to manufacture a clean tree.

Resolve review findings using existing decisions, check the latest 48-hour Operator input below 90% confidence; if uncertainty remains, choose the best-supported option and track a C/Question in A1305, apply the bounded corrections and rebuild again. Re-review affected parts before closure. A generator run is not a completed review.

Use an existing suitable local generator. If a required notation is unsupported, record the concrete capability gap for the separate Engine work; do not modify tools/runtime in this Epic. Do not mark Done until the actual graph and adopted sources agree and all required held cases are resolved.

## Definition of Done

The actual-source graph is rebuilt and reviewed; required findings have been corrected and affected views rebuilt/rechecked. All selected entities have adopted R Definitions and no required mapping or consumer gap is hidden. Advanced work and remaining Engine work are explicitly separate before this Epic closes.

## Progress

Completed the three source-backed views, source readback and independent bounded review. CA-PROJ-014 covers primary kinds and the four concrete kind links, CA-PROJ-015 properties with inheritance and explicit allowed values, and CA-PROJ-016 the 31 named Relation Types. All share the frozen 1,108-source vector. The renderer regression checks, 13 coverage checks, actual-source validation and published-artifact checks pass. See source-review.md and the Definition-coverage table. Engine/runtime and deferred Terms/advanced expressions remain separate.
