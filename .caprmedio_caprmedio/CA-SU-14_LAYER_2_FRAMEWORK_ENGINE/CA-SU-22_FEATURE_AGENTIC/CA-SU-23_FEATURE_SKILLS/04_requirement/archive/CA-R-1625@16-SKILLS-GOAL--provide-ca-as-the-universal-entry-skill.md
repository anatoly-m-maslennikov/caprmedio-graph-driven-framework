---
atom_id: CA-R-1625@16
content_role: Requirement
current_scope_unit: SKILLS
claim_target_scope_unit: SKILLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/CAPRMEDIO Main Skill
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Skill
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
version: 16
updated_at: 2026-10-25 17:32:27 +0400
relations:
  child_of:
  - CAPRMEDIO-METHODOLOGY-REQU-508
  relates_to:
  - CA-R-1522
  - CA-R-1626
tier: 3
type: Goal
---
# Summary

Provide CA as the universal entry skill

## Scope

requests submitted by Operators and AI Agents through the CAPRMEDIO Main Skill `ca` for methodology-defined Workflow execution and MCP Step instructions and results.

## Claim

FRAMEWORK_ENGINE **must** provide `ca` as the primary Skill entry point through which Operators **and** AI Agents submit requests **to** methodology-defined Workflow execution **and** exchange current Step instructions **and** results through MCP.

the Skill remains within the thin-wrapper boundary of CA-R-1626-SKILLS-RULE--keep-ca-and-specialist-skills-thin; WORKFLOW_ORCHESTRATOR retains coordination under CA-R-1522-WORKFLOW_ORCHESTRATOR-RULE--provide-workflow-orchestration-from-methodology rather than transferring route selection **or** Step sequencing into the Skill.

## Details
