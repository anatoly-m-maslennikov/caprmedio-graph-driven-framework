---
atom_id: CA-P-2697@2
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
tier: 4
version: 2
updated_at: 2026-10-29 16:28:33 +0400
subjects:
  governs: Entity
relations:
  IS_CONTAINED_BY:
  - CA-P-2694
  BLOCKS:
  - CA-P-2698
---
## Summary

Review combined Entity Definitions for coherence and conflicts

## Objective

Review the 180 existing one-Definition entities together with every entity fixed in P2696. Check the whole combined model, not only the changed Atoms.

## Details

Start after [P2696](02-CA-P-2696-TASK--establish-one-defining-requirement-per-model-entity.md) completes the confirmed ownership cohort. The Operator confirmed all 133 shared/formal cases. The starting cohort is all 337 parsed model paths: 180 one-exact-Definition, 24 multiple-candidate groups and 133 shared/formal cases. The later scope refinement makes global uniqueness strict for Object, Carrier and Graph Syntax (and the common Entity root), including their properties: 280 parsed paths, with 165 single, 23 multiple and 92 without exact ownership. The 57 Aspect paths remain in the coherence review, but their definitions may be scoped and need not be globally unique. Equivalent Markdown property spellings are one logical entity, not extra definitions.

Use the adopted Current sources and their exact IDs/Versions. Check:

- exactly one defining R per Entity; distinguish actual definitions from Rules, constraints, references and inherited use;
- compatible meanings and Claim scopes across the original 180 and the repaired groups;
- agreement between prose and formal Claims, property cardinality/format, allowed values and inheritance;
- correct specialization, containment, bearer and other typed relations, without dangling references or hidden contradictions;
- clear boundaries between kinds and instances, claims and records, Objects and Carriers, and authoritative sources and Projections;
- the accepted Relation Definition template: one full main-direction definition and only a short derived-counterpart reference, following DRY;
- gaps, duplicated meaning and conflicting rules introduced or exposed by the ownership fixes.

Relation Definition counts through its specialized template. Subtype restructuring stays deferred. Do not manufacture coherence by suppressing candidate sources, changing scope silently, adding defaults or choosing a winner by timestamp/Tier. Take genuinely unresolved meaning conflicts to the Operator.

Use Luna for mechanical checks, gathering source excerpts and bounded comparisons. Use Terra for semantic coherence, conflict judgments and independent review. Parent owns integration, shared Journal and publication. Assign disjoint groups and use thin tracking files; do not build large copied-Claim mapping files. No Engine/code/runtime or Terms Graph implementation work.

Record findings with affected Entity/Atom IDs, evidence, severity and proposed correction. Do not treat a passing generator or schema check as semantic review.

## Definition of Done

Every entity in the confirmed combined set has been reviewed. A thin finding list covers all remaining issues and supporting source evidence. P2698 has a concrete repair queue; an empty queue requires explicit review evidence. Coverage and exclusions are stated without implying the whole 337-entity model passed if only a subset was selected.

## Progress

Backlog — waits for P2696 ownership corrections ; all 133 shared/formal cases are confirmed.
