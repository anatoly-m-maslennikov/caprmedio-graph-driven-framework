---
identity:
  atom_id: CA-A-1382
  ref_id: CA-A-1382@1-draft
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
  updated_at: '2026-11-12T15:35:27.286775+00:00'
destination:
  file:
    name: CA-A-1382@1-draft-ANALYSIS_REPORT--compare-atom-prose-rewrite-batch-b48-741425539647.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Compare Atom prose rewrite batch b48 741425539647

## Details

````json
[
  {
    "ref": "CA-M-396",
    "version": 17,
    "summary": "Make failures observable without disabling healthy runtime",
    "prose_claim": "Classify each observed failure by its actual impact. Expose it through the affected operation's output or runtime failure boundary, and keep a healthy runtime available. Reserve blocking runtime failure and technical ERROR severity for a genuine runtime failure.",
    "details": "### Scope\n\nNew or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.\n\n1. Do not swallow exceptions, erase diagnostic errors, turn a failed result into empty success, or use an unobservable catch-and-continue path. If diagnostic emission fails, report that failure through a still-usable output without hiding the primary outcome.\n2. Separate an error reported to the requester from a technical log level. A request can fail, or be partially completed, while its technical diagnostic is WARNING and the runtime remains healthy.\n3. Invalid input and invalid, missing, stale or ambiguous Project artifacts do not become runtime failures because an exception is named RuntimeError, a request is rejected, or no valid result is available.\n4. Only an actual runtime failure that prevents the affected runtime component from safely operating may use ERROR severity and block that component. Attribute and report the real runtime failure; do not invent a runtime fault to escalate a Project-data problem.\n5. This construction principle does not bypass validation, authorization, source binding or effect safety. Refuse the affected unsafe operation while preserving unrelated runtime availability.\n\n### Retained invalid-input and artifact controls\n\nHandle invalid input and Project artifact problems as operation-local failures: report an attributable error in the Tool, MCP or other caller-visible output, emit a sanitized technical WARNING, and keep the runtime available. Classify each failure by the structured error type, code and state defined by the applicable contract; never classify it from an arbitrary human-message substring.\n\n#### Details\n\n##### Scope\n\nNew or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.\n\n1. Apply this classification to invalid requests and malformed, missing, stale, ambiguous or otherwise unusable Project artifacts and bindings. Technical ERROR severity is not permitted for these conditions, even when the affected operation cannot proceed. Validate invalid arguments before any effect and preserve the prior observable state when validation rejects them.\n2. Give the response a stable error code, a safe explanation and the affected logical target or safe Project-relative path when known. A warning in logs alone is not an error answer; do not rely on exception text or logs as the only output. Human-readable text such as “restart required” is explanatory only; it does not establish a true unavailable state or another failure class without the structured type, code and state.\n3. Reject unsafe or unauthorized effects at their applicable boundary. Continue only independently safe and authorized work; never select a substitute Project, repair input, bypass a guard or retry as an implicit error-handling policy.\n4. Use the error/diagnostic structure of the applicable public result contract without discarding completed data. CA-M-405 governs partial-result presentation; result errors do not determine log severity.\n5. Use the runtime-only blocking/ERROR distinction in CA-M-396. Return even an all-invalid result as an explicit failed or incomplete request outcome, not a crashed service or a false successful empty result.\n\n### Retained shared public-boundary controls\n\nReuse one transport-neutral error-handling owner at public operation boundaries, applying it through a decorator or equivalent shared wrapper rather than duplicating exception classification and logging across Tools, MCP and other callers.\n\n#### Details\n\n##### Scope\n\nPROGRAMMATIC public operation and process execution boundaries, including all first-party Tools, Workflows, Apps, MCP adapters, service entrypoints and background executors shipped in a delivered Docker image. The policy is not limited to AtomSearch, MCP-mediated invocation or a currently running container.\n\n1. The shared boundary classifies known failures, emits the technical diagnostic under CA-M-396/CA-M-399, and uses the caller's declared result/error adapter. It does not invent a competing domain model or force different existing public contracts into an undocumented universal envelope.\n2. Support synchronous and asynchronous operations while preserving their callable signature/metadata, await behavior and cancellation. Do not turn cancellation, process shutdown or an interrupt into successful output.\n3. The operation owner supplies verified completed data, effects and error context under CA-M-405. Pass already-structured partial or failed outcomes through without erasing their data, duplicating diagnostics or reclassifying a Project artifact as runtime failure.\n4. Use explicit failure classification and actual context rather than treating a Python exception base class, including RuntimeError, as proof that the runtime is broken. An unexpected failure must remain visible; never silently return success.\n5. Apply the boundary once at the relevant public execution owner, not around every helper. Registration and discovery remain effect-free. Generic handling does not start Workflows, append Journals, retry, repair, roll back or replay business work.\n6. Reuse the established shared logger and canonical execution/validation owners. Keep transport-specific response encoding in its adapter and business lifecycle recording with the Workflow executor.\n7. Derive the affected runtime coverage from the delivered image entrypoints, executable modes and their actual dispatch owners. Wire the shared handling at those owners so direct invocation, worker execution and service execution do not bypass it. Reuse existing package inventories; do not introduce a competing runtime registry, decorate every helper or modify third-party internals. A verified process-startup/runtime failure may terminate the affected process; a failed request or business Workflow does not imply that the runtime is broken.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-216",
    "version": 12,
    "summary": "Move one private carrier\n\n## Operation\n\nMove One Private Carrier **means** the reusable private Action that makes one explicitly bound file or folder location change behind an admitted logical connector `modify`. It preserves the exact admitted carrier frontier **without** choosing a lifecycle transition.\n\n### Inputs **and** preconditions\n\nRequire CA-D-630's private move binding, approved source and destination roots **and** parents, expected source state, explicit destination **and** expected absence for an actual move, sealed permission and context, **and** complete approved folder inventory. **Any** basename change **must** already be explicit. For an Atom carrier, require the already admitted exact lifecycle, currentness and history context. No helper permission substitutes for it.\n\n### Action **and** result\n\nRequire CA-R-1941's exact staged-change review **and** fresh trusted authorization and window record, including recorded outside-edits-paused confirmation. Within that confirmed window, apply CA-R-1941/CA-M-381 safety checks. Recheck the complete bound source, destination, parents, inventory, preservation, authority **and** permission frontier **before** the effect. Retain independent readback **and** verification. Perform **only** the explicitly bound location change. Reject root or ancestor effects, escapes, symlinks or substitution, stale state, collisions, overwrite, merging **and** unlisted entries. Independently verify destination contents, modes and inventory, source absence **and** unchanged unrelated frontier.\n\nReturn CA-D-625's actual data, state, effects and errors. A same-binding no-op needs verified unchanged requested state. A missing expected-present source does **not** prove an earlier move. Retain known partial effects **and** mark uncertainty with `effect_uncertain`. Errors are **not** success. No new transaction, retry, resume **or** concurrent-publication guarantee is implied.\n\n## Details\n\nArchive, retire, upgrade, replacement, identity/Version metadata and history remain owned by their existing admitted operation. This Action supplies only internal carrier movement. It never reports lifecycle completion or rewrites references. No executable or runtime admission is established.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1694",
    "version": 42,
    "summary": "Requirement — Keep Requirements realization-agnostic",
    "prose_claim": "Requirement claims and their internal realization.\n\n\n**every** Requirement **must** state its required outcome, obligation, permission, prohibition, **or** accepted external boundary **without** prescribing internal code **or** code organization merely as a construction choice.\n\n- an accepted external interface, protocol, data shape, **or** host obligation **may** be required **when** conformance **to** that boundary is itself the required outcome. this does **not** prescribe an **otherwise** interchangeable internal realization.\n- a programming language, library, algorithm, function, class, module, source-file organization, **or** another construction technique does **not** become a Requirement solely because it is normative; classify its primary contribution under CA-R-1531@20 **and** CA-R-2513.\n- packaging, release, deployment, distribution, installation, migration, upgrade, **and** rollback are topics, **not** Content Role selectors. classify a Carrier representation **or** placement under CA-R-2515, reusable Action **or** Workflow behavior under CA-R-2463, **and** treat an actual realization as native Implementation rather than an Atom Content Role. mentioning one of those topics does **not** turn a procedure into Delivery authority.\n- a candidate that combines this independently replaceable outcome with an independently replaceable construction, Carrier, **or** operational Claim requires separate Atoms under the one-Claim authority; a composite Claim is **not** split merely because it has multiple clauses.",
    "details": "Functional and non-functional Requirements both specify outcomes. A performance target can have an Engineering Subject. Subject and Content Role are independent. Architecture remains Method even when mandatory. The methodology's own model definitions and Entity Definition constraints remain within Requirement authority.\n\nCA-R-2512 owns the Requirement Content Role definition. This Atom constrains realization prescription **without** duplicating the definitions of the other Content Roles.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-176",
    "version": 13,
    "summary": "Build the candidate release image\n\n## Step\n\nThis Step invokes CA-O-168 once with phase `candidate_image_build`. It binds CA-O-175's staged package, exact source and context rows, and immutable candidate image identity. The frozen Docker worker has no Docker socket and cannot substitute for host Candidate E2E.\n\n## Details\n\nA tag, cached image or successful build alone creates no authority. A build mismatch, host mount, stale package or source, unsafe context, failed result or missing Journal receipt stops the process without proof, promotion or old-image removal.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1942",
    "version": 12,
    "summary": "Read one complete TOML configuration\n\n## Scope\n\nEffect-free complete Read of one explicit Project Structure **or** Project Settings configuration through the shared TOML connector.\n\n## Claim\n\nThe Configuration Read result **must** contain the complete authoritative TOML source **and** its complete parsed values for exactly one logical configuration **in** the bound Project. It **must** include exact observed source-state evidence **and** no mutation. Read is independently callable **without** Query, Modify **or** an enclosing Workflow.\n\nAn unpinned current Read **must not** require a pre-known source pin. A supplied pin **or** explicit historical view **must** match the exact available admitted source. Missing history **or** stale evidence **must not** fall back **to** the latest source. The caller's context selects source authority **and** schema. The connector checks these bindings **without** choosing them. Missing, ambiguous, denied, invalid **or** unreadable sources **must** return a structured failure, **not** a successful empty **or** partial document.\n\n## Details\n\nCA-D-631 fixes the representation **and** CA-O-218 binds Read on the same TOML connector as CA-O-204 Modify. Read changes no configuration, Carrier, history, Version, timestamp, lifecycle **or** runtime state. This contract does **not** admit a live route, a new backend **or** new history retention.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-559",
    "version": 19,
    "summary": "Deliver runtime Journals to configured sinks",
    "prose_claim": "technical and business runtime Journal Carriers.\n\n\nruntime technical **and** business Journals **may** be delivered **to** an explicitly configured local database, remote database, **or** governed logging sink. these Carriers **need not** reside under `.caprmedio_<project_name>/_journal/` **or** `.caprmedio_runtime/`.",
    "details": "Journal classification and recorded-history authority are independent of storage technology. The configuration identifies the intended sink. Applicable production logging policy remains in force. The shared Project-control Work Journal and persistent view Projections retain their separate _journal and _projection locations. Runtime cleanup and sink migration must preserve accepted Journal history. This Delivery does not authorize history deletion or change retention policy.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-457",
    "version": 2,
    "summary": "Reuse formal notation and write isolated constraints in prose",
    "prose_claim": "- Use admitted CFEL when it expresses the constraint.\n- Use short Claim prose only when CFEL cannot express the constraint without a single-use extension.\n- Do not invent syntax for one constraint.\n- State IS_PROPERTY_OF acyclicity in prose, including no self-loop.\n- Repetitive prose or Semantics is not required.",
    "details": "Authoring a constraint does not establish its implementation or verification.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-375",
    "version": 22,
    "summary": "Preserve the last valid MCP frontier",
    "prose_claim": "An invalid MCP frontier refresh rejects the candidate and reports its active-Tool collision. It preserves preceding complete valid bytes only for recovery, not as current or call authorization. Replacement is atomic at the validated frontier boundary.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-570",
    "version": 26,
    "summary": "Serialize Draft Revision Lineage",
    "prose_claim": "the recorded lineage metadata of a Project-owned Draft Atom Carrier, when it already exists.\n\n\nA Draft Atom **must not** require `revision_lineage`, a retained Draft-history entry or a trusted Draft head for Create, Update, promotion, another admitted Status change or their success. Every Draft Carrier carries the mandatory Draft `atom_id` marker under CA-D-378/CA-D-446; its filename follows CA-D-650.\n\nExisting `revision_lineage: {history_entry_ref: {history_revision, path}}` metadata and the actual retained records it references may remain as recorded historical data. Their presence, absence, encoding, resolvability, origin, parent chain, head/leaf status or consuming-successor state **must not** become a mutation or completion gate. Do **not** require a caller or writer to register, reconstruct, repair, reserve, append or consume such a record to admit the current operation.\n\nWhen a Current Atom changes, archive its predecessor with the old numeric Version and Updated At, an Archived status and a version-qualified identity under CA-D-446/CA-D-565; the Current successor follows the normal Version and timestamp rules. Do **not** fabricate history or reinterpret an observed value as evidence of an event that was not observed. Preserve the exact admitted target, ordinary Summary/replacement rules, applicable schema, collision/currentness checks and permissions. No new identity registry, history writer, recovery framework or Journal protocol is introduced.",
    "details": "CA-D-568 binds identity continuity without a retained-history prerequisite. Journal existence, completeness, baseline, chain, prior entry or receipt does not grant permission or gate mutation success. An actual append attempt reports its own I/O result independently. It never replays the performed effect.\n\n### Subjects-only edit-draft exception\n\nCA-D-446's explicit source-pinned Subjects-only edit draft is a derived proposed next Revision of an existing Atom. It is not a new Atom Draft or another canonical original. It carries the admitted `<canonical-ID>@<proposed-version>-draft` ID marker at its declared Header path, logical Draft Status encoded as `draft`, and a matching Draft-marker filename in the owning role's `draft/` folder. The exact canonical source remains untouched. The reviewed packet retains the canonical target/source pin and exact draft path/digest for that specific proposed edit. Approval restores the canonical ID and original Status, independently validates normalized Subjects-only materialization, and archives the old predecessor identity/version under the ordinary archive rules before the N+1/actual-time update. Staging and publication require no retained Draft-history entry, `revision_lineage`, unique Draft head, origin chain or consuming successor. New-Atom Drafts and ordinary lifecycle Drafts carry a marker under CA-D-378/CA-D-446. Filename rules are governed by CA-D-650. Canonical ID grammar and the normal source, schema, identity/collision, permission and actual-history safeguards are unchanged.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-643",
    "version": 17,
    "summary": "Evaluate workload resource bounds",
    "prose_claim": "Accept resource behavior only when meaningful configured limits and workload-dependent evidence prevent uncontrolled growth and resource exhaustion. Evaluate aggregate memory, concurrency, queues, subprocesses, temporary output and retention where applicable. A fixed worker count is not itself a bound. This Evaluation does not invent one universal numeric limit.",
    "details": "### Scope\n\nPROGRAMMATIC Tools, workflows, Apps, MCP handlers, background jobs and subprocesses whose use can grow with input, concurrency, queue depth, retention or duration.\n\n- Define workload dimensions and configured limits, including scope, admission and refusal or recovery behavior.\n- Exercise small, normal, peak and over-limit workloads, including concurrent and queued work, and observe aggregate consumption.\n- Verify over-limit work is refused, bounded, evicted or degraded as declared, without silent runaway allocation, unbounded retry or OOM-dependent recovery.\n- Check subprocess lifetime, temporary files, buffers, logs and retained results; report an unmeasured applicable dimension as unresolved.\n- Prefer workload-scaled evidence over arbitrary low test caps.",
    "semantics": null,
    "operation": null
  }
]
````