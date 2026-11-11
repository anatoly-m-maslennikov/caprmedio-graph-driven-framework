---
atom_id: CA-P-2698
ref_id: CA-P-2698
container:
  atom: CA-P-2694
role: Plan
form: Plan
label: Task
topics:
  main_subject: Entity

tier: 4
status: Done
version: 4
updated_at: 2026-10-29 17:18:14 +0400
current_scope_unit: caprmedio
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: 04-CA-P-2698-TASK--fix-definition-review-findings-and-recheck-the-graph.md
    path: .caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/020_done
---
## Summary

Fix Definition review findings and recheck the graph

## Objective

Fix the findings from [CA-P-2697](03-CA-P-2697-TASK--review-combined-entity-definitions-for-coherence-and-conflicts.md), then rebuild and recheck the affected model and the complete confirmed review set.

## Details

Use the review finding list as the work queue. Create corrected/new Drafts immediately. Preserve useful meanings and consumers when consolidating competing Definitions or reclassifying a constraint as a Rule. A new Summary or Content Role needs the applicable new identity; keep normal predecessor archives for selected Current updates. Adopt reviewed changes and record actual results.

Do not duplicate the main Relation's semantics in its derived counterpart. Keep IS_DEFINED_BY derived. Relation Definition uses the accepted specialized template; do not introduce the deferred subtype hierarchy. Do not implement Engine, runtime or Terms Graph changes as a shortcut.

Use Luna for deterministic edits, source lookup and scripted consistency checks in bounded, disjoint batches. Use Terra for ambiguous meaning changes, review and verification. Parent owns Current publication, shared Journal and integration. Ask the Operator where the intended meaning remains unresolved; do not invent business rules.

After repairs, recompute unique Definition ownership, repeat affected coherence/conflict checks, and rebuild the source-backed Entity views. Recheck the combined original-plus-repaired set to catch regressions. Preserve explicit unresolved findings instead of labeling them fixed. Keep the Epic Active until the Operator permits closure.

## Definition of Done

Every confirmed review finding is fixed and verified, or has an explicit Operator-approved disposition. The selected complete logical model has exactly one defining R per logical Entity and no unresolved coherence/conflict issue hidden by the projection. Source IDs/Versions, scope and checks are recorded; rebuilt views match actual Current sources. The Epic is not automatically moved to Done.

## Progress

Done — adopted the reviewed corrections, preserved predecessor archives, re-read 1,256 Current sources, verified 336/336 original logical owners and 33/33 Relation Type owners, then rebuilt and checked all three projections. Dedicated-definition weak fits and verification limits are explicit in the result report. The Epic remains Active.

See [definition polishing result](../definition-polishing-result.md).
