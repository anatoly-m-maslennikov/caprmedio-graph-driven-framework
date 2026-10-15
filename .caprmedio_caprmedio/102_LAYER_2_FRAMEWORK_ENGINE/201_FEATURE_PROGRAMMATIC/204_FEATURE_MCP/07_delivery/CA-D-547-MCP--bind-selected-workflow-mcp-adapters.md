---
atom_id: CA-D-547
content_role: Delivery
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-14 19:54:14 +0400"
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
location. Its existing thirteen entries materialize CA-A-1142 v2's
already-reviewed current source registry unchanged. Its two additional entries
are `find_and_fetch_artifacts` and `find_and_fetch_journal_events`, admitted
only by the exact CA-P-1618@1 and CA-P-1535@2 source-frontier pins specified in
CA-R-1847@9. The manifest keeps those two acceptance pins in one
`query_source_admissions` field and includes their accepted CA-O-158/159/160
and CA-O-161/162/163 source pins in the corresponding route definitions under CA-R-1847's explicit relocation, O163@2-to-@3 structural-successor bridge and exact O163@4 plain-Journal reading amendment. The Done acceptance carriers retain their historical accepted revisions; no third proof or automatic current-source acceptance is added. It is
not a second graph authority and cannot select, replace, repair, or independently
admit a source.

For every non-Release selected route the manifest includes one exact source Workflow, its full
ordered Step list, its full ordered Action list, and only source-closed actual
native Action calls. Every definition entry carries its repository-relative
source path, Atom ID, Version, and SHA-256 digest. Its
`canonical_manifest_sha256` is the SHA-256 of RFC 8785 canonical JSON for the
whole object with that self field omitted; a server checks that canonical digest,
all original source pins, and both query admission frontiers before registration
and again before dispatch. Absent, incomplete, duplicate, malformed, altered,
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

For non-Release selected routes, the only connected-process exception is the existing `update_atom` changed Subject-only execute variant admitted by CA-R-866/CA-O-030. Its actual outer `hot_reload.py` Gateway request/session invokes the private `subject_publication_confirmation.py` handler, using host-owned exact request, Operator and staged-candidate bindings, then consumes the one-use confirmation through the same-process existing `selected_execution.py` selected/shared Run dispatch. It reuses all current request, source, preview, permission, assessment, lock, effect, restoration and actual Run outcome checks; plain Journal append/read remains observation, not a permission, proof or completion gate, and introduces no recording retry or recovery. It returns the unchanged shared RunResult. The confirmation is never a public field, serialized queue record or child-session correlation assertion. Other non-Release selected routes and generic updates retain the declared DBOS dispatch; the direct Release commands follow their separately stated runner boundary. This placement declaration grants no publication, runtime activation or guard removal.

Only the two declared read-only Run observation routes remain; the obsolete
`recover_selected_run_recording` route and Journal recording-retry protocol are
not admitted. This is a delivery declaration, not implementation acceptance:
this source-contract alignment does not by itself claim current route registration, query execution, functional verification, or immutable-image acceptance. The complete shared-registry gate remains mandatory only for non-Release selected routes; neither direct Release command depends on that gate.

### Direct local and public Release commands

`release_version` invokes the existing `PROJECT_TOOLS/RELEASE_VERSION/local_release.py:run_local_release` with the closed request `{project_root, run_id}`. `public.release` invokes the existing public runner with `{project_root, run_id, content_draft?}`; the draft contains exactly `description` and `summary`. A missing public draft requests that input rather than executing publication. Resolve only the connected selected Project; reject foreign roots, unknown fields and a request for the other release's effects.

These are the only two Release flows. They use their direct runner interface, not the old candidate-selection, selected-N suite, Full Gate aggregate, N+1 promotion, selected D527 preview/execute envelope or DBOS queue interface. Before local delivery or public publication, run the full test suite for the requested release and stop on a failed, unavailable or unknown result. Required integration tests are part of that suite; missing Docker or another required test environment stops release, and skipped required tests do not count as a pass. There is no additional whole-catalog, dependency-registry or Release-source-admission validation gate for either direct Release command. No schema-6 Release admission record, second registry or replacement validator is introduced to enable them. Release verification adds no separate Active Atom metadata, placement or relation validation; the full test suite and normal input, permission and file/path safety checks remain. Required Docker integration tests build a disposable image from the current code; an old installed or running image is not a substitute, and test execution does not restart the running Project MCP.

Normal explicit inputs, current source/file safety, existing Operator/client permissions, Project ownership, installation locking, preserved configuration and actual installed readback remain required. The public runner retains its own explicit draft and authorized public Git/PR boundary; it does not invoke the local release. The local runner does not invoke public release, push or open a PR. A logging failure reports its actual diagnostic independently of the observed release outcome; there is no Journal receipt, prior-history, deduplication, retry or recovery gate and no effect replay.

CA-O-164's current local flow retains four declared occurrences O170/O165, O172/O166, O173/O166 and O178/O169, while the runner performs the full-suite verification before delivery. CA-O-188 owns public release. CA-D-561, the retained-ID CA-D-562 and replacement CA-D-633 preserve the local compilation, runtime installation and complete Skill delivery; D563 is retired only after D633 is active. Keep exact predecessor source history and record only the actual D562 update and D563 replacement, without synthetic baselines or a logging prerequisite for source adoption. Archived D572/D566/D567/D571 and obsolete candidate/handoff formats are not current Release gates.

These direct commands do not weaken the complete manifest/source/currentness/permission gate for the other selected capabilities or their query admissions. Source declarations are not a runtime pass, permission to activate MCP, or authority to publish the current staged changes.

### Sources

- CA-R-1847 v9; CA-R-1848 v5; CA-E-567 v4; CA-E-568 v5.
- CA-A-1142 v2; CA-P-1618 v1; CA-P-1535 v2; CA-D-527 v3; CA-D-521 v7; CA-D-548 v2; CA-D-523 v2.
