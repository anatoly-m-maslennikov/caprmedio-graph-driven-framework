---
updated_at: "2026-10-22T16:35:33Z"
---
# PROGRAMMATIC Evaluation — Implementation Prompt

## Role and use

Prepare and evaluate the assigned PROGRAMMATIC change against applicable current authority. This is a compact, non-authoritative view of explicitly Active root Evaluation atoms, not a passing-test receipt or a replacement for their exact cases.

Use together with [Methods](mrt_programmatic_methods_compact.projection.md) and [Delivery](mrt_programmatic_delivery_compact.projection.md) during preparation, not only after implementation. M guides construction, E establishes applicable quality checks, and D binds encoding, placement and package boundaries. Load applicable Project Principles, Methodology, task Requirements/Operations and child-scope rules separately. Select cases by the changed behavior and their actual applicability; the inventory is not an instruction to run every case for every task.

For a formal CA-O-016 invocation, follow the [Implementation Workflow input contract](../../../../102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/README.md): the verified full-content active-M file and separately bound R/D/E sources remain required. These compact views are supplemental guidance, not substitutes for that file or the source contents/digests, and are not automatically injected into runtime packets.

## Core evaluation boundaries

- **Observable evidence — E637.** Every declared failure predicate needs at least one reproducible check. Do not make behavioral acceptance depend solely on replaceable private implementation where a semantic/public boundary can expose the predicate. This evidence floor does not prescribe a portfolio, cost ranking or test-scope ratio.
- **Safe canary exposure — E638.** If using canaries, require isolated cohort/shadow exposure, explicit bounds, immediate stop and rollback tested against the applicable state boundary. Canary evidence supplements, not replaces, required pre-deployment evidence. E536 supplies detailed admission conditions.
- **Complete-change readiness — E639.** Before representing a change as ready for acceptance/delivery, reconcile its known required affected-surface and dependency closure as one increment: affected consumers/adapters, parsers/registries, configuration/dependencies, fixtures and delivery. Known required omissions remain readiness gaps. Distinguish invalid test targets from defective support/harness inputs; preserve deliberate red/exploratory tests. Repair known shared causes at their canonical owners, not merely the latest symptom. This neither promises a defect-free first attempt nor requires tests to pass before any test can run. Readiness is not permission or completed execution and adds no approval, Journal-completeness, live-Atom, registry or release-workflow gate.

## General evaluation policies

### Portfolio selection — E389

With the applicable Spec and failure predicates, identify for each check its authority, observed boundary, replay inputs, expected/actual results, runtime, flakiness, maintenance and failure-localization evidence. Classify test scope, purpose, realism, environment and release stage separately: functional is a purpose; canary is a release stage.

Select at least one reproducible check per predicate at the least-costly stable observable boundary established by evidence. Keep small semantic checks for pure transformations, invariants, dense edge cases and diagnosis. Reject private-helper, call-order, object-layout or mock-choreography assertions unless that interaction is governed behavior. Use focused integration/public-functional checks for real file, Git, process, packaging, protocol and adapter boundaries; controlled external dependencies may be substituted, not the implementation being evaluated.

Retain installed end-to-end checks only for critical journeys/emergent failures narrower checks cannot expose. Retain higher-boundary duplication only with an explicit emergent-risk or defense-in-depth purpose. No fixed test counts, ratios, raw coverage target or universal scope ranking establishes sufficiency. Return unresolved when coverage, boundary stability or relative cost lacks evidence.

### Canary admission — E536

Before exposure, bind exact change, cohort/shadow selector, representative workload frontier, control, health predicates, maximum exposure, observation window, stop owner, rollback procedure and replayable rollback evidence. Inadequate isolation/comparison/stopping/rollback rejects the proposed canary. Unproven representativeness or state recovery is unresolved; use dry-run, differential or recoverable-fixture evidence instead. This is not permission to run against production.

### Changed Python source and lint ratchets — E539

For new/materially changed hand-authored Tools, App backends and MCP Python, target **<=200 physical lines/file** and **<=25 logical lines/executable unit**. Units of 26–40 logical lines retain one coherent job; a larger file/unit needs a specific accepted bounded exception identifying measured size/failed rule, maximum, reason, scope and reconsideration condition. Unit-size exceptions preserve one responsibility.

