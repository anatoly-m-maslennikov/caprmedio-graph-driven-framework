---
atom_id: CA-P-2691@3
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

Formalize in-scope Claims in bounded batches

## Objective

Complete R Definition coverage for the adopted Model entities and add simple formal Claims where they preserve meaning.

## Details

Stage 3, after the mechanical Subject pass and reviewed-Draft adoption. Build a thin coverage list: Model entity/Subject | defining R Atom IDs and Versions | status. Discover entities from both the accepted Model and the actual Current governing Rs/Subjects; do not use the proposal tree as the only inventory.

Find existing Rs that already define an entity or property before creating another Atom. Reuse or refine those Definitions and classify them correctly. If an existing R mixes a definition with other contributions, preserve useful meaning through bounded replacement/splitting under the existing identity rules. Add missing R/Definition Drafts with correct Subjects, review them, then adopt them. Do not invent a new branch/kind solely to fit an unmapped legacy topic.

Cover the declared entities and their required property structures, qualified kinds, relevant value Formats and admitted Relations. A punctuation operator or classification-axis label is not automatically another entity. P2686 owns primitive Formats; P2687 owns Relation-specific gaps; keep one shared coverage record.

Every complete R Definition keeps required prose Claim. Add a full or partial Formal claim only when the settled simple structure/relation/format/cardinality notation expresses it faithfully. Otherwise retain the condition in prose and record why. Each direct property path has its own format/count; preserve inherited declarations and mark inherited views. Use basic [format] only; advanced formulas and conditions in [] remain separate. Named-relation counts stay in prose. M/E/D remain prose.

Use bounded source groups/subtasks. Do not introduce a function or helper for each entity/case; future functions need a real reusable pattern that reduces complexity.

## Definition of Done

Every declared in-scope Model entity has at least one adopted Current R Definition, with property/cardinality/format coverage where required. Existing governing R meaning is preserved or explicitly retired. Every selected R has a faithful formal/partial/prose disposition; all unresolved required coverage is resolved before final closure.

## Progress

Not executed on Current sources. Prepared Definitions and reviews are inputs; coverage still needs the actual migrated/adopted frontier.
