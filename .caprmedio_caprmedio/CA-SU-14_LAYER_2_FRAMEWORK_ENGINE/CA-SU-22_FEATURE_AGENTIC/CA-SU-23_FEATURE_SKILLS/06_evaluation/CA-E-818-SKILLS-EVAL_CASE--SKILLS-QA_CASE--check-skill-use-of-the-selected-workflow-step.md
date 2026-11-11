---
identity:
  atom_id: CA-E-818
  ref_id: CA-E-818
context:
  container:
    scope_unit: CA-SU-23
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction
    dependencies:
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Action
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Entry
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role in RMED)
    - MODEL//CAPRMEDIO <+ Actor/Operator
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Step
    - MODEL//CAPRMEDIO <+ Execution/Step Run
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
      <+ Communication <+ API
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Workflow
  tier: 4
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-818-SKILLS-EVAL_CASE--SKILLS-QA_CASE--check-skill-use-of-the-selected-workflow-step.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-23_FEATURE_SKILLS/06_evaluation
author: Anatoly Maslennikov
relations:
  evaluation_for:
  - CA-R-1626
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
---
## Summary
Check Skill use of the selected Workflow Step

## Claim

### Prose Claim

the Skill-participation Evaluation **must** check that the Skill uses the admitted framework response for the current Step rather than independently choosing a Workflow procedure **or** capability sequence.

#### Fixture and evidence

- fix the Operator request, owning Project, active authority references, routing inputs, admitted Workflow **and** Step, Action inputs, permissions, **and** required result. expose necessary capabilities **and** distinguishable irrelevant alternatives.
- identify the sufficient capability set **or** admitted equivalent alternatives for this bounded fixture. justify it from the Action **and** its bindings; do **not** assert a globally optimal minimum.
- capture the submitted request, framework response, instructions used, capability calls, reported results, **and** **any** continuation request.

#### Acceptance

- the Skill submits the request through the declared framework interface **and** uses the returned current-Step binding; it does **not** maintain another routing dictionary **or** silently substitute another Action.
- capability calls remain necessary for the admitted Action, within authorization, **and** compatible with its required outcome. an irrelevant capability, omitted input, invented source, **or** contradictory instruction yields failure.
- the Skill returns the actual result against its invocation. the executor selects the next Step; the Skill does **not** continue through a remembered **or** locally authored sequence.
- repeating the fixture with a changed admitted Action prompt but the same wrapper interface uses the new bound instructions **without** editing the Skill body. receiving a prompt alone is **not** completion.
- missing evidence **or** an unresolved fixture expectation yields an unresolved result, **not** a successful selection claim.
