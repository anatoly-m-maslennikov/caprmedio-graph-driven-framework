---
atom_id: CA-P-2636
content_role: Plan
type: Plan
label: Task
work_sequence_number: 97
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-23T18:34:36+0400"
---
# Summary

Prepare numeric-tier and parentage consumer migration

## Objective

Prepare a bounded migration plan for the authorized methodology/schema notice
about numeric Atom tiers and Scope Unit parentage. This Task is planning-only:
it must identify affected consumers and required source pins before any
schema, carrier, projection or implementation migration is proposed.

## Details

The current notice is not adopted authority. Preserve the currently admitted
`local_tier` and `global_tier` fields until exact adopted methodology and
schema sources are supplied. Do not remove authored `ScopeUnit`
`structural_level`, remove Atom `global_tier`, add a replacement `tier` field,
or change parentage/relation semantics in this Task. The proposed future
mapping is only a candidate: Project `tier: 0`, Principle `tier: 1`, Core
`tier: 2`, General `tier: 3`, Standard `tier: 4`, with no assumed maximum and
non-Project tiers at least 1. The Project Goal `-1` rule and relation-family
inverses remain unadopted decisions.

Inventory the eventual consumer boundary without editing it: project
structure declaration/normalization/tree validation/rendering and create
parameters; connector scope parsing/querying; Atom structure/parentage/tier
and Goal-tier validation; lifecycle, replacement, filename/path, projection
and test consumers. Preserve parent traversal, Rename descendant-parent
rewrites, empty-only Remove, path validation, and the separation between
local order/navigation and parentage. Do not introduce a `contains` field
solely from the notice. Scope Unit operations remain Stage 2 under CA-P-2480.

## Execution hold

Keep this Task Backlog/HOLD until exact adopted methodology/schema pins and
clarified relation families are available. A future execution must first
produce a source-bound consumer matrix, compatibility/migration order,
identity-safe archive plan, and focused golden-corpus checks. It must not
weaken identity, filename/path, deletion, or authority safeguards.

## Definition of Done

Return one reviewed planning record containing: the exact adopted source pins;
the affected reader/schema/request/lifecycle/replacement/filename/projection/
test consumer matrix; the numeric-tier and parentage compatibility mapping;
the unresolved relation-family/inverse decisions; and a bounded migration
sequence. No source Atom, schema, code, configuration, projection, runtime or
Project Structure mutation is part of this Task.

## Constraints

At most 15 minutes of own work; one Task per file. Review this Task and its
dependents after each predecessor decision. If the adopted sources or relation
families remain unclear, keep it on hold and record the uncertainty rather
than inventing a new Concern or changing current authority.
