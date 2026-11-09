---
atom_id: CA-M-167
ref_id: CA-M-167
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 2
relations:
  method_for:
  - CA-R-1105
  derived_from:
  - CA-A-057
status: Active
version: 19
updated_at: 2026-11-09 07:45:15 +0400
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

#### Applicable when

Apply **when** an authorized project-local MCP operation requests an Atom mutation.

#### Procedure

1. Preserve the human-origin Initiative **and** select the one canonical Atom Tool **without** resolving its target **or** lifecycle meaning.
2. Forward the sealed request **to** that Tool **and** return its structured outcome unchanged.
3. Report success **only** **after** the canonical Tool returns its acknowledged outcome; preserve a rejection, conflict, partial result, **or** blocked result as such.

#### Outcome

MCP transports one authorized mutation request **without** becoming the target, mutation, recovery, **or** success-state owner.

#### Failure or stop

Stop **and** return an explicit failure **when** authorization, Initiative, canonical Tool selection, **or** the Tool outcome is absent **or** invalid.
