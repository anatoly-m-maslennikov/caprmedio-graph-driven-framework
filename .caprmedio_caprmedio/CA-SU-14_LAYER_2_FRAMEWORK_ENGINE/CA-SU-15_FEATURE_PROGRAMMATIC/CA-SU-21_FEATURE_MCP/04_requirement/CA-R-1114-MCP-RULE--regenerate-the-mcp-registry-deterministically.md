---
atom_id: CA-R-1114
ref_id: CA-R-1114
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Output
    Publication
tier: 1
status: Active
version: 22
updated_at: 2026-11-09 21:15:45 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
carrier_destination:
  file:
    name: CA-R-1114-MCP-RULE--regenerate-the-mcp-registry-deterministically.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-176
---

## Summary

Regenerate the MCP registry deterministically

## Claim

### Prose Claim

MCP registry generation **must** be a programmatic deterministic derivation from `schema_version: 1` capability descriptors in the activated installed runtime. It **must** resolve **and** seal the complete descriptor source frontier before publication, use stable ordering, and produce the same semantic registry from the same descriptors **and** activated Project state. It **must not** read a checkout as a live registry source, maintain a manually edited MCP-core allowlist, or execute a capability while generating the registry.

Repeated generation over an unchanged frontier **must** be idempotent, and volatile execution metadata **must not** change MCP capability identity **or** schema. A changed activated installed image **or** descriptor frontier creates a new registry generation; existing calls remain bound to their captured generation, and notification evidence **must** distinguish an emitted change notice from confirmed client refresh.

## Details

### Registry generation

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
