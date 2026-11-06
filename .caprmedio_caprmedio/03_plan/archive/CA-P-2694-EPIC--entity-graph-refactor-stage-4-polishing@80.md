---
atom_id: CA-P-2694
ref_id: CA-P-2694
container:
  scope_unit: CA-SU-00
role: Plan
form: Plan
label: Epic
topics:
  main_subject: CAPRMEDIO_MODEL
tier: 3
status: Active
version: 80
updated_at: 2026-11-06 00:16:44 +0400
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
- Every declared Scope Unit has a stable ID. The CAPRMEDIO Project root receives CA-SU-00. It stays Unordered, has no order.number and no formal parent. CA-SU--1 is the predefined Scope Unit named world, without a Declaration.
- Move and rename existing Authority and Delivery folders to the derived names. Derive Authority and Delivery folder names. Only non-root Authority names include the Scope Unit ID; Project Authority remains .caprmedio_<project name>.
- Retire project_structure.toml as a concept, source file and executable dependency: governing Atoms, readers, row writers, file-only bindings, fixtures and documentation.
- Use Declaration Atoms directly. Do not retain a fallback, generated compatibility TOML or second authored registry.
- Keep existing Scope Unit workflow definitions unchanged. Remove their TOML-specific implementation and executable bindings; do not build replacement Scope Unit tools in this Epic.
- Preserve existing business operations through admitted Atom lifecycle behavior. Do not invent new APIs, approval systems, locks or business rules.

- Keep MODEL entities distinct from their instances. Use the latest Operator decisions when earlier wording conflicts.
- Keep Atom.Header and Atom.Content, an empty Claim container with one or two Formal Claim / Prose Claim children, declared heading interpretation, one canonical Relation Declaration with inverse aliases, and the removal of the @ reference operator.
- Atom.Header.Container is one mapping with exactly one key: scope_unit for a stable Scope Unit ID, or atom for an Atom ID. Store no Scope Unit name, name suffix or path. Resolve current names and physical destinations from the referenced identity. The root Project Declaration Atom uses scope_unit: CA-SU--1. This resolves to predefined world; it is not an unlinked scalar literal. Header.Relations stays optional and carries no duplicate containment fact. Formal Scope Unit parentage remains in its Declaration.
- Retire Substep and make Step recursive: exactly one Action, one Workflow, or one or more contained Steps. Step Run covers Step at every nesting level. Each Step has one Container and its Container chain ends at a Workflow. Preserve the separate actual Workflow-owner migration boundary.
- Runs are not Atoms. Defer Run Properties, including Header, Container and ID. Keep formal containment only: a Step Run has one Workflow Run or Step Run parent; an Action Run launched by a Step Run belongs to that Step Run. Add explicit directional permissions without a general Run root or child-execution-count rule.
- Keep # model / # instances groups and explicit $x bindings. Inherit declared formats without copying local value counts. A present Property has a value and has schema and bearer links.
- Projection identity is Form + Scope Unit. Named Selection remains source information. Terms Graph is deferred by the latest Operator input; Term Definitions and historical projections remain.

## Completed baseline

- P2695–P2706 and P2709 have recorded completed, bounded results. Preserve their history. P2708 owns the separately deferred O016 desired-behavior item.
- The Scope Unit source cutover, TOML retirement, Header/Claim/alias migration, Subject-root migration and CFEL grouping migration have application and preservation evidence.
- The earlier seven-view MODEL projection baseline used 1,159 pinned Current suppliers and Project root ownership. The graph reader passed 426 tests; the projection generator passed ten tests. Current admission passed 588 tests. These are focused results, not the final integration gate.
- A 2026-11-05 source census found 46 Current Scope Unit Declarations: one Project root, 45 unique non-root IDs and nine Ordered units. The older 44-source cutover remains historical evidence. One original Declaration is archived and three Workbench Declarations were added; all 43 surviving original Claims and metadata match after the reviewed namespace and Formal Claim wrapping changes. This bounded source snapshot does not close stable-candidate integration.
- The previous Epic version preserves the detailed checkpoint history. The acceptance matrix retains all 23 requirement groups and their evidence. These baselines do not close the remaining gates.

