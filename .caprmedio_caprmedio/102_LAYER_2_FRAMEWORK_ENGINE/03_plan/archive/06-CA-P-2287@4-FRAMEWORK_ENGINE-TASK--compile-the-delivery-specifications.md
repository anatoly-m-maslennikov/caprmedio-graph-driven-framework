---
atom_id: CA-P-2287@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
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
  - Tool
  - Subject/Domain/Node/Continuant/Projection
  - Implementation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
version: 4
updated_at: 2026-10-24 06:12:43 +0400
relations:
  is_decomposition_of:
  - CA-P-2281
  blocks:
  - CA-P-2288
  - CA-P-2290
  - CA-P-2291
tier: 3
---
# Summary

Compile the Delivery specifications

## Objective

Provide a Step that compiles all applicable active Delivery specifications into one implementation projection.

## Details

Include the applicable carrier, location, format, interface, dependency and package boundaries for the selected target. Use the target's declared Implementation Folder and current Project Structure. Preserve original-source references and Versions. Report contradictions, ambiguous locations and required missing Delivery information. The projection agent must not invent a Delivery choice to hide a gap.

Use the new TOOLS workflow: run the admitted D625 `query` through CA-O-046 under CA-R-863 to return the applicable Delivery Atom IDs and matching facts; Query returns matches, not full content. Then invoke CA-O-047 under CA-R-864 with a D625 `read` for every selected ID. Preserve each Atom's full operative content, exact identity/Version, actual `current_state` and source evidence/attribution. Block compilation and report incomplete selected coverage if any selected Atom is missing, unreadable, malformed, truncated or otherwise incomplete; never compile partial data.

Resolve the target's declared `ImplementationFolder` with a CA-O-212 Scope Unit Read using an explicit full target declaration for `ImplementationFolder`, and preserve the returned complete Scope Unit declaration and actual source-state evidence. This read is sufficient for the implementation-folder boundary; do not require an unnecessary whole-configuration read or infer the folder from unrelated settings. Block delivery compilation if the declaration is missing, ambiguous, unreadable, truncated or incomplete.

Execute this Task in its own subagent. Preserve unrelated work; the integration owner controls shared files and Git. Split only genuinely oversized own-work into smaller P Tasks before execution. This Task grants no live operation outside the selected implementation scope.

## Definition of Done

The D projection preserves the selected applicable Delivery authority and identifies missing or contradictory implementation boundaries.

