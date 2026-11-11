---
atom_id: CA-O-draft
content_role: Operations
type: Step
current_scope_unit: caprmedio
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/caprmedio/Step//Release Version/Step: stage candidate package and Skill'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Methodology Sources
  - Subject/CAPRMEDIO/Graph/Node/Aspect/UX/CAPRMEDIO Skill and MCP Entry Interface
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-167
tier: 3
---
## Summary

Stage a candidate Framework package and ca Skill before testing

## Step

This Step invokes CA-O-167 once with phase `stage_candidate`, binding CA-O-165's frozen active boundary to one private active-source copy, compiled package, runtime, and complete `ca` payload before CA-O-185's complete suite.

## Details

It stages the complete candidate package and complete `ca` directory without selecting a runtime or replacing a Project Skill. A target mismatch, incomplete Methodology or Skill directory, hook, partial staging, permission failure, or missing Journal receipt stops before image build or testing.
