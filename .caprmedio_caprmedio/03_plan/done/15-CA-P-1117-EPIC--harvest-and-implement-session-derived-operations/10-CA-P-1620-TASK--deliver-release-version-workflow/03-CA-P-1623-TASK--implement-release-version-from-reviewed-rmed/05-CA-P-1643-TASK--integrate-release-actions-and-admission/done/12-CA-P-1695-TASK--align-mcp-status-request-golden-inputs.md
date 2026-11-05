---
atom_id: CA-P-1695
ref_id: CA-P-1695
role: Plan
form: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
topics:
  main_subject: Subject/Graph Node/Engineering/Evaluation Implementation
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Manifest
  - Subject/Graph Node/Engineering/Evaluation Implementation
  - Subject/Graph Node/Engineering/Workflow
version: 9
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1643
  blocks:
  - CA-P-1644
tier: 3
container:
  atom: CA-P-1643
carrier_destination:
  file:
    name: 12-CA-P-1695-TASK--align-mcp-status-request-golden-inputs.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/10-CA-P-1620-TASK--deliver-release-version-workflow/3-CA-P-1623-TASK--implement-release-version-from-reviewed-rmed/5-CA-P-1643-TASK--integrate-release-actions-and-admission/done
---
# Summary

Align MCP status-request golden inputs

## Objective

Within <=15 minutes, align MCP status-request golden inputs.

## Details

Own only the two MCP golden test files containing test_every_selected_route_forwards_one_mutation_free_preview and test_current_physical_manifest_freezes_original_thirteen_through_queue, plus their existing fixture helper if necessary. Current failures use obsolete route_input for change_atom_status; current accepted admission requires actual target and status. Construct real disposable Atom/model/structure bindings without weakening status, source, preview, queue or no-mutation guards. Golden first, run the focused MCP suites. No production code or actual manifest/source changes, runtime/image/queue-process effects, Git/Plan writes or permission workaround. Preserve other Agents' edits; report pre-existing versus corrected findings truthfully.

## Definition of Done

The exact targeted saved effects/refusals and focused cases pass with code/test hashes. Required parent integration and image proof remain separate.

## Result

The only changed file is tests/test_selected_routes_mcp.py, SHA-256 `a9b68ee839cd4164563abd7ded89feaad9fa3fc1a6b04efd73988207935a5f2d`. Actual target/status descriptors and copied source-bound models/Project Structure replace obsolete status placeholders; the queue fixture uses a real preview receipt. Root ran all twelve tests in the designated development worker: twelve pass in1.476s. The worker's host verification was incomplete, not called a pass. This proves fixture/development regression behavior only, not actual queue-process or immutable-image acceptance.
