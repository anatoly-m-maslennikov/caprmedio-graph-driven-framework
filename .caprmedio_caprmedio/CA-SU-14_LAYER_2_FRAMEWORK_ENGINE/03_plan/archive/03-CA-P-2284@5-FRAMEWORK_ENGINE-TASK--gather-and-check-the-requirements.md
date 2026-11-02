---
atom_id: CA-P-2284@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Workflow
  depends_on:
  - Requirement
  - Method
  - Evaluation
  - Delivery
  - Subject/Engineering/Tool
  - Subject/Domain/Node/Continuant/Projection
  - Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
version: 5
updated_at: 2026-10-24 08:10:13 +0400
relations:
  is_decomposition_of:
  - CA-P-2281
  blocks:
  - CA-P-2285
  - CA-P-2286
  - CA-P-2287
  - CA-P-2288
tier: 3
---
# Summary

Gather and check the Requirements

## Objective

Provide a Step that gathers all active Requirements selected for implementation and reports their conflicts and gaps.

## Details

Accept the target Scope Unit or explicit Atom list, descendant selection and implementation boundary. Resolve the declared tree through the verified Scope Unit Query/Read producer, never infer it from folders. Supply explicit selected/ancestor unit frontiers to Atom Query and full-Read the candidates. For unit-based selection, compute Targeting Atoms by resolved Claim Target Scope Unit, including parent-owned Goals/Demands; union descendant Targeting sets when requested. Keep applicable ancestor constraints separate from target Rs and deduplicate identities. Do not treat a current_scope_unit ownership filter as complete targeting selection. Unsupported matching/filter shapes or incomplete frontier coverage are reported and block preparation rather than widen the query silently. Supply Active and Requirement filters explicitly; the connector does not invent selection defaults. Read each selected Atom's full relevant properties and Markdown. Separate target Rs from applicable ancestor constraints. Save a complete R projection with readable original-source references and Versions, selected IDs and exclusions. Check contradictions, unclear expected outcomes and missing inputs needed to implement them. Report exact affected sources and missing information; do not silently change their authority.

Execute this Task in its own subagent. Preserve unrelated work; the integration owner controls shared files and Git. Split only genuinely oversized own-work into smaller P Tasks before execution. This Task grants no live operation outside the selected implementation scope.

## Definition of Done

Fixtures prove complete selected-R coverage, explicit scope/status filtering and truthful missing, ambiguous and conflicting Requirement reports. Include a parent-owned Goal/Demand targeting the selected child, descendant inclusion/exclusion, and a missing Scope Unit Query/Read binding. No case may pass through ownership-only selection or directory-derived membership.

