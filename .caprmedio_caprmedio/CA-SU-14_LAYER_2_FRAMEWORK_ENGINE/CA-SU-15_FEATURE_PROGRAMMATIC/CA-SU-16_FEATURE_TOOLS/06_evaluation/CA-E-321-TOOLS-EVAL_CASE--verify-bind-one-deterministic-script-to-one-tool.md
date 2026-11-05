---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
version: 20
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-M-203
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-321
ref_id: CA-E-321
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
form: Eval Case
tier: 3
container:
  scope_unit: CA-SU-16
---
# Verify bind one deterministic script to one tool

## Claim checked

CA-M-203 establishes a one-to-one mapping between independently executable deterministic entry scripts **and** Tool owners, including a script invoked **only** by a Skill.

## Applicable when

apply whenever an independently executable script, Tool Scope Unit, Skill invocation, **or** canonical entrypoint declaration changes.

## Test case

consider one bounded declared frontier containing: a correctly bound script invoked **only** by a Skill, one Tool with two declared entrypoints, one orphan executable script, one Tool **without** an entrypoint, **and** two non-executable imported worker modules. resolve its bindings twice **without** changing the frontier.

## Acceptance criteria

the Skill-invoked entrypoint is accepted as the Tool's sole canonical script; duplicate, orphan, **and** missing bindings are distinct blocking findings; worker modules are **not** treated as Tools; **and** repeated resolution returns the same bindings **and** findings.

## Failure disposition

reject the binding Method **and** preserve the declared frontier, executable inventory, Skill invocation evidence, Tool declarations, support-module classification, bindings, findings, **and** repeated result.
