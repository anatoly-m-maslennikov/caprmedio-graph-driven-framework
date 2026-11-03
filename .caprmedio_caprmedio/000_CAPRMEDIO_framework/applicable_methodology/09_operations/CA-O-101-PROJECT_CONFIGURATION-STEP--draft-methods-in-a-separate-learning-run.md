---
atom_id: CA-O-101
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/caprmedio/Step//Method Lesson Drafting Step
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic Step Execution Context
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
version: 14
updated_at: 2026-10-27 19:59:45 +0400
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-102-PROJECT_CONFIGURATION-WORKFLOW--learn-methods-from-verified-implementation-issues/CA-O-101-PROJECT_CONFIGURATION-STEP--draft-methods-in-a-separate-learning-run.md
  source_atom_id: CA-O-101
  source_atom_revision: 14
  source_sha256: 4968eb5badafa2579b77563601cfeb4fd99ae9fe00c3865f5c349e77f8534911
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Draft Methods in a separate learning run

## Operation

Method Lesson Drafting Step **means** the node invoking **=1** Action, CA-O-100, **in** Isolated context.

- bind inputs from the separately admitted Method-learning request, selected Plan, retained implementation issue/test/fix evidence, current authority, existing Method Drafts, **and** permissions.
- use a native subagent with the complete bounded handoff; MCP is **not** required. missing capability **or** context blocks the Step rather than silently changing execution context.
- retain exact Action/Step Revisions **and** actual returned evidence; pass `drafted`, `already_covered`, **or** `blocked` **to** the Workflow **without** duplicating Action behavior.

## Details
