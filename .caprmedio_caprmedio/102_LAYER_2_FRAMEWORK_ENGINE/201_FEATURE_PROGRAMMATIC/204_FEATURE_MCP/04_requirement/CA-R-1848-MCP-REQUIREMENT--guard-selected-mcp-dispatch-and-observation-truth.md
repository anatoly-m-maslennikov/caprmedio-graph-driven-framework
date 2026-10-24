---
atom_id: CA-R-1848
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-24 03:32:45 +0400
subjects:
  governs: Subject/Engineering/MCP.selected Workflow dispatch truth
  depends_on:
  - Subject/Engineering/MCP
  - Subject/Engineering/Tool
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Occurrent/Execution/Run
  - Subject/Domain/Node/Continuant/History/Journal
relations: {}
type: Rule
tier: 3
---
# Summary

Guard selected MCP dispatch and observation truth

## Scope

Authorization, currentness, result truth, and defer/handoff behavior at the selected MCP boundary.

## Claim

MCP **must not** invent dispatch, completion, effects or logging success. Each reported fact must retain the actual shared-service **or** direct-runner result and its truthful diagnostics; a Journal entry is not permission or proof of source-effect completion.

## Details

`project_mcp.tool_blacklist` is an optional list of exact MCP tool names; an absent list means no names are blocked. A listed name is omitted from tool discovery and refused at invocation before its handler runs, including cached or direct calls. This Project lists `release_version` and `public.release`: their existing adapters, runner bindings and request contracts remain available in source for later reuse, but neither tool is exposed or callable through MCP. A blacklist refusal creates no release Run, delivery, publication or logging effect. The direct-runner contract below remains preserved for reuse and repository-host invocation; it grants no MCP exposure exception.

The complete manifest/source/permission gate remains required for non-Release selected routes and their query admissions. The two direct local/public Release commands instead use CA-D-547's simple connected-Project runner interface and full test suite, without an additional whole-catalog, dependency-registry, Release-source-admission, D527 selected-envelope or DBOS gate. Normal explicit inputs, existing Operator/client permissions, current source/file safety, actual Run outcomes, installation lock/readback and public Git/PR boundaries remain required. Full-suite verification includes required integration tests; missing Docker or another required test environment, or skipping required tests, cannot pass release. Release verification adds no separate Active Atom metadata, placement or relation validation; the full test suite and normal input, permission and file/path safety checks remain. Required Docker integration tests build a disposable image from the current code; an old installed or running image is not a substitute, and test execution does not restart the running Project MCP. A source-defined condition or a log entry does not prove tests or effects ran. This clause supplies no new execution, confirmation, retry or publication authority.

Before a non-Release selected preview or execute, the adapter validates that route against
exactly one outer `definition_manifest` reference/digest, its canonical binding,
exact admitted source/definition revisions, root/frontier and target/reference
digests, input schema, and parent lineage. Resolve current CA-A-1142 registry authority and current CA-P-1618/CA-P-1535 query admission carriers by identity and safe declared authoritative location under CA-R-1847. Read and validate their current supported contracts, capturing actual Version/hash evidence per operation rather than requiring compiled historical tuples. Preserve historical proof carriers without treating their old accepted tuples as current-rule gates. The source-freshness
object may carry only its selected-source registry/binding evidence: any
`definition_manifest_ref`, `definition_manifest_digest`, or other
duplicate/shadow manifest field there or anywhere else is an unknown field and
is rejected before comparison, including a matching or different digest.
Missing, incomplete, duplicate, malformed, digest-mismatched, changed, stale,
conflicted, unsupported, unsealed, or unauthorized bindings return `blocked` or
`rejected` without dispatch, Run, Action Run, worker start, effect, or Journal
event. Preview creates no Run, Action Run, Event, mutation authority, or Journal
write. A mutation-capable `execute` without exact current Operator authorization
returns `blocked`; an admitted read-only query `execute` requires its exact
current query-source admission and never substitutes mutation authority. The
adapter must not silently substitute a changed revision into an already approved
request, widen a selected set, infer authority from a prior request, or accept an
`apply` mode. A fresh operation resolves and validates current rules; a changed
captured source before dispatch refuses that operation rather than silently
refreshing its target, intent or authorization evidence.

