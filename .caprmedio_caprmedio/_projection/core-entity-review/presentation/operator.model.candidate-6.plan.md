# Candidate #6 — Entity structure, rules and Project Configuration

Status: reconciled candidate and implementation plan, partially applied. The 2026-10-16 Subjects-only batch updated 198 source Atoms. The supported small-structure Subjects-only batch updated 746 source Atoms on 2026-10-19 and passed the pinned post-publication readback. CA-R-655 followed separately as v27 with two verified Subject changes. With explicit Operator approval, the old Object definition R1964 is archived as v3, and the separate Node definition is Active as R1994 v1. Other content changes, remaining R definitions and the unfinished Core/Project Configuration separation remain pending.

Candidate update — 2026-10-18: the structure/rule decisions below supersede the earlier Object partition and proposed separate Node/Relation Definition Types. This update changes this candidate only. Earlier execution records remain historical evidence; they do not prove that these new decisions are applied.

Candidate update — 2026-10-19: the latest Operator decision places Node, Relation, Graph Rule and Carrier directly under Entity. Node has Continuant and Occurrent branches. Node is the logical abstraction; Carrier is its physical storage representation. Graph Rule governs the graph model, not every instruction in RMED. At this update, the small migration was first in CA-P-1959; it did not claim that source Subjects or definitions had already migrated. The later 746-owner batch status is recorded below.

Candidate update — 2026-10-19: the Operator clarified that Artifact is a Term whose meaning is a Node instance delivered or represented through one or more Carrier instances. The 746-owner supported Subject batch is complete; CA-R-655 was excluded pending this clarification, then separately updated to v27. Its two Subject changes, exact predecessor archive, consumed draft and unchanged body passed independent readback. See the [candidate-only decision record](../../../../.caprmedio_tmp/candidate6-artifact-term-20261019/candidate/decision.md), [R655 follow-up readback](../../../../.caprmedio_tmp/candidate6-artifact-term-20261019/review/r655-post-publication-readback.md) and [746-owner readback](../../../../.caprmedio_tmp/candidate6-small-structure-20261019/review/post-publication-readback.md).

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
- Entity remains the single root. Its direct branches are Node, Relation, Graph Rule and Carrier. Node has Continuant and Occurrent branches. This supersedes the earlier placement of Node/Relation/Rule under Continuant and Occurrent directly under Entity; it does not change old execution records.

Generic operation Subjects:

```text
Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow
Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step
Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action
```

Run Subjects:

```text
Entity/Node/Occurrent/Execution/Workflow Run
Entity/Node/Occurrent/Execution/Step Run
Entity/Node/Occurrent/Execution/Action Run
```

Separately approved: `Atom/Revision` → `Entity/Node/Continuant/History/Revision` in the updated candidate. Revision remains under History, not Atom. Longer old Revision paths still need their own mapping decisions.

Approved mapping: `AI Agent Confidence` → `Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step/Execution Kind: Agentic.Confidence`. Confidence belongs to Agentic Step, not to Execution generally.

Approved mapping: `AI Agent Delegation` → `Entity/Node/Continuant/Actor/Type: AI Agent.Permissions`. Keep the permission limits and granting Operator; do not create a separate Delegation entity. This mapping is recorded for migration, not yet applied.

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
11. **Framework Instance uses existing entities:** map `CAPRMEDIO Framework Instance` primarily to Project, and to the appropriate Execution where the source means an actual run. Do not add a separate Framework Instance entity. Resolve these uses per Atom rather than making one blanket replacement. The new canonical candidate path is `Entity/Node/Continuant/Project`, superseding both Candidate #5's `Object/Project` and this plan's earlier direct `Continuant/Project` placement; source paths remain unchanged until migration.

12. **Execution results belong to History:** records of what happened during any execution, including results, failures and evidence references, belong to History. Journal collects event records but is not mandatory for every historical artifact. Revision preserves earlier state. Authored analysis with rationale/conclusions is an Analysis Atom; compiled views of existing results are Projections. Do not add an Evaluation Report/Proof entity or a new History subtype just for this mapping.