Require current cyclomatic-complexity evidence from the admitted pinned Ruff C901 profile for every changed executable unit, satisfying the canonical configured maximum or accepted exception. Apply the pinned formatting/lint profile; missing/unpinned profiles leave conformance unresolved. Externalize static mappings exceeding 20 entries or 25 source lines. Preserve the admitted passing boundary; unmodified oversized legacy source and generated Runtime/Delivery outputs are outside this changed-source check.

Review cohesion, responsibility, dependency direction and testability separately. Lower measurements do not justify obscuring responsibilities or recovery boundaries. These are Evaluation conditions, not an absolute project-wide file/function gate or proof of quality.

### Static typing — E540

Within the admitted Mypy target set, new targets pass the strict admitted pinned profile; changed targets do not regress below their passing baseline. Explain each suppression at the narrowest affected line/symbol. Missing profile, targets, required baseline or current evidence is unresolved; broad unexplained suppressions/regressions are rejected. Typing evidence is distinct from runtime validation and behavioral evidence; unrelated unmodified legacy targets do not become a whole-project blocker.

## Conditional Standard QA playbooks

Read each selected source case for its exact fixture, acceptance criteria and failure disposition before executing or implementing it.

- **Technical contract and installation — E253–E255.** Verify changed components against Method-owned runtime/dependency selections. An exception needs the accepted bounded selecting Method plus complete configuration, implementation, delivery and evidence materializations. Its required capability, bounded-carrier, interface, boundary-cost, evidence and Operator-acceptance fields must be present; incomplete records do not admit the affected component or turn those carriers into selection authority. Installed-component checks apply when lower-scope Delivery declares installability and do not establish undeclared platform support.
- **Determinism, state and replaceable boundaries — E256–E259.** Check deterministic output from explicit inputs without ambient observations/effects; bounded state/resource/lifecycle ownership; interruption followed by restart/recovery without false completion; and typed contracts at replaceable technical boundaries.
- **Decisions before effects — E260–E261.** Observe a complete explicit decision/plan before effect application. Missing required plan inputs cause no effect, not inferred defaults or hidden policy.
- **Files and subprocess outcomes — E262–E265, E362.** Unmet file preconditions leave bytes unchanged. Interrupted replacement preserves or explicitly reports recovery without claiming completion. Nonzero process exits and timeouts are typed/diagnosable. The default subprocess case uses argument arrays, explicit timeout, checked status, controlled environment and no shell; preserve any explicit governing exception rather than inferring a universal ban from a fixture.
- **Functions, objects and inheritance — E356–E361.** Reject namespace-only classes, objects without persistent ownership, construction-time I/O and inheritance without a substitutable contract. A bounded one-shot effect may be a function with explicit boundaries and no persistent ownership; persistent state/resource/lifecycle effects require an owner object.
- **Source boundaries — E266, E363–E368.** Check the changed file/unit boundary or accepted exception, one job for medium units, current complexity evidence, explicit visible effects, unambiguous names and externalization of large static mappings. Apply the General E539 scope/exception rules; do not turn source metrics into quality proof.
- **Diagnostics and logging — E267–E269, E369–E370.** Verify structured severity/context and secret redaction; exercise a diagnostic-emission failure and retain its actual outcome. Production DEBUG selection is bounded with expiry; Logging Policy is fully materialized at its declared boundary. Do not silently swallow failure or broaden logging indefinitely.
- **Capability adoption and idioms — E270, E451.** Verify the changed-code adoption ratchet and declared benefit of a new idiom. Configuration and Implementation materialize the Method-owned selection or accepted bounded exception; Delivery governs its carrier. Journal Records carry actual-result evidence without becoming selection authority or a universal prerequisite to first mutation.
- **Performance and compatibility — E271–E272.** Performance claims need representative workload/environment, preserved baseline, observed distribution and an admitted comparison threshold; invent no numeric budget. Verify accepted declared Tool/App/MCP or host interfaces and any accepted replacement; do not infer undeclared cross-host/platform support.
- **Python workflow and profiles — E376–E378, E385, E452–E453.** From an empty selected Project environment, run `uv sync --locked`, then the declared command through `uv run --locked`: neither `pyproject.toml` nor `uv.lock` changes, the interpreter meets the Method-selected boundary and only Method-selected dependencies are used. Reject an unaccepted overlapping workflow manager before environment mutation; an exception needs governed capability, bounded carriers, commands, cost, recovery procedure and Operator acceptance. Apply the canonical Python/tool configuration plus pinned Ruff/Mypy profiles. E378 separately specifies an installed Tool in `.caprmedio_runtime/tools` runnable without uv/project virtualenv or dependencies outside the selected release; see the execution-boundary caveat below.
- **Shared Settings Reader — E454.** Observe one validated immutable Settings snapshot across representative Tool/App/MCP consumers. The shared Reader validates at its boundary; consumers receive the snapshot explicitly and preserve the same carrier/digest provenance, with no direct reads, fallbacks, private default selection or mutation. Reuse of an already validated snapshot is allowed; do not invent a per-consumer read count.
- **Temporary state — E467.** Include components, configured dependencies and test runners: temporary/scratch/staging/cache/build/evaluation/remnant carriers stay under configured Project Temporary State with concurrent owner/run-specific descendants. Detect ambient/hard-coded fallbacks and Runtime State bytecode caches. In isolated fixtures, deleting only Temporary State leaves authority, Journals, selected releases, logs, sessions, databases and resumable/service state unchanged. Unavailable roots or failed same-filesystem staging preconditions stop the affected effect with owner/path diagnostics. Do not convert an isolated deletion case into permission to delete real Project data or invent automatic teardown policy.
- **Shared-runtime routing and isolation — E641.** Build two disposable valid
  Project fixtures with identical local IDs and exercise concurrent, interleaved,
  asynchronous, nested and reload-adjacent calls through one external MCP.
  Reproduce cross-Project, outside-root, ambiguous-prefix, identity-mismatch,
  stale/inactive-tool and schema-conflict refusals; verify bounded warm-context
  behavior (idle-only eviction and busy refusal), actual bound prefixes in
  request logs, and preserved Project-owned state. Check health JSON, 503
  readiness, loopback/HTML behavior and unchanged native payloads without
  treating the planned fixture as executed evidence or an OS-security claim.
