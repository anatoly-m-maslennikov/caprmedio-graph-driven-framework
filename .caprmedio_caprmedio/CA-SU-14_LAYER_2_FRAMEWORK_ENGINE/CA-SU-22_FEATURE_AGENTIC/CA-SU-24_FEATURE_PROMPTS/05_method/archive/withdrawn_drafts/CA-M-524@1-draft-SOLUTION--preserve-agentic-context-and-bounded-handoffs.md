---
identity:
  atom_id: CA-M-524
  ref_id: CA-M-524@1-draft
context:
  container:
    scope_unit: CA-SU-24
  role: method
  form: solution
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic
      Step Execution Context
    dependencies:
    - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control
      <+ Effect Authorization
    - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
    - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Action
    - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  tier: 3
state:
  status: draft
  version: 1
  updated_at: 2026-11-10 11:53:32 +0400
destination:
  file:
    name: CA-M-524@1-draft-SOLUTION--preserve-agentic-context-and-bounded-handoffs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/05_method/draft
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-1845
---
## Summary

Preserve agentic context and bounded handoffs

## Claim scope

explicit per-Step Agentic context for the declared Implementation Workflow graph, including its eight Integrated shared-context Steps; separately admitted Isolated invocations retain their own bindings.

## Claim

### Prose Claim

the Implementation **must** use the Step's supplied Integrated or Isolated context before actual Agentic dispatch; Isolated work uses an assigned subagent with a complete handoff, a fresh admission, and one bounded P subtask estimated below fifteen minutes.

## Details

Unavailable, ambiguous, unsupported, or incomplete context blocks dispatch. A prompt returns its result and retained evidence to its caller; it neither auto-starts a successor nor grants permissions, changes Workflow state, or silently falls back between contexts.

For Integrated implementation, the MCP interface exposes only the current
admitted Step's prompt, complete bound inputs, expected result contract, and
continuation identity. The controlling session executes or delegates that work
within its permissions, then submits the actual result to the same Workflow
interface. The executor alone validates the submission and selects the next
Step. Returning a prompt leaves the Step pending, not completed; delegation does
not silently change the Step's declared context. Preserve the Plan, direct RMED
sources, actual partial results, candidate-bound review/check evidence, and
remaining retry state. Repeated identical submissions are idempotent; conflicting,
stale, or mismatched continuations are refused without replaying effects.
