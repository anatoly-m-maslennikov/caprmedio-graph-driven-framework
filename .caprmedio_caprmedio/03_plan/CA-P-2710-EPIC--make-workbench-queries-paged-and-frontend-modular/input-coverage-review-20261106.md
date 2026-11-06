# Workbench input coverage — 6 November 2026

## Scope and result

Reviewed 223 user messages from **4 November 19:58:47 to 6 November 19:58:47, Asia/Tbilisi**. Exact transcript timestamps and message IDs are in `.caprmedio_tmp/workbench/input-audit-20261106/user-input.json`; `input-ledger.md` indexes every recovered message. Four read-only lanes checked frontend, backend, MCP/Codex, and RMEDO/tasks. Questions, screenshots, corrections and control messages are retained; they are not each treated as a new requirement requiring every content role.

**Not all final decisions have completed RMEDO, task, implementation, test and deployment coverage.** Earlier query/View/grid/logging/service changes mostly do. The remaining gaps are concentrated in the latest schema/UI cycle, realistic watcher acceptance and native Codex UI. Explicit Operator decisions authorize the requested work; an unpromoted Draft is a source-recording gap, not a request for another permission gate.

## Later decisions applied

| Earlier input | Governing later decision |
| --- | --- |
| Save on every Run/Check | Do not save every query; save explicitly, only after successful Run. |
| Multiple statements selected by cursor | One View contains one query. |
| Worksheet | View. |
| Settings/Saved top left | Top right, alongside Workbench and Project name. |
| Standalone chat and its controls | Disabled/deferred; native Codex integration is the active target. |
| One text zoom | Separate Interface and Content text zoom; whole-Interface zoom remains separate. |
| Underscore-only Content columns (U207) | U213/U214 retain dots between path segments and use snake_case within them. |
| Declared Header columns only | U205: all observed Header properties; Content remains declaration-only. |
| Fixed Content schema asset | U212: generate the schema from model Declarations. |
| One-week query log | Two-day TTL, hourly batches; saved Views have no TTL. |
| Delete all results on closing a View | Retain while younger than configured TTL OR owned by an open View; successful rerun replaces previous results. |

U222 requests query **formatting**. Its old example identifiers do not repeal the explicit naming decisions. It does not request a SQL formatter, rewriting saved queries, or prefilling new Views.

## Coverage and gaps

| Area | RMEDO | Tasks | Implementation / verification |
| --- | --- | --- | --- |
| Direct/derived graph relations, paths, filename and reference | Current contracts exist; revised Header shape is Draft | Earlier cycle recorded | Implemented; new schema shape is not deployed. |
| Saving, IDs/URLs, Journal, explicit Run & Save, bounded preview | Current | Recorded | MCP/HTTP/frontend implementation and earlier integration evidence exist. |
| View CRUD/run/fetch/focus/save; per-chat Workspace | Current | Recorded | Shared API exists; this does not establish a native Codex Workbench UI. |
| Palette, shortcuts, five-second autosave, names and close confirmation | Current | Recorded | Implementation and browser tests exist. |
| Tabulator, whole-result filter/sort, one grouping column, menus, adaptive rows and cell limits | Current | Recorded | Implementation and behavior tests exist. No new menu redesign is required by this audit. |
| Query log, change log, TTL settings and sync status | Current | Recorded | Implemented with earlier integration evidence; realistic watcher acceptance remains open. |
| Restart/full reread, discovery generation and project-context binding | Current | Recorded | MCP/HTTP/health/release support exists. Auto-commit remains disabled. |
| Rebuildable Header/Content schema and declaration compiler | M500 and related amendments are Draft | Explicit adoption/reconciliation task was missing | Working-tree code and read-only current-source proof exist. Current E677 still prohibits compiled/intermediate schema state and must be reconciled. |
| Latest compact layout, muted types, split text zoom, source newlines and dark-grid fix | Revised frontend RMED is Draft | Prior completed cycle does not cover this adoption/release | Implemented and tested in working tree; not deployed. |
| Real-project all-operation canary | E794 is Draft | Full Atom/Declaration matrix was not explicit | Test implementation and offline rehearsal exist; live preflight rejected the old schema before source writes. No passing live mutation run. |
| Incremental performance at actual scale | Current M465/E677/E780 plus pending schema amendments | Scale/live acceptance already open | Incremental code and focused timing evidence exist; approximately-5,000-source Docker/new-directory acceptance and latest live timings remain pending. |
| Full native Codex Workbench | Current R2902/D681 family | Open | Inline/fullscreen probe and bridge work. Actual Workspace/View UI is not implemented. |
| Default query style | README only | Missing | Examples changed; applicable Method/prompt recording is missing. No formatter or default-query generator was requested. |
| Direct implementation trace completeness | M431 and proposal A1322 | Open audit work | ID/version comments exist; outstanding stale/missing/caller-only trace findings are not all closed. Comments alone do not prove conformance. |
| Four original Problems and prevention policies | C700–C703 and E750–E753; five M and five E amendments recorded | Recorded | Earlier fixes/evidence retained. A later reproduced child-file watcher miss needs its own open issue and realistic acceptance evidence. |

