---
atom_id: CA-M-176@22
ref_id: CA-M-176@22
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Output
    Publication
tier: 2
relations:
  method_for:
  - CA-R-1114
  derived_from:
  - CA-A-057
status: Archived
version: 22
updated_at: 2026-11-09 07:45:15 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-M-176@22-MCP-DECISION--regenerate-one-mcp-registry-deterministically.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
---

## Summary

Regenerate one MCP registry deterministically

## Claim

### Prose Claim

#### Applicable when

Every local release and image rebuild, before the MCP server starts.

#### Procedure

Generate the runtime registration asset from the installed code-owned provider inventory and canonical provider descriptors. Derive typed schemas from their code models, validate names and descriptors, and write deterministic output inside the package before its final identity verification. The image build regenerates the same asset from its copied engine code. Do not read native Atoms or call a capability during generation.

MCP loads that generated asset on startup. A source Atom edit does not change exposure or require a generic call-time source catalog scan. Replacing a running implementation follows the existing explicit restart or optional hot-reload boundary; hot reload stays disabled by default.

The actual tools/list export after readiness is a separate discovery output, not the executable registration input.

#### Outcome

Equivalent installed code and inventory produce equivalent registration bytes. Build failure stops delivery before startup; invalid individual descriptors retain the existing attributable diagnostics.

#### Failure or stop

Report unresolved code/configuration, duplicate identities, invalid generator output or generation failure. Do not rebuild registration from Atoms as a fallback.
