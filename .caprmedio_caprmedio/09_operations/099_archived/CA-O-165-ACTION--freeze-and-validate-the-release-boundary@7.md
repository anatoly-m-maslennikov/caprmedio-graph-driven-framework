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
version: 7
updated_at: "2026-10-12 00:00:00 +0000"
relations:
  relates_to: [CA-O-164, CA-O-170, CA-O-025, CA-D-563, CA-R-1525, CA-R-1720]
---
# Summary

Validate local release inputs

## Action

Validate local release inputs **means** the Action that checks current active Methodology Sources and configured delivery paths before local-release tool checks.

## Scope

The Action checks the current active Atoms from Core Meta-Model, installed extensions, and Project Configuration, plus Project Structure, protected settings, compiler, and target paths `101_FRAMEWORK_METHODOLOGY/` and `.caprmedio_caprmedio/000_CAPRMEDIO_framework/`.

## Details

Missing, inactive, ambiguous, or mismatched input stops before tests or delivery writes and is reported for manual handling. This Action does not copy or clear product or installed contents, compile, install, push, or open a PR.
