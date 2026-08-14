# Requirement connections and delta — DSET 0.3

Already accepted behavior is not redefined in this Change. The table connects
the implementation scope to its current layer-owned Requirement owners.

| Capability | Current Requirement owners |
|---|---|
| Framework-first self-hosting and bounded recursion | `CAPRMADIO-REQUIREMENT-OPS-003`, `CAPRMADIO-REQUIREMENT-TOOL-004` |
| Repository-owned rules, fail-closed ownership, customization, and one owner | `CAPRMADIO-REQUIREMENT-GOV-014..017` |
| Separate test/eval proof | `CAPRMADIO-REQUIREMENT-META-007` |
| Thin wrappers, local-rule following, lifecycle-mode entrypoints, runs, budget, continuity, shared runtime, and selectable implementation preparation | `CAPRMADIO-REQUIREMENT-SKILL-002..009`, `CAPRMADIO-REQUIREMENT-SKILL-011`, `CAPRMADIO-REQUIREMENT-SKILL-013` |
| Release transaction, RC/final gate, and coordinated version identity | `CAPRMADIO-REQUIREMENT-OPS-004..007` |
| Intake routing and stable layer-qualified IDs | `CAPRMADIO-REQUIREMENT-GOV-018..019` |
| Neutral repository or Work Area scope | `CAPRMADIO-REQUIREMENT-META-011` |
| Atomic authority, compiled projections, absorption, commit provenance, and session provenance | `CAPRMADIO-REQUIREMENT-GOV-020..022` |
| Governance constitution, dependency/precedence separation, and authority/assurance boundary | `CAPRMADIO-REQUIREMENT-GOV-023` |
| Generated project health and portable Markdown rendering | `CAPRMADIO-REQUIREMENT-GOV-024`, `CAPRMADIO-REQUIREMENT-TOOL-018` |
| Independent external review packet/report and explicit finding reconciliation | `CAPRMADIO-REQUIREMENT-GOV-025` |
| One explicit or inherited priority for every governed artifact | `CAPRMADIO-REQUIREMENT-GOV-026` |
| Workflow-independent Problem, Question, and Conflict semantics | `CAPRMADIO-REQUIREMENT-GOV-027` |
| Recommended optional rationale for Decisions and other atomic artifacts | `CAPRMADIO-REQUIREMENT-GOV-028` |
| Independent MECE artifact classification and Analysis Report boundaries | `CAPRMADIO-REQUIREMENT-GOV-029` |
| Type-first artifact names and independently selectable subtype-name capability | `CAPRMADIO-REQUIREMENT-GOV-038` |
| Medium/high immutable-artifact admission strictness | `CAPRMADIO-REQUIREMENT-GOV-039` |
| Hidden control-plane root, one settings/manifest carrier, distinct ignored runtime state, disposable host scratch, explicit path bases, and direct ownership roots | `CAPRMADIO-REQUIREMENT-GOV-043` |
| Current-only project control plane with inert historical aggregates and completed migrations outside skill discovery | `CAPRMADIO-DECISION-GOV-028` |
| Repository legal files outside `.caprmadio`, with deterministic legal-only provenance resolution | `CAPRMADIO-DECISION-GOV-029` |
| Executable product contracts in TOOL, development realization in IMPL, and post-implementation operation in OPS | `CAPRMADIO-DECISION-GOV-031`, `CAPRMADIO-DECISION-IMPL-001`, `CAPRMADIO-DECISION-OPS-013` |
| Selected Local Python Tools environment, coding, QA-implementation, portability, dry-run, diagnostics, and visible documented-constant rules | `CAPRMADIO-REQUIREMENT-IMPL-001..003` |
| Repository text-byte configuration and portable code/path/Test realization | `CAPRMADIO-DECISION-TOOL-001`, `CAPRMADIO-DECISION-IMPL-002..005` |
| Visibly ordered layer directories with stable logical layer IDs | `CAPRMADIO-REQUIREMENT-GOV-044` |
| Horizontal feature Contracts and forward-only layer authority | `CAPRMADIO-REQUIREMENT-GOV-045` |
| One-level-down project/group/feature/layer architecture views | `CAPRMADIO-REQUIREMENT-GOV-031` |
| Narrowest-common-scope ownership for project, group, feature, and layer truth | `CAPRMADIO-REQUIREMENT-GOV-032` |
| Parent-to-child artifact inheritance, local implementation/cancellation, and direct fallback | `CAPRMADIO-REQUIREMENT-GOV-033` |
| Many-to-many child-owned lineage and derived reverse/transitive traceability | `CAPRMADIO-REQUIREMENT-GOV-034` |
| Six flat Version lifecycle subtypes | `CAPRMADIO-REQUIREMENT-OPS-013` |
| Role-aware handling for every governed conflict pairing, with priority selection only where permitted | `CAPRMADIO-REQUIREMENT-TOOL-019` |
| Evidence-derived TypeScript candidate profile and promotion boundary | `CAPRMADIO-REQUIREMENT-TOOL-021` |
| Framework-reference versus project-applied TypeScript profile authority | `CAPRMADIO-REQUIREMENT-TOOL-022` |

