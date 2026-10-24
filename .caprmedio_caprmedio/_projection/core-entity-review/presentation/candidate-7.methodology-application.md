# Candidate #7 — methodology application

Date: 2026-10-23.
State: the initial increment and bounded R/M, Subject and Eng-Type definition alignment are applied and checked; full migration not complete.

Latest accepted target update, 2026-10-23: one numeric Tier, parentage without an
authored Structural Level, same-scope/ancestor relation ordering, and the new
Tool responsibility structure are now recorded in the candidate. The later
2026-10-24 continuation applied bounded Current RMEDO increments and declared
the new Tool groups in Project Structure; see the completion record. Four
existing Tool Method contracts remain in Drafts. Implementation schemas and
runtime are not changed by this methodology work.

Current continuation record: [completion progress](candidate-7.completion-progress-2026-10-23.md). The 2026-10-24 source continuation includes recovered headers, Type/Target/Tier corrections, eighty further reviewed Subject-owner updates and nine obsolete/glossary-contract retirements. The eightieth applies the Operator's R1718 Content Role correction. Checking passed all 2,252 source pins in the refreshed scratch graph. Its 393 primary roots and twenty-five diagnostics still expose unresolved old Subjects; it is not a clean published projection or evidence of full migration.

Actual result: [applied methodology increment](candidate-7.methodology-increment-2026-10-22.md). The proposals and observations below describe the preparation baseline; the result summary and source-change records identify what was actually applied.

Latest result: [methodology alignment increment](candidate-7.methodology-alignment-2026-10-23.md). Six role/Subject definitions and the Delivery registry are updated; four Eng-Type definitions have successor IDs R2119–R2122; R2123 records the PROGRAMMATIC M/D restriction. Their 12 Current source carriers and 11 predecessor archives passed bounded checks. The source snippets below remain preparation history, not current Version pins.

