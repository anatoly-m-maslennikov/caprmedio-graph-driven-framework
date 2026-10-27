---
atom_id: CA-P-2286
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow//Implementation Workflow'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Engineering/Implementation
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
version: 11
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2281
  blocks:
  - CA-P-2288
  - CA-P-2289
  - CA-P-2290
tier: 3
---
# Summary

Compile the Evaluation policies

## Objective

Provide a Step that compiles all applicable active Evaluation policies into one implementation projection.

## Details

Select applicable Evaluation policies governing how to create and assess tests, including scope, observable boundaries and evidence rules. Keep policies distinct from existing Standard test cases, which are retained as candidate reusable cases. Preserve their source references and Versions. Report conflicting, unclear or missing policy inputs. Reuse current PROGRAMMATIC CA-E-389 and CA-M-285: emphasize functional/public-boundary and integration checks, while retaining useful small semantic tests; do not invent a fixed unit-test quota or universal end-to-end mandate.

Use the new TOOLS workflow: run the admitted D625 `query` through CA-O-046 under CA-R-863 to return the applicable Evaluation Atom IDs and matching facts; Query returns matches, not full content. Then invoke CA-O-047 under CA-R-864 with a D625 `read` for every selected ID. Preserve each Atom's full operative content, exact identity/Version, actual `current_state` and source evidence/attribution. Block compilation and report incomplete selected coverage if any selected Atom is missing, unreadable, malformed, truncated or otherwise incomplete; never compile partial data.

Execute this Task in its own subagent. Preserve unrelated work; the integration owner controls shared files and Git. Split only genuinely oversized own-work into smaller P Tasks before execution. This Task grants no live operation outside the selected implementation scope.

## Definition of Done

Fixtures distinguish Evaluation policies from test cases, preserve applicable authority and expose policy conflicts and gaps.

