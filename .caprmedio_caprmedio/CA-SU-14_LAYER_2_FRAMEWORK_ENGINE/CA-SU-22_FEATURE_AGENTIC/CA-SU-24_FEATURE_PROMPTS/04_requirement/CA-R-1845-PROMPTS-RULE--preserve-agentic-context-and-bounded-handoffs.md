---
atom_id: CA-R-1845
ref_id: CA-R-1845
container:
  scope_unit: CA-SU-24
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic Step Execution Context
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
tier: 3
status: Active
version: 14
updated_at: 2026-10-27 20:00:04 +0400
carrier_destination:
  file:
    name: CA-R-1845-PROMPTS-RULE--preserve-agentic-context-and-bounded-handoffs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/04_requirement
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---
# Summary

Preserve agentic context and bounded handoffs

## Scope

explicit per-Step Agentic context for the declared Implementation Workflow graph, including its eight Integrated shared-context Steps; separately admitted Isolated invocations retain their own bindings.

## Claim

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
