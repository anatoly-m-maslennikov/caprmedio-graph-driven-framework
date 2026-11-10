---
atom_id: CA-M-321@15
ref_id: CA-M-321@15
container:
  scope_unit: CA-SU-2
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
    Structure
tier: 3
status: Archived
version: 15
updated_at: 2026-10-27 19:59:42 +0400
carrier_destination:
  file:
    name: CA-M-321@15-WORKFLOW_ORCHESTRATOR-ENG_DECISION--execute-actions-through-a-replaceable-codex-adapter.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/05_method/archive
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
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
