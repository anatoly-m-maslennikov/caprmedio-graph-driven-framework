---
atom_id: CA-P-2364
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 6
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2318
tier: 3
---
# Summary

Verify local Draft demotion bundles

## Objective

Independently verify actual native nested Workflow/Step demotion to Draft retains local placement and the matching subtree under the final P2363 source/code pins.

## Details

Own a separate independent test and verification evidence only, not production code or author tests. Read the stable P2363 correction and current D467 v6, D466 v4, O128 v6, R1432 v11 and R1788 v3. Independently build source-authenticated Workflow/Step/sub-Step fixtures, capture original carrier/tree bytes and execute the existing admitted native demotion path. Verify immediate-container lowercase draft placement, exact resulting same-stem bundle location, unchanged descendant metadata/bytes/relative nesting and retained old history. Include denied/stale/collision or unadmitted-container refusal and relevant existing publication/bundle regressions without bypassing safeguards or replacing execution with a mocked writer.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Start final acceptance only after P2363's exact final code/test freeze; Root assigns exclusive independent-test ownership and owns Plans/Git. You are not alone; preserve author and unrelated edits. Draft promotion/identity, cascade orchestration, registry activation, general recovery redesign and live migration are outside this Task.

### Definition of Done

Independent actual positive/refusal checks pass on exact final source/code/test pins. Nested Draft Markdown remains inside its original authenticated local container, its matching subtree follows the resulting filename stem, and descendants/history/unrelated siblings retain exact bytes and unchanged ID/Version/Status/Updated At where their own carrier is not changed. No matching tree is left behind, no role-root flattening is reported as success, and existing authorization/currentness/collision/recovery guarantees remain intact. Report executed checks, final pins and limits to Root. This verifies only the demotion placement/bundle correction, not promotion identity, a completed cascade, registry/runtime readiness or live effects.
