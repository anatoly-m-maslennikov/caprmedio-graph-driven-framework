---
identity:
  atom_id: CA-A-1383
  ref_id: CA-A-1383@1-draft
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
  updated_at: '2026-11-12T15:36:02.321416+00:00'
destination:
  file:
    name: CA-A-1383@1-draft-ANALYSIS_REPORT--compare-atom-prose-rewrite-batch-c34-741425539647.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Compare Atom prose rewrite batch c34 741425539647

## Details

```json
[
  {
    "ref": "CA-R-2446",
    "version": 4,
    "summary": "Expose bounded, read-only MCP health and call history",
    "prose_claim": "MCP **must** expose a browser view at `/caprmedio/health` on the same listener. The view shows:\n\n- bounded health observations;\n- recent Tool calls;\n- recent Workflow observations with status; **and**\n- safe error details.\n\nPreserve the machine JSON `ready` boolean **and** readiness HTTP status semantics. The diagnostic view is non-authoritative. It **must not** infer successful Tool **or** Workflow execution from gateway liveness, scheduler completion, **or** missing observations.",
    "details": "- Render the browser view for explicit `Accept: text/html`. Default, `application/json`, **and** `*/*` requests retain the machine representation. Preserve the loopback Host/Origin boundary. Add no HTTP credential behavior.\n- Observe actual Gateway calls **and** results **only**. Retain at most 32 recent Tool-call observations **and** 32 recent Workflow observations in process-local memory. Label the since-start coverage and reset it on restart. This is **not** persistent, cross-process, **or** complete execution history.\n- Tool observations identify the admitted Tool name, observation time, returned **or** observed outcome, **and** a fixed safe error category. Do **not** treat an ordinary returned response as proof of completed domain effects. Preserve rejected, failed, partial, canceled, **and** uncertain outcomes **without** replay.\n- Workflow observations use **only** known Run identities **and** actual call results. Keep `scheduler_status` separate from actual Workflow outcome **or** disposition. Queued **or** pending is **not** successful completion. An unobserved actual outcome is unknown even **if** a scheduler reports `SUCCESS`.\n- Show gateway generation/process availability **and** registry availability separately from provider-call observations **and** Workflow/worker observations. Last observations are historical facts, **not** live probes. Missing, stale, **or** untested state remains unknown; do **not** promote it to healthy.\n- Retain **and** display none of: raw arguments, raw results, credentials, absolute paths, **or** provider exception text. Use fixed safe error categories with explanatory labels, including timeout, connection, returned-error, **and** uncertain **where** actually known. Escape **every** dynamic HTML field. Bounded history **must not** grow with arbitrary request sizes.\n- A health GET reads the existing snapshot **only**. It does **not**:\n  - invoke a Tool **or** Workflow;\n  - initialize DBOS/Docker state;\n  - scan a Journal;\n  - start, reload, **or** recover anything;\n  - perform a mutation; **or**\n  - replay an uncertain call **or** held Run.\n- Keep canonical sources, Journals, **and** execution outcome evidence distinct from this convenience view.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-198",
    "version": 14,
    "summary": "Finalize the actual public history link\n\n## Action\n\nFinalize the actual public history link **means** the mechanical action that records a no-op if the actual PR link is already present. Otherwise, it appends the exact URL of a newly created PR to the concise Version History, follows up the commit and push, and refreshes the same PR.\n\n## Details\n\nThe actual URL is required. The Action preserves its Tool-call input/result/effect/report references on its parent Action Run. It does not create another PR, guess a URL, merge, or replay an unknown remote outcome.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-628",
    "version": 11,
    "summary": "Verify coherent connector interface\n\n## Scope\n\nRequired future conformance cases for CA-R-1936, CA-M-376 and CA-D-625 cover every CONNECTOR_TOOLS connector and its declared supported subset. These are test specifications, not evidence of execution or passing tests.\n\n## Claim\n\nEvery connector uses the coherent logical input/output roles and performs only its explicitly supplied mechanical operation. Workflow admission owns identity, Version/time, lifecycle and configuration/schema decisions.\n\n## Details\n\n1. Independently author valid query/read/create/modify requests for each connector's admitted subset and logical kinds. Require CA-D-625's exact inner keys and consistent data/current_state/effects/errors result. Reject unknown keys, unsupported operations/kinds, malformed delta, missing or conflicting target/query and unresolved authorization/context.\n2. Read an Atom by explicit full ID without a pre-known Version. Compare complete content and returned actual exact Version/state with independent expected state. Also test pinned and historical Read with exact supplied Version/state. Reject an ambiguous source view, unavailable target or stale pin. Verify no implicit Find or mutation.\n3. Require expected current state for Modify and expected absence for Create. Supply complete workflow-selected schema/identity/lifecycle/Version metadata and delta. Verify the connector checks those bindings. It must never allocate another ID, supply defaults, choose a schema, bump Version/time itself, archive/delete an Atom or rewrite references.\n4. Exercise one connector through different admitted adapters/consumers. Preserve logical identity, request meaning and result evidence. Physical locator or internal computed occurrence position is adapter evidence, not a public target or list selector. No DB implementation is required or inferred.\n5. Test malformed input, absent/ambiguous target, stale state, denied permission, invalid supplied schema evidence and backend failure. Verify the stable structured error code/message/field and actual known/unknown effects. Empty query matches and true no-op are not fabricated errors or mutation effects. Require `effect_uncertain` for every unknown effect. Nonempty errors never indicate success even after a known effect. An exception-free but unverified result cannot pass with empty errors. Prove a true no-op leaves the requested state unchanged.\n6. Query returns matches only; Read returns full requested content. Test unique-current-value and whole-set list deltas where supported, including missing/duplicate/ambiguous values and caller indexes. Verify every unrelated byte/state remains outside the explicit effect.\n7. Under the existing selected service, independently check CA-D-527 outer parameters/target/effect/definition/currentness/authorization bindings. The logical payload neither duplicates the outer protocol nor fabricates Run/Event identities, persistence, transport admission or completion.\n8. Inject an action-local effect/verification failure. Retain the connector's actual known/unknown effect evidence. A composed workflow retains earlier independent successes and stops at its first failure. No cross-Atom rollback or new retry/resume is inferred.\n\n### Acceptance and failure disposition\n\nCompare independently authored requests, complete state/effect/error ledgers and reopened source/history observations. Fail on hidden policy choice, widened scope, lifecycle/schema bypass, false completion or stale-binding acceptance. Existing file/TOML safeguards and action-local safety remain required. Stronger backend/concurrency/publication guarantees need separate proof.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-321",
    "version": 22,
    "summary": "Place Disposable Temporary State",
    "prose_claim": "disposable temporary state in a CAPRMEDIO Project.\n\nThe CAPRMEDIO Project **must** place disposable scratch, staging, test cache, atomic-write intermediate, build intermediate, **and** interrupted-cleanup Carriers under `.caprmedio_tmp/`.",
    "details": "Deleting `.caprmedio_tmp/` **must not** delete governed authority, Project Journal history, installed Framework Engine releases, runtime logs, sessions, databases, service state, **or** resumable state.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-103",
    "version": 16,
    "summary": "Author Atom content before Summary\n\n## Operation\n\nAtom Content Authoring **means** the Action that takes an authorized authoring request, the Atom's Content Role, applicable authority, **and** **any** existing Revision. It prepares a coherent candidate through this flow:\n\n1. For RMED, write Scope describing applicability. **Then** write **=1** Claim within that Scope. For other Content Roles, write their primary contribution: Question, Concern, Objective, **or** Operation.\n2. Write the remaining body sections under CA-D-479 **and** the applicable Method. Keep Details within the primary contribution **and** its applicability. RMED Details support the Claim **without** changing Claim **or** Scope.\n3. Review the primary contribution **and** its applicability against the completed remaining content. For RMED, review Scope **and** Claim together. **If** either needs changing, revise it explicitly within the authorized request **and** recheck the affected sections. Never let Details silently change the contribution **or** applicability.\n4. Derive Summary from the finalized primary contribution within its applicability **only after** that review. For RMED, summarize the Claim within Scope, **not** Scope alone. For an existing Atom identity, compare the needed Summary with its established value. **If** a change is needed, return replacement required under CA-R-1464 rather than mutating that identity.\n5. Return the candidate, its review findings, **and** ready, replacement required, **or** blocked outcome. Unresolved inconsistency **or** unmet permission **or** confidence gates returns blocked, **not** a ready candidate.\n\n## Details\n\nThis Action prepares content; it does **not** persist, promote, replace, **or** archive an Atom. Carrier display order remains Summary first even though Summary is authored last. An Analysis TLDR is part of the other Markdown written **before** the primary-contribution review. It does **not** become the Atom Summary source.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-532",
    "version": 15,
    "summary": "Deliver lifecycle result carriers\n\n## Scope\n\nWorkflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.\n\nThe returned lifecycle dispatch record and its handoff to native Tools and shared Run support.\n\n## Claim\n\nThe route-specific lifecycle payload in CA-D-527's one result preserves the typed request identity; complete sealed and observed target/predecessor Carrier sets and, for Replace, every successor Carrier set; expected and observed Version/digest; operation/model/currentness selection; authorization; diagnostics; exact native outcome; history/lineage; and known/unknown effects. It supplies those facts to the shared result without creating an outer result, a second Event schema, or an assertion of persistence that did not occur.\n\nCA-D-527 alone carries the outer disposition, actual started Run IDs/definition bindings, actual terminal/partial outcome, and Journal append diagnostics when attempted. This payload marks an affected carrier/effect unknown or unverified only when its mutation state is not observed. A missing Journal record or append failure is an independent diagnostic. It does not invalidate an observed mutation or authorize replay. Unstarted preview, decline, and block results invent no Run/Event identity.\n\n## Details\n\n### Required logical workflow result\n\nEach independent Atom action carries its logical target and observed result. A replacement result distinguishes `target`, `created` and `archived` identities with exact Versions and source-state evidence. For target 100, successful fresh-ID replacement reports created 200 and archived 100. A proposed or failed effect is not serialized as an observed created/archived Atom. Known, unknown and unperformed states stay explicit. Every actual changed same-ID state, including archival Status, is N+1 with actual time; exact prior history stays at N. A no-op retains Version/time. Summary or Type changes require replacement.\n\nAn ordered workflow result lists completed actions, the first failure and unperformed remaining targets. Earlier successful actions remain. No cross-Atom all-or-nothing or automatic rollback is implied. Every Summary edit requires fresh-ID replacement and predecessor archival. Incoming references are unchanged unless a separate explicitly authorized Find/Modify workflow changes selected referrers. Resume/retry for this new workflow family and stronger concurrency/publication guarantees remain deferred. This is a required serialization contract, not implementation or admitted-route evidence.\n\nStatus-transition diagnostics distinguish observed broken references from an unperformed or failed transition. An authorized Archive that newly breaks Relations retains the actual transition, lists every newly broken Relation and active referrer, and identifies a separate repair handoff without automatic repair or retargeting.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-517",
    "version": 1,
    "summary": "Carry Codex session context in the shared MCP envelope",
    "prose_claim": "Pass the existing trusted Project binding and native session ID without requiring a plugin. Do not invent a session ID, choose another Project or alter native Tool arguments.\n\nRead the native Codex session identifier from hook input `event.session_id` as the hook's `codex_session_id`. Before submitting the MCP call, put that unchanged value in generic `caller_context.session_id`, alongside the existing `project_root` binding. Other client adapters use the same generic caller context.\n\nThe MCP adapter validates `caller_context` and passes its `session_id` into separate runtime request context. Runtime schemas and behavior do not use a Codex-specific field or branch on the harness or LLM provider. Remove only the outer caller context from native arguments. Preserve a native Tool's own `session_id` argument. Require the session binding for session-scoped Workflow Run operations. Allow it to be absent for stateless operations. Reject disagreement with supplied context instead of silently replacing it.\n\nDeliver the receiving schema and gateway support before enabling the hook to send the new field. No plugin or transcript parsing is required.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-123",
    "version": 31,
    "summary": "Write Definitions of Done",
    "prose_claim": "authoring one Definition of Done.\n\n**To** write one Definition of Done, the Author **must** perform **all** of:\n\n1. Begin the falsification condition expression with: the Plan is **not** Done **if**.\n2. Make **every** atomic condition observable **and** decidable.\n3. Enclose **every** composite condition **and** **every** function argument **in** explicit parentheses.\n4. Evaluate the condition expression according **to** CA-M-122-CORE_META_MODEL-IMPLEMENTATION_METHOD--evaluate-condition-expressions.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1037",
    "version": 26,
    "summary": "Define Lineage Impact Analysis content",
    "prose_claim": "Lineage Impact Analysis Atoms.\n\nA Lineage Impact Analysis Atom **must** identify:\n\n- the changed Atom **and** exact previous **and** new Revisions;\n- change class **and** basis;\n- responsible Operator **and** session provenance;\n- expected impact radius;\n- **every** examined child Revision **and** disposition with its basis;\n- **every** resulting Revision, successor, **or** blocking Concern Atom;\n- **every** recursive branch result; **and**\n- the overall fixed-point conclusion.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-804",
    "version": 5,
    "summary": "Verify relation registry delivery on every image rebuild",
    "prose_claim": "Verify the selected relation registry reaches the image unchanged for every supported build entry point, including Local Release.\n\n- In refresh mode, compile the registry before image assembly. A selected Declaration change changes asset and build identity. Identical inputs yield identical bytes. A compilation failure stops the build.\n- In existing mode, use the checkout registry unchanged. A missing asset stops the build. Verify this mode with the CAPRMEDIO service stopped and without a predecessor image.\n\nVerify the source IDs, Versions, paths and fingerprints in the delivered metadata. Keep Project authority carriers outside the image context. Verify the installed runtime uses the packaged registry. Verify a Declaration change takes effect after asset refresh and image rebuild.",
    "details": null,
    "semantics": null,
    "operation": null
  }
]
```