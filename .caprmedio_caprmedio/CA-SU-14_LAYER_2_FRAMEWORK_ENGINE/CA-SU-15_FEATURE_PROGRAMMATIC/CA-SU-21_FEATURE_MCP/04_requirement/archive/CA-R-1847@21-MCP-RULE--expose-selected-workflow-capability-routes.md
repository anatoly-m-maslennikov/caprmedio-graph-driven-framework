---
atom_id: CA-R-1847@21
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 21
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/UX/MCP Selected Capability and Workflow Interface
  depends_on:
  - Subject/Graph Node/Implementation/Code/Tool
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Occurrent/Execution/Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations: {}
type: Rule
tier: 3
---
# Summary

Expose selected Workflow capability routes

## Scope

The Project-local MCP adapter surface for the original thirteen Operator-selected
P1117 capabilities, two explicitly admitted read-only P1520 query Workflows,
and separately admitted Release Version and PUBLIC_RELEASE Workflows.

Exposure uses the Project Settings snapshot loaded when the MCP host/gateway starts or is recreated; implementation-only reload does not refresh the blacklist. This policy removes callable admission only: source Atoms, retained implementations and read-only analysis remain available.

## Claim

MCP **must** expose only the capability adapters admitted below through the existing reloadable Project-local server. Except for the narrow current O016 Version 18 Integrated pending/status/`submit_result` handoff described below, Non-Release selected routes delegate execution and actual Run observations to shared `WORKFLOW_OPERATIONS/RUN_SUPPORT`; local **and** public Release use their existing direct runners.

## Details

`project_mcp.tool_blacklist` is an optional list of exact MCP tool names; an absent list means no names are blocked. A listed name is omitted from tool discovery and refused at invocation before its handler runs, including cached or direct calls. This Project lists `release_version` and `public.release`: their existing adapters, runner bindings and request contracts remain available in source for later reuse, but neither tool is exposed or callable through MCP. The admitted bindings below describe retained capability contracts, not an override of that exposure policy. Use the repository-host `PROJECT_TOOLS/release.py local|public` commands for releases.

The admitted route-name set is `create_atom`, `update_atom`, `replace_atom`,
`change_atom_status`, `create_scope_unit`, `rename_scope_unit`,
`move_scope_unit`, `remove_scope_unit`, `run_implementation_workflow`,
`revert_changes`, `build_entities_graph`, `build_terms_graph`,
`build_applicable_methodology`, `find_and_fetch_artifacts`, and
`find_and_fetch_journal_events`, `release_version`, and `public.release`. The non-Release selected-definition binding remains the derived fifteen-route
Projection `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json`.
The two Release commands have separate direct bindings declared in CA-D-547.
The selected Projection carries
every non-Release selected route's full current source Workflow, ordered Steps, ordered Action
bindings, and only source-closed native Action calls with exact source path,
Version, and SHA-256 digest. It is an immutable derived projection, not another
Workflow graph or source authority.

The original thirteen entries resolve their current selected source registry by CA-A-1142's identity and declared authoritative location. The two query entries use `query_source_admissions` in that same canonical manifest, resolving CA-P-1618 and CA-P-1535 by their identities at the declared current acceptance-carrier locations and the corresponding current CA-O-158/159/160 and CA-O-161/162/163 definitions. Historical acceptance carriers and their predecessor evidence remain unchanged provenance; their old Versions or digests are not executable current-rule gates.

Keep the existing acceptance-carrier identity/path bindings: CA-P-1618 at `.caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/29-CA-P-1618-TASK--accept-current-artifact-query-source-frontier.md`, and CA-P-1535 at the same declared parent with basename `15-CA-P-1535-TASK--accept-final-journal-query-source.md`. Resolve the named Operations definitions by their stable Atom IDs within the selected Project's registered Scope Unit authority paths and admitted content-role folders, including after a Core-to-Project Configuration move. On a fresh observation, a genuinely missing prior Carrier path may be resolved to the unique current original with that same ID. Do not substitute for an existing wrong-identity or unsafe Carrier, admit ambiguous identity claims, follow archived/draft/projected copies, or refresh a captured source inside an already admitted operation. Capture the actual resolved safe path, Version and SHA-256 for that observation. The acceptance Plan locations above remain fixed; this lookup grants no relocation or source-write authority.

Read and validate each current source's canonical identity, owning authority, safe declared path and supported contract. Capture its actual Version and SHA-256 as per-operation evidence and use those captured values consistently in the canonical manifest, route definitions and dispatch. Do not compare current sources to compiled historical Version/hash constants or infer semantic compatibility from a newer Version alone. Missing, ambiguous, malformed, unsupported or contradictory current authority refuses admission. No caller-provided rule bundle, guessed relocation or arbitrary path may replace that authority.

