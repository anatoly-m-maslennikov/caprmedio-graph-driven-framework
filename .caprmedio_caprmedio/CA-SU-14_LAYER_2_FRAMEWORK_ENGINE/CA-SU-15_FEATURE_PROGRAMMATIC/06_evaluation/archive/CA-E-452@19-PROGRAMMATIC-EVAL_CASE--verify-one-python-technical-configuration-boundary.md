---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Technical Configuration Boundary
  depends_on: []
version: 19
updated_at: 2026-10-24 11:58:20 +0400
relations:
  evaluation_for:
  - CA-M-412
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-452@19
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 5
type: Eval Case
---
# Verify one Python technical configuration boundary

## Claim checked

the selected Python series **and** development-tool profiles have one canonical
technical materialization distinct from CAPRMEDIO project settings.

## Test case

compare the root `pyproject.toml`, local workflow, **and** automated workflow
selections for the interpreter **and** one admitted development tool.

## Acceptance criteria

pass **only** **when** **all** consumers resolve the current interpreter boundary
selected by CA-M-412 **and** the same admitted development-tool profile,
**and** no CAPRMEDIO runtime setting is duplicated **in** `pyproject.toml`.

## Failure disposition

reject the conflicting carrier **or** workflow **until** one Method-owned selection is
materialized once.

## Sources

- [PyPA: `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [CA-M-412 — Declare one Python and software configuration boundary](../05_method/CA-M-412-PROGRAMMATIC-ENG_POLICY--declare-one-python-and-software-configuration-boundary.md)
