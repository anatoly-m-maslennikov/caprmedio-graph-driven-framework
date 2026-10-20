---
atom_id: CA-P-2401
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Property, Relation, Artifact/Carrier, Project Structure, Tool, Workflow]
relations: {}
version: 20
updated_at: "2026-10-20T17:58:44.616Z"
---
# Summary

Make Atom and Scope Unit Actions Good

## Objective

Make the PROGRAMMATIC Atom and Scope Unit actions complete, coherent and usable through the existing connectors, Workflows and MCP. This Epic records the Operator's decisions from this session; it is not evidence that the implementation already provides them. Its operating-context work now also covers configurable model composition and a shared multi-Project Docker/MCP runtime, with explicit adoption and implementation gates.

## Details

### Agreed PROGRAMMATIC structure

The target structure is:

```text
PROGRAMMATIC
├── TOOLS
│   ├── CONNECTORS
│   └── CAPRMEDIO_TOOLS
├── PROJECT_TOOLS
└── APPS
    ├── WORKFLOW_ORCHESTRATOR
    └── MCP
```

All shown Scope Units are unordered; individual Tool Scope Units belong under the appropriate Tool group.

- TOOLS contains reusable capabilities delivered with the framework, rather than maintenance specific to this repository.
- CONNECTORS contains logical storage access and file/folder mechanics. Backend-specific implementations are adapters within CONNECTORS, not another peer feature group. Connectors do not choose Atom identity, lifecycle or Workflow sequencing.
- CAPRMEDIO_TOOLS contains reusable CAPRMEDIO domain actions, including the Atom and Scope Unit actions in this Epic, usable in any CAPRMEDIO-managed project.
- PROJECT_TOOLS contains only the build, test, release and maintenance operations specific to developing the caprmedio framework repository itself. It is a sibling of TOOLS, not a child of CAPRMEDIO_TOOLS.
- APPS contains WORKFLOW_ORCHESTRATOR and MCP as peers. The orchestrator owns Workflow execution and coordination using Tools. MCP owns discovery and transport for Tools and Workflows; it does not own orchestration or duplicate domain behavior. Preserve other existing Apps; this tree highlights the agreed boundary.

The implementation tasks must reconcile existing TOOLS, CONNECTOR_TOOLS, TOOL_WORKFLOWS, PROJECT_TOOLS, APPS and MCP declarations and contents with this target, reusing capabilities rather than creating duplicate owners. Align applicable RMEDO, project_structure.toml and both governing/delivery bindings during that migration. This Epic update records the target only; it does not itself rename or move folders, change scope declarations, or implement Tools.

### Atom actions

- Find Atoms using filters on any supported Atom property, including nested properties and relations; do not restrict Find to Subjects or a fixed small property whitelist. Validate typed filters and report invalid sources or incomplete coverage rather than silently ignoring them.
- Create any Content Role and applicable Type directly in any status admitted by that Role/Type model, filling and validating all mandatory fields. Do not require intermediate statuses, complete Journal history or retained Draft lineage.
- Update by publishing the next revision file and archiving the exact predecessor. Preserve same identity where current change-classification rules allow it; identity-changing replacement remains distinct. An actual edit advances revision metadata; a no-op does not create a revision or archive.
- Promote ID-free Drafts to Active with a fresh unused identity; no restoration of a previous ID or history/Journal admission gate.
- Cover ordinary file Atoms and folder-backed Plan and Operations containers, including Plan/Epic, Workflow and Step. Preserve exact prior bundles and current container semantics; compose explicitly selected per-Atom operations for bulk work rather than promising a cross-Atom transaction.

### Scope Unit actions

Create, rename, move and delete Scope Units coherently across authoritative project_structure.toml and both declared governing and delivery folder bindings. Preserve references and admitted relative/path semantics, distinguish declaration from intentional non-materialization, and never infer that root delivery and governing places are identical.

Delete must refuse a Scope Unit containing any Atoms or child Scope Units. It must also refuse when either affected folder contains code, other non-Atom files or any other content that would need deletion or preservation. No recursive deletion or removal of a declaration while abandoning nonempty delivery content is authorized. This is the Operator's explicit resolution of the deletion question.

### Validation and reconciliation

Validate YAML syntax, applicable Role/Type keys, mandatory properties and typed values; exact Markdown heading set and order; and coherence among carried properties, filename and actual placement. Validate Project Structure declarations and actual governing/delivery places together, recognizing declared unmaterialized places separately from drift.