The canonical text lives in the accepted META, GOV, TOOL, SKILL, IMPL, and OPS
evergreen package fragments under `.caprmadio/100_LAYER_1_META/` through
`.caprmadio/600_LAYER_6_OPS/`. This Change
owns implementation and proof for those accepted requirements, not duplicate
normative prose.

Connected accepted IDs are `CAPRMADIO-REQUIREMENT-META-007`,
`CAPRMADIO-REQUIREMENT-META-011`, `CAPRMADIO-REQUIREMENT-TOOL-004`,
`CAPRMADIO-REQUIREMENT-GOV-014`, `CAPRMADIO-REQUIREMENT-GOV-015`,
`CAPRMADIO-REQUIREMENT-GOV-016`, `CAPRMADIO-REQUIREMENT-GOV-017`,
`CAPRMADIO-REQUIREMENT-GOV-018`, `CAPRMADIO-REQUIREMENT-GOV-019`,
`CAPRMADIO-REQUIREMENT-GOV-020`, `CAPRMADIO-REQUIREMENT-GOV-021`,
`CAPRMADIO-REQUIREMENT-GOV-022`, `CAPRMADIO-REQUIREMENT-GOV-023`,
`CAPRMADIO-REQUIREMENT-GOV-024`, `CAPRMADIO-REQUIREMENT-GOV-025`,
`CAPRMADIO-REQUIREMENT-GOV-026`, `CAPRMADIO-REQUIREMENT-GOV-027`,
`CAPRMADIO-REQUIREMENT-GOV-028`,
`CAPRMADIO-REQUIREMENT-GOV-029`,
`CAPRMADIO-REQUIREMENT-GOV-031`, `CAPRMADIO-REQUIREMENT-GOV-038`,
`CAPRMADIO-REQUIREMENT-GOV-039`,
`CAPRMADIO-DECISION-GOV-028`,
`CAPRMADIO-DECISION-GOV-029`,
`CAPRMADIO-DECISION-GOV-031`,
`CAPRMADIO-REQUIREMENT-GOV-043`, `CAPRMADIO-REQUIREMENT-GOV-044`,
`CAPRMADIO-REQUIREMENT-GOV-045`,
`CAPRMADIO-REQUIREMENT-GOV-032`,
`CAPRMADIO-REQUIREMENT-GOV-033`,
`CAPRMADIO-REQUIREMENT-GOV-034`,
`CAPRMADIO-REQUIREMENT-TOOL-018`,
`CAPRMADIO-REQUIREMENT-TOOL-019`,
`CAPRMADIO-REQUIREMENT-TOOL-021`,
`CAPRMADIO-REQUIREMENT-TOOL-022`,
`CAPRMADIO-REQUIREMENT-SKILL-002`, `CAPRMADIO-REQUIREMENT-SKILL-003`,
`CAPRMADIO-REQUIREMENT-SKILL-004`, `CAPRMADIO-REQUIREMENT-SKILL-005`,
`CAPRMADIO-REQUIREMENT-SKILL-006`, `CAPRMADIO-REQUIREMENT-SKILL-007`,
`CAPRMADIO-REQUIREMENT-SKILL-008`, `CAPRMADIO-REQUIREMENT-SKILL-009`,
`CAPRMADIO-REQUIREMENT-SKILL-011`, `CAPRMADIO-REQUIREMENT-SKILL-013`,
`CAPRMADIO-DECISION-TOOL-001`,
`CAPRMADIO-DECISION-IMPL-001`, `CAPRMADIO-DECISION-IMPL-002`,
`CAPRMADIO-DECISION-IMPL-003`, `CAPRMADIO-DECISION-IMPL-004`,
`CAPRMADIO-DECISION-IMPL-005`, `CAPRMADIO-REQUIREMENT-IMPL-001`,
`CAPRMADIO-REQUIREMENT-IMPL-002`, `CAPRMADIO-REQUIREMENT-IMPL-003`,
`CAPRMADIO-DECISION-OPS-013`,
`CAPRMADIO-REQUIREMENT-OPS-003`, `CAPRMADIO-REQUIREMENT-OPS-004`,
`CAPRMADIO-REQUIREMENT-OPS-005`, `CAPRMADIO-REQUIREMENT-OPS-006`,
`CAPRMADIO-REQUIREMENT-OPS-007`, and `CAPRMADIO-REQUIREMENT-OPS-013`.

