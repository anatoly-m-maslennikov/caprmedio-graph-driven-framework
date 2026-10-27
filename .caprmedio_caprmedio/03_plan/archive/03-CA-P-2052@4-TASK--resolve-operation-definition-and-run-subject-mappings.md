---
atom_id: CA-P-2052@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 4
updated_at: 2026-10-24 06:12:15 +0400
relations:
  is_decomposition_of:
  - CA-P-2049
tier: 3
---
# Summary

Resolve operation definition and run Subject mappings

## Objective

Refresh the operations Candidate #7 mapping lane from the live worklist and return complete, source-backed dispositions.

## Details

Read the fresh operations lane from .caprmedio_caprmedio/_projection/core-entity-review/presentation/candidate-7.remaining-subject-worklist.json. Distinguish operation definitions and named instances from actual Runs/events: definitions may use the Candidate #7 kind-to-instance boundary, while actual runs/events are Occurrents and their records belong to History. Preserve exact names, qualifiers and source identity; do not add an Invocation/Tool Call root or infer runtime behavior. Return every lane row with evidence or unresolved status. Apply no source, content, code, schema, MCP, test, Settings or runtime change.

### Definition of Done

Not Done if the fresh lane is absent/stale, assigned whole-owner or occurrence coverage is incomplete, a meaning is guessed, qualifiers or provenance are lost, unresolved rows are hidden, or any source effect or migration completion is claimed.
