---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Source Unit Responsibility
  depends_on: []
version: 17
updated_at: 2026-10-24 10:48:25 +0400
relations:
  evaluation_for:
  - CA-M-419
  - CA-E-539
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-368@17
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 6
type: Eval Case
---
# Externalize a large static mapping

## Claim checked

one large reusable static mapping is stored outside a hand-authored Python
module while its loader retains a typed, validated boundary.

## Test case

evaluate one changed Python module containing a static mapping above 20 entries
**or** 25 source lines.

## Acceptance criteria

pass **only** **when** the mapping is moved **to** TOML by default, JSON for a schema **or**
machine-interchange need, **or** YAML for one declared distinct feature; its loader
**must** validate the expected structure **without** changing the mapping's meaning.

## Failure disposition

reject the source-size claim **until** data **and** executable behavior are separated.

## Sources

- [CA-M-419 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-419-PROGRAMMATIC-ENG_POLICY--ratchet-hand-authored-python-source-boundaries.md)
- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)
- [Python documentation: `json`](https://docs.python.org/3.14/library/json.html)
