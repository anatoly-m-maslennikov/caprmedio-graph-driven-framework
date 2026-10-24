---
atom_id: CA-O-165@11
content_role: Operations
type: Action
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Validate local release inputs
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Methodology
  - Delivery
  - Test
version: 11
updated_at: 2026-10-23 03:14:50 +0400
relations:
  relates_to:
  - CA-O-164
  - CA-O-170
  - CA-O-025
  - CA-R-1525
  - CA-R-1720
---
# Summary

Validate local release inputs

## Action

Validate local release inputs **means** the Action that checks the explicit local-release inputs and configured delivery paths for file/path safety before the declared local validation scope. The complete discovered suite remains the default; a focused scope requires the explicit current Operator record admitted by CA-O-164.

## Scope

The Action checks the configured source and delivery paths, Project Structure, protected settings, compiler, and target paths `101_FRAMEWORK_METHODOLOGY/` and `.caprmedio_caprmedio/000_CAPRMEDIO_framework/` for ordinary input and file/path safety. It does not separately validate Active Atom metadata, placement or relations; release verification uses the declared scope and records whether it is complete or focused.

## Details

Missing, ambiguous or unsafe required input stops before tests or delivery writes and is reported for manual handling. This Action does not copy or clear product or installed contents, compile, install, push, or open a PR.
