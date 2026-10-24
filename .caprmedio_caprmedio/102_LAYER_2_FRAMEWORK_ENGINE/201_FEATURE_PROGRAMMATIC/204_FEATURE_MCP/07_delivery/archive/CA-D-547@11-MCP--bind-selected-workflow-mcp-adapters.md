---
atom_id: CA-D-547@11
content_role: Delivery
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 11
updated_at: "2026-10-22 23:55:40 +0400"
subjects:
  governs: "MCP/selected Workflow adapter Carrier"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal, Projection, Project]
relations:
  delivery_for: [CA-R-1847, CA-R-1848]
---
# Summary

Bind selected Workflow MCP adapters

## Scope

The declared delivery location and public request contract for selected MCP adapters.

## Claim

The adapter surface **must** be implemented in one Project-local MCP binding. Non-Release selected routes delegate to shared Run support; the two direct Release commands invoke their existing local **or** public runner under the boundary below.

## Details

`project_mcp.tool_blacklist` is an optional list of exact MCP tool names; an absent list means no names are blocked. A listed name is omitted from tool discovery and refused at invocation before its handler runs, including cached or direct calls. This Project lists `release_version` and `public.release`: their existing adapters, runner bindings and request contracts remain available in source for later reuse, but neither tool is exposed or callable through MCP. The route declarations and direct requests below retain their implementation bindings; exposure always obeys the Project blacklist. Current release invocation uses repository-host `PROJECT_TOOLS/release.py local|public`, with `--project-root`, required `--run-id`, and optional public `--content-draft` JSON containing exactly `description` and `summary`. Missing public content returns `input_required` without publication. Existing plain Journal logging reports actual observations; `recording_error` is independent of the release outcome and never requests replay.

```toml
[selected_workflow_mcp]
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/implementation_server.py"
adapter_module = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_routes.py"
shared_service = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/workflow_run_support.py"
execute_dispatch = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/orchestrator.py:enqueue_selected"
binding_manifest = ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
canonical_manifest_binding = "request.definition_manifest.{manifest_ref,manifest_digest}"
routes = ["create_atom", "update_atom", "replace_atom", "change_atom_status", "create_scope_unit", "rename_scope_unit", "move_scope_unit", "remove_scope_unit", "run_implementation_workflow", "revert_changes", "build_entities_graph", "build_terms_graph", "build_applicable_methodology", "find_and_fetch_artifacts", "find_and_fetch_journal_events", "release_version", "public.release"]
observation_routes = ["get_selected_workflow_run", "get_selected_action_run"]
```

`selected_workflow_bindings.json` is the one derived immutable per-route
Projection manifest. It resides in the selected Project's registered
`_projection/` root; the MCP implementation code retains its Engine delivery
location. Its existing thirteen entries resolve the current CA-A-1142 selected registry. The two query entries resolve current CA-P-1618 and CA-P-1535 acceptance carriers and their current Workflow/Action/Step sources under CA-R-1847. One `query_source_admissions` field captures those actual source identities, Versions, safe declared paths and SHA-256 digests for the operation. Historical acceptance and relocation evidence stays preserved; it is not a fixed old-Version/hash gate. Resolve and validate current authority and supported contracts rather than substituting caller rules or assuming any newer source is compatible. This manifest is not another graph authority and cannot select, replace or repair a source.

For every non-Release selected route the manifest includes one exact source Workflow, its full
ordered Step list, its full ordered Action list, and only source-closed actual
native Action calls. Every definition entry carries its repository-relative
source path, Atom ID, Version, and SHA-256 digest. Its
`canonical_manifest_sha256` is the SHA-256 of RFC 8785 canonical JSON for the
whole object with that self field omitted; a server checks that canonical digest,
all captured current source pins, and both current query admission frontiers before registration
and again before dispatch. Source evidence is captured from current authoritative
files per operation, not compared to compiled historical Version/hash constants. Absent, incomplete, duplicate, malformed, altered,
or stale manifests reject without shared-support invocation, Run, Action Run,
worker, effect, Event, or Journal write.