The two query admission records remain inside one canonical manifest, not another registry, authority, parser or executor. Before registration and dispatch, require complete source coverage and agreement with the current sources captured for that operation; changed source bytes or evidence require a new capture and validation before effects, not silent refresh of an approved request. Preserve exact target, proposal, permission and intent bindings, canonical manifest integrity and all source/path safety checks.

The only Release commands are `release_version` and `public.release`, bound in CA-D-547 to their existing simple local and public runners. Their closed direct requests are `{project_root, run_id}` and `{project_root, run_id, content_draft?}`, respectively; an absent public draft requests the explicit description/summary rather than performing publication. They do not use the selected D527 preview/execute envelope, candidate/N+1 pipeline or DBOS queue. The full test suite is verification before the requested local delivery or public publication; failure, unavailable execution or unknown completion stops that release. Required integration tests are included; missing Docker or another required test environment, or skipped required tests, stops release rather than satisfying verification. Release verification adds no separate Active Atom metadata, placement or relation validation; the full test suite and normal input, permission and file/path safety checks remain. Required Docker integration tests build a disposable image from the current code; an old installed or running image is not a substitute, and test execution does not restart the running Project MCP.

Neither direct Release command requires a separate whole-catalog, dependency-registry or Release-source-admission validation gate. They do not require D572/D613 admission records or a schema-6 registry extension merely to execute release. Normal explicit inputs, connected Project ownership, current source/file safety, existing Operator/client permissions, installation locking, actual installed readback and the public Git/PR permission boundary remain applicable. Local and public release never implicitly invoke each other. This exception removes only the extra Release registry/dispatch machinery; the full canonical manifest gate and query admission frontiers remain mandatory for the other selected routes. Historical Tasks remain provenance, not extra current Release approval gates.

Except for the narrow current O016 Version 18 Integrated pending/status/`submit_result` handoff described below, every non-Release selected route delegates one normalized CA-D-527 v3 request to shared
`run_selected_operation(request)`: request/route identity, typed
input/parameters, target-frontier and effects digests, caller-chosen
idempotency/retry key, optional real parent lineage, explicit current sealed
Initiative authorization for mutations, and exactly one outer
`definition_manifest` (`manifest_ref`, `manifest_digest`). That outer object is
the sole canonical manifest binding. `source_freshness` carries only current
selected-source registry/binding evidence; `definition_manifest_ref`,
`definition_manifest_digest`, or any other manifest ref/digest supplied there
or elsewhere are unknown shadow fields and are rejected, including if their
digest differs. For those general routes, it returns only the shared `RunResult`: real Run/definition IDs,
outcome, safe result/effect/report/output refs, actual supplied Journal observations and logging I/O diagnostics when present,
source currentness and diagnostics, without Journal-proof or completion prerequisites. `mode` defaults to
`preview`; preview creates no Run, Action Run, Event, mutation authority, or
Journal write. Only explicit `execute` may start work. A mutation-capable route
also requires its exact current Operator authorization. An admitted read-only
query may execute only with its exact current query-source admission, canonical
manifest, and explicit `execute` request; it gains no mutation authority. Its
actual Run/Action Run observations remain shared support's responsibility;
plain Journal append/read has no prior-history, chain, validation, receipt,
deduplication, recording retry or recovery prerequisite. No
`apply` mode exists.

Before shared support admits `find_and_fetch_journal_events`, the adapter must
capture and bind CA-O-163's sealed canonical Journal byte-prefix snapshot. The
actual Workflow/Action Run records are appended only after that capture and
cannot enter, enlarge, or replay the query result. Both query routes reuse the
one CA-R-1850 closed literal grammar and never accept SQL, code, arbitrary
expressions, secrets, or a second parser.

`get_selected_workflow_run` and `get_selected_action_run` read only one exact actual Run/Action Run and return its observed status, safe output/result/effect references, lineage, source currentness and actual logging diagnostics when present. Journal entries do not prove those source-effect outcomes. The obsolete `recover_selected_run_recording` route, canonical receipt prerequisite and recording-retry protocol are not admitted. Reading or repeated log rows never create another Run or replay an Action or Workflow. MCP must not implement a parallel request schema or execution path.

