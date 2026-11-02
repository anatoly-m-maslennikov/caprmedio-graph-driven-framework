---
atom_id: CA-A-draft
content_role: Analysis
type: Specification Proposal
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: Entity/Term
version: 1
updated_at: 2026-10-30 14:16:41 +0400
relations: {}
tier: 3
---
# Summary

Move Terms to the Entity root and Method definitions

## Question

Which source changes implement the Operator-confirmed direct Term branch, Method-owned lexical definitions and Empty meaning without silently changing Current authority or unrelated identities?

## Scope

CORE_META_MODEL Term placement and meaning ownership: direct `Entity/Term`, initially flat named Term instances, Method Type Term Definition, the explicit Empty, ID, Entity, Term and Property lexical definitions, the direct `Entity/Property` kind and the approved IS_PROPERTY_OF / derived HAS_PROPERTY Relation pair, structural and ownership Requirements, and source consumers of the old path or Requirement-qualified Type. This packet prepares Drafts only. Current adoption, identity repair, numeric allocation, archival, runtime, generated graphs, release and a complete terminology-coverage claim are outside these effects.

## Approach

Use the latest human decisions over earlier R classification and Continuant placement. Pin exact Current source paths, versions and hashes. Keep structural Requirements separate from lexical Methods, prepare coordinated N+1 consumer successors, and preserve existing Claims except the approved role/path changes. Review the primary Drafts independently and verify both mechanical successors and the later semantic corrections against their sources. Do not use an ambiguous canonical ID as a source selector.

### Rationale from the Operator's input

This rationale follows the Operator's messages in this conversation. The latest explicit correction controls earlier wording. The points below connect those inputs to the Drafts; source-governed compatibility work is identified separately.

1. **Precise vocabulary must preserve entity identity.** The Operator asked for a “precise dictionary” and “no synonyms”, then corrected the initial Term/entity equivalence: “it's not Terms, it's entities.” The resulting constraint applies to complete canonical entity names: one complete name identifies one entity, and references to that entity retain that name. This motivates the canonical-name Rule, CCE authoring Methods and naming Evaluations. It does not require a different Term for every entity.

2. **Terms are reusable components; full expressions identify entities.** The Operator used Package in Package, Eval Package and Runtime Package, and Unit in Scope Unit and Code Unit to explain reuse. The later correction requires the full expression when naming an entity. Those short lexical forms illustrate components, not complete canonical entity names outside the Term branch. The supplied `Atom/Content Role: X/Type: X` shows why repeated X components can be valid within different qualifications. The accepted `atom.id` and `projection.id` likewise reuse ID while identifying distinct qualified properties. These inputs motivate the Term-kind, subject-expression, component-reuse and full-name Drafts and their evaluation fixtures. Existing value-admission rules still apply independently in each qualified context.

3. **Structural definition and lexical definition have different targets.** The Operator distinguished an Entity with Subject `Entity` and Type R / Entity Definition from its reusable Term. The final correction makes Entity the sole exception outside the Term branch whose complete canonical name can also be one Term, “because it's our subject root.” Thus the structural definition governs `Entity`; the lexical definition governs `Entity/Term//Entity`. The earlier general permission for any outside entity to have a complete name equal to a Term is superseded. The Project and Project Implementation root examples do not extend this naming exception. The separate request “also we need Term Term” supplies the lexical target `Entity/Term//Term`, alongside the structural kind `Entity/Term`. Reusing Term in its own definition requires no further lexical instance.

4. **Terms need an explicit branch and dedicated meaning owners.** The Operator placed Terms in a “different root branch”, supplied `Entity/Term//Empty`, and deferred grouping: “maybe we'll group them later.” The Operator also settled “Term Definition is M”. Accordingly, the root and Term-kind Drafts establish the initially flat Term branch; the new Method Type declaration admits the intended specialized Type; M / Term Definition Drafts supply lexical meanings. R / Entity Definition continues to define model entities and their structure. The separate authoring Method explains how to write definition content. Changing the path alone would leave old Role/Type references and consumers inconsistent, which explains the coordinated successor Drafts.

5. **Checks should follow the authored source in stages.** The Operator found the proposed projection too complex and requested explicit definitions followed by occurrence review: entity names, Claim, Claim Scope, Semantics, Details and remaining fields. This motivates the authoring, Evaluation and evidence-carrier Drafts. They check declared meaning, ownership, complete names and consistent occurrences directly in the sources. A generated dictionary or Terms Graph is not a prerequisite for that review.

6. **The concrete Term definitions retain the Operator's boundaries.** For ID, the Operator supplied a unique identifier used to find an entity instance across Continuant and Occurrent instances, then bounded uniqueness by matching prefixes. The spelling examples do not decide version identity or lifecycle semantics. For Empty, the Operator supplied null, the empty string and omitted input, clarifying undefined as omission. The Empty Method gives the Create Draft discussion a precise input condition without broadening it to general truthiness. These are the reasons for the ID replacement and new Empty Draft; this proposal does not implement Workflow execution.

7. **Property is the one canonical concept and Term.** The Operator first grounded dependence in a Relation and permitted `Entity/Dependent Entity`, then explicitly selected Property as the single Term. The later decision supersedes that separate kind and lexical name. The structural target is `Entity/Property`, with lexical owner `Entity/Term//Property`. The Operator approved `IS_PROPERTY_OF` with strictly derived inverse `HAS_PROPERTY`; no old-name aliases are introduced. The direct Relation runs from Property to immediate bearer; dot notation runs from bearer to Property. The Operator places no separate Carrier and applicable direct-value Format/cardinality in Claim, exactly one outgoing Relation in the Formal claim, and Property-as-bearer nesting in Semantics. The latest two-sided notation places `{1}` before the token: `Property {1}((IS_PROPERTY_OF)) Bearer` counts outgoing Relation instances per Property, independently of value cardinality and of a Relation's two endpoints. The extra generic identity/lifecycle clauses were rejected. The Operator subsequently approved prohibiting IS_PROPERTY_OF cycles, including self-loops. This applies only to Property bearer Relations.
8. **Drafts record decisions before adoption.** The Operator repeatedly requested Draft updates, asked for the proper format, and stated that the latest input beats previous input. The packet therefore corrects superseded interpretations in Drafts and keeps Current adoption separate. Root structure, kind definitions, Method Type, lexical owners, naming rules, authoring Methods, Evaluations and consumers must agree before promotion. N+1 versions, exact source pins and replacement identities are governed compatibility requirements supporting that agreement. The five original Property/Type/Artifact target cases now have Draft dispositions; the Draft count does not establish that their logic is settled. The Operator also specified that the Workflow work belongs in another A/Spec Proposal with its own Drafts.

## Results

### Confirmed decisions

- Terms form a direct branch `Entity/Term`, alongside the existing root branches. Do not retain the earlier narrower placement under `Entity/Object/Continuant/Term` or infer inherited Continuant classification from that former path.
- Begin with flat named instances, including `Entity/Term//Empty`, `Entity/Term//ID` and `Entity/Term//Property`. No intermediate Term groups or categories are introduced. Grouping may be considered later.
- Type and Content Role are Properties, including when used for classification. `X.Y` addresses Property Y; generic `X: Y` means Y is an allowed value of X; `X/(.Y: Z)` qualifies the whole X by its relative Property and admitted value, retaining inheritance from X. Existing YAML keys represent these same Properties. Syntax alone establishes no Entity or value admission.
- **M / Term Definition** supplies one Term's authoritative lexical meaning as an authoring and interpretation convention. This supersedes the earlier R/Term Definition classification.
- **R / Entity Definition** continues to define the Term kind and its inherited structure. M lexical definitions supply instance-specific meaning, not duplicate structural Requirements. A separate Method explains how to write definition content; E checks well-formedness and consistent occurrences.
- **Empty means an omitted input, null, or the empty string `""`.** `undefined` denotes omitted input; it is not the literal string `"undefined"` or a general truthiness test. Whitespace-only strings, `0`, `false`, `[]` and `{}` are outside this exact set.
- ID keeps the approved meaning of a unique identifier used to find one Continuant or Occurrent entity instance, with uniqueness bounded by matching prefixes. Moving its definition to M or its target to `Entity/Term//ID` adds no lifecycle equivalence, case-folding, parser or ID-allocation semantics.

The R Entity-root successor adds direct Term and Property branches; moving reference strings alone would not establish the new hierarchy. `Entity/Property` is an entity kind and `Entity/Term//Property` its lexical Term instance. Property is the sole canonical name for the former Property/Dependent Entity distinction. Its direct Relation is `IS_PROPERTY_OF`, with strictly derived `HAS_PROPERTY`. No pairwise disjointness, new Primary Entity branch or lifecycle restriction is inferred. The separately approved Property bearer-cycle prohibition is recorded below. The Term-kind successor preserves `Name[string]{1}`. The Governed Term successor is based on Current CA-R-1319@25, Type Rule, and requires exactly one active Method Term Definition owner.
### Primary Drafts

| Contribution | Actual Draft |
|---|---|
| Entity root: preserve existing branches and add Term and Property | [CA-R-1248@24-draft-CORE_META_MODEL-DEFINITION--define-entity](../../04_requirement/draft/CA-R-1248@24-draft-CORE_META_MODEL-DEFINITION--define-entity.md) |
| Term kind and inherited Name structure | [CA-R-1318@30-draft-CORE_META_MODEL-DEFINITION--define-term](../../04_requirement/draft/CA-R-1318@30-draft-CORE_META_MODEL-DEFINITION--define-term.md) |
| Governed Term: exactly one Method meaning owner | [CA-R-1319@26-draft-CORE_META_MODEL--define-governed-term](../../04_requirement/draft/CA-R-1319@26-draft-CORE_META_MODEL--define-governed-term.md) |
| New Method-qualified Type declaration | [CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-method-type-term-definition](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-method-type-term-definition.md) |
| Empty: exact omitted/null/empty-string convention | [CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-empty](../../05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-empty.md) |
| ID: proposed Method replacement with preserved meaning | [CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-id](../../05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-id.md) |
| Entity: reusable lexical name distinct from the Entity root | [CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-entity](../../05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-entity.md) |
| Term: reusable word distinct from the Term kind | [CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-term](../../05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-term.md) |
| Property: structural kind, bearer constraint and value declaration | [CA-R-1193@23-draft-CORE_META_MODEL-DEFINITION--define-property](../../04_requirement/draft/CA-R-1193@23-draft-CORE_META_MODEL-DEFINITION--define-property.md) |
| Property: sole lexical meaning owner | [CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-property](../../05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-property.md) |
| Direct Property-to-bearer Relation | [CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-is-property-of](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-is-property-of.md) |
| Strictly derived bearer-to-Property inverse | [CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-has-property](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-has-property.md) |
| Artifact: lexical meaning for an Entity instance represented in a Carrier | [CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-artifact](../../05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-artifact.md) |
| Markdown File Carrier: structural File specialization | [CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-markdown-file-carrier](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-markdown-file-carrier.md) |
| Markdown Atom Carrier: structural Markdown specialization | [CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-markdown-atom-carrier](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-markdown-atom-carrier.md) |
| Project Settings Name: structural Property Definition | [CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-project-settings-name](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-project-settings-name.md) |
| Project Settings Prefix: structural Property Definition | [CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-project-settings-prefix](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-project-settings-prefix.md) |

The new Method-qualified Type declaration is a new unallocated R/Entity Definition. It does not rename or repurpose Current CA-R-2229@2, whose Summary and governed target declare the Requirement-qualified Type. That old declaration remains Current until coordinated replacement and retirement. Its existing ID is not transferred to the new declaration.

The ID Method Draft is a proposed replacement of the exact Current Requirement carrier `04_requirement/CA-R-2275-CORE_META_MODEL-TERM_DEFINITION--define-id.md`, Version 1, SHA-256 `e07b52086e0205f0400c6f01db7a8d2bff52b0dbc94fbf68d785283400ae6402`. A Content Role change requires a fresh canonical Method identity under CA-R-1432; no Requirement number is reused as a Method identity. Empty and both new Type/Method Drafts retain role-only markers until admitted allocation.

