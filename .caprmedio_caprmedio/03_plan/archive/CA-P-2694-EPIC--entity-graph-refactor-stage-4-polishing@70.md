---
atom_id: CA-P-2694
label: Epic
status: Active
tier: 3
version: 70
updated_at: 2026-11-05 06:06:44 +0400
subjects:
  active: CAPRMEDIO_MODEL
relations:
  IS_CONTAINED_BY:
    scope_unit: caprmedio
role: Plan
form: Plan
carrier_destination:
  file:
    name: CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing.md
    path: .caprmedio_caprmedio/03_plan
---
## Summary

Entity graph refactor stage 4 — polishing

## Objective

Complete declaration-based Scope Unit authority and the latest MODEL/CFEL content, alias, counterpart, Property and Projection changes. Verify the affected sources, consumers, projections and P2707 integration gates.

## Scope

- Remove the five obsolete authority-mode overrides.
- Promote 44 Declaration Atoms and the shared ordering, Project and identity model. Preserve source history; merge existing model Definitions rather than create duplicates.
- Non-root units have stable IDs. The Project root has no Scope Unit ID; it is Unordered and has no order.number.
- Move and rename existing Authority and Delivery folders to the derived names. Derive Authority and Delivery folder names. Only non-root Authority names include the Scope Unit ID; Project Authority remains .caprmedio_<project name>.
- Retire project_structure.toml as a concept, source file and executable dependency: governing Atoms, readers, row writers, file-only bindings, fixtures and documentation.
- Use Declaration Atoms directly. Do not retain a fallback, generated compatibility TOML or second authored registry.
- Keep existing Scope Unit workflow definitions unchanged. Remove their TOML-specific implementation and executable bindings; do not build replacement Scope Unit tools in this Epic.
- Preserve existing business operations through admitted Atom lifecycle behavior. Do not invent new APIs, approval systems, locks or business rules.

- Keep MODEL entities distinct from their instances. Use the latest Operator decisions when earlier wording conflicts.
- Keep Atom.Header and Atom.Content, an empty Claim container with one or two Formal Claim / Prose Claim children, declared heading interpretation, explicit counterpart identities, aliases, and the removal of the @ reference operator.
- Atom.Header.Container is one mapping with exactly one key: scope_unit for a stable Scope Unit ID, or atom for an Atom ID. Store no Scope Unit name, name suffix or path. Resolve current names and physical destinations from the referenced identity. The Project root ID exception and world bootstrap encoding remain pending. Header.Relations stays optional and carries no duplicate containment fact. Formal Scope Unit parentage remains in its Declaration.
- Retire Substep and make Step recursive: exactly one Action, one Workflow, or one or more contained Steps. Step Run covers Step at every nesting level. Each Step has one Container and its Container chain ends at a Workflow. Preserve the separate actual Workflow-owner migration boundary.
- Runs are not Atoms. Defer Run Properties, including Header, Container and ID. Keep formal containment only: a Step Run has one Workflow Run or Step Run parent; an Action Run launched by a Step Run belongs to that Step Run. Add explicit directional permissions without a general Run root or child-execution-count rule.
- Keep # model / # instances groups and explicit $x bindings. Inherit declared formats without copying local value counts. A present Property has a value and has schema and bearer links.
- Projection identity is Form + Scope Unit. Named Selection remains source information. Terms Graph is deferred by the latest Operator input; Term Definitions and historical projections remain.

## Completed baseline

- P2695–P2706 and P2709 have recorded completed, bounded results. Preserve their history. P2708 owns the separately deferred O016 desired-behavior item.
- The Scope Unit source cutover, TOML retirement, Header/Claim/alias migration, Subject-root migration and CFEL grouping migration have application and preservation evidence.
- The seven published MODEL projections use 1,159 pinned Current suppliers and Project root ownership. The graph reader passed 426 tests; the projection generator passed ten tests. Current admission passed 588 tests. These are focused results, not the final integration gate.
- A 2026-11-05 source census found 46 Current Scope Unit Declarations: one Project root, 45 unique non-root IDs and nine Ordered units. The older 44-source cutover remains historical evidence. One original Declaration is archived and three Workbench Declarations were added; all 43 surviving original Claims and metadata match after the reviewed namespace and Formal Claim wrapping changes. This bounded source snapshot does not close stable-candidate integration.
- The previous Epic version preserves the detailed checkpoint history. The acceptance matrix retains all 23 requirement groups and their evidence. These baselines do not close the remaining gates.

