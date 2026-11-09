---
atom_id: CA-R-1843
ref_id: CA-R-1843
container:
  scope_unit: CA-SU-24
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Prompt Authoring"
  dependencies:
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Retrieval"
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
tier: 3
status: Active
version: 15
updated_at: 2026-10-27 20:00:04 +0400
carrier_destination:
  file:
    name: CA-R-1843-PROMPTS-RULE--bind-implementation-prompts-to-current-workflow-sources.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/04_requirement
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---
# Summary

Bind implementation prompts to current Workflow sources

## Scope

the PROMPTS implementation of the admitted CA-O-016 Implementation Workflow.

## Claim

the Implementation **must** dispatch a Step prompt only with current, fully read Workflow, Step, and Action source bindings for its actually admitted graph. Context, required inputs, result labels, candidate/evidence freshness, and retry state must match those definitions. A staged shared-context definition is not executable route admission.

## Details

`source_bindings.json` is derived review evidence, not authority. Keep staged definition frontiers separate from the admitted runtime manifest and its frozen test corpus; do not relabel the old executable graph as current or enable an unsupported Step by changing a pin. A changed, absent, mismatched, or partially read source blocks the affected prompt until independent PROMPTS RMED review refreshes its binding; changing a pin only to satisfy a check is forbidden.