13. **Default Settings carrier:** Default Settings belongs in `project_settings.default.toml`. This supersedes the proposal to merge defaults into Project.Framework Settings. Preserve the distinction between defaults and explicit overrides. The file's location, field migration and actual creation/rename remain implementation work; this decision does not perform them.

14. **Extension metadata:** extension metadata belongs to the extension's existing Scope Unit. Do not create a separate Installed Extensions Catalog Entry entity. Preserve metadata when remapping; which fields are mandatory is not decided by this ownership change. The earlier separate Settings-enablement proposal is superseded by decision 23.

15. **Goals and Demands use existing scope references:** Consumer Goal / Producer Result is old notation, not additional entities. Goals and Demands use Owning Scope Unit and Target Scope Unit. Substance states the required result; Substance Scope limits its exact applicability. For a Demand, the owning Scope Unit is the consumer and the target Scope Unit is the producer. Do not confuse a result with its whole Scope Unit or require a separate P objective merely to express a Demand.

16. **Drop Exploration Mode:** remove the separate mode concept and mode-specific rules. Do not introduce a replacement mode, field or mandatory replacement Atom. Discussion versus authorization remains governed by existing permission rules.

17. **Keep the operation model small:** use Workflows, Steps, nested substeps and Actions. These can represent tool operations and prompts given to the calling session; do not add another Invocation/Tool Call entity layer. Actual executions use the existing Runs; records belong to History. The main session may optionally submit another MCP call. Do not infer an automatic continuation, mandatory callback, new lifecycle states or a completion protocol from this decision. Substeps are nested Steps, not an additional root. Decision 24 leaves internal tool-call granularity unspecified by methodology RMED.

18. **Project and framework names are different:** the project is `caprmedio`; its name belongs in Project Settings TOML. The project's result is the framework named `CAPRMEDIO`; that name is defined by a project-local Atom in Project Configuration, not by a universal Core rule. Do not map the framework-name rule to `Project.Name` or duplicate the project-name setting in an Atom. The exact project-local Subject remains mapping work.

19. **Retire Journal Revision:** Journal contains event records with their own timestamps. Retire the separate Journal snapshot/revision concept and archive CA-R-1372 during migration, without a replacement Journal revision or Journal.Updated At rule. This does not remove the existing History/Revision branch or Journal event records. Source retirement has not run.

20. **Projection scope is RMED only for now:** Plan projections are not needed now. Defer Plan Graph mapping/type admission and implementation; do not resume the deferred CONTAINS graph. This does not retire Plan Atoms or their relations, or authorize archiving their governing rules. Existing source Atoms remain unchanged pending later disposition.

21. **Terms Graph is the newer name:** the terminology Catalog/projection and Terms Graph are the same output, not separate kinds. Map M114's `Terminology Projection Derivation` Subject to `Entity/Node/Continuant/Projection/Type: Terms Graph`, following RMED governs the thing. Its obsolete Definition-Atom requirement is a separate content repair: derive meanings from source Atoms and their Semantics under the already-approved model. Do not add another Catalog type for this output. This decision does not retire the generic Catalog type or change source Atoms now.

22. **Scope Unit hierarchy names:** use `Scope Unit.Path`, `Scope Unit.Parent` and `Scope Unit.Children`. Map the old `Structural Path` Subject to `Entity/Node/Continuant/Scope Unit.Path`. Path is the ordered chain from the root Scope Unit to this Scope Unit, derived from parentage—not a filesystem path, separate primary entity or independently authored ancestry. Parent and Children refer to the corresponding Scope Units in the same hierarchy. Source changes remain migration work.

