---
atom_id: CA-O-224
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
version: 13
updated_at: 2026-10-29 22:26:57 +0400
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-224-PROJECT_CONFIGURATION-ACTION--bind-the-exact-code-candidate-and-bounded-review-context.md
  source_atom_id: CA-O-224
  source_atom_revision: 13
  source_sha256: 0092aeae0759acc91cc7db85dd0d67eb4d981dafd05b0095d60dbfa920e41855
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Bind the exact code candidate and bounded review context

## Operation

Code Candidate Review Binding means the read-only Action that freezes the review boundary before checks run. Required initiative input is either an existing bounded Plan or an actually admitted in-session P/task with instruction, Definition of Done, and source context. Required review inputs also include candidate digest, owned paths, direct full `requirements`, `methods`, `evaluations`, and `delivery` rows, Project-owned Tier 0 Atoms, permissions, allowed commands, context authority, report destination, Run identity, source revisions/hashes, and prior evidence. An optional legacy `method_projection` may accompany direct rows but is not required.

Return `bound` only when the selected Plan or in-session P/task is real, complete, current, and sufficient for downstream CA-O-020/CA-O-089. Return `blocked` when it is absent, stale, ambiguous, or missing required content. Never invent a Plan Atom ID, create a Plan artifact, substitute a target, widen permissions, or use a remembered projection.

## Details

This Action inspects only the candidate and boundary metadata. It does not execute checks, edit code, change expectations or Atoms, write a Journal event, publish MCP, or choose a hidden next Step.
