---
atom_id: CA-O-165
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Freeze and validate release boundary"
  depends_on: [Action, Operator, Version, Artifact/Revision, Methodology, Delivery, Skill, Test, Docker Image, Journal]
version: 4
updated_at: 2026-10-09 16:39:30 +0400
relations:
  relates_to: [CA-O-164, CA-O-170, CA-O-171, CA-O-025, CA-D-563, CA-R-1525, CA-R-1720]
---
# Summary

Freeze and validate the release boundary

## Action

Freeze and validate release boundary **means** the Action that first freezes the exact executing Version N and separately pinned candidate N+1, then validates all selected release bindings before a release effect is admitted.

## Scope

The `freeze` phase records N's current Framework/Methodology revisions, source frontier and rollback identity and records N+1's distinct source revisions, digests, canonical `version.toml` Version value, carrier-byte SHA-256 and candidate identity. The `validate` phase checks the selected active-source inventory, explicit extension/configuration selection and admitted pinned catalog revisions, the sealed private candidate export and its logical root `methodology/` delivery mapping, post-gate selected Project installed control target, explicit pinned-snapshot compiler Tool boundary, private candidate root `.caprmedio_tmp/release_candidates/<run_id>/`, reusable beta-release destination `.caprmedio_install/releases/<package_manifest_sha256>/` with `.caprmedio_install/current.toml`, selected Project `.caprmedio_runtime/installation/current.toml`, complete test declaration, candidate image identity, exact prior-image identity, permissions and canonical Journal capability.

## Details

N must remain the executing runtime and rollback point until candidate promotion passes all required gates. N+1 must be a distinct pinned candidate; neither a mutable label nor an unbound current source frontier is sufficient. **Before** delivery, validate the exact canonical Version value and `version.toml` carrier-byte SHA-256, active-source closure, selected configuration/catalog/lock and candidate-root byte inventory; a changed definition, source, digest, Version, configuration, catalog, lock, destination, permission, selected-snapshot compiler boundary, package contract, test declaration, image identity, Journal capability or missing reviewed path reconciliation returns blocked. This Action does not copy, compile, install, test, build, promote, remove an image, select another candidate, create a release tag, invoke a Workflow, or authorize its own retry. Its actual Action Run is journaled once with the bound boundary and result.
