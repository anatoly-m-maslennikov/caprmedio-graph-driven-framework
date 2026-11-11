---
identity:
  atom_id: CA-M-draft
context:
  container:
    scope_unit: CA-SU-21
  role: Method
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
  tier: 0
state:
  status: Draft
  version: 1
  updated_at: 2026-11-11 04:14:10 +0400
destination:
  file:
    name: CA-M-draft-MCP-SOLUTION--expose-selected-workflows-as-mcp-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/draft/cfel-native-workflow-architecture
author: Anatoly Maslennikov
---

## Summary

Expose selected Workflows as MCP Tools

## Claim

### Prose Claim

Publish selected Workflow interfaces as MCP Tools. An external public name maps to a Workflow definition and its public input/output contract; invocation enters the Workflow Engine API. Even a Workflow with one Action follows this path. An internal Tool is an implementation capability, not a synonym for an MCP Tool.

## Semantics

Use editable exposure configuration and a generated registration projection. Resolve public names to selected validated Workflow definitions and derive their public schemas and documentation from those contracts. Bind their Action interfaces to trusted installed implementations through the internal registry. Do not import or execute code named by arbitrary Project text, run a capability during generation, or publish an internal helper merely because it is installed.

Keep global blacklist and bound Project exclusions effective for listing and invocation. A Project exclusion cannot re-enable a globally denied interface. Preserve trusted Project binding and the public protocol envelope; no global mutable current Project or cross-Project fallback is introduced.

Every public Tool supports `help: true` as an input shape admitted before business-required fields at the protocol schema boundary. It returns only that exposed Workflow's purpose, parameters, formats/allowed values, minimal examples, output contract and common errors. Help, protocol initialization and interface listing are metadata operations: they do not start a business Run, invoke an Action or create business effects. This is an inspection branch of the interface, not a direct internal Tool execution shortcut.

Source discovery alone does not publish a Workflow. Current/Draft indexing, explicit exposure selection and runtime execution are separate operations. New definitions using supported constructs and installed Actions can be published through the adopted definition/registration process without a new workflow-specific Python route; schema freshness and exact source attribution still apply.

## Details

The Current registry contracts describe code-owned provider registration. Their explicit no-source-Workflow clauses must be revised before this architecture is active; existing canonical implementation schemas remain the internal Action/Tool boundary. Existing public names may be preserved only through an explicit mapping to suitable Workflow definitions, with compatibility checked at adoption. The current working read-only MCP image remains unchanged.
