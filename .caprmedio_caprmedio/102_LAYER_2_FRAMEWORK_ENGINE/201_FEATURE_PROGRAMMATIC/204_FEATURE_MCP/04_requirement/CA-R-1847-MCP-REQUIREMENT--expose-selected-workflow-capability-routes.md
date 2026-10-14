---
atom_id: CA-R-1847
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: "2026-10-14 19:54:14 +0400"
subjects:
  governs: "MCP/selected Workflow capability routes"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal]
relations: {}
---
# Summary

Expose selected Workflow capability routes

## Scope

The Project-local MCP adapter surface for the original thirteen Operator-selected
P1117 capabilities, two explicitly admitted read-only P1520 query Workflows,
and separately admitted Release Version and PUBLIC_RELEASE Workflows.

## Claim

MCP **must** expose only the capability adapters admitted below through the existing reloadable Project-local server. Non-Release selected routes delegate execution and actual Run observations to shared `WORKFLOW_OPERATIONS/RUN_SUPPORT`; local **and** public Release use their existing direct runners.

## Details

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

The original thirteen entries retain CA-A-1142 v2 as their unchanged selected
source registry and retain its closed source policies. The two query entries
are admitted only by `query_source_admissions` in that same canonical manifest;
that field contains exactly these current acceptance-frontier pins and their
corresponding Workflow/Action/Step pins:

- `find_and_fetch_artifacts`: CA-P-1618@1 at
  `.caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/29-CA-P-1618-TASK--accept-current-artifact-query-source-frontier.md`, SHA-256 `bdf10c928c10c102dc489c8e3e526ffe73e8a33d492f4dabc8b5d0129c453b1f`; CA-O-158@4 `d7fdaebdd1d0c6ca7dac9aced25552c487336f2a51f18c0f03ef65d16ff4618a`, CA-O-159@2 `3fd33badbff039e58c1c0b31dfbf3608c37a58d779a1b3ebc14d7bb5ee27dc08`, and CA-O-160@2 `a743a84fd24db32123ac8162e7a2178e6d83b1b727cbe54477b6020914537384` at the current declared Core Operations paths bound below.
- `find_and_fetch_journal_events`: CA-P-1535@2 at
  `.caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/15-CA-P-1535-TASK--accept-final-journal-query-source.md`, SHA-256 `6246b46d2961d795e29eeb224f01b14979434d4ad24cf3f4913c490268cf52dc`; CA-O-161@2 `362b9d3848a796a14e7374cfa0bf0b561c4f2035b7b2bf87bd9b56fc97a6724d`, CA-O-162@2 `71301ecf9531c70adeba03d6cf7f39761a237a081cee43eb0f9f7ce40e12f9fe`, and CA-O-163@4 `1e47a2e59581a18cc0869efedfeefb6474a404ce5f761123a1c65718726f3727` at the current declared Core Operations paths bound below.

The Done P1618@1 and P1535@2 receipts remain unchanged historical source acceptance, not runtime or image proof. P1618 accepted O158@4/O159@2/O160@2; P1535 accepted O161@2/O162@2 and O163@2 (`8d0238a1614f5888f2aa486038d271cc58db1d3f0d7014dece0baa53004a489c`), not O163@3. The full shared-registry repair retains exactly those two acceptance-frontier pins and explicitly admits their byte-identical source-path relocations plus the structurally repaired O163@3 successor (`0090078ce32293b84a1233ecc33d2fafc1b9541e7821ecc2388e8137b009b86a`). The O163 predecessor and successor differ only in Version and update time; Operation body and Subjects are unchanged. The exact predecessor archive/current source comparison and structural-repair consumer receipt must be preserved in the repair evidence. The Operator's subsequent plain-Journal decision separately admits exact O163@4 (`1e47a2e59581a18cc0869efedfeefb6474a404ce5f761123a1c65718726f3727`): its query Step retains immutable prefix/member coverage, literal grammar, limits, privacy and Project authority while removing Journal-row validation and unique-ID prerequisites. O163@3 and the Done acceptance carriers remain exact historical evidence, not proof that P1535 accepted the semantic @4 amendment. Preserve the exact @3 predecessor bytes; this explicit current binding is not automatic newer-source substitution or a query-only manifest gate.

Current O158/O159/O160/O161/O162 paths use `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/09_operations/` with their existing exact basenames, Versions and digests. Current O163@4 uses that directory's `CA-O-161-CORE_META_MODEL-WORKFLOW--find-and-fetch-journal-events/CA-O-163-CORE_META_MODEL-STEP--query-the-stable-journal-event-snapshot.md`. The adapter's exact accepted specification, manifest query records and corresponding route pins must agree. This explicit repair bridge does not permit arbitrary future revisions; complete shared-registry validation remains required before registration and dispatch.

