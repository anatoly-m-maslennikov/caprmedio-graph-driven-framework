---
atom_id: CA-P-2672
ref_id: CA-P-2672
container:
  atom: CA-P-2665
role: Plan
form: Plan
label: Task
topics:
  main_subject: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
tier: 4
status: Done
version: 3
updated_at: 2026-10-27 06:19:16 +0400
carrier_destination:
  file:
    name: 7-CA-P-2672-TASK--draft-release-workflow-model-in-project-configuration.md
    path: .caprmedio_caprmedio/03_plan/done/CA-P-2665-EPIC--refine-engineering-subject-branch/done
work_sequence_number: 7
current_scope_unit: caprmedio
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
---
# Summary

Draft release workflow model in Project Configuration

## Objective

Prepare generic Release and Release.ID definitions in CORE_META_MODEL, and Local Release / Public Release Workflow Subjects with their concrete definitions and workflow-specific RMED in PROJECT_CONFIGURATION.

## Details

Version identifies Release; it is not the Product's Version property. Local and public release are Workflow instances, not Release Types. Keep actual release result/identity Subjects distinct from Workflow rules and Engine implementation topics. Reuse the existing Workflow definitions by stable Atom ID; preserve their Summaries and behavior. Update their defining names and all directly bound Subject references in Drafts. Review positive Step/Action containment and invocation closure for coherent ownership; do not move negative or merely historical references. Prepare moves as Drafts only. Broader Engine reorganization and operational content rewrite remain excluded.

## Definition of Done

- Release and Release.ID have reviewed defining R Drafts in CORE_META_MODEL; Version is the ID's name, without a duplicated property.
- Two canonical Workflow names bind to the real Local/Public definitions; all affected Subject references and bounded closure are accounted for.
- Workflow-specific Drafts are physically in PROJECT_CONFIGURATION and declare that owner; generic Engine implementation policies remain separate.
- No Current source move, Source Summary change, new operational behavior or code change is claimed by preparation.

## Completion

Completed in Candidate #9: reviewed Drafts were promoted with predecessor archives; the four Current-source Subject views were rebuilt and checked. See the parent Epic for the applied counts and retained exclusions.
