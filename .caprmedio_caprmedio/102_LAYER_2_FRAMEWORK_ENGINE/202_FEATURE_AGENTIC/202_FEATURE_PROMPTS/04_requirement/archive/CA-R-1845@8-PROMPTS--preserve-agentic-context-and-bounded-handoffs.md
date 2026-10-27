---
atom_id: CA-R-1845@8
content_role: Requirement
type: Rule
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 06:47:02 +0400
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution/Step Run.Agentic Step Execution Context
  depends_on:
  - Subject/Engineering/Prompt
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Agent
relations:
  relates_to:
  - CA-O-231
  - CA-O-232
  - CA-O-233
  - CA-O-094
  - CA-O-234
  - CA-O-096
  - CA-O-099
tier: 3
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
