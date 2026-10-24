---
atom_id: CA-P-2054
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Subject
  depends_on: [Atom, Subject, Term, Property, Carrier, Scope Unit, Projection, Plan, Operator]
version: 2
updated_at: "2026-10-22 22:05:30 +0400"
relations:
  is_decomposition_of: [CA-P-2049]
---
# Summary

Resolve carrier and storage Subject mappings

## Objective

Refresh the carrier_storage Candidate #7 mapping lane from the live worklist and return complete, source-backed dispositions.

## Details

Read the fresh carrier_storage lane from .caprmedio_caprmedio/_projection/core-entity-review/presentation/candidate-7.remaining-subject-worklist.json. Treat Carrier as the Engineering representation/storage bearer, not the represented content. Preserve Carrier, Scope Unit, Atom, Projection and Journal distinctions and their bearer-specific IDs. Read source context before assigning a path; do not infer a target from display text or folder placement. Return complete evidence-backed or unresolved rows. Apply no source, content, code, schema, MCP, test, Settings or runtime change.

### Definition of Done

Not Done if the fresh lane is absent/stale, assigned whole-owner or occurrence coverage is incomplete, a meaning is guessed, qualifiers or provenance are lost, unresolved rows are hidden, or any source effect or migration completion is claimed.
