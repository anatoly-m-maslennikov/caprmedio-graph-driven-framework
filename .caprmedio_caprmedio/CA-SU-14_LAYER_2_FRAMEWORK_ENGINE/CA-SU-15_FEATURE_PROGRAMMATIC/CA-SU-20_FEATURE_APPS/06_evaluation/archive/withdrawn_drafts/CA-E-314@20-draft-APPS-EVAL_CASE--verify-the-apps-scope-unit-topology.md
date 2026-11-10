---
atom_id: CA-E-314
ref_id: CA-E-314@20-draft
container:
  scope_unit: CA-SU-20
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
relations:
  evaluation_for:
  - CA-M-196
status: Draft
version: 20
updated_at: 2026-11-10 09:54:52 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
destination:
  file:
    name: CA-E-314@20-draft-APPS-EVAL_CASE--verify-the-apps-scope-unit-topology.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/06_evaluation/draft
---
## Summary

Verify the APPS Scope Unit topology

## Claim

### Prose Claim

#### Claim checked

CA-M-196 registers the three immediate unordered APPS units with distinct responsibilities **and** without project authority.

#### Applicable when

Apply whenever an immediate APPS child's ownership, structural identity, responsibility boundary, **or** realization path changes.

#### Test case

Examine the current active APPS authority and its child declarations, using derived representations only as supporting evidence. Exercise graph access once with `GRAPH_UI` absent.

#### Acceptance criteria

`WORKBENCH`, `GRAPH_UI`, **and** `AGENT_HOST_PLUGINS` are distinct immediate unordered APPS children. `WORKBENCH` operates headlessly for Tools **and** MCP; `GRAPH_UI` remains optional; **and** no child becomes project authority.

#### Failure disposition

Reject the topology and preserve the examined authority, supporting evidence, **and** every missing, duplicate, dependent, **or** conflicting boundary.
