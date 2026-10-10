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
version: 5
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  relates_to: [CA-O-164, CA-O-170, CA-O-171, CA-O-025, CA-D-563, CA-R-1525, CA-R-1720]
---
# Summary

Freeze and validate the release boundary

## Action

Freeze and validate local release boundary **means** the Action that freezes one local Version and validates its exact active Methodology Source boundary before the preflight suite.

## Scope

The Action records the canonical Version value and `version.toml` digest; active Atom identities, revisions, and digests from only Core Meta-Model, installed extensions, and Project Configuration; the Project Structure, protected settings, compiler, private package/image/runtime/`ca` preparation inputs, full-suite declaration, and target paths `101_FRAMEWORK_METHODOLOGY/` and `.caprmedio_caprmedio/000_CAPRMEDIO_framework/`.

## Details

Missing, inactive, stale, unpinned, or mismatched input stops before tests or writes. This Action does not copy, compile, install, test, push, open a PR, invoke a Workflow, or authorize retry. Its actual Action Run is journaled once with the bound boundary and result.
