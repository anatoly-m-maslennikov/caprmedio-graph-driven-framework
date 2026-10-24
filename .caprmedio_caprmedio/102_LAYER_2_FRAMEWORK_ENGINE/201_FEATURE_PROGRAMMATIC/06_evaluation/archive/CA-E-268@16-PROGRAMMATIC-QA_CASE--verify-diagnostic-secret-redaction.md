---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Operational Diagnostics
  depends_on: []
version: 16
updated_at: 2026-10-24 01:28:26 +0400
relations:
  evaluation_for:
  - CA-M-414
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-268@16
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eval Case
---
# Verify diagnostic secret redaction

## Claim checked

one PROGRAMMATIC diagnostic path sanitizes a sensitive input **before** its record
is exposed **to** the declared sink.

## Applicable conditions

apply **when** a diagnostic path could receive sensitive **or** secret-bearing input.
paths whose declared inputs contain no such value are **not** applicable.

## Test case

Supply one secret-bearing input **to** one declared diagnostic path.

## Acceptance criteria

pass **only** **when** the exposed record retains the diagnostic context while omitting
**or** irreversibly redacting the secret-bearing value.

## Failure disposition

stop the diagnostic path **and** correct its sanitization boundary **before** release.

## Sources

- [CA-M-414 — Emit structured operational diagnostics](../05_method/CA-M-414-PROGRAMMATIC-STANDARD-ENG_POLICY--emit-structured-operational-diagnostics.md)
