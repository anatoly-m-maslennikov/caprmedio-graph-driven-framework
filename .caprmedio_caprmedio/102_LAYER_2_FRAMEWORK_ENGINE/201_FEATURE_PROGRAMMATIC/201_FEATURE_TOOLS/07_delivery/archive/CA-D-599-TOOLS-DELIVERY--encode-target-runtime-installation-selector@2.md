---
atom_id: CA-D-599
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 17:01:07 +0400"
subjects:
  governs: "Framework Installation contribution/Target runtime selector"
  depends_on: [Tool, Framework Package, Runtime, Project, Manifest]
relations:
  delivery_for: [CA-R-1904, CA-R-1905, CA-M-362]
---
# Summary

Encode the target runtime installation selector

## Scope

The final activation carrier for one selected target Project runtime.

## Claim

the INSTALL_TOOLS facade **must** activate a target runtime through `.caprmedio_runtime/installation/current.toml` **only** when it selects a verified current package, one target-Project context and **=1** monotonic state generation.

## Details

The closed TOML keys are `schema_version = 1`, `package_manifest_sha256`, `target_project_context_sha256`, `state_generation`, `installation_lock_generation` and `image_digest`. It is valid only when its package digest equals the reopened `.caprmedio_install/current.toml` digest, its context is a reopened CA-D-600 carrier, and its generation has an authenticated CA-D-604 record. It contains no checkout path, PID, fallback package, extension autoload list or mutable configuration. Mutable target settings live only in `.caprmedio_runtime/config.toml`, outside the package and both selectors.

The selector is atomically replaced after the target Skill, wrappers, projection and generation state are complete under the same installation lock. Default `.caprmedio_runtime/config.toml` is created only when absent; an existing config is never overwritten by first activation, upgrade, rollback or recovery. A failed write leaves the prior selector authoritative and retains the staged state as non-active evidence.
