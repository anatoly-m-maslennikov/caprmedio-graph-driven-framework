---
atom_id: CA-R-1905
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Package-owned execution"
  depends_on: [Tool, Runtime, Framework Package, Environment, Command]
relations:
  relates_to: [CA-D-601, CA-D-604]
---
# Summary

Execute installed runtime from package-owned bytes

## Scope

the native invocation boundary for an activated target runtime.

## Claim

the INSTALL_TOOLS facade **must** execute the selected package through `uv run --locked --no-sync --no-env-file` and **must not** execute checkout bytes, an ambient environment file or an unsealed command.

## Details

Every wrapper and execution record names one package-relative entrypoint, exact argv, allowlisted environment digest, target context and generation. The current package and target selectors are reopened immediately before use. A missing lockfile, changed package row, unlisted environment entry or any checkout path is a pre-execution refusal.
