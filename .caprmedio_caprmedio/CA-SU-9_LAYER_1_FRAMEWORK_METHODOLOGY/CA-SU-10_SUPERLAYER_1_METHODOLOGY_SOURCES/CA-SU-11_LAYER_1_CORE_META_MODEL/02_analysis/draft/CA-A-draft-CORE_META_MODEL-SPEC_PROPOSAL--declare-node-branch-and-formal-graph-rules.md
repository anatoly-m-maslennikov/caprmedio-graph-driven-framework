---
atom_id: CA-A-draft
content_role: Analysis
type: Spec Proposal
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  governs: Entity/CFEL
version: 3
updated_at: 2026-10-31 00:13:49 +0400
relations: {}
tier: 3
---
# Summary

Declare the Node branch and derive the graph from Formal Claims

## Question

How should the graph model, Declaration Forms and notation change so that one coherent source declares each Node without repeated inherited definitions or ambiguous constraints?

## Scope

This proposal covers governing Drafts for the Node branch, graph Relations and notation, Role/Form naming, carrier mappings and formal Scope. It records the latest human decisions; earlier conflicting alternatives are superseded. The [Epic successor Draft](../../../../../03_plan/draft/CA-P-2694@39-draft-EPIC--entity-graph-refactor-stage-4-polishing.md) tracks adoption and implementation dependencies.

Actual Workflow, Step, Substep and Action instance review/migration is deferred by the latest Operator instruction. This pass reviews their model declarations and constraints; model-level examples do not perform instance review.

## Approach

Write the governing Drafts directly, keep the design rationale here, and review the packet before adoption. Preserve Current sources and completed publication history. Resolve exact source-to-Node mappings before replacing Definitions; never replace all `/` edges with composition.

## Results

### What changes

- **Carrier placement is explicit.** Use `@Carrier//Markdown file`. Deliver non-Content Objects into frontmatter. Deliver Content descendants into Markdown. Frontmatter is delimited YAML at the beginning of the file. Carrier filename/location are properties; location is repository-relative.
- **Node scope is explicit.** `Node/**, .**` selects narrower entities plus their Properties. Add `Node` when a rule also covers the root.

- **Names and values use separate expressions.** `p{:0..1}: [format]{:1}` separates occurrence from values. `p.*[...]` constrains immediate names. `p.**[...]` constrains names recursively. Expressions use semicolons.
- **Claim is one Property.** Keep `Atom.Content.Claim`. Formal content is an optional CFEL fence inside its Markdown value. No separate Formal Claim Property is retained. RMED Claim is required. Claim Scope, Semantics and Details are optional.
- **Delivery specifies representation.** `>>` delivers Objects to a referenced Carrier or its parts. Object means Node instance. Filename/location formula details remain separate until expressible.

- **Analysis is freeform.** `Atom.Content.**[string]{:0+}: [markdown]{:1}` constrains each dependent Property recursively. Sibling names are unique. `x.y.z` differs from `x.z`. Shared Atom constraints remain inherited.

- **Graph Syntax becomes CFEL — CAPRMEDIO Formal Expression Language.** CFEL covers expression syntax and meaning for Subject addresses and Formal Claims. Graph, CFEL and Carrier remain distinct model components. This names the existing language; it does not add notation.

- **Declaration is a Form of Requirement.** Use `Role: Requirement / Form: Declaration` and the existing R prefix. Within each selected effective MODEL, each declared member selected by `(Node, Node/**, .**)`, including Properties, has one effective Current Declaration with one matching active Subject. Count only those Declarations; other RMED may address the same Node. Use CFEL Formal Claims where possible. Use Claim prose only for constraints CFEL cannot express. Keep brief Semantics for Primary Nodes only. Each Property Declaration specifies two contracts: direct-value format/cardinality; dependent-entity format/cardinality. Unchanged inherited Properties reuse their original Declaration; explicit MODEL overrides select their local replacement. CFEL entities retain a Claim and may have Semantics.
- **Use Role and Form.** Rename Content Role to Role and the Role-specific Type to Form. These names express different purposes. Naming Methods prefer words that convey the actual distinction and reuse canonical expressions consistently; they do not impose a blanket word ban on useful contextual uses of `content`, `entity` or `type`.
- **Use two root kinds.** MODEL and PROJECT STRUCTURE are Primary Node kinds declared in CAPRMEDIO's self-describing MODEL. Their instance roots are `MODEL//CAPRMEDIO`, `PROJECT STRUCTURE//CAPRMEDIO`, and the corresponding consumer Project roots. The consumer MODEL is optional. PROJECT STRUCTURE describes Scope Structure, Aspects and other declared components. Core Meta-Model contains the Atoms defining CAPRMEDIO's MODEL. Extensible axis configuration stays deferred.
- **Declare Scope outside the constrained Unit.** State permitted active/passive Subjects and Relation endpoints/cardinalities. ENGINE's proposed Scope permits allowed instances and implementation RMED; model definitions use their declared model-defining Scope. A local MODEL does not automatically widen ENGINE's Scope. Target Scope never grants wider authority.
- **Keep graph meanings distinct.** `/` narrows Primary Nodes with inheritance, `//` names their instances, `.` addresses Properties, `+>`/`<+` expresses composition, and `>|`/`|<` expresses classification. Composition uses canonical IS_CONTAINED_BY and derived CONTAINS; Container has yes/no value cases. `(Node, Node/**, .**)` includes the root, its recursive narrower branch and their recursive Properties. `@` references an existing target, parentheses group, and `in (...)` states membership. `:` denotes an allowed value, `=` tests, and `==` establishes a required/derived conclusion. In Subjects, `:=` combines allowed value and condition, as in `Atom/(.Role := Method)`. It does not write an instance value or exclude other allowed values from Atom.Role. Formal Claims keep `:` and `=` separate. Full Formal Claims stay out of Subjects; `..` and an invented `::` meaning are excluded.
- **Keep both counts.** Relation cardinality constrains both written directions; reversal swaps the counts. Property syntax uses separate expressions for occurrence, direct values and immediate dependent names: `p{:occurrence count}; p: [value format]{:value count}; p.*[name format]{:child count}`. YAML and Markdown mappings preserve that distinction, including mixed section content and nested headings.
- **Derive Primary Node versus Property.** The Node branch permits zero or one IS_PROPERTY_OF bearer. Zero derives Primary Node and no direct value; one derives Property and forbids narrowing and instantiation. Property-bearing must be acyclic. HAS_VALUE binds a Property on an instance to a literal, such as CA-P-123.version = 1; literals do not become declared graph Nodes.
- **Inheritance supplies effective rules.** Narrower instances receive applicable Relation cardinalities and declared Property constraints. Do not redeclare an inherited Property or create a new Declaration merely for an inherited lookup. Each Node's single effective Declaration in the selected MODEL resolves its Relation whitelist, endpoint constraints and counts. MODEL inheritance may replace any inherited rule through an explicit local override; unchanged Declarations are reused. Inheritance neither copies instance facts nor gives a Property a second bearer.
- **Operations use siblings and explicit composition.** Workflow, Step, Substep and Action narrow Operations. Each Workflow has one or more Steps, each Step one Workflow. A Step exclusively runs one Action or contains one or more Substeps. Each Substep has one Step and runs one Action. Actions may have zero or more callers. RUN bindings do not establish execution evidence.
- **Store authored instance Relations once.** Rename Subject links to active/passive; store modeled authored Node-instance links under `relations`, with typed containment references. Derive HAS_ACTIVE_SUBJECT from the dedicated Subject field and derive inverse views. The exact Assignee/Target reference migration remains open.

Relation Definitions now state allowed Host/Target signatures and reuse `Direct ((HAS_INVERSE)) Derived`. Inverse views have no separate Definition Atom. Repeated migration commentary is removed from the governing Drafts.

### Why these changes

The human rationale is to remove words that add no useful distinction, keep each complete expression precise, and avoid defining inherited material repeatedly. Primary Nodes, Properties, narrowing, composition and classification need different meanings so the graph can express constraints faithfully. A formal Scope outside its Unit makes the Unit's permitted authority explicit. One Declaration gathers a Node's structure and permissions; formal rules support graph reconstruction without turning an address into a second programming language. Syntax explanations remain useful where symbols are not self-explanatory.

### MODEL and PROJECT STRUCTURE — latest architecture

The two kinds are declared in MODEL//CAPRMEDIO itself. The named Subject roots are their instances:

```text
MODEL//CAPRMEDIO
PROJECT STRUCTURE//CAPRMEDIO
    <+ Scope Structure
    <+ Aspects

MODEL//<PROJECT NAME>              (optional)
PROJECT STRUCTURE//<PROJECT NAME>
    <+ Scope Structure
    <+ Aspects
```

The Project name above is a placeholder. A Project uses MODEL//CAPRMEDIO. It may define a local MODEL. A local MODEL inherits MODEL//CAPRMEDIO and may override any inherited rule. No inherited rule requires an overridable marker.

One Current authoritative Declaration per Node means one effective Declaration within the selected MODEL. Unchanged inherited Declarations are reused. A local replacement and its base source can coexist without becoming two effective owners in that MODEL. This selection context is distinct from the Project-wide instance context used by UNIQUE.

Core Meta-Model is a Scope Unit in CAPRMEDIO's Scope Structure. It contains the governing Atoms defining MODEL//CAPRMEDIO, including the two root kinds. This self-description does not identify the MODEL instance with its Scope Unit or PROJECT STRUCTURE instance. Existing ordered Scope Unit proposals remain subject to exact registration and mapping.

Model inheritance connects MODEL instances. It is separate from `/` Node narrowing and `<+` containment. The inheritance Relation name and exact Model-selection/override binding still need specification; this pass adds no invented notation or runtime behavior.

This replaces the earlier owner-wrapper layout and the MODEL-versus-PROJECT root split. The rationale is to distinguish reusable declarations from each Project's actual structure, reuse inherited material, and let each local MODEL control all of its effective rules.

### Adopted Atom register

The 139 registered Atoms are Current. The inventory includes 30 Primary Node and 60 Property Declarations. Each row links to its adopted Atom Version. The [migration record](node-declaration-20261031/migration-20261101/README.md) records predecessor archives, direct fixes, graph rebuilding and verification limits. Earlier preparation counts below are historical.

