---
atom_id: CA-E-606
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 17:01:07 +0400"
subjects:
  governs: "Framework Installation contribution/Launcher acceptance"
  depends_on: [Tool, Runtime, Framework Package, Environment, Skill, Projection]
relations:
  evaluation_for: [CA-R-1903, CA-R-1905, CA-R-1911, CA-M-362, CA-D-601]
---
# Summary

Verify package-owned launcher, environment and selector order

## Scope

the final target activation fixture.

## Claim

the QA case **must** prove that runtime command and environment resolve only package-owned bytes and the target selector is last, and **must not** allow checkout, env-file or partial-state activation.

## Details

The fixture verifies the distinct `.caprmedio_install/current.toml` and target current selector, exact `uv run --locked --no-sync --no-env-file` argv, package-relative entrypoint, allowlisted environment and monotonic generation. It verifies that a package default creates `.caprmedio_runtime/config.toml` only when absent and that existing config bytes survive first activation, upgrade, rollback and recovery. Failures inject checkout path, `--env-file`, missing lockfile, wrapper/Skill/projection failure, selector failure and an attempted config overwrite; previous activation or actual `recording_pending` selection remains authoritative.