- The Goal/Tier batch has 15 verified source contributions and exact predecessors. Seventeen reviewed Settings contributions merge logical ownership under Project.Settings; 25 ambiguous Settings sources remain held. R2747 and R2748 use fresh IDs because their Summaries changed.
- Source checkpoint a02ac7b83bf4561c7ad18b69ce9b6436dcbb02bf is reported pushed to amm/dev. It includes Goal/Tier, Settings, capability-deferral, containment-permission and refreshed-view source batches. Later code/runtime and fixture repairs remain uncommitted; this checkpoint is not final integration evidence.

- The capability deferral batch preserves confidence constraints in two revised Declarations and retires three redundant Tool/Extension Settings sources. Exact archives and frozen references remain. That earlier refreshed audit reported 56 missing and 23 unresolved Declaration-coverage cases.

## Responsibility and external dependencies

This Epic's source lane owns MODEL, CFEL, Declaration and Atom source decisions, edits, preservation and source-level review. CA #3 owns implementation and runtime changes, fixtures, regression work, and execution of the test and integration gates named below. Those are mandatory external dependencies for closure: do not count source receipts, focused source checks or unrun tests as completed gates, and do not remove them from the Definition of Done. Root coordinates source adoption, projection refresh and acceptance evidence. This plan authorizes no implementation or test execution in the source lane.

The current 11 Occurrent Declaration proposals reflect the settled Operator decisions: retain Execution, Workflow Run, Step Run, Action Run, Runtime, Session and Event; Runtime's four Internal/External Local/Remote variants are relative to the CAPRMEDIO application, and Local means on the Operator's machine; Session is narrower than External Remote Runtime; no Substep Run is added. The remaining source gates are Current pin and consumer reconciliation, endpoint/inverse-permission review, source adoption and faithful projections. Event Record direction and cardinality choices are already recorded; preserve those decisions. Runtime candidates remain unpromoted until those gates pass.


IS_BLOCKED_BY is canonical from the dependent Plan to its prerequisite; BLOCKS is its inverse alias. Store one canonical fact. The six-Atom source batch includes endpoint permissions, Delivery, authoring and Evaluation. Source migration preserves the meaning of prerequisite-side facts when normalizing their direction; CA #3 receives the checked source handoff for implementation and runtime conformance.

The Operator excludes Workbench and Workflows from this source lane: their agents own that work. Keep their required Epic gates as external dependencies. Core Occurrent and Relation Declaration sources remain this lane’s responsibility; their prepared Drafts are unpromoted pending source review. Actual Workflow definitions, execution instances and runtime behavior remain with their owners.

Term Definition is now an admitted Method Form under R2765. M450 is the sole Current ID Term meaning owner; exact R2275@2 is retired. Ten of the twelve Entity/Property Drafts remain held for Subject and scope repairs. R1318 is promoted with Term Property-bearing permissions. M451 defines Entity as anything represented in the Subject graph. Relation and Term remain separate from Node and declare their own Property-bearing rules; narrower entities inherit those rules.

## CFEL specification audit

