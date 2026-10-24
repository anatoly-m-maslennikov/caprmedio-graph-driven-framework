---
atom_id: CA-M-321@8
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: Subject/Engineering/Agent Execution/Codex Adapter Dispatch
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/History/Journal
  - Implementation
  - Subject/Engineering/Agent Execution/Codex Adapter Dispatch
relations:
  relates_to:
  - CA-R-1522
  - CA-R-1523
  - CA-R-1524
  - CA-O-104
type: Eng Decision
tier: 3
---
# Summary

Execute Actions through a replaceable Codex adapter

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

implement Agentic execution through a replaceable Codex CLI adapter with structured output admission.

## Details

1. invoke codex exec with argument arrays, stdin prompts, a JSON output schema **and** an explicit isolated working directory. native execution uses a read-only CLI sandbox; the dedicated Docker Agent service uses its container boundary **without** Project mounts. use existing authentication through runtime credential admission, never through an image layer.
2. give the Agent the selected Atom, current rules, the Action prompt **and** phase report, with no other Atom reports.
3. require a structured report plus optional proposed replacement content. validate identity, source hashes, confidence **and** saved check evidence before admission.
4. retain reports **and** candidate content under the dispatch identity before applying changes.
5. bound subprocess duration **and** output reads. timeouts, invalid output **or** missing credentials block execution rather than inventing a pass.
6. keep the executor interface independent of Codex so other harnesses can be added later.
