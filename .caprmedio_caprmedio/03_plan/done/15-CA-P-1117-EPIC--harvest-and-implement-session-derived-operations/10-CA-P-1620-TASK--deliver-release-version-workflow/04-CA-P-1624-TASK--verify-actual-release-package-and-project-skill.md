---
atom_id: CA-P-1624
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: Subject/Graph Node/Engineering/Release
  depends_on:
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Engineering/Continuant/Tool
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Engineering/CAPRMEDIO Main Skill
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 10
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1620
  blocks:
  - CA-P-1123
  - CA-P-1124
tier: 3
---
# Summary

Verify actual release package and project Skill

## Objective

Within <=15 minutes per bounded verification slice, prove the complete Release Version path against actual installed outputs and the actual newly built image.

## Details

Inputs: independently accepted source/implementation, exact frozen Version/source/package/image hashes and declared test environment. Verify full source copy, compilation source traceability, complete package in .caprmedio_runtime, runtime Methodology in .caprmedio_caprmedio/000_CAPRMEDIO_framework, project-local ca Skill without hooks, declared full test suite, installed-engine/MCP smoke/E2E and actual new-image execution. Prove old-image deletion is exact, only after success and only when no container/required rollback reference retains it. Inject bounded failure cases to prove prior good installation/history/settings/Journal preservation and truthful outcomes. C449/C447 remain explicit blockers where applicable; no fallback runner or denied-operation bypass.

## Definition of Done

Save actual package/install/Skill/image/test/Run evidence and independent closure verdict for every explicit requirement. Unexecuted, skipped, mocked or indirect gates remain incomplete. P1620 and the Epic stay Active until their complete required scope is proven.
