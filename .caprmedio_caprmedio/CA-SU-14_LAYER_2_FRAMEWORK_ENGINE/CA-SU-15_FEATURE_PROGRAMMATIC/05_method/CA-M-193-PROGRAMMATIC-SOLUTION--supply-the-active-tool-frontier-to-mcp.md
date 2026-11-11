---
identity:
  atom_id: CA-M-193
  ref_id: CA-M-193
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication
  tier: 4
relations:
  method_for:
  - CA-R-1096
  DERIVED_FROM:
  - CA-A-058
state:
  status: Active
  version: 29
  updated_at: 2026-11-10 20:47:54 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
destination:
  file:
    name: CA-M-193-PROGRAMMATIC-SOLUTION--supply-the-active-tool-frontier-to-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
---

## Summary

Supply the active Tool frontier to MCP

## Claim

### Prose Claim

Direct read and query Tools delegate to their canonical providers without a
mandatory Workflow Orchestrator wrapper. Internal CONNECTORS/adapters and
PROJECT_TOOLS are not members of this MCP callable frontier. A shared runtime
may publish the union of valid native Project frontiers, but every invocation
still uses one validated Project binding and no Tool meaning changes.

## Details

### Scope

The installed code/configuration-bound callable Tool and Workflow frontier for a Project, and
the initial union of those validated per-Project frontiers in the shared MCP
runtime.

#### Applicable when

apply **when** MCP builds **or** refreshes the callable frontier supplied by TOOLS.

#### Procedure

1. read the generated registration asset produced from the installed code-owned provider and route inventory before build/startup. Do not enumerate source Atoms or source-Workflow manifests to select exposed names.
2. validate each configured public provider's canonical code-defined machine-invocation models and descriptor without executing its operation. Runtime registration is code/configuration; operation-level source and business validation remains with the shared backend.
3. project exactly one stable endpoint for each valid enabled public name; source-only provider entries have no MCP endpoint.
4. omit unconfigured or explicitly disabled Tools; report each invalid configured provider as a diagnostic. Atom status does not control exposure.
5. delegate **every** admitted call **to** its declared Tool or Workflow provider **without** duplicating **or** changing its
   meaning, inputs, outcomes, **or** mechanics.
6. replace the exposed frontier **only** **after** the complete candidate projection
   validates; preserve the preceding valid frontier **when** refresh fails.
7. For a shared runtime, eagerly validate the bounded candidate Project
   frontiers and publish their initial union. Admit a same-name Tool across
   Projects only when its input and output schemas are identical; quarantine
   and diagnose the affected Project Tool on a conflict.
8. Add the outer `project_root` only at the native input schema root while
   preserving `$defs`, then pass the native request and result contract
   unchanged to the bound Project provider. An inactive or disabled Project
   Tool refuses the call. A new Tool name requires explicit shared restart and
   client reconnect; do not assume `tools/list_changed`.

#### Outcome

MCP exposes one complete, deterministic projection of valid active Tools and Workflows **and**
remains a replaceable interface rather than a second Tool authority.
preserving an earlier frontier **after** a failed refresh does **not** make it current;
apply the publication boundary **in** CA-R-1110.

#### Failure or stop

stop refresh **and** preserve the preceding valid frontier **when** active Tool or Workflow
enumeration is incomplete, endpoint identities collide, **or** a machine contract
is missing **or** invalid. reject a call that cannot delegate unchanged.

#### Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [Model Context Protocol: tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis_and_advisory/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)
