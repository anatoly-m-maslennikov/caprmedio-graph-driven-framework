---
atom_id: CA-R-1111
ref_id: CA-R-1111
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication <+ Interface Contracts
tier: 1
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-173
status: Active
version: 24
updated_at: 2026-11-10 20:47:54 +0400
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1111-MCP-RULE--delegate-mcp-calls-to-canonical-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
---

## Summary

Delegate MCP calls to canonical Tools

## Claim

### Prose Claim

**every** MCP Tool invocation **must** delegate **to** the selected canonical Tool executable **and** **must not** reimplement Tool decisions, project meaning, target resolution, validation, mutation, recovery behavior, **or** lifecycle semantics inside the MCP carrier. MCP owns **only** transport admission, canonical Tool selection, delegation, **and** result transport.

**every** Finder **and** **every** Doer dry run **must** remain independently executable **without** MCP. A direct executable invocation of a CAPRMEDIO Markdown Atom Doer with `--apply` **must** reject the request **unless** it carries the authorized project-local MCP delegation **and** its sealed Initiative action envelope. Introducing MCP **must not** create a Tool dependency on MCP **or** another APPS unit.

## Details

For an exposed validated Tool request, select the canonical Tool executable from the current registry, forward it without substituting MCP behavior, and transport the Tool result with every failure and side-effect boundary. Stop when canonical selection, request validation, or delegated execution fails.
