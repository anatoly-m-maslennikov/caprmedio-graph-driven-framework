---
atom_id: CA-M-181@17
ref_id: CA-M-181@17
container:
  scope_unit: CA-SU-21
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Result and Status Presentation
tier: 2
relations:
  method_for:
  - CA-R-1119
  derived_from:
  - CA-A-057
status: Archived
version: 17
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-M-181@17-MCP-ENG_DECISION--return-one-stable-model-readable-mcp-result.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
---
# Return one stable model-readable MCP result

## Applicable when

Apply **after** one canonical Tool returns an admitted outcome.

## Procedure

1. Map the Tool result, diagnostic, empty result, partial result, **or** failure **to** the declared protocol result form.
2. Preserve the original governed meaning **and** provenance.
3. Distinguish a protocol failure from a Tool failure **and** omit internal implementation details from the public response.

## Outcome

the model receives a stable, headless-readable result that retains the Tool outcome's meaning.

## Failure or stop

Stop **and** return an explicit protocol failure **when** the result cannot be represented **without** semantic loss **or** boundary leakage.