Validate registered relation/placement invariants. For example, the current task membership of an Epic's folder must equal its declared direct decomposition membership, applying reserved status-directory and current-revision rules. Use the registered direct relation and derive inverses; do not add a second independent child list, infer Workflow control flow from containment, or count archived predecessor files as extra current members.

Separate mismatch detection from repair. Support three explicitly selected reconciliation policies: files/folders canonical (repair properties and applicable relations), properties canonical (repair filenames and folder placement), or manual (report differences and make no repair). Canonical means the selected repair direction for this mismatch, not permission to bypass validation, invent identity/semantics, overwrite collisions or discard content. Ambiguous or unsafe repairs remain visible without effects.

### Shared design

Reuse the current coherent connector interface and existing storage owners. Keep domain rules in one owner and file/folder mechanics in adapters. Provide one logical property-update entry point whose mapping resolves whether a property is carried in YAML or in its named Markdown section; do not duplicate values or bypass lifecycle/revision rules.

Represent supported schema/declaration data in versioned external files rather than scattered hard-coded property/heading rules. Preserve protected Content Role meanings while allowing the admitted Type, Relation Type and Graph Rule extension points. Choose the format explicitly; JSON is a candidate. External data must retain its governing authority and not become an independent conflicting source. Cover property location, mandatory/allowed keys, values and body layout.

### Current planning checkpoint — 2026-10-20

The agreed topology above is still a migration target, not the observed Project Structure. The current declaration retains CONNECTOR_TOOLS, TOOL_WORKFLOWS and MCP as direct PROGRAMMATIC children; APPS currently declares WORKFLOW_ORCHESTRATOR. Reconcile those declarations with TOOLS/CONNECTORS, TOOLS/CAPRMEDIO_TOOLS and APPS/MCP, preserving existing capabilities and exact history rather than adding duplicate owners. CA-R-1187 already requires MCP and WORKFLOW_ORCHESTRATOR as APPS peers; the declaration mismatch must be resolved before claiming topology completion. Preserve the separate PROJECT_TOOLS boundary. Other Apps, especially GRAPH_UI, remain outside this Epic's implementation scope.

For every affected Scope Unit, reconcile the declared parent, unordered classification, name/prefix and admitted relative governing/delivery bindings with actual carriers and callers. Update applicable ownership/tier metadata only under its current rules. A delivery place is not another Scope Unit. Do not infer the tree from folders or create unused content-role directories. Preserve the distinction between declarations, intentional non-materialization and actual drift.

### Configurable model workstream

Plan PROGRAMMATIC consumption of the protected base meta-model, activated installed Extensions and the selected Project Configuration. Protect Atom identity/meaning, Content Role meanings and source-bound internal/external distinctions. Installed does not mean activated. Expandable Type, Relation Type and Graph Rule declarations may support explicit permitted overrides, but a Draft or lower-tier configuration does not grant permission to replace Core. Resolve any required Core permission and override-precedence decisions through governed source work before activation.

The accepted planning inputs are the following saved Standard Drafts, not Active requirements or implemented capabilities:

- [Model R](../04_requirement/draft/CA-R--PROGRAMMATIC-STANDARD--compose-expandable-and-overridable-model-declarations.md)
- [Model M](../05_method/draft/CA-M--PROGRAMMATIC-STANDARD--resolve-one-provenance-bearing-effective-model.md)
- [Model E](../06_evaluation/draft/CA-E--PROGRAMMATIC-STANDARD-EVALUATION_APPROACH--check-model-extension-override-and-refresh-contracts.md)
- [Model D](../07_delivery/draft/CA-D--PROGRAMMATIC-STANDARD--deliver-model-inputs-effective-generation-and-limits.md)

Choose the supported versioned file format, extension/configuration admission and precedence, composition site and refresh policy before implementation. JSON is a candidate, not an adopted format. Target supported declaration changes without editing code or rebuilding the image; distinguish data changes from unsupported engine-semantic changes. Preserve exact provider/revision/input-digest provenance, one complete effective-model generation per operation and explicit diagnostics for conflicts or invalid/stale refresh. Effective models and graph views remain non-authoritative derived data.

### Shared multi-Project Docker/MCP workstream

Target one running standalone Docker container and one MCP endpoint serving multiple explicitly bound Projects. This replaces neither the existing per-Project baseline nor its deployment until independently implemented and accepted. No Kubernetes dependency or Graph UI work is included.

Use these saved Standard Drafts as planning inputs only:

