---
atom_id: CA-E-568@6
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-15 00:35:00 +0000"
subjects:
  governs: "MCP/selected Workflow non-happy truth"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal]
relations:
  evaluation_for: [CA-R-1847, CA-R-1848]
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

Simulate an Action with independently observed completed source effects and a plain Journal append I/O failure. Retain its actual Action/Run outcome, safe effect/result references and ordinary logging diagnostic without turning logging into permission, completion proof, a pending ledger or a retry/recovery gate. Repeated plain log rows never create another actual Run or invoke an Action/Workflow. Verify the obsolete `recover_selected_run_recording` route is not exposed; no replacement recording-retry route or automatic effect replay is introduced. Genuine unknown source effects remain unknown and require their independently governed inspection, not a successful log append.

For the two direct Release commands, verify the closed connected-Project requests and explicit public draft, full-suite failure/unavailability/unknown-result stop before local delivery or public publication, including required integration tests. Missing Docker or another required test environment and skipped required tests must stop release, not produce a passing result. Required Docker integration tests build a disposable image from the current code; an old installed or running image is not a substitute, and test execution does not restart the running Project MCP. Verify there is no separate Active Atom metadata, placement or relation validation step. Retain truthful source-effect results independently of logging failure. Do not require a separate whole-catalog/dependency registry gate, old D527 selected execute envelope, DBOS dispatch or candidate/N+1 pipeline for release. Retain normal permissions, safe owned paths, installation locking/readback and public Git/PR boundaries; other selected routes keep their existing complete admission checks.

Acceptance retains request traces, target mutation traces, service invocation count, actual supplied log data and logging diagnostics, and independently observed output/result/effect references. This is planned functional proof, not a runtime pass.

### Sources

- CA-R-1847 v10; CA-R-1848 v6; CA-D-547 v7; CA-A-1142 v2; CA-P-1618 v1; CA-P-1535 v2; CA-D-527 v3; CA-R-1850 v2; CA-R-1866 v3; CA-R-1867 v1.
