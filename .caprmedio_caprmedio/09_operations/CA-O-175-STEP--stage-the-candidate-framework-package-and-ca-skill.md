---
atom_id: CA-O-175
content_role: Operations
type: Step
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step//Release Version/Step: stage candidate package and Skill'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Framework Package
  - Subject/Engineering/Methodology
  - Skill
  - Delivery
  - Subject/Domain/Node/Continuant/History/Journal
version: 7
updated_at: 2026-10-24 00:51:05 +0400
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-167
tier: 3
---
# Summary

Stage the candidate Framework package and ca Skill

## Step

This Step invokes CA-O-167 once with phase `stage_candidate`, binding CA-O-165's frozen active boundary to one private active-source copy, compiled package, runtime, and complete `ca` payload before CA-O-185's complete suite.

## Details

It stages the complete candidate package and complete `ca` directory without selecting a runtime or replacing a Project Skill. A target mismatch, incomplete Methodology or Skill directory, hook, partial staging, permission failure, or missing Journal receipt stops before image build or testing.
