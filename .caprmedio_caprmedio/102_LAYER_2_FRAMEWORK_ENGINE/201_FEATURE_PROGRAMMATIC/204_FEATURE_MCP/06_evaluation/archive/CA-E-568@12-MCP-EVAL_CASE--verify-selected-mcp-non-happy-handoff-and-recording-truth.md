---
atom_id: CA-E-568@12
content_role: Evaluation
type: Eval Case
current_scope_unit: MCP
claim_target_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/MCP.selected Workflow non-happy truth
  depends_on:
  - Subject/Graph Node/Engineering/MCP
  - Subject/Graph Node/Engineering/Continuant/Tool
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Occurrent/Execution/Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  evaluation_for:
  - CA-R-1847
  - CA-R-1848
tier: 4
---
# Summary

Verify selected MCP non-happy, handoff, and recording truth

## Scope

Functional MCP failures for unauthorized execute, incomplete or stale binding manifests, deferred/handoff, cancellation, partial/unknown effects, and truthful plain-Journal logging failure.

Verify that host/gateway start or recreation reads the changed blacklist and that implementation-only reload retains the existing Settings snapshot. Refusal disables callable admission without erasing source Atoms, retained code or read-only analysis.

## Claim

Every realization **must** preserve the shared service's actual non-happy evidence and must never replay work because logging fails or recorded rows repeat.

## Details

Verify `project_mcp.tool_blacklist` with an absent/empty list and exact listed tool names. A blocked tool is absent from discovery and direct or cached invocation refuses before any handler call or effect. This Project blocks `release_version` and `public.release`; retain their implementation and binding contracts for later reuse, with normal selected capabilities unaffected. Verify release runner behavior through repository-host invocation, without using the blacklist as an exception to release verification or permission checks.

For non-Release selected routes, using a functional fixture, submit unauthorized mutation `execute`, unsupported
`apply`, unsealed/unknown route, missing route binding, altered manifest digest,
stale original-source or query-admission pin, stale source/frontier, malformed
parent lineage, and absent worker cases. For both query routes submit a secret
selection, a mutation parameter, and each malformed/ambiguous/nonliteral
CA-R-1850 filter case. Also submit a
`source_freshness.definition_manifest_ref` or `.definition_manifest_digest`
shadow field both equal to and different from the outer canonical
`definition_manifest` digest. Each returns blocked/rejected/deferred as
applicable, performs no unapproved mutation or autostart, and creates no
invented Run, Action Run, Event, or effect for an unstarted call. Simulate
handoff-required, cancellation, failed, partial-effect, unknown-effect, and
no-op outcomes from shared support; assert the MCP result retains the exact
outcome, safe refs, and diagnostics without a success conversion or fabricated
effect.

For the current source-bound `run_implementation_workflow` O016 Version 18 Integrated binding, assert that the pending prompt plus complete bound inputs, result contract and opaque continuation do not claim completion. Exercise wrong operation, run/action/continuation identity, malformed result, caller policy override, stale continuation, exact duplicate, conflicting duplicate and oversized submission: exact duplicates return the original response, every other invalid/conflicting case refuses without replay, and no effects are recovered automatically. Read-only `status` strips `capture.definitions`, exposes actual retained recording diagnostics and never recovers or replays work.

For `find_and_fetch_journal_events`, retain the pre-dispatch sealed source
prefix, then attempt source-member mutation, truncation, deletion, unreadable
member bytes, stale continuation and self-Run/Event inclusion. Read repeated
IDs, absent/nonstring IDs, lists, scalars and ordinary duplicate-key JSON
without a Journal-row validation gate or changing the decoded data. Each retained
member failure is rejected with its diagnostic; later append strictly outside the
prefix remains allowed; the query's own Event cannot enter or enlarge the
result, and no logging retry or recovery route is introduced. Assert a preview has no Run/Event and an admitted
actual query records only actual outcomes through shared support after snapshot
capture, never by replay.

For an intentional source-blocked terminal, assert the exact public wrapper and canonical Run outcome: `disposition=terminal`, `status=interrupted_pending`, `outcome=interrupted_pending`, `graph_result.outcome=interrupted_pending`, and actual underlying `run_disposition=interrupted`; a later read-only status matches that outcome and retains diagnostics. With no checkpoint, assert read-only observation is `not_observed` with the requested Run ID only and no fabricated actual root/Run start, prompt or recovery. An unknown root or child interruption without bound canonical graph proof stays `interrupted_pending` with no prompt, while tampered or missing graph references refuse. Do not auto-recover or replay. This terminal assertion is MCP boundary QA; CA-E-652 owns the Workflow algorithm, and Journal completeness remains no permission gate. O016 Version 17 remains the legacy projection and DBOS/queue dispatch path; Version 18 is the observed current admission, not a timeless `>=18` rule, and a future Version requires fresh compatible admission.

Simulate an Action with independently observed completed source effects and a plain Journal append I/O failure. Retain its actual Action/Run outcome, safe effect/result references and ordinary logging diagnostic without turning logging into permission, completion proof, a pending ledger or a retry/recovery gate. Repeated plain log rows never create another actual Run or invoke an Action/Workflow. Verify the obsolete `recover_selected_run_recording` route is not exposed; no replacement recording-retry route or automatic effect replay is introduced. Genuine unknown source effects remain unknown and require their independently governed inspection, not a successful log append.

For the two direct Release commands, verify the closed connected-Project requests and explicit public draft, full-suite failure/unavailability/unknown-result stop before local delivery or public publication, including required integration tests. Missing Docker or another required test environment and skipped required tests must stop release, not produce a passing result. Required Docker integration tests build a disposable image from the current code; an old installed or running image is not a substitute, and test execution does not restart the running Project MCP. Verify there is no separate Active Atom metadata, placement or relation validation step. Retain truthful source-effect results independently of logging failure. Do not require a separate whole-catalog/dependency registry gate, old D527 selected execute envelope, DBOS dispatch or candidate/N+1 pipeline for release. Retain normal permissions, safe owned paths, installation locking/readback and public Git/PR boundaries; other selected routes keep their existing complete admission checks.

Acceptance retains request traces, target mutation traces, service invocation count, actual supplied log data and logging diagnostics, and independently observed output/result/effect references. This is planned functional proof, not a runtime pass.

### Sources

- CA-R-1847 v10; CA-R-1848 v6; CA-D-547 v7; CA-A-1142 v2; CA-P-1618 v1; CA-P-1535 v2; CA-D-527 v3; CA-R-1850 v2; CA-R-1866 v3; CA-R-1867 v1.
- Current CA-O-016 Project Configuration Workflow (observed Version 18), CA-R-1527 Core Meta Model General, CA-R-1845 and CA-D-544 supply the Integrated prompt/continuation contract; CA-E-652 remains Workflow-level algorithm/evaluation authority, not an MCP admission gate.
