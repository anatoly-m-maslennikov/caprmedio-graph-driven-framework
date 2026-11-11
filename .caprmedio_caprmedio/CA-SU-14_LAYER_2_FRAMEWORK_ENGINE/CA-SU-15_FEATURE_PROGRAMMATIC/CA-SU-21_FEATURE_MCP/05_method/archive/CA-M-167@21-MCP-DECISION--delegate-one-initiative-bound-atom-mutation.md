---
atom_id: CA-M-167
author: Anatoly Maslennikov
cce_form: method
cce_version: cce_1
container:
  scope_unit: CA-SU-21
current_scope_unit: MCP
destination:
  file:
    name: CA-M-167@21-MCP-DECISION--delegate-one-initiative-bound-atom-mutation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
form: Decision
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
ref_id: CA-M-167@21
relations:
  DERIVED_FROM:
  - CA-A-057
role: Method
status: archived
tier: 2
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
updated_at: 2026-11-11 14:19:47 +0400
version: 21
---

## Summary

Delegate one Initiative-bound Atom mutation

## Claim

### Prose Claim

#### Applicable when

Apply **when** an Initiative-bound project-local MCP operation requests an Atom mutation. For the six Atom Lifecycle Tools, forward the request and selected Project to the runtime backend under CA-R-1105.

#### Procedure

1. Preserve the human-origin Initiative **and** select the one canonical Atom Tool **without** resolving its target **or** lifecycle meaning.
2. Forward the sealed request **to** that Tool **and** return its structured outcome unchanged.
3. Report success **only** **after** the canonical Tool returns its acknowledged outcome; preserve a rejection, conflict, partial result, **or** blocked result as such.

#### Outcome

MCP transports one authorized mutation request **without** becoming the target, mutation, recovery, **or** success-state owner.

#### Failure or stop

Stop **and** return an explicit failure **when** authorization, Initiative, canonical Tool selection, **or** the Tool outcome is absent **or** invalid.
