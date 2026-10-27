---
atom_id: CA-P-1797
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 7
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Implementation Evaluation
  depends_on:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Evaluation
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  is_decomposition_of:
  - CA-P-1794
  relates_to:
  - CA-C-503
tier: 3
---
# Summary

Require preparation Evaluation authority

## Objective

require the bound Evaluation at preparation and test missing, stale and wrong-role bindings before any agent call.

## Details

- keep this repair bounded to its confirmed source contract. shared installed runtime, frozen candidates and historical Journals remain unchanged by fixture tests.
- preserve independent workers' edits; root owns Git, source pins and Release integration.

## Definition of Done

the preparation rejection matrix and focused prompt/binding suites pass; rejected cases call no agent.

## Result

the preparation test rejects missing, stale and wrong-role Evaluation bindings before dispatch. the focused prompt-contract suite passes 20 tests and selected-project-binding suite passes seven; independent review accepts the repair. actual full Release completion remains a separate unfinished gate.