23. **Install Extensions, then regenerate:** put all Atoms of an Extension into `METHODOLOGY_SOURCES/002_INSTALLED_EXTENSIONS`, preserving the Extension's identity, then regenerate Applicable Methodology. This is the current name recorded by Project Structure. Do not require a separate application-binding Atom, target-Scope selection in Settings, or an additional enabled-extension selection layer. This supersedes the earlier activation-selection proposal. Remove CA-R-1733's mandatory application-binding requirement and align contradictory rules in the later content pass; preserve genuine constraints and provenance. No installation or regeneration is performed by saving this candidate.

24. **Do not govern internal tool-call granularity in methodology RMED:** whether an internal tool call becomes a substep or remains an execution detail is not defined here. Remove the corresponding prescriptions in CA-R-1528/CA-M-304 during the content pass; neither require automatic substeps nor forbid them. Do not replace the removed rule with a mandatory configuration option. Preserve the generic operation model and unrelated valid source clauses. No source edit is performed now.

25. **Implementation Method and Implementation Decision are M Types:** retain `Atom/Content Role: Method/Type: Implementation Method` and `Atom/Content Role: Method/Type: Implementation Decision`. Both are Method Atoms and inherit Method/Atom rules; neither is native Implementation or a separate root. Reject the proposal to collapse them into untyped Methods. The existing special Local Tier and parent/child rules are not removed by this naming decision; their content review remains separate.

26. **Types may restrict Local Tier; exact rules are deferred:** a Type may permit only a subset of Local Tiers, including exactly one. Do not require all Types to use unrestricted tier classification. The examples Method Policy → Core and Implementation Decision → Standard illustrate this capability; they are not adopted Type-to-tier constraints. Defining the exact rules, and any additional Type definitions needed for them, remains deferred. Existing source rules stay unchanged meanwhile.

27. **Remove the mandatory Goal connection for Demands:** a Demand does not need an accepted Goal to authorize its required result. Retire CA-R-951's dedicated prerequisite rule and remove that clause from CA-R-933 during content migration, preserving the single-result constraint. Keep the Demand and Goal Types, Owning/Target Scope Unit references and separate Scope Unit Goal-coverage rules. Do not introduce a replacement mandatory link or authorization layer. Source Atoms remain unchanged until migration.

28. **Governance Origin is Internal or External:** reuse CA-R-1709 rather than adding a second definition under the old name Governance Locus. Relational is not a third value. Container nodes use the separately defined containment capability and CONTAINS relations. This does not remove the already retained Owning/Target Scope Unit references for Goals and Demands. Source-content alignment remains separate.

29. **Metadata fields and content sections represent properties:** Atom.Status, Atom.Substance and Atom.Semantics are dependent properties of the Atom. Their bearer relation is IS_BORNE_BY. YAML fields and Markdown sections are different representations inside the same File Carrier; D defines that representation. M governs how content is written, not whether Semantics is a property. Keep Semantics as a meaning-specific content section. Do not add an extra Atom.Property field or container for all properties; retain that old placeholder only as superseded review material. This does not make every property mandatory or introduce a separate Carrier entity for each field or section.

30. **Drop Carrier.Ownership Class:** do not admit this generic property or its proposed Framework-Owned / Project-Owned / Runtime State values. They mix ownership with storage purpose. Retain the empty placeholder only as superseded review material. Review actual project-specific storage rules separately in Project Configuration during content migration; do not delete useful storage protections or change active CA-D-316 in this candidate-only update.

31. **Drop Carrier.Storage Boundary:** this name labels a storage policy, not a value-bearing property. Do not admit it as a generic property. Preserve CA-D-341's protection against cleanup deleting authoritative content or history, and review its Subject and old ownership terminology during the content pass. Keep the empty placeholder only as superseded review material; active CA-D-341 remains unchanged here.

32. **Structure is not an instance catalogue:** the Entity Graph describes kinds, their properties, allowed values and structural relations. Actual Atoms and other artifacts are instances, not additional kinds. A defining R Atom supplies the definition and provenance; its ID does not automatically become a structural node. Named project instances stay distinct from the structures they use.

