---
identity:
  atom_id: CA-M-522
  ref_id: CA-M-522@1-draft
context:
  container:
    scope_unit: CA-SU-24
  role: method
  form: solution
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Authoring <+ Prompt Authoring
    dependencies:
    - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling
      <+ Source Retrieval
    - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow
    - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
    - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action
  tier: 3
state:
  status: draft
  version: 1
  updated_at: 2026-11-10 11:53:32 +0400
destination:
  file:
    name: CA-M-522@1-draft-SOLUTION--bind-implementation-prompts-to-current-workflow-sources.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/05_method/draft
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-1843
---
## Summary

Bind implementation prompts to current Workflow sources

## Claim scope

the PROMPTS implementation of a currently admitted Implementation Workflow.

## Claim

### Prose Claim

the Implementation **must** dispatch a Step prompt only with current, fully read Workflow, Step, and Action source bindings for its actually admitted graph. Context, required inputs, result labels, candidate/evidence freshness, and retry state must match those definitions. A staged shared-context definition is not executable route admission.

## Details

`source_bindings.json` is derived review evidence, not authority. Keep staged definition frontiers separate from the admitted runtime manifest and its frozen test corpus; do not relabel the old executable graph as current or enable an unsupported Step by changing a pin. A changed, absent, mismatched, or partially read source blocks the affected prompt until independent PROMPTS RMED review refreshes its binding; changing a pin only to satisfy a check is forbidden.