1. Every admitted operator, Relation and expression construct has defining authority.
2. Each Atom governs one actual active Subject; its normative Claims stay within that Subject.
3. Vocabulary and notation are coherent. Keep necessary meaning, constraints and brief Relation Semantics; remove staging notes and redundant rules.
4. Use simple explicit syntax. Resolve ambiguity with the Operator before admission.
5. HAS_ALLOWED_VALUE uses `:=`; applicable and inherited admissions combine with OR. HAS_VALUE_CONSTRAINT uses `::`; applicable and inherited constraints combine with AND. Omit an absent allowed-value group. Combine the present groups with AND. Qualified Subjects retain `:=`; allowed cardinalities use `{::n}`. Review the staged successors and migrate by context before activating the new syntax. `?==` defines a missing effective Property value, `=` tests a condition, and `==` states a required or derived value. The Project confidence default is 90 in the integer range 0..100. Do not infer a Property rename.
6. IF bindings last through the condition and matching THEN group; standalone typed bindings last through the CFEL block. A new binding uses another name.
7. Mixed AND/OR uses parentheses. Quote text when needed; use escaped double quotes and backslashes.
8. Review the full Current CFEL specification census semantically; operator-use scans and hash checks alone do not prove this audit complete.

Workbench and Workflow definitions remain owned by other agents. Their illustrative use in a CFEL example does not exclude the CFEL specification itself from this audit.

## Declarative notation proposal

CA-A-1321@1-draft records the settled design and the 49 live successor Drafts. Keep Current syntax until coordinated source adoption and migration are ready.

- CFEL states constraints, relationships and required values; Workflows perform changes.
- The Operator accepted `<Node>` for a Model-defined object kind used as a Format.
- The proposed instance forms are anonymous `$<Node>` and named `$x[<Node>]`.
- The proposed `/` means containment and `//` means narrowing. Preserve relationship direction, inherited rules and endpoint count meaning during review.
- Formats combine value domains and conditions, including primitive values. Bound names and quantifiers are logical notation.
- HAS_ALLOWED_VALUE (`:=`) admits alternatives; HAS_VALUE_CONSTRAINT (`::`) constrains formats and counts. `Name :: [string]{::1}` alone allows one string. Qualified Subjects retain `:=`. A fixed model Relation reference uses `Relation//IS_PROPERTY_OF`; it does not need a `$` binding. Relation data endpoints stay literal or constraint data; they do not create Value Nodes.
- `FOR EACH $atom[<Atom>, (conditions)]: (...)` is accepted, without WITH or IN. Its participant is scoped to its selector and grouped body. Formal Claims are self-contained. The Main Subject identifies their declared focus and supplies no implicit participant. Current metadata still uses subjects.active until the checked rename to topics.main_subject. R2778@1-draft records the quantifier. The final live cohort records the current typed-selector, binding and Rule successors, including R2487@15-draft. Their coordinated admission remains required.
- Retain the existing named reverse traversal. No additional compact reverse glyph is required or adopted.
- Container references use IDs only. Scalar Scope Unit.Path Draft R2530@3 is no longer a Container prerequisite and remains separate from this adoption packet. Keep Current Path authority until its independent proposal is resolved.
- Put Project Settings defaults on their Property Declarations with `?==`. Preserve sourced values and validation; retire the old Default Settings Artifact requirements only after dependent source reconciliation. Runtime files stay with their owners.

A narrow Journal source repair is Current as R1644@39; its Claim is unchanged and its undeclared passive History reference is removed. Seven refreshed MODEL views use 1,167 pinned Current sources: 54 missing Declaration cases, 23 unresolved cases and 47 passive-only Subjects. The historical 44-source digest is reproduced from preserved bytes; all 46 Current Declaration pins have a separately verified digest. These source checks do not close the final candidate or external gates.

The root/bootstrap decisions are settled. Ten native source Draft writes implement them; their Current predecessors are unchanged. The current parser rejects a root ID and identifies root through an absent ID. Promotion must wait for the P2707 reader/model/validator and bootstrap adapter changes. World has no Declaration, Carrier or folder. The seven MODEL views stay pinned to Current suppliers until source adoption.

D264 and D266 remain. Declared Container determines placement; the nearest eligible Directory Carrier reads back the same containment fact. Physical placement and the declared identity must agree; no second authored parent or Carrier graph is added. Earlier retirement and link-removal proposals are superseded.

