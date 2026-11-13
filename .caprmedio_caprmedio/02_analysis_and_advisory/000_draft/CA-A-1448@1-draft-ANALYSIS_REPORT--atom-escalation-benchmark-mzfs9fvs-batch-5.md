---
identity:
  atom_id: CA-A-1448
  ref_id: CA-A-1448@1-draft
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
  updated_at: '2026-11-12T20:52:14.050277+00:00'
destination:
  file:
    name: CA-A-1448@1-draft-ANALYSIS_REPORT--atom-escalation-benchmark-mzfs9fvs-batch-5.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Atom escalation benchmark mzfs9fvs batch 5

## Details

```json
{
  "batch": 5,
  "atoms": [
    {
      "source_ref": "CA-M-399",
      "source_version": 20,
      "candidate": {
        "ref": "CA-M-399",
        "version": 20,
        "summary": "Record business Workflow lifecycle separately from technical diagnostics",
        "prose_claim": "Send technical diagnostics to structured stdout or stderr streams. Record actual business Workflow lifecycle events through the declared Journal owner. Do not turn a technical warning into a business event.",
        "details": "### Scope\n\nThis Method applies to new or changed PROGRAMMATIC implementations. This includes Tools, Apps, MCP adapters, and their public operation boundaries.\n\n1. Send technical diagnostics through the shared logger. Use the actual Project prefix and sanitized context. The Docker runtime captures the streams under its bounded retention and back-pressure configuration. Use stderr when stdout carries MCP/Tool protocol or result data.\n\n   For the Project Atom Lifecycle backend, emit a stdout INFO event when each step starts and when it ends as done or failed. Include the step and elapsed time in the end event. Do not log input values or carrier contents.\n\n2. Apply CA-M-396 to severity. Use WARNING for input and Project artifact issues. Reserve ERROR for actual blocking runtime failures. A response error or failed business Workflow does not by itself require ERROR-level logging.\n\n3. For a business Workflow that was actually admitted/started, record its observed started, failed, and completed lifecycle transitions, as applicable, through its executor and the shared Journal owner. A technical cause may explain an actual business failure. Do not copy technical log records or stack traces into the Journal.\n\n4. A preflight rejection with no admitted/started business Workflow must not create a Workflow, Run, started or failed event, or completion event. Logging or generic error handling must not add hidden Journal effects to direct read-only Tool calls.\n\n5. Keep business records truthful and independent of Git and technical-log retention. Incomplete Journal records are not an admission gate. Preserve existing historical Journal bytes. Do not rewrite old technical entries as part of this Method.",
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-M-399",
        "confidence": "high",
        "escalate": false,
        "reason": "The logger, lifecycle recording, severity, preflight, and history requirements are preserved; the reordered sentences do not change the instructions."
      },
      "final": {
        "ref": "CA-M-399",
        "version": 20,
        "summary": "Record business Workflow lifecycle separately from technical diagnostics",
        "prose_claim": "Send technical diagnostics to structured stdout or stderr streams. Record actual business Workflow lifecycle events through the declared Journal owner. Do not turn a technical warning into a business event.",
        "details": "### Scope\n\nThis Method applies to new or changed PROGRAMMATIC implementations. This includes Tools, Apps, MCP adapters, and their public operation boundaries.\n\n1. Send technical diagnostics through the shared logger. Use the actual Project prefix and sanitized context. The Docker runtime captures the streams under its bounded retention and back-pressure configuration. Use stderr when stdout carries MCP/Tool protocol or result data.\n\n   For the Project Atom Lifecycle backend, emit a stdout INFO event when each step starts and when it ends as done or failed. Include the step and elapsed time in the end event. Do not log input values or carrier contents.\n\n2. Apply CA-M-396 to severity. Use WARNING for input and Project artifact issues. Reserve ERROR for actual blocking runtime failures. A response error or failed business Workflow does not by itself require ERROR-level logging.\n\n3. For a business Workflow that was actually admitted/started, record its observed started, failed, and completed lifecycle transitions, as applicable, through its executor and the shared Journal owner. A technical cause may explain an actual business failure. Do not copy technical log records or stack traces into the Journal.\n\n4. A preflight rejection with no admitted/started business Workflow must not create a Workflow, Run, started or failed event, or completion event. Logging or generic error handling must not add hidden Journal effects to direct read-only Tool calls.\n\n5. Keep business records truthful and independent of Git and technical-log retention. Incomplete Journal records are not an admission gate. Preserve existing historical Journal bytes. Do not rewrite old technical entries as part of this Method.",
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-M-542",
      "source_version": 2,
      "candidate": {
        "ref": "CA-M-542",
        "version": 2,
        "summary": "Prefer well-known technologies and interfaces",
        "prose_claim": "Prefer technologies and interfaces that AI Agents already know. Use custom technologies or interfaces when their value justifies the added learning and maintenance.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-M-542",
        "confidence": "high",
        "escalate": false,
        "reason": "“custom ones” is clarified as “custom technologies or interfaces”; the justification and costs remain the same."
      },
      "final": {
        "ref": "CA-M-542",
        "version": 2,
        "summary": "Prefer well-known technologies and interfaces",
        "prose_claim": "Prefer technologies and interfaces that AI Agents already know. Use custom technologies or interfaces when their value justifies the added learning and maintenance.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-R-1041",
      "source_version": 18,
      "candidate": {
        "ref": "CA-R-1041",
        "version": 18,
        "summary": "Coordinate Atom replacement intent\n\n## Scope\n\nThis Rule covers REPLACE_ATOM's explicit singular or frozen bulk replacement intent, delegated application boundary, and truthful result evidence.\n\n## Claim\n\nREPLACE_ATOM **must** coordinate explicit Atom replacement intent. It must not own generic Carrier creation, relation editing, or archival semantics.\n\n- An atomic replacement accepts **`=1`** exact active predecessor Atom ID, **`>=1`** distinct exact sealed prepared-new successor Carrier sets, and action context. Each prepared-new successor set contains complete sealed content, assigned identity, and destination. The operation admits no preexisting-successor mode.\n- Reject a missing, duplicate, inactive, or self-referential predecessor. Reject missing, duplicate, partial, or unsealed prepared-new successor content. Reject a used successor identity or destination. Return a sealed replacement action with the supplied predecessor, the complete prepared-new successor set, and the predecessor archive intent.\n- A multi-predecessor Workflow supplies explicit mappings. It invokes one independently admitted replacement Action for each predecessor. Stop at the first failed Action. Retain completed replacements and leave the remaining replacements untouched. Do not promise an all-or-nothing effect across predecessors.\n- Use the canonical Atom lifecycle capability to materialize only the complete sealed prepared-new successor set, establish every successor as Active, and then archive the predecessor. Pass the explicit IDs **to** the provenance pipeline. Do **not** infer successor content, perform generic Carrier creation, or write replacement relations **in** Atom Carriers.\n- Default **to** a mutation-free dry run. Permit apply **only** through authorized project-local MCP delegation with a sealed Initiative action envelope.\n- A successful delegated effect requires durable COMMIT_TRIGGER intake acknowledgment **before** MCP reports success. Intake acknowledgment is necessary for the handoff. It does **not** prove that replacement was applied or that its authoritative Journal event and Run evidence were durably recorded. REPLACE_ATOM does **not** append the Journal, stage files, or create a Git Commit.\n- Distinguish a prepared sealed description, a deferred delegated request, and an actually applied replacement. Prepared or deferred results **must** state that the archive effect is **not** applied. Acceptance, sealing, or intake alone **must not** be reported as completed replacement.\n- At the actual effect boundary, revalidate the exact predecessor; the complete sealed content and identity of every prepared-new successor; each unused destination; current source and destination conditions; the complete sealed mapping; and current delegated authority. Materialize every successor and verify that each is durably Active **before** predecessor archival. Use CA-O-051's whole-Carrier transition. Preserve the predecessor's body, Summary, Type, identity, and frontmatter values except actual archive Status, Version, and Updated At. Its actual changed archive Revision advances Version by **`=1`** and uses the applicable canonical archive encoding. Retain the exact before-Revision bytes and Version as required history.\n- Report actual replacement completion **only** with observed canonical lifecycle effects and durable authoritative archive-event evidence naming the explicit predecessor and the complete **`>=1`** materialized Active successor set under CA-R-807. Preserve each explicit mapping and its actual result. Do not describe partial or uncertain effects as completed replacement.\n- Retain exact actual Workflow/Action Run identities, definition Revisions, input/result/effect references, start and truthful terminal/pending evidence, and actual durable receipts under the reviewed CA-P-1443/CA-P-1451 shared contract. If recording fails, completion evidence remains blocked and pending evidence remains intact. Preserve the missing-recording disposition. Do not replay a performed replacement or reset authority. An unpersisted acknowledgment is **not** Journal completion.\n\n## Details\n\nCA-O-031 owns the replacement Action. CA-O-051 and CA-R-807 govern canonical lifecycle effects and immutable replacement history. CA-E-299 covers the prepared description. CA-E-247 covers admission, delegated-effect, and receipt distinctions. The Tool admits no preexisting-successor mode and does not infer missing successor content. Intake acceptance grants it no lifecycle or Journal authority.\n\nEvery Summary value change requires a new Atom ID and predecessor archival through this replacement Workflow, even if the Claim is unchanged. Return the explicit target, created, and archived IDs separately. For example, when new Atom `200` replaces target `100`, identify target `100`, created `200`, and archived `100`.\n\nReplacement does not automatically retarget incoming references. Independent Find and Modify Workflows select and update the referencing Atoms. Resume and retry policy for independent replacements remains deferred. Current source, destination, permission, preview, and each replacement's internal storage-effect safeguards remain required.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-R-1041",
        "confidence": "high",
        "escalate": false,
        "reason": "The rewrite preserves the replacement constraints, sequence, authorities, evidence requirements, and deferred behaviors. Splitting sentences and expanding contractions does not change scope."
      },
      "final": {
        "ref": "CA-R-1041",
        "version": 18,
        "summary": "Coordinate Atom replacement intent\n\n## Scope\n\nThis Rule covers REPLACE_ATOM's explicit singular or frozen bulk replacement intent, delegated application boundary, and truthful result evidence.\n\n## Claim\n\nREPLACE_ATOM **must** coordinate explicit Atom replacement intent. It must not own generic Carrier creation, relation editing, or archival semantics.\n\n- An atomic replacement accepts **`=1`** exact active predecessor Atom ID, **`>=1`** distinct exact sealed prepared-new successor Carrier sets, and action context. Each prepared-new successor set contains complete sealed content, assigned identity, and destination. The operation admits no preexisting-successor mode.\n- Reject a missing, duplicate, inactive, or self-referential predecessor. Reject missing, duplicate, partial, or unsealed prepared-new successor content. Reject a used successor identity or destination. Return a sealed replacement action with the supplied predecessor, the complete prepared-new successor set, and the predecessor archive intent.\n- A multi-predecessor Workflow supplies explicit mappings. It invokes one independently admitted replacement Action for each predecessor. Stop at the first failed Action. Retain completed replacements and leave the remaining replacements untouched. Do not promise an all-or-nothing effect across predecessors.\n- Use the canonical Atom lifecycle capability to materialize only the complete sealed prepared-new successor set, establish every successor as Active, and then archive the predecessor. Pass the explicit IDs **to** the provenance pipeline. Do **not** infer successor content, perform generic Carrier creation, or write replacement relations **in** Atom Carriers.\n- Default **to** a mutation-free dry run. Permit apply **only** through authorized project-local MCP delegation with a sealed Initiative action envelope.\n- A successful delegated effect requires durable COMMIT_TRIGGER intake acknowledgment **before** MCP reports success. Intake acknowledgment is necessary for the handoff. It does **not** prove that replacement was applied or that its authoritative Journal event and Run evidence were durably recorded. REPLACE_ATOM does **not** append the Journal, stage files, or create a Git Commit.\n- Distinguish a prepared sealed description, a deferred delegated request, and an actually applied replacement. Prepared or deferred results **must** state that the archive effect is **not** applied. Acceptance, sealing, or intake alone **must not** be reported as completed replacement.\n- At the actual effect boundary, revalidate the exact predecessor; the complete sealed content and identity of every prepared-new successor; each unused destination; current source and destination conditions; the complete sealed mapping; and current delegated authority. Materialize every successor and verify that each is durably Active **before** predecessor archival. Use CA-O-051's whole-Carrier transition. Preserve the predecessor's body, Summary, Type, identity, and frontmatter values except actual archive Status, Version, and Updated At. Its actual changed archive Revision advances Version by **`=1`** and uses the applicable canonical archive encoding. Retain the exact before-Revision bytes and Version as required history.\n- Report actual replacement completion **only** with observed canonical lifecycle effects and durable authoritative archive-event evidence naming the explicit predecessor and the complete **`>=1`** materialized Active successor set under CA-R-807. Preserve each explicit mapping and its actual result. Do not describe partial or uncertain effects as completed replacement.\n- Retain exact actual Workflow/Action Run identities, definition Revisions, input/result/effect references, start and truthful terminal/pending evidence, and actual durable receipts under the reviewed CA-P-1443/CA-P-1451 shared contract. If recording fails, completion evidence remains blocked and pending evidence remains intact. Preserve the missing-recording disposition. Do not replay a performed replacement or reset authority. An unpersisted acknowledgment is **not** Journal completion.\n\n## Details\n\nCA-O-031 owns the replacement Action. CA-O-051 and CA-R-807 govern canonical lifecycle effects and immutable replacement history. CA-E-299 covers the prepared description. CA-E-247 covers admission, delegated-effect, and receipt distinctions. The Tool admits no preexisting-successor mode and does not infer missing successor content. Intake acceptance grants it no lifecycle or Journal authority.\n\nEvery Summary value change requires a new Atom ID and predecessor archival through this replacement Workflow, even if the Claim is unchanged. Return the explicit target, created, and archived IDs separately. For example, when new Atom `200` replaces target `100`, identify target `100`, created `200`, and archived `100`.\n\nReplacement does not automatically retarget incoming references. Independent Find and Modify Workflows select and update the referencing Atoms. Resume and retry policy for independent replacements remains deferred. Current source, destination, permission, preview, and each replacement's internal storage-effect safeguards remain required.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-E-684",
      "source_version": 10,
      "candidate": {
        "ref": "CA-E-684",
        "version": 10,
        "summary": "Exercise Workbench Workspace Views and Query Log",
        "prose_claim": "Use the real native Codex plugin UI and MCP surfaces. A browser page is not the plugin UI. Verify that the host-provided native session opens its isolated Workspace with at least one View for the explicit Project. Verify a read-only Workspace/View operation through the shared backend.\n\nVerify that the native UI, standalone browser, and MCP use the same Workspace/View effects. Verify that two Codex chats keep separate Workspaces and unsaved SQL. Verify that no standalone chat, synthetic native session, magic Workflow, code runner, scheduler, or retry behavior is required.\n\nIn a disposable protocol host and disposable valid Project, verify that `workspace_open` alone exposes `ui://caprmedio/workbench.html`. Keep the compatibility probe separately linked. Verify that unknown resource URIs and unexpected inputs fail. The resource must be self-contained `text/html;profile=mcp-app`. It must have no external script or stylesheet references, Workbench HTTP request, browser opening, or second server.\n\nVerify native bootstrap with only the `workspace_open` host tool input's non-empty `session_id`, explicit `project_root`, and initial structured result. Exercise either input/result arrival order. Require the exact supplied IDs and initial Workspace. Verify that no second `workspace_open` call occurs. If input or result is absent, verify that a binding error appears and that no backend call, URL/localStorage identity fallback, synthetic native session, or alternative Workspace selection occurs.\n\nThrough native MCP transport, exercise every existing Workspace/View and query-log operation. Each call must retain the exact `project_root`, use one `tools/call`, preserve `structuredContent`, reject `isError`, and reach the shared handler. Check transport binding and error propagation without repeating shared operation acceptance cases. Native mode must not apply standalone URL, localStorage, or draft-migration behavior.\n\nIn a real new or resumed Codex chat with the installed local plugin and a disposable valid Project/Workspace, invoke the real `workspace_open` with the hook-supplied native session ID and trusted Project root. Verify that Codex renders Workbench in-chat. The shown Workspace ID must equal the tool input session. Verify that a read-only Workspace/View operation traverses the bridge, that state is visible through ordinary MCP or standalone use of the same backend, and that no browser, second chat, or second MCP connection appears. Exercise fullscreen or move-to-panel only if the host offers it, and report the observed placement.\n\nA synthetic or disposable-host test proves protocol and application behavior only. It is insufficient to claim native Codex rendering, right-panel support, or complete native Workbench delivery. The read-only probe separately verifies standard MCP Apps compatibility. Do not use it as evidence that Workbench was activated.\n\nCall the read-only `workbench_ui_probe` through the existing MCP connection. Verify that its component renders inside Codex, displays the initial host tool result, and reports a successful separate `workbench_ui_ping` bridge call. Verify that resource and tools work over real MCP transport; reject unexpected arguments and unknown resource URIs; and do not start Workbench. Verify the inline/fullscreen declaration, current and offered mode display, Expand only when fullscreen is available, accepted/inline-retained/rejected/unsupported results, actual returned-mode display, and no unavailable request. If the real host does not render native UI, record delivery as incomplete. Do not substitute a browser page. Observe move-to-panel only if offered. Otherwise, record right-panel delivery as unproven.\n\nUse a fixture whose directory basename differs from its declared Project name. Verify that HTTP and MCP `workspace_open`/`workspace_get` return the declared `project_name` and that the native Workbench header displays it. Workspace documents must not gain a persisted Project-name field. If a native initial Workspace result lacks `project_name`, report a binding error before further tool calls. Do not fall back to the directory basename.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-E-684",
        "confidence": "high",
        "escalate": false,
        "reason": "The verification steps, host conditions, failure handling, and limits on what each test proves are preserved. Rephrasing does not change actors or conditions."
      },
      "final": {
        "ref": "CA-E-684",
        "version": 10,
        "summary": "Exercise Workbench Workspace Views and Query Log",
        "prose_claim": "Use the real native Codex plugin UI and MCP surfaces. A browser page is not the plugin UI. Verify that the host-provided native session opens its isolated Workspace with at least one View for the explicit Project. Verify a read-only Workspace/View operation through the shared backend.\n\nVerify that the native UI, standalone browser, and MCP use the same Workspace/View effects. Verify that two Codex chats keep separate Workspaces and unsaved SQL. Verify that no standalone chat, synthetic native session, magic Workflow, code runner, scheduler, or retry behavior is required.\n\nIn a disposable protocol host and disposable valid Project, verify that `workspace_open` alone exposes `ui://caprmedio/workbench.html`. Keep the compatibility probe separately linked. Verify that unknown resource URIs and unexpected inputs fail. The resource must be self-contained `text/html;profile=mcp-app`. It must have no external script or stylesheet references, Workbench HTTP request, browser opening, or second server.\n\nVerify native bootstrap with only the `workspace_open` host tool input's non-empty `session_id`, explicit `project_root`, and initial structured result. Exercise either input/result arrival order. Require the exact supplied IDs and initial Workspace. Verify that no second `workspace_open` call occurs. If input or result is absent, verify that a binding error appears and that no backend call, URL/localStorage identity fallback, synthetic native session, or alternative Workspace selection occurs.\n\nThrough native MCP transport, exercise every existing Workspace/View and query-log operation. Each call must retain the exact `project_root`, use one `tools/call`, preserve `structuredContent`, reject `isError`, and reach the shared handler. Check transport binding and error propagation without repeating shared operation acceptance cases. Native mode must not apply standalone URL, localStorage, or draft-migration behavior.\n\nIn a real new or resumed Codex chat with the installed local plugin and a disposable valid Project/Workspace, invoke the real `workspace_open` with the hook-supplied native session ID and trusted Project root. Verify that Codex renders Workbench in-chat. The shown Workspace ID must equal the tool input session. Verify that a read-only Workspace/View operation traverses the bridge, that state is visible through ordinary MCP or standalone use of the same backend, and that no browser, second chat, or second MCP connection appears. Exercise fullscreen or move-to-panel only if the host offers it, and report the observed placement.\n\nA synthetic or disposable-host test proves protocol and application behavior only. It is insufficient to claim native Codex rendering, right-panel support, or complete native Workbench delivery. The read-only probe separately verifies standard MCP Apps compatibility. Do not use it as evidence that Workbench was activated.\n\nCall the read-only `workbench_ui_probe` through the existing MCP connection. Verify that its component renders inside Codex, displays the initial host tool result, and reports a successful separate `workbench_ui_ping` bridge call. Verify that resource and tools work over real MCP transport; reject unexpected arguments and unknown resource URIs; and do not start Workbench. Verify the inline/fullscreen declaration, current and offered mode display, Expand only when fullscreen is available, accepted/inline-retained/rejected/unsupported results, actual returned-mode display, and no unavailable request. If the real host does not render native UI, record delivery as incomplete. Do not substitute a browser page. Observe move-to-panel only if offered. Otherwise, record right-panel delivery as unproven.\n\nUse a fixture whose directory basename differs from its declared Project name. Verify that HTTP and MCP `workspace_open`/`workspace_get` return the declared `project_name` and that the native Workbench header displays it. Workspace documents must not gain a persisted Project-name field. If a native initial Workspace result lacks `project_name`, report a binding error before further tool calls. Do not fall back to the directory basename.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-O-190",
      "source_version": 11,
      "candidate": {
        "ref": "CA-O-190",
        "version": 11,
        "summary": "Discover a matching public `main` PR\n\n## Action\n\nDiscover a matching public `main` PR **means** a native read operation that returns zero or one actual open PR identity for the selected personal remote and the `amm/dev` to `main` boundary.\n\n## Details\n\nThe Tool-call input, result, and report references remain evidence of this Action Run. This Action neither creates nor updates a PR, and it does not claim an MCP route.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-O-190",
        "confidence": "medium",
        "escalate": true,
        "reason": "The Action means “the native read operation” in the source but “a native read operation” in the draft. The indefinite article may broaden which operation qualifies and weakens the identification of the specific operation."
      },
      "final": {
        "ref": "CA-O-190",
        "version": 11,
        "summary": "Discover a matching public `main` PR\n\n## Action\n\nDiscover a matching public `main` PR **means** the native read operation that returns zero or one actual open PR identity for the selected personal remote and the `amm/dev` to `main` boundary.\n\n## Details\n\nThe Tool-call input, result, and report references remain evidence of this Action Run. This Action neither creates nor updates a PR, and it does not claim an MCP route.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": [
        {
          "source": "the native read operation",
          "candidate": "a native read operation",
          "reason": "The indefinite article broadens the identification of the operation.",
          "status": "repaired"
        }
      ]
    },
    {
      "source_ref": "CA-E-357",
      "source_version": 23,
      "candidate": {
        "ref": "CA-E-357",
        "version": 23,
        "summary": "Reject an object without persistent ownership\n\n#### Claim checked\n\nAdmit one PROGRAMMATIC object **only** **when** it requires identity across calls **and** owns state, an invariant, a resource, a lifecycle, **or** a replaceable adapter.\n\n#### Test case\n\nEvaluate one changed object that **only** wraps a bounded one-shot effect and owns no responsibility across calls.\n\n#### Acceptance criteria\n\nPass **only** **when** the object is rejected and the effect is allocated **to** a specifically named bounded function.\n\n#### Failure disposition\n\nReject the object **until** persistent ownership is demonstrated **or** the wrapper is replaced by a function.\n\n#### Sources\n\n- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)",
        "prose_claim": "#### Claim checked\n\none PROGRAMMATIC object is admitted **only** **when** it requires identity across calls\n**and** owns state, an invariant, a resource, a lifecycle, **or** a replaceable\nadapter.\n\n#### Test case\n\nevaluate one changed object that **only** wraps a bounded one-shot effect **and** owns\nno responsibility across calls.\n\n#### Acceptance criteria\n\npass **only** **when** the object is rejected **and** the effect is allocated **to** a\nspecifically named bounded function.\n\n#### Failure disposition\n\nreject the object **until** persistent ownership is demonstrated **or** the wrapper is\nreplaced by a function.\n\n#### Sources\n\n- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-E-357",
        "confidence": "medium",
        "escalate": true,
        "reason": "The source Summary is only “Reject an object without persistent ownership”; the draft adds a Claim checked, Test case, Acceptance criteria, Failure disposition, and Sources to that Summary. This adds substantive evaluation requirements and changes the Summary’s function, so meaning preservation is uncertain."
      },
      "final": {
        "ref": "CA-E-357",
        "version": 23,
        "summary": "Reject an object without persistent ownership",
        "prose_claim": "#### Claim checked\n\none PROGRAMMATIC object is admitted **only** **when** it requires identity across calls\n**and** owns state, an invariant, a resource, a lifecycle, **or** a replaceable\nadapter.\n\n#### Test case\n\nevaluate one changed object that **only** wraps a bounded one-shot effect **and** owns\nno responsibility across calls.\n\n#### Acceptance criteria\n\npass **only** **when** the object is rejected **and** the effect is allocated **to** a\nspecifically named bounded function.\n\n#### Failure disposition\n\nreject the object **until** persistent ownership is demonstrated **or** the wrapper is\nreplaced by a function.\n\n#### Sources\n\n- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": [
        {
          "source": "Reject an object without persistent ownership",
          "candidate": "#### Claim checked",
          "reason": "The summary duplicates the evaluation sections, changing their field and section boundaries; they already appear in prose_claim.",
          "status": "repaired"
        }
      ]
    },
    {
      "source_ref": "CA-R-1441",
      "source_version": 26,
      "candidate": {
        "ref": "CA-R-1441",
        "version": 26,
        "summary": "Define Default Settings\n\nDefault Settings **means** the authoritative Artifact that contains reusable baseline values for registered CAPRMEDIO Framework Instance Settings parameters. It does **not** mean Project initialization inputs or a Project's explicit Operator selections.",
        "prose_claim": "the definition of Default Settings.\n\n\nDefault Settings **means** the authoritative Artifact containing reusable baseline values for registered CAPRMEDIO Framework Instance Settings parameters, **not** Project initialization inputs **or** a Project's explicit Operator selections.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-R-1441",
        "confidence": "high",
        "escalate": false,
        "reason": "The added Summary sentence repeats the existing definition in the prose claim: reusable baseline values are distinguished from Project initialization inputs and Operator selections. No scope or condition changes."
      },
      "final": {
        "ref": "CA-R-1441",
        "version": 26,
        "summary": "Define Default Settings\n\nDefault Settings **means** the authoritative Artifact that contains reusable baseline values for registered CAPRMEDIO Framework Instance Settings parameters. It does **not** mean Project initialization inputs or a Project's explicit Operator selections.",
        "prose_claim": "the definition of Default Settings.\n\n\nDefault Settings **means** the authoritative Artifact containing reusable baseline values for registered CAPRMEDIO Framework Instance Settings parameters, **not** Project initialization inputs **or** a Project's explicit Operator selections.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-D-279",
      "source_version": 26,
      "candidate": {
        "ref": "CA-D-279",
        "version": 26,
        "summary": "Serialize Markdown Paragraphs as Unwrapped Lines\n\nMarkdown Atom Carrier Main Content prose paragraphs **must** each use one unwrapped source line. Use one blank line between adjacent paragraphs.",
        "prose_claim": "Markdown Atom Carrier Main Content prose paragraphs.\n\n\n**every** Markdown Atom Carrier Main Content prose paragraph **must** use one unwrapped source line **and** one blank line between adjacent paragraphs.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-D-279",
        "confidence": "high",
        "escalate": false,
        "reason": "The added Summary sentence restates the existing prose claim’s one-unwrapped-line and blank-line requirements without changing their scope or modality."
      },
      "final": {
        "ref": "CA-D-279",
        "version": 26,
        "summary": "Serialize Markdown Paragraphs as Unwrapped Lines\n\nMarkdown Atom Carrier Main Content prose paragraphs **must** each use one unwrapped source line. Use one blank line between adjacent paragraphs.",
        "prose_claim": "Markdown Atom Carrier Main Content prose paragraphs.\n\n\n**every** Markdown Atom Carrier Main Content prose paragraph **must** use one unwrapped source line **and** one blank line between adjacent paragraphs.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-O-178",
      "source_version": 17,
      "candidate": {
        "ref": "CA-O-178",
        "version": 17,
        "summary": "Install the runtime and project-local ca Skill\n\n## Step\n\nThis Step invokes CA-O-169 once with phase `install`. It copies compiled `LAYER_1_FRAMEWORK_METHODOLOGY/`, preserves protected configuration and Project state, installs Engine `.install` into the Project runtime package, and installs the `ca` payload.\n\n## Details\n\nOnly this Step clears replaceable installed Framework members, copies the product as-is, installs `ca`, and restarts or reuses Project MCP for Docker/MCP smoke. It preserves settings and Project state. It does not alter authoring, push, create a PR, or retry an uncertain effect.\n\nReuse canonical image preparation only after the Workflow's full suite is green. This occurrence also owns CA-O-169's post-smoke selected-Project retention. Keep the exact admitted current-Version candidate. Remove only proven owned unused noncandidate images. Preserve all container references and images belonging to other Projects. Report pending cleanup. A matching fingerprint alone does not preserve an older rebuild. No additional retirement Step is inserted into CA-O-164.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-O-178",
        "confidence": "high",
        "escalate": false,
        "reason": "The install sequence, preservation constraints, cleanup ownership, candidate selection, and exclusions are retained. Sentence splitting does not change the requirements."
      },
      "final": {
        "ref": "CA-O-178",
        "version": 17,
        "summary": "Install the runtime and project-local ca Skill\n\n## Step\n\nThis Step invokes CA-O-169 once with phase `install`. It copies compiled `LAYER_1_FRAMEWORK_METHODOLOGY/`, preserves protected configuration and Project state, installs Engine `.install` into the Project runtime package, and installs the `ca` payload.\n\n## Details\n\nOnly this Step clears replaceable installed Framework members, copies the product as-is, installs `ca`, and restarts or reuses Project MCP for Docker/MCP smoke. It preserves settings and Project state. It does not alter authoring, push, create a PR, or retry an uncertain effect.\n\nReuse canonical image preparation only after the Workflow's full suite is green. This occurrence also owns CA-O-169's post-smoke selected-Project retention. Keep the exact admitted current-Version candidate. Remove only proven owned unused noncandidate images. Preserve all container references and images belonging to other Projects. Report pending cleanup. A matching fingerprint alone does not preserve an older rebuild. No additional retirement Step is inserted into CA-O-164.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-D-491",
      "source_version": 15,
      "candidate": {
        "ref": "CA-D-491",
        "version": 15,
        "summary": "Deliver the VALIDATE_ATOMS command\n\n## Scope\n\nThis Decision covers the `VALIDATE_ATOMS` command Carrier and its delivered test assets in TOOLS.\n\n## Claim\n\nThe `VALIDATE_ATOMS` executable Carrier **must** be delivered at `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms.py`. Its automated tests **must** be in the adjacent `tests/` directory.\n\n- Support `validate_atoms.py --input <request.json>` and `--input -` for standard input.\n- Emit **=1** JSON result on standard output under CA-D-493-TOOLS-ENG_DECISION--serialize-atom-validator-results. Send human execution diagnostics to standard error.\n- The path identifies an Implementation Artifact inside TOOLS. It does **not** declare a new Scope Unit. The Carrier implements the implementation bound under CA-R-1622-TOOLS-RULE--implement-atom-carrier-validation-in-validate-atoms. It does **not** add Workflow authority.\n- Store end-to-end command tests at `VALIDATE_ATOMS/tests/test_validate_atoms_e2e.py`, relative **to** the delivered TOOLS directory.\n- Store mock Markdown Atoms and supporting mock context in `VALIDATE_ATOMS/tests/fixtures/`. Include `good/`, `bad/`, `mixed/`, and `context/` groups. These fixtures are test inputs, not active governing Project Atoms.\n- Store the case/coverage manifest at `VALIDATE_ATOMS/tests/cases.json`. Store independently reviewed expected reports at `VALIDATE_ATOMS/tests/expected/<case_id>.json`. Each manifest case must identify its fixture inputs, request, governing rule identities/Revisions, expected report, and expected exit code.\n\n- `cases.json` is a closed object with `schema_version: 1` and `cases`, a nonempty array. Each case has a unique nonempty `case_id`, `request` path, nonempty `fixture_paths` list, nonempty `authority` list of exact Atom Bindings under CA-D-492-TOOLS-DELIVERY--serialize-atom-validator-requests, nonempty `check_codes` list, `expected_report` path, and integer `expected_exit_code` in (0, 1, 2, 3). All case paths are relative **to** `tests/`, remain inside it, and cannot escape through symlinks. Expected reports follow CA-D-493-TOOLS-DELIVERY--serialize-atom-validator-results.\n- Include positive, negative, exception, and boundary coverage for every supported check and declared failure class. Reusable fixture cases may cover multiple rules. The harness verifies the matrix against the independently resolved obligation inventory, not only against the implemented-check list.\n\n## Details",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-D-491",
        "confidence": "high",
        "escalate": false,
        "reason": "The paths, required artifacts, manifest fields, coverage obligations, and modality are preserved; the draft mainly clarifies grammar and sentence boundaries."
      },
      "final": {
        "ref": "CA-D-491",
        "version": 15,
        "summary": "Deliver the VALIDATE_ATOMS command\n\n## Scope\n\nThis Decision covers the `VALIDATE_ATOMS` command Carrier and its delivered test assets in TOOLS.\n\n## Claim\n\nThe `VALIDATE_ATOMS` executable Carrier **must** be delivered at `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms.py`. Its automated tests **must** be in the adjacent `tests/` directory.\n\n- Support `validate_atoms.py --input <request.json>` and `--input -` for standard input.\n- Emit **=1** JSON result on standard output under CA-D-493-TOOLS-ENG_DECISION--serialize-atom-validator-results. Send human execution diagnostics to standard error.\n- The path identifies an Implementation Artifact inside TOOLS. It does **not** declare a new Scope Unit. The Carrier implements the implementation bound under CA-R-1622-TOOLS-RULE--implement-atom-carrier-validation-in-validate-atoms. It does **not** add Workflow authority.\n- Store end-to-end command tests at `VALIDATE_ATOMS/tests/test_validate_atoms_e2e.py`, relative **to** the delivered TOOLS directory.\n- Store mock Markdown Atoms and supporting mock context in `VALIDATE_ATOMS/tests/fixtures/`. Include `good/`, `bad/`, `mixed/`, and `context/` groups. These fixtures are test inputs, not active governing Project Atoms.\n- Store the case/coverage manifest at `VALIDATE_ATOMS/tests/cases.json`. Store independently reviewed expected reports at `VALIDATE_ATOMS/tests/expected/<case_id>.json`. Each manifest case must identify its fixture inputs, request, governing rule identities/Revisions, expected report, and expected exit code.\n\n- `cases.json` is a closed object with `schema_version: 1` and `cases`, a nonempty array. Each case has a unique nonempty `case_id`, `request` path, nonempty `fixture_paths` list, nonempty `authority` list of exact Atom Bindings under CA-D-492-TOOLS-DELIVERY--serialize-atom-validator-requests, nonempty `check_codes` list, `expected_report` path, and integer `expected_exit_code` in (0, 1, 2, 3). All case paths are relative **to** `tests/`, remain inside it, and cannot escape through symlinks. Expected reports follow CA-D-493-TOOLS-DELIVERY--serialize-atom-validator-results.\n- Include positive, negative, exception, and boundary coverage for every supported check and declared failure class. Reusable fixture cases may cover multiple rules. The harness verifies the matrix against the independently resolved obligation inventory, not only against the implemented-check list.\n\n## Details",
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