- **Native Tool and Workflow frontier — E650.** Inventory callable native Tools
  and Workflows separately for the bound Project. Verify valid Workflow
  invocation contracts and declared providers are exposed and delegated
  unchanged; do not invent an endpoint, composition or executability from a
  source definition alone. Keep internal CONNECTORS/adapters and PROJECT_TOOLS
  outside the frontier, quarantine an invalid Project Tool without removing
  healthy entries, and retain any failed replacement only as an explicitly
  prior frontier. This is a declared check, not execution evidence.

## Source-bound caveats and outcomes

- **Execution boundary to reconcile:** M423 explicitly applies uv-managed isolation to Project Python, including installed Project Tools. E378 explicitly checks a standalone installed Tool without uv or a project virtualenv. For an artifact subject to both, resolve the actual governing execution boundary from current sources/Operator authority before choosing an incompatible realization; this projection does not silently override either source or claim the scenario passes.
- **Portfolio and ownership boundaries — E642, E644.** E642 assesses substantive
  coverage of every applicable Active Method at Core, General and Standard tiers;
  relations and definitions alone are not implementation conformance, and each
  obligation remains covered, partial, uncovered or inapplicable. E644 applies
  only to implemented, in-scope declared Requirement/Delivery obligations:
  identify their canonical owners, verify representative callers/adapters, and
  reject invented policy. Prefer cohesive locality without imposing a hard
  one-file/one-unit rule; deliberate shared ownership needs evidence.
- Excluded legacy Methods/Evaluations are not declared retired by this selection. If a selected E depends on one, resolve that original's authority/applicability separately; do not manufacture status or ignore the dependency.
- Keep pass, fail, unresolved, partial and uncertain outcomes distinct. Missing measurements, environment, replay, currentness or exception evidence cannot be reported as successful checks. A retained Journal observation is not by itself a behavioral verification receipt.
- Root guidance does not replace child-scope checks, exact source-bound validator fixtures, release rules or actual installed execution evidence.

## Sources, scope and freshness

