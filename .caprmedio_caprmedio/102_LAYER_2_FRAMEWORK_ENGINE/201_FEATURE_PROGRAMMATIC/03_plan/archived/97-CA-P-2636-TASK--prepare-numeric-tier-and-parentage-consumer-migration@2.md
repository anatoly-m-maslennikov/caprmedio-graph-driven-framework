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
version: 2
updated_at: "2026-10-23T18:36:18+0400"
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
schema sources are supplied. The target decisions stated by the notice are
specific, but still await adoption in authoritative sources: at Project
scope, `tier: 0` is Principle, `tier: 1` is Core, `tier: 2` is General and
`tier: 3` is Standard; non-Project tiers are at least 1; a Project Goal owns
literal `-1`; the target field is `tier`; and Atom `global_tier` is removed.
Do not apply these changes in this Task, and do not remove authored Scope Unit
`structural_level` or change parentage/relation semantics. R/M/E/D
structural/governing links target a same-scope strictly lower tier or a strict
ancestor scope; exact relation families still need clarification and inverse
edges are derived rather than authored.

Inventory the eventual consumer boundary without editing it: project
structure declaration/normalization/tree validation/rendering and create
parameters; connector scope parsing/querying; Atom structure/parentage/tier
and Goal-tier validation; lifecycle, replacement, filename/path, projection
and test consumers. Preserve parent traversal, Rename descendant-parent
rewrites, empty-only Remove, path validation, and the separation between
local order/navigation and parentage. Do not introduce a `contains` field
solely from the notice. Scope Unit operations remain Stage 2 under CA-P-2480.

## Observed consumer boundary

The source-bound inventory to reconcile after adoption includes:

- Scope structure: `project_structure.py` declaration fields 28–56,
  `_normalise_declaration` 166–213, `_validate_tree` 231–273,
  `_render_declaration` 296–309 and create parameters 345–389;
  `connector_scope_parsing.py` fields 10–20, parsing 60–121 and query
  declarations 167–199.
- Atom admission and requests: `VALIDATE_ATOMS/check_fields.py` 115–130,
  `check_schema_extended.py` 23–39, 61–79 and 244–272, `check_domains.py`
  57–84, `check_dispatch.py` 49–62, `request_models.py` 39–55 and
  `selection.py` 51–72.
- Lifecycle and derived consumers: `atom_operations.py` 2143–2194 and
  2273–2315 (upgrade/local-tier and filename handling),
  `lifecycle_intents.py` 460–487, `migrations/backfill_global_tier.py`
  23–143, `migrations/backfill_required_atom_properties.py` 22–49 and
  `check_graph_extended.py` 441–529.

This is an observed consumer inventory, not an implementation or migration
result. Existing parent traversal, Rename descendant-parent rewrites,
empty-only Remove, path validation and local-order/navigation separation must
remain explicit compatibility requirements.

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
