---
atom_id: CA-P-2694@40
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
tier: 3
version: 40
updated_at: 2026-11-02 08:16:41 +0400
subjects:
  active: MODEL//CAPRMEDIO
relations: {}
role: Plan
form: Plan
---
## Summary

Entity graph refactor stage 4 — polishing

## Result

The authorized model and CFEL migration is complete.

- 257 Drafts promoted; 209 predecessors preserved; 10 obsolete Atoms retired.
- All 31 starting tree diagnostics resolved.
- 41 canonical and derived Relation Declarations include Semantics and formal metadata.
- The selected contract display has no binding gaps, duplicate owners, missing Relation Semantics or inheritance diagnostics.
- Six Projections rebuilt from the 1,137-source Current frontier; the narrowing tree has 54 nodes and 46 narrowing links.
- Twelve nonblocking Questions record bounded choices and future work.

[Result, source pins and verification](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/cfel-contract-completion-20261102/README.md).

CFEL extraction remains bounded; the view preserves unsupported formal clauses. Actual Workflow instances and general runtime admission remain separate work in the Engine Epic. The eight completed child Tasks retain their recorded outcomes.

Earlier progress below is historical; this Result states the accepted completion boundary.

## Objective

Polish the adopted Entity graph: close real dependency-only coverage gaps, correct obsolete Subject paths, and rebuild the affected views from actual Current sources.

## Details

Follow the completed [formal-model migration](../CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims.md). Stage 3 is [Subject refinement stage 3](../CA-P-2673-EPIC--subject-refinement-stage-3.md); this is the next numbered refinement stage.

The boundary is Current Methodology and direct project-local RMED. The post-migration CA-PROJ-014/015/016 frontier has 1,101 sources; prior counts in the progress history describe earlier snapshots. Engine RMED/code/runtime, Terms Graph implementation and advanced formulas remain separate. No additional polishing work is silently included; add concrete Tasks as it is identified.

### First Task

- [CA-P-2695 — Fill dependency-only Subject coverage](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/01-CA-P-2695-TASK--fill-dependency-only-subject-coverage.md). Starting observation: 29 exact Subject paths, used in 63 Atom dependencies, have no exact Governs occurrence within the selected sources.

### Accepted Tier clarification

Tier is numeric. `Atom.Tier.Label` is an optional readable label:

| Tier | Label |
| --- | --- |
| 0 | Scope Contract |
| 1 | Core |
| 2 | General |
| 3 | Standard |
| 4 | Detail |

Labels are not required, including for these five numbers. Tiers can continue as 5, 6 and higher without a predefined label. Scope Contract is the accepted Tier-0 label, replacing Principle. Store `tier: 0` and carry `SCOPE_CONTRACT` in the filename; do not add a Scope Contract Type or repurpose Atom.Label. Draft the property Definition and its representation rule as part of the first Task before promoting source corrections.

### Remaining ordered work

1. [P2696 — Review competing/shared Definitions and establish exactly one owner](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/02-CA-P-2696-TASK--establish-one-defining-requirement-per-model-entity.md). Start with the 24 multiple-candidate groups and the confirmed shared/formal cohort. The Operator confirmed all 133 shared/formal cases. The starting cohort is all 337 parsed model paths: 180 one-exact-Definition, 24 multiple-candidate groups and 133 shared/formal cases. One canonical R/Entity Definition for every logical model Entity, including Aspects. A scope-specific R can add requirements or constraints but is not a competing Entity Definition. Preserve one coherent Claim per Atom. Do not invent separate entities for every nuance. Report where a dedicated Definition fits badly. The Relation Definition template remains eligible; derived counterparts use short references, not duplicated full meaning. No subtype hierarchy is introduced.
2. [CA-P-2697 — Review the combined Entity Definitions for coherence and conflicts](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/03-CA-P-2697-TASK--review-combined-entity-definitions-for-coherence-and-conflicts.md). Review all 180 original one-Definition entities together with the fixed 24 groups and fixed shared/formal cohort. Check meanings, scopes, formal/prose agreement, properties, inheritance and relations as one model.
3. [CA-P-2698 — Fix findings, rebuild and recheck](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/04-CA-P-2698-TASK--fix-definition-review-findings-and-recheck-the-graph.md). Apply reviewed Draft corrections and verify the combined model again. Do not automatically close this Epic.

### Accepted definition rules and delegation

Every logical Entity has one canonical defining R, including Objects, Carriers, Graph Syntax, Aspects and their properties. Scoped additional Rs are constraints, not additional Definitions. Scope-specific Rs may constrain an Object but not redefine its meaning. Report where the dedicated-Definition trial fits badly; do not create new entities for every nuance. Relation Definition counts through its specialized template. Define the main relation once and keep its derived counterpart as a short reference, following DRY. IS_DEFINED_BY is derived. Subtype restructuring remains deferred.

Use Luna for deterministic inventories, grouping, mechanical changes and checks; use Terra for semantic analysis, ambiguous Definition ownership, coherence review and independent verification. Keep work in bounded disjoint groups. Parent owns Current publication, shared Journal and integration. Use thin tracking files and immediate Drafts, not large copied-Claim mapping documents.

### Definition of Done

All adopted polishing Tasks are Done or Canceled. Every dependency-only starting row has an explicit source-backed disposition; required Definition/consumer fixes are adopted, and affected Entity views are rebuilt and reviewed. Draft preparation alone is not completion.

### Progress

P2695–P2698 are Done. Current-source readback gives one canonical Definition for each of 336 logical kind/property entities and 33 named Relation Types. The three projections were rebuilt from 1,256 Current sources. [Result and weak fits](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/definition-polishing-result.md) records changes, reviews and limits. The Epic remains Active as requested.

#### Final execution clarification

One canonical R/Entity Definition for every logical model Entity, including Aspects. A scope-specific R can add requirements or constraints but is not a competing Entity Definition. Preserve one coherent Claim per Atom. Do not invent separate entities for every nuance. Report where a dedicated Definition fits badly. The Relation Definition template remains eligible; derived counterparts use short references, not duplicated full meaning. No subtype hierarchy is introduced.

[CA-A-1311](../../02_analysis/done/CA-A-1311-SPEC_PROPOSAL--one-canonical-entity-definition-with-additional-scoped-requirements.md) records the latest decision. The Epic remains Active.

#### Inherited Definitions

Definitions inherit through / specialization and // instantiation. A narrower kind reuses the broader Definition and states only its differences. An instance follows its kind Definition and states only instance facts. Common meaning, properties and constraints are reused, not copied. Containment > adds no inheritance. Atom/Content Role: Method is an Atom with Content Role Method; it does not repeat the Atom Definition.

[CA-A-1312](../../02_analysis/done/CA-A-1312-SPEC_PROPOSAL--inherit-base-definitions-and-state-only-differences.md) records this clarification.

#### Current placement review

[CA-P-2699](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/05-CA-P-2699-TASK--review-current-atom-placement-between-methodology-and-engine.md) is Active. Review all Current authoritative source Atoms cheaply with Luna for Methodology/Engine placement and an existing Engine Scope Unit. This is a review-only scope expansion: it does not authorize live moves, content rewrites, Engine implementation, or Draft/archive migration. All Content Roles are included in the census; genuinely project-local/control and mixed cases remain explicit rather than being forced into the wrong group.

#### Placement review focus correction

The Operator deferred the cross-cutting Plan question and confirmed RMEDO as the focus. P2699 now reviews 2,443 Current RMEDO sources. C/A/P results and legacy Implementation carriers are parked; no move or content migration is authorized. The broader census remains acquisition evidence only.

#### RMEDO placement review completed

