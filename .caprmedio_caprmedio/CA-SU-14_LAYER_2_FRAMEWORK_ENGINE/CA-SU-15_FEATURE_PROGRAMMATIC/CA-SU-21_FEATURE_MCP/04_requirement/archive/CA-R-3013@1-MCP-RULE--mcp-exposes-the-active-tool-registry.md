---
atom_id: CA-R-3013
ref_id: CA-R-3013@1
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source
    Selection
tier: 1
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-1106
  - CA-M-510
  - CA-M-168
status: Archived
version: 1
updated_at: 2026-11-09 21:15:45 +0400
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-3013@1-MCP-RULE--mcp-exposes-the-active-tool-registry.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
---

## Summary

MCP exposes the active Tool registry

## Claim

### Prose Claim

MCP must read the generated registration asset carried by the installed package, resolve only its code-owned provider entries, and apply the bound Project's configured exclusions. It must expose the resulting enabled installed code/configuration surface through existing backend adapters. Atom status, Subjects, Scope Unit graphs, Tool-folder discovery, and unlisted implementation helpers do not determine runtime exposure. Missing or malformed registration configuration is reported explicitly; MCP must not fall back to Atom discovery.

Load the installed registration asset when MCP starts or explicitly loads a rebuilt installed implementation.

The installed registration configuration must carry an explicit `mcp_blacklist` of exact public Tool names. Blacklisted Tools must not be exposed through MCP or admitted by direct MCP invocation. Bound Project exclusions may further restrict exposure; they cannot re-enable a globally blacklisted Tool. An internal or CLI implementation may remain installed without MCP exposure.