### Consumer successors

The source inventory found 106 affected Current files, with overlapping counts of 104 old-Term-path occurrences and 14 old R-Type bindings. Five sources are handled by structural Drafts or replacement/retirement plans; the remaining 101 receive source-pinned N+1 consumer Drafts. All Current sources remain untouched. The consumer transformation changes only the approved Term path, lexical owner Role/Type and necessary authority references; it does not convert structural Requirements or Rules into lexical Methods. At the original mechanical-preparation stage, 88 consumer bodies remained byte-identical and 13 had reviewed changes: path/ownership changes plus one inherited heading normalization in the R1703 Draft, which moves an unchanged supporting paragraph from unregistered Primary claim to Details without adding another Claim.

| Current source | Proposed successor |
|---|---|
| CA-R-2003@13 | [CA-R-2003@14-draft-CORE_META_MODEL--require-exactly-one-immediate-bearer-for-each-dependent-entity-occurrence](../../04_requirement/draft/CA-R-2003@14-draft-CORE_META_MODEL--require-exactly-one-immediate-bearer-for-each-dependent-entity-occurrence.md) |
| CA-D-464@23 | [CA-D-464@24-draft-CORE_META_MODEL-ENG_DECISION--represent-one-governed-object-with-each-directory-carrier](../../07_delivery/draft/CA-D-464@24-draft-CORE_META_MODEL-ENG_DECISION--represent-one-governed-object-with-each-directory-carrier.md) |
| CA-D-505@16 | [CA-D-505@17-draft-CORE_META_MODEL-ENG_DECISION--define-the-entity-carrier-binding](../../07_delivery/draft/CA-D-505@17-draft-CORE_META_MODEL-ENG_DECISION--define-the-entity-carrier-binding.md) |
| CA-D-479@25 | [CA-D-479@26-draft-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties](../../07_delivery/draft/CA-D-479@26-draft-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md) |
| CA-D-655@1 | [CA-D-655@2-draft-CORE_META_MODEL-POLICY--carry-term-definition-and-staged-review-evidence](../../07_delivery/draft/CA-D-655@2-draft-CORE_META_MODEL-POLICY--carry-term-definition-and-staged-review-evidence.md) |
| CA-D-506@16 | [CA-D-506@17-draft-CORE_META_MODEL-ENG_DECISION--give-every-non-ephemeral-entity-a-carrier](../../07_delivery/draft/CA-D-506@17-draft-CORE_META_MODEL-ENG_DECISION--give-every-non-ephemeral-entity-a-carrier.md) |
| CA-D-309@25 | [CA-D-309@26-draft-CORE_META_MODEL-ENG_DECISION--bind-materialized-representations-to-regeneration-sources](../../07_delivery/draft/CA-D-309@26-draft-CORE_META_MODEL-ENG_DECISION--bind-materialized-representations-to-regeneration-sources.md) |
| CA-D-485@22 | [CA-D-485@23-draft-CORE_META_MODEL-ENG_DECISION--carry-defaulted-atom-values-without-copying-inherited-overrides](../../07_delivery/draft/CA-D-485@23-draft-CORE_META_MODEL-ENG_DECISION--carry-defaulted-atom-values-without-copying-inherited-overrides.md) |
| CA-E-382@47 | [CA-E-382@48-draft-CORE_META_MODEL-POLICY--validate-terms-graph](../../06_evaluation/draft/CA-E-382@48-draft-CORE_META_MODEL-POLICY--validate-terms-graph.md) |
| CA-E-449@40 | [CA-E-449@41-draft-CORE_META_MODEL-POLICY--validate-entities-graph](../../06_evaluation/draft/CA-E-449@41-draft-CORE_META_MODEL-POLICY--validate-entities-graph.md) |
| CA-E-383@39 | [CA-E-383@40-draft-CORE_META_MODEL-POLICY--reject-invalid-subject-expressions](../../06_evaluation/draft/CA-E-383@40-draft-CORE_META_MODEL-POLICY--reject-invalid-subject-expressions.md) |
| CA-E-659@1 | [CA-E-659@2-draft-CORE_META_MODEL-EVAL_CASE--check-term-definition-well-formedness](../../06_evaluation/draft/CA-E-659@2-draft-CORE_META_MODEL-EVAL_CASE--check-term-definition-well-formedness.md) |
| CA-E-522@17 | [CA-E-522@18-draft-CORE_META_MODEL-EVAL_CASE--storage-boundary-classification-interpretability](../../06_evaluation/draft/CA-E-522@18-draft-CORE_META_MODEL-EVAL_CASE--storage-boundary-classification-interpretability.md) |
| CA-E-444@32 | [CA-E-444@33-draft-CORE_META_MODEL-EVAL_CASE--validate-project-specific-term-meaning](../../06_evaluation/draft/CA-E-444@33-draft-CORE_META_MODEL-EVAL_CASE--validate-project-specific-term-meaning.md) |
| CA-E-403@32 | [CA-E-403@33-draft-CORE_META_MODEL-POLICY--report-exact-claim-value-set-consolidation-candidates](../../06_evaluation/draft/CA-E-403@33-draft-CORE_META_MODEL-POLICY--report-exact-claim-value-set-consolidation-candidates.md) |
| CA-E-246@45 | [CA-E-246@46-draft-CORE_META_MODEL-EVAL_CASE--validate-atom-subjects](../../06_evaluation/draft/CA-E-246@46-draft-CORE_META_MODEL-EVAL_CASE--validate-atom-subjects.md) |
| CA-E-512@23 | [CA-E-512@24-draft-CORE_META_MODEL-EVAL_CASE--validate-cce-lexical-case](../../06_evaluation/draft/CA-E-512@24-draft-CORE_META_MODEL-EVAL_CASE--validate-cce-lexical-case.md) |
| CA-E-520@28 | [CA-E-520@29-draft-CORE_META_MODEL-EVAL-POLICY--check-rmed-atom-coherence](../../06_evaluation/draft/CA-E-520@29-draft-CORE_META_MODEL-EVAL-POLICY--check-rmed-atom-coherence.md) |
| CA-E-402@29 | [CA-E-402@30-draft-CORE_META_MODEL-POLICY--reject-invalid-claim-value-sets](../../06_evaluation/draft/CA-E-402@30-draft-CORE_META_MODEL-POLICY--reject-invalid-claim-value-sets.md) |
| CA-E-472@26 | [CA-E-472@27-draft-CORE_META_MODEL-POLICY--check-simple-wording-without-meaning-loss](../../06_evaluation/draft/CA-E-472@27-draft-CORE_META_MODEL-POLICY--check-simple-wording-without-meaning-loss.md) |
| CA-E-443@30 | [CA-E-443@31-draft-CORE_META_MODEL-EVAL_CASE--validate-confidence-threshold-precedence-and-inheritance](../../06_evaluation/draft/CA-E-443@31-draft-CORE_META_MODEL-EVAL_CASE--validate-confidence-threshold-precedence-and-inheritance.md) |
| CA-E-505@19 | [CA-E-505@20-draft-CORE_META_MODEL-EVAL_CASE--validate-shared-label-semantics](../../06_evaluation/draft/CA-E-505@20-draft-CORE_META_MODEL-EVAL_CASE--validate-shared-label-semantics.md) |
| CA-E-404@25 | [CA-E-404@26-draft-CORE_META_MODEL-POLICY--reject-invalid-dependency-order-derivations](../../06_evaluation/draft/CA-E-404@26-draft-CORE_META_MODEL-POLICY--reject-invalid-dependency-order-derivations.md) |
| CA-M-228@31 | [CA-M-228@32-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-subject-expressions-with-bearer-and-value-qualification](../../05_method/draft/CA-M-228@32-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-subject-expressions-with-bearer-and-value-qualification.md) |
| CA-M-229@29 | [CA-M-229@30-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--render-governed-terms-and-cce-operators-distinctly](../../05_method/draft/CA-M-229@30-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--render-governed-terms-and-cce-operators-distinctly.md) |
| CA-M-125@45 | [CA-M-125@46-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--assign-subjects-from-the-claim](../../05_method/draft/CA-M-125@46-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--assign-subjects-from-the-claim.md) |
| CA-M-444@1 | [CA-M-444@2-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--atom-claims-expose-their-meaning-conditions-and-consequences-clearly](../../05_method/draft/CA-M-444@2-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--atom-claims-expose-their-meaning-conditions-and-consequences-clearly.md) |
| CA-M-271@25 | [CA-M-271@26-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence](../../05_method/draft/CA-M-271@26-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence.md) |
| CA-M-313@24 | [CA-M-313@25-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-delivery-claims-with-the-delivery-cce-profile](../../05_method/draft/CA-M-313@25-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-delivery-claims-with-the-delivery-cce-profile.md) |
| CA-M-237@29 | [CA-M-237@30-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--author-claim-value-sets](../../05_method/draft/CA-M-237@30-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--author-claim-value-sets.md) |
| CA-M-439@1 | [CA-M-439@2-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-term-definition-content](../../05_method/draft/CA-M-439@2-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-term-definition-content.md) |
| CA-M-114@41 | [CA-M-114@42-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-terminology-projection-from-definition-atoms](../../05_method/draft/CA-M-114@42-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-terminology-projection-from-definition-atoms.md) |
| CA-M-294@23 | [CA-M-294@24-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--use-simpler-words-without-losing-meaning](../../05_method/draft/CA-M-294@24-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--use-simpler-words-without-losing-meaning.md) |
| CA-M-239@23 | [CA-M-239@24-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-dependency-order-from-explicit-edges](../../05_method/draft/CA-M-239@24-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-dependency-order-from-explicit-edges.md) |
| CA-M-113@38 | [CA-M-113@39-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-claims-in-caprmedio-controlled-english](../../05_method/draft/CA-M-113@39-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-claims-in-caprmedio-controlled-english.md) |
| CA-R-1346@24 | [CA-R-1346@25-draft-CORE_META_MODEL-RULE--permit-reused-terms-in-qualified-value-domains](../../04_requirement/draft/CA-R-1346@25-draft-CORE_META_MODEL-RULE--permit-reused-terms-in-qualified-value-domains.md) |
| CA-R-1321@32 | [CA-R-1321@33-draft-CORE_META_MODEL--define-subject-expression](../../04_requirement/draft/CA-R-1321@33-draft-CORE_META_MODEL--define-subject-expression.md) |
| CA-R-1454@30 | [CA-R-1454@31-draft-CORE_META_MODEL--derive-governed-terms-views-from-selected-authority](../../04_requirement/draft/CA-R-1454@31-draft-CORE_META_MODEL--derive-governed-terms-views-from-selected-authority.md) |
| CA-R-1703@36 | [CA-R-1703@37-draft-CORE_META_MODEL-RULE--use-implementation-overview-as-a-projection](../../04_requirement/draft/CA-R-1703@37-draft-CORE_META_MODEL-RULE--use-implementation-overview-as-a-projection.md) |
| CA-R-1281@33 | [CA-R-1281@34-draft-CORE_META_MODEL-DEFINITION--define-atom-subjects-graph](../../04_requirement/draft/CA-R-1281@34-draft-CORE_META_MODEL-DEFINITION--define-atom-subjects-graph.md) |
| CA-R-1441@24 | [CA-R-1441@25-draft-CORE_META_MODEL--define-default-settings](../../04_requirement/draft/CA-R-1441@25-draft-CORE_META_MODEL--define-default-settings.md) |
| CA-R-1320@24 | [CA-R-1320@25-draft-CORE_META_MODEL-DEFINITION--define-general-term](../../04_requirement/draft/CA-R-1320@25-draft-CORE_META_MODEL-DEFINITION--define-general-term.md) |
| CA-R-1194@30 | [CA-R-1194@31-draft-CORE_META_MODEL-DEFINITION--define-subject-path](../../04_requirement/draft/CA-R-1194@31-draft-CORE_META_MODEL-DEFINITION--define-subject-path.md) |
| CA-R-1247@22 | [CA-R-1247@23-draft-CORE_META_MODEL-RULE--identify-dependent-entity-occurrences-by-complete-subject-path](../../04_requirement/draft/CA-R-1247@23-draft-CORE_META_MODEL-RULE--identify-dependent-entity-occurrences-by-complete-subject-path.md) |
| CA-R-1638@46 | [CA-R-1638@47-draft-CORE_META_MODEL-DEFINITION--register-the-implementation-overview-projection](../../04_requirement/draft/CA-R-1638@47-draft-CORE_META_MODEL-DEFINITION--register-the-implementation-overview-projection.md) |
| CA-R-1324@25 | [CA-R-1324@26-draft-CORE_META_MODEL-RULE--reserve-subject-expression-separators](../../04_requirement/draft/CA-R-1324@26-draft-CORE_META_MODEL-RULE--reserve-subject-expression-separators.md) |
| CA-R-1500@19 | [CA-R-1500@20-draft-CORE_META_MODEL-DEFINITION--define-artifact-applicability](../../04_requirement/draft/CA-R-1500@20-draft-CORE_META_MODEL-DEFINITION--define-artifact-applicability.md) |
| CA-R-1502@23 | [CA-R-1502@24-draft-CORE_META_MODEL--keep-authority-applicability-and-currentness-distinct](../../04_requirement/draft/CA-R-1502@24-draft-CORE_META_MODEL--keep-authority-applicability-and-currentness-distinct.md) |
| CA-R-1646@37 | [CA-R-1646@38-draft-CORE_META_MODEL-RULE--bind-proof-records-to-dependency-frontiers](../../04_requirement/draft/CA-R-1646@38-draft-CORE_META_MODEL-RULE--bind-proof-records-to-dependency-frontiers.md) |
| CA-R-1456@35 | [CA-R-1456@36-draft-CORE_META_MODEL--derive-entities-views-from-selected-authority](../../04_requirement/draft/CA-R-1456@36-draft-CORE_META_MODEL--derive-entities-views-from-selected-authority.md) |
| CA-R-1259@21 | [CA-R-1259@22-draft-CORE_META_MODEL-RULE--permit-zero-or-more-properties-on-every-entity](../../04_requirement/draft/CA-R-1259@22-draft-CORE_META_MODEL-RULE--permit-zero-or-more-properties-on-every-entity.md) |
| CA-R-1455@25 | [CA-R-1455@26-draft-CORE_META_MODEL--preserve-evidence-and-uncertainty-in-vocabulary-diagnostic-indexes](../../04_requirement/draft/CA-R-1455@26-draft-CORE_META_MODEL--preserve-evidence-and-uncertainty-in-vocabulary-diagnostic-indexes.md) |
| CA-R-1531@20 | [CA-R-1531@21-draft-CORE_META_MODEL-DEFINITION--define-the-content-role-property](../../04_requirement/draft/CA-R-1531@21-draft-CORE_META_MODEL-DEFINITION--define-the-content-role-property.md) |
| CA-R-1609@20 | [CA-R-1609@21-draft-CORE_META_MODEL-RULE--distinguish-projected-representations-from-represented-entities](../../04_requirement/draft/CA-R-1609@21-draft-CORE_META_MODEL-RULE--distinguish-projected-representations-from-represented-entities.md) |
| CA-R-1558@21 | [CA-R-1558@22-draft-CORE_META_MODEL-RULE--route-questions-and-ideas-through-exploration-mode](../../04_requirement/draft/CA-R-1558@22-draft-CORE_META_MODEL-RULE--route-questions-and-ideas-through-exploration-mode.md) |
| CA-R-1275@30 | [CA-R-1275@31-draft-CORE_META_MODEL--define-subject](../../04_requirement/draft/CA-R-1275@31-draft-CORE_META_MODEL--define-subject.md) |
| CA-R-1245@24 | [CA-R-1245@25-draft-CORE_META_MODEL-RULE--qualify-allowed-values-with-colon](../../04_requirement/draft/CA-R-1245@25-draft-CORE_META_MODEL-RULE--qualify-allowed-values-with-colon.md) |
| CA-R-1348@23 | [CA-R-1348@24-draft-CORE_META_MODEL-RULE--reuse-type-in-qualified-subjects](../../04_requirement/draft/CA-R-1348@24-draft-CORE_META_MODEL-RULE--reuse-type-in-qualified-subjects.md) |
| CA-R-1279@30 | [CA-R-1279@31-draft-CORE_META_MODEL-RULE--govern-every-defined-term](../../04_requirement/draft/CA-R-1279@31-draft-CORE_META_MODEL-RULE--govern-every-defined-term.md) |
| CA-R-1594@17 | [CA-R-1594@18-draft-CORE_META_MODEL-DEFINITION--define-label](../../04_requirement/draft/CA-R-1594@18-draft-CORE_META_MODEL-DEFINITION--define-label.md) |
| CA-R-1489@23 | [CA-R-1489@24-draft-CORE_META_MODEL-RULE--permit-implementation-retry-limit-defaults-and-overrides](../../04_requirement/draft/CA-R-1489@24-draft-CORE_META_MODEL-RULE--permit-implementation-retry-limit-defaults-and-overrides.md) |
| CA-R-1639@33 | [CA-R-1639@34-draft-CORE_META_MODEL-DEFINITION--register-derived-from-relation](../../04_requirement/draft/CA-R-1639@34-draft-CORE_META_MODEL-DEFINITION--register-derived-from-relation.md) |
| CA-R-1026@28 | [CA-R-1026@29-draft-CORE_META_MODEL--register-depends-on-and-required-by-relation-pair](../../04_requirement/draft/CA-R-1026@29-draft-CORE_META_MODEL--register-depends-on-and-required-by-relation-pair.md) |
| CA-R-1738@39 | [CA-R-1738@40-draft-CORE_META_MODEL--define-project-settings](../../04_requirement/draft/CA-R-1738@40-draft-CORE_META_MODEL--define-project-settings.md) |
| CA-R-1410@20 | [CA-R-1410@21-draft-CORE_META_MODEL--connect-every-caprmedio-graph-through-the-general-artifact-graph](../../04_requirement/draft/CA-R-1410@21-draft-CORE_META_MODEL--connect-every-caprmedio-graph-through-the-general-artifact-graph.md) |
| CA-R-1436@23 | [CA-R-1436@24-draft-CORE_META_MODEL--define-is-allowed-value-of](../../04_requirement/draft/CA-R-1436@24-draft-CORE_META_MODEL--define-is-allowed-value-of.md) |
| CA-R-1499@19 | [CA-R-1499@20-draft-CORE_META_MODEL-DEFINITION--define-artifact-authority](../../04_requirement/draft/CA-R-1499@20-draft-CORE_META_MODEL-DEFINITION--define-artifact-authority.md) |
| CA-R-1428@28 | [CA-R-1428@29-draft-CORE_META_MODEL--permit-confidence-threshold-defaults-and-overrides](../../04_requirement/draft/CA-R-1428@29-draft-CORE_META_MODEL--permit-confidence-threshold-defaults-and-overrides.md) |
| CA-R-1405@25 | [CA-R-1405@26-draft-CORE_META_MODEL--register-core-artifact-type-values](../../04_requirement/draft/CA-R-1405@26-draft-CORE_META_MODEL--register-core-artifact-type-values.md) |
| CA-R-1720@36 | [CA-R-1720@37-draft-CORE_META_MODEL-RULE--use-one-project-journal-for-governed-provenance](../../04_requirement/draft/CA-R-1720@37-draft-CORE_META_MODEL-RULE--use-one-project-journal-for-governed-provenance.md) |
| CA-R-1325@22 | [CA-R-1325@23-draft-CORE_META_MODEL-RULE--keep-composite-subject-expressions-out-of-terminology](../../04_requirement/draft/CA-R-1325@23-draft-CORE_META_MODEL-RULE--keep-composite-subject-expressions-out-of-terminology.md) |
| CA-R-1409@28 | [CA-R-1409@29-draft-CORE_META_MODEL--define-general-artifact-graph](../../04_requirement/draft/CA-R-1409@29-draft-CORE_META_MODEL--define-general-artifact-graph.md) |
| CA-R-1501@19 | [CA-R-1501@20-draft-CORE_META_MODEL-DEFINITION--define-artifact-currentness](../../04_requirement/draft/CA-R-1501@20-draft-CORE_META_MODEL-DEFINITION--define-artifact-currentness.md) |
| CA-R-1655@42 | [CA-R-1655@43-draft-CORE_META_MODEL-RULE--resolve-artifact-classification-from-authority-and-configuration](../../04_requirement/draft/CA-R-1655@43-draft-CORE_META_MODEL-RULE--resolve-artifact-classification-from-authority-and-configuration.md) |
| CA-R-1931@16 | [CA-R-1931@17-draft-CORE_META_MODEL-RULE--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent](../../04_requirement/draft/CA-R-1931@17-draft-CORE_META_MODEL-RULE--use-subject-path-separators-for-broader-to-narrower-and-bearer-to-dependent.md) |
| CA-R-1435@25 | [CA-R-1435@26-draft-CORE_META_MODEL--define-narrower-than](../../04_requirement/draft/CA-R-1435@26-draft-CORE_META_MODEL--define-narrower-than.md) |
| CA-R-1244@31 | [CA-R-1244@32-draft-CORE_META_MODEL-RULE--allow-multiple-direct-term-hierarchy-parents](../../04_requirement/draft/CA-R-1244@32-draft-CORE_META_MODEL-RULE--allow-multiple-direct-term-hierarchy-parents.md) |
| CA-R-1220@24 | [CA-R-1220@25-draft-CORE_META_MODEL-RULE--require-immutable-installed-extension-candidate-provenance](../../04_requirement/draft/CA-R-1220@25-draft-CORE_META_MODEL-RULE--require-immutable-installed-extension-candidate-provenance.md) |
| CA-R-1568@24 | [CA-R-1568@25-draft-CORE_META_MODEL--permit-projections-as-implementation-outputs](../../04_requirement/draft/CA-R-1568@25-draft-CORE_META_MODEL--permit-projections-as-implementation-outputs.md) |
| CA-R-1708@37 | [CA-R-1708@38-draft-CORE_META_MODEL-RULE--classify-artifacts-through-the-extensible-type-registry](../../04_requirement/draft/CA-R-1708@38-draft-CORE_META_MODEL-RULE--classify-artifacts-through-the-extensible-type-registry.md) |
| CA-R-2415@1 | [CA-R-2415@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-term-name](../../04_requirement/draft/CA-R-2415@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-term-name.md) |
| CA-R-1347@27 | [CA-R-1347@28-draft-CORE_META_MODEL-DEFINITION--define-root-term](../../04_requirement/draft/CA-R-1347@28-draft-CORE_META_MODEL-DEFINITION--define-root-term.md) |
| CA-R-1746@42 | [CA-R-1746@43-draft-CORE_META_MODEL--define-projection-artifact-form](../../04_requirement/draft/CA-R-1746@43-draft-CORE_META_MODEL--define-projection-artifact-form.md) |
| CA-R-2276@1 | [CA-R-2276@2-draft-CORE_META_MODEL-RULE--require-one-to-one-canonical-entity-names-with-reusable-terms](../../04_requirement/draft/CA-R-2276@2-draft-CORE_META_MODEL-RULE--require-one-to-one-canonical-entity-names-with-reusable-terms.md) |
| CA-R-1358@31 | [CA-R-1358@32-draft-CORE_META_MODEL--consolidate-single-value-claims-as-one-value-set-claim](../../04_requirement/draft/CA-R-1358@32-draft-CORE_META_MODEL--consolidate-single-value-claims-as-one-value-set-claim.md) |
| CA-R-1359@26 | [CA-R-1359@27-draft-CORE_META_MODEL-DEFINITION--define-claim-value-set](../../04_requirement/draft/CA-R-1359@27-draft-CORE_META_MODEL-DEFINITION--define-claim-value-set.md) |
| CA-R-1465@25 | [CA-R-1465@26-draft-CORE_META_MODEL--define-summary-as-an-atom-property](../../04_requirement/draft/CA-R-1465@26-draft-CORE_META_MODEL--define-summary-as-an-atom-property.md) |
| CA-R-1461@22 | [CA-R-1461@23-draft-CORE_META_MODEL-DEFINITION--define-reconciled-projection](../../04_requirement/draft/CA-R-1461@23-draft-CORE_META_MODEL-DEFINITION--define-reconciled-projection.md) |
| CA-R-1284@23 | [CA-R-1284@24-draft-CORE_META_MODEL--define-type](../../04_requirement/draft/CA-R-1284@24-draft-CORE_META_MODEL--define-type.md) |
| CA-R-1483@20 | [CA-R-1483@21-draft-CORE_META_MODEL--define-authoritative-project-structure](../../04_requirement/draft/CA-R-1483@21-draft-CORE_META_MODEL--define-authoritative-project-structure.md) |
| CA-R-1521@27 | [CA-R-1521@28-draft-CORE_META_MODEL-RULE--resolve-lifecycle-changes-from-applicable-status-models](../../04_requirement/draft/CA-R-1521@28-draft-CORE_META_MODEL-RULE--resolve-lifecycle-changes-from-applicable-status-models.md) |
| CA-R-1765@33 | [CA-R-1765@34-draft-CORE_META_MODEL--prohibit-artifact-type-admission-through-narrower-than](../../04_requirement/draft/CA-R-1765@34-draft-CORE_META_MODEL--prohibit-artifact-type-admission-through-narrower-than.md) |
| CA-R-1335@30 | [CA-R-1335@31-draft-CORE_META_MODEL-DEFINITION--define-terms-graph](../../04_requirement/draft/CA-R-1335@31-draft-CORE_META_MODEL-DEFINITION--define-terms-graph.md) |
| CA-R-1198@28 | [CA-R-1198@29-draft-CORE_META_MODEL-DEFINITION--define-atom-subjects](../../04_requirement/draft/CA-R-1198@29-draft-CORE_META_MODEL-DEFINITION--define-atom-subjects.md) |