- The Goal/Tier batch has 15 verified source contributions and exact predecessors. Seventeen reviewed Settings contributions merge logical ownership under Project.Settings; 25 ambiguous Settings sources remain held. R2747 and R2748 use fresh IDs because their Summaries changed.
- Source checkpoint a02ac7b83bf4561c7ad18b69ce9b6436dcbb02bf is reported pushed to amm/dev. It includes Goal/Tier, Settings, capability-deferral, containment-permission and refreshed-view source batches. Later code/runtime and fixture repairs remain uncommitted; this checkpoint is not final integration evidence.

- The capability deferral batch preserves confidence constraints in two revised Declarations and retires three redundant Tool/Extension Settings sources. Exact archives and frozen references remain. The refreshed audit reports 56 missing and 23 unresolved Declaration-coverage cases.

## Responsibility and external dependencies

This Epic's source lane owns MODEL, CFEL, Declaration and Atom source decisions, edits, preservation and source-level review. CA #3 owns implementation and runtime changes, fixtures, regression work, and execution of the test and integration gates named below. Those are mandatory external dependencies for closure: do not count source receipts, focused source checks or unrun tests as completed gates, and do not remove them from the Definition of Done. Root coordinates source adoption, projection refresh and acceptance evidence. This plan authorizes no implementation or test execution in the source lane.

The current 11 Occurrent Declaration proposals reflect the settled Operator decisions: retain Execution, Workflow Run, Step Run, Action Run, Runtime, Session and Event; Runtime's four Internal/External Local/Remote variants are relative to the CAPRMEDIO application, and Local means on the Operator's machine; Session is narrower than External Remote Runtime; no Substep Run is added. The remaining source gates are Current pin and consumer reconciliation, endpoint/inverse-permission review, source adoption and faithful projections. Event Record direction and cardinality choices are already recorded; preserve those decisions. Runtime candidates remain unpromoted until those gates pass.


The blocking Relation pair is explicit: IS_BLOCKED_BY is Direct from the dependent Plan to its prerequisite; BLOCKS is the Derived inverse. Store the Direct fact on the dependent Plan. The six-Atom source batch includes endpoint permissions, Delivery, authoring and Evaluation. CA #3 owns conversion of existing prerequisite-side relations.blocks facts to dependent-side relations.IS_BLOCKED_BY facts, preserving their meaning and history.

The Operator excludes Workbench and Workflows from this source lane: their agents own that work. Keep their required Epic gates as external dependencies. Core Occurrent and Relation Declaration sources remain this lane’s responsibility; their prepared Drafts are unpromoted pending source review. Actual Workflow definitions, execution instances and runtime behavior remain with their owners.

Term Definition is now an admitted Method Form under R2765. M450 is the sole Current ID Term meaning owner; exact R2275@2 is retired. Ten of the twelve Entity/Property Drafts remain held for Subject and scope repairs. R1318 is promoted with Term Property-bearing permissions. M451 defines Entity as anything represented in the Subject graph. Relation and Term remain separate from Node and declare their own Property-bearing rules; narrower entities inherit those rules.

## CFEL specification audit

1. Every admitted operator, Relation and expression construct has defining authority.
2. Each Atom governs one actual active Subject; its normative Claims stay within that Subject.
3. Vocabulary and notation are coherent. Keep necessary meaning, constraints and brief Relation Semantics; remove staging notes and redundant rules.
4. Use simple explicit syntax. Resolve ambiguity with the Operator before admission.
5. The Operator selected `::` for allowed values and `{::n}` for allowed cardinalities; Subject `:=` remains unchanged. Review source successors and contextual migration before declaring the new syntax active. `?==` defines a missing effective Property value, `=` tests a condition, and `==` states a required or derived value. The Project confidence default is 90 in the integer range 0..100. Do not infer a Property rename.
6. IF bindings last through the condition and matching THEN group; standalone typed bindings last through the CFEL block. A new binding uses another name.
7. Mixed AND/OR uses parentheses. Quote text when needed; use escaped double quotes and backslashes.
8. Review the full Current CFEL specification census semantically; operator-use scans and hash checks alone do not prove this audit complete.