Authority: [Candidate #7](operator.model.candidate-7.md), including the latest Operator decisions. This is an authored migration plan, not a source-derived Projection or an activated Atom. Source Versions below are observations, not immutable execution pins; re-read each source before applying its change.

## Boundary

This work changes methodology and its Governing Configurations: Subjects, their defining Atoms, Type definitions, property rules, identity rules, corresponding methodology Delivery rules and the configuration data those rules govern. Do not change tool code, implementation schemas, tests, MCP or runtime. Do not repair a missing execution binding as part of this work.

The methodology, not the code, is the source of truth. Express approved rules in methodology Atoms even when the current implementation cannot check them. Missing code support is separate implementation work; it must not block or redefine the approved methodology.

Latest Operator scope override: apply changes to Current RMEDO source Atoms and Governing Configurations. Do not migrate C/A/P, existing Drafts or existing Archives. Preserve unrelated governing configuration values. Universal model definitions may describe excluded forms, but their instance migration is not a gate for this pass. Earlier broader frontier and Draft-ID tasks below are superseded for this execution; keep them as history, not required work. Final affected views use Current RMEDO as their Atom selection and identify any included Governing Configurations separately.
Create a new predecessor archive for each Current RMEDO update, as explicitly confirmed by the Operator. Do not modify an existing Archived or Draft Atom.

Keep Core abstract and reusable. Project-specific procedures and choices remain in Project Configuration. Do not edit delivered copies as source authority. Preserve unrelated changes from the PROGRAMMATIC chat.

## Settled decisions

- Subject is the single root. Domain and Engineering are the current topic branches; Graph/Relation and Graph/Rule are global. UX and Design remain pending.
- Full paths preserve `/`, `.`, `:`, `//`, their meanings and inheritance. Do not turn a dependent property into a narrower kind.
- Each Atom may have at most one GOVERNS Subject and any number of DEPENDS_ON Subjects. The Subjects collection is optional.
- Current, Draft and Archived are distinct groups. Done, Canceled and Backlog can be Current.
- IDs are mandatory in all three groups. A new numbered Draft reserves its base ID; an edit Draft reuses its source base.
- Archived ID and filename use `@Version`. Set Status to Archived and use the correct folder. Keep the archived Version consistent in every occurrence; do not increment it just for archiving or change Updated At or unrelated content. Exact-old-bytes preservation is obsolete.
- Drafts may be incomplete. Report missing fields; enforce full applicable mandatory fields and content before promotion to Current.
- Label means the explicit Label, or the Type name when Label is absent. No redundant explicit Label is required.
- R specifies required results and runtime behavior, including delivery guarantees, error-rate limits and request-time targets. M specifies how to achieve them, including coding policies and engineering decisions. Mandatory architecture is still M, not a runtime result.
- Subjects and Content Roles are independent by definition. R includes functional requirements about business/domain logic and non-functional requirements about speed, performance and other runtime outcomes. R can have an Engineering Subject; it is not restricted to Domain.
- M and D: local Eng Policy ownership requires at least one actual, currently
  declared child Scope Unit and automatic application to every child under
  genuine topic/environment conditions. A leaf may inherit but cannot locally
  own a Policy. Eng Decision is a Scope-Unit-specific choice without automatic
  rule inheritance. Both can be reused; a technology name does not decide the
  Type. Do not invent artificial children. These names replace
  Policy/Engineering Decision for these Roles. E remains Policy and Eval Case;
  an Eval Case may use deterministic tests, LLM evaluation prompts, or both.
- Within PROGRAMMATIC and its descendants, M/D Atoms use only Eng Policy or Eng Decision. Classify legacy and missing M/D Types into those two; preserve appropriate specialized Types only outside that scope.
- For this migration only, classification-only Type corrections retain ID when Summary and Substance are unchanged. Do not generalize this exception to other changes.
- Missing Author in this project is Anatoly Maslennikov, as directly confirmed. No general fallback rule is introduced.
- Each Atom has one numeric Tier, carried as `tier`: Project ordinary Atoms use
  integers >=0; non-Project Atoms use integers >=1. Project Goal is a distinct
  Requirement Type, owned by the Operator and targeting the Project, with Tier
  exactly -1. Identify it by its Project target, not Project placement. The
  Operator Actor owner is the established exception to ordinary Local Scope
  Unit ownership; do not fabricate a Scope Unit for the Operator. Other Goals
  target non-Project Scope Units and use ordinary ownership. Numbers are unbounded. Any admitted Type may
  use any Tier admitted at its Local Scope Unit. Remove the old Local/Global
  Tier split and do not persist a replacement global rank.
  Store only the integer in Atom properties; explanatory names are not Tier
  values and no new names are required for additional numbers.
- Latest Operator clarification: Tier numbers express graph ordering, not
  named semantic classes. Preserve valid existing numbers and assign higher
  numbers where a governing same-Scope relation requires them. Missing targets,
  cycles and cross-Scope conflicts remain separate issues, not passing checks.
- Scope Unit parentage is enough hierarchy authority. Retire authored
  `structural_level`; ancestry comes from the declared parent chain.
- Governing R/M/E/D relation directions, including evaluation-for, method-for,
  delivery-for and applicable hierarchy/dependency links, target a strictly
  lower Tier in the same Local Scope Unit OR an Atom in a strict ancestor
  Scope Unit with no Tier comparison. Descendant and sibling targets do not
  pass this rule. Other Relation Type endpoint and cardinality rules remain.
  Derived inverses are not additional stored governing edges.
- Formal Graph Rule Atoms use operative YAML instead of Substance; optional
  Semantics and Details remain optional. The ordering rule now has the narrow
  Endpoint Constraint format defined by Current D637 and R2149. Code support
  remains separate implementation work.

## Source-root definition changes

Authoritative directory:

`.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement`

### CA-R-2004 — Define Subject Target

Observed source: `CA-R-2004-CORE_META_MODEL-CORE--define-subject-target.md`, Version 1.

Retain ID and Summary. Next proposed Version: 2. Type: Definition. Proposed Subject fields:

```yaml
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
    - Subject
```

Proposed content:

```markdown
## Scope

A direct GOVERNS or DEPENDS_ON target in an Atom's Subjects.

## Claim

A Subject Target is the topic addressed by a canonical Subject expression. Its full path starts at Subject. A Subject can identify a kind, a dependent property, an allowed value or a named instance; it need not identify an independently carried object.

## Semantics

Subject says what an Atom concerns. Content Role says what its content does. They are independent by definition. An Atom of any RMED Role can govern a Domain topic, an Engineering topic or a Graph topic. A topic about how work is performed does not require a separate Method root.

The Subject does not repeat or assign the Atom's Local Scope Unit, folder or Carrier. Topic meanings come from source use and Semantics; the Terms Graph derives definitions from those cases rather than creating another authority layer.
```

This removes the old Entity-or-Method-only restriction. Preserve the useful distinction between a topic and the Atom describing it.

### CA-R-2005 — Define Method Topic

Observed source: `CA-R-2005-CORE_META_MODEL-CORE--define-method-topic.md`, Version 1.

Disposition: retire the obsolete separate Method-root definition after CA-R-2004's replacement preserves its useful topic-versus-object meaning and after its actual consumers are reviewed. Do not relabel this Atom as a general Engineering definition while retaining its old identity. The archive uses ID CA-R-2005@1 and Status Archived; do not create another Version just to archive it.

This disposition does not retire Method Atoms, engineering topics, source-derived Terms or guidance Projections. It retires the requirement that those topics live under a separate Method root.

### CA-R-2006 — Define Subject Target Roots

Observed source: `CA-R-2006-CORE_META_MODEL-CORE--define-subject-target-roots.md`, Version 1.

Retain ID and Summary. Next proposed Version: 2. Type: Rule. Proposed Subject fields:

```yaml
subjects:
  governs: Subject
```

Proposed content:

```markdown
## Scope

Canonical Subject paths in this model.

## Claim

Every canonical Subject path starts at Subject. Domain and Engineering are the current product-topic branches. Graph is a global topic namespace with Relation and Rule topics that apply within and across branches.

## Semantics

Domain names what the project means and offers. Engineering names how it is structured, built, stored and operated. Graph names connections and their constraints. These branches do not assign a Content Role and do not replace the kinds described by the graph.

The model can expand. UX and Design are not admitted targets for this migration. A Scope Unit path is not automatically a Subject path.
```

## Remaining methodology work

### R/M and Eng Type alignment — definitions applied; consumers pending

CA-R-1339/CA-R-1340 now state the result-versus-means distinction; CA-R-1548/CA-R-1694 retain the methodology's own model-definition coverage. CA-R-2004/CA-R-2006 record role/Subject independence and the global Graph namespace. Their current Versions and archives are in the latest result record. Do not silently retire Definition or Graph Rule Atoms as a consequence of software-runtime examples.

CA-R-2119 through CA-R-2122 replace CA-R-2111 through CA-R-2114 as the Method
and Delivery Eng-Type definitions; the old definitions are archived. CA-R-1665
points to the new Delivery definitions, and CA-R-2123 states the project-local
restriction. Align the remaining current consumers to Eng Policy/Eng Decision
and the actual-child, every-child and leaf-inheritance rules above. PROGRAMMATIC and its descendants
admit only these two M/D Types; preserve appropriate specialized Types only
outside that scope. Both Types may be reused. Do not
infer Policy from abstract wording or Decision merely from a named technology.
Do not impose a Type-to-Tier restriction. Evaluation Policy is outside this
rename. Recheck actual declarations before moving or promoting a Policy; a
planned responsibility group is not an actual child yet.

Follow the existing identity/history rules when source Summaries or Types change. These notes are not evidence of active Atom updates, consumer migration, rebuilt Projections or runtime changes. Do not turn this terminology alignment into a new ADR publication Type or workflow.

### Bounded source mapping

Four Luna lanes inspected the current source material. Their inventories have different scopes and overlap; do not add their counts or call them a full-project migration frontier.

| Lane | Result | Limit |
| --- | --- | --- |
| Core Domain/Graph | Bounded report maps 198 of 246 Entity-root endpoint strings; 48 need Engineering routing or source-specific repair | Prefix families are templates, not an exact executable occurrence map. Generic Entity references, identity and old Revision topics require their actual governed meaning. |
| Engineering | 45 literal old Method-topic paths plus Carrier paths and Domain/Graph counterexamples | M/E/D only; feature-specific names remain held until mapped from source content. Folder or Content Role is not sufficient evidence. |
| Properties and identity | Existing R/D rule conflicts and proposed replacement text | Source-authoring preparation only; no tool or schema update is included. |
| Types | Category definitions and existing Type registration worklist; 866 of 951 direct Active Core/Project Configuration RMED carriers lack explicit Type | Those 866 assignments are unreviewed classification work, not 866 Operator questions. Missing Type requires semantic classification, not a default inferred from Role or tier. PROGRAMMATIC M/D assignments use only Eng Policy or Eng Decision; appropriate existing specialized Types remain valid outside that scope. |

Preparation notes are in `.caprmedio_tmp/candidate7-migration-20261022/`: `domain-map.md`, `engineering-map.md`, `property-rule-alignment.md` and `type-rule-alignment.md`. These are scratch research inputs, not authoritative Atoms or migration receipts. A held case is not silently dropped or turned into a new Operator question if it can be resolved from the source and already settled decisions.

### Source-rule alignment groups

| Existing sources | Required methodology change |
| --- | --- |
| R1198, R1201, R1363, D269 | Optional Subjects; at most one GOVERNS and any number of DEPENDS_ON. Preserve the existing YAML keys. Replace an identity if its Summary must change rather than quietly rewriting that Summary under its old ID. |
| D276, D378, D446, D288 | Mandatory group-specific IDs; Draft incompleteness; required Current metadata; no empty-number Draft identities. |
| D283, D289, D565, D570 | Consistent version-qualified archived identity and Draft lineage. Do not append a second version suffix to an already qualified ID. Do not normalize all historical filenames without a reviewed mapping. |
| R1432, R1788, D446 | General predecessor archive treatment: archive Status, ID/filename qualifier and folder change; archived numeric Version, Updated At and unrelated content stay unchanged. The new Current successor follows its normal Version/time rules. Git retains the exact pre-change file. |
| R1766 | Preserve ordinary Type identity semantics; record the one-time classification-only exception as a migration decision, not a new universal fallback. |
| R1594 | Effective Label: explicit Label, otherwise Type name. No redundant stored Label. |
| R2101 and historical R1393 consumers | Replace the obsolete omitted/string Local Tier treatment with owner Project and numeric `tier: -1`. Do not resurrect an absent historical source. |
| D291 and relevant property definitions | Local Scope Unit terminology, distinct from Target Scope Unit; preserve current serialized field names until their D mapping changes explicitly. |
| R1078, D274 | Required Current Author with no new Core fallback; this project's missing values use the Operator's confirmed authorship. |
| D479, D637 | Incomplete Draft body allowed; applicable completeness before Current promotion; preserve the formal Graph Rule operative-YAML exception. |

These IDs identify the affected source rules, not a blanket authorization to change every consumer's meaning or Summary. The full paths and observed Versions are in the source-alignment notes.

### Numeric Tier and parentage migration — accepted worklist

Execution update, 2026-10-24: the numeric contract and bounded data increments are applied; this table remains the impact worklist, not an assertion that every listed source is still pending. The completion-progress document distinguishes verified increments from remaining endpoint and Scope conflicts. For a verified Operator-owned Project Goal, the target Project supplies derived ordering context without replacing its Actor owner or adding a stored field.

The exact model is recorded in Candidate #7 under “One numeric Tier” and “Tier
and Scope Unit ordering for governing relations.” Apply the old-field removal
and the new rule as a coordinated successor, not as an unexplained metadata
cleanup.

| Sources to review | Required change |
| --- | --- |
| R1287, R155, R658, R659, R1431, R660, R680, R1442, R1443 | Define one numeric Tier, its owner-relative ranges and initial names; remove the finite Local Tier value model without losing useful meanings. |
| R1444, R1413, R1573, R1777, R1388–R1391 | Retire or replace the Global Tier property and derivation rules. Preserve independent useful constraints; do not maintain a hidden stored global rank. |
| R2101, R2102, D276 and actual field consumers | Use mandatory numeric `tier`; the distinct Project Goal Type targets Project, is owned by the Operator Actor instead of a Local Scope Unit, and carries -1. Other Goals target non-Project Scope Units with ordinary ownership. Replace `local_tier` and `global_tier` explicitly in the carrier contract before data migration. |
| R1751, R1730, R1485, R1932, R1731, R1737, M291, D297, D299, D300, D442, D445 | Review Structural Level references. Retain meaningful parentage, ownership and irreducible-boundary constraints; remove authored depth as governing metadata. Do not retire an unrelated claim merely because it mentions levels. |
| D285, D484 and filename consumers | Align numeric Tier with admitted display names without inventing another required rank or silently renaming historical carriers. |
| Governing Relation Type and Graph Rule sources | Add same-owner strictly-lower-Tier OR strict-ancestor ordering. Map exact registered relation kinds and preserve their independent endpoint/cardinality rules. Do not limit the rule to child-of or apply it to derived inverses. |

The active old source rules and serialized data still require their own reviewed
replacement/archive mapping. Source IDs here are an impact worklist, not a
claim that all replacements are prepared or adopted. Before authoring formal
operative YAML, settle the admitted rule representation using the current Graph
Rule format; this plan does not invent an executable schema.

PROGRAMMATIC reports held Task CA-P-2636 under Epic CA-P-2401 for consumer
migration planning. That report is coordination evidence only, not verified
implementation. Scope Unit mutation work remains in Stage 2 CA-P-2480. The
clarified ancestor rule has been sent to CA #3: PROGRAMMATIC without authorizing
code, configuration, runtime or release changes.

### Tool responsibility structure — four Draft contracts

The accepted target tree is in Candidate #7 under “PROGRAMMATIC Tool structure.”
It is target-first for Single Actions, not Find/Fetch/Check/Change first.
Adapters, Single Actions, Schedulers, actual Workflows and Action Engine are
modules/Scope Units inside one runtime, not separate services. Prompt lookup is
programmatic Find plus Fetch; there is no Prompt Helper group. Governing
Configuration is an adapter concern. Graph UI and Graph Server remain APPS.

Prepared Drafts (all Version 1; no Current promotion or implementation claim):

| Draft | Proposed owner | Numeric Tier | Contract |
| --- | --- | --- | --- |
| CA-M-433@1-draft | TOOLS | 1 | Tool module responsibilities |
| CA-M-434@1-draft | SINGLE_ACTIONS | 1 | Atom, Scope Unit, Projection, Journal, Project, Queue; operations inside each target |
| CA-M-435@1-draft | SCHEDULERS | 1 | Ordered Workflow scheduling, one batch per leaf step, at least one Single Action Run per batch, results returned to schedulers |
| CA-M-436@1-draft | ACTION_ENGINE | 3 | Execute queued Single Actions and record their results |

The Drafts live in the proposed owners' `05_method/drafts/` folders under
`201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/`. New group/target Scope Unit
declarations were applied to `project_structure.toml` on 2026-10-24. Keep existing
CONNECTOR_TOOLS, TOOL_WORKFLOWS, PROJECT_TOOLS and discovery-tool owners valid
until the actual source contracts/bindings have moved; do not delete those
declarations as a shortcut. Move code later, separately.

Active CA-M-432 records the modular-monolith Policy, but retains its existing
body. Its metadata must be read from its current source, not inferred from this preparation note. M433–M436 remain pre-existing Drafts outside the current execution boundary. The target Scope Unit declarations and bounded source-owner moves are applied; this is not evidence that the execution engine or runtime was migrated.

### Ordered continuation

1. Complete the literal Subject maps against current source Atoms, including dependent properties, classifier values, named instances and source-specific exceptions. A branch-prefix shortcut is not enough for old ambiguous topics.
2. Prepare the existing property, identity, Type and Delivery definitions for the settled decisions above. PROGRAMMATIC and its descendants admit only Eng Policy or Eng Decision for M/D; preserve meaningful specific Types and specialization rules outside that scope. Do not invent missing values or Type-to-tier restrictions.
3. Check the prepared changes against Candidate #7 and actual current sources. Keep held cases explicit. Do not claim a stale saved graph is a fresh full inventory.
4. Apply source changes only through an available authorized route. If the current route remains unavailable, report that boundary; do not turn methodology work into tool repair.
5. Rebuild source-derived views only after the corresponding source changes actually succeed. Mark preparation, application and derived output separately.

## Current application boundary

The existing CA-O-127 execution context was rechecked during preparation. It returned no input schema or tool binding and reported invalid binding evidence. The Operator answered the direct-file-edit question with “do without mcp”. The later “continue” followed the Tier discussion, not that question. This continuation authorizes direct methodology-file edits; it does not repair the MCP route or itself prove that those writes occurred.

Live methodology changes and predecessor archives are being recorded in the separate source-change files. Journal append, runtime activation, test-suite success, commits, releases and rebuilt Projections are not implied by those file edits.
