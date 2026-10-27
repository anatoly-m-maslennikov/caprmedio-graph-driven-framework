---
atom_id: CA-P-1528
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Subject/Graph Node/Engineering/Workflow
  depends_on:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/MCP
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Engineering/Implementation Evaluation
version: 10
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1520
  blocks:
  - CA-P-1529
tier: 3
---
# Summary

prove query workflows in a fresh immutable image

## Objective

Within <=15 minutes, prove both query Workflows through the integrated existing MCP/orchestrator route in a freshly built immutable image. No host-mount substitution, source/RMED revision, or broad Docker inventory.

### Exact inputs, output, ownership, and gate

Inputs: accepted/passing P1527 integration and current Docker golden harness. Ownership: the query-specific fresh-image E2E fixture/test additions under the existing Docker harness and its exact evidence record. Output: image identity plus actual two-route E2E results, source snapshot and truthful Workflow/Action Journal evidence.

P1527 is a true dispatch blocker. Verify default IDs, selected fetch, allowed filters/statuses/properties, pagination/coverage, all required diagnostics, no arbitrary evaluation or secret return, read-only/no-authority behavior, and no undeclared host code/dependencies. A failed/blocked image path remains unfinished with a typed Concern; P1123's wider image closure is separate.

### Definition of Done

Fresh-image proof covers both routes and required negative cases with retained results; an image build or host-only pass is insufficient.