- [Shared-runtime R](../04_requirement/draft/CA-R--PROGRAMMATIC-STANDARD--serve-multiple-projects-through-one-mcp-runtime.md)
- [Shared-runtime M](../05_method/draft/CA-M--PROGRAMMATIC-STANDARD--bind-caller-context-and-carry-project-identity.md)
- [Shared-runtime E](../06_evaluation/draft/CA-E--PROGRAMMATIC-STANDARD-EVALUATION_APPROACH--check-shared-runtime-routing-and-state-isolation.md)
- [Shared-runtime D](../07_delivery/draft/CA-D--PROGRAMMATIC-STANDARD--deliver-multi-project-mcp-binding-contract.md)

Select request-bound versus connection/session-bound routing and its client protocol. Codex knowing the directory is not transmission to MCP. Bind the authoritative prefix together with validated Project/root/control-root identity and admitted host-to-container mapping; never route or authorize by prefix alone or silently use the process directory. Define registration, ambiguity, rebind, mount-change and drain/removal behavior. Container recreation needed for mounts is distinct from image rebuilding.

Carry the retained binding/model generation through nested and asynchronous work, effects and recovery. Qualify caches, locks, Runs, receipts, Journal/log storage, outputs and record lookup by Project identity so identical local record IDs cannot collide. Preserve current lifecycle authorization and safe effect/recovery checks. Journal recording is not an admission gate; technical/business logs may use their declared local or remote Journal backend. No OS-level isolation between mutually hostile workloads is claimed.

### Approved Draft-format implementation — 20 October 2026

The Operator has authorized implementation after this Epic update. Bind the bounded increment to Core07 originals D288@21, D378@16, D446@16, D276@21, D568@8 and D570@12. Preserve optional ID-free Drafts; support the new-Atom marker `<PREFIX>-<ROLE>-draft`, the proposed-version marker `<canonical-ID>@<version>-draft`, and legacy `<canonical-ID>@draft`. Carried markers must match filenames and remain Draft-only. Version-qualified markers must match the proposed Version. Canonical Current/Archived identity and one-Current uniqueness remain unchanged.

Work packages, each at most 15 minutes of own work per Task: freeze the identity contract; implement parser/Create/Update handling; implement source-pinned Subjects staging/publication compatibility; implement validators and directly consumed authority fixtures; verify functional/golden cases; align Engine RMEDO and C533; independently review integrated evidence. Record each Task separately and review dependent work before execution.

Retain fresh next-unreused identity for ordinary ID-free promotion and the explicitly source-pinned Subjects-only same-ID publication. The Operator has explicitly authorized generic existing-Atom Draft promotion: `CA-R-123@4-draft` updates canonical `CA-R-123` to Version 4 and archives its exact Current predecessor. Bind the exact target and proposed next Version, and refuse stale, mismatched or colliding targets before effects; do not allocate another identity. This is distinct from ordinary ID-free promotion. Do not add Draft relation eligibility, retained-history/Journal gates, a registry, or an executor protocol.

Acceptance requires positive and negative golden cases, exact predecessor preservation, stale/tamper rejection, compatibility, and no canonical number allocation at Draft creation. Tests use synthetic/disposable Projects, never production MCP traffic. Implementation and test evidence do not imply runtime deployment. Excluded: deployment/release, live staging/publication/migration, Methodology 22-source-map repinning, held-batch replay, and other chat-owned Core edits. C533 stays open until implementation and independent review pass.

### Dependency-ordered work packages

These are unchecked planning packages, not newly created child Task Atoms or execution results. Before executing a package, create its own Task/subtask files under this Epic's matching directory; split until each has at most 15 minutes of own work and one observable acceptance condition. Keep registered direct decomposition and actual folder membership synchronized; do not invent a contains list for files that do not exist.