Selection: direct root `05_method/*.md` and `06_evaluation/*.md` with explicit `status: Active`, the matching content role and `current_scope_unit: PROGRAMMATIC`. All selected carriers are source-bound to PROGRAMMATIC. Snapshot: **39 Methods — 5 Core, 6 General, 28 Standard** and **62 Evaluations — 3 Core, 12 General, 47 Standard, 0 unclassified**. Non-active, archived, descendant and otherwise out-of-frontier carriers are excluded without inferring retirement.

Refresh from originals when relevant content, status, tier, relation or selection changes. `updated_at` marks this rebuild, not currentness or execution proof. Source revisions, links and hashes are provenance only; this view changes no source Atom, status, tier, implementation, runtime or release. Historical/legacy source carriers and their exact relation targets remain preserved; this projection does not certify their full schema or applicability.

| Tier from metadata | Source revision | Summary |
|---|---|---|
| Core | [CA-E-637@3](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-637-PROGRAMMATIC-CORE-EVAL_APPROACH--require-observable-evidence-for-behavioral-acceptance.md) | Require observable evidence for behavioral acceptance
| Core | [CA-E-638@3](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-638-PROGRAMMATIC-CORE-EVAL_APPROACH--bound-and-recover-canary-exposure.md) | Bound and recover canary exposure
| Core | [CA-E-639@5](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-639-PROGRAMMATIC-CORE-EVAL_APPROACH--require-complete-change-readiness-before-delivery.md) | Require complete change readiness before delivery
| General | [CA-E-389@15](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-389-PROGRAMMATIC-GENERAL-EVAL_APPROACH--combine-complementary-software-behavior-evidence.md) | Combine complementary software behavior evidence
| General | [CA-E-536@6](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-536-PROGRAMMATIC-GENERAL-EVAL_APPROACH--admit-safe-canary-evaluation.md) | Admit safe canary evaluation
| General | [CA-E-539@4](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-539-PROGRAMMATIC-GENERAL-EVAL_APPROACH--evaluate-python-source-boundaries-and-lint-ratchets.md) | Evaluate Python source boundaries and lint ratchets
| General | [CA-E-540@4](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-540-PROGRAMMATIC-GENERAL-EVAL_APPROACH--evaluate-static-typing-baselines-and-suppressions.md) | Evaluate static typing baselines and suppressions
| General | [CA-E-642@5](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-642-PROGRAMMATIC-GENERAL-EVAL_APPROACH--evaluate-active-method-coverage.md) | Evaluate active Method coverage
| General | [CA-E-643@4](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-643-PROGRAMMATIC-GENERAL-EVAL_APPROACH--evaluate-workload-resource-bounds.md) | Evaluate workload resource bounds
| General | [CA-E-644@5](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-644-PROGRAMMATIC-GENERAL-EVAL_APPROACH--evaluate-declared-behavior-and-canonical-ownership.md) | Evaluate declared behavior and canonical ownership
| General | [CA-E-645@4](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-645-PROGRAMMATIC-GENERAL-EVAL_APPROACH--evaluate-observed-outcomes-and-partial-results.md) | Evaluate observed outcomes and partial results
| General | [CA-E-646@4](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-646-PROGRAMMATIC-GENERAL-EVAL_APPROACH--evaluate-suitable-established-reuse.md) | Evaluate suitable established reuse
| General | [CA-E-647@3](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-647-PROGRAMMATIC-GENERAL-EVAL_APPROACH--evaluate-public-operation-error-boundaries.md) | Evaluate public operation error boundaries
| General | [CA-E-648@4](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-648-PROGRAMMATIC-GENERAL-EVAL_APPROACH--evaluate-pure-effects-and-business-recording.md) | Evaluate pure effects and business recording
| General | [CA-E-651@4](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-651-PROGRAMMATIC-GENERAL-EVAL_APPROACH--evaluate-authorized-targets-and-deltas.md) | Evaluate authorized targets and deltas
| Standard | [CA-E-253@15](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-253-PROGRAMMATIC-QA_CASE--verify-changed-component-technical-contract-conformance.md) | Verify changed component technical-contract conformance
| Standard | [CA-E-254@14](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-254-PROGRAMMATIC-QA_CASE--reject-incomplete-technical-contract-exception.md) | Reject incomplete technical-contract exception
| Standard | [CA-E-255@15](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-255-PROGRAMMATIC-QA_CASE--verify-installed-selected-runtime-component.md) | Verify installed selected-runtime component
| Standard | [CA-E-256@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-256-PROGRAMMATIC-QA_CASE--verify-deterministic-transformation-from-declared-inputs.md) | Verify deterministic transformation from declared inputs
| Standard | [CA-E-257@14](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-257-PROGRAMMATIC-QA_CASE--verify-owned-state-and-lifecycle-boundary.md) | Verify owned state and lifecycle boundary
| Standard | [CA-E-258@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-258-PROGRAMMATIC-QA_CASE--recover-an-interrupted-stateful-lifecycle-after-restart.md) | Recover an interrupted stateful lifecycle after restart
| Standard | [CA-E-259@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-259-PROGRAMMATIC-QA_CASE--verify-replaceable-technical-boundary-contract.md) | Verify replaceable technical boundary contract
| Standard | [CA-E-260@14](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-260-PROGRAMMATIC-QA_CASE--verify-decision-precedes-effect-application.md) | Verify decision precedes effect application
| Standard | [CA-E-261@14](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-261-PROGRAMMATIC-QA_CASE--reject-incomplete-plan-at-effect-boundary.md) | Reject incomplete plan at effect boundary
| Standard | [CA-E-262@14](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-262-PROGRAMMATIC-QA_CASE--reject-file-mutation-with-unmet-precondition.md) | Reject file mutation with unmet precondition
| Standard | [CA-E-263@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-263-PROGRAMMATIC-QA_CASE--recover-one-partial-file-write.md) | Recover one partial file write
| Standard | [CA-E-264@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-264-PROGRAMMATIC-QA_CASE--surface-one-nonzero-subprocess-result.md) | Surface one nonzero subprocess result
| Standard | [CA-E-265@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-265-PROGRAMMATIC-QA_CASE--surface-one-subprocess-timeout.md) | Surface one subprocess timeout
| Standard | [CA-E-266@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-266-PROGRAMMATIC-QA_CASE--verify-changed-source-boundary-or-exception.md) | Verify changed source boundary or exception
| Standard | [CA-E-267@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-267-PROGRAMMATIC-QA_CASE--verify-structured-diagnostic-schema.md) | Verify structured diagnostic schema
| Standard | [CA-E-268@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-268-PROGRAMMATIC-QA_CASE--verify-diagnostic-secret-redaction.md) | Verify diagnostic secret redaction
| Standard | [CA-E-269@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-269-PROGRAMMATIC-QA_CASE--observe-one-diagnostic-emission-failure.md) | Observe one diagnostic emission failure
| Standard | [CA-E-270@15](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-270-PROGRAMMATIC-QA_CASE--verify-changed-code-adoption-ratchet.md) | Verify changed-code adoption ratchet
| Standard | [CA-E-271@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-271-PROGRAMMATIC-QA_CASE--verify-measurement-backed-performance-claim.md) | Verify measurement-backed performance claim
| Standard | [CA-E-272@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-272-PROGRAMMATIC-QA_CASE--verify-declared-interface-compatibility.md) | Verify declared interface compatibility
| Standard | [CA-E-356@11](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-356-PROGRAMMATIC-QA_CASE--reject-a-class-used-only-as-a-function-namespace.md) | Reject a class used only as a function namespace
| Standard | [CA-E-357@11](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-357-PROGRAMMATIC-QA_CASE--reject-an-object-without-persistent-ownership.md) | Reject an object without persistent ownership
| Standard | [CA-E-358@12](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-358-PROGRAMMATIC-QA_CASE--reject-i-o-during-object-construction.md) | Reject I/O during object construction
| Standard | [CA-E-359@11](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-359-PROGRAMMATIC-QA_CASE--reject-inheritance-without-a-substitutable-contract.md) | Reject inheritance without a substitutable contract
| Standard | [CA-E-360@11](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-360-PROGRAMMATIC-QA_CASE--admit-a-bounded-one-shot-effect-function.md) | Admit a bounded one-shot effect function
| Standard | [CA-E-361@11](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-361-PROGRAMMATIC-QA_CASE--require-an-object-for-a-persistent-effect-owner.md) | Require an object for a persistent effect owner
| Standard | [CA-E-362@7](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-362-PROGRAMMATIC-QA_CASE--reject-an-unsafe-subprocess-invocation.md) | Reject an unsafe subprocess invocation
| Standard | [CA-E-363@11](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-363-PROGRAMMATIC-QA_CASE--reject-an-oversized-changed-python-file.md) | Reject an oversized changed Python file
| Standard | [CA-E-364@12](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-364-PROGRAMMATIC-QA_CASE--reject-a-medium-unit-with-multiple-jobs.md) | Reject a medium unit with multiple jobs
| Standard | [CA-E-365@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-365-PROGRAMMATIC-QA_CASE--reject-unchecked-cyclomatic-complexity.md) | Reject unchecked cyclomatic complexity
| Standard | [CA-E-366@12](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-366-PROGRAMMATIC-QA_CASE--reject-a-hidden-effect-in-changed-source.md) | Reject a hidden effect in changed source
| Standard | [CA-E-367@12](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-367-PROGRAMMATIC-QA_CASE--reject-an-ambiguous-changed-source-name.md) | Reject an ambiguous changed source name
| Standard | [CA-E-368@12](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-368-PROGRAMMATIC-QA_CASE--externalize-a-large-static-mapping.md) | Externalize a large static mapping
| Standard | [CA-E-369@11](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-369-PROGRAMMATIC-QA_CASE--reject-unbounded-production-debug-logging.md) | Reject unbounded production DEBUG logging
| Standard | [CA-E-370@11](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-370-PROGRAMMATIC-QA_CASE--verify-logging-lifecycle-materialization.md) | Verify logging lifecycle materialization
| Standard | [CA-E-376@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-376-PROGRAMMATIC-QA_CASE--reproduce-a-locked-uv-environment.md) | Reproduce a locked uv environment
| Standard | [CA-E-377@12](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-377-PROGRAMMATIC-QA_CASE--reject-an-unaccepted-overlapping-python-workflow-manager.md) | Reject an unaccepted overlapping Python workflow manager
| Standard | [CA-E-378@12](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-378-PROGRAMMATIC-QA_CASE--run-an-installed-tool-without-uv.md) | Run an installed Tool without uv
| Standard | [CA-E-385@11](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-385-PROGRAMMATIC-QA_CASE--verify-changed-python-with-mypy.md) | Verify changed Python with Mypy
| Standard | [CA-E-451@11](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-451-PROGRAMMATIC-QA_CASE--require-a-declared-benefit-for-one-new-python-idiom.md) | Require a declared benefit for one new Python idiom
| Standard | [CA-E-452@13](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-452-PROGRAMMATIC-QA_CASE--verify-one-python-technical-configuration-boundary.md) | Verify one Python technical configuration boundary
| Standard | [CA-E-453@12](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-453-PROGRAMMATIC-QA_CASE--verify-changed-python-with-ruff.md) | Verify changed Python with Ruff
| Standard | [CA-E-454@10](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-454-PROGRAMMATIC-QA_CASE--use-one-settings-reader-across-engine-software.md) | Use one Settings Reader across Engine software
| Standard | [CA-E-467@8](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-467-PROGRAMMATIC-QA_CASE--reject-temporary-state-outside-project-temp.md) | Reject temporary state outside project temp
| Standard | [CA-E-641@6](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-641-PROGRAMMATIC-STANDARD-EVAL_APPROACH--check-shared-runtime-routing-and-state-isolation.md) | Check shared-runtime routing and Project state isolation
| Standard | [CA-E-649@3](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-649-PROGRAMMATIC-STANDARD-EVAL_APPROACH--verify-initiative-binding-before-mutation.md) | Verify initiative binding before mutation
| Standard | [CA-E-650@4](../../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-650-PROGRAMMATIC-STANDARD-EVAL_APPROACH--verify-active-native-tool-frontier.md) | Verify active native Tool frontier

## Declared Method–Evaluation routing

The current [dedicated Method–Evaluation coverage projection](programmatic_method_evaluation_coverage.projection.md) records 39 root Methods, 62 root Evaluations, and direct evaluation_for references for 38 of 39 Methods; CA-M-430 has no direct reference. This is declared-reference routing only, not substantive coverage or acceptance proof. E642 still requires actual substantive per-obligation evidence.
