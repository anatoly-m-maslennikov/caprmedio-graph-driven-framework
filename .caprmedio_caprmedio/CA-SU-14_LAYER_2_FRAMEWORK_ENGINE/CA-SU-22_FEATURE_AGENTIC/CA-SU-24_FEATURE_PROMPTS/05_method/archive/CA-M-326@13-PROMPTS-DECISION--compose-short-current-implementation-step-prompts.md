---
atom_id: CA-M-326
ref_id: CA-M-326@13
container:
  scope_unit: CA-SU-24
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Prompt
    Authoring
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Prompt Authoring
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
tier: 3
status: Archived
version: 13
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-M-326@13-PROMPTS-DECISION--compose-short-current-implementation-step-prompts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/05_method/archive
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---

## Summary

Compose short current implementation Step prompts

## Claim

### Prose Claim

**to** implement one Step prompt, state its exact Step, Action, and context; name required inputs, permitted work, output artifacts, admitted result labels, and blocking conditions without restating methodology authority.

## Details

### Scope

one self-contained prompt per current CA-O-016 Step.

Keep each prompt concise, pin-aware, and scoped to its own Step. Its named
inputs include the `selected_project` binding, current pinned source
references, the verified active-M Projection, and the existing workspace and
matching disposable-workspace capability when work may write. Resolve governed
sources only under that selected Project binding; do not infer a root from the
prompt package, current directory, a host path, or a mount. The caller owns
transitions and dispatch; a prompt does not route future Steps, infer a pass,
or grant a workspace, credential, or transport capability.
