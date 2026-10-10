---
atom_id: CA-P-1972
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Tool, Operator]
version: 8
updated_at: "2026-10-11 01:25:08 +0400"
relations:
  is_decomposition_of: [CA-P-1966]
---
# Summary

Prepare disjoint Subject mapping Tasks

## Objective

Decompose the current occurrence inventory into evidence-pinned review Tasks without proposing or writing source replacements.

## Details

Own work: none. This preparation is now decomposed because source selection, snapshot comparison, independent verification and Plan creation need separate checks. The first uncommitted inventory was rejected; no rejected output counts as completion.

Required prerequisite: CA-P-1963. Pin the current authoring Core inventory and define disjoint review batches with exact occurrences, role/owner/source limits, input pins, output schema and at-most-15-minute checks. Create child Plans under CA-P-1966 before review work. Every selected occurrence has one owner; unchanged and malformed cases remain accounted for. Define final ledger integration and actual completion checks. Do not map Subjects in this preparation Task, change captured reviews or edit authoritative Atoms.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

Finishing this preparation does not finish CA-P-1966: only its generated evidence-review/integration children and verified complete ledger can do that.

### Definition of Done

The Plan is **not** Done if batches overlap or omit selected occurrences, source pins or output/check contracts are missing, any child has more than 15 minutes of undecomposed own work, or source mappings/writes are performed; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.

### Decomposing Plans

- [CA-P-1988 — Inventory current Core Subject sources](01-CA-P-1972-TASK--prepare-disjoint-subject-mapping-tasks/done/01-CA-P-1988-TASK--inventory-current-core-subject-sources.md)
- [CA-P-1989 — Compare current sources with captured evidence](01-CA-P-1972-TASK--prepare-disjoint-subject-mapping-tasks/done/02-CA-P-1989-TASK--compare-current-sources-with-captured-evidence.md)
- [CA-P-1990 — Verify current Subject inventory and batches](01-CA-P-1972-TASK--prepare-disjoint-subject-mapping-tasks/done/03-CA-P-1990-TASK--verify-current-subject-inventory-and-batches.md)
- [CA-P-1991 — Create bounded current Subject review Plans](01-CA-P-1972-TASK--prepare-disjoint-subject-mapping-tasks/done/04-CA-P-1991-TASK--create-bounded-current-subject-review-plans.md)