Five path-notation Drafts are created: R2780@1, R2781@1, R2475@6, R2476@7 and R2617@3. CONTAINS changes its sole alias from `<+` to `/`; IS_CONTAINED_BY keeps `+>`. R2605 instance syntax retirement and R2610 replacement require the common typed-selector and consumer migration.

## Reviewed source checkpoint — 2026-11-05

- Current R1559@28 and E440@38 use the Plan AI confidence threshold and applicable permissions for governing-Atom changes. They retain explicit prohibitions, required approval and re-baselining safeguards.
- Seven published MODEL views use the post-approval frontier of 1,167 Current suppliers. The latest counts remain 54 missing Declarations, 23 unresolved cases, 47 passive-only Subjects, and 252 entities including 48 without defining authority.
- The final CFEL cohort contains 49 live Drafts: 29 language Rules, 14 consumers, four value Relation Declarations and two model Declarations. It removes modeled CFEL Operator introspection; Actor/Operator remains.
- R2826 / R2827 declare HAS_ALLOWED_VALUE and its inverse. R2828 / R2829 declare HAS_VALUE_CONSTRAINT and its inverse. Their old unpromoted IDs were repaired after a concurrent allocation collision; other owners' sources are unchanged.
- Single-person attribution changes remain staged outside the promoted approval pair. Event author Relations are not yet retired. Current root-ID and CFEL sources are unchanged pending coordinated cutover.
- CA #3 owns parser, registry, adapter and runtime compatibility and its verification. This source checkpoint does not establish enforcement.

## Latest CFEL and Relation decisions

- Complete and review CFEL first. Then migrate Current and Draft Atoms mechanically in place. Check the migration before sending the implementation handoff to CA #3.
- Preserve source history and pinned before/after evidence. Keep archive snapshots, Journals and projection snapshots unchanged. Actual Workbench and Workflow work remains with its owners.
- A canonical Relation is stored once. Its reverse name is an inverse alias, without a separate inverse Relation Declaration or a second stored fact. Preserve IS_CONTAINED_BY and IS_BLOCKED_BY as canonical names.
- Declare IS_INVERSE_ALIAS_FOR. Model bindings use fixed references, such as `Relation//CONTAINS ((IS_INVERSE_ALIAS_FOR)) Relation//IS_CONTAINED_BY`. An inverse alias is neither a literal name nor a new Alias kind. Its canonical Relation Declaration owns the binding.
- The Atom model owns storage. Atom.Header.Relations stores outgoing canonical facts about that Atom by default. IS_CONTAINED_BY uses Atom.Header.Container instead. Header.Relations is optional and contains no duplicate containment fact or stored inverse alias. Claims about the active Subject remain distinct from these Atom-level metadata facts.
- Keep actual instances distinct from fixed model references. The broader binding rule and conditional derivations still require final semantic review; do not infer a new all-dollar or no-dollar expression mode.
- Kind alternatives use OR inside one participant selector. VALUES(property) explicitly selects actual direct values. The reviewed VALUES Draft is R2904@1. Earlier 49/55/56-source review counts are bounded checkpoints; the canonical/inverse-alias decision requires a revised final candidate.
- Earlier pure-inverse Declarations, fixed-name dollar rewrites and Direct/Derived classifications are superseded where they conflict with these decisions. Qualified derivations, including IS_DECLARED_BY, need explicit disposition without losing their conditions.

## Declaration Forms and Topic names

- Operator Declaration, Construct Declaration, Relation Declaration and Function Declaration are Forms under Requirement. Their admission Drafts are R2953–R2956; no new Role or ID letter is introduced.
- Each language item has an individual Subject in the MODEL namespace: for example, `CAPRMEDIO_MODEL/CFEL/Operator//Equality` and `CAPRMEDIO_MODEL/CFEL/Construct//Conditional`.
- The reviewed Format, Model Reference and INSTANCE_OF Drafts are R2248@6, R2957@1 and R2476@7. Keep the required definition order: `[]`, then `<>`, then INSTANCE_OF and its Semantics. The broader catalogue and caller review remains open.
- Rename `subjects.active` to `topics.main_subject` and `subjects.passive` to `topics.dependencies`. Main Subject means the one selected Topic. Dependencies retain their direct contextual meaning; incidental mentions are not automatically dependencies.
- Apply these names during the checked in-place Current/Draft migration after CFEL review. The checked metadata rename has since been applied; the Header/Content checkpoint below records current source evidence. Keep unresolved Relation-name and conditional-construct choices explicit.

