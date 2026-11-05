---
atom_id: CA-A-1322
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Draft
version: 1
author: Anatoly Maslennikov
role: Analysis & Advisory
form: Specification Proposal
tier: 3
subjects:
  active: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring
relations:
  depends_on:
  - CA-M-402
  - CA-M-403
  - CA-M-410
  - CA-M-424
  - CA-M-431
  - CA-M-432
  - CA-M-463
  - CA-M-465
  - CA-M-472
updated_at: 2026-11-05 06:14:51 +0400
carrier_destination:
  file:
    name: CA-A-1322@1-draft-PROGRAMMATIC-SPECIFICATION_PROPOSAL--simplify-programmatic-implementation-policies-and-workflow.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/02_analysis/draft
---

## Summary

Simplify PROGRAMMATIC implementation policies and workflow

## Proposal

Keep the modular monolith. Improve the implementation prompt and tests before adding architecture. Use the existing Policies wherever they already say what we need. Change only the Policies and local Decisions that leave a real gap or demand unnecessary work.

The first application is Workbench and its affected MCP adapters. Changes to general PROGRAMMATIC Policies require separate adoption. This proposal does not authorize code changes, result eviction, or changes to error handling.

## Review

What this change does: Workbench reads Current and Draft Atoms, builds a queryable Projection, and serves SQL through the web interface and MCP. This review assumes one personal Project with roughly 2,600 Atoms and modest query concurrency.

### Must fix

1. **A failed result response leaves an unreachable query table.**
   - What this is: Run materializes a result before converting its first page for delivery.
   - Problem: `SELECT 'NaN'::DOUBLE` fails conversion after registering the result. The caller gets no query ID, but the result table and registry entry remain. A later Page conversion can fail in the same way.
   - Fix: Release that result's table and registry entry when result conversion fails. Keep the original error; do not retry the query.
   - If skipped: Repeated failed requests keep consuming storage until restart.
   - Evidence: `FEATURE_WORKBENCH_BACKEND/query_store.py:233–270`; `tests/test_query_store.py:414–438` checks continued use after the error, but not cleanup.

2. **Closing a Worksheet can keep it open or change the wrong tab.**
   - What this is: Closing a tab removes it and chooses what remains visible.
   - Problem: Closing the only clean tab appends a replacement without removing the old tab. Closing an inactive tab always selects the first remaining tab.
   - Fix: Assign the remaining tab list once. Keep the active tab if it remains; otherwise choose a remaining tab or create one blank Worksheet.
   - If skipped: Close behaves differently from what the user requested.
   - Evidence: `FEATURE_WORKBENCH_FRONTEND/src/App.svelte:45–48`. No existing browser flow closes the last or an inactive tab.

### Should fix

3. **Watcher lifecycle tests bypass the watcher.**
   - What this is: The daemon should observe source creation, edits, moves and deletion.
   - Problem: The test named for that lifecycle calls private `_refresh()` after each operation. The permanent real watcher tests cover host creation and a Docker-mounted edit, not the complete lifecycle.
   - Fix: Start the existing functional service once; create, edit, rename and delete a source, then wait for public query results after each change. Include invalid-source exclusion and correction in the same flow. Keep the existing Docker edit proof.
   - If skipped: Tests can stay green when event delivery for moves or deletion breaks.
   - Evidence: `tests/test_workbench_functional.py:43–45,76–113`; `tests/test_workbench_docker_e2e.py:415–477`.

4. **Module traces are useful but incomplete and sometimes wrong.**
   - What this is: Header comments name directly implemented RED Atoms and local M Engineering Decisions with Versions.
   - Problem: `query_store.py` omits M462/M463; `service.py` omits M463/M465. `shared_project_catalog.py` cites Workbench query contracts that it only exposes. `http_paths.py` cites D578@2 while implementing the current prefixed route. E673/E674 have relevant tests but no direct header trace in the reviewed tests.
   - Fix: Review direct ownership and correct those comments. Do not replace every old Version mechanically: an older citation may still describe the implemented behavior.
   - If skipped: Comments give an unreliable starting point for impact analysis.
   - Evidence: backend module headers; `FEATURE_MCP/shared_project_catalog.py:1–2,57–177`; `FEATURE_MCP/http_paths.py:1,6–10`.

5. **Browser restoration loses the saved-item identity.**
   - What this is: Open Worksheet SQL and names survive reload through browser storage.
   - Problem: The stored tab omits its saved identity, so the Saved ID/link disappears after reload even when SQL is restored.
   - Fix: Persist the small saved-identity object with the tab. Continue excluding result rows. Verify Save/reload and Open Saved/reload through the browser.
   - If skipped: The restored Worksheet loses its connection to the last explicitly saved or loaded item.
   - Evidence: `FEATURE_WORKBENCH_FRONTEND/src/lib/workspace.js:13–31`; `src/App.svelte:49–52,83,114`.

### Nice to have

