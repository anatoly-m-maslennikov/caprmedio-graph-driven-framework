---
atom_id: CA-O-165
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/caprmedio/Action//Validate local release inputs
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Methodology Sources
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Release.ID
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
version: 21
updated_at: 2026-10-27 19:59:47 +0400
relations: {}
tier: 3
---
# Summary

Validate local release inputs

## Action

Validate local release inputs **means** the Action that checks the explicit local-release inputs and configured delivery paths for file/path safety before the declared local validation scope. The complete discovered suite remains the default; a focused scope requires the explicit current Operator record admitted by CA-O-164.

## Scope

The Action checks the configured source and delivery paths, Project Structure, protected settings, compiler, and target paths `101_FRAMEWORK_METHODOLOGY/` and `.caprmedio_caprmedio/000_CAPRMEDIO_framework/` for ordinary input and file/path safety. It does not separately validate Active Atom metadata, placement or relations; release verification uses the declared scope and records whether it is complete or focused.

## Details

Missing, ambiguous or unsafe required input stops before tests or delivery writes and is reported for manual handling. This Action does not copy or clear product or installed contents, compile, install, push, or open a PR.
