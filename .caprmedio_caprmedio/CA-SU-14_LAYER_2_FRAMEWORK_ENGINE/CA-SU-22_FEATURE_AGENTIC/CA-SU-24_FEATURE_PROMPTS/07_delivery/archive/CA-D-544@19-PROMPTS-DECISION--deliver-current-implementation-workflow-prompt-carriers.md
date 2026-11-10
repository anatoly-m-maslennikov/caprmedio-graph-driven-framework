---
atom_id: CA-D-544
ref_id: CA-D-544@19
container:
  scope_unit: CA-SU-24
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Prompt
    Authoring
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
tier: 4
status: Archived
version: 19
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-D-544@19-PROMPTS-DECISION--deliver-current-implementation-workflow-prompt-carriers.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/07_delivery/archive
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
relations:
  depends_on:
  - CA-D-545
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