| Atom Version | Role / Form | Current Atom |
|---|---|---|
| `CA-R-2462@2` | Requirement / Declaration | [Declare Node](../../04_requirement/CA-R-2462-CORE_META_MODEL-DECLARATION--declare-node.md) |
| `CA-R-2463@2` | Requirement / Declaration | [Declare Operations](../../04_requirement/CA-R-2463-CORE_META_MODEL-DECLARATION--declare-operations.md) |
| `CA-R-2464@2` | Requirement / Declaration | [Declare Workflow](../../04_requirement/CA-R-2464-CORE_META_MODEL-DECLARATION--declare-workflow.md) |
| `CA-R-2465@2` | Requirement / Declaration | [Declare Step](../../04_requirement/CA-R-2465-CORE_META_MODEL-DECLARATION--declare-step.md) |
| `CA-R-2466@2` | Requirement / Declaration | [Declare Substep](../../04_requirement/CA-R-2466-CORE_META_MODEL-DECLARATION--declare-substep.md) |
| `CA-R-2467@2` | Requirement / Declaration | [Declare Action](../../04_requirement/CA-R-2467-CORE_META_MODEL-DECLARATION--declare-action.md) |
| `CA-R-2468@2` | Requirement / Rule | [Register Declaration as a Requirement Form](../../04_requirement/CA-R-2468-CORE_META_MODEL-RULE--declaration-form-registration.md) |
| `CA-R-2469@2` | Requirement / Rule | [Require one Declaration for each Node](../../04_requirement/CA-R-2469-CORE_META_MODEL-RULE--declaration-one-owner-per-node.md) |
| `CA-R-2470@2` | Requirement / Rule | [Inherit Declaration constraints and enforce Relation whitelists](../../04_requirement/CA-R-2470-CORE_META_MODEL-RULE--declaration-inheritance-and-relation-whitelist.md) |
| `CA-R-2471@2` | Requirement / Rule | [Use distinct graph notation for Node relations](../../04_requirement/CA-R-2471-CORE_META_MODEL-CFEL--use-node-graph-notation.md) |
| `CA-R-2472@2` | Requirement / Rule | [Separate Property names and values](../../04_requirement/CA-R-2472-CORE_META_MODEL-CFEL--separate-property-value-and-child-constraints.md) |
| `CA-R-2473@2` | Requirement / Relation Definition | [Define Property bearing and its inverse](../../04_requirement/CA-R-2473-CORE_META_MODEL-RELATION_DEFINITION--define-property-bearing.md) |
| `CA-R-2474@2` | Requirement / Rule | [Bind direct Property values on instances](../../04_requirement/CA-R-2474-CORE_META_MODEL-RULE--bind-direct-property-values.md) |
| `CA-R-2475@2` | Requirement / Relation Definition | [Define NARROWER_THAN](../../04_requirement/CA-R-2475-CORE_META_MODEL-RELATION_DEFINITION--define-narrowing.md) |
| `CA-R-2476@2` | Requirement / Relation Definition | [Define INSTANCE_OF](../../04_requirement/CA-R-2476-CORE_META_MODEL-RELATION_DEFINITION--define-instantiation.md) |
| `CA-R-2477@2` | Requirement / Relation Definition | [Define classification and its written reverse](../../04_requirement/CA-R-2477-CORE_META_MODEL-RELATION_DEFINITION--define-classification.md) |
| `CA-R-2478@2` | Requirement / Relation Definition | [Define composition and its inverse](../../04_requirement/CA-R-2478-CORE_META_MODEL-RELATION_DEFINITION--define-composition.md) |
| `CA-R-2479@2` | Requirement / Relation Definition | [Define the derived active Subject link](../../04_requirement/CA-R-2479-CORE_META_MODEL-RELATION_DEFINITION--define-active-subject-link.md) |
| `CA-R-2480@2` | Requirement / Relation Definition | [Define RUN](../../04_requirement/CA-R-2480-CORE_META_MODEL-RELATION_DEFINITION--define-run.md) |
| `CA-M-456@2` | Method / Implementation Method | [Name Model Concepts with Canonical Terms](../../05_method/CA-M-456-CORE_META_MODEL-IMPLEMENTATION_METHOD--name-model-concepts-with-canonical-terms.md) |
| `CA-R-2481@2` | Requirement / Rule | [Use Role and Form for Declaration Atoms](../../04_requirement/CA-R-2481-CORE_META_MODEL-RULE--use-role-and-form.md) |
| `CA-R-2482@2` | Requirement / Rule | [Declare Formal Scope Independently of Scope Unit](../../04_requirement/CA-R-2482-CORE_META_MODEL-RULE--declare-formal-scope.md) |
| `CA-D-662@2` | Delivery / Eng Decision | [Encode Node Declarations in YAML](../../07_delivery/CA-D-662-CORE_META_MODEL-ENG_DECISION--encode-node-declarations-in-yaml.md) |
| `CA-E-669@2` | Evaluation / Eval Policy | [Check Node Declaration migration readiness](../../06_evaluation/CA-E-669-CORE_META_MODEL-EVAL_POLICY--check-node-declaration-migration-readiness.md) |
| `CA-D-663@2` | Delivery / Eng Decision | [Map Markdown headings to Property paths](../../07_delivery/CA-D-663-CORE_META_MODEL-ENG_DECISION--map-markdown-headings-to-property-paths.md) |
| `CA-R-2483@2` | Requirement / Rule | [Separate the CAPRMEDIO model from Project structure](../../04_requirement/CA-R-2483-CAPRMedio-RULE--separate-the-model-from-project-structure.md) |
| `CA-R-2484@2` | Requirement / Rule | [Classify permission to have parts as Container](../../04_requirement/CA-R-2484-CORE_META_MODEL-RULE--admit-container-classification.md) |
| `CA-R-2485@2` | Requirement / Relation Definition | [Define HAS_INVERSE](../../04_requirement/CA-R-2485-CORE_META_MODEL-RELATION_DEFINITION--define-has-inverse.md) |
| `CA-R-2486@2` | Requirement / Rule | [Declare Relation endpoints](../../04_requirement/CA-R-2486-CORE_META_MODEL-RULE--declare-relation-endpoints.md) |
| `CA-M-457@2` | Method / Implementation Method | [Reuse formal notation and write isolated constraints in prose](../../05_method/CA-M-457-CORE_META_MODEL-IMPLEMENTATION_METHOD--reuse-formal-notation-and-write-isolated-constraints-in-prose.md) |
| `CA-R-2487@2` | Requirement / Entity Definition | [Define CFEL](../../04_requirement/CA-R-2487-CORE_META_MODEL-ENTITY_DEFINITION--define-cfel.md) |
| `CA-R-2488@2` | Requirement / Declaration | [Declare Atom.Status](../../04_requirement/CA-R-2488-CORE_META_MODEL-DECLARATION--declare-atom-status.md) |
| `CA-R-2489@2` | Requirement / Declaration | [Declare Atom.Updated At](../../04_requirement/CA-R-2489-CORE_META_MODEL-DECLARATION--declare-atom-updated-at.md) |
| `CA-R-2490@2` | Requirement / Declaration | [Declare Atom.Relations.IS_CONTAINED_BY](../../04_requirement/CA-R-2490-CORE_META_MODEL-DECLARATION--declare-atom-relations-contained-by.md) |
| `CA-R-2491@2` | Requirement / Declaration | [Declare Atom.Relations.IS_CONTAINED_BY.atom](../../04_requirement/CA-R-2491-CORE_META_MODEL-DECLARATION--declare-atom-relations-contained-by-atom.md) |
| `CA-R-2492@2` | Requirement / Declaration | [Declare Atom.Relations.IS_CONTAINED_BY.scope_unit](../../04_requirement/CA-R-2492-CORE_META_MODEL-DECLARATION--declare-atom-relations-contained-by-scope-unit.md) |
| `CA-R-2493@2` | Requirement / Declaration | [Declare Atom.ID](../../04_requirement/CA-R-2493-CORE_META_MODEL-DECLARATION--declare-atom-id.md) |
| `CA-R-2494@2` | Requirement / Declaration | [Declare Atom.Role](../../04_requirement/CA-R-2494-CORE_META_MODEL-DECLARATION--declare-atom-role.md) |
| `CA-R-2495@2` | Requirement / Declaration | [Declare Atom.Form](../../04_requirement/CA-R-2495-CORE_META_MODEL-DECLARATION--declare-atom-form.md) |
| `CA-R-2496@2` | Requirement / Declaration | [Declare Atom.Version](../../04_requirement/CA-R-2496-CORE_META_MODEL-DECLARATION--declare-atom-version.md) |
| `CA-R-2497@2` | Requirement / Declaration | [Declare Atom.Label](../../04_requirement/CA-R-2497-CORE_META_MODEL-DECLARATION--declare-atom-label.md) |
| `CA-R-2498@2` | Requirement / Declaration | [Declare Atom.Content](../../04_requirement/CA-R-2498-CORE_META_MODEL-DECLARATION--declare-atom-content-content.md) |
| `CA-R-2499@2` | Requirement / Declaration | [Declare Atom.Content.Summary](../../04_requirement/CA-R-2499-CORE_META_MODEL-DECLARATION--declare-atom-content-summary.md) |
| `CA-R-2500@2` | Requirement / Declaration | [Declare Atom.Content.Claim](../../04_requirement/CA-R-2500-CORE_META_MODEL-DECLARATION--declare-atom-content-claim.md) |
| `CA-R-2501@2` | Requirement / Declaration | [Declare Atom.Content.Claim Scope](../../04_requirement/CA-R-2501-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-scope.md) |
| `CA-R-2502@2` | Requirement / Declaration | [Declare Atom.Content.Semantics](../../04_requirement/CA-R-2502-CORE_META_MODEL-DECLARATION--declare-atom-content-semantics.md) |
| `CA-R-2503@2` | Requirement / Declaration | [Declare Atom.Content.Details](../../04_requirement/CA-R-2503-CORE_META_MODEL-DECLARATION--declare-atom-content-details.md) |
| `CA-R-2504@2` | Requirement / Declaration | [Declare Atom.Tier](../../04_requirement/CA-R-2504-CORE_META_MODEL-DECLARATION--declare-atom-tier.md) |
| `CA-R-2505@2` | Requirement / Declaration | [Declare Atom.Tier.Label](../../04_requirement/CA-R-2505-CORE_META_MODEL-DECLARATION--declare-atom-tier-label.md) |
| `CA-R-2506@2` | Requirement / Declaration | [Declare Atom.Subjects.Passive](../../04_requirement/CA-R-2506-CORE_META_MODEL-DECLARATION--declare-atom-subjects-passive.md) |
| `CA-R-2507@2` | Requirement / Declaration | [Declare Atom.Relations](../../04_requirement/CA-R-2507-CORE_META_MODEL-DECLARATION--declare-atom-relations.md) |
| `CA-R-2508@2` | Requirement / Declaration | [Declare Atom](../../04_requirement/CA-R-2508-CORE_META_MODEL-DECLARATION--declare-atom.md) |
| `CA-R-2509@2` | Requirement / Declaration | [Declare Atom/(.Role := Concern)](../../04_requirement/CA-R-2509-CORE_META_MODEL-DECLARATION--declare-concern.md) |
| `CA-R-2510@2` | Requirement / Declaration | [Declare Atom/(.Role := Analysis)](../../04_requirement/CA-R-2510-CORE_META_MODEL-DECLARATION--declare-analysis.md) |
| `CA-R-2511@2` | Requirement / Declaration | [Declare Atom/(.Role := Plan)](../../04_requirement/CA-R-2511-CORE_META_MODEL-DECLARATION--declare-plan.md) |
| `CA-R-2512@2` | Requirement / Declaration | [Declare Atom/(.Role := Requirement)](../../04_requirement/CA-R-2512-CORE_META_MODEL-DECLARATION--declare-requirement.md) |
| `CA-R-2513@2` | Requirement / Declaration | [Declare Atom/(.Role := Method)](../../04_requirement/CA-R-2513-CORE_META_MODEL-DECLARATION--declare-method.md) |
| `CA-R-2514@2` | Requirement / Declaration | [Declare Atom/(.Role := Evaluation)](../../04_requirement/CA-R-2514-CORE_META_MODEL-DECLARATION--declare-evaluation.md) |
| `CA-R-2515@2` | Requirement / Declaration | [Declare Atom/(.Role := Delivery)](../../04_requirement/CA-R-2515-CORE_META_MODEL-DECLARATION--declare-delivery.md) |
| `CA-R-2516@2` | Requirement / Declaration | [Declare Atom/(.Role := Requirement)/(.Form := Declaration)](../../04_requirement/CA-R-2516-CORE_META_MODEL-DECLARATION--declare-requirement-declaration.md) |
| `CA-R-2517@2` | Requirement / Declaration | [Declare Atom/(.Role := Requirement)/(.Form := Relation Definition)](../../04_requirement/CA-R-2517-CORE_META_MODEL-DECLARATION--declare-requirement-relation-definition.md) |
| `CA-R-2518@2` | Requirement / Declaration | [Declare Atom/(.Role := Concern).Priority](../../04_requirement/CA-R-2518-CORE_META_MODEL-DECLARATION--declare-concern-priority.md) |
| `CA-R-2519@2` | Requirement / Declaration | [Declare Atom/(.Role := Plan).AI Agent Confidence Threshold](../../04_requirement/CA-R-2519-CORE_META_MODEL-DECLARATION--declare-plan-ai-agent-confidence-threshold.md) |
| `CA-R-2520@2` | Requirement / Declaration | [Declare Atom/(.Role := Plan).Work Sequence Number](../../04_requirement/CA-R-2520-CORE_META_MODEL-DECLARATION--declare-plan-work-sequence-number.md) |
| `CA-R-2521@2` | Requirement / Declaration | [Declare Atom/(.Role := Operations)/Action.Execution Kind](../../04_requirement/CA-R-2521-CORE_META_MODEL-DECLARATION--declare-action-execution-kind.md) |
| `CA-R-2522@2` | Requirement / Declaration | [Declare Atom/(.Role := Requirement)/(.Form := Relation Definition).Content.notation_for_subject](../../04_requirement/CA-R-2522-CORE_META_MODEL-DECLARATION--declare-relation-definition-notation-for-subject.md) |
| `CA-R-2523@2` | Requirement / Declaration | [Declare Scope Unit](../../04_requirement/CA-R-2523-CORE_META_MODEL-DECLARATION--declare-scope-unit.md) |
| `CA-R-2524@2` | Requirement / Declaration | [Declare Project](../../04_requirement/CA-R-2524-CORE_META_MODEL-DECLARATION--declare-project.md) |
| `CA-R-2525@2` | Requirement / Declaration | [Declare Package](../../04_requirement/CA-R-2525-CORE_META_MODEL-DECLARATION--declare-package.md) |
| `CA-R-2526@2` | Requirement / Declaration | [Declare Scope Unit ID](../../04_requirement/CA-R-2526-CORE_META_MODEL-DECLARATION--declare-scope-unit-id.md) |
| `CA-R-2527@2` | Requirement / Declaration | [Declare Scope Unit Name](../../04_requirement/CA-R-2527-CORE_META_MODEL-DECLARATION--declare-scope-unit-name.md) |
| `CA-R-2528@2` | Requirement / Declaration | [Declare Scope Unit Label](../../04_requirement/CA-R-2528-CORE_META_MODEL-DECLARATION--declare-scope-unit-label.md) |
| `CA-R-2529@2` | Requirement / Declaration | [Declare Scope Unit Local Order](../../04_requirement/CA-R-2529-CORE_META_MODEL-DECLARATION--declare-scope-unit-local-order.md) |
| `CA-R-2530@2` | Requirement / Declaration | [Declare Scope Unit Path](../../04_requirement/CA-R-2530-CORE_META_MODEL-DECLARATION--declare-scope-unit-path.md) |
| `CA-R-2531@2` | Requirement / Declaration | [Declare Scope Unit Project Boundary Position](../../04_requirement/CA-R-2531-CORE_META_MODEL-DECLARATION--declare-scope-unit-project-boundary-position.md) |
| `CA-R-2532@2` | Requirement / Declaration | [Declare Project.Settings](../../04_requirement/CA-R-2532-CORE_META_MODEL-DECLARATION--declare-project-settings.md) |
| `CA-R-2533@2` | Requirement / Declaration | [Declare Project Settings Name](../../04_requirement/CA-R-2533-CORE_META_MODEL-DECLARATION--declare-project-settings-name.md) |
| `CA-R-2534@2` | Requirement / Declaration | [Declare Project Settings Prefix](../../04_requirement/CA-R-2534-CORE_META_MODEL-DECLARATION--declare-project-settings-prefix.md) |
| `CA-R-2535@2` | Requirement / Declaration | [Declare Projection](../../04_requirement/CA-R-2535-CORE_META_MODEL-DECLARATION--declare-projection.md) |
| `CA-R-2536@2` | Requirement / Declaration | [Declare Journal](../../04_requirement/CA-R-2536-CORE_META_MODEL-DECLARATION--declare-journal.md) |
| `CA-R-2537@2` | Requirement / Declaration | [Declare Projection.ID](../../04_requirement/CA-R-2537-CORE_META_MODEL-DECLARATION--declare-projection-id.md) |
| `CA-R-2538@2` | Requirement / Declaration | [Declare Projection.Form](../../04_requirement/CA-R-2538-CORE_META_MODEL-DECLARATION--declare-projection-form.md) |
| `CA-R-2539@2` | Requirement / Declaration | [Declare Projection.Updated At](../../04_requirement/CA-R-2539-CORE_META_MODEL-DECLARATION--declare-projection-updated-at.md) |
| `CA-R-2540@2` | Requirement / Declaration | [Declare Projection.Source.Atoms](../../04_requirement/CA-R-2540-CORE_META_MODEL-DECLARATION--declare-projection-source-atoms.md) |
| `CA-R-2541@2` | Requirement / Declaration | [Declare Projection.Source.Named Selection](../../04_requirement/CA-R-2541-CORE_META_MODEL-DECLARATION--declare-projection-source-named-selection.md) |
| `CA-R-2542@2` | Requirement / Declaration | [Declare Actor](../../04_requirement/CA-R-2542-CORE_META_MODEL-DECLARATION--declare-actor.md) |
| `CA-R-2543@2` | Requirement / Declaration | [Declare Aspect](../../04_requirement/CA-R-2543-CORE_META_MODEL-DECLARATION--declare-aspect.md) |
| `CA-R-2544@2` | Requirement / Declaration | [Declare Actor.Name](../../04_requirement/CA-R-2544-CORE_META_MODEL-DECLARATION--declare-actor-name.md) |
| `CA-R-2545@2` | Requirement / Declaration | [Declare Atom.Subjects](../../04_requirement/CA-R-2545-CORE_META_MODEL-DECLARATION--declare-atom-subjects.md) |
| `CA-R-2546@2` | Requirement / Declaration | [Declare Atom.Subjects.Active](../../04_requirement/CA-R-2546-CORE_META_MODEL-DECLARATION--declare-atom-subjects-active.md) |
| `CA-R-2547@2` | Requirement / Entity Definition | [Define markdown value Format](../../04_requirement/CA-R-2547-CORE_META_MODEL-ENTITY_DEFINITION--define-markdown-value-format.md) |
| `CA-R-2548@2` | Requirement / Rule | [Deliver Objects to Carriers](../../04_requirement/CA-R-2548-CORE_META_MODEL-RULE--deliver-objects-to-carriers.md) |
| `CA-D-664@2` | Delivery / Eng Decision | [Deliver Atoms to Markdown files](../../07_delivery/CA-D-664-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md) |
| `CA-M-458@2` | Method / Term Definition | [Define Object](../../05_method/CA-M-458-CORE_META_MODEL-TERM_DEFINITION--define-object.md) |
| `CA-R-2549@2` | Requirement / Rule | [Compare and add numeric values in CFEL](../../04_requirement/CA-R-2549-CORE_META_MODEL-CFEL--compare-numeric-values.md) |
| `CA-R-2550@2` | Requirement / Rule | [Resolve a fallback when an optional Property is omitted](../../04_requirement/CA-R-2550-CORE_META_MODEL-CFEL--fallback-when-omitted.md) |
| `CA-R-2551@2` | Requirement / Rule | [Require unique Property tuples](../../04_requirement/CA-R-2551-CORE_META_MODEL-CFEL--require-unique-property-tuples.md) |
| `CA-R-2552@2` | Requirement / Rule | [Bind instance variables](../../04_requirement/CA-R-2552-CORE_META_MODEL-CFEL--bind-instance-variables.md) |
| `CA-R-2553@2` | Requirement / Declaration | [Declare Implementation](../../04_requirement/CA-R-2553-CORE_META_MODEL-DECLARATION--declare-implementation.md) |
| `CA-R-2554@2` | Requirement / Declaration | [Declare Scope Unit.structural_level](../../04_requirement/CA-R-2554-CORE_META_MODEL-DECLARATION--declare-scope-unit-structural-level.md) |
| `CA-R-2555@2` | Requirement / Declaration | [Declare Package.structural_level](../../04_requirement/CA-R-2555-CORE_META_MODEL-DECLARATION--declare-package-structural-level.md) |
| `CA-R-2556@2` | Requirement / Rule | [State assertions about the active Subject](../../04_requirement/CA-R-2556-CORE_META_MODEL-RULE--keep-assertions-about-the-active-subject.md) |
| `CA-R-2557@2` | Requirement / Declaration | [Declare Event Record](../../04_requirement/CA-R-2557-CORE_META_MODEL-DECLARATION--declare-event-record.md) |
| `CA-R-2558@2` | Requirement / Declaration | [Declare Event Record.ID](../../04_requirement/CA-R-2558-CORE_META_MODEL-DECLARATION--declare-event-record-id.md) |
| `CA-R-2559@2` | Requirement / Declaration | [Declare MODEL](../../04_requirement/CA-R-2559-CORE_META_MODEL-DECLARATION--declare-model.md) |
| `CA-R-2560@2` | Requirement / Declaration | [Declare PROJECT STRUCTURE](../../04_requirement/CA-R-2560-CORE_META_MODEL-DECLARATION--declare-project-structure.md) |
| `CA-R-2561@2` | Requirement / Rule | [Require scalar Property immutability](../../04_requirement/CA-R-2561-CORE_META_MODEL-CFEL--require-scalar-immutability.md) |
| `CA-R-2562@2` | Requirement / Rule | [Require functional dependencies between Property tuples](../../04_requirement/CA-R-2562-CORE_META_MODEL-CFEL--require-functional-dependencies.md) |
| `CA-M-459@2` | Method / Implementation Method | [Write Summary for the Complete Contribution](../../05_method/CA-M-459-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-summary-for-the-complete-contribution.md) |
| `CA-R-2563@2` | Requirement / Rule | [Select fenced Markdown labels](../../04_requirement/CA-R-2563-CORE_META_MODEL-CFEL--select-fenced-markdown-labels.md) |
| `CA-R-2564@2` | Requirement / Declaration | [Declare Project.Settings.AI Agent Confidence Threshold](../../04_requirement/CA-R-2564-CORE_META_MODEL-DECLARATION--declare-project-settings-ai-agent-confidence-threshold.md) |
| `CA-R-2565@2` | Requirement / Rule | [Preserve Atom Version and Updated At When Archiving](../../04_requirement/CA-R-2565-CORE_META_MODEL-RULE--preserve-atom-version-and-updated-at-when-archiving.md) |
| `CA-R-2566@2` | Requirement / Rule | [Filter instances and select maximum values](../../04_requirement/CA-R-2566-CORE_META_MODEL-CFEL--filter-instances-and-select-maximum-values.md) |
| `CA-R-2567@2` | Requirement / Rule | [Record business Property changes in one update Event Record](../../04_requirement/CA-R-2567-CORE_META_MODEL-RULE--record-business-property-changes-in-one-update-event.md) |
| `CA-R-2568@2` | Requirement / Declaration | [Declare Event Record.happened_at](../../04_requirement/CA-R-2568-CORE_META_MODEL-DECLARATION--declare-event-record-happened-at.md) |
| `CA-R-2569@2` | Requirement / Declaration | [Declare Event Record.inserted_at](../../04_requirement/CA-R-2569-CORE_META_MODEL-DECLARATION--declare-event-record-inserted-at.md) |
| `CA-R-2570@2` | Requirement / Rule | [Distinguish event time from record insertion time](../../04_requirement/CA-R-2570-CORE_META_MODEL-RULE--distinguish-event-time-from-record-insertion-time.md) |
| `CA-R-2571@2` | Requirement / Rule | [Capture Atom input and output metadata](../../04_requirement/CA-R-2571-CORE_META_MODEL-RULE--capture-atom-input-and-output-metadata.md) |
| `CA-R-2572@2` | Requirement / Declaration | [Declare Event Record.object_input](../../04_requirement/CA-R-2572-CORE_META_MODEL-DECLARATION--declare-event-record-object-input.md) |
| `CA-R-2573@2` | Requirement / Declaration | [Declare Event Record.object_input.id](../../04_requirement/CA-R-2573-CORE_META_MODEL-DECLARATION--declare-event-record-object-input-id.md) |
| `CA-R-2574@2` | Requirement / Declaration | [Declare Event Record.object_input.version](../../04_requirement/CA-R-2574-CORE_META_MODEL-DECLARATION--declare-event-record-object-input-version.md) |
| `CA-R-2575@2` | Requirement / Declaration | [Declare Event Record.object_input.updated_at](../../04_requirement/CA-R-2575-CORE_META_MODEL-DECLARATION--declare-event-record-object-input-updated-at.md) |
| `CA-R-2576@2` | Requirement / Declaration | [Declare Event Record.object_output](../../04_requirement/CA-R-2576-CORE_META_MODEL-DECLARATION--declare-event-record-object-output.md) |
| `CA-R-2577@2` | Requirement / Declaration | [Declare Event Record.object_output.id](../../04_requirement/CA-R-2577-CORE_META_MODEL-DECLARATION--declare-event-record-object-output-id.md) |
| `CA-R-2578@2` | Requirement / Declaration | [Declare Event Record.object_output.version](../../04_requirement/CA-R-2578-CORE_META_MODEL-DECLARATION--declare-event-record-object-output-version.md) |
| `CA-R-2579@2` | Requirement / Declaration | [Declare Event Record.object_output.updated_at](../../04_requirement/CA-R-2579-CORE_META_MODEL-DECLARATION--declare-event-record-object-output-updated-at.md) |
| `CA-R-2580@2` | Requirement / Declaration | [Declare Event Record.action](../../04_requirement/CA-R-2580-CORE_META_MODEL-DECLARATION--declare-event-record-action.md) |
| `CA-R-2581@2` | Requirement / Declaration | [Declare Event Record.Relations](../../04_requirement/CA-R-2581-CORE_META_MODEL-DECLARATION--declare-event-record-relations.md) |
| `CA-R-2582@2` | Requirement / Declaration | [Declare Event Record.Relations.HAS_EVENT_AUTHOR](../../04_requirement/CA-R-2582-CORE_META_MODEL-DECLARATION--declare-event-record-event-author.md) |
| `CA-R-2583@2` | Requirement / Relation Definition | [Define HAS_EVENT_AUTHOR](../../04_requirement/CA-R-2583-CORE_META_MODEL-RELATION_DEFINITION--define-event-author-link.md) |
| `CA-R-2584@2` | Requirement / Rule | [Capture Projection input and output metadata](../../04_requirement/CA-R-2584-CORE_META_MODEL-RULE--capture-projection-input-and-output-metadata.md) |
| `CA-R-2585@2` | Requirement / Rule | [Count direct Property values and distinct values](../../04_requirement/CA-R-2585-CORE_META_MODEL-CFEL--count-property-values-and-distinct-values.md) |
| `CA-D-665@2` | Delivery / Eng Decision | [Deliver Projections to Markdown files](../../07_delivery/CA-D-665-CORE_META_MODEL-ENG_DECISION--deliver-projections-to-markdown-files.md) |
| `CA-R-2586@2` | Requirement / Declaration | [Declare Projection.Source](../../04_requirement/CA-R-2586-CORE_META_MODEL-DECLARATION--declare-projection-source.md) |
| `CA-R-2587@2` | Requirement / Declaration | [Declare Named Selection](../../04_requirement/CA-R-2587-CORE_META_MODEL-DECLARATION--declare-named-selection.md) |
| `CA-M-460@2` | Method / Implementation Method | [Write positive Claims about the active Subject](../../05_method/CA-M-460-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-positive-claims-about-the-active-subject.md) |
| `CA-R-2588@2` | Requirement / Rule | [Apply default Relation cardinalities](../../04_requirement/CA-R-2588-CORE_META_MODEL-CFEL--apply-default-relation-cardinalities.md) |
| `CA-R-2589@2` | Requirement / Declaration | [Declare Continuant](../../04_requirement/CA-R-2589-CORE_META_MODEL-DECLARATION--declare-continuant.md) |
| `CA-R-2590@2` | Requirement / Declaration | [Declare Occurrent](../../04_requirement/CA-R-2590-CORE_META_MODEL-DECLARATION--declare-occurrent.md) |

