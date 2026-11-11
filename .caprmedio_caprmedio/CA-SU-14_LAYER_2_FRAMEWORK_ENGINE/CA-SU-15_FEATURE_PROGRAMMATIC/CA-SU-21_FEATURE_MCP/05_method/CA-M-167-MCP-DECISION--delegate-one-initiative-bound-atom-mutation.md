---
atom_id: CA-M-167
ref_id: CA-M-167
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
tier: 2
relations:
  DERIVED_FROM:
  - CA-A-057
status: Active
version: 23
updated_at: 2026-11-11 17:36:58 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-M-167-MCP-DECISION--delegate-one-initiative-bound-atom-mutation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method
---

## Summary

Delegate one Initiative-bound Atom mutation

## Claim

### Prose Claim

#### Atom Lifecycle Tools

Forward the operation and inputs to the bound Project runtime. If the runtime requests a correction, use an MCP form in the same call when the client supports it. Otherwise return the fields to correct. The next call in the same Project, client session and Tool may supply just those fields, plus any other corrections. Merge the corrections with the retained inputs and validate again before any effect. Return the backend outcome under CA-R-1105.

#### Initiative-bound procedure

Apply this procedure to Initiative-bound project-local Atom Tools.

1. Preserve the human-origin Initiative **and** select the one canonical Atom Tool **without** resolving its target **or** lifecycle meaning.
2. Forward the sealed request **to** that Tool **and** return its structured outcome unchanged.
3. Report success **only** **after** the canonical Tool returns its acknowledged outcome; preserve a rejection, conflict, partial result, **or** blocked result as such.

#### Outcome

The backend owns target selection, effects and verification. MCP forwards the request and reports the outcome.

#### Initiative-bound failure or stop

Stop and return an explicit failure if the Initiative, authorization, canonical Tool selection or Tool outcome is absent or invalid.
