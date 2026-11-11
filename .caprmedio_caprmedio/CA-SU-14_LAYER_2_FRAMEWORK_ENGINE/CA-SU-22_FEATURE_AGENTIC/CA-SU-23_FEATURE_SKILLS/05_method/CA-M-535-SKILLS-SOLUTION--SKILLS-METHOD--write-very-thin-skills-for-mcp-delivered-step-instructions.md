---
identity:
  atom_id: CA-M-535
  ref_id: CA-M-535
context:
  container:
    scope_unit: CA-SU-23
  role: Method
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Authoring <+ Prompt Authoring
    dependencies:
    - MODEL//CAPRMEDIO <+ Actor/AI Agent
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Action
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Entry
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role in RMED)
    - MODEL//CAPRMEDIO <+ Actor/Operator
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Step
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
    name: CA-M-535-SKILLS-SOLUTION--SKILLS-METHOD--write-very-thin-skills-for-mcp-delivered-step-instructions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-23_FEATURE_SKILLS/05_method
author: Anatoly Maslennikov
relations:
  method_for:
  - CA-R-1626
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
---
## Summary
Write very thin Skills for MCP-delivered Step instructions

## Claim

### Prose Claim

**to** author a very thin Skill under the thin-Skill boundary, separate stable bootstrap **and** response-handling instructions from the task-specific instructions supplied by the framework.

- use a short discovery description that identifies the entry purpose **and** its registered route **when** applicable; do **not** put a Workflow procedure **in** the description.
- keep the standing body limited **to** framework connection, the admitted request/result interface, **and** generic response, failure, missing-input, **and** escalation handling. explain how **to** consume the current invocation **without** embedding the decisions performed by its Action.
- reference the portable shared runtime and canonical PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ APIs, **not** scripts maintained inside the Skill.
- let the current MCP response supply the Action prompt **and** its Step bindings. retain accessible references for additional current-Step context rather than preloading the MODEL//CAPRMEDIO <+ Atom/(.Header.Role in RMED) **or** unrelated prompts.
- follow the existing delegation **and** Step-context rules. do **not** author another approval policy, routing tree, continuation table, **or** delegation procedure inside the Skill.

the result is a bounded Skill wrapper that remains valid **when** task-specific Action instructions change **without** changing the wrapper interface. **if** authoring reveals a missing interface, source, **or** authority binding, report that gap rather than hide it inside the Skill. this Method governs authoring; it does **not** define a new session Workflow **or** promote another Draft.
