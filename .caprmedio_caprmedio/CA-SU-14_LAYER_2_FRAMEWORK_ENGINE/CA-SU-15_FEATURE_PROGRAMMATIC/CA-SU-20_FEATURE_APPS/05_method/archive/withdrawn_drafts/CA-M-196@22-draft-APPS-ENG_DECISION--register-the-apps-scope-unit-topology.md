---
atom_id: CA-M-196
ref_id: CA-M-196@22-draft
container:
  scope_unit: CA-SU-20
role: Method
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
tier: 2
relations:
  method_for:
  - CA-R-1100
  derived_from:
  - CA-A-058
status: Draft
version: 22
updated_at: 2026-11-10 09:54:52 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
destination:
  file:
    name: CA-M-196@22-draft-APPS-ENG_DECISION--register-the-apps-scope-unit-topology.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/05_method/draft
---
## Summary

Register the APPS Scope Unit topology

## Claim

### Prose Claim

#### Applicable when

Use this Method **when** registering **or** changing an immediate APPS Scope Unit.

#### Procedure

1. Resolve the active APPS authority **and** the current immediate-child Scope Unit declarations.
2. Register `WORKBENCH`, `GRAPH_UI`, **and** `AGENT_HOST_PLUGINS` as distinct immediate unordered APPS children.
3. Assign the headless read model **and** service to `WORKBENCH`; assign the optional human interface to `GRAPH_UI`; retain host-specific packaging in `AGENT_HOST_PLUGINS`.
4. Verify that `WORKBENCH` exposes the complete headless boundary required by Tools **and** MCP without depending on `GRAPH_UI`.
5. State that every read model, interface, **and** Projection is derived support **and** does **not** become project authority.
6. Confirm that each declaration has one immediate typed owner, one identity, **and** no conflicting owner **or** responsibility claim.

#### Outcome

APPS has three identifiable immediate unordered children with separated server, optional UI, **and** host-plugin responsibilities.

#### Failure or stop

Stop **when** a required child is missing, duplicated, non-immediate, ordered, assigned a conflicting boundary, **or** given project authority; also stop when headless behavior depends on `GRAPH_UI`.