6. **Projection-only changes trigger source scans.**
   - What this is: Each non-Journal watcher batch rereads the full source inventory.
   - Problem: Derived `_projection` changes trigger scans although those files are excluded from the reader. Even a no-change scan releases successful parse caches under the current Decision.
   - Fix: Ignore projection-only events alongside Journal-only events. Keep full inventory refresh for admitted source changes. Review cache policy separately before changing its lifetime.
   - If skipped: Rebuilding projections causes avoidable scanning; no incorrect result was found.
   - Evidence: `FEATURE_WORKBENCH_BACKEND/service.py:54–101`; `source_reader.py:182–197`.

### Architecture and leftovers

Keep the existing responsibilities: source reader, relation materialization, serialized query store, saved-item store, service lifecycle, MCP/HTTP adapters, and small frontend components. No broad rewrite, new service, plugin framework or incremental indexer is justified by this review.

The read-only legacy saved-ID fallback is deliberate compatibility, not dead code. Private Markdown property parsing remains necessary even though raw parsing columns are no longer public. Small unused CSS selectors can wait; they do not justify a refactor.

The trace audit counted 120 versioned references across 52 bounded files: 83 match Current versions, 33 cite older versions, and four occur only in fixtures. Those counts measure comments, not conformance. Fixture references do not count as implementation ownership. No checker currently establishes that a cited Claim is implemented.

### Watcher evidence

Disposable real-watchfiles probes passed creation, edit, rename, deletion and a valid Scope Unit Declaration edit. Permanent tests still lack that complete event-driven sequence. Twenty-three focused reader/service tests and three frontend state tests passed during review. The reviewer did not run the Docker suite or inspect the live database.

An invalid ordinary Atom is excluded with stderr output. An invalid Scope Unit Declaration stops indexing and requires a restart. The Operator confirmed this stricter Declaration behavior; retain it.

Verdict: fix 1 and 2 first. Preserve the current architecture.

Not checked: a fresh full-suite run, a fresh Docker/browser run, and long-running live database growth. Review probes did not change source Atoms or the running server.

## Policy changes

| Current source | Proposed treatment |
| --- | --- |
| M402 — only declared business logic | Keep. Put its rule near the start of the implementation prompt. Ask the Operator about an undefined behavior; do not invent a gate, restriction, retry or recovery path. |
| M403 — one canonical owner | Keep. Review actual callers and ownership before adding another helper or layer. |
| M432 — modular monolith | Keep. Use existing module boundaries; do not split deployment or introduce internal network APIs. |
| M410 — resource bounds | Keep the general Policy. Require a concrete resource-lifetime check in the implementation review. Resolve its conflict with M463's unlimited Run-result retention through a local Decision. |
| M424 — test selection | Replace portfolio enumeration with the short behavioral rule below. Keep any genuinely applicable Evaluation constraints; identify affected links before adoption. |
| M431 — module trace comments | Keep its present Claim. Add a small review step to the prompt, rather than another trace Policy or runtime source pins. |
| M472 — Workbench browser testing | Keep the local Playwright/container choice. Reusable test-selection guidance belongs in M424 rather than being copied into each App. |
| M463 — Workbench ownership and materialization | Keep one owner, serialization and pagination. Adopt the confirmed Worksheet result lifetime when implementing retention. Saved-item Journal retention is separate. |
| M465 — Workbench watcher | Keep watchfiles and full-inventory refresh. Retain the confirmed fail-stop behavior for invalid Scope Unit Declarations. Clarify admitted-source events before changing their filtering. |

### Proposed replacement Claim for M424

Choose tests from the declared behavior and the ways it can fail.

- Prefer a real user or public API flow when it covers the behavior at reasonable cost.
- Test lifecycle behavior through the real lifecycle. A watcher test changes files and waits for observed results; it does not call refresh directly.
- Add focused unit tests for rules or edge cases that the broader flows cannot distinguish reliably.
- Check repeated operations and failure paths where they can retain resources or lose state.
- Reuse the existing test environment. Do not create another container for each case when one running container can cover them.
- Report uncovered behavior. Do not invent test-count ratios, require one test per Atom, or enumerate every possible test portfolio.

This replaces test-selection ceremony, not applicable behavior requirements or release checks. Review M424's related Evaluation Atoms before adopting the replacement so that Current sources do not contradict it.

### Tracing in the workflow

For each materially changed module, inspect the header against its actual responsibilities. Include only directly implemented R/E/D and M Engineering Decision IDs with Versions. Do not put generic applied Policies or called-only contracts in the header. Test modules cite Evaluations they actually exercise.

A small read-only reference check can find malformed IDs, missing sources and older Versions. It cannot determine semantic ownership or conformance. It must not pin runtime behavior to source hashes, rewrite comments automatically, or add a release gate. Start with the bounded manual check; add the command only if repeated use warrants it.

## Main implementation prompt

Use this as one prompt, compiled with the relevant Current M Policies. Select Policies by the change's responsibilities and applicable scope, rather than copying every PROGRAMMATIC Atom or using Subjects alone.

