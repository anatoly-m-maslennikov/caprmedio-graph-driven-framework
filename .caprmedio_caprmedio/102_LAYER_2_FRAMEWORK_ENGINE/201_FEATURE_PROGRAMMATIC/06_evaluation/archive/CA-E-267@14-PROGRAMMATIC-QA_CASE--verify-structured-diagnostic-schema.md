---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Operational Diagnostics
  depends_on: []
version: 14
updated_at: 2026-10-23 23:58:37 +0400
relations:
  evaluation_for:
  - CA-M-414
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-267@14
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
author: Anatoly Maslennikov
---
# Verify structured diagnostic schema

## Claim checked

one PROGRAMMATIC operational diagnostic uses an admitted severity **and** provides
the actionable contextual fields required by its declared schema.

## Applicable conditions

apply **when** a component emits a diagnostic for normal operation, degraded
operation, failure, recovery, **or** diagnostic detail.

## Test case

evaluate one emitted diagnostic record for a declared component event.

## Acceptance criteria

pass **only** **when** the record uses ERROR, WARNING, INFO, **or** DEBUG, includes its
declared actionable contextual fields, **and** does **not** repurpose Journal history
as an operational diagnostic.

## Failure disposition

reject the diagnostic path **until** its schema **and** severity are corrected.

## Sources

- [CA-M-414 — Emit structured operational diagnostics](../05_method/CA-M-414-PROGRAMMATIC-STANDARD-ENG_POLICY--emit-structured-operational-diagnostics.md)
