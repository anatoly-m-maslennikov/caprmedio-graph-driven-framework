---
atom_id: CA-E-533
ref_id: CA-E-533
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic Testing
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
tier: 3
status: Active
version: 14
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-E-533-MCP-EVAL_CASE--verify-mcp-reload-publication-and-rollback.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Verify MCP reload publication and rollback

## Claim

### Prose Claim

the MCP Evaluation **must** verify implementation reload through the real stdio protocol with controlled mock implementations.

## Details

### Scope

server-side hot reload for the Project-local MCP gateway.

- keep one client connection open; call implementation A, reload B, then call B successfully without reconnect.
- add, remove **and** change a Tool contract; verify the published list **and** negotiated notification.
- submit syntax-invalid code, initialization failure, duplicate Tool names **and** invalid schemas; verify rejection **and** continued service from A.
- reload the same frontier twice; verify unchanged generation **and** no duplicate effects.
- submit an extra field, traversal path **or** alternate Project root; verify rejection before execution.
- distinguish sent notification from unconfirmed client refresh; mocks do **not** prove Codex desktop discovery.



With hot reload disabled by default, verify that MCP and Workbench serve their retained tools without starting an implementation child; code changes require normal process restart. With explicit opt-in, run the existing reload publication/failure checks.
