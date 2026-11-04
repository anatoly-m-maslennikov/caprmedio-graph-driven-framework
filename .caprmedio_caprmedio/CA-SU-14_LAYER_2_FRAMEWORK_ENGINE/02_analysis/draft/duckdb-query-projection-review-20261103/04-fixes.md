# DuckDB query Projection — adopted MVP contracts

Updated: 2026-11-03

The 27-Atom packet is Current: 22 Engine Atoms under WORKBENCH and five Core receiving-rule revisions. [CA-A-1316](../../done/CA-A-1316-FRAMEWORK_ENGINE-SPECIFICATION_PROPOSAL--query-atoms-through-a-synchronized-duckdb-projection.md) is Done, version 4. Its index uses only Atom IDs and contains those 27 Atoms plus the WORKBENCH Declaration.

| Decision | Applied result |
| --- | --- |
| Two tables only | D672 defines `atoms` and `scope_units`; mapped Markdown and typed relations are nested values. |
| Role boundaries | R defines outcomes; M records engineering choices, including DuckDB; D defines delivered schema and MCP/web integration; E defines test cases; O defines the two direct technical processes. |
| Synchronous queries | Run and Check return through the originating MCP/web request. No query planner, scheduler, orchestrator, job queue or Workflow/Step wrappers. O242–O245 Drafts were withdrawn. |
| Source errors | Exclude failed input, report to stderr and continue with valid sources; no automatic retry or stale-row fallback. |
| Technical activity | Query/index work uses stdout/stderr without business-Journal entries. Normal source-change and business history remain. |
| WORKBENCH | GRAPH_SERVER was renamed without creating a Scope Unit: CA-SU-43 remains under APPS. Authority and Delivery folders and affected Current references were updated. The app includes backend and frontend; editing remains future work. |
| Lifecycle | Promoted files have base Header IDs and Current filenames. Five Core predecessors and the rename/adoption predecessors were archived. Existing historical content was retained. |

## Verification

- All 47 changed Current source hashes match the publication manifest.
- The Declaration reader returns 44 Scope Units including the Project root, WORKBENCH / CA-SU-43, and no GRAPH_SERVER entry.
- All 28 proposal-index links resolve. Packet links and typed targets resolve to Current sources.
- Independent read-only review found no introduced blocking regression.
- MCP appended 52 actual source-change/rename observations successfully to `Codex-2026-11-03-part-1.ndjson`, lines 7–58. These are source changes, not fabricated query or Workflow Runs.
- The unrelated historical C283 links were already broken in its predecessor; they were not repaired as part of this rename.

## Remaining implementation

DuckDB dependency/image wiring, the section-aware per-source reader, background index maintenance, synchronous SQL/expand connector, MCP Run/Check and the web page remain implementation work. No runtime SQL or container feature test was run, and no release was performed.

Custom views, renderer, arbitrary CFEL evaluation, retry machinery and query orchestration remain outside the MVP. WORKBENCH editing is future work.