33. **Nodes, Relations and Graph Rules:** use `Entity/Node`, `Entity/Relation`, `Entity/Graph Rule` and `Entity/Carrier`. Node is the logical abstraction, with Continuant and Occurrent branches. Graph Rule states conditions governing the graph model, including Nodes, Relations, properties, allowed endpoints and cardinality. A Graph Rule can be expressed by an R Atom without another authoritative instance or file. Ordinary project instructions remain RMED Atom content; they are not automatically Graph Rule instances. Carrier is the actual physical representation in files, directories or database storage, not another copy of the logical Node.

34. **Relation kinds and Relation instances:** a Relation Definition defines a kind such as CONTAINS or IS_BORNE_BY. Each typed connection is a Relation instance, including a structural connection such as `Atom.Status IS_BORNE_BY Atom`. Structural connections belong in the Entity Graph; actual artifact-to-artifact connections belong in the instance graph. A Relation instance does not automatically require its own Atom or file. Its identity is `(source, relation type, target)`, with no separate Relation ID. Its storage remains undecided.

35. **Two Requirement Types:** use `R/Type: Definition` for definitions of Node kinds, Properties and Relation kinds; use `R/Type: Rule` for conditions, permissions, prohibitions and constraints. The Subject identifies what is governed; the Type says whether the Substance defines or constrains it. Do not add separate Node Definition, Property Definition or Relation Definition Types, or a Type for every Continuant branch. These are the two Types for this modeling work, not an automatic retirement of all existing R Types.

36. **Subjects for relation definitions and constraints:** defining CONTAINS itself governs `Relation/Type: CONTAINS`. A Rule about an Atom's outgoing CONTAINS connections governs `Atom.Relations/Type: CONTAINS`; a Plan-specific Rule governs `Atom/Content Role: Plan.Relations/Type: CONTAINS`. Here `/Type` qualifies the Relation entries, not the datatype of the Relations property. Use one precise governs target. Other referenced kinds may appear in depends_on, but dependency links do not encode source/target endpoint roles; those roles belong in the Substance. Semantic Relations are not tied to a YAML field named relations; D defines their carrier.

37. **Machine-readable Substance where useful:** an Atom Type can define structured Substance for formal conditions, including relation endpoint kinds, permissions and cardinality. That structured content is authoritative; readable wording is derived from it, not a second independently maintained Claim. Keep it simple and readable; do not add a general-purpose rule language. Decision 43 supplies the initial whitelist form and endpoint matching. Remaining schema/carrier details, defaults, combination, blacklist precedence and override semantics need definition before implementation. This decision does not make every RMED Atom structured or authorize a new storage field.

38. **Small structure migration first:** put Continuant and Occurrent under Node, retain Relation/Graph Rule/Carrier at Entity's first level, and keep the logical Node distinct from its physical Carrier. A live occurrence is not the persistent record describing it. Other rules—such as how to write code—remain RMED Atom content, optionally compiled into Projections and used by O Workflows. Keep `R/Type: Rule` distinct from the Graph Rule branch; do not globally replace the word Rule. Apply only supported, boundary-aware Subject changes, plus any explicitly necessary direct structural definition alignment, before resuming the older unfinished phases. Broader content migration remains separate. This decision changes no source Atom merely by being recorded here.

39. **Artifact is a Term:** Artifact names the meaning that a Node instance is delivered or represented through one or more Carrier instances. Artifact is not a separate Entity branch, and this does not add an authoritative definition-Atom layer or new Carrier restrictions. Keep a live Occurrent distinct from any persistent record describing it. For CA-R-655, the Subjects-only change is `governs: Entity/Continuant/Node/Atom` → `Entity/Node/Continuant/Atom` and `depends_on: Entity/Continuant/Node` → `Entity/Node`. Its existing Claim, any old `governedArtifact` wording and other content remain for the later content migration. These Subject changes were applied and independently verified in v27; Run `candidate6-artifact-term-r655-20261019-001` completed without recording errors.