P2699 is Done: 2,443 Current RMEDO sources reviewed with Luna; 418 move candidates and 49 uncertain/split cases are recorded in the [placement result](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/rmedo-placement-review.md). Engine destinations use the existing registered Scope Units. C/A/P placement and the cross-cutting Plan question are deferred. This completes review only: no RMEDO moves or content rewrites were performed, and the nine new Drafts remain unpromoted. The Epic stays Active.

#### Workflow placement correction

Latest Operator decision: general Workflows for operating Atoms, Projections, Journal and implementation belong to CORE_META_MODEL. Local/Public Release are project-specific, so their definitions belong to project-level configuration. Runtime/code implementing Workflows remains Engine. P2699 is reopened to correct the review and counts; the blanket all-O-to-Project-Configuration proposal is superseded. No actual sources have moved.

#### Scope Definition and Summary trial

[P2700](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/06-CA-P-2700-TASK--trial-scope-definitions-and-summary-coherence-on-one-hundred-atoms.md) tests exactly 100 Current sources, including all 47 Goals, with Terra at high effort. Candidate Scope Definitions absorb standing responsibilities and related outcomes; specific constraints can remain additional Rs. Atom coherence is tested by a Summary that covers the whole meaning, not a one-predicate-per-file rule. Compare 70 and 100 characters before adopting a limit. Current Atoms remain unchanged.

#### Corrected Workflow placement review completed

P2699 is Done after rechecking 187 O definitions and 186 related RMED contracts. The latest rule is Core business meaning, Engine technical realization and Project-specific Release orchestration with cross-scope Step calls. The [updated review](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/rmedo-placement-review.md) replaces prior move counts. The census now also includes the Operator-owned Project Goal outside role folders: 2,444 Current RMEDO sources. Actual moves remain zero; P2700 separately trials Scope Definitions and Summary coherence.

#### Scope Definition trial completed — adoption undecided

P2700 is Done for trial review and Draft preparation: 100 Current sources including all 47 Goals produced 103 candidate units and one supporting Definition Draft. The Goal conversion yields 22 Scope Definitions plus 26 supplementary Requirements, not a mechanical relabel. All candidate Summaries fit the experimental 100-character ceiling; 42 have an established equally faithful ≤70-character alternative. See the [result](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/scope-trial-100-result.md) and its thin Draft index. Current RMEDO remains unchanged; no promotion or Goal retirement is authorized by this trial. The Epic remains Active pending the adoption decision and other open Draft work.

#### Scope Contracts replace the separate Principle concept

[A1313](../../02_analysis/done/CA-A-1313-SPEC_PROPOSAL--goals-outside-and-scope-contracts-at-tier-zero.md) records the latest decision: Goal outside; RMEDO Scope Contracts inside at Tier 0; Tier 1+ specialization. Project Principles become the same local contract pattern, not an exception. [P2701](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/07-CA-P-2701-TASK--adopt-goals-outside-and-tier-zero-scope-contracts.md) handles the concrete Goal/Core classifications, model/template Drafts, retirement, review, adoption and rebuild. This supersedes the R-only Scope Definition / Goal-retirement direction and the earlier Principle Tier label. P2700 remains completed trial evidence; its Drafts are not automatically adopted. The Epic remains Active.

#### Scope Contract naming simplification

Latest Operator correction: Scope Contract is the readable label for numeric Tier 0, not a new RMEDO Atom Type or Atom.Label. Existing Types remain; an O Atom can remain Workflow, Action or Step. Tiers 1–4 keep Core, General, Standard and Detail, with no mandatory names for 5+. A1313 and P2701 are updated; the short-lived five-Type proposal is superseded before any Type Draft was created. Goal/Core classifications and model Draft preparation continue under the simpler label model.

#### Final Scope Contract representation and serving relations

P2701 uses `tier: 0` and the filename token `SCOPE_CONTRACT`; Content Role, Type and Atom.Label remain separate. The Operator also admits appropriate typed same-Scope MEDO Tier-0 → R Tier-0 serving relations. This exception does not allow arbitrary equal-Tier edges or reverse R→MEDO / R→R / MEDO→MEDO equal-Tier governance. Review Core promotion links and update governing methodology and Evaluations together. A1313 records the accepted decisions.

#### Scope Contract Draft package prepared

P2701 has 81 actual Drafts under the final Tier-0/SCOPE_CONTRACT filename model, preserving existing Types including O/Workflow. The [adoption package](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/scope-contract-adoption.md) records review corrections, Goal/Core decisions, eight new-identity/rebinding prerequisites and holds. Current Principle retirement, source promotion/moves and graph rebuild remain pending a coherent publication packet. No Current RMEDO or Engine code/runtime changed. The Epic stays Active.

#### Scope Contract adoption complete

P2701 and A1313 are Done. The Task performed 87 Current updates and one retirement, preserved 88 archives, rebound the eight new identities and rebuilt the three views from 1,261 actual sources. [CA-P-2703](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/08-CA-P-2703-TASK--review-deferred-foundation-and-notation-drafts.md) is the next polishing follow-up; [CA-P-2702](../CA-P-2637-EPIC--migrate-engine-rmed-atoms/backlog/CA-P-2702-TASK--reconcile-deferred-engine-scope-goals.md) retains the four Engine Goal cases in the separate Engine Epic. Three extension Goals stay deferred. This Epic remains Active as requested.

#### Operator review of20 adopted Atoms

Corrected all20 fixed sample Atoms and three existing Claim/Summary writing Methods. Changed Summaries use successor IDs, with predecessor archives and necessary Current reference maintenance. Seven former Goals again live outside their target Scope Units; R707 remains a Rule. The existing list-format Method is applied, not duplicated. [Full corrected review](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/sample-20-content-corrections.md) and [Thin predecessor/successor list](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/sample-20-content-corrections.tsv) preserve the sample and expose the actual Current sources. This Epic remains Active; runtime and code were not changed.

#### Deferred Draft review in progress

[P2703](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/08-CA-P-2703-TASK--review-deferred-foundation-and-notation-drafts.md) is Active. Current adopted writing Methods govern the new Drafts; shared Term/classification preparation is kept distinct from Current authority. The next coherent adoption contains the shared Text Writing Style Definition and readable-model naming Policy. No Engine runtime or P2637 edit is included.

#### Two deferred style sources adopted

P2703 adopted R2441 and M445; [its review](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/deferred-draft-review.md) tracks twelve dispositions. Two rejected Tier0 promotions stay at Tier1; E002 awaits the Operator. Shared lexical/classification preparation and the Engine adapter handoff remain outside this narrow adoption. The Epic remains Active.

#### P2703 graph readback

The three derived views were rebuilt from1,263 actual Current Methodology/project RMED sources after R2441/M445 adoption. Source/Definition/native-target checks passed: zero missing Definition coverage and no unknown or ambiguous native targets. E002 remains unchanged pending the Operator; shared Drafts, Engine realization and P2637 remain outside this write set.

#### E002 retired without replacement

The Operator removed E002. Its existing version29 is archived; six Current parent links are removed and its unpromoted Tier0 proposal is withdrawn. Consumer Claims and other relations remain. [P2703](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/08-CA-P-2703-TASK--review-deferred-foundation-and-notation-drafts.md) records the actual outcome; the Framework offers capabilities without imposing evidence or justification duties on the Operator. The Epic remains Active.

E002 retirement readback passed. The three views now contain1,262 actual Current sources, excluding E002, with no unknown or ambiguous native targets. Scope and remaining shared-Draft holds are unchanged.

#### Deferred review complete; six adoptions handed off

[P2703](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/08-CA-P-2703-TASK--review-deferred-foundation-and-notation-drafts.md) is Done for review and explicit disposition of all twelve candidates: two adopted, E002 retired, three superseded preparations, and six unadopted preparations handed off. Five belong to the existing CA #5: WFs lexical/classification adoption; the adapter belongs to the existing CA #3: ENGINE handoff. No duplicate Drafts or new adoption Task were created. This Epic remains Active until the deferred source changes are adopted or otherwise resolved and checked against actual Current sources.