The two acceptance pins are explicit admission evidence, not a second registry,
authority, manifest, parser, or executor. Missing, malformed, incomplete,
duplicate, digest-mismatched, or stale bindings or admissions reject the route
before shared support, worker start, Run creation, Action Run creation, effect,
or Journal event.

The only Release commands are `release_version` and `public.release`, bound in CA-D-547 to their existing simple local and public runners. Their closed direct requests are `{project_root, run_id}` and `{project_root, run_id, content_draft?}`, respectively; an absent public draft requests the explicit description/summary rather than performing publication. They do not use the selected D527 preview/execute envelope, candidate/N+1 pipeline or DBOS queue. The full test suite is verification before the requested local delivery or public publication; failure, unavailable execution or unknown completion stops that release. Required integration tests are included; missing Docker or another required test environment, or skipped required tests, stops release rather than satisfying verification. Release verification adds no separate Active Atom metadata, placement or relation validation; the full test suite and normal input, permission and file/path safety checks remain. Required Docker integration tests build a disposable image from the current code; an old installed or running image is not a substitute, and test execution does not restart the running Project MCP.

Neither direct Release command requires a separate whole-catalog, dependency-registry or Release-source-admission validation gate. They do not require D572/D613 admission records or a schema-6 registry extension merely to execute release. Normal explicit inputs, connected Project ownership, current source/file safety, existing Operator/client permissions, installation locking, actual installed readback and the public Git/PR permission boundary remain applicable. Local and public release never implicitly invoke each other. This exception removes only the extra Release registry/dispatch machinery; the full canonical manifest gate and query admission frontiers remain mandatory for the other selected routes. Historical Tasks remain provenance, not extra current Release approval gates.

Every non-Release selected route delegates one normalized CA-D-527 v3 request to shared
`run_selected_operation(request)`: request/route identity, typed
input/parameters, target-frontier and effects digests, caller-chosen
idempotency/retry key, optional real parent lineage, explicit current sealed
Initiative authorization for mutations, and exactly one outer
`definition_manifest` (`manifest_ref`, `manifest_digest`). That outer object is
the sole canonical manifest binding. `source_freshness` carries only current
selected-source registry/binding evidence; `definition_manifest_ref`,
`definition_manifest_digest`, or any other manifest ref/digest supplied there
or elsewhere are unknown shadow fields and are rejected, including if their
digest differs. It returns only the shared `RunResult`: real Run/definition IDs,
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

The adapters reuse the server's existing Project-root/stdin binding, discovery helpers, `workflow_orchestrator`, and hot-reload gateway. CA-D-521's existing DBOS `enqueue_selected` variant remains the general selected-dispatch variant. For non-Release selected routes, the sole connected-process exception is a changed Subject-only `update_atom` execute request admitted under CA-R-866/CA-O-030: the existing outer connected MCP host may obtain the real Codex request/session form response and privately issue and consume its nonserializable one-use confirmation through the existing selected execution and shared Run/lifecycle service in that same process, without DBOS enqueue. All existing request/preview/manifest/currentness/permission/assessment/actual-Run/lock/source-effect checks remain required; plain Journal append/read is not approval, proof or a completion gate. Every other non-Release selected execution retains the existing APP queue path; the exception introduces no second executor or schema, standalone route, caller approval field or child/worker confirmation relay. The adapters add no alternate root, shell, arbitrary path, generic mutation, implicit dispatch, Journal writer, or duplicate business behavior. Existing discovery/context helpers and the two read-only Run observation routes remain available; no replacement recovery route is introduced. Route annotations truthfully describe preview/execute behavior and do not override client permission policy.

### Sources

- CA-A-1142 v2, unchanged original-thirteen registry; CA-P-1618 v1 and CA-P-1535 v2, the exact two query admission frontiers; current CA-O-164 and CA-D-547, the direct local Release binding; current CA-O-188, the direct public Release definition; CA-P-1622/CA-P-1869 retain historical acceptance provenance, not current runtime admission gates; CA-P-1117 v7 shared Run obligation.
- CA-D-527 v3; CA-D-521 v7; CA-D-548 v2; CA-R-1720 v19; CA-R-1525 v7; CA-R-1728 v16; CA-D-523 v2; CA-R-1850 v2; CA-R-1866 v3; CA-R-1867 v1.
