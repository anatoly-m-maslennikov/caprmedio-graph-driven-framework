# Candidate #6 — Abstract Core and concrete Project Configuration

Status: reconciled candidate and implementation plan, partially applied. On 2026-10-16, the supported Subjects-only batch updated 198 source Atoms. Content changes, missing R definitions and Core/Project Configuration relocation remain pending.

## Decision

Core Meta-model defines what a Workflow, Step or Action is.
Project Configuration defines the project's actual Workflows, Steps and Actions.

Core is abstract: reusable kinds, properties, relations and constraints.
Project Configuration is concrete: project-specific definitions, rules and choices within the Core's expansion boundaries.

Everything specific to the CAPRMEDIO project belongs in Project Configuration—not only named Operations. This includes Applicable Methodology and its project-specific definitions, compilation rules, Requirements, Methods, Evaluations and Delivery rules. Calling a rule abstract or reusable does not make it Core if it still depends on a CAPRMEDIO-project-specific concept.

The definition of Project Configuration belongs in Core. Its actual contents do not.

Examples:

| Core Meta-model | Project Configuration |
| --- | --- |
| What a Workflow is | The Applicable Methodology compilation Workflow |
| What a Step is and how it connects to an Action | That Workflow's Select, Assess and Publish Steps |
| What an Action is | A named Action used by those Steps |
| What a Projection is and its general rules | Applicable Methodology, its compilation rules and procedure |

Concrete definitions remain Atoms. Their names identify instances, not new abstract entity kinds. Shared Actions stay shared; moving a Workflow must not duplicate them.

Definitions are not executions. Workflow, Step and Action definitions are Continuants. Their actual runs are Occurrents. Journal records describe what happened; they are not the executions themselves.

## Keep these distinctions

- Local Tier `Core` is not the `CORE_META_MODEL` source layer. Project Configuration can contain its own Core-tier rules.
- Project Configuration rules are not current Settings values. Do not duplicate Settings in configuration Atoms.
- Only project-independent rules stay in Core. Applicable Methodology rules belong in Project Configuration, including rules that are general within that project-specific mechanism. Mixed Atoms need separation; do not invent broader Core rules merely to keep them there.
- A Subject describing a general kind and a Subject selecting one named instance are not interchangeable. Preserve instance applicability when migrating.
- Candidate #5's agreed hierarchy remains the starting point. This plan adds no new root entities.

Generic operation Subjects:

```text
Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow
Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step
Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action
```

Run Subjects:

```text
Entity/Occurrent/Execution/Workflow Run
Entity/Occurrent/Execution/Step Run
Entity/Occurrent/Execution/Action Run
```

Separately approved: `Atom/Revision` → `Entity/Continuant/History/Revision`. Longer old Revision paths still need their own mapping decisions.

Approved mapping: `AI Agent Confidence` → `Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step/Execution Kind: Agentic.Confidence`. Confidence belongs to Agentic Step, not to Execution generally.

Approved mapping: `AI Agent Delegation` → `Entity/Continuant/Actor/Type: AI Agent.Permissions`. Keep the permission limits and granting Operator; do not create a separate Delegation entity. This mapping is recorded for migration, not yet applied.

## Approved group decisions