#### Established principles keep their names

The Operator rejected the rephrased DRY wording. DRY is restored as M446 (“DRY — Don’t repeat yourself”), and the same correction is applied to MECE as M447 (“MECE — Mutually exclusive, collectively exhaustive”). Their Claims use the named principles directly. M442’s invented declarative-Summary restriction is removed; plain, meaningful familiar names and short instructions are valid. Previous identities and all reference-only predecessors are archived. [The same20-item review](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/sample-20-content-corrections.md) now opens latest Current successors; the original sample and earlier publication receipts remain preserved. No other sample Claim is rewritten, and no runtime or shared Term Draft is changed.

#### Rewrite the fixed twenty-Atom sample from its original archives

The same twenty Atoms were rewritten from their October 29 archived originals using the writing guide and evaluation. Eighteen have successor IDs; PROGRAMMATIC’s ownership statement and DRY were already correct and remain unchanged. Accepted metadata is retained. Today’s replaced versions and the necessary Current-reference predecessors are archived. [Review the twenty Atoms](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/sample-20-content-corrections.md). The original sample manifest and original archives remain unchanged. The legacy Concern Priority authority gap remains outside this writing pass. This Epic stays Active.

#### Check the writing against versions older than two days

The fixed twenty Atoms were reviewed against the older corpus. Two small meaning-preservation corrections were applied. Of eighteen other project Tier-0 RMEDO Atoms, seventeen received small writing updates and MECE remained unchanged. Summaries, IDs and governing metadata are retained; predecessor versions are archived. [The corpus review](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/golden-writing-review.md) records the results. A blind Summary regeneration test covers 38 contents: 30 titles were accepted and eight flagged for review in its final run. Generated titles were not applied. [The experiment](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/summary-regeneration-review.md) preserves its inputs, outputs and limits. This Epic stays Active; no runtime or code changes are claimed.

#### Content-only restoration — 31 October 2026

The Operator chose content-only restoration of Active project Principles and project Core to 27 October. All 47 currently Active matches are restored from `d029da802`; E002 remains retired. Historical Markdown, including original Summaries, is restored verbatim. Current identities, Subjects, Types, owners, Tiers, relations and file paths remain. Versions increment and restoration timestamps are current; 47 predecessors are archived and 47 actual change events are in Journal. Earlier writing changes above are superseded for this cohort; their records remain history.

[Actual restoration and real before/after Atom links](../CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/restore-project-principles-core-20261031/result.md). The Epic stays Active. Recent Declaration/Form, external Goal/Scope Constraint and internal Tier-0 Scope Contract refinements remain pending separate methodology adoption; they were not implicitly published by this restoration. Projections and Engine code/runtime are unchanged.

#### Node Declarations and formal graph rules — latest proposal

The Operator requested the [Node Declaration Spec Proposal](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/CA-A-draft-CORE_META_MODEL-SPEC_PROPOSAL--declare-node-branch-and-formal-graph-rules.md). This follow-up supersedes the earlier blanket one-R/Entity-Definition direction only for the new Node branch. Earlier completed Tasks, reviews, archives and publication outcomes remain historical evidence; they are not reopened or rewritten by this planning update.

Each member of `Node/` is to have exactly one Current Declaration Atom, with one matching active Subject and a formal-only normative Claim. Declaration is Requirement/Form: Declaration and uses the R prefix. Its Form registration, representation and replacement packet must be admitted before adoption. A Declaration includes its Node's structure, complete effective Relation whitelist, endpoint/cardinality restrictions and conditional rules. Shared Relation meaning remains defined once. Syntax Graph entities retain their Claim and optional Semantics; Carrier and Terms are not blanket retirement targets.

The syntax separates `/` Primary narrowing, `//` Primary instantiation, Property access, composition and classification. Direct values and immediate nested Properties have independent domains and counts. `..` and embedding Formal Claims in Subjects are withdrawn. The graph is derived from admitted Formal Claims with source traceability; classification is derived from the 0/1 IS_PROPERTY_OF rules, with HAS_VALUE and Primary/Property structural restrictions.

`/` narrowing also supplies effective rules for narrower Nodes' instances: inherited Relation cardinalities and Property declarations, Formats, value/child constraints and local refinements. Do not redeclare an inherited Property or create another Declaration merely for an inherited lookup/projection. Preserve its declaration provenance and bearer identity; inheritance does not copy actual values or Relation facts.

The latest Operations model keeps Workflow, Step, Substep and Action as sibling narrower Operations Nodes. Every Workflow has one or more Steps and every Step is contained by exactly one Workflow. Each Step exclusively either runs one Action or contains one or more Substeps. Each Substep runs one Action and is contained by exactly one Step. Actions can be unused or reused by Steps/Substeps. RUN/IS_RUN_BY and composition inverses are not authored twice; declaration of an execution binding is not evidence of an execution Run.

##### Ordered follow-up

1. Reconcile the proposal with exact Current sources and resolve the blocking endpoint, Form/representation, composition-identity and branch-membership decisions one at a time.
2. Prepare and independently review the governing Declaration/Relation/notation and Carrier-rule Draft packet. Preserve the Syntax Graph Claim exception and formal Scope ownership boundaries.
3. Map actual Node targets to exactly one Declaration and one explicit predecessor disposition. Preserve every needed constraint; do not blindly map all Entity-prefixed Subjects to Node or replace every `/` with `<+`.
4. Coordinate schema/parser, Markdown/YAML adapters, graph extraction, source SDK/workflow callers and meaningful positive/negative checks with the existing [Engine migration Epic](../CA-P-2637-EPIC--migrate-engine-rmed-atoms.md). Engine implementation is planned dependency work, not an effect of this Epic edit.
5. Regenerate reviewed, source-pinned migration packets. Previous notation packets are superseded inputs and must not be executed or silently repinned.
6. Establish admitted Declarations and repair references before retiring their corresponding Node Definitions through the existing lifecycle. Keep actual Current authority and historical versions distinct.
7. Rebuild and independently check Declaration coverage, effective whitelists, forbidden edges, endpoints/cardinalities and source traceability. Record source, parser, projection and runtime/semantic admission outcomes separately. Keep this Epic Active until its adopted follow-up and gates are actually complete.

The read-only Core census contains 333 Current Entity Definition carriers: 290 Object/Aspect/Property review candidates, 18 Syntax, 23 Carrier and 2 Term. Those counts are not an approved Node mapping or retirement packet. The earlier Term/Property batch has 138 verified publication receipts; O030-last, rebinding and broader notation migration remain unexecuted. Preserve that evidence and never replay completed effects.

This update records the proposal and remaining work only. No Declaration was promoted, Definition retired, Scope Unit moved, parser deployed or graph/runtime result established by creating the proposal or updating this Epic.


#### Governing Draft packet prepared — latest naming correction

Declaration is a Form of Requirement, not a separate Role. Use `Role: Requirement / Form: Declaration`; no new Role letter is required. Content Role becomes Role and each Role-specific Type becomes Form. New naming Methods explain how to avoid generic words that add no useful meaning while retaining precise contextual uses and canonical expressions.

The [Spec Proposal and complete Draft-ID register](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/CA-A-draft-CORE_META_MODEL-SPEC_PROPOSAL--declare-node-branch-and-formal-graph-rules.md) link the directly prepared governing Drafts: Node/Operations Declarations, ownership and inheritance rules, Relation definitions, graph notation, Scope, naming, carrier mappings and migration checks. Each new carrier currently has its unnumbered Draft marker; allocation is pending. The six Node Declarations do not establish full branch coverage.

Next: finish semantic gates and exact predecessor mapping, complete effective whitelists and Node coverage, then coordinate adoption and Engine consumers. Current Epic version 38 remains unchanged; this version-39 Draft does not retire Definitions or establish runtime migration.