1. [ ] Capture current scope/binding/caller inventory and reconcile the agreed unordered topology and affected RMEDO. Acceptance: one reviewed target mapping with no duplicate owners, plus verified governing/delivery and declaration changes when separately executed.
2. [ ] Resolve model adoption dependencies: protected definitions, Core permission, configurable override surfaces and precedence. Acceptance: explicit source-bound decisions or C/Question holds; no silent adoption of the four Drafts.
3. [ ] Specify model carrier/composition/refresh and its functional acceptance corpus. Acceptance: versioned contract and independent positive/negative golden cases, including inactive providers, conflicting configuration and torn/invalid refresh.
4. [ ] Implement the smallest supported effective-model path against the admitted contracts. Acceptance: exact-input provenance and generation consistency; verify the claimed no-code/no-image-rebuild data-change boundary rather than assume it.
5. [ ] Specify multi-Project client binding, registration, state ownership and Docker mount lifecycle. Acceptance: an explicit supported protocol and two-Project denial/interleaving cases before runtime changes.
6. [ ] Implement shared Docker/MCP routing and Project-scoped dependent execution, reusing the existing orchestrator and Tools. Acceptance: one container/endpoint actually serves two Projects with correct identity and no cross-Project fallback/effects.
7. [ ] Verify the scoped Atom/Scope Unit operations, applicable Workflows and MCP through the delivered Docker path. Acceptance: functional evidence for supported Role/Type/status/container cases and two-Project model/state isolation, identical record IDs, continuation/rebind, refresh/removal and path-escape refusals.
8. [ ] Deliver contracts, operational instructions and attributable acceptance records; perform deployment/release only under separate explicit authorization. Acceptance: actual supported limits and unresolved gaps are visible, without turning projections or test reports into source authority.

After every completed Task/subtask, review and update its dependent successor before execution. Blocked work is postponed and recorded as a C/Problem; unresolved decisions are C/Questions. This Epic update starts none of these packages, promotes none of the eight Drafts and claims no new runtime capability. Prefer cohesive implementation of each R/D in one module/few code units under CA-M-393, without sacrificing complete realization or forcing inappropriate coupling.

### Five-day scoped MCP audit — 2026-10-20

The Operator requested review of project sessions over [2026-10-15 14:13:44 +0400, 2026-10-20 14:13:44 +0400), exactly 120 hours. Read only actual MCP calls and paired results for: (1) Scope Unit/project_structure validation, (2) Atom structure and YAML/body/filename/placement coherence, (3) Atom create/promote/archive/status/update/move including P/O containers, and (4) Scope Unit create/move/rename/other updates. Use all relevant project sessions, not only Luna-authored sessions. Keep expected invalid-input refusals, caller mistakes, manual workarounds, missing coverage and actual defects distinct. Freeze exact call/response IDs, timestamps, target/revision and evidence before drawing conclusions.

Register/reuse concrete C/Problems with historical evidence, then check whether they are still active. Separate historical symptoms from current observations and classify active/resolved/unverified honestly; no false resolution from a plan, a code edit or a local test alone. Search for existing matching Problems before creating duplicates. Uncertain effects are inspected, never replayed. No implementation repair, release or deployment is authorized by this audit.

Hard isolation gate: every MCP reproduction/test must use an isolated nonproduction instance, a distinct verified port, isolated project/root/control-root fixture and state/locks/caches/Runs/receipts/Journal namespace. Use independent golden data rather than mutable production Atoms. Never send test effects to production, stop/reload/restart/redeploy production, reuse its state or fall back to its endpoint. If isolation is unverified, block reproductions and continue safe historical/read-only work. Normal governed record publication is not test traffic.

Use as many Luna workers as the independent ready lanes and available slots support: four historical families, isolated harness, and bounded verification/Concern work when inputs are ready. Respect exclusive write scopes and dependency gates; no filler workers. Each Task owns at most 15 minutes and must split before exceeding that budget. After each completion, review and update dependent next Tasks. These current child Task files declare their direct parent; this list is navigation, not a second authoritative inverse Relation.

- [ ] [CA-P-2402 — Freeze the exact five-day project-session MCP call corpus](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/01-CA-P-2402-TASK--freeze-the-exact-five-day-project-session-mcp-call-corpus.md)
- [ ] [CA-P-2403 — Audit Scope Unit and project_structure validation calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/02-CA-P-2403-TASK--audit-scope-unit-and-project-structure-validation-calls.md)
- [ ] [CA-P-2404 — Audit Atom YAML, body, filename and placement validity calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/03-CA-P-2404-TASK--audit-atom-yaml-body-filename-and-placement-validity-calls.md)
- [ ] [CA-P-2405 — Audit Atom lifecycle and container action calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/04-CA-P-2405-TASK--audit-atom-lifecycle-and-container-action-calls.md)
- [ ] [CA-P-2406 — Audit Scope Unit create, move, rename and update calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/05-CA-P-2406-TASK--audit-scope-unit-create-move-rename-and-update-calls.md)
- [ ] [CA-P-2407 — Register and deduplicate concrete C/Problems](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/06-CA-P-2407-TASK--register-and-deduplicate-concrete-c-problems.md)
- [ ] [CA-P-2408 — Establish and verify the isolated nonproduction MCP harness](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/07-CA-P-2408-TASK--establish-and-verify-the-isolated-nonproduction-mcp-harness.md)
- [ ] [CA-P-2409 — Recheck current concern state and reconcile the planning boundary](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/08-CA-P-2409-TASK--recheck-current-concern-state-and-reconcile-the-planning-boundary.md)
- [ ] [CA-P-2460 — Reconcile the update-atom lifecycle handoff request schema](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/49-CA-P-2460-TASK--reconcile-update-atom-handoff-request-schema.md)

