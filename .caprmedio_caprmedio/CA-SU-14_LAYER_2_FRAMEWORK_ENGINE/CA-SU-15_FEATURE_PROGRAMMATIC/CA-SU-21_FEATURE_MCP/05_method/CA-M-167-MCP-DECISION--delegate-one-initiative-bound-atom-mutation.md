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
status: active
version: 26
updated_at: '2026-11-12T09:54:14.160142+00:00'
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

Forward the operation and inputs to the bound Project runtime. If the runtime requests a correction, return the field errors and the fields to correct to the AI Agent in the MCP response. Do not request Operator input. The next call in the same Project, client session and Tool may supply just those fields or include other input fields. Merge the new inputs with the retained inputs and validate again before any effect. A call with only `cancel: true` clears the pending operation without applying any inputs. After an effect, return a failure and its completed effects instead of continuing with a correction. Archive and Promote Draft forward an ordered batch to the same backend operations. Return the backend outcome under CA-R-1105 without replay or repair. The backend reuses the current Workbench Scope Unit projection, so a newly indexed valid Scope Unit is available without a runtime restart.

#### Initiative-bound procedure

Apply this procedure to Initiative-bound project-local Atom Tools.

1. Preserve the human-origin Initiative **and** select the one canonical Atom Tool **without** resolving its target **or** lifecycle meaning.
2. Forward the sealed request **to** that Tool **and** return its structured outcome unchanged.
3. Report success **only** **after** the canonical Tool returns its acknowledged outcome; preserve a rejection, conflict, partial result, **or** blocked result as such.

#### Outcome

The backend owns target selection, effects and verification. MCP forwards the request and reports the outcome.

#### Initiative-bound failure or stop

Stop and return an explicit failure if the Initiative, authorization, canonical Tool selection or Tool outcome is absent or invalid.