40. **Retire old Object and define Node separately:** the Operator explicitly approved archiving CA-R-1964's old Object definition instead of changing its meaning into Node. Its exact v2 is preserved; v3 is Archived and no longer a current original in the canonical Core source set. The fresh CA-R-1994 v1 defines `Entity/Node`: a logical abstraction in the Entity graph, classified as a Continuant or an Occurrent. Its ID, Summary and Claim are separate from the retired Atom. It uses the currently admitted ordinary Requirement format without Type; the planned Definition/Rule Type rollout remains pending. This retires only R1964, not every occurrence of the word Object, and does not create the separate Graph Rule definition.

41. **Define Graph Rule without choosing its implementation:** CA-R-1995 v1 now defines `Entity/Graph Rule` as a condition or constraint on the graph model, concerning Nodes, Relations, their properties, endpoints or cardinality. It uses the current ordinary Requirement format without Type. An ordinary RMED instruction is not automatically a Graph Rule. At creation, the Operator deferred the machine-readable format/defaults/inheritance question and the exact whitelist scope. Decision 43 subsequently resolves the initial whitelist form and endpoint scope; remaining choices stay open. Relation identity is resolved by decision 42. No runtime implementation is claimed.

42. **Relation identity is the tuple:** the Operator confirmed `(source, relation type, target)` as a Relation instance's identity, with no separate Relation ID. This resolves identity only; it does not select a storage format or reopen the deferred Graph Rule decisions.

43. **Whitelist both Relation endpoints:** use the existing Subject notation for allowed source and target kinds, rather than separate `kind` or Content Role selector fields. `applies_to` identifies the Relation Type; `condition` contains both endpoint lists. Both endpoints must match their respective allowed list; narrower kinds inherit membership. This states allowed connections, not required connections, and does not prohibit other Relation Types merely because a Node appears in this whitelist. `type: whitelist` is the structured Graph Rule form, not the containing R Atom's Type. The structured rule is Substance in that R Atom, not a second authoritative instance or file.

```yaml
type: whitelist
applies_to:
  relation_type: evaluation_for
condition:
  source:
    - "Entity/Node/Continuant/Atom/Content Role: Evaluation"
  target:
    - "Entity/Node/Continuant/Atom/Content Role: Requirement"
```

Putting the source only in `applies_to` would restrict checking to that source, without prohibiting other source kinds; both endpoint restrictions therefore belong in `condition`. This is the approved candidate form, not an implemented parser or a migrated source rule. Combining multiple whitelists for the same Relation Type, undeclared Relation Types, other defaults and override/blacklist precedence remain undecided.

44. **Formal Graph Rule model contracts:** a Graph Rule has Type, Applies To, Condition and optional Default Value. Exactly one Type selects its structured condition form: Whitelist, Blacklist, Cardinality, Value Constraint, Topology Constraint or Endpoint Constraint. Mandatory/optional/exact connection counts use minimum and maximum per matching source or target Node, not a graph-wide total. Default Value supplies an absent value without replacing an explicit value, must satisfy applicable constraints and does not itself request a source write. Operative rule content is formal YAML; Summary is the only prose and is not another authority. Different independently replaceable rules, including rules requiring different Types, belong in separate Atoms. The containing R Atom's Type Rule is distinct from the Graph Rule Type in the operative block.

The authoritative model contracts are now R1996 Type, R1997 Applies To, R1998 Condition, R1999 Default Value, R2000 Requirement Type Rule, M394 formal authoring and D637 YAML representation. R1995 v2 and the narrow D479 v10, D495 v7, M111 v29 and M115 v27 updates align the existing definition and prose-layout contracts. The formal exception applies only to R Atoms expressing Graph Rules, not automatically to every R/Type: Rule Atom. Model Definition contracts can retain the current ordinary carrier; the structured rule remains one Claim by meaning. Runtime Type Rule/YAML-body admission and the other Type schemas are not implemented by these source changes. Whitelist combination, unknown Relation Types, blacklist precedence and override policies remain open. No actual formal Rule instances or rule engine were created.

