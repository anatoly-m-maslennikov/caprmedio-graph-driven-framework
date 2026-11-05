---
atom_id: CA-O-167
ref_id: CA-O-167
role: Operations
form: Action
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/UX/CAPRMEDIO Skill and MCP Entry Interface
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 18
updated_at: 2026-11-02 19:46:47 +0400
tier: 3
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-O-167-CAPRMEDIO-ACTION--stage-candidate-runtime-package-and-skill.md
    path: .caprmedio_caprmedio/09_operations
---
# Summary

Stage candidate runtime package and Skill

## Action

Stage candidate runtime package and Skill **means** the Action that prepares the one private `stage_candidate` package, runtime, and Skill payload from the frozen active source boundary without selecting it as the active runtime or project Skill.

## Scope

`stage_candidate` prepares the complete declared Framework package only under `.caprmedio_tmp/release_candidates/<run_id>/package/`, including the private active-source copy, compiled Methodology, Engine, complete `ca` Skill/default payload, dependency-lock identity, runtime input, and matching image context. It stages the `ca` payload for its Project target without replacing an active Skill or writing `LAYER_1_FRAMEWORK_METHODOLOGY/` or the installed Framework.

## Details

The phase requires CA-O-165's exact boundary and records the package digests used by CA-O-176, CA-O-185, and CA-O-169. A missing member, unbound target, incomplete Skill directory, digest mismatch, hook, partial staging, unavailable permission, or failed postcondition stops before image build, tests, or installation. This Action does not select a runtime or Skill, alter settings, register MCP, install, publish, or retry. Every actual invocation is journaled once.
