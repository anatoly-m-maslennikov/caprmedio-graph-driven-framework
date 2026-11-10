---
identity:
  atom_id: CA-E-467
  ref_id: CA-E-467
context:
  container:
    scope_unit: CA-SU-15
  role: evaluation
  form: eval_case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Storage <+ Directory Layout
    dependencies: []
  tier: 4
relations:
  evaluation_for:
  - CA-M-422
state:
  status: Active
  version: 17
  updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a0263a-7510-7672-bce4-58830bc4d184
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-467-PROGRAMMATIC-EVAL_CASE--reject-temporary-state-outside-project-temp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Reject temporary state outside project temp

## Claim

### Prose Claim

#### Claim checked

**every** CAPRMEDIO-controlled PROGRAMMATIC execution **must** confine temporary Carriers created by its components **and** configured dependencies **to** the Project Temporary State root.

#### Test case

1. set the working directory **and** ambient host temporary location outside the configured Project Temporary State root.
2. run representative Tool, App backend, **and** MCP fixtures, including their test runner **and** a configured dependency. exercise bytecode creation, caches, temporary workspaces, atomic staging, **and** interrupted **or** denied cleanup.
3. compare the path frontier outside the Temporary State root **before** **and** **after** execution. inspect the applicable source **and** configuration for unredirected temporary-path creation.
4. delete **only** the Temporary State root **in** an isolated fixture **and** compare its protected authority **and** runtime state.
5. make the Temporary State root unavailable **or** make the selected staging
   path fail the same-filesystem precondition **in** an isolated fixture.
   inspect the affected effect **and** its boundary diagnostic.

#### Acceptance criteria

**all** of the following **must** hold:

- **every** temporary, scratch, staging, cache, build, Evaluation, **and** cleanup-remnant Carrier is below the configured Project Temporary State root.
- concurrent owners use their declared component **or** run-specific descendants.
- no applicable source **or** configuration uses an ambient **or** hard-coded host temporary fallback.
- deletion of the Temporary State root leaves governed authority, Project Journal history, selected runtime releases, logs, sessions, databases, service state, **and** resumable state unchanged.
- no Python bytecode cache remains below the Runtime State root.
- an unavailable temporary root **or** unsatisfied same-filesystem precondition
  stops the affected effect **and** produces a stable diagnostic identifying
  the creating owner **and** violating path.

#### Failure disposition

reject the changed component, test workflow, dependency configuration, **or** release **until** **every** observed **and** statically detectable temporary Carrier uses the Project Temporary State root. report **every** violating path **and** its creating owner.