These decisions supersede the review proposals to create cross-owner property Selections or an `Object/Implementation` branch. They resolve group policy, not every per-Atom mapping. Earlier mapping files retain their captured paths until explicitly regenerated for this updated candidate.

## Effective candidate model

This section applies the decisions above to Candidate #5. Candidate #5 remains the earlier snapshot; where it differs, this section and the approved decisions take precedence. These are candidate definitions, not evidence of live migration.

### Abstract Core

```text
Entity
	Node
		Continuant
			Atom
			Governing Configuration
			Scope Unit
			Project
			Actor
			History
				Revision
				Journal
			Projection
			Selection
			Term
		Occurrent
			Event
			Execution
				Action Run
				Step Run
				Workflow Run
			Session
	Relation
	Graph Rule
	Carrier
		File Carrier
		Directory Carrier
		Database Carrier
```

This is the candidate backbone, not an exhaustive list of admitted Types or a current source-derived graph. It shows structure, not actual artifact instances. Properties remain dependent entities, outside this primary-entity tree. Existing narrower kinds inherit their broader kind's rules; specialized kinds may extend allowed values where permitted. Content Role and Type qualify Atom kinds; Plan labels do not add Types. Method has the distinct Types Implementation Method and Implementation Decision. Types may restrict allowed Local Tiers, including to one tier; the exact restrictions are deferred. Concrete named Operations, project selections and individual Rules are not new Core kinds.

### Definitions and Rules

| R Type | Substance |
| --- | --- |
| Definition | What a Node kind, Property or Relation kind means and its structure |
| Rule | Conditions, permissions, prohibitions and constraints on those structures |

Both are actual R Atoms. Defining Rule structure uses Definition; stating a particular constraint uses Rule. Neither requires another authoritative copy of the same content.

Short Subjects below omit the full prefix:

| Purpose | R Type | Governs |
| --- | --- | --- |
| Define Atom.Status | Definition | `Atom.Status` |
| Define CONTAINS | Definition | `Relation/Type: CONTAINS` |
| Constrain Atom containment | Rule | `Atom.Relations/Type: CONTAINS` |
| Constrain Plan containment | Rule | `Atom/Content Role: Plan.Relations/Type: CONTAINS` |

For example, a Rule's structured Substance can identify outgoing direction, allowed source kinds and allowed target kinds. D637 now declares the initial whitelist payload and Summary-plus-YAML carrier; parser/validator support and other Type schemas remain pending. Derive the readable Summary from the operative YAML; do not maintain a second prose condition. R2000 supplies the Rule Type definition, not a completed runtime Type rollout or retyping of existing Atoms.

#### Graph Rule properties

```text
Entity/Graph Rule
	.Type
	.Applies To
	.Condition
	.Default Value (optional)
```

R1996–R1999 define these properties. The formal block uses `type`, `applies_to`, `condition` and optional `default_value` under D637. The selected Graph Rule Type has its own schema; do not invent missing fields or encode free-form prose as an allegedly formal condition. The underlying Atom ID, Status and Version are not duplicated as a second Rule identity.

Containment permissions include Scope Unit → Atom and Container Atom → Atom. An Atom without containment permission cannot contain Atoms; permission does not require children. Role/Type rules refine this, such as Plan → Plan, Workflow → Step and Step → Step. Container Atom remains an Atom. Keep these constraints separate from definitions of Atom and CONTAINS. CONTAINS graph implementation stays deferred.

The whitelist governs both endpoints of its selected Relation Type. Using the registered name `evaluation_for`, its source list can select Evaluation Atoms and its target list Requirement Atoms; both tests must match. This does not forbid an Evaluation's other Relation Types. Multiple-whitelist combination and handling of undeclared Relation Types remain undecided.

### Dependent names and mapping rules

