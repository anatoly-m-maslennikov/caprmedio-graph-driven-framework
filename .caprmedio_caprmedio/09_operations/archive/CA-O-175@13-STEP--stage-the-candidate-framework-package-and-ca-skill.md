---
atom_id: CA-O-175@13
ref_id: CA-O-175@13
container:
  scope_unit: CA-SU-00
role: Operations
form: Step
topics:
  main_subject: 'Subject/caprmedio/Step//Release Version/Step: stage candidate package
    and Skill'
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Methodology Sources
  - Subject/CAPRMEDIO/Graph/Node/Aspect/UX/CAPRMEDIO Skill and MCP Entry Interface
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-167
status: Archived
version: 13
updated_at: 2026-10-27 19:59:47 +0400
carrier_destination:
  file:
    name: CA-O-175@13-STEP--stage-the-candidate-framework-package-and-ca-skill.md
    path: .caprmedio_caprmedio/09_operations/archive
current_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Stage the candidate Framework package and ca Skill

## Step

This Step invokes CA-O-167 once with phase `stage_candidate`, binding CA-O-165's frozen active boundary to one private active-source copy, compiled package, runtime, and complete `ca` payload before CA-O-185's complete suite.

## Details

It stages the complete candidate package and complete `ca` directory without selecting a runtime or replacing a Project Skill. A target mismatch, incomplete Methodology or Skill directory, hook, partial staging, permission failure, or missing Journal receipt stops before image build or testing.