The register identifies exact Draft paths because role-only markers alone are ambiguous. Each successor keeps its applicable Current Role, Type, Scope, author, Tier and relations except the specifically reviewed lexical-owner bindings. In particular, M439 remains the authoring Method and E659 checks Method-owned Term Definitions. R2229 is retained as historical/pending predecessor evidence, never cited as proof that the Method-qualified Type is already admitted.

### Post-review Property decisions

The Operator resolves the concept question by using Property as the single canonical Term for the former Property/Dependent Entity distinction. The Claim describes a Property whose identity requires its immediate bearer, connected through IS_PROPERTY_OF. The root, structural, lexical and registered consumer Drafts now use `Entity/Property` and `Entity/Term//Property`. The earlier separate-kind preparations are withdrawn from this active register. The reviewed 112-Draft frontier remains an immutable historical review snapshot; it does not certify these later changes.

The Operator assigns these statements to the indicated content sections:

| Statement | Placement / disposition |
|---|---|
| Exactly one immediate bearer | Formal claim, using `Property {1}((IS_PROPERTY_OF)) Bearer` under the latest two-sided Relation convention. |
| No separate Carrier of the Property's own | Claim. |
| No directed IS_PROPERTY_OF cycles, including self-loops | Structural Property Claim; checked by E449. Other Relation Types remain separately governed. |
| Applicable direct-value Format and cardinality | Claim; exactly one bearer does not imply exactly one value. |
| A Property may itself be a bearer | Semantics; nested Properties, including a possible Status Property, remain permitted. |
| Additional bearer-qualified-identity clause | Not required by this Property definition. |
| Generic prohibition on independent lifecycle / compulsory update rule | Not adopted; the definition does not ban `bearer.property.status`. |