Workbench and Workflow definitions remain owned by other agents. Their illustrative use in a CFEL example does not exclude the CFEL specification itself from this audit.

## Declarative notation proposal

CA-A-1321@1-draft records the latest design and its open grammar questions. Keep Current syntax until reviewed successor Declarations and migration are ready.

- CFEL states constraints, relationships and required values; Workflows perform changes.
- The Operator accepted `<Node>` for a Model-defined object kind used as a Format.
- The proposed instance forms are anonymous `$<Node>` and named `$x[<Node>]`.
- The proposed `/` means containment and `//` means narrowing. Preserve relationship direction, inherited rules and endpoint count meaning during review.
- Formats combine value domains and conditions, including primitive values. Bound names and quantifiers are logical notation.
- Allowed values use `::`, including `{::n}` bounds; `:=` stays unchanged. A specific Relation participant uses `$x[<Relation>, .Name = IS_PROPERTY_OF]`. These Operator decisions are settled; their defining source revisions and migration remain open.
- `FOR EACH $atom[<Atom>, (conditions)]: (...)` is accepted, without WITH or IN. Its participant is scoped to its selector and grouped body. Formal Claims are self-contained; subjects.active remains the declared focus. R2778@1-draft records the quantifier. Typed Format/binding successors R2248@6 and R2604@4 are created; R2487@14-draft is rebased. Their coordinated review, readback and admission remain required.
- Retain the existing named reverse traversal. No additional compact reverse glyph is required or adopted.
- Container references use IDs only. Scalar Scope Unit.Path Draft R2530@3 is no longer a Container prerequisite and remains separate from this adoption packet. Keep Current Path authority until its independent proposal is resolved.
- Put Project Settings defaults on their Property Declarations with `?==`. Preserve sourced values and validation; retire the old Default Settings Artifact requirements only after dependent source reconciliation. Runtime files stay with their owners.

A narrow Journal source repair is Current as R1644@39; its Claim is unchanged and its undeclared passive History reference is removed. Seven refreshed MODEL views use 1,167 pinned Current sources: 54 missing Declaration cases, 23 unresolved cases and 47 passive-only Subjects. The historical 44-source digest is reproduced from preserved bytes; all 46 Current Declaration pins have a separately verified digest. These source checks do not close the final candidate or external gates.

D264 and D266 remain. Declared Container determines placement; the nearest eligible Directory Carrier reads back the same containment fact. Physical placement and the declared identity must agree; no second authored parent or Carrier graph is added. Earlier retirement and link-removal proposals are superseded.

Five path-notation Drafts are created: R2780@1, R2781@1, R2475@6, R2476@7 and R2617@3. CONTAINS changes its sole alias from `<+` to `/`; IS_CONTAINED_BY keeps `+>`. R2605 instance syntax retirement and R2610 replacement require the common typed-selector and consumer migration.

## Remaining work

