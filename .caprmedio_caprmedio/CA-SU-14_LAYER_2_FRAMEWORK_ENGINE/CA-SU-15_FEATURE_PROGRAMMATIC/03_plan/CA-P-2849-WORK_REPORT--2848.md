---
identity:
  id: CA-P-2849
  ref_id: CA-P-2849
context:
  container:
    scope_unit: CA-SU-15
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-09 23:57:47 +0400
destination:
  file:
    name: CA-P-2849-WORK_REPORT--2848.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan
author: Anatoly Maslennikov
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2848
---

## Summary

Minimum runtime after legacy Tool retirement

## Details

The checkpoint before retirement is commit `3491118b5b`, pushed to `amm/dev`.
This change retires code first. It does not claim that source Atoms have been
reconciled, that an installed runtime has changed, or that a release has run.

### Retained entry points

- The shared MCP exposes the 28 native Workbench query, Workspace, View and
  service tools. Legacy Tool discovery, mutation, selected execution, orchestration,
  reversal and public Journal-appender interfaces are removed.
- `FEATURE_PROJECT_TOOLS/release.py local` and `public` remain host commands.
- `FEATURE_TOOLS/GENERATE_ENTITY_GRAPH/render_entity_tree.py` and
  `render_contract_graph.py` retain standalone views.
- `FEATURE_TOOLS/GENERATE_ENTITY_GRAPH/render_subject_projections.py` renders
  one explicitly selected current Subject/Topics view to stdout: primary tree,
  direct properties, inherited contracts, formal claims, passive-only Subjects,
  missing declarations, or entity coverage. It does not invoke an old Run engine.

### Reasons to retain shared code

| Boundary | Actual retained consumer | Disposition |
|---|---|---|
| Header/YAML and Subject parsing | Workbench source indexing and Subject builders | Keep the safe shared parser, aliases, duplicate/resource checks and notation. |
| Bounded filesystem reads and Project/Scope settings | Workbench isolation, source indexing and host launchers | Keep the direct no-symlink/bounded read and selection closure. |
| Graph declaration checks | Declaration/contract views | Keep exact-source rule admission; parsing alone does not grant admission. |
| Journal persistence | Workbench saved-query changes and host release events | Keep internal append/settings functions; remove old public appender and execution recovery. |
| Release packaging and runtime launch | Local/public host release and Workbench container | Keep current bootstrap, schema/relation assets and image/runtime support. Remove old Tool registry/catalog and worker stages. |
| Compiler | Local release's Applicable Methodology output | Keep the direct compilation library; remove Tool requests, Action adapters, CLI, export utility and expansion validator. |
| Frozen test inputs | Retained parser/settings/Project tests | Keep only where a retained test needs independent replay inputs; these are not runtime providers. |

Workbench now reads its two required settings through `project_settings_values`,
without importing the retired Atom-mutation or artifact-query implementations.
Workbench result hashes remain public row hashes; no new claim of source-byte
evidence is introduced.

The shared metadata/Header modules now provide reads and the atomic output
writer required by graph rendering. Atom revision CLI, scalar YAML authoring,
nested Header authoring and Journal dispatch/recovery/query APIs are removed.
Journal inspection used only by tests lives in the test module.

The gateway runs Workbench directly in one process. No implementation child,
provider registry, hot-reload controller, workflow queue, worker or Agent service
is retained. Docker/package inputs exclude the old Agentic prompts; their source
tree remains repository-only because automatic approval review rejected its
broad deletion. The canonical `ca` skill remains packaged for Workbench access.

### Verification

Focused checks passed for the 28-tool MCP frontier and retired-call refusal,
Workbench source reads, Workspace/query/View operation, shared Project isolation,
HTTP health/error boundaries, and native restart. The retained Subject/Topics
suite passed all 161 tests. Graph Rule payload guards passed 24 tests with the
same Tools import path supplied by the test runner.

After shared-helper pruning, all 65 final boundary tests passed: MCP frontier,
Graph Rule guards, settings getters, Workbench source reads and saved queries.
The helper owner passed 27 focused Header, append and release-event tests;
another 22 error-boundary/diagnostic tests passed. Malformed Header validation
and append-path symlink protection remain enforced.

Host release/package checks passed: 23 focused compiler tests, 29 local-release
tests and 25 retained
Docker/runtime/image tests, including exclusion of old prompts and preservation
of the Workbench schema, Subject builder and `ca` skill. Lock validation resolves
43 packages. Strict Mypy passes for its two declared Header modules; this is not
a whole-project typing claim.

Canonical Programmatic Python files outside test directories decreased from
345 to 140. The final AST scan found no production import of a deleted module.
Deletion includes 54 old orchestrator runtime modules, 92 exclusive app tests
and helpers, 78 MCP files, 396 Tool files, and 3,074 obsolete tracked package-copy files. Tool
counts include the old graph implementation and its obsolete fixtures/tests;
these categories must not be added a second time. Retained shared helpers were
checked against actual consumers rather than preserved as compatibility APIs.

No full-suite rerun, Docker build, release or deployment was performed. The
retirement remains local; only the pre-retirement checkpoint was pushed.
Methodology/source Atom reconciliation and installed-runtime replacement remain
separate work.