The shared `{cardinality}` syntax has different counted domains. In `property[format]{cardinality}` it counts direct Property values, with `[format]` declaring their Format. The latest `Source {forward-count}((RELATION_TOKEN)){reverse-count} Target` form counts Relation instances in each direction independently: forward per Source, reverse per Target. Each Relation connects two nodes or node instances; neither count is Relation arity or a distinct-target count. `Property {1}((IS_PROPERTY_OF)) Bearer` leaves the reverse count unspecified, so nested Properties remain permitted. R1931 and R2243 record this distinction. The expression is schematic, not an edge asserted between kind nodes.

The Operator explicitly approved **IS_PROPERTY_OF with derived inverse HAS_PROPERTY**. The new Relation Definitions receive fresh unallocated R identities because renaming a Summary cannot repurpose the old Relation's identity. Store the direct fact once; derive the inverse without an independent reverse fact. Current IS_BORNE_BY/BEARS sources remain untouched and are historical predecessors, not aliases for the proposed names.

The Operator approved prohibiting directed IS_PROPERTY_OF cycles, including self-loops. Exactly one outgoing Relation per Property alone would permit two Properties to be each other's bearer, so this is a separate structural constraint in R1193's Claim. E449 checks self-loops, mutual and longer bearer cycles, while preserving valid nested Property chains. The rule does not constrain value references or other Relation Types. The consolidation resolves the Property/Dependent Entity distinction; classification-grammar adoption and other findings from the full review remain pending.

| Additional Current source | Proposed successor |
|---|---|
| CA-R-2243@2 | [CA-R-2243@3-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-cardinality-notation](../../04_requirement/draft/CA-R-2243@3-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-cardinality-notation.md) |
| CA-R-1351@20 | [CA-R-1351@21-draft-CORE_META_MODEL--give-primary-entity-occurrences-no-bearer](../../04_requirement/draft/CA-R-1351@21-draft-CORE_META_MODEL--give-primary-entity-occurrences-no-bearer.md) |
| CA-R-2150@14 | [CA-R-2150@15-draft-CORE_META_MODEL--define-subject-graph](../../04_requirement/draft/CA-R-2150@15-draft-CORE_META_MODEL--define-subject-graph.md) |
| CA-R-1989@15 | [CA-R-1989@16-draft-CORE_META_MODEL-DEFINITION--define-atom-status](../../04_requirement/draft/CA-R-1989@16-draft-CORE_META_MODEL-DEFINITION--define-atom-status.md) |
| CA-M-232@31 | [CA-M-232@32-draft-CORE_META_MODEL--derive-atom-subjects-graph-from-current-atom-subjects](../../05_method/draft/CA-M-232@32-draft-CORE_META_MODEL--derive-atom-subjects-graph-from-current-atom-subjects.md) |
| CA-M-385@20 | [CA-M-385@21-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--generate-readable-entities-graph-trees-programmatically](../../05_method/draft/CA-M-385@21-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--generate-readable-entities-graph-trees-programmatically.md) |

At that stage, the register selected **116 RMED Drafts: 12 primary and 104 consumer successors**. This is the previous 113 minus five withdrawn preparations plus two new Relation Definitions, one lexical Property Method and five additional source-pinned consumer successors. R1193 is listed as primary. The prior 112-file review stays pinned to its own frontier; this changed packet requires scoped Delta checks and later coordinated adoption.

### Withdrawn preparations and adoption dependencies

| Preparation | Disposition |
|---|---|
| `04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-dependent-entity.md` | Retained withdrawn preparation; excluded from the active register. |
| `05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-dependent-entity.md` | Retained withdrawn preparation; excluded from the active register. |
| `04_requirement/draft/CA-R-1251@23-draft-CORE_META_MODEL-RULE--classify-property-as-a-dependent-entity.md` | Retained withdrawn preparation; excluded from the active register. |
| `04_requirement/draft/CA-R-1260@33-draft-CORE_META_MODEL-DEFINITION--define-is-borne-by.md` | Retained withdrawn preparation; excluded from the active register. |
| `04_requirement/draft/CA-R-1267@23-draft-CORE_META_MODEL-RULE--classify-dependent-entity-as-an-entity.md` | Retained withdrawn preparation; excluded from the active register. |

`04_requirement/draft/CA-R-1352@21-draft-CORE_META_MODEL--classify-type-as-a-property.md` is additionally withdrawn by the later Type decision below; it is not selected for adoption.

The older nested `05_method/draft/text-writing-style-and-format/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-property.md` is also retained as withdrawn historical preparation. The active lexical owner is the root-level M Draft in the primary register. Role-only Draft markers alone cannot distinguish these preparations; exact paths control selection.

At coordinated adoption, valid replacement authority and all affected references must be ready before retiring obsolete Current R1260/R2416 Relation names, R1243's old inverse Rule and the redundant R1251/R1267 classifications. None is retired here. R1247 and R2003 keep their immutable Current Summaries and source filenames as lineage; those historical words are not canonical aliases. The repaired R2003 Draft explicitly maps the real Selection name `Dependent Entity Occurrences` to `Property Occurrences`, preserving its selection criteria; Current remains unchanged until adoption. Primary Entity zero-outgoing semantics in R1351 remain intact; Properties borne by a Primary Entity are incoming Relations, so they remain allowed.

### Repair status and remaining adoption limits — historical frontier

1. **Identity collision repaired in Current sources:** recorded assignments establish the ID Term Definition as the original valid owner of `CA-R-2275`. Under Operator authorization and CA-M-276@28, the later Settings definition now carries fresh `CA-R-2423@1` at `04_requirement/CA-R-2423-CORE_META_MODEL-ENTITY_DEFINITION--define-project-settings-obsolete-names.md`. The canonical Project identity lock covered a fresh Current/history/reservation inventory and publication. Only the Settings carrier ID and matching filename changed; its other bytes and the original ID carrier remain preserved. Journal event `0e1853d5-f441-4bc7-9460-bd4db67a0c3c` records the mapping and original carrier text without rewriting either assignment record. The live source collision is resolved; generated CA-PROJ-014/015/016 still contain the old Settings provenance and require regeneration through their original generation path, which is not available in the current connected tooling. Do not hand-edit derived outputs or describe them as refreshed.
2. **Term/entity Draft review:** Property now has the structural target `Entity/Property` and dedicated lexical target `Entity/Term//Property`. R1193 and R1247 use the structural target; R1251 and R1267 preparations are withdrawn after the concept merge. R1348 correctly retains lexical reuse target `Entity/Term//Type`. R1352 preparation remains withdrawn because its Claim conflates the lexical Term Type with a Property; the selected R1284 successor retains the Type Property meaning. R1262 and R1747 successor preparations are withdrawn after consolidation: R1248 preserves the Entity/admission boundaries, the Artifact Method owns lexical meaning, and Current R1993 supplies CARRIES binding meaning. This packet does not invent those remaining paths or convert structural Rules blindly into Methods.
3. **Coordinated adoption:** root and kind structure, Method Type, lexical replacements, ownership rule and consumers must be reconciled as one dependency set. Admit valid replacement authority before retiring old R lexical/Type authority; use exact source paths and hashes and fresh canonical identities where the Role or Summary changes. The consumer and primary Drafts are not Current authority.
4. **Boundary of specialized Method:** R1340 admits authorship/construction conventions; the new specialized Type frames lexical meaning as an authoring and interpretation convention. R2278 distinguishes kind structure from named-instance facts. This packet does not expand PROGRAMMATIC's separate closed Method-Type policy or create an R structural Definition per lexical occurrence.
5. **Coverage and runtime:** no full occurrence campaign, canonical-name reconciliation, complete M lexical inventory, Engine schema change, parser check, Workflow execution, Terms Graph or generated-view publication was performed. The root move removes the former Continuant placement; consumers and any external runtime readers require their own coordinated migration checks at adoption.

### Property and classification clarification — historical decision stage