The only additional connected-session admission is the current source-bound
`run_implementation_workflow` binding to the Project Configuration Workflow
CA-O-016 at observed Version 18, limited to its eight Integrated Steps and
CA-O-231 entry after the same manifest/currentness/permission checks. Its
pending response exposes the current Step prompt, complete bound inputs,
expected result contract and opaque one-use continuation; the prompt is not
completion. The controlling session may perform or delegate the Step, then
submits through the same route with the closed `submit_result` packet:
`operation=submit_result`, `run_id`, `action_run_id`, `continuation_id`, and
`result={result, outputs, evidence, blockers}`. The server owns admission,
validation and digest/policy binding: exact duplicates return the original
response, while conflicting, stale or oversized submissions refuse without
replay, and caller policy overrides are not accepted. Read-only `status`
strips `capture.definitions`, exposes actual retained recording diagnostics,
and never recovers or replays work. With no checkpoint, read-only observation returns `not_observed` with the requested Run ID only; it never fabricates an actual root/Run start, prompt or recovery. A known graph-blocked terminal must retain
the exact public wrapper and canonical Run outcome: `disposition=terminal`,
`status=interrupted_pending`, `outcome=interrupted_pending`,
`graph_result.outcome=interrupted_pending`, and actual
`run_disposition=interrupted`. An unknown root or child interruption without
bound canonical graph proof remains `interrupted_pending` with no prompt;
tampered or missing graph references refuse. O016 Version 17 remains the
legacy projection and DBOS/queue dispatch path; Version 18 is the
observed current admission, not a timeless `>=18` rule, and a future Version
requires fresh current compatible admission. This source contract adds no
projection compilation gate and does not make Journal completeness a
permission condition. The existing Subject-only connected-process exception
and all other legacy/Isolated routes retain their separate unchanged
boundaries.

For `find_and_fetch_journal_events`, capture the source Journal byte-prefix and
bind CA-O-163's snapshot token before any Workflow/Action-start recording or
Action dispatch. Only the sealed prefix can be queried; later Run/Event records
are outside it. Both query routes accept only CA-R-1850's shared closed literal
grammar, safe selected fetches, and no credential/secret selection. They do not
create a new parser, Journal writer, or read-only-to-mutation conversion.

The existing shared service or direct runner owns its actual execution, cancellation and source-effect outcome. MCP preserves a deferred, handoff-required, failed, canceled, partial-effect, unknown-effect or no-op result without converting it into success. A no-op has no invented mutation; a handoff has its actual continuation/reference and no claimed local dispatch; an unstarted call has no invented Action Run. Plain Journal append/read has no prior-history, chain, validation, receipt, deduplication, retry or recovery prerequisite. Preserve actual logging I/O diagnostics independently of the observed Run/source-effect result; do not downgrade a completed source effect solely because logging fails, claim an unobserved append, or replay work because a log row is absent or repeated. Source-effect uncertainty and no-effect-replay safeguards remain unchanged.

Observation results disclose only references and redacted safe material authorized by the selected Run; they never fabricate output/results, reveal secrets, or treat an outbox/intake acknowledgement as proof of an effect or successful Journal append. The adapter reports the source currentness observed for the operation and actual safe Run, result/effect/report references and logging diagnostics returned by the service or runner. It is a projection boundary, not an authority to alter source, Artifact, or Journal history.

### Sources

- Current CA-A-1142 selected registry and current CA-P-1618/CA-P-1535 query admission carriers.
- CA-D-527 v3; CA-D-521 v7; CA-R-1720 v19; CA-R-1525 v7; CA-R-1728 v16; CA-D-523 v2; CA-R-1850 v2; CA-R-1866 v3; CA-R-1867 v1.
- Current CA-O-016 Project Configuration Workflow (observed Version 18), CA-R-1527 Core Meta Model General, CA-R-1845 and CA-D-544 supply the Integrated prompt/continuation contract; CA-E-652 remains Workflow-level algorithm/evaluation authority, not an MCP admission gate.
