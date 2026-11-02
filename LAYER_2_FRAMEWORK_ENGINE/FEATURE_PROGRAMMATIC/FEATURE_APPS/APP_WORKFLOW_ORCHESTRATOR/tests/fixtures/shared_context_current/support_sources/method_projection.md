---
subjects:
  governs: Method/Mutation Initiative Binding
  depends_on: []
version: 13
updated_at: "2026-10-22 12:45:09 +0400"
relations:
  method_for:
  - CA-R-1094
  derived_from:
  - CA-A-058
atom_id: CA-M-191
content_role: Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Summary

Bind one programmatic mutation to its Initiative

## Scope

## Claim

## Details

### Applicable when

apply **before** accepting **or** dispatching a programmatic mutation governed by
CA-R-1094.

### Procedure

1. resolve **or** create **=1** sealed Initiative from the accepted human
   instruction. it **may** bind **to** a persisted Plan **or** Task **or** remain an ephemeral
   session task.
2. assign one stable action identity **and** preserve a short instruction-derived
   summary plus enough structured context **to** identify the instruction.
3. attach the Initiative **and** action identities **before** **any** Hook, queue, worker,
   retry, Git, Journal, **or** reconciliation handoff.
4. propagate both identities unchanged through **every** handoff. a process,
   thread, adapter, queue, **or** worker identity **may** be linked as execution
   context but **must not** replace them.
5. return an explicit blocked outcome **before** mutation **when** either identity is
   missing, ambiguous, changed, **or** bound **to** more than one Initiative.

### Outcome

**every** accepted mutation remains attributable **to** one human-origin Initiative
**and** one stable action across asynchronous execution **and** provenance systems.

### Failure or stop

stop **before** mutation **when** the Initiative is unsealed, the action identity is
absent **or** reused for another Initiative, **or** a handoff cannot preserve both
identities.

### Sources

- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)


---
subjects:
  governs: Method/Callable Frontier Publication
  depends_on: []
version: 14
updated_at: "2026-10-22 12:45:09 +0400"
relations:
  method_for:
  - CA-R-1096
  derived_from:
  - CA-A-058
atom_id: CA-M-193
content_role: Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
---
# Summary

Supply the active Tool frontier to MCP

## Scope

The source-bound active callable Tool and Workflow frontier for a Project, and
the initial union of those validated per-Project frontiers in the shared MCP
runtime.

## Claim

Direct read and query Tools delegate to their canonical providers without a
mandatory Workflow Orchestrator wrapper. Internal CONNECTORS/adapters and
PROJECT_TOOLS are not members of this MCP callable frontier. A shared runtime
may publish the union of valid native Project frontiers, but every invocation
still uses one validated Project binding and no Tool meaning changes.

## Details

### Applicable when

apply **when** MCP builds **or** refreshes the callable frontier supplied by TOOLS.

### Procedure

1. enumerate the complete current set of active declared callable CAPRMEDIO Tools and declared Workflows from the
   source-bound capability frontier.
2. read **and** validate **every** active Tool's or Workflow's machine-invocation contract **without**
   inferring missing meaning from its code **or** runtime state.
3. project **=1** stable callable endpoint for **every** valid active Tool.
4. omit inactive **and** explicitly disabled Tools; report **every** invalid active
   Tool as a diagnostic rather than silently omitting it.
5. delegate **every** admitted call **to** its declared Tool or Workflow provider **without** duplicating **or** changing its
   meaning, inputs, outcomes, **or** mechanics.
6. replace the exposed frontier **only** **after** the complete candidate projection
   validates; preserve the preceding valid frontier **when** refresh fails.
7. For a shared runtime, eagerly validate the bounded candidate Project
   frontiers and publish their initial union. Admit a same-name Tool across
   Projects only when its input and output schemas are identical; quarantine
   and diagnose the affected Project Tool on a conflict.
8. Add the outer `project_root` only at the native input schema root while
   preserving `$defs`, then pass the native request and result contract
   unchanged to the bound Project provider. An inactive or disabled Project
   Tool refuses the call. A new Tool name requires explicit shared restart and
   client reconnect; do not assume `tools/list_changed`.

### Outcome

MCP exposes one complete, deterministic projection of valid active Tools and Workflows **and**
remains a replaceable interface rather than a second Tool authority.
preserving an earlier frontier **after** a failed refresh does **not** make it current;
apply the publication boundary **in** CA-R-1110.

### Failure or stop

stop refresh **and** preserve the preceding valid frontier **when** active Tool or Workflow
enumeration is incomplete, endpoint identities collide, **or** a machine contract
is missing **or** invalid. reject a call that cannot delegate unchanged.

### Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [Model Context Protocol: tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)


---
atom_id: "CA-M-284"
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
claim_target_scope_unit: "PROGRAMMATIC"
local_tier: "General"
global_tier: 7
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: Method/Project Settings Snapshot
  depends_on:
  - Entity/Carrier
  - Entity/Node/Continuant/Project.Settings
version: 17
updated_at: "2026-10-22 12:45:09 +0400"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
---
# Summary

Read Engine settings through one shared boundary

## Scope

apply **when** PROGRAMMATIC behavior depends on Project Settings.

## Claim

use one centralized Settings Reader for **every** applicable Tool, App, **and** MCP
component. the Reader reads the authoritative Project Settings Artifact,
validates the complete input, **and** returns an immutable typed snapshot with
the actual validated values, exact selected Project, physical source path,
raw SHA-256 Digest, **and** declared schema marker. the Reader **must not** query
the Work Journal **or** determine logical Revision **or** currentness. the snapshot
is derived; Project Settings is **not** a Projection.

## Details

### Procedure
1. read the authoritative Project Settings Carrier bound by CA-D-364 through
   the shared Reader; do **not** infer a replacement from a legacy filename.
2. validate the complete carrier at the boundary **and** return structured
   diagnostics for invalid input.
3. pass the immutable snapshot explicitly **to** the consuming deterministic core
   **or** application service.
4. do **not** add component-specific parsers, default chains, environment
   fallbacks, semantic overrides, **or** writes **to** the Reader.
5. make the control panel use the same Reader **and** request changes **to** the
   authoritative Project Settings Artifact through its dedicated Doer, **not**
   through the Reader, its immutable snapshot, **or** a Projection.

### Outcome

**every** component observes one validated settings snapshot **without** duplicating
parsing **or** inventing a second control panel.

### Failure or stop

stop **when** the authoritative Project Settings Carrier is missing **or** schema-invalid,
mandatory physical source path **or** Digest provenance is absent, **or** a consumer
would bypass **or** mutate the shared snapshot.

### Sources

- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-395
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-22 12:45:09 +0400"
subjects:
  governs: Method/Change Dependency Closure
  depends_on:
  - 'Entity/Node/Continuant/Atom/Content Role: Requirement'
  - 'Entity/Node/Continuant/Atom/Content Role: Method'
  - 'Entity/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Entity/Node/Continuant/Atom/Content Role: Delivery'
  - Entity/Carrier
relations:
  child_of:
  - CA-M-403
  depends_on:
  - CA-E-639
  - CA-M-402
  - CA-M-417
---
# Summary

Prepare coherent changes through a closed dependency world

## Scope

Preparation of a bounded PROGRAMMATIC implementation change and its applicable test/fixture world, including descendant Scope Units.

## Claim

Prepare a change by deriving its bounded affected-surface and dependency closure from applicable governing sources and actual consumers, then reconcile that closure through existing canonical owners as one coherent increment. Construct the required verification world from an explicit, self-contained selection of consistent inputs rather than ambient mutable Project state or duplicated fixture logic.

## Details

1. Bind the requested outcome, applicable source revisions, authorized scope and expected state. Identify the actual consumers and supporting contracts, schemas/registries, configuration, dependencies, fixtures and delivery carriers affected by the change. Record an unresolved required input or semantic decision explicitly; use the existing authority/conflict boundary instead of inventing its answer.
2. Map each required adjustment to its existing capability or artifact owner. Reuse canonical parsers, resolvers, adapters and valid scenario/carrier builders; do not create another behavioral owner or a facade over unreconciled consumers. Keep the closure bounded to what the requested change actually needs.
3. For a reproducible fixture world, select its input bytes, governing definitions, support/schema/registry/configuration inputs, dependency/environment binding and expected results together. Include dependencies read lazily by the exercised path. Materialize isolated cases using shared builders and the selected frozen inputs; do not mix frozen source bytes with mutable live manifests, expected-output generators or installed pins.
4. Keep intentionally invalid targets distinct from valid harness/support state. Carry their expected refusal or failure without repairing away the condition being tested. Keep any live-current compatibility check separately identified rather than letting live state change the frozen oracle.
5. Reconcile affected implementation, consumers and fixture/delivery metadata together when the exercised contract deliberately changes. Inspect known mechanical consistency and required environment/dependency availability during preparation, so missing support is diagnosed at its owner instead of hidden behind a later behavioral assertion.
6. Execute the Evaluation portfolio selected under the applicable E policy and M285, retaining actual outcomes and unresolved coverage. A prepared world is not proof of passing tests or completed effects. Apply the new readiness Evaluation without creating another approval, Journal, live-Atom or release gate.