The Operator confirms that both addressed and classification uses are Properties. Keep the existing meaning and notation; align the real YAML representation with those same Properties. `X.Y` addresses Property Y; `X.Y: Z` expresses that Z is an allowed value of Y; `X/Y: Z` identifies a narrower kind of X through classification Property Y and admitted value Z. The complete `Y: Z` segment qualifies the kind without creating an intermediate X/Y kind. No separate Classification Property kind or lexical Term is introduced by this usage distinction.

Use `Atom/Content Role: Method` for the example: Method is a Content Role here. Current CA-D-478@27 already states that qualified classifications are ordinary metadata Properties, maps Content Role to `content_role` and Type to `type`, and prohibits inventing a nested object or field from a display path. CA-D-276 supplies the canonical value encodings. YAML frontmatter is the existing Carrier location for those Property values, not a second Property ontology. No key, encoding, filename template, Carrier format or runtime is changed.

The interim statement “Type is not a property” is superseded by this later explicit clarification. At that stage, the explored `=` qualification alternative and possible uses of `::` or `<::` were not adopted. The later Status Group clarification below selects `::` with a classification-axis meaning. Colon retains the allowed-value meaning and slash retains narrower-than. R1284 preserves Type as a Property and explains its classification use; R1931, M228 and E383 were aligned to that stage without a new grammar. Parenthesized qualification was still unresolved at that stage; the later relative Property qualification clarification below now resolves its target and inheritance. No parser implementation was established by either stage.

R1352's preparation remains withdrawn because it incorrectly classifies the lexical Term Type as a Property. Its valid underlying Type-as-Property meaning is retained in R1284; no Current Rule is retired. The previous Type-not-Property consumer inventory is historical and must not drive new successor creation or retirement. At that stage, the selected register contained 115 Drafts: 12 primary and 103 consumer successors. Other full-review questions and coordinated adoption remain open.

### Focused review of the eight successors after Property consolidation

| Draft | Entity or Term concern | Review result |
|---|---|---|
| R1193@23 | Property kind | Corrected to `Entity/Property`; approved Claim, Formal claim and Semantics recorded. |
| R1352@21 | Lexical Term versus Type Property | Withdrawn for Term/entity conflation; Type-as-Property meaning is retained in R1284. |
| R1251@23 | Property narrower than the former separate kind | Withdrawn; the merged concept would make this classification reflexive. |
| R1267@23 | Former separate kind narrower than Entity | Withdrawn; R1193 and the root branch supply the Property kind. |
| R1262@23 | Entity category versus represented instance | Withdrawn preparation; Artifact lexical distinction is preserved in its Method. |
| R1747@27 | Native target versus admitted instance/Carrier binding | Withdrawn preparation; generic admission boundary is consolidated into R1248. |
| R1247@23 | Qualified identity of Property occurrences | Corrected to govern `Entity/Property`; inherited Summary preserves lineage. |
| R1348@24 | Reuse lexical Term Type in qualified names | Correct Term target; no correction required. |

The latest Property consolidation resolves R1193's concept target and withdraws the now-redundant R1251/R1267 preparations. The Artifact decision resolves the last two original target questions in Drafts. Type follows the shared-Property clarification; the interim no-Property inventory is superseded. R1738 is resolved by the later Settings Property decision; D416 is resolved by the Carrier-kind decision below. R1348 needs no correction. Broad Entity substitution is not used to conceal those gaps or duplicate the existing Entity definition under R2278.

### Historical Dependent Entity extension

Before the Property consolidation, the separate-kind extension brought the register to 110 RMED Drafts: eight primary and 102 consumer successors. The Entity and Term lexical definitions then brought it to 112. Those historical counts and the frozen FPF review describe earlier frontiers. The former separate structural/lexical Dependent Entity preparations and the old-name R1260 successor are now withdrawn from the active register. The later explicit Property and Relation-name decisions above supersede their former operative paths and names.
### Entity name and reusable Term

The latest Operator correction supersedes the earlier general permission: an Entity outside the Term branch cannot have a complete canonical name that is just one registered Term. The only exception is `Entity`, because it is the Subject root. R / Entity Definition governs `Entity`; M / Term Definition governs `Entity/Term//Entity`. Their matching word is the explicit exception, not a general allowance for all roots or all Entity names.

Identification and comparison use the full source-admitted expression. Schematically, `Atom/(.Content Role: X)/(.Type: X)` is possible because the repeated X components are differently qualified; each value remains separately admitted in its own context. This does not introduce X, grant a new value admission or define another grammar. The complete expression `Entity/Property` is distinct from the reusable Term Property, so its structural and lexical Drafts have distinct targets under this full-expression distinction.

The Term-kind and Entity lexical Drafts now record the restriction and sole exception. The canonical-name and qualified-value-domain Rule Drafts carry the full-expression check and repeated-X example. The Project and Project Implementation examples do not extend the Subject-root exception. This correction changes no Current source, performs no promotion and creates no new numeric identity.

### Term kind and the Term named Term

The Operator additionally requires the lexical Term Term. R / Entity Definition governs `Entity/Term`; the new M / Term Definition governs `Entity/Term//Term`. The structural kind Draft keeps its exactly-one Name constraint and states kind-membership requirements; the new Method supplies the word's dedicated meaning. Self-reference in that meaning creates no further lexical instance or infinite definition chain. Both declarations remain Draft dependencies, not evidence of Current adoption.

The full-expression correction updates nine existing RMED Drafts and this proposal. It restricts one-Term complete entity names outside the Term branch to the sole Subject-root Entity exception, preserves qualified component reuse, now rendered schematically as `Atom/(.Content Role: X)/(.Type: X)`, and keeps relation-token resolution separate from canonical entity-expression comparison. The added Term Method brought that historical register to 112 Drafts; no other root exception, rename or value admission is introduced. Independent semantic review passed both the nine corrected Drafts and the new lexical Method with its kind counterpart. Checks of that historical frontier covered all 112 Drafts, 112 register links and 102 pinned consumer sources. No full occurrence campaign or runtime validation is claimed.

### Connection to the ongoing Workflow logic discussion

The confirmed Create Draft input rule can now say: **if the input ID is Empty, create a Draft of a new Atom**. A valid Current or Archived reference selects the existing-Atom path; a Draft reference routes to Edit Draft; invalid references error and stop; ambiguous references show options and wait for the Actor. An intentionally selected archived @3 supplies content while latest Current @7 supplies the next proposed version @8; Current remains untouched.

Workflow Atoms must carry a Mermaid scheme with all Steps, and Steps with Substeps also require a sequence scheme. No new Workflow or Step Atom is created by this Term packet. The remaining logic questions—content authoring versus a prepared payload, the exact Update archival/promotion boundary, and the scope of the requested no-logic/linear diagram rule—are not silently answered by accepting this Term hierarchy.

### Preparation and verification

The original preparation contained 107 RMED Drafts: six primary definitions/structural changes and 101 consumer successors, plus this Analysis tracker. The Dependent Entity extension added three Drafts; the Entity lexical clarification and explicit Term lexical definition add one each, yielding the 112 entries registered at that historical stage. No canonical numbers were allocated; Current sources, history, Journal, runtime and Git remain unchanged by this preparation. Independent primary-six review and independent consumer-101 review passed, including the focused R1703 heading repair. The original fence-aware and Type-specific layout checks, Draft identities/versions, 107 register links, source pins and manifest hashes passed; the extension receives its own updated checks and independent review. The extension passed independent semantic review and updated checks of all 110 Draft identities/layouts, 110 register links and 102 consumer source pins. All 1,144 Current Core fingerprints in the extension baseline remain unchanged. Three new Drafts and seven existing-Draft updates are recorded; no canonical number was allocated or Current Atom promoted by the extension. All 1,058 Current Core source fingerprints match the preparation baseline. Relation Definition notation_for_subject sections retain their registered R2228/R2392 format. These are Draft-consistency checks, not adoption or runtime proof.

### Property consolidation Delta checks

At that stage, the selected post-decision packet had 116 unique Draft paths and register links: 12 primary definitions/structure changes and 104 consumer successors. All selected frontmatter parses, exact local Draft dependency links resolve, and the 108 numeric successors retain their Current Summary, Content Role, Type and other checked immutable metadata with N+1 versions. Eight unallocated definitions retain role-only markers. Fifteen previously registered Drafts changed, eight were added, and five original preparations were withdrawn from this active register. The older nested Property Method remains withdrawn historical preparation.

Scoped source checks confirm binary endpoints, exactly-one outgoing typed Relation counting distinct from value cardinality, a strict derived inverse, one Property root branch and one selected lexical Property owner. Historical old-name provenance and immutable summaries/Selection names are preserved as labelled lineage; no old-name alias is admitted. The direct Relation's registered dot-notation section and the counterpart's short-reference template follow CA-R-2228/CA-R-2392. Independent Delta review passed after operational rendering prose was corrected to use Property consistently. This is a review of the changed decision frontier, not a repeat or replacement of the frozen full FPF review.

All 1,086 Current Core fingerprints captured at the start of this consolidation match. The scoped whitespace check passes. The local evidence manifest, source receipts and independent review are under `/tmp/cce-property-relation-adoption-20261029/`; that temporary evidence does not constitute a durable governed report or adoption record. No canonical identity was allocated, no Current Atom was promoted or retired, and no runtime, parser or generated-view effect was checked. That Delta review predates the subsequent cycle decision; the other unresolved full-review findings remain open.

### Cycle-decision Delta checks

The Operator approved forbidding IS_PROPERTY_OF cycles, including self-loops. This decision updates R1193, its lexical Property Method, the direct Relation Definition, E449 and this proposal. R1193 owns the structural constraint; the Relation and lexical definitions refer to that authority, and E449 records the acceptance/rejection cases. No new formula syntax, transitive fact, general graph-cycle prohibition or requirement for a chain to terminate at a particular kind is introduced.

Checks passed for all 116 selected Drafts' frontmatter and the unchanged exact register; changed local links resolve, immutable metadata/Summaries are preserved, and scoped whitespace checks pass. All 1,086 captured Current fingerprints still match. The temporary decision snapshot and checks are under `/tmp/cce-property-cycle-20261029/`. Runtime checks and promotion were not performed; the earlier full-review issues remain open.

### Property qualification and YAML alignment checks

The latest clarification updates three registered Drafts: R1284 restores Type as a Property, R1931 clarifies the existing classification use, and M228 points to the existing D478 metadata mapping. E383 is unchanged because its checks already fit. The withdrawn R1352 preparation now explains the actual Term/entity conflation rather than rejecting Type-as-Property. This proposal records the supersession explicitly. No notation, YAML key/value encoding, filename template, Carrier structure or runtime changed.

The exact 115-Draft register, frontmatter and local links pass the scoped checks. The three changed registered Drafts retain their Current Summary, Content Role, Type and N+1 version. All 1,086 captured Current fingerprints still match. One unrelated existing successor is stale: E520@28 Draft now has the same Version as Current E520@28, so the packet cannot claim universal N+1 readiness. That Draft is unchanged here and needs a separate source-pinned rebase before adoption. Independent semantic Delta review passed for this bounded clarification; the earlier full-review issues remain open. Temporary snapshots and verification are under `/tmp/cce-property-qualification-20261029/`. Parser/runtime checks and promotion were not performed.

### Adoption scope and review gate — latest Operator task

The Operator requests review and repairs of the full Term/Property proposal,
then promotion to Active and migration to the selected notation. This includes
the 125-Draft Term/settings packet and its necessary notation-owner closure;
it is not a notation-only extraction that leaves IS_PROPERTY_OF and
Method-owned lexical definitions pending. Current promotion remains gated by
fresh source pins, complete review, correct identity allocation, and the
admitted lifecycle execution path.

The Operator closes the former Classification-placement gap: use named
Relation instances `Entity/Graph Syntax <+ Relation//HAS_CLASSIFICATION` and
`Entity/Graph Syntax <+ Relation//IS_CLASSIFIED_BY`. No new Classification
Entity kind or branch is requested. A generic Classification definition,
if needed, is a Term Definition, not a structural kind. The established axis
and membership meanings are not made into an invented inverse pair by this
clarification.

