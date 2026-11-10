---
atom_id: CA-E-533
ref_id: CA-E-533
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - MODEL//CAPRMEDIO <+ Package/Project Package
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification
    <+ Dynamic Testing
  - MODEL//CAPRMEDIO <+ Actor/Operator
  - MODEL//CAPRMEDIO <+ Project
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Workflow
  - MODEL//CAPRMEDIO <+ Atom
tier: 3
status: Active
version: 15
updated_at: 2026-11-10 20:47:54 +0400
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

### Reload publication checks

- Keep one client connection open; call A, reload B, then call B without reconnect. Add/remove/change a Tool contract and verify published list plus negotiated notification.
- Submit syntax-invalid code, initialization failure, duplicate Tool names, or invalid schemas; verify rejection and continued service from A. Reload the same frontier twice and verify unchanged generation/no duplicate effects.
- Submit an extra field, traversal path, or alternate Project root; verify rejection before execution. Distinguish sent notification from unconfirmed client refresh; mocks do not prove Codex desktop discovery.
- With hot reload disabled by default, MCP and Workbench retain tools without an implementation child and code changes require normal restart. With explicit opt-in, run existing reload publication/failure checks.