1. **Relation permissions.** Verify the adopted outgoing permissions, model/instance scope, endpoint bounds and qualifications against final sources. Retain separate direct/inverse permissions and source-linked unary bounds in projections.
2. **Property contracts and containment.** Resolve the conditional cases from applicable Declarations. Update source and schema authority for the required Atom.Header.Container, optional Header.Relations and retained formal containment Relations; do not duplicate containment in Header.Relations. Verify one formal Container per non-Project Scope Unit and none for the Project root, separately from the mandatory Container of its Declaration Atom. Repair the optional Subjects grouping without weakening Current Active-subject requirements.
3. **MODEL coverage.** Disposition every remaining flag in the latest pinned coverage audit: source correction, declared authority, valid scope, authorized retirement or an Operator decision. The Occurrent hierarchy is settled by the latest Operator decision; finish the reviewed endpoint/inverse-permission and Event Record Relation source gates rather than reopening that decision. Reconcile Settings ownership, preserve operative Claims and exact history, and retain only explicitly authorized deferrals.
4. **Projection identity.** Verify the adopted Form + Scope Unit constraints, required Scope Unit reference and distinct Forms across Delivery, readers, identity checks and published instances. Keep all seven views at the Project root. Preserve versioned source references and the explicit Terms Graph deferral.
5. **CFEL and faithful projections.** Create and review the `::` and `{::n}` source successors, commit their checkpoint, then migrate allowed-value expressions by context while preserving `:=`, YAML and literals. Repair declared narrowing and namespace binding, supported qualified selectors and bindings. Classify remaining opaque expressions; retain their complete source and diagnostics. Rebuild all seven MODEL-only views from actual Current Declarations. Formats, cardinalities and Formal Claims come only from Declarations.
6. **Current carrier admission.** The source lane reconciles live Delivery authority, source closure and Current Atom requirements. CA #3 owns the corresponding registry, validator and runtime implementation, fixtures and execution. Remove dependencies on retired D274 using Current authority; preserve fail-closed checks. Reconcile Header/Claim, role/form, Author removal and required fields with their Current authority before enabling admission. Live admission remains a required external gate.
7. **P2707.** The source lane verifies Current Scope Declaration counts, identities and hashes and explains source-set drift. CA #3 owns code/runtime changes, fixtures and execution of the live Project admission, complete current-source suite, launcher, fresh Docker query/status and W10 lifecycle checks. These required external gates must pass on one stable candidate, with one authoritative result tied to its source, implementation and image identities; focused or mixed-state results do not close them.
8. **Independent closure.** Audit every requirement in the acceptance matrix against live evidence. Verify exact predecessors, metadata/identity rules, actual published projections and the requested remote checkpoint. Mark the Epic Done only after every required item passes or the Operator explicitly changes its scope.

## Decisions and execution

- Ask one question at a time when confidence is below 90%. Record each answer and its affected sources.
- Prepare and review source changes, commit the declaration checkpoint to amm/dev before a dependent mechanical migration, apply the accepted migration in place, then check it. Preserve disabled hooks and concurrent work.
- After the reviewed Container source and schema checkpoint, the source lane owns one mechanical data migration and its preservation evidence. CA #3 owns the implementation, runtime, fixture and test gates; Workbench and Workflow owners retain their files and work.
- Root owns canonical source integration and source commits. CA #3 owns code and test execution. Workers prepare separate source previews and evidence. No release is required. The amm/dev checkpoint, final source push and external verification evidence remain required.

## Definition of Done

1. Every acceptance-matrix requirement has current authoritative evidence. Required MODEL decisions and migration defects are closed.
2. Current Declarations, Relations, Property contracts, Projection identity and affected R/M/E/D are coherent with the latest Operator decisions. Each retained model entity has its applicable defining authority. History is preserved.
3. No live project_structure.toml or production read/write dependency remains. No retired binding or compatibility registry replaces Declaration authority. All Current Scope Declarations and their identities are verified, preserving the original 44-source cutover and explaining later source-set changes.
4. Required source, reader, validator, script, Docker and launcher checks pass on the final candidate. CA #3 owns implementation/runtime changes, fixture and test work, and execution of its P2707 gates; those results remain mandatory external dependencies and are not marked Done by this plan. P2707 must reach Done; the separately owned P2708 disposition is explicit. Focused tests alone do not satisfy this gate.
5. All seven published MODEL views match the final source frontier and their governing Declarations. Unsupported expressions remain complete and explicitly classified.
6. The declaration checkpoint and checked final changes are committed and pushed to amm/dev, with matching local/remote evidence.

## Evidence

- [Full acceptance matrix](../02_analysis/draft/epic-completion-20261104/acceptance/matrix.json).
- [Completion lanes and current findings](../02_analysis/draft/epic-completion-20261104/README.md).
- [P2707 verification task](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/12-CA-P-2707-TASK--verify-declaration-source-cutover.md).
- [Adopted Property and inherited-format batch](../02_analysis/draft/property-instances-20261104/REPORT.md).
- [Earlier Header/Claim/alias stages](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-content-alias-followup-20261103.md).

## Status

Active. Current source and integration gates remain open. Implementation and test execution are external CA #3 dependencies; the 11 Occurrent kind choices are settled, while the reviewed endpoint/Relation source gates and adoption remain open.