Each non-Release selected route adapts to, rather than redefines, `run_selected_operation(request)`.
Its shared request contains route/operation identity, typed input/parameters, an
idempotency/retry key, real parent lineage only, and exactly the outer canonical
`definition_manifest` (`manifest_ref`, `manifest_digest`). A mutation also
contains explicit current sealed Initiative authorization. `source_freshness`
retains only selected-source registry/binding evidence; a manifest ref/digest
there or anywhere else is a shadow unknown field and is rejected, whether
matching or different. Its shared `RunResult` contains real Run/definition IDs,
outcome, result/effect/report/output refs, actual supplied Journal observations and logging I/O diagnostics when present,
currentness and diagnostics, without Journal-proof or completion prerequisites. Non-Release selected MCP routes use `mode` defaulting to `preview`; preview
has no Run/Event, and only explicit `execute` may request selected dispatch. An admitted
read-only query execute has no mutation authority; it is source-bound to its
canonical manifest and acceptance frontier. For the Journal route, capture the
CA-O-163 source token before shared support can record its own Run/Event.
CA-D-521 v7's existing `enqueue_selected` remains the accepted general DBOS
dispatch variant: the adapter reuses the existing APP and does not introduce an
executor. Unknown fields, raw filesystem/shell instructions, mixed route
capability, alternate root, `apply`, or execute without its required exact
authorization/admission are errors or blocked outcomes.

For the current source-bound `run_implementation_workflow`, the explicitly
admitted connected-session binding is the Project Configuration Workflow
CA-O-016 at observed Version 18, limited to its eight Integrated Steps and
CA-O-231 entry after the existing manifest/currentness/permission checks. It
uses the existing APP and canonical RunTracker: a pending response carries the
current Step prompt, complete bound inputs, expected result contract and
opaque one-use continuation, and does not claim completion. The controlling
session may perform or delegate the Step and submit through the same route
with the closed inner fields `operation=submit_result`, `run_id`,
`action_run_id`, `continuation_id`, and
`result={result, outputs, evidence, blockers}`. The server owns admission,
validation and digest/policy binding; exact duplicates return the original
response, conflicting/stale/oversized submissions refuse, and no effect is
replayed. Read-only status strips `capture.definitions`, exposes retained
recording diagnostics and never recovers or replays work. With no checkpoint, read-only observation returns `not_observed` with the requested Run ID only; it never fabricates an actual root/Run start, prompt or recovery. A known graph-blocked
terminal must expose the exact wrapper/canonical Run tuple
`disposition=terminal`, `status=interrupted_pending`,
`outcome=interrupted_pending`, `graph_result.outcome=interrupted_pending`,
and `run_disposition=interrupted`; unknown root/child interruption without
bound canonical graph proof stays `interrupted_pending` with no prompt, while
tampered/missing graph refs refuse. O016 Version 17 remains the legacy
projection/direct-runtime compatibility path; Version 18 is the observed
current admission, not a timeless `>=18` rule, and a future Version requires
fresh current compatible admission. This delivery declaration adds no
projection compilation gate or Journal completeness permission gate, and no
new Tool, executor or registry.

The separate connected-process exception is the existing `update_atom` changed Subject-only execute variant admitted by CA-R-866/CA-O-030. Its actual outer `hot_reload.py` Gateway request/session invokes the private `subject_publication_confirmation.py` handler, using host-owned exact request, Operator and staged-candidate bindings, then consumes the one-use confirmation through the same-process existing `selected_execution.py` selected/shared Run dispatch. It reuses all current request, source, preview, permission, assessment, lock, effect, restoration and actual Run outcome checks; plain Journal append/read remains observation, not a permission, proof or completion gate, and introduces no recording retry or recovery. It returns the unchanged shared RunResult. The confirmation is never a public field, serialized queue record or child-session correlation assertion. All remaining non-Release selected routes and generic updates retain the declared DBOS dispatch; the direct Release commands follow their separately stated runner boundary. This placement declaration grants no publication, runtime activation or guard removal.

Only the two declared read-only Run observation routes remain; the obsolete
`recover_selected_run_recording` route and Journal recording-retry protocol are
not admitted. This is a delivery declaration, not implementation acceptance:
this source-contract alignment does not by itself claim current route registration, query execution, functional verification, or immutable-image acceptance. The complete shared-registry gate remains mandatory only for non-Release selected routes; neither direct Release command depends on that gate.

### Instructed Subjects-only batch dispatch