Planning-only manual publication was explicitly authorized because the connected MCP discovery/context reads returned implementation-call failures. Preserve exact v3 history; do not extend that exception to Concern or implementation writes. The audit starts only after this Epic revision and its Task files are saved and checked.

### Delivery plan and execution rules

Align affected project-local, methodology-source and PROGRAMMATIC/connector/Workflow RMEDO before implementing newly decided behavior. Reuse existing capabilities and keep changes bounded; do not reopen settled fresh-ID, optional-history or deletion decisions.

Decompose into separate Task files under this Epic's matching directory, each with an estimated own-work budget of at most 15 minutes and an observable acceptance condition. Split any larger task before execution. After completing each task, review and update dependent next tasks before starting them. Record actual results; a plan or local fixture pass is not implementation or release acceptance.

Use functional/integration/golden-corpus checks as the primary proof, with only narrowly useful unit tests. Test data must be independent from mutable live project Atoms. Include valid Role/Type/status cases, negative validation, predecessor preservation, no-op, P/O containers, arbitrary property filters, relation/folder mismatches, all three repair policies and nonempty deletion refusal.

Creation of this Epic and its task records does not start implementation, a full suite, deployment or a release.

### Definition of Done

False if any scoped Atom or Scope Unit operation, validation invariant or reconciliation policy lacks aligned current contracts and implemented, independently checked functional evidence; or if container/ordinary Atom behavior diverges, predecessor content is lost, empty-only deletion is violated, or required relation/filename/folder/property coherence remains unreported; or the agreed framework/project Tool separation and App hierarchy are not reflected coherently in governing declarations and delivery carriers.

The Epic is also not Done while the agreed topology is unreconciled, model adoption/override permissions are unresolved, or the claimed shared Docker/MCP path lacks attributable two-Project functional evidence and declared operational limits. The eight Drafts and this plan are not that evidence.

### Operator-authorized manual fallback — 2026-10-20

The Operator confirmed the general rule: if MCP cannot do the job, continue manually. This replaces the earlier planning-only manual exception; it is not permission to bypass source/schema rules, overwrite conflicts, fabricate MCP effects or replay uncertain mutations. Preserve actual prior revisions and record actual provenance. Normal MCP authoring remains usable where it succeeds; recovered discovery/context or an outer preview does not prove carrier-admission success. Production MCP test/reproduction traffic remains prohibited.

The reviewed audit Problems are CA-C-525 (current graph-authority pin mismatch), CA-C-526 (historical uncertain CA-P-1959 update) and CA-C-527 (historical interrupted CA-P-1911 status Run). CA-C-528 separately records the current Concern-status authority gap discovered during authoring. They were saved manually after unchanged local full-carrier preflight refused; no create execute or uncertain historical effect was replayed. One current source problem does not establish deployed impact, and historical symptoms remain unverified today. See the Concern records and .caprmedio_tmp/mcp-audit-20261020/report.md.

### Bounded continuation — 2026-10-20

The Operator requested continuation. Tasks CA-P-2420 through CA-P-2424 independently own the two current validator repairs, exact retained-history reconciliation for the two historical symptoms, and isolated functional-check preparation. CA-P-2425 is a dependent current-source runtime acceptance gate; it cannot start from queued work, unreviewed changes or a stale fixture image. This does not authorize production tests/restarts/reloads/deployment or historical mutation replay. Each Task has at most15minutes own work and must be split before extending it.

### Continuation checkpoint and successor review

Tasks2420-2424 completed their bounded source-repair, historical-reconciliation and preparation deliverables; this is not Epic or deployed completion. Concern identity repair passed516validator tests and source-root/D305 repair passed33focused/related tests. Historical CA-P-1959 failure is now precisely a failed preview, with no lasting source change observed at retainedv90; CA-C-526 remains Active for its unexplained failure, not as an executed mutation claim. CA-P-1911 remains effect-uncertain; CA-C-527 stays Active.