#### Review gaps — resolved instance values and composition names

The Operator confirmed literal Property values on instances: CA-P-123.version has value 1, constrained by the Property declaration. HAS_VALUE is a value binding, not an ordinary Node-to-Node Relation; no Declaration is needed for the literal. Its exact Formal Claim spelling remains to be settled. Canonical composition names are IS_PART_OF and derived HAS_PART, with Container classification yes/no. Existing IS_CONTAINED_BY/CONTAINS sources and consumers need coordinated migration; Current names are not rewritten by this Draft.

Review also established that omitted cardinality remains undefined under the existing syntax rule. Same-member condition/conclusion binding and effective inheritance are explicit in the Drafts. Markdown subtree retrieval includes its own heading, as requested by the Operator; the current fetch implementation differs. Exact Node mapping, full whitelists, formal acyclicity, omitted value-domain behavior and remaining reference/Markdown encoding choices are still open.


#### Phase boundary — actual Operations instances deferred

The Operator deferred review of actual Workflow, Step, Substep and Action instances. The current pass covers model Declarations, relation meanings, notation and constraints. Generic kind-source mapping is preparation evidence; actual O-instance audit, repair, execution and migration belong to a later phase and are not prerequisites for calling this bounded model review complete. This does not mark later implementation or adoption checks as passed.


#### Relation endpoint signatures and concise Claims

The Operator requires formal Host/Target permissions in Relation Definitions and approved `RUN ((HAS_INVERSE)) IS_RUN_BY`, reusable for other inverse pairs. Inverse views have no separate Definition Atom. Define HAS_INVERSE once; remove repeated placement commentary and Draft boilerplate. The RUN Draft is shortened to Define RUN and its formal signatures.

Do not add formal syntax for a single-use constraint. Acyclicity remains prose; Primary Node literal-value prohibition also uses prose instead of a new HAS_VALUE binding predicate. The model review permits precise prose with existing Formal Claim notation; actual Operations instance review remains deferred.


#### Latest containment correction

The Operator restored IS_CONTAINED_BY with derived CONTAINS because containment is more specific than general part/whole membership. This supersedes the earlier IS_PART_OF/HAS_PART choice in this Draft's history. Keep Container: yes/no, +>/<+ and typed relations.contained_by. The formal inverse declaration is IS_CONTAINED_BY ((HAS_INVERSE)) CONTAINS. There is no separate CONTAINS Definition.


#### Language name — CFEL

The Operator renamed Graph Syntax to CFEL (CAPRMEDIO Formal Expression Language). The governing Drafts and proposal use CFEL for the language's syntax and expression meanings. Graph, CFEL and Carrier are distinct model components. Earlier Graph Syntax wording in this history denotes the previous name. Current carriers and runtime are unchanged by this Draft rename.


#### Declaration expansion — Property contracts and meaning

- Prepare one Declaration per entity in Node/.
- Specify direct-value Format and cardinality for every Property.
- Specify dependent-entity Format and cardinality separately.
- Retain the original Declaration for an inherited Property.
- Use CFEL where possible.
- Use Claim prose only for constraints CFEL cannot express.
- Keep brief Semantics for Primary Nodes only.
- Use short sentences, consistent Terms, lists for parallel statements.

The source census covers all 750 active direct Core R carriers. It finds 120 formal Property expressions. Five initial Property Declarations cover Status, Updated At, the typed containment group, its Atom reference, its Scope Unit reference. Missing dependent-entity contracts remain explicit decisions. Actual Operations instance review stays deferred.


#### Smaller inventory first — latest selection

The Operator chose a smaller Node inventory instead of importing the existing taxonomy. Stop further expansion until that inventory is selected. The proposed tree is linked from the Spec Proposal. Prepared Property Drafts remain candidates.

- Resolve declared dependent entities locally.
- Resolve inherited dependent entities.
- Forbid undeclared dependents with explicit .[]{:0}.
- Keep missing counts for declared dependents unresolved.
- Keep actual Operations instances deferred.

The census and prepared candidates do not approve a larger model. Current sources remain unchanged.


#### Reduced inventory selected — Primary coverage prepared

The Operator selected Actor, Atom, Scope Unit with Project, Aspect, Package, Projection, Journal. Atom keeps eight Roles. Operations keeps Workflow, Step, Substep, Action. Requirement includes Declaration and Relation Definition. The selected tree has 23 Primary Nodes, including Node. Each has one Draft Declaration.

- Do not import Object, Continuant, Occurrent automatically.
- Keep inherited Properties under their original Declaration.
- Review the Property contracts before claiming full coverage.
- Resolve incomplete body and Settings dependent-entity contracts.
- Review effective Relation whitelists separately.
- Keep actual Operations instances deferred.

Current sources remain unchanged. This is Draft coverage, not migration completion.


#### Analysis freeform content and Property identity

- Analysis content is freeform.
- CFEL `**` selects dependent Properties recursively.
- `*` remains the immediate-dependent selector.
- The following Format/cardinality applies to each selected Property.
- Sibling names are unique.
- x.y.z and x.z identify different Properties.

The Analysis Declaration uses Content.**[string]{:1}. The section-presence versus direct-value counts are being clarified separately. Projection's primary Declaration no longer repeats the six separately declared Property contracts.


#### CFEL v2 names, values and representation

- Use colon for allowed values.
- Put Property occurrence counts before colon.
- Put value Format/count after colon.
- Use * for immediate dependent names.
- Use ** for recursive dependent names.
- Count names on the left.
- Count values per existing Property on the right.
- Separate expressions with semicolons.
- Use markdown for Content section values.
- Keep Atom.Content.Claim.
- Put formal content in a CFEL fence.
- Remove the separate Formal Claim Property.
- Use >> for representation mapping.

The typed containment alternatives remain individually optional. Their parent requires exactly one named dependent. Sibling names are unique; x.y.z differs from x.z. Actual instance review remains deferred.


#### Minimal Settings and Carrier movement — latest decisions

