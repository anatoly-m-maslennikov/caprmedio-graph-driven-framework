---
atom_id: CA-O-165
content_role: Operations
type: Action
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Validate local release inputs"
  depends_on: [Action, Operator, Methodology, Delivery, Test]
version: 8
updated_at: "2026-10-14 19:54:14 +0400"
relations:
  relates_to: [CA-O-164, CA-O-170, CA-O-025, CA-R-1525, CA-R-1720]
---
# Summary

Validate local release inputs

## Action

Validate local release inputs **means** the Action that checks the explicit local-release inputs and configured delivery paths for file/path safety before the full test suite.

## Scope

The Action checks the configured source and delivery paths, Project Structure, protected settings, compiler, and target paths `101_FRAMEWORK_METHODOLOGY/` and `.caprmedio_caprmedio/000_CAPRMEDIO_framework/` for ordinary input and file/path safety. It does not separately validate Active Atom metadata, placement or relations; release verification uses the full test suite.

## Details

Missing, ambiguous or unsafe required input stops before tests or delivery writes and is reported for manual handling. This Action does not copy or clear product or installed contents, compile, install, push, or open a PR.
