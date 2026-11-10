---
atom_id: CA-E-452
ref_id: CA-E-452@24
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Code
    Authoring/Python Code
tier: 5
relations:
  evaluation_for:
  - CA-M-412
  derived_from:
  - CA-A-053
status: Archived
version: 24
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-E-452@24-PROGRAMMATIC-EVAL_CASE--verify-one-python-technical-configuration-boundary.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
---
## Summary

Verify one Python technical configuration boundary

## Claim

### Prose Claim

#### Claim checked

the selected Python series **and** development-tool profiles have one canonical
technical materialization distinct from CAPRMEDIO project settings.

#### Test case

compare the root `pyproject.toml`, local workflow, **and** automated workflow
selections for the interpreter **and** one admitted development tool.

#### Acceptance criteria

pass **only** **when** **all** consumers resolve the current interpreter boundary
selected by CA-M-412 **and** the same admitted development-tool profile,
**and** no CAPRMEDIO runtime setting is duplicated **in** `pyproject.toml`.

#### Failure disposition

reject the conflicting carrier **or** workflow **until** one Method-owned selection is
materialized once.

#### Sources

- [PyPA: `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [CA-M-412 — Declare one Python and software configuration boundary](../05_method/CA-M-412-PROGRAMMATIC-ENG_POLICY--declare-one-python-and-software-configuration-boundary.md)
