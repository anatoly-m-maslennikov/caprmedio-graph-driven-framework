---
atom_id: CA-M-362
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-10 01:20:06 +0400"
subjects:
  governs: "Framework Installation contribution/Runtime activation"
  depends_on: [Tool, Runtime, Framework Package, Skill, Projection, State]
relations:
  method_for: [CA-R-1904, CA-R-1905, CA-R-1911, CA-R-1913]
---
# Summary

Stage and activate one package-owned target runtime

## Scope

the package-to-target state staging and destructive replacement activation procedure.

## Claim

the INSTALL_TOOLS facade **must** stage package-owned state under the shared target lock, remove the selected installed package only after validation and quiescence, and publish the target selector last; it **must not** run the checkout, expose a partial runtime or retain a removed package as rollback.

## Details

1. Reopen `.caprmedio_install/current.toml`, package manifest, catalog, Full Gate/image proof and target context.
2. Allocate the next generation; write package-relative command and environment records using `uv run --locked --no-sync --no-env-file`.
3. If `.caprmedio_runtime/config.toml` is absent, stage its package default once; otherwise reopen and retain the existing mutable configuration bytes. Stage wrappers, hook-free `ca`, projection and state; reopen all bytes, modes, configuration retention and generation proof. An activation, replacement or recovery does not overwrite configuration.
4. After the staged bytes, quiescence and migration evidence are reopened, remove exactly the selected installed package, install the sealed replacement, then atomically replace `.caprmedio_runtime/installation/current.toml`. Reopen the actual selected bytes and record canonical Journal evidence. A failure before removal keeps staged carriers non-active and the prior selection authoritative. A failure after removal but before complete replacement selection leaves the runtime unavailable and no selector may claim the removed or partial package is current; configuration, Project authority, Journal and transaction evidence remain intact. A recording failure after complete selector replacement retains the actual new selected bytes and returns `recording_pending`; it does not imply rollback, replay or a new activation. Recovery may append only the missing terminal Event after reopening the original selected bytes, package, context and started-Run evidence.
