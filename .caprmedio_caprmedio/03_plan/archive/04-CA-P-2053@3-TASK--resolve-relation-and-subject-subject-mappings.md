---
atom_id: CA-P-2053@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Atom
  - Subject
  - Term
  - Property
  - Carrier
  - Scope Unit
  - Projection
  - Plan
  - Operator
version: 3
updated_at: 2026-10-24 06:04:11 +0400
relations:
  is_decomposition_of:
  - CA-P-2049
tier: 3
---
# Summary

Resolve relation and subject Subject mappings

## Objective

Refresh the relations_subjects Candidate #7 mapping lane from the live worklist and return complete, source-backed dispositions.

## Details

Read the fresh relations_subjects lane from .caprmedio_caprmedio/_projection/core-entity-review/presentation/candidate-7.remaining-subject-worklist.json. Keep Graph/Relation definitions separate from Graph/Rule constraints and keep Subject links separate from ordinary Atom relations. Preserve direct relation direction, derive inverses, and treat containment as IS_CONTAINED_BY on the child with CONTAINS derived. Map only from current source meaning, preserving endpoint qualifiers and current Atom ID targets. Return unresolved cases explicitly. Apply no source, content, code, schema, MCP, test, Settings or runtime change.

### Definition of Done

Not Done if the fresh lane is absent/stale, assigned whole-owner or occurrence coverage is incomplete, a meaning is guessed, qualifiers or provenance are lost, unresolved rows are hidden, or any source effect or migration completion is claimed.
