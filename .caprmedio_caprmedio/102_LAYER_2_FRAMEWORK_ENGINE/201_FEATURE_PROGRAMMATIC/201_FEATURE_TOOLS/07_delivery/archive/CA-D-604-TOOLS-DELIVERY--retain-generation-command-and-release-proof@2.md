---
atom_id: CA-D-604
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-10 02:57:51 +0400"
subjects:
  governs: "Framework Installation contribution/Generation and release proof"
  depends_on: [Tool, Runtime, Framework Package, Command, Docker Image, Journal]
relations:
  delivery_for: [CA-R-1913, CA-R-1918, CA-M-362]
---
# Summary

Retain generation, command and release proof

## Scope

The evidence that one runtime execution belongs to one activated package and target context.

## Claim

the INSTALL_TOOLS facade **must** bind every runtime process observation to state generation, command and package release proof, and **must not** accept a PID-only assertion as execution identity.

## Details

`.caprmedio_runtime/installation/generations/<state_generation>/release-proof.toml` contains package manifest SHA-256, `framework_version`, version carrier SHA-256, source catalog SHA-256, Full Gate receipt SHA-256, immutable image digest, target context SHA-256 and selector SHA-256. `command.toml`, `environment.toml`, and `wrapper` use the single canonical native schema in CA-D-601-TOOLS-DELIVERY--bind-package-owned-runtime-environment-and-wrappers; their fields are not redefined here. `process.toml`, if present, contains a transient PID only beside those immutable bindings and observed start token.

The generation directory uses the positive integer generation defined by CA-D-601-TOOLS-DELIVERY--bind-package-owned-runtime-environment-and-wrappers and is written under CA-D-603-TOOLS-DELIVERY--serialize-per-project-installation-lock and retained across a later generation. A process observation with a changed selector, command, package, context or generation is stale even when its PID remains live. No process record grants selector publication, migration cleanup or retry authority.
