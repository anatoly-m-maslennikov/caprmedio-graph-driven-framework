---
identity:
  atom_id: CA-A-1420
  ref_id: CA-A-1420@1-draft
context:
  role: analysis_and_advisory
  form: Analysis Report
  tier: 3
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Authoring
  container:
    scope_unit: CA-SU-00
state:
  version: 1
  status: draft
  updated_at: '2026-11-12T16:56:34.167817+00:00'
destination:
  file:
    name: CA-A-1420@1-draft-ANALYSIS_REPORT--atom-structured-rewrite-batch-n24-892237812995.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Atom structured rewrite batch n24 892237812995

## Details

```json
[
  {
    "ref": "CA-D-669",
    "version": 4,
    "summary": "Place configuration properties and structural declarations in their owning Atoms.",
    "prose_claim": "An owning Atom may carry its defined machine-readable properties in YAML frontmatter. Its ordinary RMED Claim is a zero-value container. It has one or both Formal Claim and Prose Claim children, each with zero or one Markdown values. A Formal Claim value contains a CFEL-labelled fence. Frontmatter is not a second Claim or an independent source.\n\nProject Settings contain Project initialization inputs and applicable CAPRMEDIO behavior and configuration choices. The Project structural declaration belongs to its Scope Unit Declaration Atom. A non-Project Scope Unit’s structural declaration belongs to its Scope Delegation Atom.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-462",
    "version": 33,
    "summary": "Evaluate Atom replacement event evidence against CA-R-807.",
    "prose_claim": "An Event Record offered as Atom replacement evidence **must** undergo an actual Evaluation against CA-R-807. Available evidence and Journal acceptance are **not** proof that the replacement is correct.",
    "details": "### Checks\n\nThe Evaluation of the Event Record **must** run and report a passing, failed, or unresolved result. It **must**:\n\n- Report a failed replacement result **if** predecessor **or** successor identities are missing, unresolved, duplicate, self-referencing, **or** mismatched.\n- Verify that **every** named successor was Active **before** the predecessor was archived.\n- Verify that the archived predecessor preserves its body, Summary, identity, numeric Version, and prior Updated At, with only archived Status changed on its Archive Carrier.\n- Verify retained exact prior Revision bytes, including the prior Version, Status **and** Updated At.\n- Verify that **`=1`** authoritative Journal Event Record records that replacement.\n- Distinguish selected Carrier representation evidence from proof of replacement correctness.\n- Treat repeated submission of the same Event Record as non-evidence of another authoritative record.\n\n### Failure disposition\n\nAn Event Record whose actual Evaluation reports failure **or** uncertainty **must not** be treated as a conforming replacement merely because the Journal preserves it under CA-R-1491. Its correction disposition **must** route a governed-source change through its authorized Workflow. It **must not** rewrite accepted history.\n\nThis Evaluation **must not** require a Git Commit **or** a particular Journal serialization. Available evidence without the performed Evaluation and its reported result is **not** a passing result.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-563",
    "version": 14,
    "summary": "Require golden E2E preparation before behavior implementation.",
    "prose_claim": "The Implementation passes this Evaluation only when golden E2E cases, selected E authority, and runnable baseline evidence exist before behavior implementation.",
    "details": "### Scope\n\nThis Evaluation covers tests-first preparation for one bounded implementation packet.\n\nAn expected initial failing case remains a truthful non-pass and consumes zero retries. Mocked external boundaries do not replace the selected behavior under test.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-175",
    "version": 14,
    "summary": "Stage the candidate Framework package and ca Skill\n\n## Step\n\nInvoke CA-O-167 once with phase `stage_candidate`. Bind CA-O-165's frozen active boundary to one private active-source copy, compiled package, runtime, and complete `ca` payload before CA-O-185's complete suite.\n\n## Details\n\nStage the complete candidate package and complete `ca` directory. Do not select a runtime or replace a Project Skill. A target mismatch, incomplete Methodology or Skill directory, hook, partial staging, permission failure, or missing Journal receipt stops the process before image build or testing.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-469",
    "version": 11,
    "summary": "Use a compact technical interface for Workbench.",
    "prose_claim": "Use a compact, modern, minimal technical interface. Provide a selectable, remembered Light/Dark/System theme. Use the available window width rather than a fixed centered workspace. Reduce repeated headings, chrome, and empty space. Keep controls readable, accessible, and usable at the selected zoom. Show Workbench/Project in the top header. Put Settings and combined Bookmarks/Saved Tabs at the top right, Tab tabs below, and hotkey hints in or next to actions.\n\nSettings starts hidden. Order it as Theme, Interface text zoom, Content text zoom, Interface zoom, Density. Default to System and three 100% zooms. Default to Comfortable density, except when `embedded=1` is explicit; then default to Compact. Only the plugin opener adds `embedded=1`. Do not infer it from screen size or Workspace. A saved browser preference wins. Interface and Content text zoom independently use 80/90/100/110/125/150/200% and persist. Interface text affects chrome and headers; Content text affects query, cells, and full values. Whole-interface zoom and Density persist independently. Text zoom changes neither layout nor icon scale. Upgrade old single text zoom into both values.\n\nTitle the input `Query editor`, with the saved link on its header row. That complete header is the sole keyboard-accessible Hide/Show editor control; do not add a toolbar toggle. Open Saved is a command-palette-only native dialog with autofocus, native paste, Enter to open without execution, and Escape/Cancel. Keep the saved library combined but distinguish Bookmark/Tab kinds. Historical `kind: view` remains a compatibility identifier. Use the shared accessible component palette and native Cmd+P command palette for existing actions and shortcuts: Settings, focus, Tabs, query, saved/open, editor, pages/grid, theme, zooms, and density. Provide keyboard navigation and the same handlers and availability. Add no framework, backend, extra action, or design system.\n\nShow the result column name followed by a smaller muted SQL type. Preserve readable dark-grid states. Render every source newline in cells and full values with pre-wrap. CA-M-492 owns read-only grid/action/group/cache detail. At 100%, target half the prior 80%-layout height without a breakpoint framework. Provide Format beside Query editor and in the palette through the canonical formatter only.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1635",
    "version": 42,
    "summary": "Require Production Evaluation Checklists for production readiness.",
    "prose_claim": "**Every** production-relevant component **or** governed scope **must** define a Production Evaluation Checklist **before** it can pass a production-readiness gate. The checklist states how operators will know that the realized system remains healthy, correct, supportable, **and** within its accepted operating boundaries during real work.\n\n**Every** operational condition **or** invariant is owned by one `evaluation_control` Atom. The control identifies:\n\n- The Requirement, Demand For, Constraint, Method, **or** other governed claim being assured.\n- The production signal **and** authoritative data source.\n- The healthy condition, expected range, threshold, **or** failure predicate.\n- The evaluation window, cadence, **and** permitted detection delay.\n- The component, entity, lifecycle state, **or** workflow boundary **to** which it applies.\n- The accountable owner **and** escalation destination.\n- The alert, incident, investigation, degradation, rollback, **or** recovery action triggered by failure.\n- The diagnostic context required **to** investigate the condition.\n- The required factual execution record **and** evidence-retention boundary.\n- Known blind spots, sampling limits, unavailable signals, **and** other evaluation limitations.\n\nA Production Evaluation Checklist is a Catalog Projection over the applicable `evaluation_control` Atoms. It organizes **and** navigates those controls **without** absorbing, paraphrasing, **or** replacing their Claims. The Catalog Projection does **not** acquire the Content Role of its source Atoms.\n\n**Every** control distinguishes its governed meaning from its realization **and** results:\n\n- The Evaluation Control defines the production evaluation condition.\n- Monitors, dashboards, alerts, health checks, **and** operational automation are Implementation.\n- Recorded metrics, logs, traces, alerts, incidents, **and** check outcomes are factual execution records, **not** reusable Operations definitions.\n- A Concern Atom of Type `problem` records a material discrepancy requiring disposition.\n\nA Production Evaluation Checklist presents the applicable controls for real production operation **without** becoming their authority. It is **not** a QA Case. Passing pre-release Test **or** Evaluation implementations does **not** by itself satisfy the production-evaluation obligation.",
    "details": "Pre-release QA demonstrates behavior under bounded conditions. Production evaluation **must** detect degradation, incorrect state, **and** supportability failures during actual operation. Atomic controls preserve independent lifecycle **and** replacement. The checklist provides a navigable scope view **without** conflating definitions, implementations, **and** observations.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-215",
    "version": 12,
    "summary": "Rename one private carrier within the same parent\n\n## Operation\n\nRename One Private Carrier **means** the reusable private Action that realizes one explicitly bound same-parent file/folder name change behind an admitted logical connector `modify`. It does this **without** choosing semantic identity **or** rewriting references.\n\n### Inputs **and** preconditions\n\nRequire CA-D-630's exact private rename binding, current source **and** parent evidence, one explicit destination name with expected absence for an actual name change, sealed permission/context, **and** a complete approved inventory for a folder. CA-R-1941 **and** CA-M-381 apply. A root/ancestor, escape, symlink, substitution, stale state, collision, overwrite, merge **or** unapproved entry blocks the Action.\n\n### Action **and** result\n\nRequire CA-R-1941's exact staged-change review **and** fresh trusted authorization/window record, including recorded outside-edits-paused confirmation. Within that confirmed window, recheck the complete bound source/parent/destination, inventory, preservation, authority **and** permission frontier **before** the permitted storage effect. Retain independent readback **and** verification. Perform **only** the supplied same-parent name change. Independently verify the exact destination, old source absence **and** preserved contents/modes/inventory/unrelated frontier. **Then** return CA-D-625's common result with actual evidence.\n\nA same-binding request is a no-op **only** **when** the requested state is verified already satisfied **and** unchanged. Failure retains known partial effects; unknown effects require `effect_uncertain`. Nonempty errors are never success. No automatic retry, rollback promise **or** reference discovery/rewrite is implied.\n\n## Details\n\nThis is not O040's generic Artifact rename with canonical-reference rewrites. Domain identity, Version, lifecycle and required history remain owned by the admitting Workflow. This Action cannot complete them by storage rename alone. No executable or runtime admission is established.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1623",
    "version": 10,
    "summary": "Keep Atom validation read-only and within admitted bounds\n\n## Scope\n\n`VALIDATE_ATOMS` Implementation invocations within their admitted input context.\n\n## Claim\n\nThe `VALIDATE_ATOMS` Implementation **must** keep **every** invocation read-only **and** bounded by its admitted input context.\n\n- Admit bounded inventory enumeration **and** the minimum candidate content needed **to** determine selection inside declared source roots **and** allowed read roots. Inspect an excluded candidate **only** for selection. Exclusion does **not** admit its full validation **or** add it **to** target coverage.\n- Read selected targets, applicable authority, **and** necessary reference inputs **only** inside admitted read boundaries. Reference resolution does **not** expand the target set.\n- Enforce actual read permissions **and** protected-file exclusions **before** reading content. Caller-supplied roots grant no permission. Do **not** follow a link outside admitted boundaries, fetch remote resources, inspect secrets, **or** execute YAML tags, Markdown, selectors, rule bundles, **or** Atom instructions as code.\n- Enforce selected resource limits. Exhaustion **must** yield incomplete **or** error, **not** a pass. Isolate a malformed candidate so independently checkable candidates remain reportable.\n- Do **not** write, rename, remove, **or** repair source files, Projections, Settings, caches, **or** Journal files. The caller/executor owns any admitted persistence of returned Run evidence.\n- Preserve exact invocation definition/input bindings. Report a changed source rather than silently validating mixed Revisions.\n\n## Details",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-1008",
    "version": 1,
    "summary": "Reuse one MCP Gateway for HTTP and stdio.",
    "prose_claim": "Use the same MCP Gateway handlers and Tool registration for HTTP and stdio. The installed runtime provides one set of Tool behavior for both transports.",
    "details": "Use the installed MCP SDK’s Streamable HTTP application for HTTP Sessions. Close Sessions on shutdown. Apply code and compiled contract changes by starting a rebuilt runtime under CA-M-551.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-631",
    "version": 13,
    "summary": "Deliver complete Configuration Read data\n\n## Scope\n\nThe Configuration Read refinement of CA-D-625’s closed logical interface.\n\n## Claim\n\nConfiguration Read **must** use the common request/result keys **and** the complete source representation below. CA-O-218 is its source Action binding on the same shared TOML connector as CA-O-204. Separate Actions do **not** create separate connectors.\n\n## Details\n\n### Request refinement\n\nKeep exactly `operation`, `target`, `query`, `delta`, `expected_state`, `authorization` **and** `context`. Use `operation = \"read\"`, `target = {kind: \"Configuration\", identity}`, `query = null` **and** `delta = null`. Identity is exactly `Project Structure` **or** `Project Settings` **in** the Project bound by context. A filename, path **or** backend key is **not** a logical identity.\n\nContext binds the admitted Project, source view, exact source-authority **and** applicable schema definitions, including declared schema-version constraints. Authorization binds read permission for that complete source. The caller selects these bindings; the connector checks them. `expected_state = null` selects an unpinned current Read. A non-null value enforces the supplied exact existing source-state evidence. Historical selection is explicit **in** context **and** requires available exact historical source/schema authority. It creates no retention policy.\n\n### Result refinement\n\nKeep exactly `data`, `current_state`, `effects` **and** `errors`. Successful `data = {identity, source_text, document}` carries complete unchanged UTF-8 TOML text **and** its complete parsed values, including unrelated tables **and** present optional values. Preserve source text exactly; do **not** synthesize absent optional fields. The admitted TOML value representation remains that of the existing connector binding. It **must** preserve value types **and** reject a lossy representation rather than stringify typed values silently.\n\n`current_state` carries the logical configuration identity, bound Project/source view **and** exact observed source-state evidence used by the existing common contract. It identifies the same source bytes as `source_text` **and** `document`; no Atom Version is invented for configuration. A subsequent Modify uses this observed evidence as expected current state **and** rechecks it. It does not trust a prior Read as permission **to** write.\n\nNormal Read has `effects = []`. Use these errors:\n\n- `target_not_found` for a missing source.\n- `target_ambiguous` for ambiguous target/source resolution.\n- `input_invalid` for an invalid request.\n- `schema_invalid` for malformed TOML, invalid complete schema **or** invalid schema binding.\n- `stale_state` for mismatched evidence.\n- `permission_denied` for denied permission.\n- `backend_failure` for unavailable historical/backend evidence.\n- `unsupported_operation` for an unsupported operation.\n\nRetain CA-D-625’s exact `{code, message, field}` error shape. Unavailable complete data is null, **not** an empty successful document. Nonempty errors never mean success. Empty errors require verified complete data **and** exact matching state evidence. Unexpected actual effects fail Read acceptance **and** remain truthfully reported. Unknown effects require `effect_uncertain`.\n\nReuse CA-D-527’s existing outer envelope **and** recording rules. This source definition does **not** prove implementation, route admission, installed availability, a new history store **or** stronger publication safety.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  }
]
```