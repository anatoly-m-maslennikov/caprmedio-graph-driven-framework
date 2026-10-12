---
atom_id: CA-D-603
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Per-Project installation lock"
  depends_on: [Tool, Project, Runtime, Skill, Projection, State]
relations:
  delivery_for: [CA-R-1912, CA-R-1913, CA-M-364]
---
# Summary

Serialize per-Project installation state

## Scope

The exclusive lock shared by all mutable target installation carriers.

## Claim

the INSTALL_TOOLS facade **must** use **=1** per-Project installation lock for selector, wrappers, Skill, projection and state publication, and **must not** treat a PID as lock ownership or process proof.

## Details

`.caprmedio_runtime/installation/lock.toml` contains `schema_version = 1`, `target_project_context_sha256`, `owner_run_id`, `operation`, `lock_generation`, `acquired_at`, `command_sha256` and `lease_nonce`. It is acquired through a create-if-absent atomic filesystem operation, is reopened before every publish boundary and is released only by the matching owner generation after a terminal result. A stale or uncertain lock refuses publication until an explicit inspection/recovery path establishes ownership.

All installation, adoption, migration, selector publication, wrapper replacement, Skill publication, projection write and runtime-state write take this lock. A distinct package candidate lock or first-install lock is not a substitute. Lock records are project-contained, do not serialize unrelated Projects and do not make a cross-Project registry.