- Project.Settings contains Name, Prefix and required AI Agent Confidence Threshold; other Framework Settings remain deferred.
- Framework Settings is deferred.
- Remove its unpublished candidate from this packet.
- >> means move into a referenced Carrier or Carrier part.
- Use @Carrier//Markdown file.
- Frontmatter is delimited YAML at the beginning of the file.
- Filename is a Carrier property.
- Location is a Carrier property relative to repository root.
- Move Atom descendants excluding Content and its descendants into frontmatter.
- Move Content descendants into the Markdown part.
- Node/**, .** selects narrower entities plus their Properties.
- Add Node separately when root inclusion is required.

The selected contracts are prepared. Relation whitelist completeness and reference mappings still need semantic review. Current sources remain unchanged.


#### Deliver Objects — latest operator meaning

- Object means a Node instance.
- >> means deliver an Object to a Carrier.
- This supersedes the earlier move wording in this history.
- The Carrier instance reference is @Carrier//Markdown file.
- Filename is a Carrier property.
- Location is a repository-relative directory property.

The Term does not restore the retired Object taxonomy branch. Actual file delivery remains outside this Draft work.


#### Reusable CFEL constraints — 2026-10-31

- Keep brief Semantics for Primary Node Declarations. Properties have none.
- Formal-only Claims increased from 37 to 40.
- Add a numeric-comparison Rule for >, >=, < and <=, used by Version Number, Tier and Work Sequence Number.
- The packet now contains 99 Drafts.
- Defaults, scoped uniqueness, revision pairing and reference domains remain syntax candidates with unresolved semantics.

[Coverage review](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/node-declaration-20261031/formal-coverage-review-20261031.md) records the independent preservation review and remaining decisions. Parser implementation and source adoption remain separate.


#### Author deferred and omission fallback — latest decisions

- Remove Author from the proposed model and artifact metadata; defer authorship.
- Withdraw the unpublished Atom.Author Declaration.
- Preserve the Operator registry and existing Operator identity/ownership.
- Use p ?= expression for omission fallback; Atom.Label ?= Atom.Form is the first consumer.
- Inheritance already supplies its applicable declarations and constraints; add no extra inheritance stage.
- The packet has 99 Drafts: 23 Primary Declarations and 45 Property Declarations.
- Current author-required R/D sources and runtime remain unchanged; reconcile them before adoption.


#### Operations execute; RMED constrains — latest decisions

- Processes belong to Operations. RMED states invariants.
- Use existing IF/THEN for conditional constraints.
- Do not add before/after grammar or extra Workflow Rs.
- Keep version-change and Project.Settings input-selection instructions in deferred Operations notes, outside Property Declarations.
- Preserve timestamp, identity, archive and other invariant guarantees.
- Settle the population for the Atom ID + Version uniqueness key before writing its formal constraint.


#### Project-wide version key and promotion — latest decisions

- Rename the proposed Atom.Version Number Property to Atom.Version.
- Inside a Project, `(Atom.ID, Atom.Version)` is unique across all Draft, Current and Archived instances.
- Add the reusable UNIQUE tuple constraint to the existing Atom Declaration.
- Promotion assigns max(Version) + 1 across every same-ID instance in the Project, including the selected Draft.
- This supersedes preservation of a higher proposed number and next-free gap selection.
- Current 5 with Drafts 6/7: promote Draft 7 as Current 8, then remaining Draft 6 as Current 9.
- Current 7 with Drafts 6/8: promote Draft 6 as Current 9.
- Preserve these Operations notes without extra Workflow Rs, Workflow instances or before/after grammar.
- The previous Current/Archived-only uniqueness answer is superseded.


#### Promotion max-version formula — latest decision

The promotion Workflow uses the following pseudocode within the Project. Select all same-ID versions, including the selected Draft; do not filter to Current.

```text
$last_version = max(atom.version) where atom.id = X;
$new_version = $last_version + 1;
```

This replaces the earlier keep-proposed/next-free rule. RMED retains the Project-wide unique ID/Version tuple constraint. No additional Workflow Rs or CFEL query/assignment syntax are added.


#### Structural levels and root kinds — latest decisions

- Scope Unit.structural_level and Package.structural_level are explicit nonnegative integers, written once in the applicable Declaration; containment validates their values.
- Project and Implementation instances are roots: level 0, not contained by another instance of the same kind.
- Implementation is a narrower Package kind, not one named instance.
- Non-roots are contained by one immediate container; each IS_CONTAINED_BY link satisfies contained level = container level + 1.
- Use typed instance-variable binding and membership; add numeric value addition to CFEL.
- Withdraw the unpublished recursive Relation-path Rule. No instance-population COUNT syntax is added.
- The selected packet has 104 Drafts: 24 Primary and 47 Property Declarations. Current sources and runtime remain unchanged.


#### Successor refreshed against Current version 38

Current Epic 38 includes the 31 October content-restoration record. This version-39 Draft preserves that addition and all pending methodology notes. The prior version-38 Draft was not promoted or archived; it was an unpublished successor refreshed to avoid a stale version. Current version 38 remains unchanged.


#### Cardinality on instance selections — latest decision

Use the existing cardinality on the selected items: Package/Implementation//{:1}, Scope Unit/Project//{:1} and Journal//{:1}. Each Project has exactly one Journal; no narrower Work Journal kind is introduced. Root and Journal singleton constraints are formal. No separate counting construct or Rule is added. The selected Project supplies the evaluation boundary.


#### Allowed counts and Declaration ownership — latest decisions

- Use {:n} for allowed counts; {=n} remains a test and {==n} a required/derived conclusion.
- Use the same cardinality for Property, value, name, instance and Relation selections.
- A Node Declaration constrains its own Host-side Relation counts; put each inverse view's count in that Host's Declaration.
- Keep target kinds and derived inverse semantics; do not duplicate authored links.
- Step, Workflow, Substep, Action, Scope Unit and Package Claims are aligned. No Workflow instances or runtime were changed.


#### Every Atom states about its active Subject — latest clarification

The scope rule applies to every Atom with an active Subject, across Roles and Forms. Independent statements about other Subjects belong in their own Atoms. References needed for the active Subject's relations, inputs, outputs, conditions and dependencies remain valid. The Step/Workflow relation-count split is an example, not a Declaration-only exception.


#### Event Record — approved inventory addition

Add the Event Record Primary Node Declaration. Each record has exactly one containing Journal; Journal is a Container with zero or more records. Keep one Journal per Project and the existing derived inverse. Event Record has its own required scalar string ID, unique across Event Records in the Project. Add its Property Declaration, using the existing UNIQUE constraint. The packet now has 107 Drafts: 25 Primary and 48 Property Declarations. Append-only formalization remains pending; no execution instances or runtime changed.


#### Combined Subject value case — latest decision

Use := in Subjects for allowed value and condition together, for example Atom/(.Role := Method). This admits Method as a Role value and selects its Method case; it does not assign an instance value or close the Role domain. Formal Claims retain separate : and = meanings. Update proposed Subject addresses; Current bindings and runtime remain unchanged.


#### MODEL and PROJECT STRUCTURE instance roots — latest architecture

- Add MODEL and PROJECT STRUCTURE as Primary Node kinds, declared by CAPRMEDIO's self-describing MODEL.
- Use MODEL//CAPRMEDIO and PROJECT STRUCTURE//CAPRMEDIO. Consumer Projects have their own PROJECT STRUCTURE root and an optional MODEL root.
- PROJECT STRUCTURE includes Scope Structure, Aspects and further declared components. Core Meta-Model contains the Atoms defining CAPRMEDIO's MODEL.
- A local MODEL inherits CAPRMEDIO's MODEL and may expand it, add constraints or override any inherited rule. Its explicit overrides replace local effective rules; the base remains unchanged.
- Resolve one effective Current Declaration per Node in the selected MODEL. Reuse unchanged inherited Declarations.
- Distinguish MODEL inheritance, Node narrowing and containment. Keep ENGINE's declared Scope distinct from local MODEL override authority.
- Supersede the earlier PROJECT wrapper and MODEL/PROJECT root split. Keep exact Relation naming, Model-selection binding and source-to-root migration open.
- The selected packet now has 108 Drafts: 27 Primary and 47 Property Declarations. The separately recorded Scope Unit Navigation Number withdrawal is preserved. Current sources and runtime remain unchanged.


#### Zero-prose Declaration Claims — staged pass

Target zero prose Claims in Node descendants and their Properties. Keep brief Primary Semantics. Existing-syntax and shared-Rule reductions move the count from26 to25; no normative constraint is discarded. Projection.Form's three known literal cases are formal without closing its domain. Align the readiness Evaluation with := Subjects and effective MODEL overrides. Reusable language/binding patterns and the Current-Atom completeness decision remain open. No parser, runtime or Current-source change is claimed.


#### Active Subject for every Current Atom — latest decision

Require one Active Subject for every Current-group Atom, including Backlog, Active, Done and Canceled. Remove the completeness exception. Atom.Subjects.Active Claim is formal-only with its existing IF/THEN and cardinalities unchanged. Other Status Groups retain their existing occurrence contract. Node descendant Claims with prose:24.


#### Projection.Form — latest correction

Rename the proposed Projection.Type Property to Projection.Form. Select its cases through Projection/(.Form: Catalog), Projection/(.Form: Map) and Projection/(.Form: Hub). The Property contract and existing literal admissions are formal-only; remove the explanatory classification sentence. Update the Projection.ID identity wording to use Form. Node descendant Claims with prose:23. Current sources, carrier keys and runtime are unchanged.


#### Atom.ID freeze boundary — latest decision

Freeze Atom.ID on first promotion to Current or Archived. Direct Draft to Archived is permitted; no prior Current state is required. Record this in the deferred lifecycle Workflow work. Version/timestamp preservation on archive and the Current-promotion version formula are unchanged. Freeze scope across later Draft versions remains the next question; no new CFEL predicate has been admitted.


#### Scalar immutability across versions — latest decision

Define IMMUTABLE(p) once and use it for Atom.ID and admitted Event Record.ID. Atom.ID activates on first Current or Archived promotion, including direct Draft to Archived, and remains fixed in later Draft versions of the same Atom. Resolve logical identity through supplied lineage, never rematch by mutable ID, Version or Carrier. Missing required evidence cannot pass. After activation, removal of an optional Property also fails. The scalar contracts and Event Record uniqueness remain unchanged. Atom.ID is formal-only;22 Node descendant Claims retain prose. The packet now has109 Drafts;27 Primary and47 Property Declarations. Parser/runtime history binding remains unimplemented.


#### Property-tuple dependencies — reusable CFEL extension

Define DETERMINES over complete relevant state history within one Project. Apply ID to Summary dependency and both Projection basis/ID directions. Compare reference targets by declared identity, not Carrier paths. Projection.ID is formal-only; Summary's qualitative coverage rule remains. The packet has110 Drafts,27 Primary and47 Property Declarations. Node descendant Claims with prose:21. History/reference bindings and parser/runtime support remain adoption work.


#### Summary Method and new-identity Draft — 2026-11-01

Move Summary coverage into its authoring Method; preserve the requirement and keep the Declaration formal-only. If an update Draft changes Summary, create a fresh Atom.ID and set its Version to1. Record this in lifecycle Workflow design; a fresh ID identifies a new identity rather than changing the accepted identity. Clarify whether an unchanged-Summary Draft remains under the old ID while still being a new Atom instance. Current prose count20;111 Drafts with27 Primary and47 Property Declarations. No lifecycle implementation or Current-source change is performed.


#### Current plus Archived Summary invariant — latest clarification

Atom.ID determines Summary only over Current and Archived states. Filter each historical state before tuple resolution; Drafts are outside this dependency. Repeated IDs with equal Summaries are permitted. A new Draft is a new Atom instance, not a reason to enforce Atom.ID uniqueness across versions. Keep the Summary-change update branch:allocate a fresh ID and create Version1. This formal invariant does not implement that Workflow branch.


#### Active Plan numbering per direct container — latest decisions

Sequence Number remains optional and positive when supplied. Enforce uniqueness only for Status Active, per direct container. Done/Canceled/Backlog/Draft/Archived are excluded from that check. A numbered Active Plan needs a known direct container. Use the actual typed containment leaf in two conditional UNIQUE calls, evaluated in one snapshot rather than history. The model owns only number constraints; the Workflow for P execution owns execution order. The Number Declaration is formal-only. Current descendant prose count19;111 Drafts. No numbering or Workflow runtime was changed.


#### Role and Form may share a name — 2026-11-01

Remove the proposed ban on copying a Role name as a Form. A Form remains subject to admission under that Role. Equal names alone neither forbid nor admit the Form. No CFEL admission function or runtime validation change is introduced by this correction.


#### Explicit structural levels — 2026-11-01

Choose the explicit Declaration value rather than deriving it from the containment chain. Retain root level 0 and contained level = container level + 1 as validation constraints. Remove the superseded sole-derivation prose from both Property Declarations. Do not add DERIVED_FROM or a chain-computation mechanism. Both Claims are formal-only;17 descendant Declaration Claims retain prose.


#### Claim writing rule in Method — 2026-11-01

Use the existing formal-notation authoring Method for the rule to write prose only when CFEL cannot express the constraint without a single-use extension. Remove that writing instruction from Atom.Content.Claim’s Declaration; retain its one-CFEL-block and no-other-fenced-block constraints. No new Method Draft or language syntax is added. The prose-Claim count remains17 because the structural fence constraints still use prose.


#### Fenced-block constraints in CFEL — 2026-11-01

Add one FENCED_LABELS selector. Use the existing finite literal Format [in (CFEL)] with count0..1 to replace both fence-limit prose clauses in Atom.Content.Claim. Count duplicate labels separately; exclude indented code by Operator decision. Preserve the label-binding and CFEL-body-validation boundaries. Independent review passed. The packet has112 Drafts;16 descendant Declaration Claims retain prose. Parser/runtime label binding remains unimplemented.


#### Retry handling belongs to Workflow — 2026-11-01

Withdraw the Plan Implementation Retry Limit Property Draft. Retry handling belongs to the Workflow; do not recreate the Plan field or invent a replacement Workflow parameter. Keep Autonomous Confidence Threshold as a Plan Property, with its current Declaration unchanged. The packet has111 Drafts,27 Primary and46 Property Declarations;15 descendant Declaration Claims retain prose. Current methodology and runtime remain unchanged.


#### AI Agent Confidence Threshold fallback — 2026-11-01

Rename the Plan Property to AI Agent Confidence Threshold. Keep it optional. Resolve own authored value first, then the nearest applicable authored value along IS_CONTAINED_BY recursively, then required Project.Settings.AI Agent Confidence Threshold. Reuse one non-writing fallback mechanism; do not copy inherited values into the Plan carrier. Expand Settings only by this required default. Retry handling remains Workflow responsibility; its withdrawn Plan Property stays withdrawn. Exact CFEL chain integration is in progress; no runtime configuration value is invented.


#### Reviewed non-writing confidence fallback — 2026-11-01

Keep optional P.AI Agent Confidence Threshold; require Project.Settings.AI Agent Confidence Threshold. Extend ?= with one ordered chain and LOOKUP over existing IS_CONTAINED_BY facts. Select nearest compatible authored value; do not copy it. Bind the terminal Project through the current Project evaluation context, not a newly required containment route. Preserve evaluated fallback-expression-cycle and traversal-cycle errors. Final review passed. The packet has112 Drafts with27 Primary and47 Property Declarations;14 descendant Declaration Claims retain prose. Actual Project default value and parser/runtime migration remain separate work.


#### Archive preservation in Workflow requirements — 2026-11-01

Keep archive Version/Updated At preservation and no new Version solely for archiving in one Workflow-subject Requirement Draft. Remove those clauses from Atom.Status and Atom.Updated At Declarations; retain accepted-edit timestamp meaning and exact-no-op preservation. No before/after syntax or Workflow instance is added. Independent preservation review passed. Atom.Status is formal-only;113 Drafts and13 descendant Declaration Claims retain prose. Current sources and runtime are unchanged.


#### Core timestamp requirements versus process — 2026-11-01

Core Meta-model R atoms define what Updated At must represent. Keep Atom accepted-edit/no-op and Projection latest-completed-rebuild invariants in their Core Declarations. Workflows define how compliant values are produced; Engine implements the process. The existing archive-preservation Rule is also a Core R specifying required Workflow results, not Operations steps. No timestamp requirement moves to Engine and no data contract is removed. Prose-Claim count remains13.


#### Event-based Updated At candidate — 2026-11-01

Use the Operator’s proposed shared pattern: Updated At equals MAX of timestamps from matching update Event Records, for both Atom and Projection. This remains a Core R invariant. Resolve qualifying update events first; then event target/action/time schema, version-safe target identity, initial timestamp and complete Journal coverage. Keep both existing timestamp Declarations until equivalence is established. No candidate syntax, event field or runtime behavior is adopted yet; residual prose count13.


#### Accepted update events and generic MAX — 2026-11-01

An update Event Record denotes an accepted completed update, including a completed Projection rebuild. Exclude no-ops, failures and archiving from timestamp maxima. Add one reviewed generic CFEL filtered-selection/MAX Rule Draft, independent of Event Record field design. Keep both timestamp Declarations unchanged pending the initial-creation event policy and reference/time bindings. The packet has114 Drafts;13 descendant Declaration Claims retain prose. No Event Record schema or query runtime is implemented.


#### Creation included in Updated At maximum — 2026-11-01

For Atoms and Projections, select accepted completed create and update Event Records for the target object. MAX(timestamp) yields the initial create time or latest update time. Creation need not emit an additional update record. No-op, failed and archive events remain excluded. Resolve event target identity through Draft promotion/Version reassignment and event-field/time bindings before replacing timestamp Declarations. No schema or runtime change;13 prose Claims remain.


#### One old-to-new Event Record — 2026-11-01

Capture the Operator’s old → new, one record direction. Clarify whether endpoints are separate Atom instances or states of one instance before choosing event reference fields or changing timestamp matching. Do not infer rewritten history or merge distinct versions. No schema, Declaration or runtime change;13 prose Claims remain.


#### Business Property delta and promotion timestamp — 2026-11-01

Promotion is update; its accepted timestamp advances the promoted Atom’s Updated At. One update Event Record holds only changed logical Property paths with old/new values or absence, such as Version6→8 and StatusDraft→Active. No complete object snapshots are required. Exclude Carrier filename/directory changes; Carrier-only rename/move creates no update event. Normal record metadata remains. Add one Core RRule Draft; review passed. Derived Updated At inclusion and schema encoding remain unsettled. Packet115 Drafts,13 residual prose Claims; no runtime change.


#### Derived Updated At may be recorded — 2026-11-01

Allow old/new Updated At in the change delta when the value changes. It is derived audit data, not an independently authored time or an input to the timestamp maximum. Its capture does not constitute another business update. This supersedes the earlier omission suggestion; no mandatory copy or runtime option is introduced. The timestamp invariant remains MAX over accepted create/update events. Rule amendment review passed; no schema or runtime change.


#### Event happened and inserted times — 2026-11-01

Event Records have separate happened_at and inserted_at fields. happened_at is event time; inserted_at is Journal insertion time. Both Property Declarations require one datetime and no dependents. A shared Core R states their meanings without a clock or ordering policy. Updated At MAX uses happened_at. Author is the event performer; object_input/object_output shape remains the current question. Instance links belong under Relations. No Atom.Author is restored. Time-field review passed;118 Drafts,27 Primary/49 Property Declarations,13 prose Claims remain. No database/runtime change.


#### Atom input/output metadata and Content omission — 2026-11-01

Capture ID, Version and Updated At for each present Atom input/output side, before/after the change. Input and output IDs may differ. Add one short Core Rule. Exclude Atom.Content and descendants from Event Records for now; retain the event for an accepted Content-only update without recording Content paths/values. Timestamp selection uses the result/output identity. Projection Version remains the current question. Two-Rule review passed;119 Drafts and13 prose Claims remain. No schema encoding, event rows or runtime change.


#### Reviewed Event Record schema and formal timestamps — 2026-11-01

Projection has no Version. Add common input/output metadata maps, required id/updated_at and optional version; Atom capture requires Version, Projection forbids it. Create/update outputs and update inputs are required; creation input may be absent. Add action and canonical event-performer Actor link under Relations.HAS_EVENT_AUTHOR. Explicitly qualify create/update as accepted completed business events. Guarded MAX(happened_at) now makes Atom and Projection Updated At Declarations formal-only, matching output metadata and excluding irrelevant/absent fields. Integrated review passed after required-output and qualification safeguards. Packet132 Drafts,27 Primary/60 Property Declarations,11 prose Claims remain. No runtime, event row or projection Version was created.


#### Form is one string — 2026-11-01

Use the Operator’s Atom.Form string contract. Remove the additional admission/placeholder prose; keep required occurrence and zero dependents. The formal block is unchanged, and Form is formal-only. No generic admission helper is needed for this Property. Packet132 Drafts;10 descendant Declaration Claims retain prose. No runtime change.


#### Role string and Project Goal Tier direction — 2026-11-01

Use a single string for Atom.Role, retaining required occurrence and no dependents; named Role case Declarations remain. The Project-target Goal Tier is -1; no extra Tier rule for other Goals. Resolve the target Scope from the active Subject; do not add a Target Scope Unit Property. Define the exact mapping before changing the Tier Claim. The later explicit decision removes the Project Goal ownership requirement. No runtime change.

#### Passive Subject distinctness — 2026-11-01

COUNT and DISTINCT now express duplicate exclusion per Atom. Direct contextual-dependency meaning remains prose. Target Scope resolution from the active Subject is confirmed; the exact mapping remains open. The later explicit decision removes the Tier ownership requirement. Packet: 133 Drafts, 27 Primary and 60 Property Declarations, 10 residual prose Claims. Draft-only review; no parser or runtime implementation.

#### Relation notation prose retained — 2026-11-01

Keep the conditional `notation_for_subject` requirement in prose for now. Defer its formalization; preserve the Declaration. Ten descendant Declaration Claims still contain prose.

#### Projection Sources narrowed — 2026-11-01

Projection.Sources contains only Atom IDs with explicit Versions. Remove extra dependency-provenance wording and the duplicate broader source bullet from the Projection Declaration. Cardinalities are unchanged; the short format constraint remains prose. No Current source or runtime change.

#### Project Goal ownership requirement removed — 2026-11-01

Remove Operator ownership from the Tier Declaration. Do not create a separate Core R for it. The Operator registry and numeric Tier block are unchanged; exact active-Subject-to-target-Scope binding remains open.

#### Projection Source Of Truth removed — 2026-11-01

Withdraw the separate Source Of Truth Property. Sources remains the list of Atom IDs with Versions. Projection ID now determines, and is determined by, Form and Named Selection. Do not add mutable source Versions to that identity basis. Current packet: 132 Drafts, 27 Primary and 59 Property Declarations; 9 residual prose Claims. Current sources and runtime remain unchanged.

#### Projection Declaration cleanup — 2026-11-01

Projection creation and editing instructions belong to Operations. Its Declaration Claim is formal-only, with a short Semantics sentence preserving the source-Claim boundary. A separate D Draft states `Projection// >> Carrier/Markdown_file//`. Source Versions remain defined only by Projection.Sources. Packet: 133 Drafts, 27 Primary and 59 Property Declarations; 8 residual prose Claims and 79 formal-only Claims. No Current or runtime changes.

#### Journal prose retained — 2026-11-01

Keep the Journal rules in short prose bullet points. Formalization is deferred; the existing CFEL block is unchanged. Eight descendant Declaration Claims still contain prose.

#### MODEL prose retained — 2026-11-01

Keep MODEL rules in short prose bullet points. Formalization is deferred; the existing CFEL block is unchanged. Preserve optional local MODELs, inheritance, additions, any-rule overrides, the unchanged base and reuse of unmodified Declarations. Eight descendant Declaration Claims still contain prose.

#### MODEL wording narrowed to four points — 2026-11-01

Use the latest four prose points. Every Project uses CAPRMEDIO's MODEL. An optional local MODEL inherits it and may override any inherited rule. This replaces the earlier eight-point wording; the formal Claim block is unchanged. No runtime change.

#### Projection.Source grouping — 2026-11-01

Group the required Named Selection instance reference and optional concrete Atoms list under Projection.Source. The concrete list uses Atom IDs with Versions. Add the Source Property and Named Selection Primary Declarations; update both ID dependency paths. Preserve cardinalities and keep changing source Versions outside the stable ID basis. Existing strings need instance-reference binding at adoption; no actual instance migration. Packet: 135 Drafts, 28 Primary and 60 Property Declarations; 82 formal-only Claims and 7 residual prose Claims.

#### Journal topic and positive wording — 2026-11-01

Journal Claim prose now has two points: an ordered table of accepted Event Records; immutable accepted Event Records. Remove the other prose. Preserve the formal block. Add an authoring Method for positive wording, the active Subject and reuse of applicable shared rules. Packet: 136 Drafts; 7 Declaration Claims retain prose. No new syntax or runtime change.

#### Active Subject prose and Relation whitelist audit — 2026-11-01

Move immutability to Event Record; Journal keeps formal zero-or-more containment. Project owns required CAPRMEDIO MODEL use. MODEL keeps its inheritance constraint; permission boilerplate is removed. Shared Property bearing now has a formal exact-one count. Audit all 28 Primary and 60 Property Declarations for formal Relation whitelists. The whitelist encoding choice is pending; no complete effective whitelist or runtime implementation is claimed.

#### Subject ownership and two whitelist layers — 2026-11-01

Audit all 136 existing Draft Claims and prepare one new default-cardinality Rule. Journal owns containment; Event Record owns immutability. Structural-level Properties own their equations; Plan owns its container dependency. Other moved/shared rules preserve their constraints. Model-entity and instance whitelists use separate scopes, Node/** and Node/**//. The wildcard fallback is {:0}((*)); {:x} remains allowed-value notation. Full root/Property coverage is the current pending question. Packet: 137 Drafts; 8 Declaration Claims retain prose; complete effective whitelists and runtime enforcement remain open.

