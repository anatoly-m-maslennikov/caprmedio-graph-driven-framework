---
atom_id: CA-O-168
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Run complete local release test preflight"
  depends_on: [Action, Test, Methodology, Artifact/Revision, Journal]
version: 6
updated_at: "2026-10-10 18:44:09 +0400"
relations:
  relates_to: [CA-O-164, CA-O-185, CA-R-1525]
---
# Summary

Verify candidate release package and image

## Action

Verify candidate release package and image **means** the Action that performs the complete local test preflight, exact candidate-image build, or exact image canary for the frozen local boundary.

## Scope

The `complete_local_suite` phase binds the Version, active source identities and digests, Project Structure, settings, and declared complete test inventory before either clear operation. `candidate_image_build` and `candidate_image_canary` bind the exact staged package, runtime, compiled product, and `ca` payload after compilation. They verify the same local boundary; they do not create another release Workflow or another full-suite obligation.

## Details

A partial, cached, focused, stale, source-only, or unjournaled result is not proof. This Action never clears, copies, installs, publishes, or retries. Each actual Action Run is journaled once with its exact inputs and result.
