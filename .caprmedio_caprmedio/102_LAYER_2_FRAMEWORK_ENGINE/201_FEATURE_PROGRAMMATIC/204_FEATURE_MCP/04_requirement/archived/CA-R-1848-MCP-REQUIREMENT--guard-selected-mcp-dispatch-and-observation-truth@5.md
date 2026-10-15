---
atom_id: CA-R-1848
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-14 19:54:14 +0400"
subjects:
  governs: "MCP/selected Workflow dispatch truth"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal]
relations: {}
---
# Summary

Guard selected MCP dispatch and observation truth

## Scope

Authorization, currentness, result truth, and defer/handoff behavior at the selected MCP boundary.

## Claim

MCP **must not** invent dispatch, completion, effects or logging success. Each reported fact must retain the actual shared-service **or** direct-runner result and its truthful diagnostics; a Journal entry is not permission or proof of source-effect completion.

## Details

The complete manifest/source/permission gate remains required for non-Release selected routes and their query admissions. The two direct local/public Release commands instead use CA-D-547's simple connected-Project runner interface and full test suite, without an additional whole-catalog, dependency-registry, Release-source-admission, D527 selected-envelope or DBOS gate. Normal explicit inputs, existing Operator/client permissions, current source/file safety, actual Run outcomes, installation lock/readback and public Git/PR boundaries remain required. Full-suite verification includes required integration tests; missing Docker or another required test environment, or skipping required tests, cannot pass release. Release verification adds no separate Active Atom metadata, placement or relation validation; the full test suite and normal input, permission and file/path safety checks remain. Required Docker integration tests build a disposable image from the current code; an old installed or running image is not a substitute, and test execution does not restart the running Project MCP. A source-defined condition or a log entry does not prove tests or effects ran. This clause supplies no new execution, confirmation, retry or publication authority.

Before a non-Release selected preview or execute, the adapter validates that route against
exactly one outer `definition_manifest` reference/digest, its canonical binding,
exact admitted source/definition revisions, root/frontier and target/reference
digests, input schema, and parent lineage. That one manifest preserves CA-A-1142
v2 as the unchanged original-thirteen registry and contains the two exact
CA-P-1618@1/CA-P-1535@2 query-source admission frontier pins required by
CA-R-1847, including its explicit byte-identical relocation, O163@2-to-@3 structural-successor bridge and exact O163@4 plain-Journal reading amendment; the two Done proof carriers remain unchanged and it has no competing registry, manifest, or third query proof. The source-freshness
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
adapter must not substitute a newer source revision, widen a selected set,
infer authority from a prior request, or accept an `apply` mode.

For `find_and_fetch_journal_events`, capture the source Journal byte-prefix and
bind CA-O-163's snapshot token before any Workflow/Action-start recording or
Action dispatch. Only the sealed prefix can be queried; later Run/Event records
are outside it. Both query routes accept only CA-R-1850's shared closed literal
grammar, safe selected fetches, and no credential/secret selection. They do not
create a new parser, Journal writer, or read-only-to-mutation conversion.

The existing shared service or direct runner owns its actual execution, cancellation and source-effect outcome. MCP preserves a deferred, handoff-required, failed, canceled, partial-effect, unknown-effect or no-op result without converting it into success. A no-op has no invented mutation; a handoff has its actual continuation/reference and no claimed local dispatch; an unstarted call has no invented Action Run. Plain Journal append/read has no prior-history, chain, validation, receipt, deduplication, retry or recovery prerequisite. Preserve actual logging I/O diagnostics independently of the observed Run/source-effect result; do not downgrade a completed source effect solely because logging fails, claim an unobserved append, or replay work because a log row is absent or repeated. Source-effect uncertainty and no-effect-replay safeguards remain unchanged.

Observation results disclose only references and redacted safe material authorized by the selected Run; they never fabricate output/results, reveal secrets, or treat an outbox/intake acknowledgement as proof of an effect or successful Journal append. The adapter reports the source currentness observed for the operation and actual safe Run, result/effect/report references and logging diagnostics returned by the service or runner. It is a projection boundary, not an authority to alter source, Artifact, or Journal history.

### Sources

- CA-A-1142 v2, unchanged original-thirteen registry; CA-P-1618 v1 and CA-P-1535 v2, exact query admission frontiers.
- CA-D-527 v3; CA-D-521 v7; CA-R-1720 v19; CA-R-1525 v7; CA-R-1728 v16; CA-D-523 v2; CA-R-1850 v2; CA-R-1866 v3; CA-R-1867 v1.
