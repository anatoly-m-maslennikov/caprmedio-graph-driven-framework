---
atom_id: CA-P-1968
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 9
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 2
updated_at: "2026-10-10 23:24:00 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1969]
---
# Summary

Apply approved Subject migration batches

## Objective

Apply only the separately approved exact migration packet and retain truthful history and effect records.

## Details

This grouping Plan has no own implementation work. Decompose the approved packet into bounded child Tasks before execution. Required prerequisites: CA-P-1967, CA-P-1910's actual Done receipt and separate Operator approval of CA-P-1910's exact final preview hash/source frontier. CA-P-1911 owns the sole application execution; these Tasks only organize its bounded batches. Its current execution gates must pass before any effect.

Reuse the existing governed mutation boundary. Coordinate the applier with CA-P-1911; one owner applies each source once. If no admitted applier is available, stop and request the required authority; do not invoke raw ATOM_UPDATE internals or remove the standalone apply guard.

Recheck all pins before effects. Apply only approved Subjects, required Version +1/updated_at/history effects and the exact approved minimum grammar revisions. Preserve ordinary Summary/Substance/Scope/Details and all unrelated metadata. Preserve earlier Atom contents through Git and the applicable approved archive policy; record effect/Atom IDs in the Journal, not duplicate Atom bodies.

Process disjoint approved batches with one integration/Git owner. Failed or uncertain effects stop; inspect actual state before resume. No automatic rollback, retry, runtime activation or release permission is implied. Validate each batch and record actual after pins.

Preparation alone cannot complete this group. Require the prepared effect children, CA-P-1911's actual completed single execution and after-state verification. For each same-ID update, verify exact Version +1, actual Project-time timestamp, new current Active revision and prior Archived history. Git retains exact prior contents/versions. Report actual Journal record references for required effects; an absent/failed required record is incomplete, not a fabricated success.

All other body updates remain blocked until CA-P-1969 passes.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Decomposing Plans

- [CA-P-1973 — Prepare approved Subject application Tasks](09-CA-P-1968-EPIC--apply-approved-subject-migration-batches/01-CA-P-1973-TASK--prepare-approved-subject-application-tasks.md)

### Definition of Done

The Plan is **not** Done if a live effect lacks exact approval/current pins, a source is applied twice, ordinary content changes, required history/records are missing, a failure is masked, or an admission guard is bypassed; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
