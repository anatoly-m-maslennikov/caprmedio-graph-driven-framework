---
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on: []
version: 22
updated_at: 2026-10-27 06:04:45 +0400
relations:
  method_for:
  - CA-R-1096
  derived_from:
  - CA-A-058
atom_id: CA-M-193
content_role: Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
type: Eng Decision
tier: 4
---
# Summary

Supply the active Tool frontier to MCP

## Scope

The source-bound active callable Tool and Workflow frontier for a Project, and
the initial union of those validated per-Project frontiers in the shared MCP
runtime.

## Claim

Direct read and query Tools delegate to their canonical providers without a
mandatory Workflow Orchestrator wrapper. Internal CONNECTORS/adapters and
PROJECT_TOOLS are not members of this MCP callable frontier. A shared runtime
may publish the union of valid native Project frontiers, but every invocation
still uses one validated Project binding and no Tool meaning changes.

## Details

### Applicable when

apply **when** MCP builds **or** refreshes the callable frontier supplied by TOOLS.

### Procedure

1. enumerate the complete current set of active declared callable CAPRMEDIO Tools and declared Workflows from the
   source-bound capability frontier.
2. read **and** validate **every** active Tool's or Workflow's machine-invocation contract **without**
   inferring missing meaning from its code **or** runtime state.
3. project **=1** stable callable endpoint for **every** valid active Tool.
4. omit inactive **and** explicitly disabled Tools; report **every** invalid active
   Tool as a diagnostic rather than silently omitting it.
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

### Outcome

MCP exposes one complete, deterministic projection of valid active Tools and Workflows **and**
remains a replaceable interface rather than a second Tool authority.
preserving an earlier frontier **after** a failed refresh does **not** make it current;
apply the publication boundary **in** CA-R-1110.

### Failure or stop

stop refresh **and** preserve the preceding valid frontier **when** active Tool or Workflow
enumeration is incomplete, endpoint identities collide, **or** a machine contract
is missing **or** invalid. reject a call that cannot delegate unchanged.

### Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [Model Context Protocol: tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)
