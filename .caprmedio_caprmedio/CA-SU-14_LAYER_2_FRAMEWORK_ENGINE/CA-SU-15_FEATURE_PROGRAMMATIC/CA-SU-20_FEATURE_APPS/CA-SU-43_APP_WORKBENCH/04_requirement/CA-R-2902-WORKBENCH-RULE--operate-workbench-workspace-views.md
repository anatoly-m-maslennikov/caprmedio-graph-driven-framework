---
identity:
  atom_id: CA-R-2902
  ref_id: CA-R-2902
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Rule
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Workspace
    dependencies:
    - MODEL//CAPRMEDIO <+ View
    - MODEL//CAPRMEDIO <+ Project
  tier: 3
state:
  status: Active
  version: 8
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2902-WORKBENCH-RULE--operate-workbench-workspace-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-476
  - CA-D-681
---

## Summary

Operate Workbench Workspace Views

## Claim

### Prose Claim

Workspace handling **must** use one shared Workbench backend. Native mode requires a host-supplied native thread reference; standalone browser mode uses a browser-owned Workspace ID without a native chat. Neither mode creates a second conversation history.

An explicit `workspace_open` initialization **must** use the selected mode’s required context and return that Workspace’s state. Binding occurs only after trusted Project context, the mode-specific required input and that result are available. Missing context is a binding error: it **must not** issue backend calls, infer identity from a URL or localStorage, invent a native thread or session ID, select another Workspace or Project, or open a Workspace again.

Each Workspace is isolated by its explicit Project and mode-appropriate Workspace context and has at least one Tab (historical API name View). `workspace_open` initializes or resumes only that context’s Workspace. Except for this explicit initialization, unknown Workspace or View IDs **must** return an error and **must not** silently select another context or Project. Existing standalone browser drafts and their localStorage session remain standalone-only and **must not** be silently migrated into a native Workspace.

The backend **must** provide only the minimum operations needed to list known Workspaces for an explicit Project, get a Workspace by ID and explicitly initialize or open a Workspace in the selected mode. Each View **must** have a stable string ID. Create and list operations **must** return View IDs, and every operation on one View **must** take its explicit View ID. Workspace state and standalone browser autosave and restore **must** be keyed by Project and the applicable Workspace context.

Standalone, embedded and native-mode clients **must** expose the same Workspace, View and query-log capabilities through the same Workbench backend. Every operation **must** retain the explicitly selected Project and Workspace. No client-specific create, update, run, fetch, focus, rename, remove, save, query or backend path is introduced.

Tabs support caller-ordered editing, execution, checking, paginated results, focus, renaming, removal and saving. Removing the last Tab is rejected. Running a Tab returns per-statement execution metadata and result IDs; reading each result is a separate explicit operation, including results completed before a later failure. Ordinary Run, Check and result fetch do not echo full SQL; an explicit query read returns it. Saved Views and Bookmarks remain separate from temporary query history.

All access modes **must** expose the same Workspace and Tab effects. Each Tab holds one SQL script; Run and Check follow CA-R-2728 for whole-script or explicitly selected statements. Existing saved multi-statement scripts remain intact. Historical View names in persisted records and API identifiers are compatibility names for Tabs, not a separate active UI object. No magic Workflow, code runner, scheduler or retry behavior is introduced.

In the standalone browser, an explicit `?workspace=<workspace_id>` URL **must** select that Workspace. `embedded=1` is only a density-default marker and **must not** affect backend identity or Workspace selection. Assigning a standalone Workspace **must** preserve existing URL parameters, including the saved-query/open-saved `query`. On first explicit standalone Workspace binding, migrate an unbound browser draft at most once without executing SQL; retain the local copy until the backend confirms the copy. Do not repeat a confirmed migration, merge shared Project Workspaces, import another chat's draft, or import an unbound browser draft into a native Workspace.

Public `workspace_open` and `workspace_get` responses **must** include `project_name` alongside the existing Workspace state and request-derived `workspace_url`. Clients **must** use that canonical name for the Project header. A missing name is a binding error; it does not permit a directory-basename inference, query, parser, fallback name or tool.