The machine-readable [Draft register](node-declaration-20261031/draft-register.json) records every carrier and its reviewed content hash. The selected model has 28 Primary Node Declarations and 60 Property Declarations. Source adoption remains separate.

### Smaller inventory first

The Operator selected the smaller Node inventory. See the [selected Node tree](node-declaration-20261031/declaration-expansion/node-inventory-proposal.md) for the agreed kinds. All 27 selected Primary Nodes now have Declaration Drafts. The old taxonomy is evidence, not the target inventory. Property contracts remain under review. Project.Settings contains Name, Prefix and required AI Agent Confidence Threshold. Framework Settings is deferred. All selected Property contracts now state their dependent-name constraints.

### Reusable CFEL constraints

The Operator permits reusable syntax extensions when remaining prose shows a repeated pattern. Keep brief Semantics for Primary Nodes. Language definitions and constraints without a mature formal representation retain short prose.

Numeric bounds recur in Atom.Version, Work Sequence Number and Tier. A new CFEL Draft defines `>`, `>=`, `<` and `<=` as numeric value comparisons. Both operands must resolve to one numeric value without string coercion. Optional Properties are guarded before comparison. Existing composition and classification operators keep their meanings. The packet uses this syntax for all three bounds. Version-change behavior is retained in deferred Operations notes. Work Sequence Number grouping remains unresolved; the Atom ID/Version key now uses the generic UNIQUE constraint.

