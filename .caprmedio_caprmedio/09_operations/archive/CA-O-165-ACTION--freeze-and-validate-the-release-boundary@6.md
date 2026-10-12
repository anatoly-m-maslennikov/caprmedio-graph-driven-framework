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
  governs: "Freeze and validate local release boundary"
  depends_on: [Action, Operator, Version, Artifact/Revision, Methodology, Delivery, Test, Journal]
version: 6
updated_at: "2026-10-11 16:46:21 +0000"
relations:
  relates_to: [CA-O-164, CA-O-170, CA-O-171, CA-O-025, CA-D-563, CA-R-1525, CA-R-1720]
---
# Summary

Freeze and validate the release boundary

## Action

Freeze and validate local release boundary **means** the Action that freezes one local Version and validates its exact active Methodology Source boundary before the preflight suite.

## Scope

At Run start the Action automatically discovers the current registered release definitions and their Action-to-Tool bindings and records the prepared internal Version value and `version.toml` digest. It captures active Atom bytes, identities, revisions, and digests from only Core Meta-Model, installed extensions, and Project Configuration into one consistent snapshot. It also records the Project Structure, protected settings, compiler, private package/image/runtime/`ca` preparation inputs, full-suite declaration, and target paths `101_FRAMEWORK_METHODOLOGY/` and `.caprmedio_caprmedio/000_CAPRMEDIO_framework/`.

## Details

Missing, inactive, ambiguous, or mismatched captured input stops before tests or delivery writes. The Operator supplies no manual revision bindings or separately refreshed source manifest. Every later release phase consumes the same captured active-source snapshot and verifies its integrity. This Action does not copy or clear product or installed contents, compile, install, test, push, open a PR, invoke a Workflow, or authorize retry. Its actual Action Run is journaled once with the bound boundary and result.