#### Node defaults inherited through the branch — 2026-11-01

Use `(Node, Node.**)` for model entities and `(Node//, (Node//).**)` for Node instances and their recursive Properties. Declare both wildcard zero defaults only in Node; descendants inherit them. Each inverse direction requires its own named permission; all applicable cardinalities are checked together. Preserve dependent Property traversal without independent instantiation. Shared-root review passed after allowing model Properties to bear nested Properties. Complete local whitelist and runtime validation remain open.

#### Node migration started — 2026-11-01

The Operator requested migration, then an expanded graph projection, then issue repair. The 137 registered preparation carriers now have unique Draft identities: R2462–R2588, M456–M460, D662–D665 and E669. Role/Form and Subjects.Active/Passive replace their legacy field names in these Drafts. Structural checks pass for 28 Primary and 60 Property Declarations; the 750 pinned Current Core R sources and Current Epic remain unchanged. [Migration tracking](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/node-declaration-20261031/migration-20261101/README.md) records the lifecycle and integration boundary.

1. Complete source dispositions and answer whether Definitions outside the smaller inventory are retired or retained.
2. Reconcile authored-schema authority and admit the allocated packet.
3. Replace mapped Current sources with exact predecessor archives and repair consumers.
4. Rebuild graph views from adopted Current sources, including supported CFEL facts and Property constraints. Report unsupported expressions explicitly.
5. Repair revealed model/projection issues and repeat the focused checks.

