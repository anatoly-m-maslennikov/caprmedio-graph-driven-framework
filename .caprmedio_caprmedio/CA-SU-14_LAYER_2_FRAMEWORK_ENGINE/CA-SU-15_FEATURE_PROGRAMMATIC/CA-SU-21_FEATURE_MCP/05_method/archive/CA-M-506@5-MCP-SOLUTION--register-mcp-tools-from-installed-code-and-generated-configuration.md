---
atom_id: CA-M-506
ref_id: CA-M-506@5
container:
  scope_unit: CA-SU-21
role: Method
form: Solution
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 2
relations:
  method_for:
  - CA-R-3013
  - CA-R-1108
status: Archived
version: 5
updated_at: 2026-11-09 21:15:45 +0400
carrier_destination:
  file:
    name: CA-M-506@5-MCP-SOLUTION--register-mcp-tools-from-installed-code-and-generated-configuration.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Register MCP tools from installed code and generated configuration

## Claim

### Prose Claim

MCP tool exposure comes from installed code and configuration. Keep an explicit code-owned provider inventory and generate its deterministic runtime registration asset on every local release and image rebuild, before the server starts. Derive provider descriptions and typed schemas from code; do not derive eligibility from Atom content, Tool folders, or a Project graph scan.

At startup, read the generated registration asset and register enabled providers and code-owned route names. Do not build a full Atom catalog, load a source-Workflow manifest to select exposed names, or reread an Atom catalog before a generic Tool call. A source Atom edit alone does not add, remove or change MCP exposure. Preserve Project selection, configured exclusions, duplicate-name checks, typed request/result validation and existing public call protocols.

Each operation retains its own input, source and business validation when it runs. Exposing a route does not claim that its business prerequisites are currently satisfied. Native Workbench tools remain available through their installed code-owned registrations; retired Tool and Workflow execution adapters are not restored by registration.

A missing or invalid generated registration asset is an explicit configuration error; do not fall back to Atom discovery. The tools/list response describes the admitted generated registration after exclusions; it does not authorize additional providers. Code hot reload remains optional and disabled by default.

MCP and the Workbench web interface are transport adapters to the same backend API. That backend invokes the real tools and owns shared operations. MCP translates protocol input and output; it does not implement a separate copy of business behavior. Reuse the existing in-process backend services and canonical Tool APIs in the modular monolith; do not add an internal HTTP hop or another server merely to connect these layers.

Use the official MCP Python SDK for MCP transport. The code/configuration and shared-backend changes do not replace that library.

Keep provider/factory and descriptor-factory bindings in the editable installed inventory. Generate names and schemas from installed provider code. Adding or modifying an installed Tool/provider and regenerating the asset must not require edits to a central gateway Tool-name allowlist or dispatch branch. Apply the explicit global `mcp_blacklist` and bound Project exclusions to publication, then enforce the same admission on every invocation.
