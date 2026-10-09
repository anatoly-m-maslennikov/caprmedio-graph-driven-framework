---
atom_id: CA-D-601
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 17:01:07 +0400"
subjects:
  governs: "Framework Installation contribution/Package-owned runtime invocation"
  depends_on: [Tool, Runtime, Framework Package, Environment, Command]
relations:
  delivery_for: [CA-R-1905, CA-R-1918, CA-M-362]
---
# Summary

Bind package-owned runtime environment and wrappers

## Scope

The declared runtime command and environment generated for an active target installation.

## Claim

the INSTALL_TOOLS facade **must** execute runtime state and environment from the selected package through `uv run --locked --no-sync --no-env-file` and **must not** execute from an installer checkout or ambient environment file.

## Details

For each state generation, `.caprmedio_runtime/installation/generations/<generation>/command.toml` records package manifest digest, package-relative entrypoint, exact argv, target context digest and command digest; `environment.toml` records an allowlisted environment map digest and no secret values. Mutable target settings reside only at `.caprmedio_runtime/config.toml`; a package default may create that file only if absent and never replaces existing bytes during first activation, upgrade, rollback or recovery. Generated wrappers may reference only these files and the selected package root derived from CA-D-598; their own bytes and modes are manifest-recorded.

The accepted argv begins with `uv`, `run`, `--locked`, `--no-sync`, `--no-env-file` and uses only a package-relative Python entrypoint. A missing lockfile, changed package row, unsealed default, checkout path, `--env-file`, unlisted variable or wrapper drift refuses before execution.
