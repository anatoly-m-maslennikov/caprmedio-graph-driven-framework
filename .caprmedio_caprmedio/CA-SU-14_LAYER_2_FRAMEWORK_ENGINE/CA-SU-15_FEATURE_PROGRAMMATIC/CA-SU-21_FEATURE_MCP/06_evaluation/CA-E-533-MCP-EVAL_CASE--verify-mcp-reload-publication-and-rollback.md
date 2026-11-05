---
atom_id: CA-E-533
ref_id: CA-E-533
role: Evaluation
form: Eval Case
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 19:59:37 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
tier: 3
container:
  scope_unit: CA-SU-21
carrier_destination:
  file:
    name: CA-E-533-MCP-EVAL_CASE--verify-mcp-reload-publication-and-rollback.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---
# Summary

Verify MCP reload publication and rollback

## Scope

server-side hot reload for the Project-local MCP gateway.

## Claim

the MCP Evaluation **must** verify implementation reload through the real stdio protocol with controlled mock implementations.

## Details

- keep one client connection open; call implementation A, reload B, then call B successfully without reconnect.
- add, remove **and** change a Tool contract; verify the published list **and** negotiated notification.
- submit syntax-invalid code, initialization failure, duplicate Tool names **and** invalid schemas; verify rejection **and** continued service from A.
- reload the same frontier twice; verify unchanged generation **and** no duplicate effects.
- submit an extra field, traversal path **or** alternate Project root; verify rejection before execution.
- distinguish sent notification from unconfirmed client refresh; mocks do **not** prove Codex desktop discovery.