The remaining repeated patterns and their decisions are:

- Omission fallback uses `p ?= expression`. The Label Declaration uses `Atom.Label ?= Atom.Form`. Inheritance remains part of the existing rules, without another lookup stage. No Author admission-fill mechanism is included.
- Uniqueness: define the comparison key and exact grouping Scope for repeated values and Work Sequence Numbers.
- Revision processes belong to deferred Operations work. Do not add before/after CFEL language or extra Workflow Rules in this pass.
- Reference domains and dynamic admitted sets: bind their resolution rules and governing registry.

These are research candidates, not adopted syntax. The two pattern reports and coverage report retain their source cases and unresolved semantics.

### Author deferral and omission fallback

The Operator removed Author from the proposed artifact model and deferred it to a future version. The unpublished Atom.Author Declaration is withdrawn. This packet and its proposal/Epic Draft omit author metadata; artifact carrier contracts omit the field. Operator identity and ownership remain in the existing Operator registry, which is unchanged.

Use `p ?= expression` when an optional Property is omitted. A supplied Property is not replaced; null, an empty string, zero and false are not omission. The fallback must satisfy the Property's value Format and count. It does not write a Carrier or satisfy a required authored occurrence. Both paths bind the same selected bearer. Existing inheritance carries declarations and constraints; no second inheritance operator or instance-value lookup stage is introduced.