The exact packet uses the existing selected update route, request Initiative and Operator authorization from the actual instructed operation. Do not invoke an additional batch form, review/pause response, content-review round, confirmation receipt or fabricated approval; ordinary singleton confirmation remains unchanged. Reuse existing selected dispatch and updater, not another executor or Tool family. Derive public batch frontier/effects from packet metadata without initial intent-hash fields; fresh native intent stays internal where needed. Preserve normal target/draft/patch/layout, exact source, archive, Version/time and conditional-write/readback checks, not a redundant full-candidate validation gate. The caller composes current commit, bounded draft creation, draft commit, promotion and existing graph rebuild after completion, reporting actual results. Stop first failure/uncertainty and preserve completed/held/remaining sources without automatic batch rollback/replay/retry/resume; native failed-write handling remains.

### Retained direct local and public Release bindings

`release_version` invokes the existing `PROJECT_TOOLS/RELEASE_VERSION/local_release.py:run_local_release` with the closed request `{project_root, run_id}`. `public.release` invokes the existing public runner with `{project_root, run_id, content_draft?}`; the draft contains exactly `description` and `summary`. A missing public draft requests that input rather than executing publication. Resolve only the connected selected Project; reject foreign roots, unknown fields and a request for the other release's effects.

These are the only two Release flows. They use their direct runner interface, not the old candidate-selection, selected-N suite, Full Gate aggregate, N+1 promotion, selected D527 preview/execute envelope or DBOS queue interface. Before local delivery or public publication, run the full test suite for the requested release and stop on a failed, unavailable or unknown result. Required integration tests are part of that suite; missing Docker or another required test environment stops release, and skipped required tests do not count as a pass. There is no additional whole-catalog, dependency-registry or Release-source-admission validation gate for either direct Release command. No schema-6 Release admission record, second registry or replacement validator is introduced to enable them. Release verification adds no separate Active Atom metadata, placement or relation validation; the full test suite and normal input, permission and file/path safety checks remain. Required Docker integration tests build a disposable image from the current code; an old installed or running image is not a substitute, and test execution does not restart the running Project MCP.

Normal explicit inputs, current source/file safety, existing Operator/client permissions, Project ownership, installation locking, preserved configuration and actual installed readback remain required. The public runner retains its own explicit draft and authorized public Git/PR boundary; it does not invoke the local release. The local runner does not invoke public release, push or open a PR. A logging failure reports its actual diagnostic independently of the observed release outcome; there is no Journal receipt, prior-history, deduplication, retry or recovery gate and no effect replay.

CA-O-164's current local flow retains four declared occurrences O170/O165, O172/O166, O173/O166 and O178/O169, while the runner performs the full-suite verification before delivery. CA-O-188 owns public release. CA-D-561, the retained-ID CA-D-562 and replacement CA-D-633 preserve the local compilation, runtime installation and complete Skill delivery; D563 is retired only after D633 is active. Keep exact predecessor source history and record only the actual D562 update and D563 replacement, without synthetic baselines or a logging prerequisite for source adoption. Archived D572/D566/D567/D571 and obsolete candidate/handoff formats are not current Release gates.

These direct commands do not weaken the complete manifest/source/currentness/permission gate for the other selected capabilities or their query admissions. Source declarations are not a runtime pass, permission to activate MCP, or authority to publish the current staged changes.

### Sources

- Current CA-R-1847, CA-R-1848, CA-E-567 and CA-E-568.
- Current CA-A-1142, CA-P-1618 and CA-P-1535; CA-D-527 v3; CA-D-521 v7; CA-D-548 v2; CA-D-523 v2.
- Current CA-O-016 Project Configuration Workflow (observed Version 18), CA-R-1527 Core Meta Model General, CA-R-1845 and CA-D-544 supply the Integrated prompt/continuation contract; CA-E-652 remains Workflow-level algorithm/evaluation authority, not an MCP admission gate.

The existing `atom_update` preparation Tool also binds CA-D-425's `stage_subject_batch` with closed `{operation, subject_batch: {path, digest}, limit?}`, strict limit1..10/default10, compact actual progress and final schema1 packet. This creates no canonical/history effect. Draft-backed packets bind every temporary-ID/Status proposal; map-only execution remains available. Existing request authorization admits subsequent exact promotion without an extra form/review/full-validation round. Restore canonical ID/original Status through normal writer checks; canonical ID grammar and ordinary `preview_subjects`/`stage_subjects` behavior are unchanged.
