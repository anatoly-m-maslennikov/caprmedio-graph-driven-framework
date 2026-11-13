---
identity:
  atom_id: CA-A-1403
  ref_id: CA-A-1403@1-draft
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
  updated_at: '2026-11-12T16:30:19.005262+00:00'
destination:
  file:
    name: CA-A-1403@1-draft-ANALYSIS_REPORT--atom-cut-comparison-batch-v81-892237812994.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Atom cut comparison batch v81 892237812994

## Details

```json
[
  {
    "ref": "CA-D-669",
    "version": 4,
    "summary": "Encode configuration surfaces in owning Atoms",
    "prose_claim": "An owning Atom may carry its defined machine-readable properties in YAML frontmatter. Its ordinary RMED Claim is a zero-value container with one or both Formal Claim and Prose Claim children, each with zero or one Markdown values. A Formal Claim value contains a CFEL-labelled fence. Frontmatter is not a second Claim or independent source. Project initialization inputs and applicable CAPRMEDIO behavior and configuration choices belong to Project Settings; The Project structural declaration belongs to its Scope Unit Declaration Atom; a non-Project Scope Unit’s structural declaration belongs to its Scope Delegation Atom.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-462",
    "version": 33,
    "summary": "Validate Atom replacement event evidence",
    "prose_claim": "Atom replacement event evidence.\n\n\nan Event Record offered as Atom replacement evidence **must** undergo an actual Evaluation against CA-R-807. Available evidence and Journal acceptance are **not** proof that the replacement is correct.",
    "details": "### Checks\n\nthe Evaluation of that Event Record **must** run and report a passing, failed, or unresolved result. It **must**:\n\n- report a failed replacement result **if** predecessor **or** successor identities are missing, unresolved, duplicate, self-referencing, **or** mismatched;\n- verify that **every** named successor was Active **before** the predecessor was archived, that the archived predecessor preserves its body, Summary, identity, numeric Version, and prior Updated At, with only archived Status changed on its Archive Carrier; verify retained exact prior Revision bytes, including the prior Version, Status **and** Updated At, and that **`=1`** authoritative Journal Event Record records that replacement;\n- distinguish selected Carrier representation evidence from proof of replacement correctness; and\n- treat repeated submission of the same Event Record as non-evidence of another authoritative record.\n\n### Failure disposition\n\nan Event Record whose actual Evaluation reports failure **or** uncertainty **must not** be treated as a conforming replacement merely because the Journal preserves it under CA-R-1491. Its correction disposition **must** route a governed-source change through its authorized Workflow and **must not** rewrite accepted history.\n\nthis Evaluation **must not** require a Git Commit **or** a particular Journal serialization. Available evidence without the performed Evaluation and its reported result is **not** a passing result.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-563",
    "version": 14,
    "summary": "Verify implementation prompt golden E2E preparation",
    "prose_claim": "the Implementation passes this Evaluation only when golden E2E cases, selected E authority, and runnable baseline evidence exist before behavior implementation.",
    "details": "### Scope\n\ntests-first preparation for one bounded implementation packet.\n\nAn expected initial failing case remains a truthful non-pass and consumes zero retries. Mocked external boundaries do not replace the selected behavior under test.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-175",
    "version": 14,
    "summary": "Stage the candidate Framework package and ca Skill\n\n## Step\n\nThis Step invokes CA-O-167 once with phase `stage_candidate`, binding CA-O-165's frozen active boundary to one private active-source copy, compiled package, runtime, and complete `ca` payload before CA-O-185's complete suite.\n\n## Details\n\nIt stages the complete candidate package and complete `ca` directory without selecting a runtime or replacing a Project Skill. A target mismatch, incomplete Methodology or Skill directory, hook, partial staging, permission failure, or missing Journal receipt stops before image build or testing.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-469",
    "version": 11,
    "summary": "Use a minimal technical visual design for Workbench",
    "prose_claim": "Use a compact, modern, minimal technical interface with selectable remembered Light/Dark/System theme and available window width, not a fixed centered workspace. Reduce repeated headings, chrome and empty space while controls remain readable, accessible and usable at selected zoom. Top header shows Workbench/Project; Settings and combined Bookmarks/Saved Tabs are top-right, with Tab tabs below and hotkey hints in/next to actions.\n\nSettings starts hidden and orders Theme, Interface text zoom, Content text zoom, Interface zoom, Density. Defaults are System and three 100% zooms; Comfortable density except explicit `embedded=1`, where Compact is default. Only plugin opener adds `embedded=1`; screen size/Workspace does not infer it and saved browser preference wins. Interface/Content text zoom independently use 80/90/100/110/125/150/200% and persist; Interface text affects chrome/headers, Content text affects query/cells/full values. Whole-interface zoom and Density persist independently; text zoom changes neither layout nor icon scale. Upgrade old single text zoom into both values.\n\nTitle input `Query editor`, with saved link on its header row. That complete header is the sole keyboard-accessible Hide/Show editor control; no toolbar toggle. Open Saved is command-palette-only native dialog with autofocus, native paste, Enter-open-without-execution and Escape/Cancel. Keep saved library combined but distinguish Bookmark/Tab kinds (historical `kind: view` remains a compatibility identifier). Use the shared accessible component palette and native Cmd+P command palette for existing actions/shortcuts (Settings, focus, Tabs, query, saved/open, editor, pages/grid, theme/zooms/density), keyboard navigation and the same handlers/availability—no framework, backend, extra action or design system.\n\nShow result column name then smaller muted SQL type; preserve readable dark-grid states and render every source newline in cells/full values with pre-wrap. CA-M-492 owns read-only grid/action/group/cache detail. At 100%, target half the prior 80%-layout height without a breakpoint framework. Provide Format beside Query editor and in palette via the canonical formatter only.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1635",
    "version": 42,
    "summary": "Require production evaluation checklists",
    "prose_claim": "production-relevant components and governed scopes.\n\n\n**every** production-relevant component **or** governed scope **must** define a Production Evaluation Checklist **before** it can pass a production-readiness gate. the checklist states how operators will know that the realized system remains healthy, correct, supportable, **and** within its accepted operating boundaries during real work.\n\n**every** operational condition **or** invariant is owned by one `evaluation_control` Atom. the control identifies:\n\n- the Requirement, Demand For, Constraint, Method, **or** other governed claim being assured;\n- the production signal **and** authoritative data source;\n- the healthy condition, expected range, threshold, **or** failure predicate;\n- the evaluation window, cadence, **and** permitted detection delay;\n- the component, entity, lifecycle state, **or** workflow boundary **to** which it applies;\n- the accountable owner **and** escalation destination;\n- the alert, incident, investigation, degradation, rollback, **or** recovery action triggered by failure;\n- the diagnostic context required **to** investigate the condition;\n- the required factual execution record **and** evidence-retention boundary; **and**\n- known blind spots, sampling limits, unavailable signals, **and** other evaluation limitations.\n\na Production Evaluation Checklist is a Catalog Projection over the applicable `evaluation_control` Atoms. it organizes **and** navigates those controls **without** absorbing, paraphrasing, **or** replacing their Claims. the Catalog Projection does **not** acquire the Content Role of its source Atoms.\n\n**every** control distinguishes its governed meaning from its realization **and** results:\n\n- the Evaluation Control defines the production evaluation condition;\n- monitors, dashboards, alerts, health checks, **and** operational automation are Implementation;\n- recorded metrics, logs, traces, alerts, incidents, **and** check outcomes are factual execution records, **not** reusable Operations definitions; **and**\n- a Concern Atom of Type `problem` records a material discrepancy requiring disposition.\n\na Production Evaluation Checklist presents the applicable controls for real production operation **without** becoming their authority. it is **not** a QA Case, **and** passing pre-release Test **or** Evaluation implementations does **not** by itself satisfy the production-evaluation obligation.",
    "details": "pre-release QA demonstrates behavior under bounded conditions, while production evaluation **must** detect degradation, incorrect state, **and** supportability failures during actual operation. atomic controls preserve independent lifecycle **and** replacement, while the checklist provides a navigable scope view **without** conflating definitions, implementations, **and** observations.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-215",
    "version": 12,
    "summary": "Rename one private carrier\n\n## Operation\n\nRename One Private Carrier **means** the reusable private Action that realizes one explicitly bound same-parent file/folder name change behind an admitted logical connector `modify`, **without** choosing semantic identity **or** rewriting references.\n\n### Inputs **and** preconditions\n\nrequire CA-D-630's exact private rename binding, current source **and** parent evidence, one explicit destination name with expected absence for an actual name change, sealed permission/context **and** a complete approved inventory for a folder. CA-R-1941 **and** CA-M-381 apply. a root/ancestor, escape, symlink, substitution, stale state, collision, overwrite, merge **or** unapproved entry blocks the Action.\n\n### Action **and** result\n\nrequire CA-R-1941's exact staged-change review **and** fresh trusted authorization/window record, including recorded outside-edits-paused confirmation. within that confirmed window, recheck the complete bound source/parent/destination, inventory, preservation, authority **and** permission frontier **before** the permitted storage effect. retain independent readback **and** verification. perform **only** the supplied same-parent name change. independently verify the exact destination, old source absence **and** preserved contents/modes/inventory/unrelated frontier, **then** return CA-D-625's common result with actual evidence.\n\na same-binding request is a no-op **only** **when** requested state is verified already satisfied **and** unchanged. failure retains known partial effects; unknown effects require `effect_uncertain`, **and** nonempty errors are never success. no automatic retry, rollback promise **or** reference discovery/rewrite is implied.\n\n## Details\n\nThis is not O040's generic Artifact rename with canonical-reference rewrites. Domain identity, Version, lifecycle and required history remain owned by the admitting Workflow; this Action cannot complete them by storage rename alone. No executable or runtime admission is established.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1623",
    "version": 10,
    "summary": "Keep Atom validation execution bounded and read-only\n\n## Scope\n\n`VALIDATE_ATOMS` Implementation invocations within their admitted input context.\n\n## Claim\n\nthe `VALIDATE_ATOMS` Implementation **must** keep **every** invocation read-only **and** bounded by its admitted input context.\n\n- admit bounded inventory enumeration **and** the minimum candidate content needed **to** determine selection inside declared source roots **and** allowed read roots. inspect an excluded candidate **only** for selection; exclusion does **not** admit its full validation **or** add it **to** target coverage.\n- read selected targets, applicable authority, **and** necessary reference inputs **only** inside admitted read boundaries. reference resolution does **not** expand the target set.\n- enforce actual read permissions **and** protected-file exclusions **before** reading content. caller-supplied roots grant no permission; do **not** follow a link outside admitted boundaries, fetch remote resources, inspect secrets, **or** execute YAML tags, Markdown, selectors, rule bundles, **or** Atom instructions as code.\n- enforce selected resource limits; exhaustion **must** yield incomplete **or** error, **not** a pass. isolate a malformed candidate so independently checkable candidates remain reportable.\n- do **not** write, rename, remove, **or** repair source files, Projections, Settings, caches, **or** Journal files. the caller/executor owns any admitted persistence of returned Run evidence.\n- preserve exact invocation definition/input bindings; report a changed source rather than silently validating mixed Revisions.\n\n## Details",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-1008",
    "version": 1,
    "summary": "Reuse one Gateway for HTTP and stdio",
    "prose_claim": "Use the same MCP Gateway handlers and Tool registration for HTTP and stdio. The installed runtime provides one set of Tool behavior for both transports.",
    "details": "Use the installed MCP SDK’s Streamable HTTP application for HTTP Sessions. Close Sessions on shutdown. Apply code and compiled contract changes by starting a rebuilt runtime under CA-M-551.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-631",
    "version": 13,
    "summary": "Deliver complete configuration read data\n\n## Scope\n\nthe Configuration Read refinement of CA-D-625's closed logical interface.\n\n## Claim\n\nConfiguration Read **must** use the common request/result keys **and** the complete source representation below. CA-O-218 is its source Action binding on the same shared TOML connector as CA-O-204; separate Actions do **not** create separate connectors.\n\n## Details\n\n### Request refinement\n\nkeep exactly `operation`, `target`, `query`, `delta`, `expected_state`, `authorization` **and** `context`. use `operation = \"read\"`, `target = {kind: \"Configuration\", identity}`, `query = null` **and** `delta = null`. identity is exactly `Project Structure` **or** `Project Settings` **in** the Project bound by context. a filename, path **or** backend key is **not** a logical identity.\n\ncontext binds the admitted Project, source view, exact source-authority **and** applicable schema definitions, including declared schema-version constraints. authorization binds read permission for that complete source. the caller selects these bindings; the connector checks them. `expected_state = null` selects an unpinned current Read. a non-null value enforces the supplied exact existing source-state evidence. historical selection is explicit **in** context **and** requires available exact historical source/schema authority; it creates no retention policy.\n\n### Result refinement\n\nkeep exactly `data`, `current_state`, `effects` **and** `errors`. successful `data = {identity, source_text, document}` carries complete unchanged UTF-8 TOML text **and** its complete parsed values, including unrelated tables **and** present optional values. preserve source text exactly; do **not** synthesize absent optional fields. the admitted TOML value representation remains that of the existing connector binding; it **must** preserve value types **and** reject a lossy representation rather than stringify typed values silently.\n\n`current_state` carries the logical configuration identity, bound Project/source view **and** exact observed source-state evidence used by the existing common contract. it identifies the same source bytes as `source_text` **and** `document`; no Atom Version is invented for configuration. a subsequent Modify uses this observed evidence as expected current state **and** rechecks it, rather than trusting a prior Read as permission **to** write.\n\nnormal Read has `effects = []`. missing source uses `target_not_found`; ambiguous target/source resolution uses `target_ambiguous`; invalid request uses `input_invalid`; malformed TOML, invalid complete schema **or** invalid schema binding uses `schema_invalid`; mismatched evidence uses `stale_state`; denied permission uses `permission_denied`; unavailable historical/backend evidence uses `backend_failure`; unsupported operation uses `unsupported_operation`. retain CA-D-625's exact `{code, message, field}` error shape. unavailable complete data is null, **not** an empty successful document. nonempty errors never mean success; empty errors require verified complete data **and** exact matching state evidence. unexpected actual effects fail Read acceptance **and** remain truthfully reported; unknown effects require `effect_uncertain`.\n\nreuse CA-D-527's existing outer envelope **and** recording rules. this source definition does **not** prove implementation, route admission, installed availability, a new history store **or** stronger publication safety.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  }
]
```