# Project release tools

These tools belong to the `caprmedio` Project, not the reusable Framework
package. Shared compiler, installer and test-gate helpers remain in the Engine.

## Two workflows

- **Local release:** validate inputs and run the complete suite before replacing
  delivered or installed files. Copy active Methodology sources, compile the
  product, build the Engine/package and candidate image, install the Methodology
  and Project runtime, then start and verify MCP. Preserve configuration and
  remove only proven superseded Project-owned images.
- **Public release:** one prompt produces the full PR description and concise
  Version History bullets. Discover at most one matching open PR, prepare the
  version and documentation, and run the complete suite before public effects.
  Push `amm/dev`, create/update its Draft `main` PR, then insert its actual URL
  when newly known. That URL-only follow-up does not repeat the suite. Never merge.

The implementation cores are `RELEASE_VERSION/local_release.py` and
`PUBLIC_RELEASE/public_release.py`. Direct MCP requests bind the connected
Project through `project_root` and an Operator-selected `run_id`; Public release
also needs `content_draft` with exactly `description` and `summary`. No selected
Session, sealed proposal or Journal receipt gates the release. Journal recording
errors are reported separately from the actual release outcome.

Release effects run on the host, with its Git, GitHub and Docker tools; the
ordinary MCP container has none of those host privileges. Both commands start
only on Operator instruction and checkpoint safe, nonignored changes. Public
release binds matching fetch/push `origin` identities to the configured repository
slug, requires `amm/dev`, and refuses source drift during its prepared-materials
suite. Focused tests do not establish an actual release or runtime installation.

## Kept small

MCP remains the command surface. Automatic recovery/resume, legacy-layout
compatibility and extra release CLI/configuration wrappers are deferred.
Failures stop and report the actual failed step for manual handling.

## Focused tests

```sh
UV_PROJECT_ENVIRONMENT=.caprmedio_runtime/launcher-venv uv run --locked --no-sync --no-env-file --group rmed-workflow-mcp --group workflow-orchestrator python -B -m unittest discover -s PROJECT_TOOLS/tests
```

These tests use temporary fixtures, real scoped Git checkpoints and mocked
external integrations. They are not a real release gate and do not publish,
install or start the current Project.