Graph element categories and Projection.Form remain separate classifications; Form replaces the former Atom Type field. Existing Workflow-instance review remains deferred.

#### Complete replacement inventory confirmed — 2026-11-01

The Operator confirmed that the 88 selected Declarations replace the old Node inventory. The live candidate manifest contains 291 Definition retirements and preserves 43 non-Node Definitions (18 CFEL, 23 Carrier, 2 Term). Resolve non-Definition consumers of omitted concepts separately; do not treat authorization to retire Definitions as authorization to drop their consumers’ independent Claims. Current lifecycle writes remain pending that disposition and authored-schema reconciliation.

#### Continuant and Occurrent retained — 2026-11-01

Latest Operator correction: Continuant and Occurrent remain in the model. The earlier 88-Declaration starting packet is not evidence that every other concept is deleted. Revise the replacement inventory and the 291-row Definition-carrier retirement plan before Current adoption. Preserve R1967/R1972 and applicable R1502/D654 Claims. The migration review list separates replacement of a Definition carrier from removal of its concept. No Current archive or promotion has run.

#### Node migration and graph refresh applied

139 prepared Atoms are Current, including 30 Primary Node and 60 Property Declarations. Continuant and Occurrent are retained through R2589/R2590; former Definition carriers are archived. The migration preserves 1,276 predecessor archives and records 302 retirements after the direct obsolete-rule fix. Twelve followup updates repair direct field/Claim conflicts and include the selected external Project Goal. CA-PROJ-014/015/016 are refreshed; CA-PROJ-017 is the declared-model Map. The 1,101-source frontier and readback receipts are in the [migration record](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/02_analysis/draft/node-declaration-20261031/migration-20261101/README.md).