## RMED reconciliation packet

The nine Draft entries in `.caprmedio_tmp/workbench/header-sql-column-names/drafts.json` are R2726@5, D672@12, E675@6, M500@1, M464@8, R2727@15, D674@20, E794@1 and M465@17. They are not promoted by this review. Reconcile all related Current sources too, especially E677's obsolete no-schema assertions; promoting the nine entries alone would leave that contradiction.

Content declaration generation currently yields only five literal model-declared columns. Former TLDR/Analysis/Plan/Operation fields lack the needed literal declarations. This is a model-source coverage issue to resolve with the source owner, not permission for Workbench to invent implicit columns. The shared Header handoff also needs its actual final identity layout reviewed before claiming compatibility. No native MODEL or live Header migration belongs to this audit.

## Runtime and evidence boundary

Read-only health, schema and sync-status requests passed during this audit. Docker inspection verified version **0.4.4.27**, image `sha256:86fe6c76e0f3abb8679dd37c9cf68e8035f86a8cfe268e3b9f85c9d7a18a719b`, source commit `704877a8a35b3dbad5d90d5b90d3642ab7849a72`. The live schema still exposes short `id`/`status` and `content.claim.formal claim`, proving it does not contain the latest schema changes. Exact responses are in `.caprmedio_tmp/workbench/input-audit-20261106/live-read-only.json`.

Earlier recorded latest-code checks: 142 host tests with one opt-in skip, 19 browser flows, seven native MCP/HTTP Workspace cases, 24 shared Scope Unit cases, and a read-only disposable-database proof using 4,969 indexed real Atoms and 47 Scope Units. These are recorded evidence, not fresh tests run by this audit or proof that their code is deployed. No full-repository green, latest Docker scale pass, latest live canary, Header cutover or new release is claimed.

The old closed-cycle checkboxes refer to earlier releases. The Epic needs a separate current cycle and one accurate current runtime status. Preserve historical receipts rather than rewriting them as if newer work had already shipped.

## Review adjudication

The initial frontend suggestion to remove dots was rejected: it used superseded U207 and missed U213/U214. The suggestion to require a prefilled new-View query was rejected: U222 requests writing style. An extra row-copy shortcut in a cell menu is minor surplus, not a missing approved capability, and is not used to add a new blocking task. Context makes U206's requested adaptive width clear; no spelling question is needed.

No unresolved Operator choice is needed to record or execute the confirmed remaining tasks within the accepted scope. Ask if a real new behavior decision is found during that work.

## Remaining work

Update CA-P-2710 with separate tasks to reconcile/adopt RMED, record query-writing style, complete the remaining trace/issue records, implement/fix the accepted sources, run realistic Docker and live-project acceptance, deliver the native Codex UI, release the tested Workbench, and verify completion. Leave standalone chat and its known bridge failure deferred.

This audit changes its reports and the Epic only. No tool code, runtime, native MODEL, live Header data or existing Draft is changed; no suite is rerun.
