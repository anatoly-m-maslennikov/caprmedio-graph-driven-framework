---
atom_id: CA-P-2638@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-25 17:32:27 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2637
tier: 4
---
# Summary

Reshape Subject graph roots

## Objective

Apply the approved Graph Node, Graph Relation and Graph Rule structure to the
Current source Subjects, necessary taxonomy definitions and derived views.

## Details

### Approved runtime distinction — first-task update

The Operator resolved C603: Domain and Engineering both have Continuant and
Occurrent branches. Modeled Action/Step/Workflow Runs belong to Domain/Occurrent;
technical sessions and actual tool/app runtimes belong to Engineering/Occurrent.
Technical components and carriers use Engineering/Continuant. UX remains a
Graph Node branch for MCP interface and health-page appearance, not backend code.

This supersedes the earlier temporary deferral and extends only this first
structural task. It does not start the other Engine migration stages. Abstract
Engineering policy topics may stay directly under Engineering; do not invent
temporal classifications for them. Generic Node and Node.Type move to Graph
Node and Graph Node.Type, not to Domain-specific properties.

Graph Node contains Domain, Engineering, Documentation and Product. Domain
directly contains Continuant and Occurrent; remove its extra Node segment.
Keep specific Product names and all other suffixes. Resolve the existing UX
branch explicitly without guessing a new meaning. Preserve noncanonical
literals under their existing dispositions rather than inventing mappings.

This task starts with a prefix mapping and checked source inventory. Apply
normal Version increments and predecessor archives, then regenerate the
existing Core, project Methodology and Engine Subject projections with their
stable Projection IDs and actual source Versions. No other Engine task starts.

## Definition of Done

- The approved prefixes occur in the actual Current source Subjects.
- The required defining rules describe the new flat three-branch structure.
- All affected source updates and normal predecessor archives pass readback.
- The three Subject projections use actual updated sources, not a candidate.
- Existing Draft/Archive carriers, code, Scope Units and unrelated content
  remain unchanged; remaining Engine work stays in the parent Epic.
