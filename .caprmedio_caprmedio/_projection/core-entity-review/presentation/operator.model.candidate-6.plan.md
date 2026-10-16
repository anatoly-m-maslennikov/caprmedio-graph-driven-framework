# Candidate #6 — Abstract Core and concrete Project Configuration

Status: implementation plan. The distinction is approved; the Core Atom changes and relocation below are not yet applied.

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
5. **Implementation is deferred:** do not add an Implementation entity anywhere in this candidate. Track old Implementation Subjects separately for later disposition. Deferral does not authorize deleting implementation code or its governing Atoms, nor hiding current source Subjects from the as-is graph.
6. **Agentic Step classification:** use `Step/Execution Kind: Agentic` under the Operations Step path above.
7. **Execution context:** required context belongs to the Step definition; actual supplied context belongs to the Step Run. Classify old context Subjects by the source meaning rather than applying one blanket replacement.
8. **Confidence Threshold precedence:** Settings supplies the default; a Plan can override it; a direct Operator prompt can override it for the Plan. Highest priority is direct prompt, then Plan, then Settings. Do not add another precedence layer or retain the old Hub-chain requirement as an extra layer. This is the threshold, not the Step's actual Confidence.
9. **Remove Activity:** the separate `Activity: Active | Inactive` classification is not needed. Retire that concept and its dedicated rules; remap uses to the appropriate Status only where meanings match. Do not equate every non-Active Status with one invented Inactive Status or delete valid Status rules.
10. **Methodology sources are Scope Units:** Core Meta-model, Extensions and Project Configuration use their existing Scope Units. Their Atoms belong there. Do not add another Methodology Source Object or named Selection just to represent these collections. Preserve the particular Scope Unit identity when mapping references; general meanings still belong in Terms.
11. **Framework Instance uses existing entities:** map `CAPRMEDIO Framework Instance` primarily to Project (Operator's path: `Entity/Continuant/Project`), and to the appropriate Execution where the source means an actual run. Do not add a separate Framework Instance entity. Resolve these uses per Atom rather than making one blanket replacement. This records the current direction; it does not silently rewrite every older Project path in source Atoms.

12. **Execution results belong to History:** records of what happened during any execution, including results, failures and evidence references, belong to History. Journal collects event records but is not mandatory for every historical artifact. Revision preserves earlier state. Authored analysis with rationale/conclusions is an Analysis Atom; compiled views of existing results are Projections. Do not add an Evaluation Report/Proof entity or a new History subtype just for this mapping.

13. **Default Settings carrier:** Default Settings belongs in `project_settings.default.toml`. This supersedes the proposal to merge defaults into Project.Framework Settings. Preserve the distinction between defaults and explicit overrides. The file's location, field migration and actual creation/rename remain implementation work; this decision does not perform them.

14. **Extension metadata and activation:** extension metadata belongs to the extension's existing Scope Unit. Project Settings selects which extensions are enabled. Do not create a separate Installed Extensions Catalog Entry entity. Preserve metadata when remapping; which fields are mandatory is not decided by this ownership change.

These decisions supersede the review proposals to create cross-owner property Selections or an `Object/Implementation` branch. They resolve group policy, not every per-Atom mapping.

## Plan

### 1. Classify the current Core Atoms

- [ ] Use the graph built from current source Subjects, without filtering out unmapped names.
- [ ] Separate project-independent Core rules, all CAPRMEDIO-project-specific definitions and rules, and mixed Atoms. Review every content role, not only Operations.
- [ ] Record each Atom's ID, current owner, proposed owner and reason.
- [ ] Apply the approved group decisions: distinguish exact remapping, obsolete-reference removal, Terms handling, content conflict and deferred Implementation. Do not count a group decision as a completed source migration.
- [ ] Ask unresolved questions one at a time, with source context and a proposed mapping or retirement.

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

- [Candidate #6 recalculated Subject review](../candidate5-migration/next-migration/candidate6-classification/review.md): 511 entries classified; 193 mapped candidates, 80 Terms, 16 removal candidates, 13 deferred, 209 unresolved. This completes inventory triage, not per-occurrence source migration or authoritative adoption.

- [Candidate #5](CA-PROJ-001-CORE_META_MODEL--Entities-Graph-Candidate--Primary-Entities-Candidate-5.md).
- [Current unmapped Subject review](../candidate5-migration/next-migration/subject-review.md).
- [Current source-derived tree](../../core-subject-notation/after-current/inherency.md).

No blanket content migration, automatic retirement, new graph roots, tool redesign, FPF review or release is included.
