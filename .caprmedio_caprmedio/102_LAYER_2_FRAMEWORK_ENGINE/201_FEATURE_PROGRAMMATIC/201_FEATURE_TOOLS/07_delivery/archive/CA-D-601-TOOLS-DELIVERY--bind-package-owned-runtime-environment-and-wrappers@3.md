---
atom_id: CA-D-601
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 02:57:51 +0400"
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

1. Native `state_generation` is a positive integer; its directory name is the decimal rendering of that integer. Legacy migration generation names remain a separate representation.
2. `command.toml` has exactly these keys: `schema_version = 1`, `package_manifest_sha256`, `target_project_context_sha256`, `state_generation`, `entrypoint`, `argv`, `environment_sha256`, `wrapper_sha256`, `invocation_nonce`, `command_sha256`. The command digest is SHA-256 of UTF-8 canonical JSON of the other keys: sorted keys, compact separators, no non-finite numbers, and unescaped Unicode.
3. `entrypoint` is a relative regular `.py` member with role `engine` in the reopened package inventory. The exact argv is `uv run --locked --no-sync --no-env-file --project <selected-package-root> python <entrypoint>`, followed by declared fixed non-secret arguments. No runtime argument forwarding is appended.
4. `environment.toml` has exactly `schema_version = 1`, `variables`, and `environment_sha256`. Its digest uses the same canonical JSON rule, excluding its own digest. The only allowed variable names are `PATH`, `HOME`, `UV_PROJECT_ENVIRONMENT`, and `UV_CACHE_DIR`. PATH contains explicit absolute directories; HOME is an explicit absolute non-secret path. The UV environment and cache paths are generated under the target's `.caprmedio_runtime` and `.caprmedio_tmp`, respectively.
5. `wrapper` is a deterministic `/bin/sh` script. It changes directory to the selected package root, then executes `env -i` with only the declared variables and exact argv. Every value is shell-quoted. It neither reads ambient environment files nor forwards `$@`.
6. Staging writes only `command.toml`, `environment.toml`, `wrapper`, and `stage-manifest.toml` under `.caprmedio_tmp/installation/staging/<lock_generation>` while holding the concrete installation publication lock. TOML carriers use mode 0600; the wrapper uses 0700. The closed stage manifest has `schema_version = 1`, `package_manifest_sha256`, `target_project_context_sha256`, `state_generation`, `lock_generation`, and `files`; the files list has exactly the other three members, with their relative path, integer mode, and byte SHA-256.
7. A staged command is prospective data, not permission to invoke it or proof of a complete runtime. Staging reopens the package and target context, validates inventory membership, writes and reopens the fragment, and performs no process execution, environment provisioning, configuration write, selector publication, Skill installation, or projection installation. Actual invocation requires an installation-specific Operator command binding the exact command digest and target context.
8. Mutable target settings reside only at `.caprmedio_runtime/config.toml`. A package default creates that file only when absent; installation retains existing bytes. Execution requires the declared locked environment to be provisioned and the command, environment, wrapper, package, context, and invocation authority to be revalidated.

