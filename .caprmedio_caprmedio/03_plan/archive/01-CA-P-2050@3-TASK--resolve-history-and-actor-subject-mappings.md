---
atom_id: CA-P-2050@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
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

Resolve history and actor Subject mappings

## Objective

Refresh the history_actor Candidate #7 mapping lane from the live worklist and return complete, source-backed dispositions.

## Details

Read the fresh history_actor lane from .caprmedio_caprmedio/_projection/core-entity-review/presentation/candidate-7.remaining-subject-worklist.json. Re-read each current owner and preserve the distinction between History records, actual Occurrents and Actor bearers. Map only where source meaning supports a full Candidate #7 path; retain qualifiers, IDs and dependency direction. If the source does not support a target at 90% confidence, return an explicit unresolved row. Apply no source, content, code, schema, MCP, test, Settings or runtime change.

### Definition of Done

Not Done if the fresh lane is absent/stale, assigned whole-owner or occurrence coverage is incomplete, a meaning is guessed, qualifiers or provenance are lost, unresolved rows are hidden, or any source effect or migration completion is claimed.
