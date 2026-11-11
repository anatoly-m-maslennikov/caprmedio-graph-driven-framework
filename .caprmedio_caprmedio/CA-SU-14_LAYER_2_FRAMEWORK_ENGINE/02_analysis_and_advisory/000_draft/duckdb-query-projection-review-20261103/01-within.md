# DuckDB query-projection packet review — within-packet

Reviewed: 2026-11-03 21:33:33 +0400

## Result

**Needs correction: 1 must-fix defect and 1 unresolved policy/acceptance gap.** The 26 Drafts otherwise carry the
proposal's key boundaries: governed sources remain authoritative; the existing
Docker/server owner is reused; native DuckDB SQL plus `expand` is the only
extension; source errors stay out of result rows; MCP and the ordinary web page
share Run/Check; and custom views and a renderer remain deferred.

## Scope and baseline

This is a source-only review of Active [CA-A-1316](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis/CA-A-1316-FRAMEWORK_ENGINE-SPECIFICATION_PROPOSAL--query-atoms-through-a-synchronized-duckdb-projection.md:29) version 2 and all 26 listed RMEDO Drafts. It does not review implementation, Docker, runtime, tests, or project-wide alignment.

The 27 inputs in `/private/tmp/duckdb-rmedo-review-input-snapshot-20261103.json` were re-hashed before this report: **27/27 matched** the snapshot SHA-256 values (0 drift). Filenames use `@1-draft`; headers keep base Atom IDs; and the proposal index labels are base Atom IDs only.

## Must fix

### 1. The Run/Check workflow fails to bind the transport required by its Step

**Scenario.** MCP and web both invoke the workflow for a Run whose result is
larger than a caller transport can carry. The Step requires a `calling
transport` to be bound by the enclosing Workflow, but the Workflow accepts only
Project, owner, SQL text, and request kind. It therefore cannot supply all Step
inputs or select the required explicit transport-limit terminal.

**Evidence.** [CA-O-242:40](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/09_operations/draft/duckdb-query-projection/CA-O-242@1-draft-FRAMEWORK_ENGINE-STEP--execute-the-shared-read-only-duckdb-query.md:40) lists `calling transport` as a bound precondition. Its parent [CA-O-245:40](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/09_operations/draft/duckdb-query-projection/CA-O-245@1-draft-FRAMEWORK_ENGINE-WORKFLOW--run-or-check-a-duckdb-query.md:40) omits it, although it must explicitly report a transport limitation. This is required by [CA-A-1316:197-200](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis/CA-A-1316-FRAMEWORK_ENGINE-SPECIFICATION_PROPOSAL--query-atoms-through-a-synchronized-duckdb-projection.md:197).

**Consequence.** The shared operation has an unsatisfied parameter contract at
the one boundary that must distinguish a complete Run response from an explicit
incomplete-transport result.

**Smallest correction.** Add the calling transport (or its explicit result-size
capability) to CA-O-245's preconditions and state that it is passed unchanged
to CA-O-242. No new evaluator, view, or response format is needed.

## Unresolved policy/acceptance gap

### Transient unreadable-carrier visibility is not decided or tested

**Scenario.** A previously indexed carrier is still present but cannot be read
on one reconciliation pass, such as during a transient I/O or permission error.
The Action says to remove its owned rows; the proposal calls a source read error
not proof of deletion and requires an unstable capture to be deferred. Neither
source states whether the previous committed rows remain visible, or whether the
carrier is excluded until a readable capture establishes its state.

**Evidence.** [CA-O-241:47](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/09_operations/draft/duckdb-query-projection/CA-O-241@1-draft-FRAMEWORK_ENGINE-ACTION--reconcile-the-duckdb-query-projection.md:47) chooses removal for both unreadable and invalid sources. [CA-A-1316:174-177](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis/CA-A-1316-FRAMEWORK_ENGINE-SPECIFICATION_PROPOSAL--query-atoms-through-a-synchronized-duckdb-projection.md:174) requires defer-on-unstable-capture; [CA-A-1316:185-189](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis/CA-A-1316-FRAMEWORK_ENGINE-SPECIFICATION_PROPOSAL--query-atoms-through-a-synchronized-duckdb-projection.md:185) specifies exclusion for invalid new/edited data and says read error is not proof of deletion, but does not prescribe transient-unreadable visibility. [CA-E-677:60-61](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/06_evaluation/draft/duckdb-query-projection/CA-E-677@1-draft-FRAMEWORK_ENGINE-EVAL_CASE--reconcile-source-lifecycle-and-invalid-repair-state.md:60) also has no assertion for the affected row.

**Why this is not a contradiction.** “Not proof of deletion” does not itself
forbid exclusion, and the proposal does not promise that a last-good row remains
current after a read failure. The Action's exclusion choice is therefore not
shown to conflict with settled source policy.

**Required choice before promotion.** State one policy and assert it in CA-E-677:
(a) retain the prior committed row while reporting/defer-retrying the read error,
or (b) exclude the unreadable carrier until a later readable state is captured.
Either choice must remain distinct from confirmed deletion and stable invalid
content; this review does not recommend one as already approved.

## Optional improvements

None. The review found no other actionable within-packet defect; repetition of
the same invariant across Requirement, Method, Delivery, Evaluation, and
Operations is traceability, not an independent conflicting Claim.

## Gaps

The two items above are the only connected-contract gaps found: an unresolved
source-state policy for an unreadable carrier, and the confirmed Workflow-to-Step
transport parameter defect. The packet otherwise has connected typed relations, compatible
tiers, and resolvable internal file links within this review scope.

## Verification

Read all 1,458 lines of the 27 manifest inputs; re-computed the snapshot hashes;
checked every packet header, filename convention, proposal-index label, and the
Requirement-to-Method/Delivery/Evaluation/Operations connections relevant to
the two findings. No source content was changed.

## Changed files

None (source packet). This report is the sole review artifact.

## Uncertainty

This report deliberately does not establish that the proposed DuckDB modes,
connector APIs, Docker image, stable-read helper, or runtime ownership can be
implemented as stated; those require the excluded implementation/runtime review.

## Not checked

No Current/Draft promotion, code, Docker, MCP registration, web implementation,
runtime execution, tests, Git operations, or whole-repository consistency check
was performed.

## Next action

Correct CA-O-245/CA-O-242's transport binding and choose the unreadable-carrier
policy with a CA-E-677 assertion; then re-review those four Drafts against
CA-A-1316 before any promotion.
