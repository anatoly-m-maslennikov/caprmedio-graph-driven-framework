# Project release tools

These tools belong to the `caprmedio` Project, not the reusable Framework
package. Shared compiler, installer and test-gate helpers remain in the Engine.

## Two workflows

- **Local release:** first commit all tracked changes and untracked nonignored
  files, then verify a clean worktree and index. A clean repository needs no
  empty commit; a failed commit or remaining changes stop before tests, builds
  or Docker work. Validate inputs and run the complete suite before replacing
  delivered or installed files. Copy active Methodology sources, compile the
  product, build the Engine/package and candidate image, install the Methodology
  and Project runtime, then start and verify MCP. Preserve configuration and
  remove eligible stopped obsolete Project-owned containers before MCP startup,
  then repeat cleanup and remove unused obsolete images after successful smoke.
  Preserve verified current-code resources, other running containers and
  unrelated or unproven targets; report unfinished cleanup.
- **Public release:** one prompt produces the full PR description and concise
  Version History bullets. Discover at most one matching open PR, prepare the
  version and documentation, and run the complete suite before public effects.
  Push `amm/dev`, create/update its Draft `main` PR, then insert its actual URL
  when newly known. That URL-only follow-up does not repeat the suite. Never merge.

Local checkpoints keep existing ignored-file and environment-file exclusions.
Excluded nonignored changes stop release rather than being committed or waived.

Fresh Local-release image builds carry exact Project ownership, Project name and
the full build-time owning-repository HEAD commit ID; missing or invalid name or
HEAD stops fresh preparation before building. Name and HEAD record provenance;
the source fingerprint
and immutable image ID identify current code. Matching ownership labels allow
cleanup to identify labelled orphan images. Cached images keep their existing
labels and reuse behavior; no metadata-only rebuild or ownership claim is added.
Legacy unlabelled or otherwise unproven images remain retained and reported.

The implementation cores are `RELEASE_VERSION/local_release.py` and
`PUBLIC_RELEASE/public_release.py`. Run them through `release.py` on the host,
with an Operator-selected `--run-id`. No selected Session, sealed proposal or
Journal receipt gates the release. The host command records linked start and
completed/failed Journal events; a recording failure appears as `recording_error`
without changing the release outcome. Missing content or invalid CLI/draft inputs
record no events.

The MCP bindings remain implemented for reuse. This Project disables their
exposure through its settings:

```toml
[project_mcp]
tool_blacklist = ["release_version", "public.release"]
```

Blacklisted names are absent from discovery and cannot be called through MCP.
Omitting `tool_blacklist` means an empty list. Restart/recreate the MCP gateway
after changing this setting; an implementation-only reload does not refresh it.
The host commands below are the release entry point for this Project.

## Host commands

From the repository root, use the project-local locked uv environment:

```sh
UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
uv run --project "$PWD" --locked --no-sync --python 3.14 --managed-python --no-env-file \
  --all-groups python -B PROJECT_TOOLS/release.py local --run-id local-001
UV_PROJECT_ENVIRONMENT="$PWD/.caprmedio_runtime/launcher-venv" \
uv run --project "$PWD" --locked --no-sync --python 3.14 --managed-python --no-env-file \
  --all-groups python -B PROJECT_TOOLS/release.py public --run-id public-001 --content-draft /absolute/path/release-draft.json
```

`--project-root PATH` is optional; the default is this repository's root, derived
from the script location. Choose a new run ID for each new release; simple IDs
such as `local-001` and `public-001` work for both commands.

The Public draft is a UTF-8 JSON file with exactly `description` and `summary`:

```json
{"description":"## New\n- Describe the additions.\n\n## Fixed\n- Describe the fixes.\n","summary":["Concise Version History bullet."]}
```

The full Markdown description needs nonempty `## New` and `## Fixed` bullet
sections. Summary entries must be nonempty single-line strings of at most 240
characters. The draft must be a regular file, not a symlink, and at most 1 MiB.
Without `--content-draft`, Public returns `input_required` with the content prompt
and schema, without release effects. Supply the draft and rerun with the same
run ID. Results are JSON on stdout; exit status is zero only for `completed`.

Local release reports phase and test-module progress on stderr. Its full test
output is streamed to a log under `.caprmedio_tmp/simple_local_release`, with
the location printed before testing starts. Interruption during release execution
retains that log and a failure report, attempts the terminal Journal event, and exits 130.
It stops the owned test processes without retrying effects or rolling back
earlier release changes. Interrupted Journal recording does not replace an
already observed release outcome.

Release effects run on the host, with its Git, GitHub and Docker tools; the
ordinary MCP container has none of those host privileges. Both commands start
only on Operator instruction and checkpoint safe, nonignored changes. Public
release binds matching fetch/push `origin` identities to the configured repository
slug, requires `amm/dev`, and refuses source drift during its prepared-materials
suite. Focused tests do not establish an actual release or runtime installation.

## Kept small

These repository commands are separate from MCP and the Workflow worker.
Automatic recovery/resume and legacy-layout compatibility are deferred.
Failures stop and report the actual failed step for manual handling.

## Focused tests

```sh
UV_PROJECT_ENVIRONMENT=.caprmedio_runtime/launcher-venv uv run --locked --no-sync --no-env-file --group rmed-workflow-mcp --group workflow-orchestrator python -B -m unittest discover -s PROJECT_TOOLS/tests
```

These tests use temporary fixtures, real scoped Git checkpoints and mocked
external integrations. They are not a real release gate and do not publish,
install or start the current Project.