---
atom_id: CA-M-396
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-22 12:45:09 +0400"
subjects:
  governs: Method/Runtime Failure Classification
  depends_on: []
relations:
  relates_to: [CA-M-405, CA-M-414]
---
# Summary

Make failures observable without disabling healthy runtime

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

## Claim

Classify each observed failure by its actual impact, expose it through the affected operation's output or runtime failure boundary, and keep a healthy runtime available. Reserve blocking runtime failure and technical ERROR severity for a genuine failure of the runtime itself.

## Details

1. Do not swallow exceptions, erase diagnostic errors, turn a failed result into empty success, or use an unobservable catch-and-continue path. If diagnostic emission fails, report that failure through a still-usable output without hiding the primary outcome.
2. Separate an error reported to the requester from a technical log level. A request can fail, or be partially completed, while its technical diagnostic is WARNING and the runtime remains healthy.
3. Invalid input and invalid, missing, stale or ambiguous Project artifacts do not become runtime failures because an exception is named RuntimeError, a request is rejected, or no valid result is available.
4. Only an actual runtime failure that prevents the affected runtime component from safely operating may use ERROR severity and block that component. Attribute and report the real runtime failure; do not invent a runtime fault to escalate a Project-data problem.
5. This construction principle does not bypass validation, authorization, source binding or effect safety. Refuse the affected unsafe operation while preserving unrelated runtime availability.


---
atom_id: CA-M-397
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-22 12:45:09 +0400"
subjects:
  governs: Method/Operation-Local Failure Containment
  depends_on: []
relations:
  child_of: [CA-M-396]
  relates_to: [CA-M-404, CA-M-398]
---
# Summary

Contain invalid input and Project artifact failures

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

## Claim

Handle invalid input and Project artifact problems as operation-local failures: report an attributable error in the Tool, MCP or other caller-visible output, emit a sanitized technical WARNING, and keep the runtime available.

## Details

1. Apply this classification to invalid requests and malformed, missing, stale, ambiguous or otherwise unusable Project artifacts and bindings. Technical ERROR severity is not permitted for these conditions, even when the affected operation cannot proceed.
2. Give the response a stable error code, a safe explanation and the affected logical target or safe Project-relative path when known. A warning in logs alone is not an error answer; do not rely on exception text or logs as the only output.
3. Reject unsafe or unauthorized effects at their applicable boundary. Continue only independently safe and authorized work; never select a substitute Project, repair input, bypass a guard or retry as an implicit error-handling policy.
4. Use the error/diagnostic structure of the applicable public result contract without discarding completed data. CA-M-398 governs partial-result presentation; result errors do not determine log severity.
5. Use the runtime-only blocking/ERROR distinction in CA-M-396. Return even an all-invalid result as an explicit failed or incomplete request outcome, not a crashed service or a false successful empty result.


---
atom_id: CA-M-398
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-22 12:45:09 +0400"
subjects:
  governs: Method/Partial Result Reporting
  depends_on: []
relations:
  child_of: [CA-M-405]
  relates_to: [CA-M-404, CA-M-397]
---
# Summary

Return verified partial results before failure details

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

## Claim

When an operation has completed only part of the request, retain and present the verified completed results first, followed by the attributable errors and unfinished or uncertain work, without representing aggregate success.

## Details

1. At the operation owner, retain actual completed items and observed effects as work proceeds. A general exception wrapper cannot reconstruct lost local progress or decide business commit boundaries.
2. Return completed data together with errors in the same applicable response contract. Mark incompleteness or partial outcome explicitly and identify failed, skipped, unattempted and uncertain items where known. Do not discard useful verified data because another independent item failed.
3. Results-before-errors is presentation and consumption priority, not a demand for JSON member ordering or a new universal response schema. Preserve each transport's governed result contract while making both available.
4. Do not label an unverified, rolled-back or uncertain effect as completed, leak unsafe/private intermediate data, broaden an effect frontier, or weaken an explicitly atomic operation. If no verified result exists, state that honestly.
5. Do not introduce automatic retry, compensation or replay. Preserve actual recovery information and leave those actions with their declared owner.


---
atom_id: CA-M-399
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-22 12:45:09 +0400"
subjects:
  governs: Method/Business Workflow Lifecycle Recording
  depends_on: []
relations:
  child_of: [CA-M-426]
  relates_to: [CA-M-414, CA-R-1095, CA-M-396, CA-M-397]
---
# Summary

Record business Workflow lifecycle separately from technical diagnostics

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

## Claim

Keep technical diagnosis on structured stdout/stderr streams and record actual business Workflow lifecycle events through the declared Journal owner, without turning a technical warning into a business event.

## Details

1. Emit technical diagnostics through the shared logger with the actual Project prefix and sanitized context. The Docker runtime captures these streams under its bounded retention/back-pressure configuration; use stderr when stdout carries MCP/Tool protocol or result data.
2. Apply CA-M-396 and CA-M-397 to severity: input and Project artifact issues use WARNING; ERROR is reserved for real blocking runtime failures. Do not confuse a response error or a failed business Workflow with ERROR-level logging.
3. For an actually admitted/started business Workflow, record its observed started, failed and completed lifecycle transitions, as applicable, through its executor and the shared Journal owner. A technical cause may explain a real business failure without copying technical log records or stack traces into the Journal.
4. A preflight rejection with no admitted/started business Workflow must not fabricate a Workflow, Run, started/failed event or completion event. Direct read-only Tool calls do not gain hidden Journal effects from logging or generic error handling.
5. Keep business records truthful and independent from Git and technical-log retention. Journal incompleteness is not an admission gate. Preserve existing historical Journal bytes and do not rewrite old technical entries as part of this Method.


---
atom_id: CA-M-400
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: General
global_tier: 7
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-22 12:45:09 +0400"
subjects:
  governs: Method/Public Operation Error Boundary
  depends_on: []
relations:
  child_of: [CA-M-403]
  relates_to: [CA-M-396, CA-M-397, CA-M-398, CA-M-399]
---
# Summary

Apply one shared public-operation error boundary

## Scope

PROGRAMMATIC public operation and process execution boundaries, including all first-party Tools, Workflows, Apps, MCP adapters, service entrypoints and background executors shipped in a delivered Docker image. The policy is not limited to AtomSearch, MCP-mediated invocation or a currently running container.

## Claim

Reuse one transport-neutral error-handling owner at public operation boundaries, applying it through a decorator or equivalent shared wrapper rather than duplicating exception classification and logging across Tools, MCP and other callers.

## Details

1. The shared boundary classifies known failures, emits the technical diagnostic under CA-M-396/397/399, and uses the caller's declared result/error adapter. It does not invent a competing domain model or force different existing public contracts into an undocumented universal envelope.
2. Support synchronous and asynchronous operations while preserving their callable signature/metadata, await behavior and cancellation. Do not turn cancellation, process shutdown or an interrupt into successful output.
3. The operation owner supplies verified completed data, effects and error context under CA-M-398. Pass already-structured partial or failed outcomes through without erasing their data, duplicating diagnostics or reclassifying a Project artifact as runtime failure.
4. Use explicit failure classification and actual context rather than treating a Python exception base class, including RuntimeError, as proof that the runtime is broken. An unexpected failure must remain visible; never silently return success.
5. Apply the boundary once at the relevant public execution owner, not around every helper. Registration and discovery remain effect-free. Generic handling does not start Workflows, append Journals, retry, repair, roll back or replay business work.
6. Reuse the established shared logger and canonical execution/validation owners. Keep transport-specific response encoding in its adapter and business lifecycle recording with the Workflow executor.
7. Derive the affected runtime coverage from the delivered image entrypoints, executable modes and their actual dispatch owners. Wire the shared handling at those owners so direct invocation, worker execution and service execution do not bypass it. Reuse existing package inventories; do not introduce a competing runtime registry, decorate every helper or modify third-party internals. A verified process-startup/runtime failure may terminate the affected process; a failed request or business Workflow does not imply that the runtime is broken.


---
atom_id: CA-M-401
content_role: Method
type: Implementation Method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-22 12:45:09 +0400"
subjects:
  governs: Method/Project Identity Binding
  depends_on: []
relations:
  method_for: [CA-R-2008]
---
# Summary

Bind caller context and carry Project identity

## Scope

Request binding, shared Project discovery, bounded loading and all dependent
work in the shared HTTP MCP runtime.

## Claim

Obtain the caller's explicit `project_root` through the supported client
contract, resolve it against the admitted host configuration and Project
declarations, then freeze one validated Project identity for the complete
operation. Carry that binding through Tool execution, asynchronous continuations,
nested calls, receipts and result attribution while preserving the native
request and each Project's actual state owners.

## Procedure