## ADDED — CAPRMADIO-REQUIREMENT-SKILL-013 Selectable implementation preparation

Public skills accept a desired outcome rather than requiring the operator to
invoke every prerequisite skill manually. Repository-local lifecycle rules own
entry criteria, allowed prerequisite workflows, exit criteria, and stops. Each
transition must satisfy a missing criterion and re-read authority; no progress,
repeated state, cycles, ambiguity, failure, or a new authorization boundary
stops the finite closure.

`.caprmadio/caprmadio_settings.toml` selects `workflows.implement.mode`. Lazy mode invokes
`decisions` first, conditionally prepares separate Test/Evaluation and
implementation plans, and implements only after all entry criteria are
satisfied. Strict mode performs implementation only and stops on missing
accepted prerequisites. Session history is candidate evidence rather than
authority, so reconciliation never invents acceptance or edits immutable atoms.

## ADDED — CAPRMADIO-REQUIREMENT-GOV-029 MECE artifact classification

Every governed carrier must have one primary artifact type and at most one
allowed direct artifact subtype, independently from the four semantic Types.
The project-local artifact-type registry owns the eleven development roles,
their primary questions, direct subtypes, fallback behavior, and path rules.
Analysis Report is non-authoritative and permits Solution Landscape,
Root-Cause Analysis, Proposal, Technical Investigation, and External Audit
Analysis. Unknown, mismatched, nested, missing, or ambiguous classifications
fail closed.

Roadmap, Version Scope, Change, Release Plan, Readiness Record, and Release
Record are direct subtypes of Version and share the `VERSION` identity
sequence for newly emitted carriers.

**Scenario CAPRMADIO-SCENARIO-GOV-030:** A Proposal recommends one candidate; a
separate Decision accepts it; Specification/Design compiles it; Evidence Record
captures a Test run; Verification assesses the evidence; and Readiness Record
makes the explicit release gate disposition without any workflow-derived
reclassification.

## ADDED — CAPRMADIO-REQUIREMENT-GOV-032 Structural-scope ownership

Every claim and compiled artifact belongs to the narrowest common structural
scope containing all affected owners and subjects. Project-level truth owns
only genuinely cross-child or whole-project concerns—shared outcomes and
requirements, Contracts and semantics, end-to-end QA, cross-cutting policy,
integration architecture, release/readiness, and cross-owner unresolved work.
High-level wording does not promote a child-owned claim, and parents link rather
than duplicate child detail.

## ADDED — CAPRMADIO-DECISION-GOV-013 Typed artifact relations

Consequential forward edges use `child_of`, `analysis_of`, `projection_of`,
`implementation_of`, `check_of`, `evidence_for`, `resolution_of`,
`override_of`, `replacement_of`, or fallback `relates_to`. Reverse edges are
derived and never authored. One source-target pair has one primary relation;
`child_of`, scoped `override_of`, and complete `replacement_of` never overlap.

