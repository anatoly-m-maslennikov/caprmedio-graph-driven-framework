---
cce_version: cce_1
cce_form: method
subjects:
  governs: Subject/Engineering/Tool.Source Architecture
  depends_on: []
version: 14
updated_at: 2026-10-24 01:28:26 +0400
relations:
  method_for:
  - CA-R-1124
  derived_from:
  - CA-A-058
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-203@14
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eng Policy
---
# Bind one deterministic script to one Tool

## Applicable when

use this Method **when** admitting **or** reviewing an independently executable deterministic script, including one invoked exclusively by a Skill.

## Procedure

1. select the active Tool Scope Units **and** independently executable deterministic entry scripts within one declared frontier.
2. resolve **every** script's declared Tool identity **and** **every** Tool's canonical entrypoint from their owning authority carriers; include entrypoints invoked **only** through a Skill.
3. compare the two sets **and** require one exact Tool-to-entrypoint binding **in** **every** direction.
4. classify imported modules, workers, **and** shared libraries that are **not** independently executable as implementation support, even **when** several Tools call them.
5. report **every** missing, duplicate, cross-boundary, **or** orphan binding with the Tool identity **and** both relevant paths.

## Outcome

**every** independently executable deterministic script has **=1** Tool owner, **and** **every** Tool has **=1** canonical executable entrypoint.

## Failure or stop

do **not** infer ownership from directory proximity, import topology, **or** invocation by a Skill; treat ambiguous **or** multi-owner bindings as blocking findings.