Before Current adoption, reconcile the Author-required clauses in CA-R-655@42, CA-R-1078@31, CA-R-1080@29, CA-R-2102@13, CA-R-2356@1, CA-D-274@30 and CA-D-463@25. They remain Current and unchanged. The authorless Draft carriers deliberately express the Operator's target format; bounded Draft checks do not establish conformance with those legacy author-required rules.

### Operations and RMED responsibility

Processes belong to Operations. RMED states invariants: valid structures, value domains, allowed conditions, method constraints, evaluation criteria and delivery contracts. A condition about an allowed Operation may remain an invariant; it does not describe the execution sequence.

Use the existing IF/THEN syntax for conditional constraints. Do not add before/after language. The later archive-preservation decision adds one Workflow Requirement; other deferred Operations notes remain notes. Retain brief Semantics for Primary Nodes.

The Current-group Active Subject requirement is now a formal conditional. Every Current-group Atom requires one Active Subject, including Backlog, Active, Done and Canceled. There is no completeness exception. The base optional occurrence for other Status Groups is unchanged.

The Atom version key is `(Atom.ID, Atom.Version)`, globally unique inside its Project across Draft, Current and Archived instances, regardless of containment. `UNIQUE(Atom//, (.ID, .Version))` is stated in the existing Atom Declaration. Version replaces the previous Draft Property name Version Number; it is not a second Property or an alias. Repeated carriers of one logical instance do not create another key. This global pair constraint does not replace the separate one-Current-version-per-Atom lifecycle rule.

#### Deferred Operations notes

The following Version and Settings instructions are removed from Property Declarations and retained for later Operations work. They do not create new Workflow instances or new Workflow Requirements. The later archive-preservation decision is recorded separately as an explicit Workflow Requirement.

Source: [CA-R-2496-CORE_META_MODEL-DECLARATION--declare-atom-version.md](../../04_requirement/draft/node-declaration-20261031/property-expansion/CA-R-2496-CORE_META_MODEL-DECLARATION--declare-atom-version.md).

> - It increases monotonically across successive versions of the same Atom.

Source: [CA-R-2532-CORE_META_MODEL-DECLARATION--declare-project-settings.md](../../04_requirement/draft/node-declaration-20261031/property-expansion/CA-R-2532-CORE_META_MODEL-DECLARATION--declare-project-settings.md).

> Select the inputs before either is created:
> 
> - The first Project Atom.
> - The root Package.

The exact removed clauses and source hashes are preserved in the [relocation evidence](node-declaration-20261031/declaration-expansion/invariant-process-result.json). Timestamp meaning, no-op preservation, identity immutability and other invariant constraints remain in their Declarations. Archive preservation now belongs to the separate Workflow Requirement below.

#### Promotion version allocation — latest decision

On promotion, calculate the maximum Version across all logical instances with Atom.ID = X inside the Project, including Draft, Current and Archived instances and the Draft being promoted. Assign that maximum plus one. There is no Current-only filter, preservation of a Draft's proposed number, or search for the smallest unused gap.

This pseudocode belongs to the promotion Workflow:

```text
$last_version = max(atom.version) where atom.id = X;
$new_version = $last_version + 1;
```

| Before promotion | Selected Draft | Maximum Version | Promoted Current version |
|---|---|---|---|
| Current 5; Drafts 6 and 7 | Draft 7 | 7 | 8 |
| Current 8; remaining Draft 6 | Draft 6 | 8 | 9 |
| Current 7; Drafts 6 and 8 | Draft 6 | 8 | 9 |
| Current 7; Drafts 6 and 12 | Draft 6 | 12 | 13 |

Recheck the complete same-ID version population when promotion is committed. This supersedes the earlier keep-proposed/next-free rule and the earlier example where Draft 7 became Current 7. These are deferred Operations notes; no Workflow instance, extra Workflow Requirement or new CFEL variable/query/arithmetic grammar is added.

See the [invariant/Operations review](node-declaration-20261031/invariant-operations-version-review-20261031.md) for coverage and verification limits.

### Structural levels and root kinds — latest decision

Scope Unit.structural_level and Package.structural_level are explicit nonnegative integers, written once in the applicable Declaration. Do not derive their effective values from the containment chain. The IS_CONTAINED_BY constraints validate the declared values: roots have level 0; each contained instance has its container’s level plus 1. This supersedes the earlier sole-derivation requirement; no provenance operator is needed.

- Scope Unit roots are instances of Scope Unit/Project. Their level is 0 and they are not contained by another Scope Unit.
- Package roots are instances of Package/Implementation. Their level is 0 and they are not contained by another Package.
- Every other Scope Unit or Package is contained by exactly one immediate container of the same kind.
- For each actual IS_CONTAINED_BY link, contained.structural_level = container.structural_level + 1.

Implementation is a narrower Package kind, not a named Package instance. `Package/Implementation//{:1}` states its single instance per Project. `Scope Unit/Project//{:1}` states the Project root count. `Journal//{:1}` states exactly one Journal per Project; no narrower Work Journal kind is introduced. These use the same cardinality mechanism already applied to Properties; no separate COUNT function or counting Rule is introduced.

Instance variables use Kind//$x. Repeated references bind the same matched instance; typed instance selectors include narrower kinds. Instance-set membership uses in/not in. Relation patterns in IF test actual or legitimately derived links; equations apply only to those linked bindings. Numeric + is static value addition, and = remains an equality constraint.

