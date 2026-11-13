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
version: 27
updated_at: '2026-11-12T17:12:00.434020+00:00'
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

Forward the operation and inputs to the bound Project runtime. If the runtime requests a correction, return the field errors and the fields to correct to the AI Agent in the MCP response. Do not request Operator input. Return the Run ID with the correction request. Keep the pending input in the live Project runtime so disconnecting a client does not discard it. Continue that exact Run by ID with only the requested fields or additional fields. Retain recognized valid fields, report invalid, missing and unknown fields, and validate the merged input before effects. Cancellation by ID clears a Run waiting for correction without applying inputs. After an effect, return a failure and its completed effects instead of continuing with a correction. Archive and Promote Draft forward an ordered batch to the same backend operations. Return the backend outcome under CA-R-1105 without replay or repair. The backend reuses the current Workbench Scope Unit projection, so a newly indexed valid Scope Unit is available without a runtime restart.

#### Initiative-bound procedure

Apply this procedure to Initiative-bound project-local Atom Tools.

1. Preserve the human-origin Initiative **and** select the one canonical Atom Tool **without** resolving its target **or** lifecycle meaning.
2. Forward the sealed request **to** that Tool **and** return its structured outcome unchanged.
3. Report success **only** **after** the canonical Tool returns its acknowledged outcome; preserve a rejection, conflict, partial result, **or** blocked result as such.

#### Outcome

The backend owns target selection, effects and verification. MCP forwards the request and reports the outcome.

#### Initiative-bound failure or stop

Stop and return an explicit failure if the Initiative, authorization, canonical Tool selection or Tool outcome is absent or invalid.