1. Load and validate the host TOML at
   `XDG_CONFIG_HOME/caprmedio/runtime.toml`, or
   `~/.config/caprmedio/runtime.toml` when the environment variable is absent.
   Require `schema_version = 1` and a `[shared_mcp]` section with
   `projects_root`, `http_port`, and optional `max_loaded_projects` (default
   `2`). Treat a host-config change as a restart boundary.
2. Eagerly enumerate a bounded candidate set below the configured canonical
   non-symlink `projects_root`. Admit only existing canonical Project roots
   whose declarations provide an authoritative prefix, control-root and full
   opaque identity. Reject outside, missing, symlink-substituted, ambiguous or
   undeclared roots without sibling/parent/global-cwd fallback.
3. Carry the outer `project_root` plus the native request unchanged to the
   shared MCP. Resolve the same absolute host/container root without
   translation; otherwise retain the admitted mapping revision. Set the
   root-per-call context and construct a child ProjectGateway keyed by the
   validated identity. Do not set a global `current_project`.
4. Load or reuse only that Project's applicable sources, settings, model
   generation, native Tool frontier, DBOS/Git/Journal state, locks, caches and
   result paths. Derive keys from the opaque full identity, not prefix text
   alone. A context at `max_loaded_projects` may evict only an idle entry;
   refuse a busy admission and never retry or replay it.
5. Build the initial public frontier as the union of valid native Tool
   contracts from admitted Projects. A same-name Tool is shared only when its
   input and output schemas are identical. Quarantine and diagnose the
   affected Project Tool on a conflict. Add the outer `project_root` only at
   the native input schema root while preserving `$defs`; disabled/inactive
   Project Tools refuse calls and native Tool meaning remains unchanged.
6. Discover new or nested Projects lazily only for already advertised,
   compatible Tool names. Require explicit shared restart and client reconnect
   before publishing a new Tool name; do not rely on
   `tools/list_changed`. Carry the frozen binding through nested and
   asynchronous work and recheck it at existing freshness/effect boundaries;
   never silently switch mappings.
7. Keep health and diagnostics read-only. Report host readiness from initialized
   published frontier state, and show known Project contexts (prefix and opaque
   identity) separately from unloaded/unknown contexts. Host startup/log events
   are unbound; request logs use the real bound prefix. Health GETs do not
   dispatch, poll, reload, mutate or replay work.

## Outcome

Every shared-MCP operation is attributable to exactly one validated Project
frontier and retains the Project's real state ownership, while one container and
one external HTTP endpoint can serve multiple Projects.

## Failure or stop

Stop the affected call on an invalid host config, outside/symlink/ambiguous
root, missing declaration, stale mapping, unavailable/busy pool admission or
conflicting Tool contract. Refuse without selecting another Project, changing a
native Tool contract, retrying or replaying uncertain work.


---
atom_id: CA-M-402
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Core"
global_tier: 6
status: Active
subjects:
  governs: "Method/Business Logic Authority"
  depends_on:
    - "Method/Implementation Reconstructability"
    - "Method/Implementation Authorization"
    - "Entity/Node/Continuant/Atom/Content Role: Requirement"
    - "Entity/Node/Continuant/Atom/Content Role: Method"
    - "Entity/Node/Continuant/Atom/Content Role: Evaluation"
    - "Entity/Node/Continuant/Atom/Content Role: Delivery"
    - "Entity/Node/Continuant/Actor/Type:Operator"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
author: Anatoly Maslennikov
relations:
  derived_from: [CA-A-1185]
---
# Summary

Implement only declared business logic

## Scope

New or changed PROGRAMMATIC implementation, including its tests.

## Claim

Implement business logic **only** as declared in the applicable Active RMED. **Do not** invent additional policies, restrictions, approval gates, lifecycle rules or workflows. **When** the specification has a gap or conflict affecting the behavior, ask the Operator **before** implementing that behavior.

## Details

Candidate source: [CA-M-384@1](archive/CA-M-384-PROGRAMMATIC-CORE-METHOD--implement-only-declared-business-logic@1.md)

1. Read the applicable Active RMED before changing behavior. A derived prompt helps find and use the rules; it does not add authority.
2. Choose ordinary implementation details freely within those rules. A choice of algorithm, function layout or internal data structure does not require its own policy when it preserves the declared behavior and constraints.
3. If an additional business rule seems necessary, explain the gap and the smallest proposed change to the Operator. Do not silently implement it or make tests require it. Continue independent work that does not depend on that decision.
4. After the Operator resolves the gap, align the affected RMED before implementing the new business rule. Do not create a new approval mechanism to enforce this Method.

## Outcome

Implementation and tests realize the declared behavior without adding an implicit second specification.

## Failure or stop

Pause the affected behavior when its business meaning requires an undeclared decision. This Method does not authorize removing existing checks or overriding applicable Active RMED without an Operator decision.


---
atom_id: CA-M-403
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Core"
global_tier: 6
status: Active
subjects:
  governs: "Method/Behavior Ownership"
  depends_on:
    - "Method/Authoritative Representation"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
author: Anatoly Maslennikov
---
# Summary

Keep one canonical owner of behavior

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** expose a declared capability through different transports, adapters or storage backends, reuse its canonical behavioral owner rather than independently redefining its meaning.

## Details

Candidate source: [CA-M-387@2](archive/CA-M-387-PROGRAMMATIC-CORE--keep-one-canonical-owner-of-behavior@2.md)

- Adapters translate supported requests and results; they do not invent domain decisions or hidden Workflow composition.
- Keep identity, lifecycle, semantic admission and sequencing with their declared owner.
- Replacing a transport or backend must not silently change the declared capability.

Source basis: CA-M-341, CA-M-376.


---
atom_id: CA-M-404
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Core"
global_tier: 6
status: Active
subjects:
  governs: "Method/Effect Authorization"
  depends_on:
    - "Method/Implementation Authorization"
    - "Method/Behavior Ownership"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
author: Anatoly Maslennikov
---
# Summary

Limit effects to the authorized target and delta

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** change state, bind the admitted target, explicit delta and required expected state, then apply **only** that authorized change.

## Details

Candidate source: [CA-M-388@2](archive/CA-M-388-PROGRAMMATIC-CORE--limit-effects-to-the-authorized-target-and-delta@2.md)

- Do not substitute targets, broaden the affected frontier or add semantic operations.
- Observing additional files or state does not grant permission to change them.
- An unresolved, ambiguous, stale or unsupported binding stops the affected change; it does not authorize a fallback target or broader effect.

Source basis: CA-M-376, CA-M-381.


---
atom_id: CA-M-405
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Core"
global_tier: 6
status: Active
subjects:
  governs: "Method/Outcome Evidence"
  depends_on:
    - "Method/Statement Authority"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
author: Anatoly Maslennikov
---
# Summary

Report outcomes from observed evidence

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** execute PROGRAMMATIC behavior and report its outcome, compare the requested result with observed effects and retained execution evidence, distinguish verified completion, verified no-op, partial effects and uncertain effects, and reuse established evidence rather than blindly replaying completed or uncertain mutations.

## Details

Candidate source: [CA-M-390@2](archive/CA-M-390-PROGRAMMATIC-CORE--report-outcomes-from-observed-evidence@2.md)

- A returned call, scheduler completion or absence of reported errors does not alone establish the requested result.
- A no-op means the requested state was already satisfied and remained unchanged; do not fabricate writes or history.
- Preserve partial results, uncertainty, gaps and blockers honestly. Outcome reporting introduces no automatic retry or recovery policy.

Source basis: CA-M-376, CA-M-323, CA-M-322.


---
atom_id: CA-M-406
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Python Idiom Selection"
  depends_on:
    - "Method/Compatibility Boundary"
    - "Method/Necessity"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Adopt current Python idioms only for declared benefit

adopt a stable idiom available **in** the selected Python boundary **only** **when** it
improves a named project quality such as correctness, understandability,
safety, **or** measured performance. preserve the simpler supported idiom **when** a
newer construct adds no useful distinction.

## Details

Candidate source: [CA-M-280@8](archive/CA-M-280-PROGRAMMATIC-CORE-METHOD--adopt-current-python-idioms-only-for-declared-benefit@8.md)

## Applicable when

apply **when** new **or** materially changed PROGRAMMATIC Python source proposes a
runtime-specific language construct **or** concurrency model.

## Procedure

1. state the quality improved **and** the supported Python boundary that admits
   the idiom.
2. prefer the simplest current construct that expresses the required meaning.
3. use f-strings for immediate trusted string construction; use t-strings **only**
   **when** a processor needs structured interpolation data.
4. keep synchronous work synchronous **unless** related concurrent operations
   create a demonstrated need for structured concurrency.
5. record a compatibility exception **when** an admitted host boundary cannot use
   the selected idiom.

## Outcome

current Python capabilities improve the code for an explicit reason **without**
turning novelty into a requirement **or** obscuring the supported boundary.

## Failure or stop

stop adoption **when** the benefit is unnamed, the simpler idiom is equally clear,
**or** the construct exceeds the selected runtime **or** compatibility boundary.

## Sources