For the current source-bound `run_implementation_workflow`, the explicitly admitted current Integrated binding is the O016 Project Configuration Workflow at observed Version 18, limited to its eight Integrated Steps and the CA-O-231 entry, after the existing manifest/currentness/permission/assessment checks. Its direct APP/canonical RunTracker handoff may expose the current Step prompt, complete bound inputs, expected result contract and opaque one-use continuation while the Step remains pending: a prompt is not completion. The controlling session may perform or delegate the Step and call the same route with a closed `submit_result` packet whose inner fields are exactly `operation=submit_result`, `run_id`, `action_run_id`, `continuation_id`, and `result={result, outputs, evidence, blockers}`. The server owns continuation admission, result validation and digest/policy binding; callers cannot override policy. An exact duplicate returns the original response, while a conflicting, stale or oversized submission is refused without replay. Read-only status strips `capture.definitions`, exposes the actual retained recording diagnostics, and never recovers or replays work. With no checkpoint, read-only observation returns `not_observed` with the requested Run ID only; it never fabricates an actual root/Run start, prompt or recovery. A known graph-blocked terminal is reported by the public wrapper as `disposition=terminal`, `status=interrupted_pending`, `outcome=interrupted_pending`, `graph_result.outcome=interrupted_pending`, with the actual underlying `run_disposition=interrupted`; an unknown root or child interruption without bound canonical graph proof remains `interrupted_pending` with no prompt. Tampered or missing graph references refuse. O016 Version 17 retains its legacy projection and DBOS/queue dispatch path; Version 18 is the observed current admission, not a timeless `>=18` rule, and any future Version requires a fresh current compatible admission. No projection compilation gate is introduced.

The adapters reuse the server's existing Project-root/stdin binding, discovery helpers, `workflow_orchestrator`, and hot-reload gateway. CA-D-521's existing DBOS `enqueue_selected` variant remains the general selected-dispatch variant. The separate connected-process exception is a changed Subject-only `update_atom` execute request admitted under CA-R-866/CA-O-030: the existing outer connected MCP host may obtain the real Codex request/session form response and privately issue and consume its nonserializable one-use confirmation through the existing selected execution and shared Run/lifecycle service in that same process, without DBOS enqueue. All existing request/preview/manifest/currentness/permission/assessment/actual-Run/lock/source-effect checks remain required; plain Journal append/read is not approval, proof or a completion gate. Every remaining non-Release selected execution retains the existing APP queue path; the exception introduces no second executor or schema, standalone route, caller approval field or child/worker confirmation relay. The adapters add no alternate root, shell, arbitrary path, generic mutation, implicit dispatch, Journal writer, or duplicate business behavior. Existing discovery/context helpers and the two read-only Run observation routes remain available; no replacement recovery route is introduced. Route annotations truthfully describe preview/execute behavior and do not override client permission policy.

### Instructed Subjects-only batch dispatch

The exact packet uses the existing selected update route, request Initiative and Operator authorization from the actual instructed operation. Do not invoke an additional batch form, review/pause response, content-review round, confirmation receipt or fabricated approval; ordinary singleton confirmation remains unchanged. Reuse existing selected dispatch and updater, not another executor or Tool family. Derive public batch frontier/effects from packet metadata without initial intent-hash fields; fresh native intent stays internal where needed. Preserve normal target/draft/patch/layout, exact source, archive, Version/time and conditional-write/readback checks, not a redundant full-candidate validation gate. The caller composes current commit, bounded draft creation, draft commit, promotion and existing graph rebuild after completion, reporting actual results. Stop first failure/uncertainty and preserve completed/held/remaining sources without automatic batch rollback/replay/retry/resume; native failed-write handling remains.

### Sources

- Current CA-A-1142 selected registry; current CA-P-1618 and CA-P-1535 query admission carriers; current CA-O-164 and CA-D-547, the direct local Release binding; current CA-O-188, the direct public Release definition; CA-P-1622/CA-P-1869 retain historical acceptance provenance, not current runtime admission gates; CA-P-1117 v7 shared Run obligation.
- CA-D-527 v3; CA-D-521 v7; CA-D-548 v2; CA-R-1720 v19; CA-R-1525 v7; CA-R-1728 v16; CA-D-523 v2; CA-R-1850 v2; CA-R-1866 v3; CA-R-1867 v1.
- Current CA-O-016 Project Configuration Workflow (observed Version 18), CA-R-1527 Core Meta Model General, CA-R-1845 and CA-D-544 supply the Integrated prompt/continuation contract; CA-E-652 remains Workflow-level algorithm/evaluation authority, not an MCP admission gate.

The existing `atom_update` preparation Tool also binds CA-D-425's `stage_subject_batch` with closed `{operation, subject_batch: {path, digest}, limit?}`, strict limit1..10/default10, compact actual progress and final schema1 packet. This creates no canonical/history effect. Draft-backed packets bind every temporary-ID/Status proposal; map-only execution remains available. Existing request authorization admits subsequent exact promotion without an extra form/review/full-validation round. Restore canonical ID/original Status through normal writer checks; canonical ID grammar and ordinary `preview_subjects`/`stage_subjects` behavior are unchanged.
