---
atom_id: CA-P-1623
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
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
  - Subject/Graph Node/Engineering/Skill
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 11
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-1620
  blocks:
  - CA-P-1624
tier: 3
---
# Summary

Implement Release Version from reviewed RMED

## Objective

Within <=15 minutes per bounded implementation slice, implement the independently accepted Release Version contract using existing components.

## Details

Own only the release capability implementation/tests and necessary additive discovery/MCP/orchestrator bindings. Begin with golden E2E tests and mocks for complete copy/compile/test/install/Skill/image flow and non-happy cases. Preserve current fifteen-route contracts unless reviewed source explicitly extends them. Bind full package Version/digests and enforce source/settings/Journal preservation, rollback and no old-image deletion before successful new installation/image verification. Do not provision around C449, retry C447, publish images, deploy or force-remove shared images. Decompose into <=15-minute slices before work exceeding the bound.

### Bounded decomposition

CA-P-1639 owns pure sealed contracts; CA-P-1640 owns the independent golden corpus; CA-P-1641 owns non-active complete package staging; CA-P-1642 binds the candidate compiler interface. These independent leaves can run in parallel with separate file ownership. All four block CA-P-1643 integration and additive admission; CA-P-1644 independently reviews resulting evidence. Parent remains Active until its full requested implementation is complete. Split any leaf exceeding15 minutes; no source, pure model, mock, development worker or build substitutes for P1624 actual image gates.

## Definition of Done

Reviewed source is implemented with focused passing golden tests, source-current bindings, truthful shared Run outputs and exact implementation diff. Mock/development proof is labeled separately from actual install/Docker proof.
