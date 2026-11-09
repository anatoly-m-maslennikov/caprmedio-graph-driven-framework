---
atom_id: CA-R-1626
ref_id: CA-R-1626
container:
  scope_unit: CA-SU-23
role: Requirement
form: Rule
topics:
  {"main_subject": "Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Interaction", "dependencies": ["Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect Authorization", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action.Execution Kind", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)", "CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator", "CAPRMEDIO_MODEL <+ Project", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step", "CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution", "CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run.Invocation Context", "CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow"]}
tier: 3
relations:
  child_of:
  - CA-R-1124
  - CA-R-643
status: Active
version: 21
carrier_destination:
  file:
    name: CA-R-1626-SKILLS-RULE--keep-ca-and-specialist-skills-thin.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-23_FEATURE_SKILLS/04_requirement
current_scope_unit: SKILLS
claim_target_scope_unit: SKILLS
author: Anatoly Maslennikov
updated_at: 2026-11-09 19:30:15 +0400
---

## Summary

Keep CA **and** specialist skills thin

## Claim

### Prose Claim

the CAPRMEDIO Main Skill `ca` **and** specialist entry Skills **must** remain very thin bootstrap **and** response handlers rather than contain task-specific procedures.

- retain **only** the standing instructions needed **to** establish the owning Project's framework connection, use the admitted MCP interface, handle Step responses, return actual results, **and** report unavailable inputs, failures, **or** escalation needs. a specialist entry **may** identify its registered route **without** copying that route's procedure.
- obtain task-specific instructions **and** necessary context through MCP responses for the current admitted Agentic Step under CA-R-1605-WORKFLOW_ORCHESTRATOR-SCOPE_CONTRACT-RULE--coordinate-workflow-runs **and** `CA-R-1789-CORE_META_MODEL--provide-self-contained-agentic-step-invocation-payloads`. the response supplies the Action instructions, bound inputs **or** accessible references, required output, **and** execution boundaries. do **not** preload the whole Methodology, unrelated resources, **or** future-Step instructions merely **to** remember what comes next.
- keep Workflow transitions **and** execution state with the executor. the Skill **must not** independently select the next Step, replay an uncertain effect, **or** infer completion from receiving a prompt. additional context required by the current Step remains admissible; thinness **must not** omit governing authority **or** necessary inputs.
- retain methodology Action **and** Workflow definitions as behavioral authority. ACTION_PROMPTS implements the Action instructions under CA-R-1601-PROMPTS-GOAL--implement-actions-as-agent-instructions; the MCP response delivers the bound invocation, **not** another independently authored procedure. reference canonical Tools **and** the shared runtime rather than embedding **or** copying executable helpers into Skills.
- keep MCP-delivered instructions within current Operator authorization **and** the admitted Step context. a response does **not** expand delegation, replace higher authority, **or** authorize a guessed fallback procedure **when** the framework connection is unavailable. Integrated **and** Isolated participation retain CA-R-1527-CORE_META_MODEL-DEFINITION--define-agentic-step-execution-context's existing boundary.

## Details

### Scope

the CAPRMEDIO Main Skill `ca` and specialist entry Skills.
