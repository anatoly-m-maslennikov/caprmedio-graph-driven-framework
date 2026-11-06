# Workbench release acceptance

Accepted Workbench RMED is Current and implemented. Five remaining RMED Drafts belong to the deferred standalone chat. General PROGRAMMATIC proposals in A1322 remain Drafts and are outside this release.

- C704: Resolved in source. Docker misclassified a new directory as a file; the watcher now checks its actual filesystem type and registers before publishing.
- E780: 5,000 Atoms, twelve timed mutations at 1.34–1.40 seconds; full reread, retained log and restart passed. Total isolated acceptance: 96.184 seconds.
- Header compatibility: nineteen shared checks, nine nested-reader checks and six SQL-column checks pass; the source/writer cutover is not performed.
- Native Project name: both transports and four rebuilt actual-backend bridge checks pass. Actual Codex host remains unverified.
- MCP trace corrections: nineteen affected checks, Ruff and diff check pass.
- Prior full Docker module: other six cases pass; the corrected watcher case now passes independently. The release reruns the integrated selection.

Pending: local release, live-project all-operation canary, actual Codex-host UI and final Epic acceptance. The full repository suite is not claimed green.

Detailed test logs and the immutable test-image IDs are in `.caprmedio_tmp/workbench/release-20261106/`.