The migration covers `X/(.Property: Value)`, `Part +> Whole` / `Whole <+ Part`,
`X >| Y` / `Y |< X`, and independent pre-/post-Relation count slots. It also
aligns generic allowed-value `:`, declared-Entity `@`, logical grouping `()`,
Property `[format]{cardinality}`, escaped literal characters, and named
Relations without treating them as Terms. `//` keeps named-instance meaning.
Old `Whole >{n} Part` becomes `Whole {n}<+ Part`; an opposite count is added
only when independently established. Archives, literal source quotations,
journals, and passed FPF artifacts retain their historical content.

Initial full review has found stale same-version successors and an obsolete
M301 preparation. Rebase from live Current sources and preserve their newer
content; use the live M444 owner for that Method rather than restoring M301.
Exact repaired identities, retirement references, implementation checks and
migration effects will be recorded before claiming adoption complete.

### Selected Composition, Classification and two-sided Relation cardinality — latest decisions

The Operator selects `Part +> Whole / Whole <+ Part` and `something >| its classification / its classification |< something`. The Composition pointer faces the Whole in both written directions; the Classification pointer faces the Classification endpoint. These spellings supersede bare `>` / `<` containment and the earlier `::` axis spelling. The underlying stored IS_CONTAINED_BY and derived CONTAINS pair, and HAS_CLASSIFICATION, retain their meanings. The reverse axis spelling `|<` adds no separately authored reverse fact or new canonical inverse Relation Type name. Separate `::>` / `<::` classification-membership preparations are not repurposed.

The selected Composition direction differs from the FPF report's earlier conditional `Whole +> Part` candidate. The latest human selection controls; the passed FPF report remains an immutable comparison snapshot.

Relation cardinality has two independent slots:

```text
Source {forward-count}RELATION{reverse-count} Target
Step {1}+>{1+} Workflow
Workflow {1+}<+{1} Step
Property {1}((IS_PROPERTY_OF)) Bearer
```

The count before the token constrains links in the written Source-to-Target direction per Source; the count after it constrains the reverse count per Target. Each Step belongs to exactly one Workflow, and each Workflow has one or more Steps. Reversing the written direction swaps the count positions. An omitted side remains unspecified; count meaning does not depend on whether one or both slots are shown. This supersedes the former Relation convention that every postfix count was outgoing from the left. Relation instances remain binary; the slots count applicable links in the two directions, not Relation arity. Property value cardinality remains `x.y[format]{cardinality}` and is independent of either Relation count.

The earlier bounded preparation updated R1931, R2243, M228 and E383; R1193's exactly-one-bearer spelling; the glossary, Status Group and HAS_CLASSIFICATION Drafts; and the M301 dependency spelling. M301 still has no Current predecessor and is not revived or made promotion-ready. New source-pinned successors R1368@28 and R2419@2 retain the existing full-pair/reference ownership. Their exact paths are `04_requirement/draft/CA-R-1368@28-draft-CORE_META_MODEL--define-containment-relation-pair.md` and `04_requirement/draft/CA-R-2419@2-draft-CORE_META_MODEL-RELATION_DEFINITION--define-is-contained-by-relation.md`. They remain outside the 125-Draft Term/settings register, like the separate Classification preparations.

The selected baseline is `02_analysis/draft/CA-A-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--notation-baseline-for-intuitive-symbol-review.md`. Evidence and the bounded residual inventory are under `/tmp/cce-selected-composition-classification-notation-20261030/`. Other structural-path consumers and Current sources still need coordinated adoption; no parser, runtime, Current Atom, generated view or filename is changed by this preparation. No alternative to `X/(.Y: Z)` was selected.

### Historical Atom Status Group and classification notation — superseded spellings

The Operator earlier distinguished Property, Classification and a proposed Classification Property overlap. The later relative Property qualification decision below supersedes the separate Classification Property category. Content Role and Type remain Properties and retain their real YAML mappings. Status Group remains a Classification without a separate Property or stored `status_group` field; the earlier demand for a separate Classification kind is withdrawn by the latest Operator clarification.

The Operator's latest clarification selects `Atom.Status :: Status Group` and these Formal claim declarations:

```text
Atom.Status :: Status Group: Draft > Draft
Atom.Status :: Status Group: Archived > Archived
Atom.Status :: Status Group: Current > * not in (Draft, Archived)
```

They declare allowed groups and their Status parts, not simultaneous membership in all three. The Operator explicitly defines `>` as has-parts and `<` as is-part-of; neither is a numeric comparison or narrower-kind operator. The underlying direct containment fact remains Part IS_CONTAINED_BY Whole, with CONTAINS derived. `* not in (Draft, Archived)` ranges only over admitted Atom Status values. The exhaustive, mutually exclusive Status mapping selects one: Draft to Draft, Archived to Archived, every other admitted Status to Current, including Backlog, Active, Done and Canceled where allowed. No second exact-one Rule Atom is needed. Atom Statuses remain the classified subjects, superseding the earlier direct Atom classification `Atom :: Status Group`. Filename and placement rules still describe their effects on the Atom or its Carrier explicitly in their Claim scope and Claim.

The existing preparation `04_requirement/draft/classification-and-status-groups/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-status-group.md` now uses the full Entity-rooted `Atom.Status :: Status Group` target and records the three Formal claim lines. The `::` spelling supersedes `..` for this proposal. The Operator approved HAS_CLASSIFICATION as the Relation name behind `::`, applicable to Classification axes generally. The new sibling preparation `04_requirement/draft/classification-and-status-groups/CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-has-classification.md` defines the directed Entity-to-Classification-axis Relation, distinct from historical organizational membership and from IS_CLASSIFIED_BY membership in a particular classifier. This decision approves the name and proposed meaning; it does not admit a Current operator.

This proposal extends colon allowed-value notation to Classification contexts as well as Property contexts. Current R1245 and R1436 still restrict that meaning to Properties; coordinated Draft changes to those sources and the syntax consumers, plus the Classification definition, are dependencies before adoption. The later relative qualification decision removes the proposed separate Classification Property category. No admitted Current operator, parser or runtime effect is claimed. These Status Group preparations remain outside the earlier frozen 115-Draft Term register and need their own coordinated review.

### Historical Status Group and Delivery scope — meaning retained, spelling superseded

Status Group classifies Atom Statuses across Content Roles. Group-dependent rules describe their effects on the Atom or its Carrier according to their own contribution. The base group-based filename template is selected through `Atom.Status :: Status Group`. The Operator's P/Plan override remains scoped by `Atom/Content Role: Plan`; it does not move Status Group itself to a Role-qualified scope. Other Role-dependent values remain base-template parameters rather than separate template definitions.

| D Atom Subject | Delivery contribution |
|---|---|
| `Atom.Status :: Status Group: Archived` | Filename template for Carriers of Atoms whose Status belongs to the Archived group, as specified in the D Claim. |
| `Atom.Status` | Folder location of the Atom Carrier according to its Status. |

The contributions compose into a Carrier address: the group-qualified filename and Status-dependent folder. These are conditional rules for the Atom/Carrier, not constraints inherited by the Status value entity. This clarification does not globally redefine classification inheritance or create another Property/field.

The Operator selects the P-specific template override rather than extending a common sequence-number field to P and O/Steps. The common template remains the default; the P override preserves its optional Work Sequence Number prefix and governs only its filename contribution. Draft/Archived identity-marker obligations remain applicable inside that template. This decision grants no new O/Steps sequence-number permission. Current D283@31 already excludes Plans, and D469@23 already supplies the ordered Plan stem, so those existing policies provide the implementation basis without a duplicate D Atom or filename migration. D289@23 supplies the Archived version-marker rule; D466@21 supplies Status-dependent placement selection. All these Current policies and existing filenames/references remain unchanged by this Draft decision.

The superseded Property-shaped Status Group target and its string-value cardinality are removed. YAML keys and encodings, Type/Content Role Property meanings and Current sources are unchanged. The scoped checks cover Draft YAML, unchanged identity/Role/Type/Version/Summary, the three Formal declarations and Current fingerprints; they do not establish adoption readiness.

The later HAS_CLASSIFICATION and Status-subject correction is checked separately under `/tmp/cce-has-classification-20261030/`. It edits this proposal and the Status Group preparation and adds one Relation Definition preparation. These classification preparations remain outside the selected 125-Draft Term register. No Current source, parser, generated graph, filename or actual settings value is changed.

### Relative Property qualification and inheritance — latest clarification

The Operator proposes `Atom/(.Type: Method)` instead of introducing a separate Classification Property category. The parenthesized Property expression is relative to the preceding Atom context: `.Type` addresses `Atom.Type`, and `: Method` supplies the qualification. The whole expression denotes an Atom with that Type value, narrower than Atom; it does not denote a Property made into a narrower kind of its bearer. The Operator explicitly confirms that this qualified Atom inherits all applicable Atom features and constraints. This resolves the earlier apparent inheritance conflict and supersedes the earlier Classification Property category proposal.

This notation example does not independently admit Method as a Type value or change its separately governed Content Role meaning. Concrete allowed values still require their existing authority. `Atom/(.Content Role: Method)` expresses the corresponding Content Role qualification.

The `>`/`<` Status Group correction and this relative qualification are recorded under `/tmp/cce-status-group-parts-20261030/`. Parenthesized relative qualification, the inverse containment short notation, the Classification axis, and `* not in (...)` need coordinated grammar/evaluation reconciliation before adoption. Existing full-path sources and generated views are not rewritten by these examples, and no Current or parser implementation is changed.

### Historical Artifact Term and Rule correction — superseded by consolidation

The Operator states that Artifact is a Term and describes Artifacts as Entity instances represented in a Carrier, with files, folders and database rows as examples. The new lexical Method governs `Entity/Term//Artifact`. No separate Artifact entity kind, classification axis, Property or second identity is introduced. The represented instance retains its admitted identity and remains distinct from its Carrier.

R1262 and R1747 are generic structural boundary Rules over Entity instances and their Carrier representations, so their corrected Governs target is `Entity`, with Carrier and lexical Artifact dependencies. This follows Current R1994's existing no-Artifact-branch meaning; it is not a substitute for an invented Artifact kind. R1262 keeps the Entity/category versus represented-instance distinction. R1747 preserves admission of the Entity instance and Carrier binding without demanding another Artifact identity. Native file existence alone is not admission; an admitted Implementation Entity instance can be referred to as an Artifact when represented.

The five original TR-F01 target cases now have Draft dispositions: Property has structural and lexical definitions; redundant Property/Dependent Entity preparations are withdrawn; Type retains its Property meaning while the Term/entity conflation preparation is withdrawn; Artifact has a lexical Method and its structural Rules govern Entity. The frozen FPF report is unchanged. R1738 and D416 receive their later Property/kind dispositions below; other findings still require disposition; this is not a full-packet review or Current adoption.

At that stage the Term packet selected 116 Drafts: 13 primary and 103 consumer successors, adding one Artifact lexical Method to the previous 115. Earlier counts describe their historical frontiers. The separate Status Group/classification preparations remain outside this register. Coordinated grammar/source adoption remains open. The current predecessor inventory also shows unrelated existing staleness: E246@45, E520@28, M125@45, M237@29 and M113@38 Drafts now have the same Version as their Current sources; M301@27 Draft has no Current M301 source. These items require explicit reconciliation and cannot be blindly promoted or used to revive a retired source. They are unchanged in this Artifact correction.

The Artifact Delta passed independent semantic review and scoped checks: one new Method, two corrected Rule successors, exact 116-Draft register links, YAML/metadata/immutable Summary preservation, N+1 and predecessor pins for the two edited Rules, and all 1,086 captured Current fingerprints unchanged. Evidence is under `/tmp/cce-artifact-term-20261030/`. These checks do not claim all 116 successors are ready for adoption. No canonical number, Current source, runtime, parser or generated view was changed.

### Artifact/Entity consolidation and planned retirement — approved

