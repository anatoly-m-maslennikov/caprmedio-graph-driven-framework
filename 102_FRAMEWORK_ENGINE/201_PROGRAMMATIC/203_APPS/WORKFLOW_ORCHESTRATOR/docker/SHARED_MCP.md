# Shared host MCP handoff

This lane provides the source-level shape for one external Streamable HTTP MCP
service shared by configured Projects. It is not activated, released, or a
production deployment claim. The existing Project-local runtime remains the
legacy runtime until a coordinated replacement is approved.

## Host settings

Settings live outside any Project. With no explicit `--host-settings` argument,
the loader reads `$XDG_CONFIG_HOME/caprmedio/runtime.toml`, or
`~/.config/caprmedio/runtime.toml` when `XDG_CONFIG_HOME` is unset:

```toml
schema_version = 1

[shared_mcp]
projects_root = "/Users/am/Documents/My_Repos"
http_port = 8092
max_loaded_projects = 2
```

`projects_root` is the host root containing the configured Projects. The
`max_loaded_projects` value bounds warm in-memory contexts; it does not limit
which Projects under the configured root may be addressed.

The container has exactly two application bind mounts: the configured host
Projects root at the same absolute path, read/write, and this host settings file
at the same absolute path, read-only. There is no `/project` remapping, Docker
socket, or home-directory volume. This is an application boundary, not
operating-system or adversarial isolation.

## Dry-run and explicit start

The launcher requires an explicit immutable image reference (`sha256:` followed
by 64 lowercase hexadecimal characters). It never builds an image or guesses a
tag. The default action is a Docker-free dry-run that prints the validated
Compose command and explicit `CAPRMEDIO_*` settings. Inherited Docker client
environment remains internal to the subprocess and is not printed. From the
repository root, using the selected Python 3.14 environment:

```sh
UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
uv run --project "$PWD" --locked --no-sync --python 3.14 --managed-python --no-env-file \
  --group workflow-orchestrator python \
  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/shared_mcp_launcher.py \
  --host-settings "${XDG_CONFIG_HOME:-$HOME/.config}/caprmedio/runtime.toml" \
  --image sha256:<admitted-image-digest>
```

Append `--apply` only as an explicit operator start after the immutable image
includes the intended source changes and the release gate has passed. Readiness
is reported only after Docker readback verifies the image, mounts, loopback
publication, and `/health`; a Docker error or unverified readiness is not a
started/ready claim. No `--apply` invocation is implied by this document.

The shared listener publishes one loopback host port configured by
`shared_mcp.http_port` to container port `8092`, with MCP at `/mcp` and health
at `/health`. Do not start it on the current production port `56317`; preserve
the legacy runtime there until a coordinated replacement is authorized. Tests
use non-production ports and fakes.

Canonical `ca` installation/client integration is a later step. This handoff
does not claim source activation, Docker build, deployment, scheduling, stop,
cleanup, or any additional launcher operation.
