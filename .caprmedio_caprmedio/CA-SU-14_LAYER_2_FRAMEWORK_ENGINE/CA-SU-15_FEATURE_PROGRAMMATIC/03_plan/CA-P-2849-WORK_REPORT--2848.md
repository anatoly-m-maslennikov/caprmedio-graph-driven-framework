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

The pre-retirement checkpoint is `3491118b5b`. The main retirement checkpoint is
`c5a2727db6`. Both were pushed to `amm/dev`.
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
At the main retirement checkpoint, deletion included 54 old orchestrator runtime modules, 92 exclusive app tests
and helpers, 78 MCP files, 396 Tool files, and 3,074 obsolete tracked package-copy files. Tool
counts include the old graph implementation and its obsolete fixtures/tests;
these categories must not be added a second time. Retained shared helpers were
checked against actual consumers rather than preserved as compatibility APIs.

No full-suite rerun, Docker build, release or deployment was performed. The
main retirement was pushed as `c5a2727db6`; the audit cleanup below remains local.
Methodology/source Atom reconciliation and installed-runtime replacement remain
separate work.

### Audit cleanup after the main checkpoint

Removed four unreferenced config/prompt files, three unused validator authority manifests, and 161 orphan workflow-fixture files with five exclusive helpers. The retained Graph Rule loader now reads only its required schema authority manifest. Stale validator, release and shared-MCP documentation was reconciled with the current code.

Runtime package and Docker inputs exclude Programmatic tests, fixtures and prose Markdown while preserving implementation Skills, schemas, frontend/build assets, methodology sources and compiled methodology. Workbench resource acceptance mounts the host test directory read-only. Two scope-declaration fixture helpers that live outside test directories are also excluded from runtime packaging while remaining available to host tests. The full-suite runner no longer invokes the deleted legacy launcher CLI.

Fixed the missed retained-test imports of deleted status/admission modules and Docker bridge code. Removed the exclusively retired admission/archive/route test cases instead of restoring their implementation. A final AST scan across canonical production and test files found no import of a uniquely deleted module.

Focused verification: 161 Subject-builder tests; MCP frontier 1; Project context 4; Workbench source reader 33; Graph Rule body 24 and declaration sources 12; package 29; runner 13 + 8 + 4; resource harness 1; image override 3; release CLI 13; public release 3. The live-canary module passed its fixture case with the live probe explicitly skipped. The single-root context test passed host-native after a sandbox FSEvents failure. These are focused checks, not a full-suite or built-image acceptance claim.

### Report and inventory relocation

The five loose reports became Analysis Report Atoms: [CA-A-1330](../../../02_analysis/CA-A-1330-ANALYSIS_REPORT--review-449-plans-semantic-adjudication.md), [CA-A-1331](../../../02_analysis/CA-A-1331-ANALYSIS_REPORT--assess-harness2-fit-for-caprmedio.md), [CA-A-1332](../../../02_analysis/CA-A-1332-ANALYSIS_REPORT--harvest-development-quality-gates.md), [CA-A-1333](../../../02_analysis/CA-A-1333-ANALYSIS_REPORT--challenge-subject-model-candidate-10.md), [CA-A-1334](../../../02_analysis/CA-A-1334-ANALYSIS_REPORT--challenge-formal-model-specification-proposal.md). Their original report bytes are preserved in Details; the original root paths were removed. Historical self-references inside the preserved report text were left as evidence.

The frontend Draft-ownership inventory is preserved as [CA-PROJ-027](../../../_projection/CA-PROJ-027-FEATURE_WORKBENCH_FRONTEND--Map--Historical-P2724-Draft-Inventory.md), a historical Map pinned to its exact source bytes in `c5a2727db6`. It was not rebuilt against Current Atoms.

Remaining limits: follow-up cleanup is local and has not been pushed, built, released or deployed. Production and its older installed package remain unchanged.