The Operator approved consolidating the three Rules rather than keeping their repeated meanings in separate Atoms. The selected owners are R1248 / Entity Definition for Entity and admission boundaries, M / Term Definition Artifact for lexical meaning, and existing R1993 / CARRIES Relation Definition for Carrier-binding direction and meaning. No new Rule or CARRIES successor is needed.

| Former source meaning | Preserved owner |
|---|---|
| R1262: Artifact is not a synonym for the Entity category | Artifact Term Definition; no additional identity or disjoint kind. |
| R1747: native existence alone does not admit an Entity instance or Carrier binding | R1248 Claim and Semantics; applicable kind/source/runtime authority remains in force. |
| R1994: Subject nodes address things/topics; descriptions and Carriers remain distinct; categories stay open | R1248 Claim and Semantics; lexical Artifact meaning is owned by its Method. |
| CARRIES / IS_CARRIED_BY binding meaning | Current R1993@16, reused unchanged. |

The two corrected Rule successor preparations are now withdrawn and excluded from the active register: `04_requirement/draft/CA-R-1262@23-draft-CORE_META_MODEL-RULE--keep-entity-and-artifact-distinct.md`; `04_requirement/draft/CA-R-1747@27-draft-CORE_META_MODEL--distinguish-native-targets-from-governed-artifacts.md`. Their prior Claims and immutable metadata are retained as historical preparation. R1994 needs no competing successor because its useful constraints are preserved in the Entity Definition. All three Current Rules remain unchanged and active until coordinated adoption and retirement.

| Planned Current retirement | Exact source | SHA-256 |
|---|---|---|
| `CA-R-1262@22` | `04_requirement/CA-R-1262-CORE_META_MODEL-RULE--keep-entity-and-artifact-distinct.md` | `398c6acd55c8b34e20eb1139d72383d9a47b17961a581ea289754118d9aec14a` |
| `CA-R-1747@26` | `04_requirement/CA-R-1747-CORE_META_MODEL--distinguish-native-targets-from-governed-artifacts.md` | `5efa75b803aa4aa036e6c0c1209d43b604be491275f7c4684f9e33b75cb038a4` |
| `CA-R-1994@14` | `04_requirement/CA-R-1994-CORE_META_MODEL--define-entity-node.md` | `41b8b0ef51a71969db07cec2008a19e3c6372e90ae9cc66727de31287d722ce8` |

Adoption must first establish valid replacement authority in R1248 and the Artifact Method, with the pending Term/Method-Type dependencies resolved. Reconcile operative references, preserve source/history evidence and follow the existing Current archival/retirement flow; then remove the three redundant Current authorities from active use. This plan introduces no new Status, lifecycle gate, per-Artifact registration, duplicate identity or Definition for every runtime instance. Historical source pins remain evidence, not continuing authority dependencies. Generated copies, installed sources and runtime consumers require their own normal refresh/check path; this Draft does not modify them.

At that stage, the selected Term register had **114 Drafts: 13 primary and 101 consumer successors**, removing the two Rule preparations from the previous 116-file frontier. The separate Status Group preparations stay outside this register. Other FPF findings and existing predecessor staleness remain open; no full-packet adoption readiness is claimed.

The consolidation passed independent semantic Delta review: all three Rules' distinct meanings are preserved in the selected owners. The exact 114-Draft register, YAML/local links, root Definition metadata/N+1 and unchanged Formal claim, lexical Method Claim, retained withdrawn Rule Claims, three Current source pins and all 1,086 captured Current fingerprints pass scoped checks. Exact-ID inventory covered authoritative Methodology, direct project sources and both Engine roots, including `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE`; it found no independent live Current semantic consumer. Mirrors, generated/installed copies, history and planning evidence are not independent consumers and were not rewritten. Evidence is under `/tmp/cce-artifact-consolidation-20261030/`. These are bounded Draft checks, not Current retirement, runtime validation or stale-packet repair.


### Markdown Carrier kind hierarchy — Operator decision, TR-F07

The Operator explicitly selects `carrier/file/markdown/Markdown Atom Carrier`. Using existing canonical Entity-rooted spelling, the hierarchy is:

```text
Entity/Carrier/File
Entity/Carrier/File/Markdown
Entity/Carrier/File/Markdown/Markdown Atom Carrier
```

These are structural Entity kinds connected by narrower-than specialization and its applicable inheritance. The final kind inherits File through Markdown. They are not lexical Terms related through a Term hierarchy, and no new Artifact/Carrier identity is allocated by a kind declaration alone. Current R1957@10 supplies the existing File parent; the two new R Definitions supply only the specialization differences. No duplicate File definition or automatic lexical Method is introduced.

Current D262@26 admits the Markdown Carrier format. R2269@2 is actually a Rule despite its filename: generic Markdown permits optional YAML Frontmatter and logical content regions. D356@21 requires YAML followed by Main Content only for authoritative Markdown Atom Carriers, and Current D478@29 governs applicable metadata/body placement. The new kind definitions must preserve those scopes rather than require YAML for every Markdown file or impose complete Current-Atom fields on an incomplete Draft. Concrete serialization, filename policies and inherited Property definitions remain in their existing owners.

The D416@28 successor preparation is now withdrawn from the active register because its Claim wrongly classifies a Term in a Delivery Atom. Current D416@27 at `07_delivery/CA-D-416-CORE_META_MODEL-ENG_DECISION--classify-markdown-atom-carrier.md`, SHA-256 `f438282578c8add490f64cae986e07fa0932af8e51bf2e6d4bc808c35c85d8e8`, remains unchanged. Its retirement is planned only after valid kind Definitions and affected consumers are ready. The existing D representation policies remain in force; this plan does not retire their actual format constraints.

The bounded impact inventory found one actual Engine test consumer: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/tests/test_term_hierarchy.py:39-40` asserts D416's old Term-hierarchy claim. Coordinated adoption must update that test to the structural-kind meaning and preserve genuine Term-hierarchy coverage. No test source, runtime, Current source or generated view is changed here.

At that stage, the selected Term packet had **115 Drafts: 15 primary and 100 consumer successors**: previous 114 minus the withdrawn D416 preparation plus two fresh role-only R Definitions. This records the TR-F07 design disposition in Drafts; it is not a new full FPF review or Current adoption. Other findings and stale predecessor reconciliation remain open.

The two new Entity Definitions and D416 disposition passed independent semantic Delta review. Scoped checks pass for the 115 exact register entries, Draft YAML/local links, two unique kind owners, source hashes, preserved withdrawn D416 metadata/Claim and whitespace. Relevant Current source pins, including D416@27, match; this work changes Drafts only. The wider Current baseline changed concurrently for R1697, R1698 and R1699 outside this edit; those changes are preserved and require a fresh whole-packet frontier check before adoption. No whole-Current unchanged claim is made for this stage. Temporary evidence is under `/tmp/cce-markdown-carrier-kinds-20261030/`. The Engine test and runtime were not executed or modified.


### Project Settings Properties — Operator decision, TR-F08

The Operator selects `Project.Settings.Name` and `Project.Settings.Prefix`, and explicitly says Prefix usage is not the matter here. The named-instance example is `Project//caprmedio.Settings.Prefix = CA`: an instance value, not a global allowed-value restriction or an instruction to write settings. The R1738 successor now defines the Property group and its children instead of saying “the Term Project Settings”. Its parent `{0}` still means zero direct values, with each declared child `[string]{1}`; it does not make the children optional.

The two fresh field Definitions replace the old Project Name / Atom Prefix names. Fresh role-only identities are prepared because their Summaries change; no R2413/R2414 number is repurposed. The canonical logical paths are corrected without introducing another Settings entity, selected-value copy, Artifact identity or automatic lexical Method. Existing TOML keys remain `project.name` and `artifacts.identity.project_prefix`; actual values, encodings, schema version and initialization timing remain unchanged.

The serialization and checking successors carry only the logical-name correction. The earlier Atom/Projection/Journal discussion is not a prefix-use policy decision in this packet. Existing consumer Subjects and wording are synchronized without changing their unrelated filename, schema, ownership, Journal/history or MCP behavior. The instance equality example records meaning only; no general assignment parser or Current instance admission is claimed.

| Supporting preparation | Actual Draft |
|---|---|
| `CA-D` preparation | [CA-D-draft-CORE_META_MODEL-DECISION--serialize-project-prefix](../../07_delivery/draft/CA-D-draft-CORE_META_MODEL-DECISION--serialize-project-prefix.md) |
| `CA-R-1750@38` preparation | [CA-R-1750@38-draft-CORE_META_MODEL--partition-operator-settings-between-settings-artifacts](../../04_requirement/draft/CA-R-1750@38-draft-CORE_META_MODEL--partition-operator-settings-between-settings-artifacts.md) |
| `CA-D-366@28` preparation | [CA-D-366@28-draft-CORE_META_MODEL-ENG_DECISION--serialize-project-settings-content-in-toml](../../07_delivery/draft/CA-D-366@28-draft-CORE_META_MODEL-ENG_DECISION--serialize-project-settings-content-in-toml.md) |
| `CA-D-375@28` preparation | [CA-D-375@28-draft-CORE_META_MODEL-ENG_DECISION--serialize-project-initialization-identity](../../07_delivery/draft/CA-D-375@28-draft-CORE_META_MODEL-ENG_DECISION--serialize-project-initialization-identity.md) |
| `CA-D-292@33` preparation | [CA-D-292@33-draft-CORE_META_MODEL-ENG_DECISION--serialize-external-project-goal-filenames](../../07_delivery/draft/CA-D-292@33-draft-CORE_META_MODEL-ENG_DECISION--serialize-external-project-goal-filenames.md) |
| `CA-D-392@25` preparation | [CA-D-392@25-draft-CORE_META_MODEL-ENG_DECISION--register-obsolete-project-names](../../07_delivery/draft/CA-D-392@25-draft-CORE_META_MODEL-ENG_DECISION--register-obsolete-project-names.md) |
| `CA-D-398@25` preparation | [CA-D-398@25-draft-CORE_META_MODEL-ENG_DECISION--encode-configuration-surfaces-in-owning-atoms](../../07_delivery/draft/CA-D-398@25-draft-CORE_META_MODEL-ENG_DECISION--encode-configuration-surfaces-in-owning-atoms.md) |
| `CA-E-459@37` preparation | [CA-E-459@37-draft-CORE_META_MODEL-POLICY--validate-authoritative-project-settings-artifact](../../06_evaluation/draft/CA-E-459@37-draft-CORE_META_MODEL-POLICY--validate-authoritative-project-settings-artifact.md) |

Current R2414@1, R2413@1 and D376@25 are planned replacement/retirement sources after their fresh Name/Prefix Definitions and Prefix serialization authority are valid and consumers are reconciled. All remain Current and unchanged here. The role-only Prefix Decision uses its actual Decision Type token in its new filename; this renames only the just-created Draft, not any existing Carrier or setting. Source-pinned evidence records their exact predecessors.

The selected Term/settings packet now has **125 Drafts: 17 primary and 108 consumer successors**, adding two field Definitions, one Prefix Decision and seven pinned consumer successors to the previous 115. Other FPF findings, classification grammar and stale predecessor reconciliation remain open; this is a bounded TR-F08 Draft disposition, not Current adoption.

| Planned replacement source | Exact Current carrier | SHA-256 |
|---|---|---|
| `CA-R-2414@1` | `CA-R-2414-CORE_META_MODEL-ENTITY_DEFINITION--define-project-settings-project-name.md` | `462e610a4808574eec843bc8bfd61a024933a604ff34c49ceedd81317da85a54` |
| `CA-R-2413@1` | `CA-R-2413-CORE_META_MODEL-ENTITY_DEFINITION--define-project-settings-atom-prefix.md` | `f27b7d0f5e60396f48c7f5ba660aeb34a8fe7ac7272f228ed212d80c9760607c` |
| `CA-D-376@25` | `CA-D-376-CORE_META_MODEL-ENG_DECISION--serialize-the-project-atom-prefix.md` | `3b04a0bd6dfce9eec731a550edcdd86c6fdba8560255477bd4810f3c254bd614` |

