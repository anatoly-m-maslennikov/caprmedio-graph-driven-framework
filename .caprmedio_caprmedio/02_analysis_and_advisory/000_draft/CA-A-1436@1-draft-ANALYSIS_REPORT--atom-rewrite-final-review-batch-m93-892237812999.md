---
identity:
  atom_id: CA-A-1436
  ref_id: CA-A-1436@1-draft
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
  updated_at: '2026-11-12T19:00:30.471013+00:00'
destination:
  file:
    name: CA-A-1436@1-draft-ANALYSIS_REPORT--atom-rewrite-final-review-batch-m93-892237812999.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Atom rewrite final review batch m93 892237812999

## Details

```json
{
  "candidates": [
    {
      "ref": "CA-M-399",
      "version": 20,
      "summary": "Record business Workflow lifecycle events separately from technical diagnostics",
      "prose_claim": "Keep technical diagnostics on structured stdout/stderr streams. Record actual business Workflow lifecycle events through the declared Journal owner. Do not turn a technical warning into a business event.",
      "details": "### Scope\n\nThis Method applies to new or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.\n\n1. Emit technical diagnostics through the shared logger with the actual Project prefix and sanitized context. The Docker runtime captures these streams under its bounded retention/back-pressure configuration; use stderr when stdout carries MCP/Tool protocol or result data.\n   For the Project Atom Lifecycle backend, emit a stdout INFO event when each step starts and when it ends as done or failed. Include the step and elapsed time in the end event. Keep input values and carrier contents out of the log.\n2. Apply CA-M-396 to severity: input and Project artifact issues use WARNING; ERROR is reserved for real blocking runtime failures. Do not confuse a response error or a failed business Workflow with ERROR-level logging.\n3. For an actually admitted/started business Workflow, record its observed started, failed and completed lifecycle transitions, as applicable, through its executor and the shared Journal owner. A technical cause can explain a real business failure. Do not copy technical log records or stack traces into the Journal.\n4. A preflight rejection with no admitted/started business Workflow must not fabricate a Workflow, Run, started/failed event or completion event. Direct read-only Tool calls do not gain hidden Journal effects from logging or generic error handling.\n5. Keep business records truthful and independent from Git and technical-log retention. Journal incompleteness is not an admission gate. Preserve existing historical Journal bytes and do not rewrite old technical entries as part of this Method.",
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-M-542",
      "version": 2,
      "summary": "Prefer technologies and interfaces familiar to AI Agents",
      "prose_claim": "Prefer technologies and interfaces that AI Agents already know. Use custom technologies and interfaces when their value justifies the extra learning and maintenance.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-R-1041",
      "version": 18,
      "summary": "Coordinate explicit Atom replacement intent and report its actual effects\n\n## Scope\n\nThis Rule applies to REPLACE_ATOM's explicit singular or frozen bulk replacement intent, delegated application boundary and truthful result evidence.\n\n## Claim\n\nREPLACE_ATOM **must** coordinate explicit Atom replacement intent **without** owning generic Carrier creation, relation editing, **or** archival semantics.\n\n- An atomic replacement accepts **`=1`** exact active predecessor Atom ID, **`>=1`** distinct exact sealed prepared-new successor Carrier sets, **and** action context. Each prepared-new successor set contains complete sealed content, assigned identity, and destination; no preexisting-successor mode is admitted.\n- Reject a missing, duplicate, inactive, or self-referential predecessor; missing, duplicate, partial, or unsealed prepared-new successor content; or a used successor identity or destination. Return a sealed replacement action containing the supplied predecessor, complete prepared-new successor set, and predecessor archive intent.\n- A several-predecessor Workflow supplies explicit mappings but invokes one independently admitted replacement Action per predecessor. Stop at its first failed Action, retain completed replacements and leave the remainder untouched; do not promise a cross-predecessor all-or-nothing effect.\n- Use the canonical Atom lifecycle capability to materialize only the complete sealed prepared-new successor set, establish every successor as Active, and then archive the predecessor; pass the explicit IDs **to** the provenance pipeline. Do **not** infer successor content, perform generic Carrier creation, or write replacement relations **in** Atom Carriers.\n- Default **to** a mutation-free dry run. Permit apply **only** through authorized project-local MCP delegation with a sealed Initiative action envelope.\n- A successful delegated effect requires durable COMMIT_TRIGGER intake acknowledgment **before** MCP reports success. An intake acknowledgment is necessary for that handoff **but** is **not** proof that replacement was applied **or** that its authoritative Journal event **and** Run evidence were durably recorded. REPLACE_ATOM does **not** append the Journal, stage files, **or** create a Git Commit.\n- Distinguish a prepared sealed description, a deferred delegated request, **and** an actually applied replacement. Prepared **or** deferred results **must** state that the archive effect is **not** applied; acceptance, sealing, **or** intake alone **must not** be reported as completed replacement.\n- At the actual effect boundary, revalidate the exact predecessor and every prepared-new successor's complete sealed content, identity, unused destination, current source/destination conditions, complete sealed mapping, and current delegated authority. Materialize every successor and verify each is durably Active **before** predecessor archival. Use CA-O-051's whole-Carrier transition: preserve the predecessor's body, Summary, Type, identity **and** frontmatter values except actual archive Status, Version **and** Updated At. Its actual changed archive Revision advances Version by **`=1`** and uses the applicable canonical archive encoding; retain exact before-Revision bytes and Version as required history.\n- Report actual replacement completion **only** with observed canonical lifecycle effects **and** durable authoritative archive-event evidence naming the explicit predecessor **and** complete **`>=1`** materialized Active successor set under CA-R-807. Preserve each explicit mapping and its actual result; partial or uncertain effects must not be described as completed replacement.\n- Retain exact actual Workflow/Action Run identities, definition Revisions, input/result/effect references, start **and** truthful terminal/pending evidence **and** actual durable receipts under the reviewed CA-P-1443/CA-P-1451 shared contract. Recording failure leaves completion evidence blocked **and** pending evidence intact; preserve the missing-recording disposition **without** replaying performed replacement **or** resetting authority. An unpersisted acknowledgment is **not** Journal completion.\n\n## Details\n\nCA-O-031 owns the replacement Action; CA-O-051 and CA-R-807 govern canonical lifecycle effects and immutable replacement history. CA-E-299 covers the prepared description; CA-E-247 covers admission, delegated-effect and receipt distinctions. The Tool admits no preexisting-successor mode, does not infer missing successor content, and gains no lifecycle or Journal authority from intake acceptance.\n\nEvery Summary value change requires a new Atom ID and predecessor archival through this replacement Workflow, even when the Claim remains unchanged. Return the explicit target, created and archived IDs separately: for target `100` replaced by new Atom `200`, the result identifies target `100`, created `200` and archived `100`. Replacement does not automatically retarget incoming references; independent Find and Modify Workflows select and update those referencing Atoms. Resume and retry policy for independent replacements remains deferred. Current source, destination, permission, preview and each replacement's internal storage-effect safeguards remain required.",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-E-684",
      "version": 10,
      "summary": "Verify Workbench Workspace Views, Query Log and native UI delivery",
      "prose_claim": "Use the real native Codex plugin UI and MCP surfaces. Do not treat a browser page as the plugin UI. Verify that the host-provided native session opens its isolated Workspace with at least one View for the explicit Project. Verify a read-only Workspace/View operation through the shared backend.\n\nVerify the native UI, standalone browser and MCP use the same Workspace/View effects. Verify that two Codex chats keep separate Workspaces and unsaved SQL. Verify no standalone chat, synthetic native session, magic Workflow, code runner, scheduler, or retry behavior is required.\n\nIn a disposable protocol host and disposable valid Project, verify that `workspace_open` alone exposes `ui://caprmedio/workbench.html`; the compatibility probe remains separately linked; unknown resource URIs and unexpected inputs fail. Verify the resource is self-contained `text/html;profile=mcp-app` with no external script or stylesheet references, Workbench HTTP request, browser opening, or second server.\n\nVerify native bootstrap accepts only the `workspace_open` host tool input's non-empty `session_id` and explicit `project_root` plus its initial structured result. Exercise either input/result arrival order, require the exact supplied IDs and initial Workspace, and verify no second `workspace_open` call occurs. For absent input or result, verify a binding error is shown and no backend call, URL/localStorage identity fallback, synthetic native session, or alternative Workspace selection occurs.\n\nThrough the native MCP transport, exercise every existing Workspace/View and query-log operation. Each call retains the exact `project_root`, uses one `tools/call`, preserves `structuredContent`, rejects `isError`, and reaches the shared handler. Check transport binding and error propagation without repeating the shared operation acceptance cases. Native mode must not apply standalone URL, localStorage or draft-migration behavior.\n\nIn a real new or resumed Codex chat with the installed local plugin and a disposable valid Project/Workspace, invoke the real `workspace_open` with the hook-supplied native session ID and trusted Project root. Verify that Codex renders the Workbench in-chat; the shown Workspace ID equals the tool input session; a read-only Workspace/View operation traverses the bridge; state is visible through ordinary MCP or standalone use of the same backend; and no browser, second chat, or second MCP connection appears. Exercise fullscreen or move-to-panel only if the host offers it and report the observed placement.\n\nA synthetic or disposable-host test proves protocol and application behavior only. Do not use it to claim native Codex rendering, right-panel support, or complete native Workbench delivery. The read-only probe separately verifies standard MCP Apps compatibility and must not be used as Workbench activation evidence.\n\nCall the read-only `workbench_ui_probe` through the existing MCP connection. Verify its component renders inside Codex, displays the initial host tool result, and reports a successful separate `workbench_ui_ping` bridge call. Verify resource and tools work over real MCP transport, reject unexpected arguments and unknown resource URIs, and do not start Workbench. Verify inline/fullscreen declaration, current and offered mode display, Expand only when fullscreen is available, accepted/inline-retained/rejected/unsupported results, actual returned-mode display, and no unavailable request. If the real host does not render native UI, record delivery as incomplete and do not substitute a browser page. Observe move-to-panel only if offered; otherwise record right-panel delivery as unproven.\n\nUse a fixture whose directory basename differs from its declared Project name. Verify HTTP and MCP workspace_open/workspace_get return the declared project_name and the native Workbench header displays it. Verify that Workspace documents do not gain a persisted Project-name field. A native initial Workspace result missing project_name reports a binding error before further tool calls; no directory-basename fallback is used.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-O-190",
      "version": 11,
      "summary": "Discover a matching open public `main` PR\n\n## Action\n\nDiscover a matching public `main` PR **means** the native read operation that returns zero or one actual open PR identity for the selected personal remote and `amm/dev` to `main` boundary.\n\n## Details\n\nThe Tool-call input, result, and report references remain evidence of this Action Run. This Action does not create or update a PR. It does not claim an MCP route.",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-E-357",
      "version": 23,
      "summary": "Reject a one-shot object without persistent ownership",
      "prose_claim": "#### Claim checked\n\nAdmit one PROGRAMMATIC object **only** **when** it requires identity across calls **and** owns state, an invariant, a resource, a lifecycle, **or** a replaceable adapter.\n\n#### Test case\n\nEvaluate one changed object that **only** wraps a bounded one-shot effect **and** owns no responsibility across calls.\n\n#### Acceptance criteria\n\nPass **only** **when** the object is rejected **and** the effect is allocated **to** a specifically named bounded function.\n\n#### Failure disposition\n\nReject the object **until** persistent ownership is demonstrated **or** the wrapper is replaced by a function.\n\n#### Sources\n\n- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-R-1441",
      "version": 26,
      "summary": "Define Default Settings as the baseline Settings Artifact",
      "prose_claim": "The definition of Default Settings.\n\nDefault Settings **means** the authoritative Artifact that contains reusable baseline values for registered CAPRMEDIO Framework Instance Settings parameters. Default Settings are **not** Project initialization inputs **or** a Project's explicit Operator selections.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-D-279",
      "version": 26,
      "summary": "Serialize Markdown prose paragraphs as unwrapped lines",
      "prose_claim": "Markdown Atom Carrier Main Content prose paragraphs.\n\n**Every** Markdown Atom Carrier Main Content prose paragraph **must** use one unwrapped source line. Use one blank line between adjacent paragraphs.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-O-178",
      "version": 17,
      "summary": "Install the runtime and project-local `ca` Skill\n\n## Step\n\nThis Step invokes CA-O-169 once with phase `install`. It copies compiled `LAYER_1_FRAMEWORK_METHODOLOGY/`, preserves protected configuration and Project state, installs Engine `.install` into the Project runtime package, and installs the `ca` payload.\n\n## Details\n\nOnly this Step clears replaceable installed Framework members, copies the product as-is, installs `ca`, and restarts or reuses Project MCP for Docker/MCP smoke. It preserves settings and Project state. It does not alter authoring, push, create a PR, or retry an uncertain effect.\n\nReuse canonical image preparation only after the Workflow's full suite is green. This occurrence also owns CA-O-169's post-smoke selected-Project retention. Keep the exact admitted current-Version candidate. Remove only proven owned unused noncandidate images. Preserve all container references and other Projects' images, and report pending cleanup. Same fingerprint alone does not preserve an older rebuild. No additional retirement Step is inserted into CA-O-164.",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-D-491",
      "version": 15,
      "summary": "Deliver the VALIDATE_ATOMS command and test assets\n\n## Scope\n\nThe `VALIDATE_ATOMS` command Carrier and its delivered test assets in TOOLS.\n\n## Claim\n\nThe `VALIDATE_ATOMS` executable Carrier **must** be delivered as `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms.py`, with its automated tests **in** the adjacent `tests/` directory.\n\n- Expose `validate_atoms.py --input <request.json>` **and** `--input -` for standard input.\n- Emit **=1** JSON result on standard output under CA-D-493-TOOLS-ENG_DECISION--serialize-atom-validator-results; Human execution diagnostics belong on standard error.\n- The path identifies an Implementation Artifact inside TOOLS, **not** a newly declared Scope Unit. It carries the implementation bound under CA-R-1622-TOOLS-RULE--implement-atom-carrier-validation-in-validate-atoms, **not** another Workflow authority.\n- Store the end-to-end command tests **in** `VALIDATE_ATOMS/tests/test_validate_atoms_e2e.py` relative **to** the delivered TOOLS directory.\n- Store mock Markdown Atoms **and** supporting mock context **in** `VALIDATE_ATOMS/tests/fixtures/`, with `good/`, `bad/`, `mixed/`, **and** `context/` groups. Fixture files are test inputs, **not** active governing Project Atoms.\n- Store the case/coverage manifest **in** `VALIDATE_ATOMS/tests/cases.json` **and** independently reviewed expected reports **in** `VALIDATE_ATOMS/tests/expected/<case_id>.json`. **Every** manifest case identifies its fixture inputs, request, governing rule identities/Revisions, expected report, **and** expected exit code.\n\n- `cases.json` is a closed object with `schema_version: 1` **and** `cases`: a nonempty array. Each case has a unique nonempty `case_id`, `request` path, nonempty `fixture_paths` list, nonempty `authority` list of exact Atom Bindings under CA-D-492-TOOLS-DELIVERY--serialize-atom-validator-requests, nonempty `check_codes` list, `expected_report` path, **and** integer `expected_exit_code` **in** (0, 1, 2, 3). All case paths are relative **to** `tests/`, remain inside it, **and** cannot escape through symlinks. Expected reports follow CA-D-493-TOOLS-DELIVERY--serialize-atom-validator-results.\n- Include positive/negative/exception/boundary coverage for every supported check **and** declared failure class; reusable fixture cases may cover multiple rules. The harness verifies the matrix against the independently resolved obligation inventory, **not** just the list of implemented checks.\n\n## Details",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    }
  ],
  "review": [
    {
      "ref": "CA-M-399",
      "version": 20,
      "checks": {
        "main_subject": "pass",
        "summary": "pass",
        "claim": "pass",
        "dependencies": "pass",
        "sections": "pass",
        "fidelity": "pass"
      },
      "issues": []
    },
    {
      "ref": "CA-M-542",
      "version": 2,
      "checks": {
        "main_subject": "pass",
        "summary": "pass",
        "claim": "pass",
        "dependencies": "pass",
        "sections": "pass",
        "fidelity": "pass"
      },
      "issues": []
    },
    {
      "ref": "CA-R-1041",
      "version": 18,
      "checks": {
        "main_subject": "pass",
        "summary": "pass",
        "claim": "pass",
        "dependencies": "pass",
        "sections": "pass",
        "fidelity": "pass"
      },
      "issues": []
    },
    {
      "ref": "CA-E-684",
      "version": 10,
      "checks": {
        "main_subject": "pass",
        "summary": "pass",
        "claim": "pass",
        "dependencies": "pass",
        "sections": "pass",
        "fidelity": "pass"
      },
      "issues": []
    },
    {
      "ref": "CA-O-190",
      "version": 11,
      "checks": {
        "main_subject": "pass",
        "summary": "pass",
        "claim": "pass",
        "dependencies": "pass",
        "sections": "pass",
        "fidelity": "pass"
      },
      "issues": []
    },
    {
      "ref": "CA-E-357",
      "version": 23,
      "checks": {
        "main_subject": "pass",
        "summary": "pass",
        "claim": "pass",
        "dependencies": "pass",
        "sections": "pass",
        "fidelity": "pass"
      },
      "issues": []
    },
    {
      "ref": "CA-R-1441",
      "version": 26,
      "checks": {
        "main_subject": "pass",
        "summary": "pass",
        "claim": "pass",
        "dependencies": "pass",
        "sections": "pass",
        "fidelity": "pass"
      },
      "issues": []
    },
    {
      "ref": "CA-D-279",
      "version": 26,
      "checks": {
        "main_subject": "pass",
        "summary": "pass",
        "claim": "pass",
        "dependencies": "pass",
        "sections": "pass",
        "fidelity": "pass"
      },
      "issues": []
    },
    {
      "ref": "CA-O-178",
      "version": 17,
      "checks": {
        "main_subject": "pass",
        "summary": "pass",
        "claim": "pass",
        "dependencies": "pass",
        "sections": "pass",
        "fidelity": "pass"
      },
      "issues": []
    },
    {
      "ref": "CA-D-491",
      "version": 15,
      "checks": {
        "main_subject": "pass",
        "summary": "pass",
        "claim": "pass",
        "dependencies": "pass",
        "sections": "pass",
        "fidelity": "pass"
      },
      "issues": []
    }
  ]
}
```