1. **Old Artifact / Structural Entity partition:** remap uses to the agreed model where possible. If a use cannot be remapped, remove the obsolete category or reference. Do not preserve the old partition by inventing replacement roots. Record each disposition; this is not permission to delete whole Atoms containing still-valid rules.
2. **RMED governs the thing:** all RMED Subjects name what the rule governs, not an invented procedure entity. For example, M with Subject `Atom.Substance` specifies how to write Substance; E specifies how to check it; D specifies how to store it. R specifies required outcomes. Operations selects and uses these rules to arrange actions in sequence; it does not duplicate or reinvent RMED.
3. **Shared meanings belong to Terms:** general meanings across owners, such as Status, Type or Property, belong in the Terms graph/branch. Do not add entity nodes or named Selections merely to represent those shared meanings. Actual owner-qualified properties remain in the entity model. Terms definitions remain derived from source usage and Semantics, not a new authoritative definition layer.
4. **Remove vague topic dependencies:** replace tags such as `atom-boundary`, `relation-model` and `scope-topology` with evidenced precise Subjects. Remove redundant or unsupported topic links instead of inventing entities to preserve them. Do not invent a precise dependency where the source supplies none.
5. **Implementation is deferred:** do not add a separate Implementation entity anywhere in this candidate. Track old Implementation Subjects separately for later disposition. This does not defer the Method Atom Types confirmed in decision 25. Deferral does not authorize deleting implementation code or its governing Atoms, nor hiding current source Subjects from the as-is graph.
6. **Agentic Step classification:** use `Step/Execution Kind: Agentic` under the Operations Step path above.
7. **Execution context:** required context belongs to the Step definition; actual supplied context belongs to the Step Run. Classify old context Subjects by the source meaning rather than applying one blanket replacement.
8. **Confidence Threshold precedence:** Settings supplies the default; a Plan can override it; a direct Operator prompt can override it for the Plan. Highest priority is direct prompt, then Plan, then Settings. Do not add another precedence layer or retain the old Hub-chain requirement as an extra layer. This is the threshold, not the Step's actual Confidence.
9. **Remove Activity:** the separate `Activity: Active | Inactive` classification is not needed. Retire that concept and its dedicated rules; remap uses to the appropriate Status only where meanings match. Do not equate every non-Active Status with one invented Inactive Status or delete valid Status rules.
10. **Methodology sources are Scope Units:** Core Meta-model, Extensions and Project Configuration use their existing Scope Units. Their Atoms belong there. Do not add another Methodology Source Object or named Selection just to represent these collections. Preserve the particular Scope Unit identity when mapping references; general meanings still belong in Terms.
11. **Framework Instance uses existing entities:** map `CAPRMEDIO Framework Instance` primarily to Project (Operator's path: `Entity/Continuant/Project`), and to the appropriate Execution where the source means an actual run. Do not add a separate Framework Instance entity. Resolve these uses per Atom rather than making one blanket replacement. This is the candidate's canonical Project path, superseding Candidate #5's `Object/Project` placement; source paths remain unchanged until migration.

12. **Execution results belong to History:** records of what happened during any execution, including results, failures and evidence references, belong to History. Journal collects event records but is not mandatory for every historical artifact. Revision preserves earlier state. Authored analysis with rationale/conclusions is an Analysis Atom; compiled views of existing results are Projections. Do not add an Evaluation Report/Proof entity or a new History subtype just for this mapping.

13. **Default Settings carrier:** Default Settings belongs in `project_settings.default.toml`. This supersedes the proposal to merge defaults into Project.Framework Settings. Preserve the distinction between defaults and explicit overrides. The file's location, field migration and actual creation/rename remain implementation work; this decision does not perform them.

14. **Extension metadata:** extension metadata belongs to the extension's existing Scope Unit. Do not create a separate Installed Extensions Catalog Entry entity. Preserve metadata when remapping; which fields are mandatory is not decided by this ownership change. The earlier separate Settings-enablement proposal is superseded by decision 23.

15. **Goals and Demands use existing scope references:** Consumer Goal / Producer Result is old notation, not additional entities. Goals and Demands use Owning Scope Unit and Target Scope Unit. Substance states the required result; Substance Scope limits its exact applicability. For a Demand, the owning Scope Unit is the consumer and the target Scope Unit is the producer. Do not confuse a result with its whole Scope Unit or require a separate P objective merely to express a Demand.

16. **Drop Exploration Mode:** remove the separate mode concept and mode-specific rules. Do not introduce a replacement mode, field or mandatory replacement Atom. Discussion versus authorization remains governed by existing permission rules.

17. **Keep the operation model small:** use Workflows, Steps, nested substeps and Actions. These can represent tool operations and prompts given to the calling session; do not add another Invocation/Tool Call entity layer. Actual executions use the existing Runs; records belong to History. The main session may optionally submit another MCP call. Do not infer an automatic continuation, mandatory callback, new lifecycle states or a completion protocol from this decision. Substeps are nested Steps, not an additional root. Decision 24 leaves internal tool-call granularity unspecified by methodology RMED.

18. **Project and framework names are different:** the project is `caprmedio`; its name belongs in Project Settings TOML. The project's result is the framework named `CAPRMEDIO`; that name is defined by a project-local Atom in Project Configuration, not by a universal Core rule. Do not map the framework-name rule to `Project.Name` or duplicate the project-name setting in an Atom. The exact project-local Subject remains mapping work.

19. **Retire Journal Revision:** Journal contains event records with their own timestamps. Retire the separate Journal snapshot/revision concept and archive CA-R-1372 during migration, without a replacement Journal revision or Journal.Updated At rule. This does not remove the existing History/Revision branch or Journal event records. Source retirement has not run.

20. **Projection scope is RMED only for now:** Plan projections are not needed now. Defer Plan Graph mapping/type admission and implementation; do not resume the deferred CONTAINS graph. This does not retire Plan Atoms or their relations, or authorize archiving their governing rules. Existing source Atoms remain unchanged pending later disposition.

21. **Terms Graph is the newer name:** the terminology Catalog/projection and Terms Graph are the same output, not separate kinds. Map M114's `Terminology Projection Derivation` Subject to `Entity/Continuant/Projection/Type: Terms Graph`, following RMED governs the thing. Its obsolete Definition-Atom requirement is a separate content repair: derive meanings from source Atoms and their Semantics under the already-approved model. Do not add another Catalog type for this output. This decision does not retire the generic Catalog type or change source Atoms now.

22. **Scope Unit hierarchy names:** use `Scope Unit.Path`, `Scope Unit.Parent` and `Scope Unit.Children`. Map the old `Structural Path` Subject to `Entity/Continuant/Object/Scope Unit.Path`. Path is the ordered chain from the root Scope Unit to this Scope Unit, derived from parentage—not a filesystem path, separate primary entity or independently authored ancestry. Parent and Children refer to the corresponding Scope Units in the same hierarchy. Source changes remain migration work.

23. **Install Extensions, then regenerate:** put all Atoms of an Extension into `METHODOLOGY_SOURCES/002_INSTALLED_EXTENSIONS`, preserving the Extension's identity, then regenerate Applicable Methodology. This is the current name recorded by Project Structure. Do not require a separate application-binding Atom, target-Scope selection in Settings, or an additional enabled-extension selection layer. This supersedes the earlier activation-selection proposal. Remove CA-R-1733's mandatory application-binding requirement and align contradictory rules in the later content pass; preserve genuine constraints and provenance. No installation or regeneration is performed by saving this candidate.

24. **Do not govern internal tool-call granularity in methodology RMED:** whether an internal tool call becomes a substep or remains an execution detail is not defined here. Remove the corresponding prescriptions in CA-R-1528/CA-M-304 during the content pass; neither require automatic substeps nor forbid them. Do not replace the removed rule with a mandatory configuration option. Preserve the generic operation model and unrelated valid source clauses. No source edit is performed now.

25. **Implementation Method and Implementation Decision are M Types:** retain `Atom/Content Role: Method/Type: Implementation Method` and `Atom/Content Role: Method/Type: Implementation Decision`. Both are Method Atoms and inherit Method/Atom rules; neither is native Implementation or a separate root. Reject the proposal to collapse them into untyped Methods. The existing special Local Tier and parent/child rules are not removed by this naming decision; their content review remains separate.

26. **Types may restrict Local Tier; exact rules are deferred:** a Type may permit only a subset of Local Tiers, including exactly one. Do not require all Types to use unrestricted tier classification. The examples Method Policy → Core and Implementation Decision → Standard illustrate this capability; they are not adopted Type-to-tier constraints. Defining the exact rules, and any additional Type definitions needed for them, remains deferred. Existing source rules stay unchanged meanwhile.

27. **Remove the mandatory Goal connection for Demands:** a Demand does not need an accepted Goal to authorize its required result. Retire CA-R-951's dedicated prerequisite rule and remove that clause from CA-R-933 during content migration, preserving the single-result constraint. Keep the Demand and Goal Types, Owning/Target Scope Unit references and separate Scope Unit Goal-coverage rules. Do not introduce a replacement mandatory link or authorization layer. Source Atoms remain unchanged until migration.

These decisions supersede the review proposals to create cross-owner property Selections or an `Object/Implementation` branch. They resolve group policy, not every per-Atom mapping.

## Effective candidate model

This section applies the decisions above to Candidate #5. Candidate #5 remains the earlier snapshot; where it differs, this section and the approved decisions take precedence. These are candidate definitions, not evidence of live migration.

### Abstract Core

```text
Entity
	Occurrent
		Event
		Execution
			Action Run
			Step Run
			Workflow Run
		Session
	Continuant
		Object
			Atom
			Governing Configuration
			Scope Unit
			Relation
		Project
		Actor
		History
			Revision
			Journal
		Projection
		Selection
		Term
	Carrier
		File Carrier
		Directory Carrier
		Database Carrier
```

This is the backbone, not an exhaustive list of admitted Types. Existing narrower kinds inherit their broader kind's rules. Content Role and Type qualify Atom kinds; Plan labels do not add Types. Method has the distinct Types Implementation Method and Implementation Decision. Types may restrict allowed Local Tiers, including to one tier; the exact restrictions are deferred. Concrete named Operations and project selections are not new Core kinds.

### Dependent names and mapping rules

Display paths below omit the unchanged full prefix. Migration records use full paths.

| Governed thing | Candidate meaning |
| --- | --- |
| `Scope Unit.Path` | Ordered ancestry derived from parentage; not a filesystem path |
| `Scope Unit.Parent`, `Scope Unit.Children` | References within the same Scope Unit hierarchy |
| `Atom.Owning Scope Unit` | Where the Atom belongs |
| `Atom.Target Scope Unit` | Target of a relational Atom, such as a Goal or Demand; a Demand does not require a separate accepted Goal |
| `Atom.Substance Scope` | Exact applicability of its Substance |
| `Atom.Substance` | Shared content field; Claim, question and issue are role-specific labels |
| `Atom/Content Role: Operations/Type: Step/Execution Kind: Agentic.Confidence` | Confidence belongs to the Agentic Step |
| Agentic Step.Execution Context | Required context belongs to the Step; the actual execution-context choice belongs to Step Run.Execution Context. The supplied Invocation Context payload is distinct |
| `Actor/Type: AI Agent.Permissions` | Permission limits, scope and granting Operator; no Delegation entity |
| `History/Revision` | Historical state, not `Atom/Revision` or `Atom.Revision` |
| `History/Journal` | Event records; no separate Journal snapshot/revision concept |
| `Projection/Type: Terms Graph` | Newer name for the terminology projection; meanings derive from source Atoms and Semantics |

RMED governs these things directly: R states required outcomes, M how to produce them, E how to check them, and D how to store or deliver them. Operations arranges actions using RMED. Do not turn authoring, validation, storage or compilation procedure names into extra entities merely to map a Subject.

### Project-specific definitions

- The project is `caprmedio`, named in Project Settings TOML. Its result is the framework `CAPRMEDIO`, named by a project-local Atom. These are not the same Name property.
- Core Meta-model, Extensions and Project Configuration are existing Scope Units. Preserve their identities; do not introduce Methodology Source Objects for them.
- Applicable Methodology and its project-specific rules, concrete Workflows, Steps, substeps and Actions belong in Project Configuration. A generic Core Workflow, Step or Action definition does not describe a particular project procedure.
- A named Operation is identified by its Atom ID under its generic kind. Candidate mapping records may keep the kind and ID separately. This is not a new executable Subject syntax or permission to replace a specific instance with every member of its kind.
- Default Settings belongs in `project_settings.default.toml`. Keep defaults separate from explicit overrides. Confidence-threshold precedence is Settings → Plan → direct Operator prompt, with the later source taking priority.
- Extension metadata belongs to its Scope Unit. Install the Extension's Atoms under `002_INSTALLED_EXTENSIONS` → regenerate Applicable Methodology. No separate application-binding Atom or Settings enablement/application-selection layer.
- Actual runs are Occurrents. Records of results, failures and evidence belong to History; authored analysis remains A, and compiled views remain Projections.

### Removed and deferred concepts

- Retire the obsolete Artifact / Structural Entity partition only where valid meanings cannot be remapped; preserve mixed valid claims.
- Remove Activity, Exploration Mode and unsupported vague topic links. Cross-owner meanings belong to Terms, not extra entity roots.
- Retire Journal Revision and CA-R-1372. Keep History/Revision and Journal event records.
- No extra Invocation or Tool Call entity layer. Use Workflows, Steps/substeps and Actions for definitions, Runs for execution and History for records. Methodology RMED does not prescribe whether internal tool calls become substeps.
- No Implementation branch for now. Current projection work is RMED only; Plan projections and construction/CONTAINS graph implementation remain deferred. This does not remove containment relations or Plan rules.

## Answer application — 2026-10-16

At the answer-reconciliation stage, all 204 remaining review entries were reconciled against the Operator's answers:

- 137 candidate dispositions resolved: 135 mappings and 2 removals.
- 48 required per-occurrence mapping within already-approved distinctions; that review is now complete below.
- 19 need the separate content pass because the old claim conflicts with the accepted model.
- No new Operator questions were found. Ask only if further source inspection reveals a concrete conflict not covered by these answers.

The [combined review map](../candidate5-migration/next-migration/candidate6-classification/review-map.json) records these applications and their remaining work. Compound targets and named instances retain separate kind paths, Atom IDs and source applicability; they are not flattened into one generic Subject. This is candidate data, not a new selector grammar.

Reviewed normalization also uses `Project.Settings` consistently and keeps required execution context distinct from the actual Invocation Context payload.

### Source-occurrence review — complete

The [occurrence report](../candidate5-migration/next-migration/candidate6-classification/occurrence-review.md) covers all 48 source-specific families: 546 Subject/source pairs across 441 current source Atoms, with 548 governs/depends_on uses.

- 314 source-specific mappings and 94 redundant-reference removals.
- 82 uses held for content work; 58 C/A uses left untouched.
- No new Operator questions. Source Atoms remain unchanged.

The six occurrence maps retain exact source paths, roles, targets and evidence. They supersede pending per-occurrence assignments in the earlier review, not the separately deferred content work. If an Atom has any held occurrence, its other mappings do not authorize a partial live update. No new entity kind, selector grammar or live migration is introduced by these records.

## Plan

### Subjects-first execution — 2026-10-16

The Operator requested Subject migration before missing R definitions and content work. This supersedes the earlier execution order for the supported Subjects-only batch, not the remaining model requirements.

- [x] Checkpoint sources and 198 edit drafts; execute the existing MCP batch workflow.
- [x] Apply 198 supported Atom updates, archive exact predecessors and consume edit drafts.
- [x] Verify Subjects-only changes and rebuild the graph from current source Atoms.
- [ ] Resolve the 708 whole-Atom holds; 84 other current Atoms needed no change.

See the [execution result](../candidate5-migration/next-migration/candidate6-execution/result.md) and its exact exclusions. The broader steps below are not complete merely because this supported batch succeeded.

### 1. Classify the current Core Atoms

- [ ] Use the graph built from current source Subjects, without filtering out unmapped names.
- [ ] Separate project-independent Core rules, all CAPRMEDIO-project-specific definitions and rules, and mixed Atoms. Review every content role, not only Operations.
- [ ] Record each Atom's ID, current owner, proposed owner and reason.
- [x] Apply the approved group decisions to the candidate and review map: distinguish candidate remapping, obsolete-reference removal, Terms handling, content conflict and deferred Implementation. This is not a completed source migration.
- [x] Reconcile the currently flagged questions with the Operator's answers. Ask further questions one at a time only if a concrete uncovered conflict appears during remaining source work.
- [x] Review all 48 source-specific Subject families against cited current sources; record mappings, redundant links and whole-Atom holds.

Start with Applicable Methodology: CA-O-011, its Steps CA-O-152–CA-O-157, and related RMED such as CA-R-1316 and CA-E-379. Inspect their referenced Actions and dependencies. Move the project-specific rules too, not only the Workflow. Separate genuinely project-independent claims only where a mixed Atom contains them.

### 2. Put the boundary into authoritative Core Atoms

- [ ] Define Core Meta-model as the abstract, reusable model, not the project's catalogue of concrete procedures.
- [ ] Define Project Configuration as the owner of all project-specific definitions and rules, including Applicable Methodology and named Workflows, Steps and Actions.
- [ ] Review and update existing definitions before adding duplicates: CA-R-1218, CA-R-1207, CA-R-1696 and CA-R-1434.
- [ ] Preserve the distinction already stated by CA-R-1234 between Local Tier Core and the Core Meta-model source layer.
- [ ] Give these rules the correct governing Subjects. Add missing R definitions where needed; empty drafts do not count as definitions.
- [ ] Align directly conflicting M/E/D/O rules only where necessary to apply this boundary.
- [ ] Encode the RMED/O distinction and entity-versus-Term boundary in the relevant Core Atoms; preserve derived Terms authority.
- [ ] Align Step classification/context rules, confidence-threshold precedence and removal of Activity with the approved decisions above.

This is a bounded content change for the Core/configuration boundary. It does not authorize rewriting all Atom content.

### 3. Prepare the source migration

- [ ] For each affected Atom, record its destination Scope Unit, Subject changes, reference changes and disposition.
- [ ] Place all CAPRMEDIO-project-specific definitions and rules under `METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION`, in their appropriate content-role folders and owning scopes.
- [ ] Keep abstract definitions under `METHODOLOGY_SOURCES/001_CORE_META_MODEL`.
- [ ] Split mixed claims only where needed. Preserve reusable Core constraints and rehome the concrete project parts.
- [ ] Preserve identities where the same Atom is moved. Follow the accepted new-ID rule when its Summary changes.
- [ ] Preserve Workflow/Step/Action links and containment. Update affected ownership and carrier references.
- [ ] Keep unresolved mappings explicit. Remove obsolete Artifact / Structural Entity uses only after checking that they cannot be remapped; apply the approved topic-link cleanup without deleting unrelated valid claims.

### 4. Apply the approved changes

- [ ] Use the existing migration and Atom workflows; do not build another migration system.
- [ ] Checkpoint the affected sources, create the proposed drafts, then checkpoint those drafts.
- [ ] On success, archive predecessors and promote or relocate the approved successors. Stop on failure.
- [ ] Apply the approved Revision mapping as part of the mapped Subject changes.
- [ ] Record what actually changed. Do not mark staged or proposed changes as applied.

### 5. Rebuild and check

- [ ] Rebuild the Core and Project Configuration graph views from their current source Atoms.
- [ ] Confirm the Core describes generic Workflow, Step and Action kinds, not named project procedures as additional kinds.
- [ ] Confirm CAPRMEDIO-project-specific definitions and rules, including Applicable Methodology, are actually outside Core, not merely hidden by the renderer.
- [ ] Check moved Atoms' ownership, references and containment.
- [ ] Check that Operations uses RMED rather than restating it, shared meanings are handled by Terms, and no Implementation branch was added.
- [ ] Check R coverage for resulting entities; list remaining gaps and drafts honestly.
- [ ] Keep all remaining unmapped Subjects visible for the next one-by-one review.

## Done when

The distinction exists in authoritative Core Atoms, the reviewed CAPRMEDIO-project-specific definitions and rules have moved to Project Configuration, and rebuilt graphs show the resulting source model without display-only corrections.

Saving this plan alone does not meet that condition.

## Inputs and limits

- [Candidate #6 recalculated Subject review](../candidate5-migration/next-migration/candidate6-classification/review.md): 511 entries classified; 330 mapped candidates, 80 Terms, 20 removal candidates, 14 deferred, 67 source-detail/content tasks. Operator answers are applied to the candidate, not to authoritative sources.

- [Candidate #5](CA-PROJ-001-CORE_META_MODEL--Entities-Graph-Candidate--Primary-Entities-Candidate-5.md).
- [Current unmapped Subject review](../candidate5-migration/next-migration/subject-review.md).
- [Current source-derived tree](../../core-subject-notation/after-current/inherency.md).

No blanket content migration, automatic retirement, new graph roots, tool redesign, FPF review or release is included.
