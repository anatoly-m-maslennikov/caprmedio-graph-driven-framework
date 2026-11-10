---
atom_id: CA-E-368
ref_id: CA-E-368@23
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Static
    Analysis/Python Code
tier: 6
relations:
  evaluation_for:
  - CA-M-419
  - CA-E-539
  derived_from:
  - CA-A-053
status: Archived
version: 23
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
    name: CA-E-368@23-PROGRAMMATIC-EVAL_CASE--externalize-a-large-static-mapping.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
---
## Summary

Externalize a large static mapping

## Claim

### Prose Claim

#### Claim checked

one large reusable static mapping is stored outside a hand-authored Python
module while its loader retains a typed, validated boundary.

#### Test case

evaluate one changed Python module containing a static mapping above 20 entries
**or** 25 source lines.

#### Acceptance criteria

pass **only** **when** the mapping is moved **to** TOML by default, JSON for a schema **or**
machine-interchange need, **or** YAML for one declared distinct feature; its loader
**must** validate the expected structure **without** changing the mapping's meaning.

#### Failure disposition

reject the source-size claim **until** data **and** executable behavior are separated.

#### Sources

- [CA-M-419 — Ratchet hand-authored Python source boundaries](../05_method/CA-M-419-PROGRAMMATIC-ENG_POLICY--ratchet-hand-authored-python-source-boundaries.md)
- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)
- [Python documentation: `json`](https://docs.python.org/3.14/library/json.html)