```text
Implement the approved change with the smallest complete solution.

Inputs:
- Operator goal and explicit scope.
- Accepted R/E/D and local M Engineering Decisions for this change.
- Relevant Current M Policies from PROGRAMMATIC and applicable descendants.

Read the touched code, its callers, tests and existing helpers. Keep one owner
for each behavior. Reuse the current modular application and its dependencies.

Implement only declared behavior. Do not add business rules, restrictions,
retries, repair, rollback or approval stages. If required behavior is missing
or conflicting, ask the Operator. Resolve routine implementation choices yourself.

Keep functions and modules focused on their jobs. Use pure functions for
transformations and objects for owned state and resources. Keep UI components
small and reuse the component palette. Above 300 lines, restructuring is strongly
recommended; above 500 lines, it is mandatory. Split by responsibility.

For retained state, define when it is created and released. Check repeated
successes, failures and shutdown against the declared resource bounds. Do not
silently invent a retention or eviction policy.

Add header comments for directly implemented R/E/D and M Engineering Decisions:
one Atom ID with Version per line, with no labels or prose. Applied generic
Policies and called-only contracts do not belong in module headers.

Prove behavior at its real boundary. Prefer a real UI/API/lifecycle flow; use
focused unit tests for remaining rules and edge cases. Do not mock away the
behavior under test or call a private method in place of the lifecycle.

Run the affected checks. Review the connected code for wrong ownership,
leftover paths, retained resources and unsupported extra behavior. Fix concrete
issues without broad cleanup. Report what changed, what passed and what remains
unverified. Passing focused tests does not mean deployment is complete.
```

The 300/500-line thresholds above preserve the Operator's frontend/module-size instruction. Do not turn them into a reason to create meaningless helpers.

## Implementation workflow

1. Read the Operator request and relevant Current RMED. Update and review RMED only where behavior changes or authority has a gap; adopt those changes before implementation.
2. Compile one short implementation prompt from those sources and the relevant M Policies. Keep the selected source IDs and Versions with that prompt, not as a second business specification.
3. Implement one complete behavior at a time, including callers, tests, fixtures and documentation. Prepare the real boundary test alongside it.
4. Review the implemented behavior, direct trace ownership and resource lifetime. Use independent review for distinct risky areas, with exclusive edit ownership when work is parallel.
5. Run affected checks. Reuse one built image for the required integration/browser flows. Preserve the existing release requirements; do not add full-Atom or registry validation as another release gate.
6. Release only the tested result, verify the public behavior, then update the Epic. A proposal, code comment or focused test result does not close implementation work.

Do not require a separate Analysis Atom or report for each changed Atom, module or function. Keep work instructions in Tasks and design in RMED or a Spec Proposal.

## Workbench decisions

1. **Transient Run-result retention — confirmed.** Keep a browser result while its Worksheet is open, including inactive tabs. Remove it when that Worksheet closes or a successful Run replaces it. A failed Run leaves the previous result available. Saved queries and Worksheets store SQL, not result tables. Browser-crash handling, disconnected-browser detection, and a new MCP Release result operation are outside this change. Do not add an LRU, TTL, count budget or cleanup daemon. Keep existing startup cleanup.
2. **Invalid Scope Unit Declaration — confirmed.** Keep the stricter existing behavior: report the error to stderr, stop indexing and require a restart. Do not skip the Declaration and continue with partial structure, resume automatically after a later edit, repair the source or use stale structure. Ordinary invalid Atoms retain their separate skip-and-report behavior. No runtime change is needed for this decision.

## Sources

The review paths below are relative to `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH` unless prefixed with `FEATURE_MCP`.

- Current Policies: CA-M-402@11, CA-M-403@9, CA-M-410@9, CA-M-424@12, CA-M-431@11, CA-M-432@8.
- Current local Decisions: CA-M-462@7, CA-M-463@4, CA-M-465@11; Workbench test guidance CA-M-472@1.
- Review targets: backend `query_store.py`, `service.py`, `source_reader.py`; frontend `src/App.svelte`, `src/lib/workspace.js`; Workbench functional and Docker tests; affected MCP adapters and tests.
- Execution is tracked by CA-P-2710. The previous deployment is Workbench 0.4.4.21; this review makes no runtime change.


## Workbench service operation

Add one service operation, `workbench_restart`, available through MCP and a health-page button, to restart only the selected Project's Workbench inside the existing server process. Close the previous Workbench owner, start a fresh index from its sources, and clear temporary result IDs. Keep MCP and other services running. Preserve source files and saved-query/Worksheet Journal entries. Report failure explicitly if startup is still invalid; do not retry or recover automatically. Do not add generic shell, container control, a service registry, or unrelated maintenance commands.

Related adopted service contracts: CA-R-2782@2, CA-D-676@2, CA-D-677@1, CA-E-679@1, CA-E-680@1 and CA-D-639@15. General policy changes and result-retention implementation remain pending.

The MCP and health-page restart implementation passed focused tests and independent code review. Verification: `.caprmedio_tmp/workbench/service-restart/verification.json`. It is not yet deployed. Other audit fixes, general Policy adoption and query-result retention remain pending.
