---
atom_id: CA-D-604
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 03:33:44 +0400"
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

### Native proof staging

The closed native `release-proof.toml` keys are `schema_version = 1`, `package_manifest_sha256`, `framework_version`, `version_toml_sha256`, `source_catalog_sha256`, `full_gate_receipt_sha256`, `image_digest`, `target_project_context_sha256`, `state_generation`, `installation_lock_generation`, `installation_command_sha256`, `command_sha256`, `command_stage_manifest_sha256`, and `selector_sha256`.

A staged proof lives with the exact prospective `selector.toml` bytes under `.caprmedio_tmp/installation/proofs/<installation_lock_generation>`, both mode 0600. The concrete installation lock remains held while creating and reopening these regular carriers. The writer physically reopens the selected D598 package/selector, persisted D600 context, and D601 command-stage carriers. It derives package/version/catalog/Full Gate/image facts from those reopened carriers, not caller strings. The command-stage manifest byte hash binds all staged command files. `installation_command_sha256` equals the lock's command binding; `command_sha256` is the separate prospective runtime command digest.

The raw prospective selector must use the closed D599 native schema and match that same package, context, positive integer generation, lock generation and immutable image. `selector_sha256` hashes those exact bytes without changing their formatting. This avoids a cycle: render selector bytes, hash them, render proof, then publish the already-rendered selector only after the complete installation is independently admitted.

The reader reopens and validates all of the same byte and typed bindings. Staging and successful reading confer no Operator authority or Full Gate pass, publish no selector, write no configuration or process state, and do not reuse legacy string-generation proof writers. The later admitted publisher copies the verified proof to the final native generation, then publishes those same selector bytes last.
