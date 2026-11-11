---
atom_id: CA-D-544
ref_id: CA-D-544
container:
  scope_unit: CA-SU-24
role: Delivery
form: Decision
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Authoring <+ Prompt Authoring
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery
  - MODEL//CAPRMEDIO <+ Carrier
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Step
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Action
tier: 4
status: Active
version: 20
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-D-544-PROMPTS-DECISION--deliver-current-implementation-workflow-prompt-carriers.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/07_delivery
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---

## Summary

Deliver current Implementation Workflow prompt carriers

## Claim

### Prose Claim

the package **must** contain only `CA-O-231`, `CA-O-232`, `CA-O-233`, `CA-O-094`, `CA-O-234`, `CA-O-096`, `CA-O-099`, and `CA-O-239` `.prompt.md` carriers, plus `README.md`, `definition_frontier.projection.json`, and `tests/`.

## Details

### Scope

the definition-only shared-context package at `LAYER_2_FRAMEWORK_ENGINE/FEATURE_AGENTIC/FEATURE_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/SHARED_CONTEXT/`.

Each prompt header carries exact Step, Action, and context. This Delivery specifies definition-only carriers, not executable admission. Keep the existing native package, executable source_bindings, and frozen corpus unchanged until separately admitted runtime realization; do not dispatch these definitions through the old adapter.