Evergreen `projection_of` normally records one semantic-Type/exact-scope range
through a globally ordered immutable `ATOMIC-RECORD` frontier. A newer
applicable atom makes the projection stale. Sealed legacy `child_of` remains
compatibility input; new artifacts use `relations`.

## ADDED — CAPRMADIO-REQUIREMENT-OPS-012 Integration delivery is the default

Every applicable DSET project must use its configured local integration branch,
remote integration branch, and integration-to-protected release PR as the base
delivery flow. A Change may opt into a separate branch-backed worktree when
parallelism, risk, or conflicting work needs stronger isolation. That branch
must integrate into the configured integration branch before release. Workspace
mode never changes Change identity, scope, authorization, or proof ownership.

**Scenario CAPRMADIO-SCENARIO-OPS-013:** This repository works locally on `dev`,
pushes remote `dev`, and opens PR `dev` to `main`. A parallel high-risk Change
selects `branch-worktree`, reviews that branch into `dev`, and then participates
in the same protected release flow without creating a permanent layer branch.

## ADDED — CAPRMADIO-REQUIREMENT-GOV-020 Artifact roles

DSET must classify durable artifacts as atomic authority sources, evergreen
compiled projections, transactional context/evidence, or implementation-layer
artifacts so reviewers do not confuse rationale, evidence, code, or generated
views with accepted source truth.

**Scenario CAPRMADIO-SCENARIO-GOV-021:** An accepted Decision owns its atomic choice,
the spec and proof plans compile the current consequences, and implementation
cites the Decision without becoming authority. If projection and Decision
differ, the Decision wins and the projection is stale.

## ADDED — CAPRMADIO-REQUIREMENT-GOV-021 Atomic-source compilation

Accepted, active, applicable Requirements, Contracts, Decisions, and other
normative atoms must compile their current behavioral consequences into the
owning evergreen specs, plans, runbooks, or governing rules. Atomic artifacts
are immutable; later state is append-only. A new atom may explicitly and
acyclically absorb older ones while preserving or replacing every applicable
consequence. Only a fully retired atom may move byte-for-byte to `archive/`.

**Scenario CAPRMADIO-SCENARIO-GOV-022:** A resolved Question produces a Decision, the
Decision compiles into the relevant projection, and review rejects a code-only
change that leaves the spec stale. A successor Decision explicitly absorbs its
immutable predecessor rather than winning because it is newer.

## ADDED — CAPRMADIO-REQUIREMENT-GOV-022 Commit and session provenance

Commits that change evergreen truth or implementation artifacts must cite the
Decision or Decisions they implement. A Problem, Question, QA atom, or Change
may be cited as additional provenance but never substitutes for authorizing
Decision authority. Newly emitted atomic artifacts and
append-only lifecycle events expose explicit unique host-prefixed
`llm_session_ids` when an LLM helped produce them, or an explicit empty/`none`
disposition for human-only work. Review, correction, and status changes emit
linked records instead of revising atoms. Missing provenance is invalid. The
rule applies to Changes, intake items, Decisions, promoted proofs, skill-run
records, and session checkpoints.

**Scenario CAPRMADIO-SCENARIO-GOV-023:** A commit body contains
`Implements: CAPRMADIO-DECISION-GOV-001`, and the Decision artifact records the
Codex session IDs that produced or materially revised it.

## ADDED — CAPRMADIO-REQUIREMENT-GOV-023 Governance constitution

`CAPRMADIO-RULE-ARCHITECTURE` remains the sole dependency-free governance root.
Every rule declares separate acyclic dependency and conflict-precedence
relations. Rule authority comes from accepted active atomic sources compiled
into the applicable current local governing document; a mismatch selects the
source and makes the projection stale. Active Decisions explain and authorize
changes, provenance identifies origin, and tests/evals/reviews/evidence assess
assurance without becoming authority.

**Scenario CAPRMADIO-SCENARIO-GOV-024:** A precedence cycle or missing precedence
owner fails closed. Stale evidence leaves the affected assurance claim stale
and blocks its relying gate without silently erasing the applicable rule.
