# Project release tools

These tools belong to the `caprmedio` Project, not the reusable Framework
package. Shared compiler, installer and test-gate helpers remain in the Engine.

## Two workflows

- **Local release:** stage active Methodology sources, compile and test the
  candidate, replace the release product, compile it, and copy that product to
  the installed Methodology. Keep five separate scoped Git checkpoints. Keep
  configurations unchanged and install the tested Engine/package before MCP
  startup and smoke verification.
- **Public release:** one prompt produces the full PR description and concise
  Version History bullets. Apply documentation, run the full gate, commit/push
  `amm/dev`, create/update its `main` PR, then insert the actual PR URL. That
  URL-only follow-up does not repeat the test suite. Never merge the PR.

The implementation cores are `RELEASE_VERSION/local_release.py` and
`PUBLIC_RELEASE/public_release.py`. Their callbacks are integration boundaries,
not substitute test passes. MCP integration must use the existing admitted
Session, concrete candidate-bound gate evidence and canonical Journal.
The selected MCP provider calls the Project-local Public helper and the
current ten-phase Local dispatcher. Local callbacks retain candidate-bound
proofs, scoped Git checkpoint receipts and installed MCP readiness evidence.
This is source-level integration: the current live runtime has not been
reinstalled or released by these focused tests.

## Kept small

MCP remains the command surface. Automatic recovery/resume, legacy-layout
compatibility and extra release CLI/configuration wrappers are deferred.
Failures stop and report the actual failed step for manual handling.

## Focused tests

```sh
UV_PROJECT_ENVIRONMENT=.caprmedio_runtime/launcher-venv uv run --locked --no-sync --no-env-file --group rmed-workflow-mcp --group workflow-orchestrator python -B -m unittest discover -s PROJECT_TOOLS/tests
```

These tests use temporary fixtures and mocked integrations; they are not a
real release gate and do not publish, install or start the current Project.
