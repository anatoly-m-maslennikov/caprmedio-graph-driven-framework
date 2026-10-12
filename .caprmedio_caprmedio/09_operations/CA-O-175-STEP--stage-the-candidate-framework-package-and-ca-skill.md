---
atom_id: CA-O-175
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: stage candidate package and Skill"
  depends_on: [Workflow, Step, Action, Framework Package, Methodology, Skill, Delivery, Journal]
version: 4
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-167]
---
# Summary

Stage the candidate Framework package and ca Skill

## Step

This Step invokes CA-O-167 once with phase `stage_candidate`, binding CA-O-165's frozen active boundary to one private active-source copy, compiled package, runtime, and complete `ca` payload before CA-O-185's complete suite.

## Details

It stages the complete candidate package and complete `ca` directory without selecting a runtime or replacing a Project Skill. A target mismatch, incomplete Methodology or Skill directory, hook, partial staging, permission failure, or missing Journal receipt stops before image build or testing.
