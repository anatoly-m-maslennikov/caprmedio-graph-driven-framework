---
atom_id: CA-P-1966
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 7
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 1
updated_at: "2026-10-10 22:32:47 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1967]
---
# Summary

Map current Core Subject origins

## Objective

Map every selected current RMEDO Subject occurrence to its supported candidate Entity without guessing.

## Details

This grouping Plan has no own implementation work. Before execution, create disjoint child Tasks of at most 15 minutes each.

Required prerequisite: CA-P-1963. Pin the current authoritative Core frontier and inventory every governs/depends_on occurrence, including unchanged and excluded cases. Compare current meanings with the frozen candidate and consolidated review; do not overwrite their captured inputs or reuse old pins as current.

Read the actual source content to decide whether an old / denotes narrowing or bearer qualification and whether a whole Subject target needs replacement. Keep the governs/dependency distinction and content-role views. The 442 display-path proposals are not executable replacements; the 149 follow-ups remain research work until supported.

Produce explicit occurrence-level before/after decisions, evidence refs, preserved distinctions and unresolved cases. Low confidence below 90% triggers investigation; ask only when a concrete design conflict remains. Do not delete redundant-looking entities or invent Carrier bindings. No authoritative write is permitted.

Root owns integration of the complete ledger; workers own disjoint review batches.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Decomposing Plans

- [CA-P-1972 — Prepare disjoint Subject mapping Tasks](07-CA-P-1966-EPIC--map-current-core-subject-origins/01-CA-P-1972-TASK--prepare-disjoint-subject-mapping-tasks.md)

### Definition of Done

The Plan is **not** Done if any selected occurrence is missing or guessed, a mapping lacks current source evidence, unresolved cases are hidden, captured outputs change, or source Atoms are edited, any direct decomposing Plan is not Done, or own work exceeds 15 minutes without decomposition.
