---
identity:
  atom_id: CA-M-draft
context:
  container:
    scope_unit: CA-SU-14
  role: Method
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
  tier: 0
state:
  status: Draft
  version: 1
  updated_at: 2026-11-11 04:14:10 +0400
destination:
  file:
    name: CA-M-draft-FRAMEWORK_ENGINE-SOLUTION--continue-interactive-workflows-in-the-calling-session.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method/000_draft/cfel-native-workflow-architecture
author: Anatoly Maslennikov
---

## Summary

Continue interactive Workflows in the calling session

## Claim

### Prose Claim

Execute prompt-backed and input-requesting Actions through the calling session. Return the current Action's prompt, bound inputs and expected structured output to that session; wait for its result, validate the submitted output, complete that Action, and let the Workflow Engine select the next Step.

## Semantics

The in-session Agent may perform the work itself, use a subagent, or request an Operator decision under the applicable policy and confidence settings. The engine owns formal routing and data bindings; it does not interpret the Agent's prose as proof of a completed Step or move control to a separate autonomous Agent service.

Return a waiting state with Run/Step/interaction identity and required output contract. Carry the trusted Project and captured definition binding through the next MCP call. Store execution position and the correlation needed to accept the result once; a stale, cross-Project or terminal interaction cannot advance a Run. Public continuation operations are exposed Workflows too; their Actions call the engine's internal continuation API rather than bypassing the exposure architecture.

Missing or invalid supplied formats/allowed values return a short explanation and a requested-input dictionary. The session supplies corrected data at the declared waiting boundary. This is normal interaction, not automatic failure recovery or replay of completed effects. Cancel is allowed while waiting; it does not interrupt a running Action or undo prior effects.

A prompt being returned is not completion. The Run remains waiting until the output contract is satisfied or it ends with an explicit failure/cancellation. Do not preload the full methodology or future Step prompts when the current Action needs only its bound context. Keep business-event observations separate from technical logs and from authorization.
