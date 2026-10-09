---
atom_id: CA-M-362
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-09 17:01:07 +0400"
subjects:
  governs: "Framework Installation contribution/Runtime activation"
  depends_on: [Tool, Runtime, Framework Package, Skill, Projection, State]
relations:
  method_for: [CA-R-1904, CA-R-1905, CA-R-1911, CA-R-1913]
---
# Summary

Stage and activate one package-owned target runtime

## Scope

the package-to-target state staging and single activation procedure.

## Claim

the INSTALL_TOOLS facade **must** stage package-owned state under the shared target lock and publish the target selector last, and **must not** run the checkout or expose a partial runtime.

## Details

1. Reopen `.caprmedio_install/current.toml`, package manifest, catalog, Full Gate/image proof and target context.
2. Allocate the next generation; write package-relative command and environment records using `uv run --locked --no-sync --no-env-file`.
3. If `.caprmedio_runtime/config.toml` is absent, stage its package default once; otherwise reopen and retain the existing mutable configuration bytes. Stage wrappers, hook-free `ca`, projection and state; reopen all bytes, modes, configuration retention and generation proof. An activation, upgrade, rollback or recovery does not overwrite configuration.
4. Atomically replace `.caprmedio_runtime/installation/current.toml`, then reopen the actual selected bytes and record canonical Journal evidence. A failure before replacement keeps staged carriers non-active and the prior selection authoritative. A failure after replacement retains the actual new selected bytes and returns `recording_pending`; it does not imply rollback, replay or a new activation. Recovery may append only the missing terminal Event after reopening the original selected bytes, package, context and started-Run evidence.