Display paths below omit the full prefix. Logical Node paths start with `Entity/Node/Continuant` or `Entity/Node/Occurrent`; Relation, Graph Rule and Carrier are sibling branches of Node under Entity. Existing migration records retain their captured historical paths until a new migration is actually applied.

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

### Definition draft reconciliation — 2026-10-16

- [x] Reconcile all 54 review placeholders against this candidate and current defining R evidence.
- [x] Prepare 45 minimal definition Claims; retain 2 existing-definition pointers and 7 superseded placeholders without duplicate Claims.
- [x] Resolve Atom.Property and Atom.Semantics: concrete metadata/content properties remain; the aggregate Atom.Property placeholder is superseded.
- [x] Drop Carrier.Ownership Class from the candidate; defer actual storage-rule review to the content migration.
- [x] Drop Carrier.Storage Boundary from the candidate; retain its storage-protection policy for the content pass. All 54 placeholder dispositions are resolved.
- [x] Prepare exact Status, containment, Revision and Carrier source-alignment proposals and a 45-definition inventory in the [admission package](../candidate5-migration/definition-admission/README.md).
- [x] Resolve Local Tiers: 10 Core, 3 General and 32 Standard; update 13 review drafts' metadata only.
- [x] Propose all 45 parent links with applicability evidence and a narrow R796 correction; audit fresh IDs without reserving them.
- [x] Fix local reference lookup and ancestor-parent validation with regression coverage; verify a real Continuant creation preview without publishing it. C/A migration remains deferred.
- [ ] Deploy the local fixes and apply the bounded R796 source correction. Parent proposals, passing previews and unused-ID evidence are not successful admission.
- [ ] Align conflicting source content and admit approved definitions separately. Draft Claims do not close active R coverage.

See the [draft reconciliation](../candidate5-migration/candidate6-definition-drafts.md). No source Atoms were changed by this preparation.

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

- [x] Apply the supported, boundary-aware Subjects-only Node / Relation / Graph Rule / Carrier migration and Node's Continuant/Occurrent structure to 746 Atoms; the exact post-publication readback passed. CA-R-655 was excluded from that batch, then separately updated to v27 with its two approved Subjects and passing independent readback. After the explicit R1964 retirement, eight whole-owner holds remain: CA-O-159, CA-O-160, CA-R-850, CA-E-441, CA-E-446, CA-E-473, CA-M-120 and CA-M-271. Directly affected definition/content work remains separate. Do not duplicate ordinary RMED instructions under Graph Rule.
- [x] Archive old Object definition CA-R-1964 without reinterpreting its Claim; create the independent Core Node definition CA-R-1994, governing `Entity/Node`. Preserve the former's exact history. Other definition gaps remain pending; the separate Graph Rule result follows below.
- [x] Create the plain Core Graph Rule definition CA-R-1995, governing `Entity/Graph Rule`. Its creation completed through the existing workflow; the machine-readable format and whitelist policy remain deferred. This closes this root definition gap only, not all defining-R coverage.
- [ ] Define R Types Definition and Rule, including Property definitions, and reconcile affected existing Types without blanket retirement.
- [ ] Admit the agreed Subject qualification for Relation entries and the whitelist Substance form from decision 43 into the relevant Core rules before implementing them. Resolve only the remaining concrete default, combination and override questions needed for implementation; do not reopen the agreed endpoint scope or narrower-kind membership.
- [ ] Keep structure declarations separate from constraints; derive readable Rule wording from the same structured Substance where that format is adopted.
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

This candidate records the latest Node / Relation / Graph Rule / Carrier organization, its abstraction-versus-storage boundary, and Artifact as a Term meaning. The supported 746-owner Subjects-only migration, separate CA-R-655 v27 follow-up, explicitly approved R1964 retirement, new R1994 Node definition and plain R1995 Graph Rule definition are complete. Remaining content/definition work is still pending. No blanket content migration, automatic retirement, tool redesign, FPF review or release is included.
