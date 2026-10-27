---
atom_id: CA-P-2049@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 56
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
  - CA-P-1966
tier: 3
---
# Summary

Resolve remaining Subject mappings

## Objective

Coordinate seven disjoint Candidate #7 mapping lanes and preserve every unresolved result for integration.

## Details

Use .caprmedio_caprmedio/_projection/core-entity-review/presentation/candidate-7.remaining-subject-worklist.json as the only current ownership input. Refresh lane scope from its contents rather than the old current-subjects.research-ownership.json, fixed counts or manifests. Each lane reads the actual current source when needed and returns every assigned owner/occurrence as an evidence-backed target, unchanged, held or unresolved.

The lanes cover Candidate #7 Subjects, defining R/D rules, property paths, Type classification and ID implications. Keep Subject separate from Content Role, preserve Domain/Engineering/Graph meaning, and do not invent entities or aliases. Classification-only Type corrections retain IDs only when Summary and Substance remain unchanged. Ordinary content migration remains CA-P-1970; no source application, code, schema, MCP, test, Settings or runtime work is included.

### Decomposing Plans

- CA-P-2050 — history_actor
- CA-P-2051 — content_roles_types
- CA-P-2052 — operations
- CA-P-2053 — relations_subjects
- CA-P-2054 — carrier_storage
- CA-P-2055 — methodology_configuration
- CA-P-2056 — other

### Definition of Done

Not Done if the fresh worklist is absent/stale, a lane has incomplete or overlapping whole-owner coverage, a source meaning is guessed, below-90% cases are hidden, or a lane result is mistaken for source adoption or migration completion.
