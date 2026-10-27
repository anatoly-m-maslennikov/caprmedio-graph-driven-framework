---
atom_id: CA-P-2392
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Status
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Engineering/Workflow
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
version: 8
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2386
tier: 3
---
# Summary

Align methodology Draft-history contracts

## Objective

Remove mandatory retained Draft-head/lineage/consuming-successor prerequisites from methodology Status/create/update contracts. Preserve ID allocation and collision checks, exact actual predecessor archives and truthful effects.

## Details

### Observed completion — 2026-10-16

CA-D-568/570/446/276/288 were aligned with exact predecessor archives and CA-A-1192–1196. Ordinary ID-free Draft promotion always allocates a fresh unused ID, including a tool-demoted Draft; actual historical IDs are not restored. Exact actual predecessor history remains preserved without a retained-head/lineage admission gate.

Estimated own work: at most 15 minutes. Use the complete current mrt_programmatic_methods prompt. Preserve unrelated work; no speculative behavior, fabricated history or unrelated status cascade. Source edits retain exact predecessors and actual N+1/time.

### Definition of Done

The bounded contracts are aligned or an exact blocker is recorded. Evidence and independent review distinguish authoritative source changes from code, tests and connected runtime acceptance. Review/update the next dependent task before execution.
