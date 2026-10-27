---
atom_id: CA-P-1851@7
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 08:53:04 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Framework Instance Settings
  - Subject/Domain/Node/Continuant/Scope Unit
  - Applicable Methodology
  - Project Structure
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Engineering/Carrier
relations:
  is_decomposition_of:
  - CA-P-1848
  blocks:
  - CA-P-1852
tier: 3
---
# Summary

Consolidate Methodology source **and** delivery paths

## Objective

Use the declared source, product and installed Methodology folders without compatibility migration.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

- Completion evidence: project_structure.toml declares the authoring sources below the Project methodology unit. Live source export, product compilation and installed copy used those paths without compatibility migration.
- Live Local receipt: .caprmedio_runtime/simple_local_release/reports/epic1848-direct-local-20261012-001.md. Consolidated verification: .caprmedio_tmp/epic1848/direct-local-completion.md.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