## Header and Content order — 2026-11-05

- Current R2965 declares IS_ORDERED_RIGHT_AFTER with `<;` and its inverse alias IS_ORDERED_RIGHT_BEFORE with `;>`. Current R2966 declares Header.Ref ID. Current R2967 gives the default for sibling Properties outside either endpoint of an explicit order: last, with unspecified mutual order. Explicit Header and Content order stays in their Declarations.
- Header order is ID, Ref ID, Container, Role, Form, Label, Topics, Tier, Relations, Status, Version, Updated At, Carrier Destination. Other Header fields follow without an imposed mutual order. Relations is optional; each present canonical Relation key uses a nonempty YAML list of base Atom IDs. Scalar/null values and empty lists are rejected by the Delivery rule. Optional empty Properties are omitted.
- The model batch applied 61 checked operations with 33 outputs and 20 exact predecessor snapshots. The ordering pass applied 4,624 stable sources and reconciled 12 concurrent successors; ten Drafts consumed by the other source lane were not restored. An independent fresh census verified all 4,669 live sources have the selected Header order and no empty/null Header Properties.
- Ref ID is base ID for Current, ID@Version for Archived and ID@Version-draft for Draft. The final census has 4,463 formula-matching values and zero mismatches. 206 records remain held for missing or unallocated identity/state: 177 lack explicit ID or Status and 29 have unallocated or invalid IDs. No missing data was invented. Fifty-five legacy Relation-list strings need separate domain review; they were preserved.
- Actual Workflow schema work and anonymous Mermaid Drafts from the other owner were preserved; this ordering change does not promote those schemas. Parser, lifecycle maintenance, projection regeneration and runtime/test gates remain CA #3 dependencies. The full Epic remains Active.
- Evidence: [model/data/ordering packet](../02_analysis/draft/epic-completion-20261104/application/property-order-20261105/README.md), [independent readback](../02_analysis/draft/epic-completion-20261104/permissions/property-order-final-readback-20261105.json), [final Header check](../02_analysis/draft/epic-completion-20261104/coverage/ordered-source-migration-20261105/property-audit/final-header-check.json).

## Ref ID repair — 2026-11-05

- Of the original 206 identity/Status holds, 41 now have formula-valid Ref IDs. Forty existing v1 Drafts received numeric IDs; Workflow Mermaid Draft R2962@1 recovered its recorded identity. Their bodies, Versions and Draft state were preserved; withdrawn proposals remain withdrawn.
- D409 recovered its explicit archived ID. Its Status and Ref ID remain held. Exact filename references and related Markdown targets were repaired without changing frozen evidence.
- The remaining 165 holds comprise 159 missing Status values and six unnumbered Version 2/3 Drafts. Eight of the Status holds also lack independently established IDs. Status defaults and unresolved identity choices await the Operator; no state was guessed.
- Evidence: [repair packet](../02_analysis/draft/epic-completion-20261104/application/ref-id-repair-20261105/README.md), [original-set readback](../02_analysis/draft/epic-completion-20261104/application/ref-id-repair-20261105/progress-readback.json). No promotion or implementation gate is claimed. The Epic remains Active.

## Folder-based Status repair — 2026-11-06

