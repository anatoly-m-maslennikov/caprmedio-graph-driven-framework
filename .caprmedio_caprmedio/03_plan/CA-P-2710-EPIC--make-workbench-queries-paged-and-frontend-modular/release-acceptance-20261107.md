# Workbench release acceptance

Local release **0.4.4.29** completed from source commit `e972fa26abbf8d75c150f610a809e5d832d492fc`. The endpoint remains `http://127.0.0.1:56317/caprmedio/mcp`.

## Passed

- 34 selected modules: 233 tests, one opt-in live-canary skip. This is not a full-repository green claim.
- All seven Docker cases and launcher integration.
- The 5,000-small-Atom watcher matrix: twelve mutations at 1.29–1.38 seconds, retained log, full reread and restart. C704 is Resolved.
- The opt-in live-project canary then passed all fourteen checks and cleanup in 235.484 seconds. Native Atom create/update/rename/move/delete and Scope Unit declaration create/update/move/rename/delete were exercised.
- Shared Header compatibility: nineteen checks; nested-reader and SQL-column checks: fifteen. The live source/writer Header cutover was not performed.
- Four rebuilt native-bridge checks and both public Project-name transports.
- Installed MCP create/update/run/fetch/remove View operations, `preview: 5` and `save: false`. The temporary verification View was removed and the prior focus restored.
- Plugin cache refreshed from the local repository.

## Timings

The small-content fixture is not the rich live project. Live update/move took 3.7–3.9 seconds. The canary's empty `subjects: {}` introduces a new observed `header_subjects` column; its create/delete therefore rebuild the schema and took roughly 23–24 seconds; Scope Unit changes took 18–21 seconds. The initial cold index took 31.7 seconds. These rebuilds are separate from ordinary incremental updates.

## Open

C705: the Operator sees no native interface after `workspace_open`. Live metadata advertises `ui://caprmedio/workbench.html`; the current 1,019,529-byte self-contained resource is served with MIME `text/html;profile=mcp-app`. Disposable-host tests do not establish native Codex mounting. Wrapped Code Mode calls are a possible explanation, not a proven cause. No documented direct render operation is available in this session. Do not change cache keys, add a browser fallback or restart repeatedly without evidence.

The Epic remains Active. Five standalone-chat RMED Drafts and general PROGRAMMATIC proposals remain deferred/outside this release.

## Evidence

Detailed immutable-image IDs, test output, live canary results, phase timings and descriptor metadata are in `.caprmedio_tmp/workbench/release-20261106/`. The local release receipt is `.caprmedio_runtime/simple_local_release/reports/workbench-20261107-final.md`.
