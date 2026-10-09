---
atom_id: CA-P-1906
content_role: Plan
type: Plan
label: Task
work_sequence_number: 22
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 4
updated_at: "2026-10-10 02:10:14 +0400"
relations:
  is_decomposition_of: [CA-P-1872]
  blocks: [CA-P-1907]
---
# Summary

Design Continuant Occurrent groups and inherited constraints

## Objective

Design a smaller-root Entities Graph candidate with Continuant/Occurrent grouping, inherited common constraints and both derived RMED presentations, using the reviewed Core baseline.

## Details

Child work only; no separately executable own work. The larger review is split into the bounded direct Tasks below before execution.

Required start prerequisite: CA-P-1905. Inputs: its complete pinned inventory and review, the Operator's draft, and current Core definitions.

Group model objects under Continuant and Occurrent. Separate reusable Action/Step/Workflow definitions and Analysis Reports from actual Action/Step/Workflow Runs and analysis activity. Keep a model object's identity separate from its representation.

Use inheritance of common constraints through justified narrower-than specializations. A Plan Atom or Requirement Atom inherits the common Atom Carrier obligation; it does not inherit another Atom's concrete file. Define shared rules once and show subtype additions or differences. Preserve type-specific Status domains and stricter constraints.

Use as few genuine root entities as the evidence permits. Do not invent relations, collapse incompatible identities or force an uncertain classification merely to reduce the count. Report top-level display groups separately from independent model roots and justify each retained root.

Keep Carrier separate from the carried Entity and its binding metadata. Reuse CARRIES/IS_CARRIED_BY rather than invent another equivalent primitive. Carrier-specific fields such as Basename apply only where the relevant Carrier kind supports them.

Deliver both of the latest Operator's views: separate R/M/E/D trees, and an Entity-centered view with applicable M/E/D links. R shows the Entity-model skeleton and required results; M shows construction or Implementation conventions; E shows checks and acceptance criteria; D shows Carrier, representation, format, storage and placement constraints. The two views may share the same source-backed identities and Claims. Do not require an M, E or D Atom for every Entity unless applicable authority requires it.

Treat `/`, `.` and `:` as Entity-model notation, not as automatic Method/Evaluation links. Shared M/E/D Claims may apply to several Entities and need not be copied. A visual M/E/D grouping is not Property ownership, narrower-than inheritance or a newly admitted native Relation. Keep exact applicability and inherited constraints evidenced; unresolved cross-links remain questions. Do not exclude current Carrier definitions merely because their governing source role is Delivery, and do not filter the complete baseline to R-only sources.

Output: a proposed grouped structure, inherited-constraint map, old-to-candidate identity mapping, complete occurrence-to-proposed-relation ledger, comparison of the two RMED view options and explicit questions. This is candidate design, not BFO adoption or Core authority.

The relation ledger must retain **every** old source Subject relation segment, including every `/` occurrence, each supporting qualified prefix and unchanged `:` row. It is not a deduplicated graph-edge list or a ledger only for affected nodes. Each row must record the source Atom ID, Revision and Carrier hash; Subjects field index, complete path and exact segment; original qualified endpoints and graph kind; and disposition with confidence. For an evidenced proposal, record the proposed display operator, canonical Relation and direction, proposed qualified endpoints and evidence span. For an `unresolved` or `not-native` row, leave the asserted native proposal, direction and new endpoints explicitly absent; record the missing-evidence or inapplicability reason, what was checked and any required Operator question. Do not invent a proposal or positive evidence to complete a row.

Classify an old `/` as `/` or `.` only from source Main Content evidence. Propose `@` only where independent Core-declared Carrier-binding evidence supports it, never from Atom incidence or matching spelling. Record aliases and inverse views once as the same underlying Relation, not duplicate facts. Preserve every old occurrence without silent omission, and do not serialize raw `@` into Atom Subjects.

Exclusive scope: read baseline and Core definitions; write candidate structure and design evidence only. Do not update the authoritative Subjects or step-1 graph, or silently remove nodes.

### Bounded direct Tasks

| Task | Responsibility | Estimate |
|---|---|---|
| [CA-P-1913](22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints/01-CA-P-1913-TASK--review-first-atom-and-artifact-relation-batch.md) | Review first Atom and Artifact relation batch | 15 min |
| [CA-P-1914](22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints/02-CA-P-1914-TASK--review-second-atom-and-artifact-relation-batch.md) | Review second Atom and Artifact relation batch | 15 min |
| [CA-P-1915](22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints/03-CA-P-1915-TASK--review-third-atom-and-artifact-relation-batch.md) | Review third Atom and Artifact relation batch | 15 min |
| [CA-P-1916](22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints/04-CA-P-1916-TASK--review-projection-carrier-and-journal-relations.md) | Review Projection Carrier and Journal relations | 15 min |
| [CA-P-1917](22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints/05-CA-P-1917-TASK--review-first-context-and-operation-relation-batch.md) | Review first context and operation relation batch | 15 min |
| [CA-P-1918](22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints/06-CA-P-1918-TASK--review-second-context-and-operation-relation-batch.md) | Review second context and operation relation batch | 15 min |
| [CA-P-1919](22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints/07-CA-P-1919-TASK--design-core-temporal-groups-and-inherited-constraints.md) | Design Core temporal groups and inherited constraints | 15 min |
| [CA-P-1920](22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints/08-CA-P-1920-TASK--design-parallel-and-entity-centered-rmed-views.md) | Design parallel and Entity centered RMED views | 15 min |
| [CA-P-1921](22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints/09-CA-P-1921-TASK--integrate-the-source-pinned-core-relation-ledger.md) | Integrate the source pinned Core relation ledger | 15 min |
| [CA-P-1922](22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints/10-CA-P-1922-TASK--verify-the-core-grouping-and-relation-design.md) | Verify the Core grouping and relation design | 15 min |

CA-P-1913 through CA-P-1920 may run in parallel after CA-P-1905 is Done. CA-P-1921 starts only after all eight are Done; CA-P-1922 starts only after CA-P-1921 is Done. This explicit BLOCKS model, not navigation or decomposition, controls execution. Temporary batch outputs are preserved in the durable verified handoff before their receipts are recorded. The six sorted case-ID partitions must cover each of the 294 old slash cases exactly once.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold; do not disguise uncertainty as an accepted fact. If the ready workload exceeds 15 minutes, split it into bounded direct child Plans before execution. The children are created before execution; their outputs remain proposed design, not candidate acceptance.

### Definition of Done

the Plan is **not** Done **if** ((the stated output, complete source traceability, complete occurrence-to-proposed-relation ledger, comparison of the two RMED view options **or** required handoff is missing) **or** (any old relation segment lacks its source coordinates, original qualified endpoints, graph kind **or** disposition) **or** (a proposed relation lacks its proposal fields **or** evidence span) **or** (an unresolved **or** not-native row asserts an invented native proposal **or** lacks its reason, checks performed **or** required Operator question) **or** (a required start prerequisite is **not** Done) **or** (the stated acceptance conditions are failed, stale **or** unverified) **or** (uncertainty below the inherited confidence threshold is silently resolved **or** not put to the Operator) **or** (work exceeds the admitted boundary **or** any source, Subject, history **or** marked Entity was changed **or** deleted without separate authorization) **or** (any direct decomposing Plan is **not** Done)).