CA-P-2426 found15remaining graph binding drifts, four with changed behavioral sections. New bounded Tasks2427(canonical Concern frozen corpus) and2428(current graph Claim/adapter reconciliation) are prerequisites for reviewed CA-P-2425 isolated acceptance. No automatic pin refresh, production test, deployment or replay is authorized or claimed. The PROGRAMMATIC M projection drove small single-owner changes and frozen functional coverage, not live-corpus tests.

### Current source and runtime checkpoint — 2026-10-20

The earlier15binding-drift statement is catalog-verification evidence, not proof of native admission refusal: current source self-consistency verification does not enforce the manifest expected digest. All26approved graph entries were reconciled only after Claim review. Frozen current graph semantics and canonical Concern/Plan consumers pass their bounded checks; the full validator suite passed525tests before the final Current-target and PlanDraft follow-ups.

The Operator settled any-Content-Role Concern targets; C530 is Resolved and R1022v17 now explicitly requires canonical Current Atom targets (including admitted Done/Canceled/etc, excluding Draft/Archived), with actual affectedness left semantic. P2432 implements this narrow admission; it must not add Journal, retained-review or incoming-link cleanup gates.

New actual child Tasks P2431-P2435 cover frozen graph/status consumers, Concern admission, installedparser diagnosis and DoneTask placement. P2436 reconciles D461PlanDraft placement and its directly broken frozen consumers. P2437 prepares frozen public MCP Concern/Subject regression cases. P2438 builds an immutable reviewed candidate; P2439 executes isolated Docker/MCP proof; P2440 owns separately coordinated deployment after success. Each Task is one file and <=15minutes ownwork; split before extending. CompletedTasks are carried in localdone perD461, exact history preserved.

The installedimagea44ad091 runs older source9fc7a3e and lacks the already-fixed // parser; C532 remains Active until actual deployment proof. The Operator expressly approved replacing the running MCP AFTER isolatedtests pass, without replaying the stoppedbatch. This does not authorize production test traffic or replay/reset/cancel of the inspection-required stage. The only existing canonical replacement flow also commits all checkout changes and runs a full localrelease. The Operator separately expressly approved that full flow, including otherchat current changes, AFTER isolatedtests pass. Coordinate source/Git freeze before starting; approval is not an execution receipt. Epic remains Active; existing historical C526/C527 remain unresolved.


### Reviewed regression and archive-policy checkpoint — 2026-10-20

The final host validator passed 535 tests and frozen Subject notation passed 12. P2441–P2444 completed Current-target identity, qualified Type, inherited Status-base and explicit root Plan-path corrections. These are source/host proofs, not deployed acceptance. The first isolated three-case gate passed all29supported Markdown Role/Status creation pairs but failed Concern creation and errored Subject staging; C540 records the exact receipts. P2445/P2446 narrow fixture preparation and diagnosis do not close P2439. The corrected Subject test connects before client access; the Concern fixture materializes its existing frozen D378 identity authority. Strict validation/effect assertions are unchanged. A fresh immutable image and complete three-case run are required before P2440; no production endpoint or uncertain historical request may be tested/replayed.

The latest Operator decision is flatten archived Plans. D461v15 and E502v13 now place each archived Plan carrier directly in its owning Scope Unit 03_plan/archived folder, without archived parent/child hierarchy. C536 is resolved as a policy question; C539 records separate unimplemented archive-layout work. No physical archive migration, auxiliary-file policy, incoming-link repair or non-Archived status/nesting change is claimed. C533 legacy edit-draft markers, C537 non-ActiveCurrent RMED extension handling and C538 non-Archived suffix validation remain explicit independent limits.

The Methodology source/Git freeze is held for candidate testing and the separately approved full local release. Production replacement and Git checkpointing remain conditional on isolated success; no root Git or production lifecycle effects have occurred at this checkpoint. The Epic remains Active.


### Final isolated acceptance and release handoff

