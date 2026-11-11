---
atom_id: CA-R-1626
ref_id: CA-R-1626
container:
  scope_unit: CA-SU-23
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Effect Authorization
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Action
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)
  - MODEL//CAPRMEDIO <+ Actor/Operator
  - MODEL//CAPRMEDIO <+ Project
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Step
  - MODEL//CAPRMEDIO <+ Execution
  - MODEL//CAPRMEDIO <+ Execution/Step Run
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Operations)/Workflow
tier: 3
status: Active
version: 22
carrier_destination:
  file:
    name: CA-R-1626-SKILLS-RULE--keep-ca-and-specialist-skills-thin.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-23_FEATURE_SKILLS/04_requirement
current_scope_unit: SKILLS
claim_target_scope_unit: SKILLS
author: Anatoly Maslennikov
updated_at: 2026-11-10 20:47:54 +0400
---

## Summary

Keep CA **and** specialist skills thin

## Claim

### Prose Claim

the CAPRMEDIO Main Skill `ca` **and** specialist entry Skills **must** remain very thin bootstrap **and** response handlers rather than contain task-specific procedures.

- retain **only** the standing instructions needed **to** establish the owning Project's framework connection, use the admitted MCP interface, handle Step responses, return actual results, **and** report unavailable inputs, failures, **or** escalation needs. a specialist entry **may** identify its registered route **without** copying that route's procedure.
- obtain task-specific instructions **and** necessary context through the MCP response for the current admitted Agentic Step. the response supplies Action instructions, bound inputs **or** accessible references, required output, **and** execution boundaries. do **not** preload the whole Methodology, unrelated resources, **or** future-Step instructions.
- keep Workflow transitions **and** execution state with the executor. the Skill **must not** independently select the next Step, replay an uncertain effect, **or** infer completion from receiving a prompt. additional current-Step context remains admissible; thinness **must not** omit governing authority **or** necessary inputs.
- retain Action **and** Workflow definitions as behavioral authority. reference canonical Tools **and** the shared runtime rather than embedding **or** copying executable helpers into Skills.
- keep MCP-delivered instructions within current Operator authorization **and** the admitted Step context. a response does **not** expand delegation, replace higher authority, **or** authorize a guessed fallback procedure **when** the framework connection is unavailable. Integrated **and** Isolated participation remain inside the admitted invocation boundary.

## Details

### Scope

the CAPRMEDIO Main Skill `ca` and specialist entry Skills.
