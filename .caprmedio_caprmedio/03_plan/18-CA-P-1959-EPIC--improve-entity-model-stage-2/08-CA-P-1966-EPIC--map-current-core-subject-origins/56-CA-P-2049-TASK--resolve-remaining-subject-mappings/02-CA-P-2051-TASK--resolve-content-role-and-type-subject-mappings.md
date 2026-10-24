---
atom_id: CA-P-2051
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
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

Resolve content role and type Subject mappings

## Objective

Refresh the content_roles_types Candidate #7 mapping lane from the live worklist and return complete, source-backed dispositions.

## Details

Read the fresh content_roles_types lane from .caprmedio_caprmedio/_projection/core-entity-review/presentation/candidate-7.remaining-subject-worklist.json. Keep Subject (what content concerns) separate from Content Role (what content does), and classify Types from source meaning rather than folder, Role or tier. Candidate #7's one-time classification-only exception retains an ID only when Summary and Substance are unchanged; otherwise preserve ordinary identity rules. Return complete supported/unchanged/held/unresolved rows without guessing. Apply no source, content, code, schema, MCP, test, Settings or runtime change.

### Definition of Done

Not Done if the fresh lane is absent/stale, assigned whole-owner or occurrence coverage is incomplete, a meaning is guessed, qualifiers or provenance are lost, unresolved rows are hidden, or any source effect or migration completion is claimed.