A cycle of k links would require level = level + k for k > 0, which no integer satisfies. The unpublished recursive Relation-path proposal is withdrawn. Existing Property .** and narrower-branch /** selectors are unchanged.

[Structural-level review](node-declaration-20261031/structural-level-review-20261031.md) records the root constraints, derivation decision, coverage and verification limits.

This explicitly replaces the legacy Project Implementation kind spelling with the target Package/Implementation spelling only in the proposed model. CA-R-2239 remains unchanged; its realization, editability and nonautomatic-Projection clauses are pinned as unmigrated source coverage. This structural Declaration does not claim their full migration.

### Event Record — approved inventory addition

Add Event Record as a Primary Node. Each Event Record belongs to exactly one Journal. Journal is a Container and permits zero or more Event Records. Each Declaration states its own relation count; CONTAINS remains the derived inverse of IS_CONTAINED_BY. The Project still has exactly one Journal. Each Event Record has its own required scalar string ID, unique across Event Records in the Project. It is not keyed by Journal and Sequence Number. Use the existing UNIQUE constraint; no new ID notation or allocation algorithm is introduced. Append-only formalization remains pending review.

### Count modes and active-Subject scope — latest decision

The same cardinality mechanism applies to selected Property occurrences, values, names, instances and Relation links. `{:n}` declares an allowed count, `{=n}` tests the count, and `{==n}` states a required or derived conclusion. The selector identifies what is counted; literal allowed values still follow colon outside a count group.

Every Atom with an active Subject states assertions and prescriptions about that active Subject, regardless of Role or Form. Other Subjects can supply the endpoints, inputs, outputs, conditions or dependencies needed to define it. Independent assertions about them belong in their own Atoms. The two count slots remain part of CFEL; their availability does not expand an Atom's active-Subject scope. For Node relation counts, use the Node's own view. Allowed target kinds remain part of that contract. Step and Workflow Declarations demonstrate this general rule.

```CFEL
Step//{:1}((IS_CONTAINED_BY)) Workflow//;
Workflow//{:1+}((CONTAINS)) Step//
```

The two lines belong in Step and Workflow Declarations respectively. The same containment link is authored once; CONTAINS remains the derived view. Step/Substep/Action execution alternatives and cardinalities are preserved. Scope Unit and Package now state IS_CONTAINED_BY and CONTAINS counts as separate Host-side views.

### Atom.ID immutability boundary — latest decision

Atom.ID becomes immutable on first promotion to either Current or Archived. An Atom may move directly from Draft to Archived; prior Current status is not required. Keep that path available in the deferred lifecycle Workflows. This decision does not change the separately stated archive preservation of Version and Updated At, or the Current-promotion version formula.

The cross-version scope is resolved: the same Atom keeps the immutable ID across all later versions, including Drafts. IMMUTABLE(p) binds the first applicable scalar value through supplied logical-bearer lineage. A later Version, Carrier or false guard does not reset the constraint. An optional Property cannot disappear after activation. Unknown lineage/history cannot prove compliance. The first consumers are Atom.ID and admitted Event Record.ID. [Reviewed examples](node-declaration-20261031/declaration-expansion/immutability-examples-20261031.json) cover the direct archive path and later Drafts. Runtime lineage binding and parser support remain adoption work.

### Functional dependencies — reusable formal invariant

DETERMINES(selector, key tuple, dependent tuple) requires equal keys to have equal dependent values over complete relevant historical states within one Project. Repeated equal states are permitted; different keys may share dependent values. References compare their declared target identities rather than Carrier locators. Missing historical or reference bindings cannot pass. This declares a constraint and does not allocate an ID or execute a Workflow.

For Current and Archived states only, Atom.ID determines Atom.Content.Summary. Draft states are outside this formal dependency. Separately, the update Workflow creates a fresh ID at Version 1 when Summary changes; its coverage requirement is preserved in the Summary authoring Method, leaving the Declaration formal-only. For Projection.ID, use both directions between ID and the Form and Named Selection tuple. The later Operator decision removes the separate Source Of Truth Property. This preserves stable identity across rebuilds and requires a different ID for a changed basis. Projection.ID is formal-only. [Independent review](node-declaration-20261031/declaration-expansion/functional-dependency-review-20261031.json) and [reference-identity example](node-declaration-20261031/declaration-expansion/functional-dependency-evidence-20261031.json) distinguish semantic identity from physical representation.

### Summary authoring and new identity — latest decisions

Keep the Summary's coverage requirement in an authoring Method. Its Declaration retains the format, cardinalities and ID-to-Summary dependency. This preserves the writing requirement while making the Declaration formal-only.

When an update Draft changes Summary, create a new Atom.ID and set the new Draft's Version to 1. This is new-identity creation rather than mutation of the accepted ID. Record the creation/reset rule in the deferred lifecycle Workflow work; it does not replace the existing archive preservation constraints. A new Draft is a new Atom instance. This does not make Atom.ID unique per version: the formal constraint permits repeated IDs with equal Summaries across Current and Archived versions, and rejects equal IDs with different Summaries there. It does not constrain Draft Summary differences. The new-ID/Version-1 update branch is a separate Workflow rule.

### Accepted-state Summary dependency — 2026-11-01

The operator explicitly restricts the invariant to Current plus Archived: two such Atom instances with the same Atom.ID cannot have different Summaries. The optional DETERMINES condition filters each historical state before tuple resolution; a Draft state is not included merely because another version is Current. Repeated same-ID/same-Summary states are allowed. The rule does not require different IDs to have different Summaries. An unknown state condition cannot be silently skipped.

### Plan Sequence Number constraints — latest decisions

The number is optional; a supplied value retains its positive integer contract. Uniqueness applies only to Plans whose Status is Active, within the same direct container. Done, Canceled, Backlog, Draft and Archived Plans are outside this uniqueness check. Numbering may restart in each direct container, so a Task 1 can contain its own Subtask 1.

A numbered Active Plan must have one direct containment group. The existing typed group has exactly one Atom or Scope Unit leaf. Separate UNIQUE clauses group by these actual reference leaves plus the number; referenced container identity is resolved explicitly. Missing or ambiguous grouping information cannot silently pass.

UNIQUE accepts an optional third condition. It filters instances in one Project snapshot before tuple resolution; it does not replay earlier Active states from history. Its existing unfiltered form continues to include all selected Status Groups, preserving the Atom.ID/Version rule.

The model contains only Sequence Number constraints. Execution ordering belongs to the Workflow for P execution and is deferred with other Workflow-instance review. Remove the execution-order sentence from the Number Declaration; no additional Method or single-use predicate is needed.

### Zero-prose Declaration Claims — staged pass

Target zero prose Claims in Node descendants and their Properties, retaining brief Primary Node Semantics. The baseline is 26 Claims with prose. The first verified pass leaves 25. The Current-group decision then leaves 24: Atom.Content.Semantics and Atom.Subjects.Active are formal-only. Shared-Rule coverage preserves Semantics policy; every Current Atom requires one Active Subject. Projection.Form now has a formal-only Claim: its Property contract and the Catalog, Map and Hub value cases express the intended qualification, such as Projection/(.Form: Catalog). After scalar immutability is defined, Atom.ID is formal-only and the dependency pass makes Projection.ID formal-only and the authoring-Method decision makes Summary formal-only and the Active per-container number constraints leave the latest count at 19 Claims with prose. Other exact duplicates are removed while their governing constraints remain.

Use reusable capabilities for the remaining cases: registered domains, Markdown structure, direct-value and scoped uniqueness, derived/default bindings, identity/history invariants, and MODEL/provenance bindings. IMMUTABLE and DETERMINES are explicitly defined reusable extensions. The remaining catalog entries do not admit operators or undocumented value formats. Keep a constraint until its equivalent is expressed or an explicit human decision changes it. Unmigrated Current sources alone are not sufficient grounds to delete a target constraint.

The Current-group decision is resolved: every Current Atom requires an Active Subject. Projection.Form is resolved: it is a Property with value-qualified Projection cases. The old Type name is superseded in the proposed model; exact Current source/carrier migration remains separate. The four stale readiness-Evaluation checks are aligned with Subject := and effective MODEL overrides. [Pattern catalog and verification](node-declaration-20261031/declaration-expansion/zero-prose-patterns-20261031.json) retain the conversion traces and remaining gaps.

### Role and Form names — latest decision

A Form may have the same name as its Role. Name equality alone is not a validation error. The later string-contract decision removes the extra admission check from the Form Declaration.

### Claim authoring rule — Method ownership

Keep “Use prose only for constraints CFEL cannot express” in the existing [formal-notation authoring Method](../../05_method/draft/node-declaration-20261031/CA-M-457-CORE_META_MODEL-IMPLEMENTATION_METHOD--reuse-formal-notation-and-write-isolated-constraints-in-prose.md). Its rule now explicitly says “only when.” Remove the writing instruction from Atom.Content.Claim’s Declaration; retain the one-CFEL-block and no-other-fenced-block constraints there. No duplicate Method or new CFEL syntax is introduced.

### Fenced Markdown structure — formal constraint

Add one read-only selector, [FENCED_LABELS](../../04_requirement/draft/node-declaration-20261031/CA-R-2563-CORE_META_MODEL-CFEL--select-fenced-markdown-labels.md). Apply the existing finite literal Format and value cardinality to its result:

```CFEL
FENCED_LABELS(Atom/(.Role in RMED).Content.Claim): [in (CFEL)]{:0..1}
```

This requires zero or one fenced block with label CFEL. Duplicate labels count as separate blocks. Indented code is outside this restriction. The selector inspects parsed Markdown values; it does not create dependent Properties. Preserve the existing governing label meaning; raw info-string interpretation remains an explicit parser-adoption binding. CFEL body syntax is checked separately.

The Claim Declaration is formal-only. The packet has112 Drafts;16 Node descendant Declaration Claims retain prose. This adds no parser or runtime implementation. [Independent review](node-declaration-20261031/declaration-expansion/fenced-labels-final-review-20261101.json).

### Plan confidence and Workflow retry responsibility — latest decision

Keep AI Agent Confidence Threshold as a Plan Property. Remove Implementation Retry Limit from the proposed Plan model; retry handling belongs to the Workflow. Its preparation Draft is withdrawn, not promoted. The P Property is optional. Resolve its effective value from its own authored value, then the nearest applicable authored value along the recursive IS_CONTAINED_BY chain, then the required Project.Settings.AI Agent Confidence Threshold. Do not copy fallback values into P carriers. This supersedes the earlier same-bearer-only fallback limit and the Name/Prefix-only Settings scope.

The packet has112 Drafts,27 Primary and47 Property Declarations. Fourteen Node descendant Declaration Claims retain prose. The withdrawal does not change Current sources or runtime retry behavior. [Withdrawal record](node-declaration-20261031/declaration-expansion/withdrawn-plan-retry-limit-20261101.json).

### Recursive confidence fallback — reviewed Draft

AI Agent Confidence Threshold is optional on P Atoms. The Project Settings default is required. Use one ordered, non-writing fallback chain:

```CFEL
Atom/(.Role: Plan).AI Agent Confidence Threshold
  ?= LOOKUP(IS_CONTAINED_BY, Atom/(.Role: Plan).AI Agent Confidence Threshold)
  ?= Scope Unit/Project//$project.Settings.AI Agent Confidence Threshold
```

LOOKUP follows the existing containment direction and selects the nearest applicable authored value. It does not invent a Property on intervening Scope Units or match unrelated Properties by name. Invalid present values do not trigger fallback. Evaluated traversal cycles, fallback-expression cycles, unresolved graph facts and ambiguous targets are errors. The contextual Project is the existing singleton in the current Project evaluation context; the fallback does not require a new containment route to it.

The [fallback Rule](../../04_requirement/draft/node-declaration-20261031/CA-R-2550-CORE_META_MODEL-CFEL--fallback-when-omitted.md) defines the extension. Root/default cardinalities remain independent constraints even when lookup short-circuits. The P Declaration is formal-only. No actual Project threshold number is selected, and no runtime configuration is changed. [Final review](node-declaration-20261031/declaration-expansion/confidence-fallback-final-review-20261101.json).

### Archive preservation — Workflow requirement

The [archive-preservation Rule Draft](../../04_requirement/draft/node-declaration-20261031/CA-R-2565-CORE_META_MODEL-RULE--preserve-atom-version-and-updated-at-when-archiving.md) requires a Workflow that archives an Atom to preserve Version and Updated At. Archiving alone creates no new Version. This also preserves an archived predecessor’s timestamp.

Remove those clauses from Atom.Status and Atom.Updated At Declarations. Keep the timestamp’s accepted-edit meaning and exact-no-op requirement in the latter. Both existing CFEL blocks remain unchanged. The Workflow Requirement addresses the existing Workflow kind conditionally; no Archive Workflow instance or before/after language is introduced.

Atom.Status is formal-only. The packet has113 Drafts;13 Node descendant Declaration Claims retain prose. [Independent preservation review](node-declaration-20261031/declaration-expansion/archive-preservation-workflow-review-20261101.json).

### Core requirements, Workflow process and Engine implementation

Core Meta-model R atoms define required values and invariants. Atom.Updated At identifies the accepted-edit instant and retains its prior value on an exact no-op. Projection.Updated At identifies the latest completed rebuild represented by the Projection. Keep these contracts in their Core Property Declarations.

Workflows define the process that produces compliant results. Engine implements that process. A Core R may constrain a Workflow’s required result, as the archive-preservation Requirement does; that Requirement is not a sequence of Operations steps.

This clarifies responsibility without moving the timestamp requirements or adding syntax. The packet still has13 Node descendant Declaration Claims with prose.

### Event-based Updated At — proposed formal pattern

The Operator proposed one invariant for both Atoms and Projections: Updated At equals the maximum timestamp of matching update Event Records.

```text
Atom//$atom.updated_at == MAX(Event Record//(.object=$atom, (.action=create OR .action=update)).happened_at)
```

This is pseudocode, not an admitted query grammar. The matching object is the specific logical instance. Atom versions must not be conflated by a bare ID. Event references also need to remain resolvable when a Draft’s Version changes on promotion. Event records currently declare only ID and Journal containment; target, action and timestamp bindings still need governing declarations.

The Operator resolved update qualification: action = update denotes accepted completed updates, including completed Projection rebuilds. No-ops, failed attempts and archiving do not qualify. The Operator resolved initial creation: select accepted create and update events together. Creation supplies the first timestamp; no extra update event is required solely for creation. Event-time meaning and complete Project/Journal coverage remain subsequent checks. No new event schema, MAX implementation or current Declaration replacement is implied by this proposal. [Pattern review](node-declaration-20261031/event-timestamp-pattern-review-20261101.md).

### Generic filtered selection and MAX — reviewed Draft

The [query-language Rule Draft](../../04_requirement/draft/node-declaration-20261031/CA-R-2566-CORE_META_MODEL-CFEL--filter-instances-and-select-maximum-values.md) defines `Kind//(conditions).p` and `MAX(selection)`. Filters bind relative fields to the same candidate while preserving enclosing variables. Selection uses the current Project snapshot and includes narrower kinds. MAX returns the greatest typed scalar; datetime ordering compares instants. Empty, invalid and unresolved inputs are errors.

This defines reusable language independently of the Event Record schema. Creation semantics are settled: include create and update events. The later descriptor/schema and timestamp conversion below replaces both timestamp consumers with reviewed formal Claims. The packet has114 Drafts and13 remaining Node descendant prose Claims. [Final language review](node-declaration-20261031/declaration-expansion/event-timestamps-query-language-final-review-20261101.json).

### One business update Event Record — changed Properties only

Promotion is an accepted update. A promotion at11:00 contributes an11:00 timestamp for the promoted Atom even if its Draft was last edited at10:00. Archive preservation for the predecessor remains a separate constraint.

The [business-change Rule Draft](../../04_requirement/draft/node-declaration-20261031/CA-R-2567-CORE_META_MODEL-RULE--record-business-property-changes-in-one-update-event.md) records one update in one Event Record. Its change delta contains only changed logical Properties, identified by complete paths, with old/new values or absence. It does not require complete old/new object copies.

For promotion, the business data may include:

```text
Version: 6 -> 8
Status: Draft -> Active
```

Carrier filename and directory changes are excluded. A Carrier-only rename or move creates no update Event Record. In a mixed operation, the record still contains the business changes without the Carrier changes. Event metadata is not removed by this payload restriction.

Updated At may appear in the delta when changed. Its new value is derived from the agreed accepted create/update timestamp maximum. This audit copy is neither another source for Updated At nor another business update. Its historical new value is evaluated through that record’s happened_at, not against later updates or insertion time. DRY preserves one authoritative derivation; it does not forbid a captured derived value. The exact object-reference and field encodings remain schema work; the earlier abstract instance/state question is retired. No permanent hidden ID, history rewrite or version merging is inferred. The packet has115 Drafts;13 Node descendant Declaration Claims retain prose. [Review](node-declaration-20261031/declaration-expansion/business-update-delta-review-20261101.json).

### Event Record fields and two times — latest decision

The proposed record fields are happened_at, inserted_at, author, action, object_input (old) and object_output. Keep the existing ID. Author means the Actor who performs the event; this does not restore Atom.Author or identify the record inserter by default.

Two [time Property Declarations](../../04_requirement/draft/node-declaration-20261031/property-expansion/CA-R-2568-CORE_META_MODEL-DECLARATION--declare-event-record-happened-at.md) require one datetime each, without dependents. The second is [inserted_at](../../04_requirement/draft/node-declaration-20261031/property-expansion/CA-R-2569-CORE_META_MODEL-DECLARATION--declare-event-record-inserted-at.md). Their [shared Core Rule](../../04_requirement/draft/node-declaration-20261031/CA-R-2570-CORE_META_MODEL-RULE--distinguish-event-time-from-record-insertion-time.md) distinguishes event time from addition to the Journal. No ordering inequality or clock policy is introduced.

Updated At uses MAX of happened_at for matching accepted create/update events. inserted_at does not replace event time when insertion is delayed. For example, an event happening at10:00 and inserted at10:05 contributes10:00.

For Atom events, object_input and object_output capture metadata triplets: ID, Version and Updated At before and after the change. Their IDs may differ. The captured values remain historical facts. This replaces the earlier references-versus-change-maps question. Real instance links, including author, remain under Relations. Carrier-only changes remain excluded; changed Updated At may still be captured as derived audit data.

The packet has118 Drafts,27 Primary and49 Property Declarations. Thirteen Node descendant Declaration Claims retain prose. [Time-field review](node-declaration-20261031/declaration-expansion/event-record-two-times-review-20261101.json). No actual Event Record, database column or runtime behavior is created by these Drafts.

### Atom input/output metadata and Content exclusion — latest decision

The [metadata-capture Rule Draft](../../04_requirement/draft/node-declaration-20261031/CA-R-2571-CORE_META_MODEL-RULE--capture-atom-input-and-output-metadata.md) requires each present Atom side to capture Atom.ID, Atom.Version and Atom.Updated At. Input captures before; output captures after. IDs are not required to match. Creation input presence and descriptor encoding are not guessed here.

The [business-change Rule](../../04_requirement/draft/node-declaration-20261031/CA-R-2567-CORE_META_MODEL-RULE--record-business-property-changes-in-one-update-event.md) excludes Atom.Content and all recursive descendants from Event Records for now, including Summary and Claim. A Content-only accepted update can still have an Event Record; its Content values and paths are omitted. Non-Content changed Properties remain eligible for the delta.

For Atoms, timestamp matching must use the output ID and Version, so an old input ID is not treated as the result identity. The query remains pseudocode until the descriptor fields are declared. Projection currently has no Version Property; whether its descriptor has two fields or gains Version is the sole current question.

The packet has119 Drafts;13 Node descendant Declaration Claims retain prose. [Review](node-declaration-20261031/declaration-expansion/atom-event-input-output-metadata-review-20261101.json). No Event Record row, runtime reference encoding or new identifier is created by these requirements.

### Event Record schema and timestamp conversion — reviewed Drafts

Projection has no Version. Its [capture Rule](../../04_requirement/draft/node-declaration-20261031/CA-R-2584-CORE_META_MODEL-RULE--capture-projection-input-and-output-metadata.md) records only ID and Updated At. The existing Atom Rule requires ID, Version and Updated At. Common object_input/object_output maps admit id, updated_at and optional version; the kind-specific Rules require Version for Atom sides and forbid it for Projection sides. Both creation/update outputs are required. Update inputs are required; creation inputs may be absent. IDs may differ across sides.

Author is a real Actor link stored under Relations.HAS_EVENT_AUTHOR. [HAS_EVENT_AUTHOR](../../04_requirement/draft/node-declaration-20261031/CA-R-2583-CORE_META_MODEL-RELATION_DEFINITION--define-event-author-link.md) identifies the event performer; its inverse is derived. Atom.Author remains deferred. action is a required string; create/update/archive are admitted cases, not a closed global domain. Core R restricts create/update to accepted completed business events, excluding failures, no-ops, archiving and Carrier-only changes.

Both Updated At Declarations are formal-only. Their MAX selections read happened_at, never inserted_at or captured output.updated_at. Atom filters match captured output ID and Version; Projection filters match output ID with Version absent. Left-to-right guards exclude unrelated absent descriptors without hiding an evaluated invalid value. Missing required supported-event output remains a separate model violation.

No Atom.Content paths or values enter the records. Content-only accepted updates still have their metadata event. Historical captured Updated At values retain their event-time scope.

The packet has132 Drafts,27 Primary and60 Property Declarations. Eleven Node descendant Declaration Claims retain prose. [Integrated review](node-declaration-20261031/declaration-expansion/event-schema-final-review-20261101.json) and [model cases](node-declaration-20261031/declaration-expansion/event-schema-acceptance-cases-20261101.json) establish Draft semantics, not executable parser/runtime support or actual event backfill.

### Atom.Form string contract — latest decision

Use `Atom.Form: [string]{:1}` for the Form value. Remove the earlier admitted-atomic-unit and placeholder prose from its Declaration. Keep its required occurrence and zero-dependent constraints. The existing CFEL block is unchanged and the Claim is formal-only. This resolves Form’s prior admission-pattern question without a new query helper. [Decision](node-declaration-20261031/declaration-expansion/atom-form-string-contract-decision-20261101.json).

Ten Node descendant Declaration Claims retain prose. No new Draft or language syntax is added.

### Role string and Project Goal Tier — latest decisions

Use `Atom.Role: [string]{:1}`. Replace the earlier closed value Format while preserving required occurrence and zero dependents. Existing named Role cases retain their Declarations.

The Operator proposed:

```text
IF (Atom target Scope Unit = Project AND Atom.Form = Goal) THEN Atom.Tier == -1
```

No extra Tier rule is to be added for other Goals. Resolve the target Scope Unit from the active Subject; do not add a Target Scope Unit Property. The exact mapping for arbitrary active Subjects is not yet declared. Keep this expression as pseudocode until that binding is defined. The Operator explicitly removed the Project Goal ownership requirement. The Tier Declaration now omits that clause; no replacement Core R is added. Its numeric formal block is unchanged.

[Role decision](node-declaration-20261031/declaration-expansion/atom-role-string-contract-decision-20261101.json), [Tier direction](node-declaration-20261031/declaration-expansion/project-goal-tier-conditional-decision-20261101.json). No runtime or new syntax change is implied.

### Passive Subject distinctness — latest decision

Use `COUNT(Atom.Subjects.Passive: $) = COUNT(DISTINCT Atom.Subjects.Passive: $)` per Atom. COUNT preserves repeated value occurrences; DISTINCT uses the declared Format's equality. Known absence counts as zero; unresolved or invalid data is an error. The current string Format does not imply alias canonicalization. Keep the prose meaning: Passive Subjects identify direct contextual dependencies.

The packet has 133 registered Drafts, 27 Primary and 60 Property Declarations. Ten Node descendant Declaration Claims retain prose; 77 Claims across the packet are formal-only. The [COUNT review](node-declaration-20261031/declaration-expansion/passive-distinct-count-review-20261101.json) covers the Draft contract, not a parser implementation.

### Relation notation requirement — retained prose

Keep the `notation_for_subject` requirement in prose for now: when a short subject notation is admitted for a Relation, this Property is required. Defer formalization; preserve the existing Declaration. The 10-Claim prose census is unchanged. [Decision](node-declaration-20261031/declaration-expansion/relation-notation-prose-retention-decision-20261101.json).

### Projection Sources — Atom IDs and Versions only

Each Projection.Source.Atoms value is an Atom ID with an explicit Version, for example `CA-R-123@4`. Remove the broader contributing-source and optional dependency-provenance wording. Keep the existing occurrence and cardinality limits. The Property retains one short prose constraint with its string Format; no new CFEL syntax is introduced. [Decision](node-declaration-20261031/declaration-expansion/projection-sources-atom-version-decision-20261101.json).

### Projection Source Of Truth — removed

Remove the separate Projection.Source Of Truth Property; Sources already records the versioned source Atoms. Withdraw its preparation Draft and remove the Property from both directions of the Projection ID dependency. The remaining identity basis is Form and Named Selection. Source-version changes on rebuild do not become a new identity component. The later decision nests Named Selection and Atoms under Projection.Source. [Decision](node-declaration-20261031/declaration-expansion/projection-source-of-truth-removal-decision-20261101.json).

Current packet: 132 Drafts; 27 Primary and 59 Property Declarations. Nine Node descendant Declaration Claims retain prose; 77 Claims are formal-only. Current sources are unchanged.

### Projection Declaration — invariant, meaning and delivery

Remove creation and update instructions from the Projection Declaration; retain them as deferred Operations notes. Its Claim is formal-only. Brief Semantics explains that a Projection is a derived view of source Atoms and cannot establish or override their Claims. Projection.Source.Atoms owns the versioned source-reference constraint.

Use a separate Delivery Draft for `Projection// >> Carrier/Markdown_file//`. This uses the Operator's exact Carrier expression; it does not define a creation Workflow. [Decision and deferred Operations notes](node-declaration-20261031/declaration-expansion/projection-operations-and-delivery-decision-20261101.json).

Current packet: 133 Drafts; 27 Primary and 59 Property Declarations. Eight Node descendant Declaration Claims retain prose; 79 Claims across the packet are formal-only.

### Journal and Event Record — latest topic split

Journal's Claim uses the existing containment expression: `Journal// {:0+}((CONTAINS)) Event Record//`. Remove its ordering and member-immutability prose. Event Record owns the positive prose statement: “An Event Record is immutable.” Its ID Declaration retains Format, counts and uniqueness, while whole-record immutability supplies the shared constraint.

### MODEL and Project — latest topic split

Project owns: “A Project uses CAPRMEDIO's MODEL.” MODEL owns local inheritance and effective override resolution. Local overrides preserve base rules; unchanged inherited Declarations are reused. The Node inheritance Rule keeps Node consequences. Possibility boilerplate is omitted.

### Projection.Source — confirmed grouping

Projection.Source is required and has no direct value. It contains:

- Named Selection: one required reference to a Named Selection instance.
- Atoms: an optional list of concrete Atom IDs with explicit Versions.

Only these child names are allowed. Both children forbid dependent Properties. Existing occurrence and value counts are preserved. The instance reference uses the existing `[Kind//]` Format pattern; no new CFEL syntax is introduced. A new Named Selection Primary Declaration supplies the target kind and names selection criteria without copying selected members. Existing string-to-instance reference bindings and the old Selection definition need reconciliation at adoption; no instances are created here.

Both Projection ID dependencies now use `.Source.Named Selection`; concrete source Versions remain outside the ID basis. [Migration and file mapping](node-declaration-20261031/declaration-expansion/projection-source-group-application-20261101.json). Current packet: 135 Drafts, 28 Primary and 60 Property Declarations, 82 formal-only Claims and 7 residual Declaration prose Claims.

### Positive wording and Claim topic

The Journal revision keeps its two direct statements. The writing Method captures the general rule for other Claims. Current packet: 136 Drafts, 28 Primary and 60 Property Declarations; 82 formal-only Claims and 7 Declaration Claims with prose. No new syntax or runtime changes.

### Prose and formal Relation whitelist review

Use positive statements about the active Subject, and reuse ancestor rules. Journal's Claim is formal-only; Event Record owns immutability. Structural-level value equations now belong to their Property Declarations. Plan owns the dependency between active numbering and a declared direct container. Work Sequence Number retains its value and uniqueness constraints.

The audit covers all 136 previously registered Drafts: 28 Primary Declarations, 60 Property Declarations and 48 other Claims. Endpoint/condition/input references remain valid when they constrain the active Subject. Independent constraints move to their own Subject or are explicitly bound as delivery/structure context.

The approved wildcard is `Host {:0}((*))`, with applicable named constraints as exceptions. Model entities and their instances have separate inherited scopes: `(Node, Node.**)` and `(Node//, (Node//).**)`. `{:x}` remains allowed-value notation, not a new graph Relation. The prepared CFEL Rule explains this fallback without treating named bounds as contradictory global zeros.

The latest scopes are `(Node, Node.**)` for the model and `(Node//, (Node//).**)` for instances and their Properties. Both zero defaults are stated once in Node; narrower Nodes inherit them. Recursive Property traversal is explicit. Complete local whitelist coverage is still under review. [Current status and evidence](node-declaration-20261031/declaration-expansion/whitelist-current-status-20261101.json).

Current packet: 137 Drafts; 28 Primary and 60 Property Declarations; 82 formal-only Claims; 8 Declaration Claims retain prose. Node root is formal-only. The prose count reflects correct ownership, rather than hiding constraints in another Subject.

### Inherited defaults — final selector spelling

Declare both defaults once in Node:

```CFEL
(Node, Node.**) {:0}((*));
(Node//, (Node//).**) {:0}((*))
```

The first scope covers the model. The second covers Node instances and their recursive Properties. Narrowing inheritance applies the rules to descendant kinds. `(Node//).**` traverses dependent Properties; it does not independently instantiate Property kinds. This supersedes the recursive slash and `Node.**//` default spellings.

Each inverse direction needs an explicit whitelist entry. It remains a view of one fact. Check its own cardinality together with every applicable bound, after MODEL override resolution. The shared model HAS_PROPERTY exception includes Property bearers so nested Properties remain permitted. [Application and review](node-declaration-20261031/declaration-expansion/node-inherited-defaults-application-20261101.json). Shared-rule review passed; complete local whitelist and runtime validation remain open.

### Carrier transition notes

- Draft carriers retain the admitted `content_role` and `type` keys until the replacement carrier schema is admitted. The target names remain Role and Form.
- Assignee and Target reference mappings remain unresolved. Author is deferred.
- The current section reader excludes the selected heading. Migration must reconcile it with retrieval of the complete selected subtree, including that heading.
- Reserved-key handling and exact character normalization remain open where existing rules do not settle them.

### Adoption and migration

1. Review the actual Drafts together; settle only blocking decisions one at a time.
2. Map each selected existing Definition to its intended Node, Declaration and predecessor disposition. Preserve constraints and avoid duplicating inherited Properties. The [source inventory](node-declaration-20261031/source-inventory.json) contains 333 Current Entity Definition sources: 290 Object/Aspect/Property review candidates, 18 Syntax, 23 Carrier and 2 Term. These are candidates, not an approved retirement list.
3. Establish complete governing Drafts, effective whitelists and source coverage. Keep CFEL Claims and optional Semantics. Retire only the reviewed Node Definitions after their replacement Declarations and references are ready.
4. Coordinate parser/schema, Markdown/YAML adapters, graph extraction, lookup, SDK/workflow callers and fixtures with the Engine Epic. Rebuild projections and check source provenance, permissions, endpoints and cardinalities after actual adoption.

Open gates are complete Node membership and effective whitelists; remaining reference mappings; omitted value-domain behavior (an omitted cardinality remains undefined under the existing rule); lossless Markdown retrieval details; exact new Subject bindings; and effective MODEL selection and override binding. The pending Declaration Role-letter question is closed: Declaration uses Requirement and R. These gates block dependent adoption, not preparation of unrelated Drafts.

## TLDR

The linked governing Drafts define the proposed changes. Declaration is Requirement/Form: Declaration. This packet adds precise naming Methods, formal Node rules, Relation notation and carrier/validation contracts. Current sources, Definition retirement, parser deployment and full Node migration are not completed by this proposal.

### Inventory correction — 1 November 2026

Continuant and Occurrent remain in the model under the latest Operator correction. The registered 88 Declarations are the current prepared packet, not a final statement that every other concept is removed. Revise inventory coverage and source dispositions before Current adoption. Retiring an old Definition carrier and removing its concept are separate dispositions. See the [retirement review list](node-declaration-20261031/migration-20261101/retirement-review-list.md).

### Retained kinds included

The packet now contains 139 Drafts: 30 Primary Node Declarations and 60 Property Declarations. Continuant and Occurrent remain as Node kinds. Their old Definitions are replaced by the corresponding Declarations; their concepts are retained. This is the agreed migration inventory correction.

### Atom migration applied

The 139 prepared Atoms are Current. The selected inventory has 30 Primary and 60 Property Declarations, including Continuant and Occurrent. Their old Definition carriers are archived as replaced versions; the concepts remain. The publication receipt preserves 1,263 predecessor archives and records 301 retirements, 962 updates and 139 promotions. Source fields now use Role/Form and Active/Passive. Graph rebuilding and direct migration issue checks follow. No Engine runtime or actual Operations-instance migration was performed.

### Graph refresh and direct fixes applied

CA-PROJ-014/015/016 now use the selected 1,101 Current RMED sources; CA-PROJ-017 presents the declared model from 128 Current sources. All 90 selected Declarations are included. Twelve direct followup updates and the obsolete Term-as-Property retirement are recorded. Unsupported legacy Subject expressions remain observations or diagnostics. Native runtime and actual Operations instances remain deferred. See the [applied result and checks](node-declaration-20261031/migration-20261101/README.md).