- The Operator confirmed Done, Resolved, Canceled and other non-Active lifecycle states use separate folders. All 159 Status holds are directly in ordinary Role folders. Restored Status Active and added 151 Ref IDs from established base IDs, preserving body, Version and Updated At.
- The original 206-record set now has 192 formula-valid Ref IDs and 14 identity holds: eight Current IDs lacking sufficient identity evidence and six unnumbered Drafts already at Version 2 or 3. No Status holds remain. Identity/version decisions remain open; no Draft was promoted.
- Evidence: [folder Status receipt](../02_analysis/draft/epic-completion-20261104/application/ref-id-repair-20261105/folder-status-application-20261106/adoption-receipt.json), [updated readback](../02_analysis/draft/epic-completion-20261104/application/ref-id-repair-20261105/progress-readback.json). The Epic remains Active; implementation gates remain external dependencies.

## Identity and Status repair complete — 2026-11-06

- All 206 original identity/Status holds now have formula-valid Ref IDs, with zero remaining missing Status values, missing IDs or unallocated Draft-lineage identities in this set.
- The Operator approved fresh IDs for six existing Drafts while preserving their Versions: R2994@2, M498@2, M499@2, E792@2, E793@2 and A1327@3. Their known archived predecessors remain unchanged. Exact filename references and Markdown targets were repaired.
- The Operator approved recovering the final eight Current IDs from filenames after collision checks: C268–C272, D019, D021 and D022. Their body, Version and Updated At were preserved; matching base Ref IDs were added.
- Evidence: [completed repair packet](../02_analysis/draft/epic-completion-20261104/application/ref-id-repair-20261105/README.md), [original-set readback](../02_analysis/draft/epic-completion-20261104/application/ref-id-repair-20261105/progress-readback.json), [independent final check](../02_analysis/draft/epic-completion-20261104/application/ref-id-repair-20261105/verification/final-206-readback-20261106.json). This bounded repair does not imply full schema conformance or a completed Epic. The Epic remains Active; existing implementation gates remain external dependencies.

## Remaining work

1. **Relation permissions.** Verify the adopted outgoing permissions, model/instance scope, endpoint bounds and qualifications against final sources. Retain separate direct/inverse permissions and source-linked unary bounds in projections.
2. **Property contracts and containment.** Resolve the conditional cases from applicable Declarations. Update source and schema authority for the required Atom.Header.Container, optional Header.Relations and retained formal containment Relations; do not duplicate containment in Header.Relations. Verify one formal Container per ordinary non-Project Scope Unit and none for the Project root. Predefined world is exempt from the ordinary parent requirement. Separately verify each Declaration Atom has its own Container. Preserve the required Topics/Main Subject and optional Dependencies contract.
3. **MODEL coverage.** Disposition every remaining flag in the latest pinned coverage audit: source correction, declared authority, valid scope, authorized retirement or an Operator decision. The Occurrent hierarchy is settled by the latest Operator decision; finish the reviewed endpoint/inverse-permission and Event Record Relation source gates rather than reopening that decision. Reconcile Settings ownership, preserve operative Claims and exact history, and retain only explicitly authorized deferrals.
4. **Projection identity.** Verify the adopted Form + Scope Unit constraints, required Scope Unit reference and distinct Forms across Delivery, readers, identity checks and published instances. Keep all seven views at the Project root. Preserve versioned source references and the explicit Terms Graph deferral.
5. **CFEL and faithful projections.** Finish the revised canonical-Relation/inverse-alias specification and review its complete authority set. Commit the source checkpoint, then migrate Current and Draft Atoms in place by context. Preserve fixed model Relation references, qualified-Subject `:=`, YAML and literal text. Apply `:=` OR / `::` AND, inherited rules and the absent-admission case. Check the source migration, then send the implementation handoff. Repair declared narrowing and namespace binding, supported qualified selectors and bindings. Classify remaining opaque expressions; retain their complete source and diagnostics. Rebuild all seven MODEL-only views from actual Current Declarations. Formats, cardinalities and Formal Claims come only from Declarations.
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
