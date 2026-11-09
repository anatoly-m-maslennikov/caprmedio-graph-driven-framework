---
atom_id: CA-R-1119
ref_id: CA-R-1119
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Result and Status Presentation
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/Interface
    Contracts
tier: 1
status: Active
version: 20
updated_at: 2026-11-09 21:15:45 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
carrier_destination:
  file:
    name: CA-R-1119-MCP-RULE--return-stable-model-readable-mcp-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-181
---

## Summary

Return stable model-readable MCP results

## Claim

### Prose Claim

MCP **must** map Tool results, diagnostics, empty results, partial results, **and** failures into stable model-readable protocol responses while preserving their governed meaning **and** provenance. Responses **must** remain usable **without** a user interface, distinguish protocol failure from Tool failure, **and** **must not** expose internal implementation details as part of the public MCP contract.

## Details

### Result projection

#### Applicable when

Apply **after** one canonical Tool returns an admitted outcome.

#### Procedure

1. Map the Tool result, diagnostic, empty result, partial result, **or** failure **to** the declared protocol result form.
2. Preserve the original governed meaning **and** provenance.
3. Distinguish a protocol failure from a Tool failure **and** omit internal implementation details from the public response.

#### Outcome

the model receives a stable, headless-readable result that retains the Tool outcome's meaning.

#### Failure or stop

Stop **and** return an explicit protocol failure **when** the result cannot be represented **without** semantic loss **or** boundary leakage.
