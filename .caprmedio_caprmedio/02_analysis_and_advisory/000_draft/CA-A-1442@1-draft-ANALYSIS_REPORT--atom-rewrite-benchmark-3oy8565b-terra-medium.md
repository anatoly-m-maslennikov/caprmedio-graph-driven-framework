---
identity:
  atom_id: CA-A-1442
  ref_id: CA-A-1442@1-draft
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
  updated_at: '2026-11-12T20:20:10.836248+00:00'
destination:
  file:
    name: CA-A-1442@1-draft-ANALYSIS_REPORT--atom-rewrite-benchmark-3oy8565b-terra-medium.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Atom rewrite benchmark 3oy8565b Terra medium

## Details

```json
{
  "intent": "Improve prose and preserve the original meaning.",
  "candidates": [
    {
      "ref": "CA-M-399",
      "version": 20,
      "summary": "Record business Workflow events separately from technical diagnostics",
      "prose_claim": "Send technical diagnostics to structured stdout or stderr. Record actual business Workflow lifecycle events through the declared Journal owner. Do not turn a technical warning into a business event.",
      "details": "### Scope\n\nThis Method applies to new or changed PROGRAMMATIC implementation. This includes Tools, Apps, MCP adapters, and their public operation boundaries.\n\n1. Send technical diagnostics through the shared logger. Use the actual Project prefix and sanitized context. The Docker runtime captures the streams under its bounded retention and back-pressure configuration. Use stderr when stdout carries MCP or Tool protocol or result data. For the Project Atom Lifecycle backend, emit a stdout INFO event when each step starts and when it ends as done or failed. Include the step and elapsed time in the end event. Do not log input values or carrier contents.\n2. Apply CA-M-396 to severity. Use WARNING for input and Project artifact issues. Reserve ERROR for real blocking runtime failures. A response error or failed business Workflow does not by itself require ERROR-level logging.\n3. For an actually admitted/started business Workflow, record its observed started, failed, and completed transitions, as applicable. Use its executor and the shared Journal owner. A technical cause may explain a real business failure without copying technical log records or stack traces into the Journal.\n4. A preflight rejection with no admitted or started business Workflow must not create a Workflow, Run, started or failed event, or completion event. Logging or generic error handling must not add hidden Journal effects to direct read-only Tool calls.\n5. Keep business records truthful and independent of Git and technical-log retention. Incomplete Journal records are not an admission gate. Preserve existing historical Journal bytes. Do not rewrite old technical entries as part of this Method.",
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-M-542",
      "version": 2,
      "summary": "Prefer well-known technologies and interfaces",
      "prose_claim": "Prefer technologies and interfaces that AI Agents already know. Use custom ones when their value justifies the extra learning and maintenance.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-R-1041",
      "version": 18,
      "summary": "Coordinate Atom replacement intent\n\n## Scope\n\nREPLACE_ATOM's explicit single or frozen bulk replacement intent, delegated application boundary, and truthful result evidence.\n\n## Claim\n\nREPLACE_ATOM **must** coordinate explicit Atom replacement intent **without** owning generic Carrier creation, relation editing, **or** archival semantics.\n\n- An atomic replacement accepts **`=1`** exact active predecessor Atom ID, **`>=1`** distinct exact sealed prepared-new successor Carrier sets, **and** action context. Each prepared-new successor set has complete sealed content, an assigned identity, and a destination. A preexisting successor mode is not admitted.\n- Reject a missing, duplicate, inactive, or self-referential predecessor; missing, duplicate, partial, or unsealed prepared-new successor content; or a used successor identity or destination. Return a sealed replacement action with the supplied predecessor, complete prepared-new successor set, and predecessor archive intent.\n- A Workflow with several predecessors supplies explicit mappings and invokes one independently admitted replacement Action per predecessor. Stop at the first failed Action. Keep completed replacements and leave the remaining ones untouched. Do not promise all-or-nothing effects across predecessors.\n- Use the canonical Atom lifecycle capability to materialize only the complete sealed prepared-new successor set, make every successor Active, and then archive the predecessor. Pass the explicit IDs **to** the provenance pipeline. Do **not** infer successor content, perform generic Carrier creation, or write replacement relations **in** Atom Carriers.\n- Default **to** a mutation-free dry run. Allow apply **only** through authorized project-local MCP delegation with a sealed Initiative action envelope.\n- A successful delegated effect requires durable COMMIT_TRIGGER intake acknowledgment **before** MCP reports success. Intake acknowledgment is necessary for that handoff, **but** it does not prove that replacement was applied or that its authoritative Journal event **and** Run evidence were durably recorded. REPLACE_ATOM does **not** append the Journal, stage files, **or** create a Git Commit.\n- Distinguish a prepared sealed description, a deferred delegated request, **and** an actually applied replacement. Prepared or deferred results **must** state that the archive effect is **not** applied. Acceptance, sealing, or intake alone **must not** be reported as a completed replacement.\n- At the actual effect boundary, revalidate the exact predecessor and each prepared-new successor's complete sealed content, identity, unused destination, current source and destination conditions, complete sealed mapping, and current delegated authority. Materialize every successor and verify that each is durably Active **before** predecessor archival. Use CA-O-051's whole-Carrier transition. Preserve the predecessor's body, Summary, Type, identity, and frontmatter values except for its actual archive Status, Version, **and** Updated At. Its actual changed archive Revision advances Version by **`=1`** and uses the applicable canonical archive encoding. Retain exact before-Revision bytes and Version as required history.\n- Report actual replacement completion **only** with observed canonical lifecycle effects **and** durable authoritative archive-event evidence naming the explicit predecessor **and** complete **`>=1`** materialized Active successor set under CA-R-807. Preserve each explicit mapping and its actual result. Do not describe partial or uncertain effects as completed replacement.\n- Retain exact actual Workflow and Action Run identities, definition Revisions, input, result, and effect references, start and truthful terminal or pending evidence, **and** actual durable receipts under the reviewed CA-P-1443/CA-P-1451 shared contract. If recording fails, completion evidence remains blocked and pending evidence remains intact. Preserve the missing-recording disposition **without** replaying performed replacement or resetting authority. An unpersisted acknowledgment is **not** Journal completion.\n\n## Details\n\nCA-O-031 owns the replacement Action. CA-O-051 and CA-R-807 govern canonical lifecycle effects and immutable replacement history. CA-E-299 covers the prepared description. CA-E-247 covers admission, delegated-effect, and receipt distinctions. The Tool admits no preexisting-successor mode and does not infer missing successor content. Intake acceptance gives it no lifecycle or Journal authority.\n\nEvery Summary value change requires a new Atom ID and predecessor archival through this replacement Workflow, even when the Claim does not change. Return the explicit target, created, and archived IDs separately. For example, if target `100` is replaced by new Atom `200`, identify target `100`, created `200`, and archived `100`. Replacement does not automatically retarget incoming references. Independent Find and Modify Workflows select and update Atoms that reference it. Resume and retry policy for independent replacements remains deferred. Current source, destination, permission, and preview checks, and each replacement's internal storage-effect safeguards, remain required.",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-E-684",
      "version": 10,
      "summary": "Test Workbench Workspace Views and Query Log",
      "prose_claim": "Use the real native Codex plugin UI and MCP surfaces. A browser page does not count as the plugin UI. Verify that a host-provided native session opens its isolated Workspace with at least one View for the explicit Project. Verify one read-only Workspace or View operation through the shared backend.\n\nVerify that the native UI, standalone browser, and MCP use the same Workspace and View effects. Verify that two Codex chats have separate Workspaces and unsaved SQL. The system must not require a standalone chat, synthetic native session, magic Workflow, code runner, scheduler, or retry behavior.\n\nIn a disposable protocol host and valid disposable Project, verify that `workspace_open` alone exposes `ui://caprmedio/workbench.html`. The compatibility probe must remain separately linked. Unknown resource URIs and unexpected inputs must fail. Verify that the resource is self-contained `text/html;profile=mcp-app`. It must have no external script or stylesheet references, Workbench HTTP request, browser opening, or second server.\n\nVerify native bootstrap behavior. It accepts only the `workspace_open` host tool input's non-empty `session_id`, explicit `project_root`, and initial structured result. Exercise both input and result arrival orders. Require the exact supplied IDs and initial Workspace. Verify that no second `workspace_open` call occurs. If input or result is absent, verify that a binding error appears and that there is no backend call, URL or localStorage identity fallback, synthetic native session, or alternative Workspace selection.\n\nThrough the native MCP transport, exercise every existing Workspace, View, and query-log operation. Each call must retain the exact `project_root`, use one `tools/call`, preserve `structuredContent`, reject `isError`, and reach the shared handler. Check transport binding and error propagation without repeating shared operation acceptance cases. Native mode must not use standalone URL, localStorage, or draft-migration behavior.\n\nIn a real new or resumed Codex chat with the installed local plugin and a valid disposable Project and Workspace, call the real `workspace_open` with the hook-supplied native session ID and trusted Project root. Verify that Codex renders the Workbench in-chat. The shown Workspace ID must equal the tool input session. Verify that a read-only Workspace or View operation traverses the bridge, that ordinary MCP or standalone use shows state from the same backend, and that no browser, second chat, or second MCP connection appears. Exercise fullscreen or move-to-panel only if the host offers it and report the observed placement.\n\nA synthetic or disposable-host test proves protocol and application behavior only. It does not prove native Codex rendering, right-panel support, or complete native Workbench delivery. The read-only probe separately tests standard MCP Apps compatibility. It must not be used as evidence that Workbench was activated.\n\nCall the read-only `workbench_ui_probe` through the existing MCP connection. Verify that its component renders inside Codex, displays the initial host tool result, and reports a successful, separate `workbench_ui_ping` bridge call. Verify that the resource and tools work over real MCP transport, reject unexpected arguments and unknown resource URIs, and do not start Workbench. Verify the inline and fullscreen declaration; current and offered mode display; Expand only when fullscreen is available; accepted, inline-retained, rejected, and unsupported results; actual returned-mode display; and no unavailable request. If the real host does not render native UI, record delivery as incomplete and do not substitute a browser page. Observe move-to-panel only if offered. Otherwise, record right-panel delivery as unproven.\n\nUse a fixture whose directory basename differs from its declared Project name. Verify that HTTP and MCP `workspace_open` and `workspace_get` return the declared `project_name`, and that the native Workbench header displays it. Workspace documents must not gain a persisted Project-name field. If a native initial Workspace result lacks `project_name`, report a binding error before further tool calls. Do not fall back to the directory basename.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-O-190",
      "version": 11,
      "summary": "Discover a matching public `main` PR\n\n## Action\n\nDiscover a matching public `main` PR **means** the native read operation that returns zero or one actual open PR identity for the selected personal remote and `amm/dev` to `main` boundary.\n\n## Details\n\nThe Tool-call input, result, and report references remain evidence of this Action Run. This Action does not create or update a PR. It does not claim an MCP route.",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-E-357",
      "version": 23,
      "summary": "Reject an object without persistent ownership",
      "prose_claim": "#### Claim checked\n\nAdmit a PROGRAMMATIC object **only** if it requires identity across calls **and** owns state, an invariant, a resource, a lifecycle, **or** a replaceable adapter.\n\n#### Test case\n\nEvaluate one changed object that **only** wraps a bounded, one-shot effect **and** owns no responsibility across calls.\n\n#### Acceptance criteria\n\nPass **only** if the object is rejected **and** its effect is assigned **to** a specifically named bounded function.\n\n#### Failure disposition\n\nReject the object **until** persistent ownership is demonstrated **or** a function replaces the wrapper.\n\n#### Sources\n\n- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-R-1441",
      "version": 26,
      "summary": "Define Default Settings",
      "prose_claim": "This Atom defines Default Settings.\n\nDefault Settings **means** the authoritative Artifact that contains reusable baseline values for registered CAPRMEDIO Framework Instance Settings parameters. It is **not** Project initialization inputs **or** a Project's explicit Operator selections.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-D-279",
      "version": 26,
      "summary": "Serialize Markdown Paragraphs as Unwrapped Lines",
      "prose_claim": "This Decision defines the serialization of Markdown Atom Carrier Main Content prose paragraphs.\n\n**every** Markdown Atom Carrier Main Content prose paragraph **must** use one unwrapped source line **and** one blank line between adjacent paragraphs.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-O-178",
      "version": 17,
      "summary": "Install the runtime and project-local ca Skill\n\n## Step\n\nThis Step invokes CA-O-169 once with phase `install` to copy compiled `LAYER_1_FRAMEWORK_METHODOLOGY/`, preserve protected configuration and Project state, install Engine `.install` into the Project runtime package, and install the `ca` payload.\n\n## Details\n\nOnly this Step clears replaceable installed Framework members, copies the product as-is, installs `ca`, and restarts or reuses Project MCP for Docker/MCP smoke. It preserves settings and Project state. It does not alter authoring, push, create a PR, or retry an uncertain effect.\n\nReuse canonical image preparation only after the Workflow's full suite is green. This occurrence also owns CA-O-169's post-smoke selected-Project retention: keep the exact admitted current-Version candidate, remove only proven owned unused noncandidate images, preserve all container references and other Projects' images, and report pending cleanup. The same fingerprint alone does not preserve an older rebuild. Do not insert an additional retirement Step into CA-O-164.",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-D-491",
      "version": 15,
      "summary": "Deliver the VALIDATE_ATOMS command\n\n## Scope\n\nThis Decision applies to the `VALIDATE_ATOMS` command Carrier and its delivered test assets in TOOLS.\n\n## Claim\n\nDeliver the `VALIDATE_ATOMS` executable Carrier as `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms.py`. Put its automated tests in the adjacent `tests/` directory.\n\n- Support `validate_atoms.py --input <request.json>` and `--input -` for standard input.\n- Emit **=1** JSON result on standard output under CA-D-493-TOOLS-ENG_DECISION--serialize-atom-validator-results. Send human execution diagnostics to standard error.\n- the path identifies an Implementation Artifact inside TOOLS, **not** a newly declared Scope Unit. it carries the implementation bound under CA-R-1622-TOOLS-RULE--implement-atom-carrier-validation-in-validate-atoms, **not** another Workflow authority.\n- Store end-to-end command tests at `VALIDATE_ATOMS/tests/test_validate_atoms_e2e.py`, relative **to** the delivered TOOLS directory.\n- store mock Markdown Atoms **and** supporting mock context **in** `VALIDATE_ATOMS/tests/fixtures/`, with `good/`, `bad/`, `mixed/`, **and** `context/` groups. Fixture files are test inputs, not active governing Project Atoms.\n- Store the case and coverage manifest at `VALIDATE_ATOMS/tests/cases.json`. Store independently reviewed expected reports at `VALIDATE_ATOMS/tests/expected/<case_id>.json`. Each manifest case identifies its fixture inputs, request, governing rule identities and Revisions, expected report, and expected exit code.\n\n- `cases.json` is a closed object with `schema_version: 1` and a non-empty `cases` array. Each case has a unique, non-empty `case_id`; a `request` path; a non-empty `fixture_paths` list; a non-empty `authority` list of exact Atom Bindings under CA-D-492-TOOLS-DELIVERY--serialize-atom-validator-requests; a non-empty `check_codes` list; an `expected_report` path; and an integer `expected_exit_code` in (0, 1, 2, 3). All case paths are relative **to** `tests/`, remain inside it, and cannot escape through symlinks. Expected reports follow CA-D-493-TOOLS-DELIVERY--serialize-atom-validator-results.\n- Include positive, negative, exception, and boundary coverage for every supported check and declared failure class. Reusable fixture cases may cover multiple rules. The harness verifies this matrix against the independently resolved obligation inventory, not only the list of implemented checks.\n\n## Details",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    }
  ],
  "handoff": {
    "CA-M-399": {
      "main_contribution": "Keep technical diagnostics and business Workflow lifecycle records separate, while recording only observed business transitions.",
      "rewrite_choice": "I separated the logging rules from the Journal rules into numbered steps so each condition and boundary is easier to apply.",
      "watch": [
        {
          "field": "details",
          "source_anchor": "For the Project Atom Lifecycle backend, emit a stdout INFO event",
          "concern": "Check that this Project-specific stdout exception remains compatible with protocol data on stdout."
        }
      ]
    },
    "CA-M-542": {
      "main_contribution": "Prefer familiar technologies and interfaces unless custom ones justify their extra learning and maintenance cost.",
      "rewrite_choice": "",
      "watch": []
    },
    "CA-R-1041": {
      "main_contribution": "Coordinate explicit, delegated Atom replacement and report completion only when its actual lifecycle and durable evidence support that result.",
      "rewrite_choice": "I split dense clauses into shorter sentences and bullets while retaining each admission, effect, authority, and evidence condition.",
      "watch": [
        {
          "field": "summary",
          "source_anchor": "complete sealed mapping, and current delegated authority",
          "concern": "Check which source or destination conditions must be revalidated at the effect boundary."
        },
        {
          "field": "summary",
          "source_anchor": "under the reviewed CA-P-1443/CA-P-1451 shared contract",
          "concern": "Confirm the shared contract's exact requirements for durable receipts and pending evidence."
        }
      ]
    },
    "CA-E-684": {
      "main_contribution": "Verify real native Workbench behavior and keep synthetic protocol checks distinct from evidence of Codex rendering.",
      "rewrite_choice": "I grouped the long test criteria by behavior and stated each check as a direct instruction to make the evaluation easier to execute.",
      "watch": [
        {
          "field": "prose_claim",
          "source_anchor": "the exact supplied IDs and initial Workspace",
          "concern": "Confirm which IDs and Workspace fields the bootstrap binding must match exactly."
        },
        {
          "field": "prose_claim",
          "source_anchor": "actual returned-mode display",
          "concern": "Check the host's supported mode outcomes and how each is returned over real transport."
        }
      ]
    },
    "CA-O-190": {
      "main_contribution": "Return zero or one actual open PR identity for the selected personal remote and the amm/dev-to-main boundary.",
      "rewrite_choice": "I clarified the negative scope by making the no-create, no-update, and no-MCP-route limits direct statements.",
      "watch": []
    },
    "CA-E-357": {
      "main_contribution": "Reject a one-shot wrapper that owns no cross-call responsibility and assign its effect to a named bounded function.",
      "rewrite_choice": "I changed compressed line breaks into complete short sentences while preserving the evaluation headings and source reference.",
      "watch": []
    },
    "CA-R-1441": {
      "main_contribution": "Define Default Settings as the authoritative reusable baseline Artifact for registered Framework Instance Settings parameters.",
      "rewrite_choice": "I stated the meaning as a direct definition and made the exclusion of Project inputs and Operator selections explicit.",
      "watch": []
    },
    "CA-D-279": {
      "main_contribution": "Require each Markdown Atom Carrier Main Content prose paragraph to use one source line with a blank line between paragraphs.",
      "rewrite_choice": "I split the two serialization requirements into separate short sentences.",
      "watch": []
    },
    "CA-O-178": {
      "main_contribution": "Install the compiled runtime and ca payload once while preserving protected state and safely retaining only the selected Project's current image candidate.",
      "rewrite_choice": "I separated install behavior from post-smoke image retention so the preservation and deletion conditions are easier to follow.",
      "watch": [
        {
          "field": "summary",
          "source_anchor": "the exact admitted current-Version candidate",
          "concern": "Confirm which admission evidence identifies the selected Project's current-Version image candidate."
        },
        {
          "field": "summary",
          "source_anchor": "Remove only proven owned unused noncandidate images",
          "concern": "Check how ownership and unused status are proven before image removal."
        }
      ]
    },
    "CA-D-491": {
      "main_contribution": "Specify the VALIDATE_ATOMS executable's delivery path, command interface, JSON result contract, and complete independently checked test assets.",
      "rewrite_choice": "I made the delivery requirements direct bullets and retained each exact path, governing reference, manifest constraint, and coverage condition.",
      "watch": [
        {
          "field": "summary",
          "source_anchor": "integer `expected_exit_code` **in** (0, 1, 2, 3)",
          "concern": "Confirm this notation means the four listed exit-code values and whether the manifest schema enforces that set."
        },
        {
          "field": "summary",
          "source_anchor": "independently resolved obligation inventory",
          "concern": "Check which independently resolved obligations define full matrix coverage."
        }
      ]
    }
  },
  "validation": [
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
      "issues": [
        {
          "check": "sections",
          "source": "actually admitted/started business Workflow",
          "candidate": "actually admitted and started",
          "reason": "Requires both admission and start where the source uses admitted/started.",
          "resolution": "repaired",
          "certainty": "confirmed"
        },
        {
          "check": "sections",
          "source": "may explain a real business failure without copying technical log records or stack traces into the Journal",
          "candidate": "A technical cause can explain an actual business failure. Do not copy technical log records or stack traces into the Journal.",
          "reason": "Turns a restriction attached to the explanation into a separate unconditional instruction.",
          "resolution": "repaired",
          "certainty": "confirmed"
        }
      ]
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
      "issues": [
        {
          "check": "claim",
          "source": "real native Codex plugin UI",
          "candidate": "native Codex plugin UI",
          "reason": "Omits the explicit requirement to use the real native UI.",
          "resolution": "repaired",
          "certainty": "confirmed"
        },
        {
          "check": "claim",
          "source": "only if the host offers it and report the observed placement",
          "candidate": "only if the host offers it. Report the observed placement.",
          "reason": "The split removes the host-offer condition from reporting placement.",
          "resolution": "repaired",
          "certainty": "confirmed"
        },
        {
          "check": "claim",
          "source": "If the real host does not render native UI, record delivery as incomplete and do not substitute a browser page",
          "candidate": "If the real host does not render native UI, record delivery as incomplete. Do not substitute a browser page.",
          "reason": "The split detaches the no-substitution instruction from the specified condition.",
          "resolution": "repaired",
          "certainty": "confirmed"
        }
      ]
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
      "issues": [
        {
          "check": "claim",
          "source": "every Markdown Atom Carrier Main Content prose paragraph **must** use one unwrapped source line **and** one blank line between adjacent paragraphs",
          "candidate": "prose paragraph **must** use one unwrapped source line. Put one blank line between adjacent paragraphs.",
          "reason": "The split leaves the second instruction without the original Markdown Carrier paragraph scope.",
          "resolution": "repaired",
          "certainty": "confirmed"
        }
      ]
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
      "issues": [
        {
          "check": "claim",
          "source": "invokes CA-O-169 once with phase `install` to copy",
          "candidate": "invokes CA-O-169 once with phase `install`. It copies",
          "reason": "The pronoun makes it unclear whether the Step or invoked CA-O-169 performs the actions.",
          "resolution": "repaired",
          "certainty": "confirmed"
        },
        {
          "check": "sections",
          "source": "This occurrence also owns CA-O-169's post-smoke selected-Project retention: keep",
          "candidate": "This occurrence also owns CA-O-169's post-smoke selected-Project retention. Keep",
          "reason": "Splitting the list detaches the retention actions from the owning occurrence and post-smoke scope.",
          "resolution": "repaired",
          "certainty": "confirmed"
        }
      ]
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
      "issues": [
        {
          "check": "claim",
          "source": "it carries the implementation bound under CA-R-1622",
          "candidate": "The command implements the bound implementation under CA-R-1622",
          "reason": "Changes the path and artifact carrying the bound implementation into a command implementing an implementation.",
          "resolution": "repaired",
          "certainty": "confirmed"
        },
        {
          "check": "claim",
          "source": "fixtures/`, with `good/`, `bad/`, `mixed/`, **and** `context/` groups",
          "candidate": "fixtures/`. Use the `good/`, `bad/`, `mixed/`, and `context/` groups",
          "reason": "The split leaves the groups without an explicit binding to the fixtures directory.",
          "resolution": "repaired",
          "certainty": "confirmed"
        }
      ]
    }
  ]
}
```