This closes the agreed source publication and graph refresh slice. Legacy expressions remain explicit observations/diagnostics; full CFEL/native runtime validation and actual Operations instances remain deferred. No additional model concepts, axes, runtime mechanisms or Epic Tasks were added. This successor Draft records progress; Current Epic38 remains unchanged and the Epic is not automatically closed.

#### CFEL and full graph contracts — authorized work

Latest Operator scope: fix the 31 narrowing-tree diagnostics; provide the Subject graph with the complete formal contract for each entity; check and repair the CFEL description; describe and declare every Relation, including derived Relations. This supersedes the earlier omission of separate derived-Relation Declarations. Preserve one authored fact and explicit inverse permissions.

Execution order:

1. Record this work in the Epic.
2. Run the independent source, Relation, CFEL and projection lanes in parallel.
3. Review the combined drafts against the latest Operator decisions. Ask one real unresolved question at a time.
4. Archive exact predecessors, adopt the reviewed corrections, repair their direct consumers and record the changes.
5. Rebuild the narrowing tree and the graph with entity contracts. Verify source coverage, Relation coverage and focused tooling checks.

Parallel deliverables:

- Repair 16 legacy CFEL Subject expressions without changing composition into narrowing.
- Resolve the 14 legacy Entity-path Definitions and Event Record placement without inventing deferred model concepts.
- Declare canonical and derived Relations with meaning, direction, endpoints, notation and inverse binding.
- Align CFEL documentation with the admitted operators, selectors, conditions, value/Property contracts and Relation declarations.
- Render formal Claims, allowed Relations, formats, cardinalities and inherited/shared constraints beside their entities, with source IDs and Versions. Keep unresolved or prose-only rules visible.
- Verify coverage and conflicts independently before publication and after rebuilding.

Acceptance:

- Every reported diagnostic has an applied, source-backed disposition; none is silently hidden.
- Every modeled Relation, including derived Relations, has a Declaration. Derivation remains explicit and does not grant automatic inverse permission.
- Every selected entity has its complete available contract in the graph: own and inherited/shared constraints, direct values, dependent Properties, formats, cardinalities and allowed Relations. Missing or conflicting rules are explicit failures.
- The CFEL description covers the syntax actually used by those contracts; examples and parser/extraction checks agree.
- Current source changes preserve exact predecessors and summaries/identity constraints. Regenerated views cite actual Current Atom Versions.

Actual Workflow/Step/Substep/Action instance redesign, additional model concepts or axes, a general CFEL evaluator, runtime/MCP work and Git publication remain outside this request. This Epic remains open until its existing work is resolved.

#### Relation contracts and Project Settings — latest decisions

- Replace Relation Definition Atoms with Requirement / Declaration Atoms, including a Declaration for each derived Relation.
- Keep graph Relations and other CFEL operators distinct; each receives its appropriate Declaration.
- Each Relation has Semantics and formal metadata: its admitted short notation, Direct/Derived classification, and applicable counterpart/source binding. Use IS_DERIVED_RELATION_OF for derivation and HAS_INVERSE separately for endpoint reversal. Preserve independent permissions and cardinalities.
- All Project settings are Properties of Project, which narrows Scope Unit. Extend Project.Settings with source-backed existing fields and their dependent contracts. This supersedes the earlier deferral of the seven Framework Settings model fields; it does not authorize restoring the withdrawn Plan Retry Limit.
- The displayed graph must retain every relevant Claim clause, including unsupported formal text and essential prose. A successful extraction count is not evidence of complete semantics.
