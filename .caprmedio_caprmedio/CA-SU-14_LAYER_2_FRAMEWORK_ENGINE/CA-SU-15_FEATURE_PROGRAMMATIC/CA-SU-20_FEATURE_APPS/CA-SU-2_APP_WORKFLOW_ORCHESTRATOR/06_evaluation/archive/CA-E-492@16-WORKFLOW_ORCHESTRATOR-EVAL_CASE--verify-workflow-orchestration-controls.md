---
atom_id: CA-E-492@16
ref_id: CA-E-492@16
container:
  scope_unit: CA-SU-2
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool//WORKFLOW_ORCHESTRATOR
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic Testing
tier: 5
relations:
  evaluation_for:
  - CA-R-1522
  - CA-R-1523
  - CA-M-302
status: Archived
version: 16
updated_at: 2026-11-09 07:45:15 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: WORKFLOW_ORCHESTRATOR
destination:
  file:
    name: CA-E-492@16-WORKFLOW_ORCHESTRATOR-EVAL_CASE--verify-workflow-orchestration-controls.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/06_evaluation/archive
---

## Summary

Verify Workflow orchestration controls

## Claim

### Prose Claim

Verify observable Workflow coordination and client control against the applicable RMED.



### Coordination acceptance cases

the Evaluation **must** check WORKFLOW_ORCHESTRATOR's observable conformance **and** client-control behavior against its RMED.

1. submit an admitted Workflow with a deliberately long-running Action; require an accepted-work identifier **before** Action completion.
2. disconnect the submitting client, reconnect using that identifier, **and** inspect progress **and** the final result **without** creating another Run.
3. exercise an admitted Operator-input wait **and** cancellation request; require responsive controls **and** a distinction between requested cancellation **and** confirmed termination.
4. provide valid methodology fixtures with different declared continuation mappings; require the application **to** follow the supplied definitions rather than a hard-coded Update-to-Replace branch.
5. submit a malformed definition rejected by the applicable methodology checks; require a visible definition-validation failure rather than invented execution behavior.
6. submit a valid definition with an unavailable required worker **or** capability, missing invocation input, **or** absent current permission; require a distinct execution-admission block while preserving the valid definition **and** its validation result.

7. execute an admitted mixed-context fixture: preserve the same reusable Action identity across Integrated **and** Isolated invocations, return the Integrated input **and** instruction through MCP, **and** dispatch Programmatic Steps **without** an Agent-context requirement.
8. reconnect **without** earlier session conversation: recover the pending invocation, exact Run identities, relevant results, next instruction, **and** return route from executor state; do **not** replay an already performed effect merely **to** reconstruct context.
9. when AI-Agent execution is separately admitted, let an Agentic Step make several Tool calls: require nested canonical Journal evidence **without** invented Workflow nodes **or** a second execution-history authority.

fail on blocked coordination, lost accepted work, unauthorized effects, false completion, **or** independently authored Workflow policy. these are application tests; they consume methodology correctness authority rather than redefining it.

Agent-specific observations apply only to separately admitted AI-Agent execution; they do not enable its code or prove that runtime is present.
