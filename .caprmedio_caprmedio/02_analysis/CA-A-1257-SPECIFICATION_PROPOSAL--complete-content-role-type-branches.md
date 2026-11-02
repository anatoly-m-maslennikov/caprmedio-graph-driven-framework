---
atom_id: CA-A-1257
content_role: Analysis
type: Specification Proposal
status: Active
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 21:13:38 +0400
relations: {}
tier: 3
---
# Summary

Complete Content Role Type branches

## Decision

Add Requirement Type Requirement; Analysis Types Analysis Report, Rationale and Spec Proposal; Concern Types Problem, Bug, Risk and Opportunity; Evaluation Types Eval Policy and Eval Case; and Method Types Eng Policy and Eng Decision to the primary proposal. Keep already included Requirement Definition, Demand and Project Goal branches. This addition is not a retirement decision for unlisted legacy Types.

Use the Operator's current proposed names Spec Proposal and Eval Policy in the prepared model. Existing Current source names Specification Proposal and Policy stay unchanged until adoption. No name alias registry is introduced.

Label is an Atom property. Epic, Task, Subtask and Version are Plan Label examples, not new Plan Types or primary entities. Labels do not change the general Plan containment rules. No closed Label whitelist is introduced by these examples.

## State

Primary-tree and source-definition preparation only. Current Type/Label properties are not migrated. Full Type-catalog reconciliation remains an Epic task; these additions do not claim it complete.
