---
identity:
  atom_id: CA-A-1446
  ref_id: CA-A-1446@1-draft
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
  updated_at: '2026-11-12T20:52:06.527228+00:00'
destination:
  file:
    name: CA-A-1446@1-draft-ANALYSIS_REPORT--atom-escalation-benchmark-mzfs9fvs-batch-3.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Atom escalation benchmark mzfs9fvs batch 3

## Details

```json
{
  "batch": 3,
  "atoms": [
    {
      "source_ref": "CA-D-669",
      "source_version": 4,
      "candidate": {
        "ref": "CA-D-669",
        "version": 4,
        "summary": "Keep configuration in its owning Atom.",
        "prose_claim": "An owning Atom may store its defined machine-readable properties in YAML frontmatter. The ordinary RMED Claim is a zero-value container. It has one or both of these children: Formal Claim and Prose Claim. Each child has zero or one Markdown values. A Formal Claim value contains a CFEL-labelled fence.\n\nFrontmatter is not a second Claim or an independent source.\n\nStore project initialization inputs and applicable CAPRMEDIO behavior and configuration choices in Project Settings. Store the Project structural declaration in its Scope Unit Declaration Atom. Store a non-Project Scope Unit's structural declaration in its Scope Delegation Atom.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-D-669",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate preserves the frontmatter and Claim structure, including 'one or both' children with 'zero or one' Markdown values, and keeps all three configuration destinations unchanged."
      },
      "final": {
        "ref": "CA-D-669",
        "version": 4,
        "summary": "Keep configuration in its owning Atom.",
        "prose_claim": "An owning Atom may store its defined machine-readable properties in YAML frontmatter. The ordinary RMED Claim is a zero-value container. It has one or both of these children: Formal Claim and Prose Claim. Each child has zero or one Markdown values. A Formal Claim value contains a CFEL-labelled fence.\n\nFrontmatter is not a second Claim or an independent source.\n\nStore project initialization inputs and applicable CAPRMEDIO behavior and configuration choices in Project Settings. Store the Project structural declaration in its Scope Unit Declaration Atom. Store a non-Project Scope Unit's structural declaration in its Scope Delegation Atom.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-E-462",
      "source_version": 33,
      "candidate": {
        "ref": "CA-E-462",
        "version": 33,
        "summary": "Evaluate Atom replacement evidence against CA-R-807.",
        "prose_claim": "An Event Record offered as evidence for Atom replacement **must** undergo an actual Evaluation against CA-R-807. Available evidence and Journal acceptance do **not** prove that the replacement is correct.",
        "details": "### Checks\n\nThe Evaluation of the Event Record **must** run and report a passing, failed, or unresolved result. It **must**:\n\n- report failure if the predecessor or successor identities are missing, unresolved, duplicated, self-referencing, or mismatched;\n- verify that **every** named successor was Active before the predecessor was archived;\n- verify that the archived predecessor preserves its body, Summary, identity, numeric Version, and prior Updated At. Only its Status may change on its Archive Carrier;\n- verify that the exact prior Revision bytes are retained, including the prior Version, Status, and Updated At;\n- verify that **`=1`** authoritative Journal Event Record records the replacement;\n- distinguish evidence of the selected Carrier representation from proof that the replacement is correct; and\n- treat repeated submission of the same Event Record as no evidence of another authoritative record.\n\n### Failure disposition\n\nAn Event Record whose actual Evaluation reports failure or uncertainty **must not** be treated as a conforming replacement just because the Journal preserves it under CA-R-1491. To correct it, route a governed-source change through its authorized Workflow. Do **not** rewrite accepted history.\n\nThis Evaluation **must not** require a Git Commit or a particular Journal serialization. Available evidence without a performed Evaluation and its reported result is not a passing result.",
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-E-462",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate retains the identity checks, predecessor preservation, exact prior Revision bytes, single authoritative Journal record, and failure disposition. Splitting the long source bullet preserves its requirements."
      },
      "final": {
        "ref": "CA-E-462",
        "version": 33,
        "summary": "Evaluate Atom replacement evidence against CA-R-807.",
        "prose_claim": "An Event Record offered as evidence for Atom replacement **must** undergo an actual Evaluation against CA-R-807. Available evidence and Journal acceptance do **not** prove that the replacement is correct.",
        "details": "### Checks\n\nThe Evaluation of the Event Record **must** run and report a passing, failed, or unresolved result. It **must**:\n\n- report failure if the predecessor or successor identities are missing, unresolved, duplicated, self-referencing, or mismatched;\n- verify that **every** named successor was Active before the predecessor was archived;\n- verify that the archived predecessor preserves its body, Summary, identity, numeric Version, and prior Updated At. Only its Status may change on its Archive Carrier;\n- verify that the exact prior Revision bytes are retained, including the prior Version, Status, and Updated At;\n- verify that **`=1`** authoritative Journal Event Record records the replacement;\n- distinguish evidence of the selected Carrier representation from proof that the replacement is correct; and\n- treat repeated submission of the same Event Record as no evidence of another authoritative record.\n\n### Failure disposition\n\nAn Event Record whose actual Evaluation reports failure or uncertainty **must not** be treated as a conforming replacement just because the Journal preserves it under CA-R-1491. To correct it, route a governed-source change through its authorized Workflow. Do **not** rewrite accepted history.\n\nThis Evaluation **must not** require a Git Commit or a particular Journal serialization. Available evidence without a performed Evaluation and its reported result is not a passing result.",
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-E-563",
      "source_version": 14,
      "candidate": {
        "ref": "CA-E-563",
        "version": 14,
        "summary": "Require golden E2E preparation before behavior implementation.",
        "prose_claim": "The Implementation passes this Evaluation only if golden E2E cases, the selected E authority, and runnable baseline evidence exist before behavior implementation.",
        "details": "### Scope\n\nThis Evaluation checks tests-first preparation for one bounded implementation packet.\n\nAn expected initial failing case remains a truthful non-pass and consumes zero retries. Mocked external boundaries do not replace the selected behavior under test.",
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-E-563",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate preserves the pass condition and timing ('before behavior implementation'), the bounded packet scope, truthful initial failure with zero retries, and mocked-boundary restriction."
      },
      "final": {
        "ref": "CA-E-563",
        "version": 14,
        "summary": "Require golden E2E preparation before behavior implementation.",
        "prose_claim": "The Implementation passes this Evaluation only if golden E2E cases, the selected E authority, and runnable baseline evidence exist before behavior implementation.",
        "details": "### Scope\n\nThis Evaluation checks tests-first preparation for one bounded implementation packet.\n\nAn expected initial failing case remains a truthful non-pass and consumes zero retries. Mocked external boundaries do not replace the selected behavior under test.",
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-O-175",
      "source_version": 14,
      "candidate": {
        "ref": "CA-O-175",
        "version": 14,
        "summary": "Stage the complete candidate package and `ca` Skill before building or testing.\n\n## Step\n\nInvoke CA-O-167 once with phase `stage_candidate`. Bind CA-O-165's frozen active boundary to one private active-source copy, compiled package, runtime, and complete `ca` payload. Do this before CA-O-185's complete suite.\n\n## Details\n\nStage the complete candidate package and complete `ca` directory. Do not select a runtime or replace a Project Skill. A target mismatch, incomplete Methodology or Skill directory, hook, partial staging, permission failure, or missing Journal receipt stops the process before image build or testing.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-O-175",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate preserves the single stage_candidate invocation, frozen-boundary bindings, ordering before the complete suite, prohibited runtime or Skill changes, and all stop conditions."
      },
      "final": {
        "ref": "CA-O-175",
        "version": 14,
        "summary": "Stage the complete candidate package and `ca` Skill before building or testing.\n\n## Step\n\nInvoke CA-O-167 once with phase `stage_candidate`. Bind CA-O-165's frozen active boundary to one private active-source copy, compiled package, runtime, and complete `ca` payload. Do this before CA-O-185's complete suite.\n\n## Details\n\nStage the complete candidate package and complete `ca` directory. Do not select a runtime or replace a Project Skill. A target mismatch, incomplete Methodology or Skill directory, hook, partial staging, permission failure, or missing Journal receipt stops the process before image build or testing.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-M-469",
      "source_version": 11,
      "candidate": {
        "ref": "CA-M-469",
        "version": 11,
        "summary": "Use a compact, minimal technical Workbench interface. Provide a remembered Light, Dark, or System theme and use available window width. Do not fix the workspace to a centered width. Reduce repeated headings, chrome, and empty space while keeping controls readable, accessible, and usable at the selected zoom.\n\nThe header shows Workbench/Project. Put Settings and combined Bookmarks/Saved Tabs at the top right. Put Tab tabs below the header. Show hotkey hints in or next to actions.\n\nSettings starts hidden. Order its controls as Theme, Interface text zoom, Content text zoom, Interface zoom, and Density. Defaults are System and 100% for all three zooms. Density defaults to Comfortable, except `embedded=1` defaults to Compact. Only the plugin opener adds `embedded=1`; neither screen size nor Workspace implies it. A saved browser preference takes precedence. Interface and Content text zooms each offer 80/90/100/110/125/150/200% and persist separately. Interface text zoom affects chrome and headers. Content text zoom affects queries, cells, and full values. Interface zoom and Density persist independently. Text zoom changes neither layout nor icon scale. Upgrade the old single text zoom value into both values.\n\nLabel the title input `Query editor`. Put its saved link on the header row. The complete header is the only keyboard-accessible Hide/Show editor control. Do not add a toolbar toggle. Open Saved is available only through the command palette and uses a native dialog. Autofocus the dialog, support native paste, open on Enter without execution, and support Escape/Cancel. Keep the saved library combined, but distinguish Bookmark and Tab kinds. Historical `kind: view` remains a compatibility identifier.\n\nUse the shared accessible component palette and native Cmd+P command palette for existing actions and shortcuts: Settings, focus, Tabs, query, saved/open, editor, pages/grid, theme, zooms, and density. Support keyboard navigation and use the same handlers and availability. Add no framework, backend, extra action, or design system.\n\nShow each result column name, then its SQL type in smaller muted text. Preserve readable dark-grid states. Render every source newline in cells and full values with pre-wrap. At 100%, target half the height of the prior 80% layout without a breakpoint framework. Provide Format beside Query editor and in the palette, using only the canonical formatter.\n\nCA-M-492 owns read-only grid, action, group, and cache details.",
        "prose_claim": "Use a compact, modern, minimal technical interface. Use the available window width instead of a fixed, centered workspace. Reduce repeated headings, chrome, and empty space. Keep controls readable, accessible, and usable at the selected zoom.\n\nThe top header shows Workbench/Project. Put Settings and combined Bookmarks/Saved Tabs at the top right. Put Tab tabs below the header. Show hotkey hints in or next to actions.\n\nSettings starts hidden. Order its controls: Theme, Interface text zoom, Content text zoom, Interface zoom, Density. Defaults are System and 100% for the three zooms. Density defaults to Comfortable, except `embedded=1`, where Compact is the default. Only the plugin opener adds `embedded=1`. Screen size and Workspace do not imply it. A saved browser preference takes precedence. Interface and Content text zoom each offer 80/90/100/110/125/150/200% and persist. Interface text zoom affects chrome and headers. Content text zoom affects query, cells, and full values. Interface zoom and Density persist independently. Text zoom does not change layout or icon scale. Upgrade the old single text zoom to both values.\n\nLabel the title input `Query editor`. Put the saved link on its header row. Make the complete header the only keyboard-accessible Hide/Show editor control. Do not add a toolbar toggle. Make Open Saved available only in the command palette. It uses a native dialog with autofocus, native paste, Enter to open without execution, and Escape/Cancel. Keep the saved library combined and distinguish Bookmark and Tab kinds. Keep historical `kind: view` as a compatibility identifier.\n\nUse the shared accessible component palette and native Cmd+P command palette for existing actions and shortcuts: Settings, focus, Tabs, query, saved/open, editor, pages/grid, theme, zooms, and density. Support keyboard navigation. Use the same handlers and availability. Do not add a framework, backend, extra action, or design system.\n\nShow the result column name, then its SQL type in smaller muted text. Preserve readable dark-grid states. Render every source newline in cells and full values with pre-wrap. At 100%, target half the height of the prior 80% layout without a breakpoint framework. Provide Format beside Query editor and in the palette through the canonical formatter only.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-M-469",
        "confidence": "medium",
        "escalate": true,
        "reason": "The source Summary is the brief label 'Use a minimal technical visual design for Workbench'; the candidate Summary expands into a multi-paragraph full specification that substantially duplicates its Prose Claim. The requirements appear retained, but this may change the Summary's section function."
      },
      "final": {
        "ref": "CA-M-469",
        "version": 11,
        "summary": "Use a minimal technical visual design for Workbench",
        "prose_claim": "Use a compact, modern, minimal technical interface with a selectable, remembered Light/Dark/System theme. Use the available window width instead of a fixed, centered workspace. Reduce repeated headings, chrome, and empty space. Keep controls readable, accessible, and usable at the selected zoom.\n\nThe top header shows Workbench/Project. Put Settings and combined Bookmarks/Saved Tabs at the top right. Put Tab tabs below the header. Show hotkey hints in or next to actions.\n\nSettings starts hidden. Order its controls: Theme, Interface text zoom, Content text zoom, Interface zoom, Density. Defaults are System and 100% for the three zooms. Density defaults to Comfortable, except `embedded=1`, where Compact is the default. Only the plugin opener adds `embedded=1`. Screen size and Workspace do not imply it. A saved browser preference takes precedence. Interface and Content text zoom each offer 80/90/100/110/125/150/200% and persist. Interface text zoom affects chrome and headers. Content text zoom affects query, cells, and full values. Interface zoom and Density persist independently. Text zoom does not change layout or icon scale. Upgrade the old single text zoom to both values.\n\nLabel the title input `Query editor`. Put the saved link on its header row. Make the complete header the only keyboard-accessible Hide/Show editor control. Do not add a toolbar toggle. Make Open Saved available only in the command palette. It uses a native dialog with autofocus, native paste, Enter to open without execution, and Escape/Cancel. Keep the saved library combined and distinguish Bookmark and Tab kinds. Keep historical `kind: view` as a compatibility identifier.\n\nUse the shared accessible component palette and native Cmd+P command palette for existing actions and shortcuts: Settings, focus, Tabs, query, saved/open, editor, pages/grid, theme, zooms, and density. Support keyboard navigation. Use the same handlers and availability. Do not add a framework, backend, extra action, or design system.\n\nShow the result column name, then its SQL type in smaller muted text. Preserve readable dark-grid states. Render every source newline in cells and full values with pre-wrap. CA-M-492 owns read-only grid/action/group/cache detail. At 100%, target half the height of the prior 80% layout without a breakpoint framework. Provide Format beside Query editor and in the palette through the canonical formatter only.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": [
        {
          "source": "Use a minimal technical visual design for Workbench",
          "candidate": "Use a compact, minimal technical Workbench interface. Provide a remembered Light, Dark, or System theme",
          "reason": "The summary expands a brief label into a full multi-paragraph specification, changing its section function.",
          "status": "repaired"
        },
        {
          "source": "selectable remembered Light/Dark/System theme",
          "candidate": "Use a compact, modern, minimal technical interface.",
          "reason": "The prose claim omits theme choices and their selection and persistence.",
          "status": "repaired"
        },
        {
          "source": "CA-M-492 owns read-only grid/action/group/cache detail",
          "candidate": "Preserve readable dark-grid states.",
          "reason": "The prose claim omits the ownership reference and boundary for those details.",
          "status": "repaired"
        }
      ]
    },
    {
      "source_ref": "CA-R-1635",
      "source_version": 42,
      "candidate": {
        "ref": "CA-R-1635",
        "version": 42,
        "summary": "Require production evaluation checklists before readiness gates.",
        "prose_claim": "### Scope\n\nProduction-relevant components and governed scopes.\n\n### Claim\n\n**Every** production-relevant component or governed scope **must** define a Production Evaluation Checklist before it can pass a production-readiness gate. The checklist states how operators will know that the realized system remains healthy, correct, supportable, and within its accepted operating boundaries during real work.\n\n**Every** operational condition or invariant is owned by one `evaluation_control` Atom. The control identifies:\n\n- the Requirement, Demand For, Constraint, Method, or other governed claim it assures;\n- the production signal and authoritative data source;\n- the healthy condition, expected range, threshold, or failure predicate;\n- the evaluation window, cadence, and permitted detection delay;\n- the component, entity, lifecycle state, or workflow boundary to which it applies;\n- the accountable owner and escalation destination;\n- the alert, incident, investigation, degradation, rollback, or recovery action triggered by failure;\n- the diagnostic context needed to investigate the condition;\n- the required factual execution record and evidence-retention boundary; and\n- known blind spots, sampling limits, unavailable signals, and other evaluation limitations.\n\nA Production Evaluation Checklist is a Catalog Projection over the applicable `evaluation_control` Atoms. It organizes and navigates these controls. It does not absorb, paraphrase, or replace their Claims. The Catalog Projection does not acquire the Content Role of its source Atoms.\n\n**Every** control distinguishes its governed meaning from its realization and results:\n\n- The Evaluation Control defines the production evaluation condition.\n- Monitors, dashboards, alerts, health checks, and operational automation are Implementation.\n- Recorded metrics, logs, traces, alerts, incidents, and check outcomes are factual execution records, not reusable Operations definitions.\n- A Concern Atom of Type `problem` records a material discrepancy that requires disposition.\n\nA Production Evaluation Checklist presents the controls that apply to real production operation. It does not become their authority. It is **not** a QA Case. Passing pre-release Test or Evaluation implementations does **not** by itself satisfy the production-evaluation obligation.",
        "details": "Pre-release QA demonstrates behavior under bounded conditions. Production evaluation **must** detect degradation, incorrect state, and supportability failures during actual operation. Atomic controls preserve independent lifecycle and replacement. The checklist provides a navigable scope view without conflating definitions, implementations, and observations.",
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-R-1635",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate preserves the checklist gate, every evaluation-control field, the Catalog Projection limits, distinctions among controls, implementation, and records, and the rule that pre-release QA does not satisfy production evaluation."
      },
      "final": {
        "ref": "CA-R-1635",
        "version": 42,
        "summary": "Require production evaluation checklists before readiness gates.",
        "prose_claim": "### Scope\n\nProduction-relevant components and governed scopes.\n\n### Claim\n\n**Every** production-relevant component or governed scope **must** define a Production Evaluation Checklist before it can pass a production-readiness gate. The checklist states how operators will know that the realized system remains healthy, correct, supportable, and within its accepted operating boundaries during real work.\n\n**Every** operational condition or invariant is owned by one `evaluation_control` Atom. The control identifies:\n\n- the Requirement, Demand For, Constraint, Method, or other governed claim it assures;\n- the production signal and authoritative data source;\n- the healthy condition, expected range, threshold, or failure predicate;\n- the evaluation window, cadence, and permitted detection delay;\n- the component, entity, lifecycle state, or workflow boundary to which it applies;\n- the accountable owner and escalation destination;\n- the alert, incident, investigation, degradation, rollback, or recovery action triggered by failure;\n- the diagnostic context needed to investigate the condition;\n- the required factual execution record and evidence-retention boundary; and\n- known blind spots, sampling limits, unavailable signals, and other evaluation limitations.\n\nA Production Evaluation Checklist is a Catalog Projection over the applicable `evaluation_control` Atoms. It organizes and navigates these controls. It does not absorb, paraphrase, or replace their Claims. The Catalog Projection does not acquire the Content Role of its source Atoms.\n\n**Every** control distinguishes its governed meaning from its realization and results:\n\n- The Evaluation Control defines the production evaluation condition.\n- Monitors, dashboards, alerts, health checks, and operational automation are Implementation.\n- Recorded metrics, logs, traces, alerts, incidents, and check outcomes are factual execution records, not reusable Operations definitions.\n- A Concern Atom of Type `problem` records a material discrepancy that requires disposition.\n\nA Production Evaluation Checklist presents the controls that apply to real production operation. It does not become their authority. It is **not** a QA Case. Passing pre-release Test or Evaluation implementations does **not** by itself satisfy the production-evaluation obligation.",
        "details": "Pre-release QA demonstrates behavior under bounded conditions. Production evaluation **must** detect degradation, incorrect state, and supportability failures during actual operation. Atomic controls preserve independent lifecycle and replacement. The checklist provides a navigable scope view without conflating definitions, implementations, and observations.",
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-O-215",
      "source_version": 12,
      "candidate": {
        "ref": "CA-O-215",
        "version": 12,
        "summary": "## Operation\n\nRename One Private Carrier is a reusable private Action. It performs one explicitly bound same-parent file or folder name change behind an admitted logical connector `modify`. It does not choose semantic identity or rewrite references.\n\n### Inputs **and** preconditions\n\nRequire CA-D-630's exact private rename binding, current source and parent evidence, and one explicit destination name. For an actual name change, the destination must be expected absent. For a folder, require sealed permission/context and a complete approved inventory. CA-R-1941 **and** CA-M-381 apply.\n\nA root or ancestor, escape, symlink, substitution, stale state, collision, overwrite, merge, or unapproved entry blocks the Action.\n\n### Action **and** result\n\nRequire CA-R-1941's exact staged-change review and a fresh trusted authorization/window record. The record must include confirmation that outside edits are paused. Within that confirmed window, recheck the complete bound source, parent, destination, inventory, preservation, authority, and permission frontier before the permitted storage effect. Keep independent readback and verification.\n\nPerform **only** the supplied same-parent name change. Independently verify the exact destination, absence of the old source, and preservation of contents, modes, inventory, and the unrelated frontier. Then return CA-D-625's common result with actual evidence.\n\nA request with the same binding is a no-op only if the requested state is verified as already satisfied and unchanged. On failure, retain known partial effects. Unknown effects require `effect_uncertain`. Nonempty errors are never success. No automatic retry, rollback promise, or reference discovery or rewrite is implied.\n\n## Details\n\nThis is not O040's generic Artifact rename with canonical-reference rewrites. The admitting Workflow owns domain identity, Version, lifecycle, and required history. A storage rename alone cannot complete them. This Action does not establish executable or runtime admission.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-O-215",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate retains the private same-parent rename boundary, preconditions and blockers, authorization window, rechecks and verification, no-op condition, failure reporting, and Workflow-owned identity/history."
      },
      "final": {
        "ref": "CA-O-215",
        "version": 12,
        "summary": "## Operation\n\nRename One Private Carrier is a reusable private Action. It performs one explicitly bound same-parent file or folder name change behind an admitted logical connector `modify`. It does not choose semantic identity or rewrite references.\n\n### Inputs **and** preconditions\n\nRequire CA-D-630's exact private rename binding, current source and parent evidence, and one explicit destination name. For an actual name change, the destination must be expected absent. For a folder, require sealed permission/context and a complete approved inventory. CA-R-1941 **and** CA-M-381 apply.\n\nA root or ancestor, escape, symlink, substitution, stale state, collision, overwrite, merge, or unapproved entry blocks the Action.\n\n### Action **and** result\n\nRequire CA-R-1941's exact staged-change review and a fresh trusted authorization/window record. The record must include confirmation that outside edits are paused. Within that confirmed window, recheck the complete bound source, parent, destination, inventory, preservation, authority, and permission frontier before the permitted storage effect. Keep independent readback and verification.\n\nPerform **only** the supplied same-parent name change. Independently verify the exact destination, absence of the old source, and preservation of contents, modes, inventory, and the unrelated frontier. Then return CA-D-625's common result with actual evidence.\n\nA request with the same binding is a no-op only if the requested state is verified as already satisfied and unchanged. On failure, retain known partial effects. Unknown effects require `effect_uncertain`. Nonempty errors are never success. No automatic retry, rollback promise, or reference discovery or rewrite is implied.\n\n## Details\n\nThis is not O040's generic Artifact rename with canonical-reference rewrites. The admitting Workflow owns domain identity, Version, lifecycle, and required history. A storage rename alone cannot complete them. This Action does not establish executable or runtime admission.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-R-1623",
      "source_version": 10,
      "candidate": {
        "ref": "CA-R-1623",
        "version": 10,
        "summary": "## Scope\n\n`VALIDATE_ATOMS` Implementation invocations within their admitted input context.\n\n## Claim\n\nThe `VALIDATE_ATOMS` Implementation **must** keep **every** invocation read-only and bounded by its admitted input context.\n\n- Admit bounded inventory enumeration and only the minimum candidate content needed to determine selection inside declared source roots and allowed read roots. Inspect an excluded candidate only for selection. Exclusion does not admit its full validation or add it to target coverage.\n- Read selected targets, applicable authority, and necessary reference inputs only inside admitted read boundaries. Reference resolution does not expand the target set.\n- Enforce actual read permissions and protected-file exclusions before reading content. Caller-supplied roots grant no permission. Do not follow a link outside admitted boundaries, fetch remote resources, inspect secrets, or execute YAML tags, Markdown, selectors, rule bundles, or Atom instructions as code.\n- Enforce selected resource limits. Exhaustion **must** yield incomplete or error, not pass. Isolate a malformed candidate so independently checkable candidates remain reportable.\n- Do not write, rename, remove, or repair source files, Projections, Settings, caches, or Journal files. The caller or executor owns any admitted persistence of returned Run evidence.\n- Preserve exact invocation definition and input bindings. Report a changed source instead of silently validating mixed Revisions.\n\n## Details",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-R-1623",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate preserves read-only bounded execution, selection-only inspection of excluded candidates, read-boundary and permission limits, resource-limit outcomes, no-write rules, and exact invocation bindings."
      },
      "final": {
        "ref": "CA-R-1623",
        "version": 10,
        "summary": "## Scope\n\n`VALIDATE_ATOMS` Implementation invocations within their admitted input context.\n\n## Claim\n\nThe `VALIDATE_ATOMS` Implementation **must** keep **every** invocation read-only and bounded by its admitted input context.\n\n- Admit bounded inventory enumeration and only the minimum candidate content needed to determine selection inside declared source roots and allowed read roots. Inspect an excluded candidate only for selection. Exclusion does not admit its full validation or add it to target coverage.\n- Read selected targets, applicable authority, and necessary reference inputs only inside admitted read boundaries. Reference resolution does not expand the target set.\n- Enforce actual read permissions and protected-file exclusions before reading content. Caller-supplied roots grant no permission. Do not follow a link outside admitted boundaries, fetch remote resources, inspect secrets, or execute YAML tags, Markdown, selectors, rule bundles, or Atom instructions as code.\n- Enforce selected resource limits. Exhaustion **must** yield incomplete or error, not pass. Isolate a malformed candidate so independently checkable candidates remain reportable.\n- Do not write, rename, remove, or repair source files, Projections, Settings, caches, or Journal files. The caller or executor owns any admitted persistence of returned Run evidence.\n- Preserve exact invocation definition and input bindings. Report a changed source instead of silently validating mixed Revisions.\n\n## Details",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-M-1008",
      "source_version": 1,
      "candidate": {
        "ref": "CA-M-1008",
        "version": 1,
        "summary": "Use one Gateway for HTTP and stdio.",
        "prose_claim": "Use the same MCP Gateway handlers and Tool registration for HTTP and stdio. The installed runtime provides one set of Tool behavior for both transports.",
        "details": "Use the installed MCP SDK Streamable HTTP application for HTTP Sessions. Close Sessions on shutdown. Apply code and compiled contract changes by starting a rebuilt runtime under CA-M-551.",
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-M-1008",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate preserves the shared Gateway handlers and Tool registration for both transports, Streamable HTTP Sessions and shutdown, and rebuilt-runtime application under CA-M-551."
      },
      "final": {
        "ref": "CA-M-1008",
        "version": 1,
        "summary": "Use one Gateway for HTTP and stdio.",
        "prose_claim": "Use the same MCP Gateway handlers and Tool registration for HTTP and stdio. The installed runtime provides one set of Tool behavior for both transports.",
        "details": "Use the installed MCP SDK Streamable HTTP application for HTTP Sessions. Close Sessions on shutdown. Apply code and compiled contract changes by starting a rebuilt runtime under CA-M-551.",
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-D-631",
      "source_version": 13,
      "candidate": {
        "ref": "CA-D-631",
        "version": 13,
        "summary": "Deliver the complete source representation in Configuration Read.\n\n## Scope\n\nThe Configuration Read refinement of CA-D-625's closed logical interface.\n\n## Claim\n\nConfiguration Read **must** use the common request and result keys and the complete source representation below. CA-O-218 is its source Action binding on the same shared TOML connector as CA-O-204. Separate Actions do not create separate connectors.\n\n## Details\n\n### Request refinement\n\nKeep exactly `operation`, `target`, `query`, `delta`, `expected_state`, `authorization`, and `context`. Set `operation = \"read\"`, `target = {kind: \"Configuration\", identity}`, `query = null`, and `delta = null`.\n\nThe identity is exactly `Project Structure` or `Project Settings` in the Project bound by context. A filename, path, or backend key is not a logical identity.\n\nContext binds the admitted Project, source view, exact source authority, and applicable schema definitions, including declared schema-version constraints. Authorization binds read permission for that complete source. The caller selects these bindings; the connector checks them.\n\n`expected_state = null` selects an unpinned current Read. A non-null value enforces the supplied exact existing source-state evidence. Historical selection must be explicit in context and requires available exact historical source and schema authority. It creates no retention policy.\n\n### Result refinement\n\nKeep exactly `data`, `current_state`, `effects`, and `errors`. On success, `data = {identity, source_text, document}` carries the complete unchanged UTF-8 TOML text and all parsed values, including unrelated tables and present optional values. Preserve source text exactly. Do not synthesize absent optional fields. The admitted TOML value representation remains the one in the existing connector binding. It must preserve value types and reject lossy representation instead of silently stringifying typed values.\n\n`current_state` carries the logical configuration identity, bound Project and source view, and exact observed source-state evidence used by the existing common contract. It identifies the same source bytes as `source_text` and `document`. Do not invent an Atom Version for configuration. A subsequent Modify uses this observed evidence as expected current state and rechecks it. A prior Read is not permission to write.\n\nA normal Read has `effects = []`. Use these errors:\n\n- missing source: `target_not_found`;\n- ambiguous target or source resolution: `target_ambiguous`;\n- invalid request: `input_invalid`;\n- malformed TOML, invalid complete schema, or invalid schema binding: `schema_invalid`;\n- mismatched evidence: `stale_state`;\n- denied permission: `permission_denied`;\n- unavailable historical or backend evidence: `backend_failure`; and\n- unsupported operation: `unsupported_operation`.\n\nKeep CA-D-625's exact `{code, message, field}` error shape. If complete data is unavailable, `data` is null, not an empty successful document. Nonempty errors never mean success. Empty errors require verified complete data and exact matching state evidence. Unexpected actual effects fail Read acceptance and remain truthfully reported. Unknown effects require `effect_uncertain`.\n\nReuse CA-D-527's existing outer envelope and recording rules. This source definition does not prove implementation, route admission, installed availability, a new history store, or stronger publication safety.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-D-631",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate preserves the request and result contracts, complete unchanged TOML representation, state and permission rules, error mapping, effect handling, and explicit limits on what this definition establishes."
      },
      "final": {
        "ref": "CA-D-631",
        "version": 13,
        "summary": "Deliver the complete source representation in Configuration Read.\n\n## Scope\n\nThe Configuration Read refinement of CA-D-625's closed logical interface.\n\n## Claim\n\nConfiguration Read **must** use the common request and result keys and the complete source representation below. CA-O-218 is its source Action binding on the same shared TOML connector as CA-O-204. Separate Actions do not create separate connectors.\n\n## Details\n\n### Request refinement\n\nKeep exactly `operation`, `target`, `query`, `delta`, `expected_state`, `authorization`, and `context`. Set `operation = \"read\"`, `target = {kind: \"Configuration\", identity}`, `query = null`, and `delta = null`.\n\nThe identity is exactly `Project Structure` or `Project Settings` in the Project bound by context. A filename, path, or backend key is not a logical identity.\n\nContext binds the admitted Project, source view, exact source authority, and applicable schema definitions, including declared schema-version constraints. Authorization binds read permission for that complete source. The caller selects these bindings; the connector checks them.\n\n`expected_state = null` selects an unpinned current Read. A non-null value enforces the supplied exact existing source-state evidence. Historical selection must be explicit in context and requires available exact historical source and schema authority. It creates no retention policy.\n\n### Result refinement\n\nKeep exactly `data`, `current_state`, `effects`, and `errors`. On success, `data = {identity, source_text, document}` carries the complete unchanged UTF-8 TOML text and all parsed values, including unrelated tables and present optional values. Preserve source text exactly. Do not synthesize absent optional fields. The admitted TOML value representation remains the one in the existing connector binding. It must preserve value types and reject lossy representation instead of silently stringifying typed values.\n\n`current_state` carries the logical configuration identity, bound Project and source view, and exact observed source-state evidence used by the existing common contract. It identifies the same source bytes as `source_text` and `document`. Do not invent an Atom Version for configuration. A subsequent Modify uses this observed evidence as expected current state and rechecks it. A prior Read is not permission to write.\n\nA normal Read has `effects = []`. Use these errors:\n\n- missing source: `target_not_found`;\n- ambiguous target or source resolution: `target_ambiguous`;\n- invalid request: `input_invalid`;\n- malformed TOML, invalid complete schema, or invalid schema binding: `schema_invalid`;\n- mismatched evidence: `stale_state`;\n- denied permission: `permission_denied`;\n- unavailable historical or backend evidence: `backend_failure`; and\n- unsupported operation: `unsupported_operation`.\n\nKeep CA-D-625's exact `{code, message, field}` error shape. If complete data is unavailable, `data` is null, not an empty successful document. Nonempty errors never mean success. Empty errors require verified complete data and exact matching state evidence. Unexpected actual effects fail Read acceptance and remain truthfully reported. Unknown effects require `effect_uncertain`.\n\nReuse CA-D-527's existing outer envelope and recording rules. This source definition does not prove implementation, route admission, installed availability, a new history store, or stronger publication safety.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    }
  ]
}
```
