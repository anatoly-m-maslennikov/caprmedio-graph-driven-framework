---
cce_version: cce_1
cce_form: method
subjects:
  governs: Subject/Graph Node/Engineering/MCP
  depends_on: []
version: 14
updated_at: 2026-10-25 17:32:27 +0400
relations:
  method_for:
  - CA-R-1119
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-181@14
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eng Decision
tier: 2
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
