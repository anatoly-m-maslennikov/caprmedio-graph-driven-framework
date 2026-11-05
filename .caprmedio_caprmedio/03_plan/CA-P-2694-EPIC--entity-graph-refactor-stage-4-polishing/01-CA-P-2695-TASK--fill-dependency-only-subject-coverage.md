---
atom_id: CA-P-2695
ref_id: CA-P-2695
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
updated_at: 2026-10-29 16:52:01 +0400
current_scope_unit: caprmedio
author: Anatoly Maslennikov
---
## Summary

Fill dependency-only Subject coverage

## Objective

Resolve the 29 Subject paths that occur only in dependencies within the selected Current Methodology and project-local RMED sources.

## Details

Use [the thin tracker](dependency-only-subjects.tsv): Atom ID | old Subject | new Subject | status. Its 63 rows record actual dependency uses, not 63 missing entities. Recompute the exact-path set from live selected sources before applying changes.

For each group, inspect current defining R Claims and formal clauses first. A Subject can already be defined by a broader governing R or inherited definition even when its exact path has no Governs occurrence. Reuse that authority; do not create redundant definitions merely to make a text-set subtraction empty.

Where an entity/property/value genuinely lacks defining R authority, create its R/Entity Definition Draft with the correct governing Subject and required format/cardinality. Where the dependency is obsolete, ambiguous or misnamed, draft the supported consumer correction or retirement. Track any deliberately retained dependency-only path with its defining R ID and reason. New or updated source Atoms are drafted immediately; keep the tracker thin.

### Tier Label correction

Apply the accepted numeric Tier/optional Label distinction from the parent Epic. Define `Atom.Tier.Label` and the labels 0 Principle, 1 Core, 2 General, 3 Standard, 4 Detail; numeric Tiers extend beyond 4 and labels are optional. `CA-E-477` currently depends on `Entity/Object/Continuant/Governing Objects/Atom.Tier: Principle`; its confirmed target is `Entity/Object/Continuant/Governing Objects/Atom.Tier.Label: Principle`. Review its existing evaluation content for a faithful corresponding correction. Keep the numeric Tier authoritative; determine its Label carrier through D, rather than substituting label text for the number.

Review Drafts, promote accepted replacements with normal predecessor archives, and repair their in-scope consumers. Rebuild the three focused Entity views and recompute the dependency-only set. Separate missing definitions, corrected references and legitimate coverage through broader R Claims in the final readback.

## Definition of Done

Each of the starting 29 paths and 63 uses has a recorded disposition and supporting source authority. Required Drafts/corrections are adopted; Tier Label is defined with the approved optional numeric mapping; obsolete Principle-as-Tier references are corrected. The affected graph/properties/Relation views are rebuilt and reviewed, with any remaining dependency-only paths explicitly justified.

## Progress

Done for the dependency-only coverage scope: all 29 paths / 63 uses have source-backed dispositions in the thin tracker. Applied 21 updated Atoms with predecessor archives and 3 new Definitions; rebuilt CA-PROJ-014/015/016 from 1,111 Current sources. Remaining 20 exact dependency-only paths are explained in the thin remainder list. See [coverage result](dependency-coverage-result.md).

The newer exactly-one Definition ownership requirement is tracked separately in P2696 and remains Active. This Task does not claim uniqueness or resolution of the deferred E477 conflict-policy content.