- [PEP 750 — Template Strings](https://peps.python.org/pep-0750/)
- [Python documentation: task groups](https://docs.python.org/3.14/library/asyncio-task.html#task-groups)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-407
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Function Purity"
  depends_on:
    - "Method/Business Logic Authority"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Allocate deterministic transformations to functions

use a side-effect-free function as the default unit of PROGRAMMATIC behavior.
implement one deterministic transformation as a function **when** its result
follows **only** from its declared inputs **and** the responsibility needs no identity
across calls.

## Details

Candidate source: [CA-M-157@12](archive/CA-M-157-PROGRAMMATIC-CORE-METHOD--allocate-deterministic-transformations-to-functions@12.md)

## Applicable when

apply **when** Tools, App backend services, **or** MCP components parse, classify,
validate, plan, project, format, **or** **otherwise** transform explicit input into a
result.

## Procedure

- use a function **unless** the responsibility **must** own mutable state, an
   invariant across calls, a resource, a lifecycle, **or** a replaceable adapter.
- give the function a specific, intention-revealing verb phrase that states
   its one responsibility; prefer clarity over brevity **and** split a function
   whose accurate name requires multiple responsibilities.
- state the function's input, result, **and** failure values explicitly.
- do **not** mutate inputs **or** shared state, perform I/O **or** logging export, **or** read
   the filesystem, process, clock, environment, network, persistence, **or**
   randomness.
- pass **every** required observation **and** setting as explicit input rather than
   obtaining them implicitly.
- group related functions **in** a specifically named module; do **not** create a
   class **only** **to** provide a namespace.

## Outcome

behavior is locally readable, reproducible from declared input, **and** free of
observable side effects. it can be reused, checked, **or** extended **without**
constructing component lifecycle state.

## Failure or stop

stop treating the unit as a deterministic transformation **when** it applies an
external effect. a bounded one-shot effect **may** remain a function under
CA-M-425; allocate an object **only** **when** identity across calls **or** owned state,
invariant, resource, lifecycle, **or** adapter behavior is required.

## Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-408
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/State Ownership"
  depends_on:
    - "Method/Business Logic Authority"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Allocate owned state and lifecycle to objects

introduce an object **only** **when** one PROGRAMMATIC responsibility needs identity
across calls because it owns mutable technical state, preserves an invariant,
manages a resource **or** lifecycle, **or** implements a replaceable adapter. do **not**
create an object merely **to** group functions **or** **to** perform a bounded one-shot
effect.

## Details

Candidate source: [CA-M-158@13](archive/CA-M-158-PROGRAMMATIC-CORE-METHOD--allocate-owned-state-and-lifecycle-to-objects@13.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component **must** retain state,
preserve an invariant across calls, acquire **or** release a resource, transition
through a lifecycle, **or** encapsulate one replaceable technical adapter.

## Procedure

- give the class **or** object a specific, intention-revealing noun phrase that
   states the one state, invariant, resource, lifecycle, **or** adapter
   responsibility it owns; do **not** use an unqualified generic name such as
   `Manager`, `Helper`, **or** `Utils`.
- give **every** effectful method a specific verb phrase that declares the effect
   **or** lifecycle transition it performs.
- keep construction free of I/O **and** start acquisition **or** activation through
   an explicit method.
- make acquisition, use, failure, **and** release **or** recovery boundaries
   explicit.
- keep deterministic transformations outside the object **unless** they require
   its owned responsibility.
- compose the object from explicit collaborators instead of inheriting
   behavior for code reuse.
- use inheritance **only** for one stable, substitutable subtype contract; stop
   **when** a module, function, **or** composed adapter expresses the variation.

## Outcome

**every** object has one clearly named owner responsibility, a visible invariant **or**
lifecycle, explicit collaborators, **and** no unrelated function-grouping role.

## Failure or stop

stop **and** split **or** redesign the object **when** it owns unrelated state **or**
lifecycle concerns, hides an external effect, exists **only** as a namespace **or**
one-shot effect wrapper, **or** uses an ambiguous generic name **or** inheritance
**where** composition provides the same substitution boundary.

## Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [Python documentation: data classes](https://docs.python.org/3.14/library/dataclasses.html)
- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-409
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/External Effect Boundary"
  depends_on:
    - "Method/Effect Authorization"
    - "Method/Effect Boundary"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Bound file and subprocess effects

plan, validate, **and** bound **every** PROGRAMMATIC file mutation **or** subprocess
invocation **before** applying it; make partial failure diagnosable **and** recoverable
**without** guessing.

## Details

Candidate source: [CA-M-161@11](archive/CA-M-161-PROGRAMMATIC-CORE-METHOD--bound-file-and-subprocess-effects@11.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component writes, replaces, **or**
removes a file, **or** invokes a subprocess.

## Procedure

1. validate the target **and** preconditions **before** mutation.
2. write replacement content through a secure temporary carrier on the
   destination filesystem, flush required bytes, **and** use an atomic replacement
   **only** **where** the supported boundary provides that guarantee.
3. invoke a subprocess with an argument array, explicit timeout, checked exit
   status, controlled environment input, **and** shell execution disabled by
   default.
4. return the target, inputs, outcome, **and** partial-failure context needed for
   diagnosis **or** recovery.

## Outcome

**every** applicable effect has a declared precondition, bounded execution
surface, observable result, **and** explicit recovery limit.

## Failure or stop

stop the effect **when** preconditions fail, an atomicity guarantee is unavailable
**and** no weaker recovery boundary is accepted, **or** subprocess completion,
timeout, **and** exit status cannot be observed.

## Sources

- [Python documentation: `tempfile`](https://docs.python.org/3.14/library/tempfile.html)
- [Python documentation: `subprocess`](https://docs.python.org/3.14/library/subprocess.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-410
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Resource Bounds"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
author: Anatoly Maslennikov
---
# Summary

Bound resource use to the workload

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** implement PROGRAMMATIC behavior, account for input size and resource growth, choose bounded or incremental processing and controlled concurrency, and apply appropriate resource budgets to prevent uncontrolled growth and resource exhaustion, including out-of-memory failures.

## Details

Candidate source: [CA-M-386@2](archive/CA-M-386-PROGRAMMATIC-CORE--bound-resource-use-to-the-workload@2.md)

- Use streaming, batching, bounded buffers or bounded work admission where they satisfy the declared behavior.
- Account for aggregate concurrent work, memory, queues, workers, subprocesses and retained state, not only the cost of one operation.
- Concrete limits belong to configuration and implementation; resource-behavior verification and acceptance belong to Evaluation. This Method fixes no product, concurrency count or universal threshold.

The Operator explicitly selected reasonable, bounded resource use to prevent OOM and similar failures on 2026-10-15.


---
atom_id: CA-M-411
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Implementation Cohesion"
  depends_on:
    - "Method/Source Unit Responsibility"
    - "Method/Behavior Ownership"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  derived_from: [CA-M-403]
---
# Summary

Concentrate Requirement and Delivery implementation

## Scope

New or changed PROGRAMMATIC implementation of Requirement (R) and Delivery (D) Atoms, including descendant Scope Units.

## Claim

For each implemented R or D Atom, prefer concentrating its actual claim-specific implementation in one cohesive implementation module and as few code units as practical, ideally one. Preserve complete realization of the Claim and allow justified multi-module exceptions when forced concentration would harm correctness or cohesion. Many-to-many implementation relations remain valid.

## Details

Candidate source: [CA-M-393@1](archive/CA-M-393-PROGRAMMATIC-CORE--concentrate-requirement-and-delivery-implementation@1.md)

- Apply the preference to actual implementation, not merely an owner label, trace link or facade over dispersed logic. Several Atoms may share one module or code unit; several code units within one module may realize one Atom.
- Use code units, such as functions or classes, at the stated implementation granularity; do not confuse them with governed Scope Units.
- For R, concentrate its claim-specific meaning, behavior or enforcement. For D, concentrate its representation, serialization, storage or placement logic. Implementation need not be executable code.
- Distinguish claim-specific realization from callers, dependencies, tests and other evidence. Their presence alone does not add a realizing module; a caller that performs part of the required enforcement does count.
- Preserve complete and truthful implementation relations. Leave unimplemented Atoms without invented implementation targets.
- When multiple modules are necessary, retain the required boundaries and state the concrete reason; do not duplicate logic, inflate a module or omit obligations merely to reduce the count.

This Method is an implementation-organization preference, not an absolute cardinality limit, new approval gate or test policy.



---
atom_id: CA-M-412
content_role: "Method"
type: "Implementation Decision"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Technical Configuration Boundary"
  depends_on:
    - "Method/Authoritative Representation"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
claim_target_scope_unit: "PROGRAMMATIC"
author: "Anatoly Maslennikov"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
---
# Summary

Declare one Python and software configuration boundary

## Scope

apply **when** Python source **or** a development workflow depends on an interpreter,
dependency, formatter, linter, type checker, evaluator, **or** packager setting.

## Claim

select the stable CPython `3.14.*` series **and** require one project-owned
technical configuration boundary for interpreter, formatting, linting, typing,
evaluation, **and** packaging. CA-D-250 owns the current carrier placement **and**
encoding **in** the root `pyproject.toml`; configuration **and** Implementation
materialize this Method's selections there. keep that technical configuration
separate from CAPRMEDIO project settings.

## Details

Candidate source: [CA-M-281@13](archive/CA-M-281-PROGRAMMATIC-GENERAL-IMPLEMENTATION_METHOD--declare-one-python-and-software-configuration-boundary@13.md)

### Procedure
1. resolve the current Delivery carrier, **then** materialize the selected
   interpreter series **and** admitted development-tool profiles through that
   boundary.
2. keep one value for **every** setting **and** make local **and** automated workflows read
   that value rather than reproduce it.
3. change the interpreter series **or** a selected tool profile **only** through its
   accepted Method **before** changing configuration.
4. verify the selected stable series **before** using version-specific behavior.
5. keep runtime project settings outside `pyproject.toml` **and** expose them **only**
   through the shared Settings Reader.

### Outcome

this Method owns one set of Python workflow selections; Delivery owns its
carrier, **and** configuration **and** Implementation reproduce the selections **without**
becoming another methodological authority.

### Failure or stop

stop **when** two carriers disagree, a moving `latest` label replaces the selected
series, the materialization conflicts with its Delivery, **or** technical **and**
CAPRMEDIO project settings are mixed.

### Sources

- [Python 3.14 release notes](https://docs.python.org/3.14/whatsnew/3.14.html)
- [PyPA: `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)
- [CA-A-054 — Validate the Python 3.14 contract upgrade](../02_analysis/CA-A-054-PROGRAMMATIC-ANALYSIS_RPRT--validate-the-python-3-14-contract-upgrade.md)


---
atom_id: CA-M-413
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Interface Design"
  depends_on:
    - "Method/Behavior Ownership"
    - "Method/Compatibility Boundary"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Define typed contracts at replaceable technical boundaries

declare an explicit typed contract wherever a PROGRAMMATIC component depends on
a replaceable technical implementation, adapter, transport, storage mechanism,
**or** host boundary.

## Details

Candidate source: [CA-M-159@9](archive/CA-M-159-PROGRAMMATIC-CORE-METHOD--define-typed-contracts-at-replaceable-technical-boundaries@9.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component can substitute one
technical implementation for another **or** crosses a host-owned interface.

## Procedure

1. define the accepted inputs, outcomes, failure values, ownership boundary,
   **and** compatibility expectation at the interface.
2. keep callers dependent on that contract rather than on implementation-only
   state **or** incidental representation.
3. use a structural `Protocol` **when** consumers need one capability contract
   **without** requiring implementations **to** inherit from a framework base class.
4. keep substrate-specific behavior **in** a small adapter **and** keep deterministic
   semantic decisions outside that adapter.
5. record an exception **in** its bounded owner **when** a required external interface
   cannot meet the contract directly.

## Outcome

the component can replace the bounded technical implementation **without**
silently changing its callers' declared expectations.

## Failure or stop

stop substitution **or** host integration **when** the boundary has no explicit
contract, its failures cannot be represented, **or** compatibility cannot be
identified from current authority.

## Sources

- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
- [Python documentation: `typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-414
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Operational Diagnostics"
  depends_on:
    - "Method/Outcome Evidence"
    - "Entity/Node/Continuant/Atom/Content Role: Operations"
    - "Entity/Carrier"
    - "Entity/Node/Continuant/History/Journal.Record"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Emit structured operational diagnostics

emit structured operational diagnostics for PROGRAMMATIC work under the active
Logging Policy **in** `CAPRMEDIO-GOV-REQU-315`, including its ERROR, WARNING, INFO,
**and** DEBUG meanings. this Method applies that authority **to** PROGRAMMATIC
diagnosis; it does **not** own the level vocabulary, level meanings, **or** Journal
meaning.

## Details

Candidate source: [CA-M-163@15](archive/CA-M-163-PROGRAMMATIC-CORE-METHOD--emit-structured-operational-diagnostics@15.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component reports normal
operation, degraded operation, failure, recovery, **or** diagnostic detail.

## Procedure

1. select ERROR, WARNING, INFO, **or** DEBUG according **to** the active Logging Policy;
   do **not** introduce a fifth shared severity.
   Apply CA-M-396 and CA-M-397 to failure classification: invalid input or Project
   artifacts produce WARNING diagnostics and an explicit request-output error;
   ERROR is reserved for a genuine blocking failure of the runtime itself.
   A refused request or failed business Workflow is not by itself an ERROR-level
   runtime failure. Preserve partial results under CA-M-398, use the shared
   boundary under CA-M-400, and leave business lifecycle recording with CA-M-399.
2. emit records through one project-owned logging abstraction **and** schema.
   include timestamp, level, component, operation, outcome, **and** the canonical
   action **or** event identity **when** one exists.
3. include actionable, contextual, sanitized fields **and** keep DEBUG bounded **to**
   diagnosable need.
4. materialize sink **and** runtime settings **in** configuration **or** Implementation,
   govern carrier placement **and** encoding through Delivery, **and** preserve actual
   execution evidence through Journal Records **and** diagnostic evidence through
   the applicable production-log Carriers. For the selected Docker runtime, write
   structured technical diagnostics to **stderr** for Docker's local logging driver;
   every record carries the validated Project prefix from the existing bound Project
   selection and canonical prefix-field validation, never a guessed path, container,
   process, or caller identity. This uses the selected immutable settings view; it
   adds no settings carrier and makes no claim of full SettingsReader conformance.
   Configure bounded local rotation as `max-size=10m` and `max-file=3`, with Docker
   logging `mode=non-blocking` and `max-buffer-size=1m`; when that buffer is full,
   new technical messages may be dropped so logging cannot stall primary work.
   Docker logs are removed with the container. Do not create a separate local log
   directory or place technical diagnostics in the business Journal. Operations
   defines the reusable behavior; it does **not** make emitted records O Atoms.
5. declare retention, loss, **and** back-pressure behavior at those bounded
   materialization **and** operational boundaries.
6. make logging failure observable **without** silently breaking primary work.

### Technical warnings are not business Journal records

When a bounded scan isolates a schema-invalid Atom and continues with a warning,
emit the warning through the selected Docker `stderr` diagnostic stream with the
validated Project prefix, repository-relative path, and reason, and preserve the
incomplete result (`complete: false`) in the operation response. Do not append that
technical warning as a business Journal event, fabricate a Run to carry it, or
rewrite historical Journal records. Docker local rotation is bounded to
`max-size=10m` and `max-file=3`; non-blocking buffering is bounded to 1 MiB and
may drop new technical messages when full; a logging failure remains observable
without breaking the primary scan.

## Outcome

Operators can diagnose component behavior **without** exposing secrets, confusing
operational diagnostics with governed Journal history, **or** relying on an
undeclared sink behavior.

## Failure or stop

stop emission **or** release of the affected diagnostic path **when** required context
cannot be sanitized, a logging failure is hidden, **or** the component would use
the Journal as a substitute logging sink.

## Sources

- [Python Logging HOWTO](https://docs.python.org/3.14/howto/logging.html)
- [Python Logging Cookbook](https://docs.python.org/3.14/howto/logging-cookbook.html)
- [OpenTelemetry: logs](https://opentelemetry.io/docs/concepts/signals/logs/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-415
content_role: "Method"
type: "Implementation Decision"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Programming Language Selection"
  depends_on:
    - "Method/Technical Configuration Boundary"
    - "Entity/Node/Continuant/History/Journal.Record"
    - "Entity/Node/Continuant/Atom/Content Role: Operations"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
claim_target_scope_unit: "PROGRAMMATIC"
author: "Anatoly Maslennikov"
relations: {"derived_from":["CA-A-053"],"child_of":["CA-M-261"]}
---
# Summary

Implement PROGRAMMATIC components in Python

## Scope

apply **when** a Tool, App backend service, **or** MCP component is added **or** materially
changed, **or** **when** its Python realization, runtime dependency, **or** non-Python
exception is proposed.

## Claim

use Python for applicable PROGRAMMATIC Tools, App backend services, **and** MCP
components. this Method owns the Python technology selection for that bounded
scope. Configuration **and** Implementation materialize the selected runtime,
dependencies, **and** exceptions; Delivery governs their carrier placement **and**
encoding; Operations defines reusable workflow behavior, **and** Journal Records carry execution evidence. this Method
does **not** govern Skills **or** make Python a discipline-independent CAPRMEDIO
meaning.

## Details

Candidate source: [CA-M-110@21](archive/CA-M-110-PROGRAMMATIC-GENERAL-IMPLEMENTATION_METHOD--implement-programmatic-components-in-python@21.md)

### Procedure
1. apply the Python selection established by this Method **and** read its current
   materialization **before** realizing a component.
2. use the standard library **when** it provides the required behavior with
   comparable clarity **and** reliability.
3. add **or** change a runtime, library, workflow tool, **or** non-Python exception
   **only** through an accepted Method that selects it for a bounded scope.
4. materialize **every** accepted selection **in** canonical configuration **and**
   Implementation **without** making either carrier a second authority.
5. place **and** encode **every** materialization through its Delivery, **and** preserve
   evidence of actual execution results **in** Journal Records.

### Outcome

**every** applicable component follows one Method-owned technology selection.
Configuration **and** Implementation reproduce it, Delivery locates its carriers,
**and** the Journal records execution evidence **without** taking over selection authority.

### Failure or stop

stop admission **or** release **when** no accepted Method owns a required selection,
its materialization disagrees with that Method, **or** the Delivery **or** Operations boundary
is absent. do **not** infer a platform-support claim from local execution.

### Sources

- [Python 3.14 documentation](https://docs.python.org/3.14/)
- [Python Packaging User Guide: `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-416
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Performance Measurement"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Measure before optimizing PROGRAMMATIC performance

measure a PROGRAMMATIC performance concern **before** accepting an optimization;
use a representative workload for its Hook, interactive, batch, MCP, App, **or**
background surface rather than treating one surface as universal.

## Details

Candidate source: [CA-M-165@9](archive/CA-M-165-PROGRAMMATIC-CORE-METHOD--measure-before-optimizing-programmatic-performance@9.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component proposes **or** assesses
a performance-sensitive change.

## Procedure

1. profile the applicable surface **to** locate the measured bottleneck, **then**
   select its representative workload.
2. preserve the input, environment, baseline, observed distribution, **and**
   comparison threshold with the measurement.
3. compare the change **to** the recorded baseline **before** accepting the claimed
   improvement.
4. leave numeric budgets **to** a later bounded authority **until** current baselines
   **and** Operator priorities establish them.

## Outcome

an accepted performance claim is tied **to** one reproducible workload **and**
measurement boundary instead of a universal **or** unmeasured optimization claim.

## Failure or stop

stop the performance claim **when** no representative workload, preserved
baseline, **or** comparable observation exists; do **not** invent a numeric budget.

## Sources

- [Python documentation: profilers](https://docs.python.org/3.14/library/profile.html)
- [pyperf documentation](https://pyperf.readthedocs.io/en/latest/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-417
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Configuration Access"
  depends_on:
    - "Method/Project Settings Snapshot"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
author: Anatoly Maslennikov
---
# Summary

Pass validated configuration through one shared boundary

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** implement behavior that depends on Project Settings, resolve and validate the authoritative settings through one shared Reader, then pass an immutable snapshot explicitly to consumers **without** duplicating parsing, inventing fallback values or turning the snapshot into authority.

## Details

Candidate source: [CA-M-389@2](archive/CA-M-389-PROGRAMMATIC-CORE--pass-validated-configuration-through-one-shared-boundary@2.md)

- Keep the Reader read-only; settings changes use the authoritative Artifact's dedicated writer.
- Preserve the actual values and source provenance in the snapshot.
- Keep component-specific interpretation and behavior outside the shared Reader.

Source basis: CA-M-284.


---
atom_id: CA-M-418
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Compatibility Boundary"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Preserve declared interface compatibility boundaries

preserve **or** explicitly replace **every** declared PROGRAMMATIC interface **or** host
compatibility boundary; do **not** infer a broader support claim from
local use, stale workflow configuration, **or** one implementation.

## Details

Candidate source: [CA-M-166@11](archive/CA-M-166-PROGRAMMATIC-CORE-METHOD--preserve-declared-interface-compatibility-boundaries@11.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component changes a declared
technical interface, host integration, transport, **or** dependency-facing
interface boundary.

## Procedure

1. identify the current Requirement, technical contract, **or** pinned external
   origin that declares the affected interface boundary.
2. preserve its declared behavior **or** obtain an accepted bounded replacement
   **before** releasing the change.
3. keep component-specific interface details at the child Scope that owns
   them.
4. **when** no current boundary exists, record the absence rather than claiming
   platform **or** cross-host compatibility.

## Outcome

**every** compatibility claim has one current authority **and** remains limited **to** its
declared interface surface.

## Failure or stop

stop release **or** compatibility claims **when** the affected interface boundary has
no current authority, pinned external origin **where** one is required, **or**
accepted replacement.

## Sources

- [Python documentation: `typing.Protocol`](https://docs.python.org/3.14/library/typing.html#typing.Protocol)
- [Semantic Versioning 2.0.0](https://semver.org/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-419
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Source Unit Responsibility"
  depends_on:
    - "Method/Function Purity"
    - "Method/Source Check Adoption"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Ratchet hand-authored Python source boundaries

**to** construct bounded hand-authored PROGRAMMATIC Python source, decompose code
by responsibility under CA-M-407, CA-M-408, **and** CA-M-425; choose smaller coherent
units **and** external data Carriers; **and** use measurements **to** guide the next
construction choice. CA-E-539 owns source-size, complexity, exception, **and**
ratchet acceptance policy.

## Details

Candidate source: [CA-M-162@15](archive/CA-M-162-PROGRAMMATIC-CORE-METHOD--ratchet-hand-authored-python-source-boundaries@15.md)

## Applicable when

apply **to** **every** new **or** materially changed hand-authored Python file **in** Tools, App
backend services, **or** MCP components. generated Runtime **and** Delivery outputs
are outside this source rule.

## Procedure

1. read the applicable Evaluation policy **and** changed-source measurements.
2. separate independently reusable responsibilities **and** move deterministic
   transformations outside effect **and** lifecycle owners.
3. extract related units into specifically named modules **when** that keeps
   dependencies **and** responsibility visible.
4. externalize large static mappings. use TOML by default, JSON for schemas
   **or** machine interchange, **and** YAML **only when** its distinct features are required.
5. submit the resulting source **and** any bounded exception rationale **to** the
   applicable Evaluation. use its result **to** choose the next decomposition.

## Outcome

changed source ratchets toward readable, bounded units **and** externalized static
data. construction choices remain traceable **to** responsibility boundaries
**and** the measurements supplied **to** CA-E-539.

## Failure or stop

return unresolved construction choices **when** the applicable Evaluation policy
**or** required measurement is unavailable. retain a separate responsibility **and**
needed recovery boundary **when** a proposed decomposition would obscure either.
acceptance **and** rejection follow CA-E-539.

## Sources

- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)
- [Python documentation: `json`](https://docs.python.org/3.14/library/json.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-420
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Source Check Adoption"
  depends_on:
    - "Method/Outcome Evidence"
    - "Entity/Node/Continuant/History/Journal.Record"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Ratchet typing and automation adoption

advance PROGRAMMATIC typing **and** automation through bounded target selection,
explicit tool configuration, **and** deliberate expansion. Evaluation authority
owns acceptance profiles **and** regression policy under CA-E-539, CA-E-540,
**and** the applicable behavioral Evaluation.

## Details

Candidate source: [CA-M-164@13](archive/CA-M-164-PROGRAMMATIC-CORE-METHOD--ratchet-typing-and-automation-adoption@13.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component adds **or** materially
changes source that falls within an admitted typing, formatting, linting, **or**
behavioral-check capability.

## Procedure

1. resolve **every** selected typing, formatting, linting, **or** behavioral-check
   capability from its accepted Method owner.
2. read its current tool, version, profile, **and** bounded target materialization
   from canonical configuration **or** Implementation; read carrier placement **and**
   encoding from Delivery.
3. keep formatting, linting, typing, **and** behavioral evidence distinct.
4. provide changed **or** new target evidence **and** its current admitted baseline
   **to** the applicable Evaluation for its regression decision.
5. expand **or** replace a selected capability **only** through a Method change;
   materialize that change separately **and** preserve evidence of actual runs **in** Journal Records.

## Outcome

automation **and** typing improve monotonically at an admitted surface **without**
turning an unselected tool, version, **or** strictness level into shared authority.

## Failure or stop

return unresolved selection **when** no accepted Method owns the tool choice **or**
the bounded materialization is unavailable. Evaluation authority determines
whether the supplied baseline **and** execution evidence admit the claimed ratchet.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Mypy: using Mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-421
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Established Solution Reuse"
  depends_on:
    - "Method/Necessity"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
author: Anatoly Maslennikov
---
# Summary

Reuse suitable established solutions

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** implement declared PROGRAMMATIC behavior, prefer well-adopted, well-suited existing libraries, approaches and tools over reimplementing their mechanics; use custom mechanics **when** existing solutions cannot meet a declared requirement **or** the custom choice provides a concrete benefit.

## Details

Candidate source: [CA-M-391@2](archive/CA-M-391-PROGRAMMATIC-CORE--reuse-suitable-established-solutions@2.md)

- Check existing Project capabilities and established solutions for actual fit, not popularity alone.
- Consider the complexity and dependency cost introduced by the choice.
- Keep custom work limited to the unmet requirement or demonstrated benefit. This Method selects no mandatory product or technology.

The Operator explicitly selected reuse of well-adopted and suitable libraries, approaches and tools instead of reinventing the wheel on 2026-10-15.


---
atom_id: CA-M-422
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Temporary State Placement"
  depends_on:
    - "Method/External Effect Boundary"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: cce_1
cce_form: method
llm_session_ids:
  - codex:01a0263a-7510-7672-bce4-58830bc4d184
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1473
---
# Summary

Route all temporary Carriers through project temp

resolve the configured Project Temporary State root **before** a PROGRAMMATIC
component creates a temporary Carrier **or** invokes a dependency that can create
one. allocate a component-owned **and**, **when** concurrency is possible, run-specific
descendant below `.caprmedio_tmp/`. pass that descendant explicitly **to**
temporary-file APIs **and** configure dependency cache, temporary, staging, build,
**and** Evaluation paths **before** invocation. materialize shared development-tool
cache paths through the root `pyproject.toml`; provide explicit run-specific
paths through launch Carriers for dependencies that do **not** read that file.
do **not** rely on an ambient host
temporary directory **or** the process working directory.

route Python bytecode cache output **to** `.caprmedio_tmp/cache/python/` **before**
importing Project modules, **or** disable bytecode writes for an isolated process.
do **not** create `__pycache__/` **or** `.pyc` Carriers below `.caprmedio_runtime/`.

for an atomic replacement, create its staging Carrier below the Project
Temporary State root **and** verify that the staging **and** destination Carriers satisfy the
required same-filesystem atomicity boundary **before** the first mutation. stop
**without** falling back **to** a destination sibling **or** host temporary location **when**
that precondition is false.

attempt bounded cleanup **when** the owning operation ends. treat interrupted **or**
denied cleanup as retained non-authoritative temporary state, report its owned
path, **and** leave it confined below `.caprmedio_tmp/`. never weaken placement
because cleanup is best-effort.

keep executable releases, shared implementation libraries, registries, stable
launchers, Hook Carriers, runtime logs, sessions, databases, service state,
resumable state, **and** governed Artifacts outside the Temporary State root **in**
their applicable authority **or** runtime places.

## Details

Candidate source: [CA-M-289@9](archive/CA-M-289-PROGRAMMATIC-CORE-METHOD--route-all-temporary-carriers-through-project-temp@9.md)


---
atom_id: CA-M-423
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Isolated Python Execution"
  depends_on:
    - "Method/Python Environment Frontend"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
author: Anatoly Maslennikov
---
# Summary

run Project Python **only** in uv-managed isolated environments

## Scope

the interpreter and library environment used to execute, develop, evaluate, build, package, or otherwise run Project Python source.

## Claim

Project Python **must** execute **only** through a uv-managed isolated environment **and** **must not** use naked **or** system Python, **or** system-installed libraries.

## Details

Candidate source: [CA-M-358@2](archive/CA-M-358-PROGRAMMATIC-GENERAL--run-project-python-only-in-uv-managed-isolated-environments@2.md)

1. resolve the Project interpreter through `uv python` **and** materialize its declared dependencies through the Project `pyproject.toml` **and** `uv.lock`.
2. synchronize the isolated environment with `uv sync --locked` **before** governed execution **and** start Project Python with `uv run --locked` **or** another uv command that selects that same isolated environment. Child processes **may** reuse **only** the selected environment's interpreter.
3. reject unselected `python`, `python3`, `pip`, **or** `pip3` commands, `PYTHONPATH` injection, user-site packages, system site packages, **and** library resolution outside the uv-managed Project environment.
4. apply the same isolated-environment boundary to development, tests, host launchers, **and** installed Project Tools. Non-Python executables **and** installing uv itself do **not** create a system-Python fallback for Project source.
5. stop **when** uv cannot resolve the declared interpreter **or** locked environment. Do **not** substitute a system interpreter, ambient virtual environment, **or** globally installed library.

## Outcome

Project Python execution has one reproducible uv-managed interpreter and dependency boundary.

## Failure or stop

stop before execution when the command would use an ambient interpreter, an unlocked environment, or any system-installed Project library.


---
atom_id: CA-M-424
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Evaluation Technique Selection"
  depends_on:
    - "Method/Specification Sufficiency"
    - "Entity/Node/Continuant/Actor"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  derived_from:
    - CA-A-053
  child_of:
    - CA-M-415
---
# Summary

Select software Evaluation techniques by failure mode

## Scope

selection of behavioral software Evaluation techniques for PROGRAMMATIC components.

## Claim

**to** select behavioral software Evaluation techniques for a PROGRAMMATIC component, the Actor selecting the portfolio **must** take the applicable Spec, declared failure predicates, **and** active Evaluation authority as inputs; identify candidate checks for **every** predicate; evaluate candidate portfolios against the applicable Core **and** General Evaluation policy **and** each selected technique's own acceptance **and** disposition rules; select one admitted portfolio; repeat **until** all predicates are covered **or** no candidate remains; produce the selected Evaluation identities **and** selection rationale; **and** return unresolved predicates for authority **or** design clarification **when** no portfolio is admitted.

## Details

Candidate source: [CA-M-285@14](archive/CA-M-285-PROGRAMMATIC--select-software-evaluation-techniques-by-failure-mode@14.md)

1. enumerate the failure predicates established by applicable authority **and** bind each predicate **to** the observable behavior that can distinguish acceptance from rejection.
2. identify applicable Evaluation Atoms across test scopes, purposes, boundary-realism choices, execution environments, **and** release stages **without** treating those labels as a universal ranking.
3. construct candidate portfolios from those Evaluation Atoms. include a specialized technique **only when** its Evaluation applicability **and** evidence preconditions are satisfied.
4. evaluate **every** candidate portfolio under the Core evidence invariant in CA-E-637, the General portfolio criteria in CA-E-389, **and** the acceptance **and** disposition rules of **every** selected Evaluation Atom. apply the Core exposure invariant in CA-E-638 **and** the General canary criteria in CA-E-536 **when** a candidate includes canary evidence.
5. stop with one traceable admitted portfolio **when** all predicates are covered. **when** no candidate passes, return the uncovered predicates, failed policy conditions, **and** missing evidence rather than inventing a test-count ratio **or** silently accepting incomplete coverage.

## Sources

- [CA-E-389-PROGRAMMATIC-GENERAL-EVAL_APPROACH--combine-complementary-software-behavior-evidence](../06_evaluation/CA-E-389-PROGRAMMATIC-GENERAL-EVAL_APPROACH--combine-complementary-software-behavior-evidence.md)
- [CA-E-536-PROGRAMMATIC-GENERAL-EVAL_APPROACH--admit-safe-canary-evaluation](../06_evaluation/CA-E-536-PROGRAMMATIC-GENERAL-EVAL_APPROACH--admit-safe-canary-evaluation.md)
- [CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)

- [CA-E-637 — Require observable evidence for behavioral acceptance](../06_evaluation/CA-E-637-PROGRAMMATIC-CORE-EVAL_APPROACH--require-observable-evidence-for-behavioral-acceptance.md)
- [CA-E-638 — Bound and recover canary exposure](../06_evaluation/CA-E-638-PROGRAMMATIC-CORE-EVAL_APPROACH--bound-and-recover-canary-exposure.md)


---
atom_id: CA-M-425
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Effect Boundary"
  depends_on:
    - "Method/Function Purity"
    - "Method/State Ownership"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Separate deterministic transformations from effects and lifecycle

keep PROGRAMMATIC decisions **in** a function-based deterministic core. apply
filesystem, process, clock, environment, network, persistence, **or**
logging-export effects through a specifically named bounded one-shot function
**when** no identity **or** ownership is required, **or** through a specifically named
method on an object that owns state, an invariant, a resource, a lifecycle, **or**
a replaceable adapter.

## Details

Candidate source: [CA-M-160@12](archive/CA-M-160-PROGRAMMATIC-CORE-METHOD--separate-deterministic-transformations-from-effects-and-lifecycle@12.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component combines a decision
with an external effect, asynchronous work, **or** lifecycle transition.

## Procedure

1. form the decision, target, ordering, **and** expected outcome with deterministic
   functions from explicit observations **before** applying an effect.
2. pass the resulting plan **to** one bounded effect boundary.
3. use a function for a one-shot effect **only** **when** its complete target,
   dependency, input, outcome, **and** failure boundary are explicit **and** it owns
   no identity across calls, state, invariant, resource, lifecycle, **or** adapter.
4. use a specifically named object method **when** the effect **must** own **any** of those
   responsibilities across calls.
5. return typed observations **or** completion facts **to** the decision boundary;
   do **not** let the effect owner invent, reorder, **or** suppress a decision.

## Outcome

decision logic is locally readable **and** replayable. **every** effect has a visible,
bounded function **or** object owner, ordered input, **and** recoverable result
boundary. objects exist **only** **where** persistent identity **or** ownership requires
them.

## Failure or stop

stop execution **when** the plan is incomplete, an effect owner would make a new
business decision, a one-shot effect hides a dependency **or** exceeds its declared
boundary, an object exists **without** owned identity **or** ownership, **or** the effect
boundary cannot report a typed result.

## Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [Python documentation: data classes](https://docs.python.org/3.14/library/dataclasses.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-426
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Pure Computation and Recording Boundary"
  depends_on:
    - "Method/Effect Boundary"
    - "Method/Outcome Evidence"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
author: Anatoly Maslennikov
---
# Summary

Separate pure computation from effects and recording

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

## Claim

**To** construct a result, keep pure computation independent of persistence and Run or Journal writes, leaving those effects with their declared execution owners.

## Details

Candidate source: [CA-M-392@2](archive/CA-M-392-PROGRAMMATIC-CORE--separate-pure-computation-from-effects-and-recording@2.md)

- Construct from bound inputs and return results and diagnostics without hidden writes.
- Persist an output only through its applicable authorized effect boundary.
- Actual execution recording remains with its declared executor; generated output alone does not establish durable terminal completion.

Source basis: CA-M-330, CA-M-259.


---
atom_id: CA-M-427
content_role: "Method"
type: "Implementation Decision"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Python Type Checks"
  depends_on:
    - "Method/Isolated Python Execution"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Use Mypy for static Python type checking

use Mypy as the selected static type checker for hand-authored PROGRAMMATIC
Python source. CA-E-540 owns strict-profile, baseline, **and** suppression
acceptance policy.

## Details

Candidate source: [CA-M-283@9](archive/CA-M-283-PROGRAMMATIC-CORE-METHOD--use-mypy-for-static-python-type-checking@9.md)

## Applicable when

apply **to** new **or** materially changed Python source within Tools, App, **or** MCP.

## Procedure

1. materialize one pinned Mypy profile **and** bounded target set **in**
   `pyproject.toml`.
2. run Mypy through the selected uv workflow.
3. provide the current diagnostics **and** recorded baseline **to** CA-E-540.
4. bind suppression rationale **to** the affected line **or** symbol for evaluation
   under CA-E-540.
5. keep static typing evidence distinct from runtime validation **and** behavioral
   evidence.

## Outcome

changed Python interfaces become more explicit **without** making untyped legacy
source an unrelated whole-project blocker.

## Failure or stop

return unavailable configuration **when** the profile **or** target set is absent.
typing acceptance, baseline regression, **and** suppression disposition follow
CA-E-540.

## Sources

- [Mypy documentation](https://mypy.readthedocs.io/en/stable/)
- [Mypy: using Mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [Mypy: strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-428
content_role: "Method"
type: "Implementation Decision"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Python Style Checks"
  depends_on:
    - "Method/Isolated Python Execution"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Use Ruff for Python formatting, linting, and complexity

use Ruff as the selected formatter **and** linter for hand-authored PROGRAMMATIC
Python source, including cyclomatic-complexity lint for changed executable
units.

## Details

Candidate source: [CA-M-282@9](archive/CA-M-282-PROGRAMMATIC-CORE-METHOD--use-ruff-for-python-formatting-linting-and-complexity@9.md)

## Applicable when

apply **to** new **or** materially changed Python source within Tools, App, **or** MCP.

## Procedure

1. materialize one pinned Ruff profile **in** `pyproject.toml`.
2. run Ruff formatting **and** linting through the selected uv workflow.
3. enable the Ruff `C901` rule **and** materialize the applicable Evaluation-owned
   complexity maximum under CA-E-539.
4. provide rule diagnostics, measured values, **and** exception rationale **to**
   CA-E-539 for its acceptance **and** disposition decision.
5. keep Ruff evidence distinct from typing **and** behavioral evidence.

## Outcome

mechanical style, lint, **and** cyclomatic-complexity checks use one reproducible
Method-owned selection **and** one materialized profile.

## Failure or stop

return unavailable configuration **when** Ruff is unpinned **or** the current profile
is absent. changed-source acceptance **and** exception admission follow CA-E-539.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Ruff: configuration](https://docs.astral.sh/ruff/configuration/)
- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-429
content_role: "Method"
type: "Implementation Decision"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Python Environment Frontend"
  depends_on:
    - "Method/Technical Configuration Boundary"
    - "Entity/Node/Continuant/History/Journal.Record"
    - "Entity/Node/Continuant/Atom/Content Role: Operations"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Use uv as the default Python workflow frontend

use uv as the default frontend for **every** admitted Python workflow capability
that uv provides. this Method owns that tool selection; configuration **and**
Implementation materialize it, Delivery governs its carriers, Operations defines reusable workflow behavior,
**and** Journal Records carry evidence of actual workflow execution.

## Details

Candidate source: [CA-M-221@15](archive/CA-M-221-PROGRAMMATIC-CORE-METHOD--use-uv-as-the-default-python-workflow-frontend@15.md)

## Applicable when

apply **when** developing, evaluating, building, packaging, **or** executing
PROGRAMMATIC Python source, including installed Project Tools **and** host launchers.

## Procedure

1. resolve the supported Python boundary from its accepted Method **and** canonical
   Project technical-configuration materialization, **then** install **or** select it
   through `uv python`.
2. materialize dependencies selected by accepted Methods **in** `pyproject.toml`;
   change them through `uv add` **or** `uv remove` so the declaration **and** `uv.lock`
   change together.
3. reproduce the project environment with `uv sync --locked` **and** execute
   governed Python commands with `uv run --locked`.
4. run an isolated Python CLI through `uv tool run` **only** with a pinned tool
   version **and** command **when** it is **not** an admitted project dependency.
   unpinned ephemeral execution cannot supply acceptance evidence.
5. use `uv build` **or** `uv publish` **only** **when** an accepted Delivery authorizes a
   package **or** publication target.
6. do **not** mix pip, venv, virtualenv, pipx, Poetry, Conda, a naked/system
   Python interpreter, system-installed libraries, **or** another overlapping
   Python workflow manager into the governed Project-Python path. A capability
   gap or external boundary does not authorize a non-uv fallback for Project Python.
7. stop rather than record a non-uv fallback exception for Project Python.
8. apply CA-M-423's uv-managed environment boundary to installed Tools **and**
   host launchers as well as development commands. Packaged runtimes retain
   their selected isolated environment **and** locked dependencies; child
   processes reuse **only** that environment's interpreter. Route uv cache,
   build, **and** staging state into `.caprmedio_tmp/`.

## Outcome

one declared Python boundary **and** one reviewed lockfile reproduce the admitted
Python environment **and** commands **without** an undeclared manager **or** dependency
source.

## Failure or stop

stop **when** the supported interpreter cannot be resolved, the lockfile is stale,
a command would update the environment implicitly during evidence collection,
or a Project-Python command would use a non-uv, naked/system, or system-library
fallback.

## Sources

- [uv: Features](https://docs.astral.sh/uv/getting-started/features/)
- [uv: Installing and managing Python](https://docs.astral.sh/uv/guides/install-python/)
- [uv: Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/)
- [uv: Tools](https://docs.astral.sh/uv/concepts/tools/)
- [uv: Configuring projects](https://docs.astral.sh/uv/concepts/projects/config/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)


---
atom_id: CA-M-430
content_role: "Method"
type: "Implementation Decision"
current_scope_unit: "PROGRAMMATIC"
local_tier: "Standard"
global_tier: 8
status: Active
subjects:
  governs: "Method/Structured Input Validation"
  depends_on:
    - "Method/Interface Design"
version: 1
updated_at: "2026-10-21T23:29:13+00:00"
cce_version: "cce_1"
cce_form: "method"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Validate untrusted structured data with Pydantic

use Pydantic **when** untrusted structured data crosses an admitted Python
boundary. validate once at the boundary **and** pass accepted typed values into
the deterministic core **without** making Pydantic the universal internal model.

## Details

Candidate source: [CA-M-286@8](archive/CA-M-286-PROGRAMMATIC-CORE-METHOD--validate-untrusted-structured-data-with-pydantic@8.md)

## Applicable when

apply **to** an admitted CLI payload, Hook event, configuration carrier, Journal
record, protocol message, **or** external adapter whose invalid structure could
hide a contract defect.

## Procedure

1. define the bounded input model with field types **and** constraints **before**
   custom validators.
2. use strict validation **when** coercion could hide a defect; admit lax conversion
   **only** for a declared interoperability need **and** make it observable.
3. reject undeclared extra fields for closed machine contracts.
4. return structured validation diagnostics **and** pass the accepted typed value
   **to** the deterministic core.
5. add Pydantic as a runtime dependency **only** **where** validation **and** schema value
   justify its dependency cost.

## Outcome

untrusted structured inputs become explicit typed values at one boundary while
the internal model remains independent of the validation library.

## Failure or stop

stop admission **when** the boundary is **not** declared, coercion is silent, extra
fields escape a closed contract, **or** the dependency has no bounded benefit.

## Sources

- [Pydantic: models](https://docs.pydantic.dev/latest/concepts/models/)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [Pydantic: model configuration](https://docs.pydantic.dev/latest/concepts/config/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
