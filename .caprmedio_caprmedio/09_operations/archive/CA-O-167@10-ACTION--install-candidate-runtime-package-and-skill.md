---
atom_id: CA-O-167@10
content_role: Operations
type: Action
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Engineering/Methodology
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Framework Package
  - 'Subject/Domain/Node/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Engineering/CAPRMEDIO Main Skill
  - Artifact/Revision
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Subject/Domain/Node/Continuant/History/Journal
version: 10
updated_at: 2026-10-24 10:08:20 +0400
relations:
  relates_to:
  - CA-O-164
  - CA-O-175
  - CA-R-1525
  - CA-R-1720
tier: 3
---
# Summary

Stage candidate runtime package and Skill

## Action

Stage candidate runtime package and Skill **means** the Action that prepares the one private `stage_candidate` package, runtime, and Skill payload from the frozen active source boundary without selecting it as the active runtime or project Skill.

## Scope

`stage_candidate` prepares the complete declared Framework package only under `.caprmedio_tmp/release_candidates/<run_id>/package/`, including the private active-source copy, compiled Methodology, Engine, complete `ca` Skill/default payload, dependency-lock identity, runtime input, and matching image context. It stages the `ca` payload for its Project target without replacing an active Skill or writing `101_FRAMEWORK_METHODOLOGY/` or the installed Framework.

## Details

The phase requires CA-O-165's exact boundary and records the package digests used by CA-O-176, CA-O-185, and CA-O-169. A missing member, unbound target, incomplete Skill directory, digest mismatch, hook, partial staging, unavailable permission, or failed postcondition stops before image build, tests, or installation. This Action does not select a runtime or Skill, alter settings, register MCP, install, publish, or retry. Every actual invocation is journaled once.
