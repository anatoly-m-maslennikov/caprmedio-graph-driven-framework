---
identity:
  atom_id: CA-A-1443
  ref_id: CA-A-1443@1-draft
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
  updated_at: '2026-11-12T20:38:48.654768+00:00'
destination:
  file:
    name: CA-A-1443@1-draft-ANALYSIS_REPORT--atom-rewrite-one-pass-benchmark-6oc1f0r-luna-high.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Atom rewrite one-pass benchmark 6oc1f0r Luna high

## Details

```json
{
  "model": "gpt-6-luna",
  "reasoning_effort": "high",
  "intent": "Rewrite and review in one isolated session.",
  "candidates": [
    {
      "ref": "CA-M-399",
      "version": 20,
      "summary": "Record business Workflow lifecycle separately from technical diagnostics",
      "prose_claim": "Send technical diagnostics to structured stdout/stderr streams. Record actual business Workflow lifecycle events through the declared Journal owner. Do not turn a technical warning into a business event.",
      "details": "### Scope\n\nNew or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters, and their public operation boundaries.\n\n1. Send technical diagnostics through the shared logger. Use the actual Project prefix and sanitized context. The Docker runtime captures these streams under its bounded retention and back-pressure configuration. Use stderr when stdout carries MCP/Tool protocol or result data.\n   For the Project Atom Lifecycle backend, emit a stdout INFO event when each step starts and when it ends as done or failed. Include the step and elapsed time in the end event. Keep input values and carrier contents out of the log.\n2. Apply CA-M-396 to severity. Use WARNING for input and Project artifact issues. Reserve ERROR for real blocking runtime failures. A response error or failed business Workflow does not by itself warrant ERROR-level logging.\n3. For a business Workflow that was actually admitted and started, record its observed started, failed, and completed lifecycle transitions, as applicable, through its executor and the shared Journal owner. A technical cause may explain a real business failure. Do not copy technical log records or stack traces into the Journal.\n4. If preflight rejects a request and no business Workflow was admitted or started, do not fabricate a Workflow, Run, started/failed event, or completion event. Direct read-only Tool calls gain no hidden Journal effects from logging or generic error handling.\n5. Keep business records truthful and independent of Git and technical-log retention. Journal incompleteness is not an admission gate. Preserve existing historical Journal bytes. Do not rewrite old technical entries as part of this Method.",
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-M-542",
      "version": 2,
      "summary": "Prefer well-known technologies and interfaces",
      "prose_claim": "Prefer technologies and interfaces that AI Agents already know. Use a custom technology or interface when its value justifies the extra learning and maintenance.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-R-1041",
      "version": 18,
      "summary": "Coordinate Atom replacement intent\n\n## Scope\n\nREPLACE_ATOM’s explicit singular or frozen bulk replacement intent, delegated application boundary, and truthful result evidence.\n\n## Claim\n\nREPLACE_ATOM **must** coordinate explicit Atom replacement intent. It must **not** own generic Carrier creation, relation editing, **or** archival semantics.\n\n- An atomic replacement accepts **`=1`** exact active predecessor Atom ID, **`>=1`** distinct exact sealed prepared-new successor Carrier sets, **and** action context. Each prepared-new successor set contains complete sealed content, assigned identity, and destination. No preexisting-successor mode is admitted.\n- Reject a missing, duplicate, inactive, or self-referential predecessor; missing, duplicate, partial, or unsealed prepared-new successor content; or a used successor identity or destination. Return a sealed replacement action containing the supplied predecessor, complete prepared-new successor set, and predecessor archive intent.\n- A several-predecessor Workflow supplies explicit mappings. It invokes one independently admitted replacement Action per predecessor. Stop at the first failed Action, retain completed replacements, and leave the remainder untouched. Do not promise an all-or-nothing effect across predecessors.\n- Use the canonical Atom lifecycle capability to materialize only the complete sealed prepared-new successor set, establish every successor as Active, and then archive the predecessor. Pass the explicit IDs **to** the provenance pipeline. Do **not** infer successor content, perform generic Carrier creation, or write replacement relations **in** Atom Carriers.\n- Default **to** a mutation-free dry run. Permit apply **only** through authorized project-local MCP delegation with a sealed Initiative action envelope.\n- A successful delegated effect requires durable COMMIT_TRIGGER intake acknowledgment **before** MCP reports success. Intake acknowledgment is necessary for that handoff, **but** does **not** prove that replacement was applied or that its authoritative Journal event **and** Run evidence were durably recorded. REPLACE_ATOM does **not** append the Journal, stage files, **or** create a Git Commit.\n- Distinguish a prepared sealed description, a deferred delegated request, and an actually applied replacement. Prepared **or** deferred results **must** state that the archive effect is **not** applied. Acceptance, sealing, **or** intake alone **must not** be reported as completed replacement.\n- At the actual effect boundary, revalidate the exact predecessor; every prepared-new successor’s complete sealed content, identity, and unused destination; current source and destination conditions; the complete sealed mapping; and current delegated authority. Materialize every successor and verify each is durably Active **before** archiving the predecessor. Use CA-O-051’s whole-Carrier transition: preserve the predecessor’s body, Summary, Type, identity, and frontmatter values except actual archive Status, Version, **and** Updated At. Its actual changed archive Revision advances Version by **`=1`** and uses the applicable canonical archive encoding. Retain exact before-Revision bytes and Version as required history.\n- Report actual replacement completion **only** with observed canonical lifecycle effects **and** durable authoritative archive-event evidence naming the explicit predecessor **and** complete **`>=1`** materialized Active successor set under CA-R-807. Preserve each explicit mapping and its actual result. Do not describe partial or uncertain effects as completed replacement.\n- Retain exact actual Workflow/Action Run identities, definition Revisions, input/result/effect references, start and truthful terminal/pending evidence, and actual durable receipts under the reviewed CA-P-1443/CA-P-1451 shared contract. If recording fails, completion evidence remains blocked and pending evidence remains intact. Preserve the missing-recording disposition without replaying a performed replacement or resetting authority. An unpersisted acknowledgment is **not** Journal completion.\n\n## Details\n\nCA-O-031 owns the replacement Action. CA-O-051 and CA-R-807 govern canonical lifecycle effects and immutable replacement history. CA-E-299 covers the prepared description. CA-E-247 covers admission, delegated-effect, and receipt distinctions. The Tool admits no preexisting-successor mode, does not infer missing successor content, and gains no lifecycle or Journal authority from intake acceptance.\n\nEvery Summary value change requires a new Atom ID and predecessor archival through this replacement Workflow, even when the Claim remains unchanged. Return the explicit target, created, and archived IDs separately. For target `100` replaced by new Atom `200`, identify target `100`, created `200`, and archived `100`. Replacement does not automatically retarget incoming references. Independent Find and Modify Workflows select and update those referencing Atoms. Resume and retry policy for independent replacements remains deferred. Current source, destination, permission, preview, and each replacement’s internal storage-effect safeguards remain required.",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-E-684",
      "version": 10,
      "summary": "Exercise Workbench Workspace Views and Query Log",
      "prose_claim": "Use the real native Codex plugin UI and MCP surfaces. A browser page is not the plugin UI. Verify that the host-provided native session opens its isolated Workspace with at least one View for the explicit Project. Verify a read-only Workspace/View operation through the shared backend.\n\nVerify that the native UI, standalone browser, and MCP use the same Workspace/View effects. Two Codex chats must keep separate Workspaces and unsaved SQL. Verify that no standalone chat, synthetic native session, magic Workflow, code runner, scheduler, or retry behavior is required.\n\nIn a disposable protocol host and disposable valid Project, verify that `workspace_open` alone exposes `ui://caprmedio/workbench.html`. Keep the compatibility probe separately linked. Unknown resource URIs and unexpected inputs must fail. Verify that the resource is self-contained `text/html;profile=mcp-app` and has no external script or stylesheet references, Workbench HTTP request, browser opening, or second server.\n\nVerify native bootstrap accepts only the `workspace_open` host tool input’s non-empty `session_id` and explicit `project_root`, plus its initial structured result. Exercise either input/result arrival order. Require the exact supplied IDs and initial Workspace, and verify that no second `workspace_open` call occurs. If input or result is absent, verify that a binding error appears and that there is no backend call, URL/localStorage identity fallback, synthetic native session, or alternative Workspace selection.\n\nThrough the native MCP transport, exercise every existing Workspace/View and query-log operation. Each call must retain the exact `project_root`, use one `tools/call`, preserve `structuredContent`, reject `isError`, and reach the shared handler. Check transport binding and error propagation without repeating the shared operation acceptance cases. Native mode must not apply standalone URL, localStorage, or draft-migration behavior.\n\nIn a real new or resumed Codex chat with the installed local plugin and a disposable valid Project/Workspace, invoke the real `workspace_open` with the hook-supplied native session ID and trusted Project root. Verify that Codex renders the Workbench in-chat; the shown Workspace ID equals the tool input session; a read-only Workspace/View operation traverses the bridge; state is visible through ordinary MCP or standalone use of the same backend; and no browser, second chat, or second MCP connection appears. Exercise fullscreen or move-to-panel only if the host offers it, and report the observed placement.\n\nA synthetic or disposable-host test proves protocol and application behavior only. It is insufficient to claim native Codex rendering, right-panel support, or complete native Workbench delivery. The read-only probe separately verifies standard MCP Apps compatibility. Do not use it as Workbench activation evidence.\n\nCall the read-only `workbench_ui_probe` through the existing MCP connection. Verify that its component renders inside Codex, displays the initial host tool result, and reports a successful separate `workbench_ui_ping` bridge call. Verify that resource and tools work over real MCP transport, reject unexpected arguments and unknown resource URIs, and do not start Workbench. Verify inline/fullscreen declaration, current and offered mode display, Expand only when fullscreen is available, accepted/inline-retained/rejected/unsupported results, actual returned-mode display, and no unavailable request. If the real host does not render native UI, record delivery as incomplete; do not substitute a browser page. Observe move-to-panel only if offered; otherwise record right-panel delivery as unproven.\n\nUse a fixture whose directory basename differs from its declared Project name. Verify that HTTP and MCP `workspace_open`/`workspace_get` return the declared `project_name` and that the native Workbench header displays it. Workspace documents must not gain a persisted Project-name field. If the native initial Workspace result lacks `project_name`, report a binding error before further tool calls; do not use a directory-basename fallback.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-O-190",
      "version": 11,
      "summary": "Discover a matching public `main` PR\n\n## Action\n\nDiscover a matching public `main` PR **means** the native read operation that returns zero or one actual open PR identity for the selected personal remote and `amm/dev`-to-`main` boundary.\n\n## Details\n\nThe Tool-call input, result, and report references remain evidence of this Action Run. This Action neither creates nor updates a PR and does not claim an MCP route.",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-E-357",
      "version": 23,
      "summary": "Reject an object without persistent ownership\n\n#### Claim checked\n\nAdmit one PROGRAMMATIC object **only** **when** it requires identity across calls **and** owns state, an invariant, a resource, a lifecycle, **or** a replaceable adapter.\n\n#### Test case\n\nEvaluate one changed object that wraps **only** a bounded one-shot effect **and** owns no responsibility across calls.\n\n#### Acceptance criteria\n\nPass **only** **when** the object is rejected **and** the effect is allocated **to** a specifically named bounded function.\n\n#### Failure disposition\n\nReject the object **until** persistent ownership is demonstrated **or** the wrapper is replaced by a function.\n\n#### Sources\n\n- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)",
      "prose_claim": "#### Claim checked\n\none PROGRAMMATIC object is admitted **only** **when** it requires identity across calls\n**and** owns state, an invariant, a resource, a lifecycle, **or** a replaceable\nadapter.\n\n#### Test case\n\nevaluate one changed object that **only** wraps a bounded one-shot effect **and** owns\nno responsibility across calls.\n\n#### Acceptance criteria\n\npass **only** **when** the object is rejected **and** the effect is allocated **to** a\nspecifically named bounded function.\n\n#### Failure disposition\n\nreject the object **until** persistent ownership is demonstrated **or** the wrapper is\nreplaced by a function.\n\n#### Sources\n\n- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-R-1441",
      "version": 26,
      "summary": "Define Default Settings",
      "prose_claim": "Default Settings **means** the authoritative Artifact that contains reusable baseline values for registered CAPRMEDIO Framework Instance Settings parameters. It does **not** mean Project initialization inputs **or** a Project’s explicit Operator selections.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-D-279",
      "version": 26,
      "summary": "Serialize Markdown Paragraphs as Unwrapped Lines",
      "prose_claim": "Every Markdown Atom Carrier Main Content prose paragraph **must** use one unwrapped source line. Put one blank line between adjacent paragraphs.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-O-178",
      "version": 17,
      "summary": "Install the runtime and project-local ca Skill\n\n## Step\n\nThis Step invokes CA-O-169 once with phase `install`. It copies compiled `LAYER_1_FRAMEWORK_METHODOLOGY/`, preserves protected configuration and Project state, installs Engine `.install` into the Project runtime package, and installs the `ca` payload.\n\n## Details\n\nOnly this Step clears replaceable installed Framework members, copies the product as-is, installs `ca`, and restarts or reuses Project MCP for Docker/MCP smoke. It preserves settings and Project state. It does not alter authoring, push, create a PR, or retry an uncertain effect.\n\nReuse canonical image preparation only after the Workflow’s full suite is green. This occurrence also owns CA-O-169’s post-smoke selected-Project retention: keep the exact admitted current-Version candidate; remove only proven-owned unused noncandidate images; preserve all container references and other Projects’ images; and report pending cleanup. Same fingerprint alone does not preserve an older rebuild. Do not insert an additional retirement Step into CA-O-164.",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-D-491",
      "version": 15,
      "summary": "Deliver the VALIDATE_ATOMS command\n\n## Scope\n\nthe `VALIDATE_ATOMS` command Carrier and its delivered test assets in TOOLS.\n\n## Claim\n\nthe `VALIDATE_ATOMS` executable Carrier **must** be delivered as `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms.py`, with its automated tests **in** the adjacent `tests/` directory.\n\n- Expose `validate_atoms.py --input <request.json>` **and** `--input -` for standard input.\n- Emit **=1** JSON result on standard output under CA-D-493-TOOLS-ENG_DECISION--serialize-atom-validator-results. Put human execution diagnostics on standard error.\n- The path identifies an Implementation Artifact inside TOOLS, **not** a newly declared Scope Unit. It carries the implementation bound under CA-R-1622-TOOLS-RULE--implement-atom-carrier-validation-in-validate-atoms, **not** another Workflow authority.\n- Store end-to-end command tests **in** `VALIDATE_ATOMS/tests/test_validate_atoms_e2e.py` relative **to** the delivered TOOLS directory.\n- Store mock Markdown Atoms **and** supporting mock context **in** `VALIDATE_ATOMS/tests/fixtures/`, in `good/`, `bad/`, `mixed/`, **and** `context/` groups. Fixture files are test inputs, **not** active governing Project Atoms.\n- Store the case/coverage manifest **in** `VALIDATE_ATOMS/tests/cases.json` **and** independently reviewed expected reports **in** `VALIDATE_ATOMS/tests/expected/<case_id>.json`. **Every** manifest case identifies its fixture inputs, request, governing rule identities/Revisions, expected report, **and** expected exit code.\n\n- `cases.json` is a closed object with `schema_version: 1` **and** `cases`: a nonempty array. Each case has a unique nonempty `case_id`, `request` path, nonempty `fixture_paths` list, nonempty `authority` list of exact Atom Bindings under CA-D-492-TOOLS-DELIVERY--serialize-atom-validator-requests, nonempty `check_codes` list, `expected_report` path, **and** integer `expected_exit_code` **in** (0, 1, 2, 3). All case paths are relative **to** `tests/`, remain inside it, **and** cannot escape through symlinks. Expected reports follow CA-D-493-TOOLS-DELIVERY--serialize-atom-validator-results.\n- Include positive, negative, exception, and boundary coverage for every supported check **and** declared failure class. Reusable fixture cases may cover multiple rules. The harness verifies the matrix against the independently resolved obligation inventory, **not** only the list of implemented checks.\n\n## Details",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    }
  ]
}
```
