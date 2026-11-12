---
identity:
  atom_id: CA-R-970308662
  ref_id: CA-R-970308662
context:
  role: requirement
  form: requirement
  container:
    scope_unit: CA-SU-14
  tier: 3
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution
      Control
state:
  version: 1
  status: active
  updated_at: '2026-11-12T01:57:01.398751+00:00'
destination:
  file:
    name: CA-R-970308662-FRAMEWORK_ENGINE-REQUIREMENT--report-workflow-execution-outcomes-and-effects.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement
---
## Summary

Report Workflow execution outcomes and effects

## Claim

### Prose Claim

The Engine returns a structured outcome for each Workflow invocation. A successful Run reports saved and removed Object references and confirmed effects, where applicable. If an Action fails, report the failed Action, the reason, and any confirmed effects already applied. Include the Actions left unrun when the Workflow had already selected them. Distinguish uncertain effects from confirmed effects.

Reject invalid Workflow invocation inputs before any Action can apply effects. Identify each rejected field that needs correction. If a later Action rejects an input or source revision, report that Action failure with the effects already applied. The internal API and admitted MCP routes preserve these outcome details.
