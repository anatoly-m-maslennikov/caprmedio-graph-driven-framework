---
atom_id: CA-E-564@13
ref_id: CA-E-564@13
container:
  scope_unit: CA-SU-24
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Prompt
    Authoring
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Validation
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
tier: 3
status: Archived
version: 13
updated_at: 2026-10-27 19:59:37 +0400
carrier_destination:
  file:
    name: CA-E-564@13-PROMPTS-EVAL_CASE--verify-implementation-prompt-source-currentness.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/06_evaluation/archive
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---
# Summary

Verify implementation prompt source currentness

## Scope

the source-binding frontier for all seven Implementation Workflow prompts.

## Claim

the Implementation passes this Evaluation only when each required source identity, version, path, and digest matches current fully reviewed authority.

## Details

The stale delivered O016v9 and old Step/Action pins fail this case until an independent PROMPTS review has refreshed them; a digest edit alone is not a pass.

The Evaluation also fails when a packet resolves the reviewed source rows from
an immutable prompt-code root, ambient current directory, host-path guess, or
unbound mount rather than its `selected_project` binding. It fails when a
source reference is absolute, escapes `.caprmedio_caprmedio`, has a duplicate,
missing, stale, or mismatched identity/version/digest, or when the active-M
Projection is not verified against the same selected Project source frontier.
An Agent must not launch in those cases. If a packet declares executable work,
the Evaluation also requires the existing explicit `workspace` and the exact
matching `permissions.implementation_workspace` capability; their absence or
mismatch is blocked evidence, not a new permission or a successful mock run.
