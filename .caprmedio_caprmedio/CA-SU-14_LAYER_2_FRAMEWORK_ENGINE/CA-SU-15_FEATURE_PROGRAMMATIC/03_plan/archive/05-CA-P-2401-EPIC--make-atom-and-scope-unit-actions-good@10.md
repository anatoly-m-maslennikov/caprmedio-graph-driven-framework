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
version: 10
updated_at: "2026-10-20T13:51:29.766Z"
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

Use as many Luna workers as the independent ready lanes and available slots support: four historical families, isolated harness, and bounded verification/Concern work when inputs are ready. Respect exclusive write scopes and dependency gates; no filler workers. Each Task owns at most 15 minutes and must split before exceeding that budget. After each completion, review and update dependent next Tasks. These eight actual child Task files declare their direct parent; this list is navigation, not a second authoritative inverse Relation.

- [ ] [CA-P-2402 — Freeze the exact five-day project-session MCP call corpus](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/01-CA-P-2402-TASK--freeze-the-exact-five-day-project-session-mcp-call-corpus.md)
- [ ] [CA-P-2403 — Audit Scope Unit and project_structure validation calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/02-CA-P-2403-TASK--audit-scope-unit-and-project-structure-validation-calls.md)
- [ ] [CA-P-2404 — Audit Atom YAML, body, filename and placement validity calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/03-CA-P-2404-TASK--audit-atom-yaml-body-filename-and-placement-validity-calls.md)
- [ ] [CA-P-2405 — Audit Atom lifecycle and container action calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/04-CA-P-2405-TASK--audit-atom-lifecycle-and-container-action-calls.md)
- [ ] [CA-P-2406 — Audit Scope Unit create, move, rename and update calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/05-CA-P-2406-TASK--audit-scope-unit-create-move-rename-and-update-calls.md)
- [ ] [CA-P-2407 — Register and deduplicate concrete C/Problems](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/06-CA-P-2407-TASK--register-and-deduplicate-concrete-c-problems.md)
- [ ] [CA-P-2408 — Establish and verify the isolated nonproduction MCP harness](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/07-CA-P-2408-TASK--establish-and-verify-the-isolated-nonproduction-mcp-harness.md)
- [ ] [CA-P-2409 — Recheck current concern state and reconcile the planning boundary](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/08-CA-P-2409-TASK--recheck-current-concern-state-and-reconcile-the-planning-boundary.md)

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