The final selected Docker/MCP gate passed all three tests in 229.835 seconds, with zero failures/errors/skips and protected production equality. Receipt: .caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-1q3i92q7/receipt.json. Candidate image sha256:2c2c218b561ff9868d2e6648c32b6ac0c6bb7df587d340cf6134e54bee03c427; source fingerprint d08ba9be7c5d275a5c72e77c24e8a3994cf63ab194f88ff71a4b2426ee0591e6. Coverage is exactly 29 supported Markdown Role/Status creation pairs, Current Concern targets Active/Done/Canceled, and approved double-slash Subject preview/staging with canonical bytes unchanged. No production endpoint was tested, and the uncertain historical batch was not replayed. Fixture failures were fixed without weakening source validation. P2439 and P2425 may close for this bounded evidence; C540 closes for the corrected fixture failures, not as a production-defect or deployment claim.

The Operator-approved normal full local release is now eligible under the coordinated source/Git/runtime freeze. P2440 remains a separate actual replacement responsibility: require its full suite, source/image provenance and fresh readiness before claiming deployment. The all-current-changes Git checkpoints are expressly approved, but have not occurred at this handoff. Current source fixes do not close installed-runtime Problems until replacement proof. The Epic remains Active for wider Atom/Scope Unit operations, topology, model/shared-runtime adoption and C539 flat nested archival; this selected gate is not that broader acceptance.


### Broad-suite fixture repair and retry gate

The first full local release local-20261020-current-target-parser-repair-1412 made authorized checkpoint c1dfc37e4, then exposed a shared legacy Subject fixture missing frozen base Atom.Status authority R1947 after Plan R1539 inherited it. Root intentionally interrupted the already-failing suite; canonical report records tests/KeyboardInterrupt130, not a completed full-suite result. No copy/install/replacement phase ran. C541 records the fixture cause; the production Status/frontier validators were not weakened. One shared test-helper tuple now also copies R1947. All128 affected host checks passed (66 plus lifecycle48 plus staging14).

Four detached worker/agent test services with the exact owned full-suite attempt label remained. Root verified ownership, stopped only those services, retained their containers/data/images, and reverified original production container432d276a/imagea44ad091/running/127.0.0.1:56317. P2451 closes that bounded manual teardown; C542 remains Active for automatic interruption cleanup. No broad cleanup or production MCP request occurred.

P2452 admitted fresh image sha256:febd5bcc189e3eda2b4926206beb23f26d26c7757092580b0ddf56705ac0aac9 with fingerprint b71c2770aef150235984df90e4e0984e17d2b7e8d7a8169ac8de15b3763a15b8. P2453 repeated all three isolated cases with zero failures/errors/skips in217.438s and exact protected production equality; receipt .caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-e7s6sznn/receipt.json. Reused historical wrapper labels are not new completion claims for earlier Tasks. P2454 is the dependency-reviewed successor for the same expressly approved all-current-changes full local release. Its broad tests and actual replacement/readiness remain required before closing P2440 or installed-runtime Problems. The Epic and broader uncovered operations remain Active.

### Historical second full local-release failure and repair chain — as of 2026-10-20T15:18:47Z

The second full local-release terminal `local-20261020-current-target-parser-repair-1438` failed before replacement. Exact log: `.caprmedio_tmp/simple_local_release/local-20261020-current-target-parser-repair-1438-tests-a71g3vcj.log`; matching report: `runtime/reports/runid.md`. It covered 410 modules and 3555 tests with zero skips and 12 failed modules: nine `VALIDATE_ATOMS` fresh-child import failures and three shared frozen Plan-status mismatches in `test_proposed_relation_admission`, `test_relation_fixture_isolation` and `test_status_bundle_publication_independent`. Root recorded checkpoint `ac1952165`; no replacement phase ran and these results are not production guard failures.

CA-C-543 records the fresh-child runner/import cause and CA-C-544 records the shared frozen-fixture cause. Active repair Tasks CA-P-2455 and CA-P-2456 own those bounded checks. Their Backlog successors are CA-P-2457 (fresh immutable build), CA-P-2458 (three isolated cases with protected production equality) and CA-P-2459 (approved full-local-release retry). CA-P-2454 records the failed retry and delegates to CA-P-2459 without claiming completed delivery; CA-P-2440 now depends on CA-P-2459 and remains unexecuted. Preserve all prior candidate/isolated receipts and historical failure checkpoints. The Epic remains Active; no deployment, release completion or broader capability acceptance is claimed.

### Historical focused repair, fresh build and isolated gate checkpoint — as of 2026-10-20T15:18:47Z

