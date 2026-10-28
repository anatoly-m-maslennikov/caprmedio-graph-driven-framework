---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/Verification/Dynamic Testing
  depends_on: []
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-M-203
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-321@18
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
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