Independent semantic Delta review passed for the logical-field correction. Scoped checks pass for all 125 exact register entries, Draft YAML/local links, unique Name/Prefix Definition owners, unchanged metadata/Summaries and N+1 versions of the edited parent and seven numeric consumers, fresh role-only identities for the changed-Summary replacements, preserved TOML keys/closed signature and all 1,087 captured Current fingerprints. Parent `{0}` and child `[string]{1}` meanings are preserved. Evidence is under `/tmp/cce-project-settings-properties-20261030/`. No Current replacement/retirement, setting-value write, runtime/parser implementation or prefix-use policy change was performed.


### Full-packet review and adoption closure — latest task

The Operator explicitly selected the full Term/Property proposal, including IS_PROPERTY_OF, Method-owned Term Definitions and the complete 125-Draft register after review and repairs, followed by notation migration. This selection supersedes the narrower notation-only adoption option. Earlier stage counts, pending findings and unchanged-file statements above describe their recorded historical frontiers.

The full review read all 125 selected Draft bodies and their 110 live numeric predecessors, plus six related Drafts and two additional predecessors. Repairs rebase ten stale successors from the actual Current bytes, preserving newer constraints and metadata rather than merely incrementing their Version. The retired M301 preparation is withdrawn; live M444@1 supplies M444@2 instead. This preserves the live Method's typed-relation citations, shared lead-in/list guidance and Workflow-call bindings. The register above now uses the repaired paths and actual Current versions.

The required adoption closure is **130 Drafts**: the repaired 125-Draft register, with M444 replacing M301, plus five source dependencies. The five additions are `04_requirement/draft/CA-R-1368@28-draft-CORE_META_MODEL--define-containment-relation-pair.md`, `04_requirement/draft/CA-R-2419@2-draft-CORE_META_MODEL-RELATION_DEFINITION--define-is-contained-by-relation.md`, `04_requirement/draft/CA-R-2244@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-graph-syntax.md`, and the HAS_CLASSIFICATION and Status Group Drafts under `04_requirement/draft/classification-and-status-groups/`. These additions close notation/source ownership; they add no Classification Entity kind. HAS_CLASSIFICATION and IS_CLASSIFIED_BY remain named Relation instances under Graph Syntax, without inventing an inverse pairing. Membership proposals remain outside this closure.

The source repair records, exact path mapping, Current hashes, independent Delta audits and publication dependencies are retained under `/tmp/cce-notation-adoption-20261030/full-review/`. Temporary evidence supports this proposal; it is not an adoption record or a governed Analysis Report. Fresh role-only Drafts retain their unallocated markers. The E459 binding to the replacement Prefix Decision must use its actual allocated canonical ID and receive a fresh check before that target's publication; no placeholder ID is admitted.

The 15 planned Current retirements/reconciliations are R2229, R2275, R1260, R2416, R1243, R1251, R1267, R1262, R1747, R1994, D416, R2414, R2413, D376 and R1352. Each remains conditional on its replacement authority and affected-reference readiness. Exact Current versions/hashes and conditions are in `full-review/retirement-plan.json`; no retirement is performed by this Draft edit.

The selected notation is `/`, `//`, `.`, generic `:`, whole-bearer `X/(.Y: Z)`, Part `+>` Whole / Whole `<+` Part, and Entity `>|` axis / axis `|<` Entity. Relation counts occupy independent written source/forward and target/reverse slots: `Step {1}+>{1+} Workflow` reverses as `Workflow {1+}<+{1} Step`. Property `[format]{cardinality}`, `@` declared Entity references, logical grouping, escaped literals and declared `((RELATION_TYPE))` calls retain their separate meanings. Old `Whole >{n} Part` converts to `Whole {n}<+ Part`. Lowercase carrier-access examples are contextual spellings, not aliases or independently admitted canonical Subjects. The exact old/new source mappings and stale graph-root concerns must remain visible during migration.

Source implementation preparation now includes an approved AST parser and its graph, lookup and validator consumers. It preserves historical grammar profiles and does not alter installed runtime copies. Current native semantic graph admission remains explicitly unavailable; syntax/source graphs do not prove semantic admission. Focused checks and broader filesystem-limited test runs are recorded separately from source review. No Current Atom, archive, allocation counter, Journal, installed runtime or generated publication is changed by this review/repair work.

The generic O127 → O129 → O128 Change Status workflow independently admits model-approved Draft-to-Active transitions. The dedicated O066/ATOM_PROMOTE rule is not a universal prohibition on that separate route. At the prepublication stage, the actual Project MCP binding and valid fresh-marker support required repair. Those repairs now support actual source-stdio MCP execution in an isolated scheduler namespace. Native discovery, sealed request binding and per-target preflight precede each effect. The selected HTTP container is stopped; the old native and Docker scheduler databases remain unchanged. After verified adoption, run the pinned notation migration and normal graph rebuild. The execution checkpoint below records the effects actually observed.

### Migration source-alignment extension — 11 reviewed successors

This bounded review resolves eleven held body rows and D539’s parser-contract observation from existing definitions and the accepted Term/Property and notation decisions. No new Entity kind, Type value, alias, ownership rule or inverse Relation Type is introduced.

Eleven N+1 successors (nine Requirements, two Deliveries) extend the original effective 130 set to 141 RMED source entries. The original manifest and R1284/D657 supplement stay immutable. Existing native publication receipts remain authoritative for completed members; live adoption checkpoints report progress. The two Analysis documents are outside this RMED count.

| Current at preparation | Reviewed Draft | Purpose |
|---|---|---|
| CA-R-1959@11 | [CA-R-1959@12-draft-CORE_META_MODEL-DEFINITION--define-entity-continuant-actor-type-ai-agent](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1959@12-draft-CORE_META_MODEL-DEFINITION--define-entity-continuant-actor-type-ai-agent.md) | Correct the established Actor/AI Agent permission bridge; retain Candidate #6 as labelled history. |
| CA-R-2327@1 | [CA-R-2327@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-cardinality](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2327@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-cardinality.md) | Use existing Cardinality, Format and Relation targets under Graph Syntax. |
| CA-R-2328@1 | [CA-R-2328@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-format](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2328@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-format.md) | Use existing Cardinality, Format and Relation targets under Graph Syntax. |
| CA-R-2329@1 | [CA-R-2329@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-relation](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2329@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-relation.md) | Use existing Cardinality, Format and Relation targets under Graph Syntax. |
| CA-R-2338@1 | [CA-R-2338@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-asset](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2338@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-asset.md) | Use existing Asset, Documentation, Module and Prompt targets under Package. |
| CA-R-2339@1 | [CA-R-2339@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-documentation](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2339@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-documentation.md) | Use existing Asset, Documentation, Module and Prompt targets under Package. |
| CA-R-2340@1 | [CA-R-2340@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-module](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2340@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-module.md) | Use existing Asset, Documentation, Module and Prompt targets under Package. |
| CA-R-2341@1 | [CA-R-2341@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-prompt](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2341@2-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-prompt.md) | Use existing Asset, Documentation, Module and Prompt targets under Package. |
| CA-D-653@14 | [CA-D-653@15-draft-CORE_META_MODEL-ENG_DECISION--deliver-readable-subject-graph-views-as-markdown](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/CA-D-653@15-draft-CORE_META_MODEL-ENG_DECISION--deliver-readable-subject-graph-views-as-markdown.md) | Preserve Content Role as a Property, whole-Atom qualification and the adopted graph-view scope. |
| CA-R-2004@12 | [CA-R-2004@13-draft-CORE_META_MODEL--define-subject-target](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2004@13-draft-CORE_META_MODEL--define-subject-target.md) | Preserve Content Role as a Property, whole-Atom qualification and the adopted graph-view scope. |
| CA-D-539@15 | [CA-D-539@16-draft-ENG_DECISION--bind-strict-graph-request-and-result-contract](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/07_delivery/draft/CA-D-539@16-draft-ENG_DECISION--bind-strict-graph-request-and-result-contract.md) | Align grammar wording/current pins; preserve API defaults, admission and freshness. |

All eleven successors passed independent delta review and were created only at approved Draft paths. No fresh numeric identity or new retirement decision is required. They supersede the ten held token-only spans; those spans must not be applied again. The separately reviewed 152 ready spans in 108 other sources remain frozen.

Publish after the governing original-packet successors with fresh Current bindings. Draft creation does not establish native admission, successful promotion, runtime graph admission or completed migration. D539 retains its graph request’s legacy omission default; its approved profile binds actual Current Versions/paths/hashes. Other entry-point defaults remain separately governed.

[Exact addition overlay](/tmp/cce-notation-adoption-20261030/migration/semantic-alignment/closure-overlay-11.json) · [Actual Draft receipt](/tmp/cce-notation-adoption-20261030/migration/semantic-alignment/actual-draft-receipt.json)

### Definition-ownership hold on seven migration candidates

The subsequent full-source review found an ownership constraint missed by the earlier bounded delta audits: Current R2227 and R2278 require one canonical defining Requirement per Entity. The seven retargeting preparations R2327–R2329 and R2338–R2341 are held from publication. Their corrected targets appear to be owned already by R2243/R2247/R2248 and R2237/R2180/R2177/R2179 respectively. The earlier eleven-file audit receipts record their bounded review; they are not authority to bypass this later finding.

The correction must preserve each existing canonical defining owner, compare the complete Claims and constraints, and reconcile erroneous duplicate definitions and affected references. It must not invent distinct Entities, aliases or a changed Definition Type merely to preserve the seven preparations. A separate corrective supplement will record the verified disposition and effective publication count. An independent ownership crosscheck also covers the original 130-file closure. No member of the eleven-file addition has been published.

### Native adoption checkpoint — 2026-10-30

6 source publications are verified by actual generic Change Status MCP Workflow/Step/Action terminal receipts and exact Current-carrier readback. This is partial execution, not whole-proposal adoption.

| Current Atom | Version / Status | Effect |
|---|---|---|
| CA-R-1931 | 17 / Active | Draft consumed; prior version 16 archived |
| CA-R-1248 | 24 / Active | Draft consumed; prior version 23 archived |
| CA-R-1318 | 30 / Active | Draft consumed; prior version 29 archived |
| CA-R-2453 | 2 / Active | Fresh native allocation; role-only Draft consumed |
| CA-R-2454 | 2 / Active | Fresh native allocation; role-only Draft consumed |
| CA-R-2455 | 2 / Active | Fresh native allocation; role-only Draft consumed |

The original 130-entry closure has 124 entries not yet published, including explicit source-review holds at indices 70 (R1531 ownership), 124 (D398 target) and 127 (R2244 fence layout). The later eleven-file candidate addition has no publication effect; seven of those candidates are held by the later ownership finding. Retirements, broader notation migration and graph rebuild remain pending.

The exact live execution register and per-target native evidence are under `/tmp/cce-notation-adoption-20261030/adoption/root-driver-preparation/`. The failed first IS_PROPERTY_OF attempt was inspected as producing no Current carrier or native effect before the Root explicitly chose a fresh request nonce after the R2228 adapter repair; the failed attempt remains in history. No automatic replay or cross-Atom rollback is authorized by this checkpoint.

The selected HTTP container is stopped. Native task execution uses the isolated source-stdio MCP/worker namespace. Both older scheduler databases remain untouched; their queued work is not resumed. Native semantic graph admission remains unavailable and is not claimed by these source publications.

## TLDR

Propose direct `Entity/Term`, structural `Entity/Property`, Method-owned lexical meanings, IS_PROPERTY_OF with derived HAS_PROPERTY, and the selected compact notation. The full review repairs the original 125-Draft packet and identifies a 130-Draft adoption closure, including ten live-source rebases and M301 → M444. Remaining publication, the 15 conditional retirements, Current notation migration and graph rebuild remain pending actual lifecycle execution; source preparation and tests are not those effects.