CA-C-543 and CA-C-544 are resolved for their scoped test-environment causes. CA-P-2455 passed runner13/13 and former fresh-child modules133/133 with zero skips and independent review `APPROVE`; CA-P-2456 passed fixture25/25 (relation8, isolation2, status15) plus2 current Plan-placement checks with strict validation and current D461 placement unchanged, no production guard change, and independent review pending. CA-P-2457 then admitted fresh image `sha256:a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3` with fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`; its prelaunch source/image/compose inputs were unchanged, production snapshot equality was true, and independent fixture review was `APPROVE` with no findings.

CA-P-2458 passed the isolated gate in `215.658s`: 3 tests, zero failures/errors/skips, protected production equality true, `production_endpoint_tested: false`, and `historical_replay: false`. CA-P-2459 is now Active and eligible after the required source/Git/runtime freeze, but remains unexecuted. The second full-suite failure and its 410-module/3555-test/12-module boundary remain retained; P2454 and P2440 remain Active. No installed deployment, release completion or Epic completion is claimed.

### Current verified full local release checkpoint — 2026-10-20

The approved release completed successfully. Proof `.caprmedio_tmp/mcp-audit-20261020/continuation/local-release-verified-20261020.json` and canonical receipt `.caprmedio_runtime/simple_local_release/reports/local-20261020-current-target-parser-repair-1521.md` record version `0.4.4.8`, 410 modules, 3680 tests, zero skips/failures and a passing final isolated launcher. The released image is `sha256:a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3` with source fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`; healthy container `b1676bbd01e451f6bf5b32237bdc0d44147dbcc7f9da43638ca8de724a939d44` serves port `56317`, the prior container is absent and its old image was removed by the approved release. Parser `6b377172306c9a6aa662f8436885aeee51922e9980606d08d70b0dc2273c0329` was verified in the released package and container. P2459, P2454 and P2440 are now Done for their bounded release responsibilities; C525, C528, C529, C532, C534 and C535 are Resolved only for their repaired deployment blockers. C539, C542, C545 and other unrepaired or historical concerns remain open. This checkpoint claims neither historical batch replay, public release/merge nor full Atom/Scope Unit, topology, model/shared-runtime or Epic completion.

### Draft implementation execution checkpoint

CA-P-2461 completed source-contract review; dependent Active Tasks CA-P-2462 through CA-P-2465 own parser/Create/Update, Subjects staging, validation/frozen authority and functional/Engine-contract alignment. CA-P-2467 owns the latest same-ID generic promotion decision. CA-P-2466 remains Backlog for independent integrated review after those dependencies. Each is a separate actual Task file, at most 15 minutes own work.

Native Update saved Epic v18 successfully with six terminal Runs. Fresh Task Create Run `candidate6-activation-001-f146b92b0c85551f` interrupted with LifecycleError before any Task carrier was observed; preserve its inspect-or-recover-only evidence at `.caprmedio_tmp/draft-format-implementation-20261020/tasks/step-1/dispatch.json`. The batch stopped. All seven Task records were then saved under the Operator-authorized manual fallback, after verifying their destinations absent. No failed Run or held batch was replayed. This checkpoint is planning/execution attribution, not implementation acceptance.

### Marker promotion completion decisions and task split

The Operator has now explicitly confirmed both remaining marker rules: a new-Atom role-only marker such as `CA-R-draft` promotes with a fresh canonical ID; compatible `CA-R-123@draft` promotes to the same canonical Atom using the explicitly supplied proposed Version. Qualified `CA-R-123@4-draft` remains same-ID promotion with exact Current predecessor preservation. ID-free promotion remains fresh-ID. Require exact target/source and canonical predecessor bindings; do not infer a target from a nonunique marker.

Original Core D446@17 is published and independently checked (SHA-256 `189cc02e8a9e085d4e49bc59148bfc013d64ad14d660bc48c17fa66a86272d5c`); its qualified-marker rule requires Current+1 for an actual change and no Version/time/archive churn for an exact no-op. The other two defaults above are explicit Operator/Engine decisions, not an inference from that Core rule's scope. Other five pinned Core originals are unchanged.

P2467 is split into actual child Tasks P2468 (binding/preflight), P2469 (shared safe publication), and P2470 (both-entry acceptance), each at most 15 minutes own work, with dependent review before execution. Parser and validator lanes produced bounded positive evidence; full integrated acceptance still depends on promotion and frozen fixture closure completion. Source/RMEDO alignment is prepared; no deployment or held-Draft publication is implied.

The earlier Task Create interruption was independently attributed to the caller's Done Plan path outside its required done/ folder. The corrected planning carrier is under done/. No product defect is inferred; the interrupted Run remains inspect-only, with no replay.
