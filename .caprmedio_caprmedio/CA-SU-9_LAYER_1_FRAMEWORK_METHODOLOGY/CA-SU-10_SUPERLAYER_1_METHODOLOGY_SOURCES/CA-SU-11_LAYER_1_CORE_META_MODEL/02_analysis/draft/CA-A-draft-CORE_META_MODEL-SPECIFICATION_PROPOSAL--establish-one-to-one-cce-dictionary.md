---
atom_id: CA-A-draft
container:
  scope_unit: CA-SU-11
role: Analysis
form: Specification Proposal
topics:
  main_subject: Entity/Object/Continuant/Term
tier: 3
status: Draft
version: 1
updated_at: 2026-10-29 14:12:43 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
# Summary

Establish explicit Term Definitions and staged CCE consistency checks

## Question

How were the seventeen-RMED CCE packet and its necessary consumers reconciled with the Current subject system and promoted?

## Scope

Source adoption of the original seventeen-RMED packet in CORE_META_MODEL, including the three previously promoted Methods, plus narrow compatibility updates to optional terminology consumers. This Analysis remains a provisional tracking Draft. Runtime, parser, generated-view publication, project-wide vocabulary migration and complete occurrence review are outside these source effects.

## Approach

Apply the Operator's latest decisions over older Draft text. Verify Current authority from Project Structure, rebase stale candidates without losing adopted metadata or formal constraints, independently review the new Subject bindings and semantic boundaries, allocate fresh identities under the canonical Project lock, archive actual Current predecessors and consume only the fourteen remaining packet Drafts. Record actual source effects independently in the Journal.

## Results

### Accepted model

Each reusable Term has one explicit authoritative R/Term Definition. M explains writing its content; E checks well-formedness and consistent use in stages: entity names, Claim, Claim Scope, Semantics, Details and remaining authored fields. D carries content and review evidence through existing carriers. No dictionary Projection or lookup service is a prerequisite.

Complete canonical entity names retain one-to-one bindings and exact authored usage. `atom.id` and `projection.id` are distinct complete qualified property names using the same ID meaning; their terminal component need not be globally unique. ID means a unique identifier used to find an entity instance across Continuant and Occurrent instances, with uniqueness within matching prefix namespaces. The supplied version/state-qualified identifier examples do not independently establish lifecycle equivalence or a general case-folding rule.

`Package` is reused in `Package`, `Eval Package` and `Runtime Package`; `Unit` in `Scope Unit` and `Code Unit`. The chain `Package > Module > Code Unit` connects three entities without a fourth chain entity. Qualification syntax, explicit definitions and source identity remain separate. Ordinary words, property labels, instance labels and path spelling do not automatically become Project Terms or defining authority.

### New subject system and resolved lexical binding

Current authority uses the `Entity` root with Object, Aspect, Graph Syntax and Carrier branches. References use admitted `/`, `//`, `.`, `:`, `>`, existing-kind `@(...)` and named-relation syntax. The old `Subject/CAPRMEDIO/...` paths and unsupported `::` notation were removed from operative packet references. RMED bodies now use Current CA-D-479@25 sibling headings: Summary, optional Claim scope, Claim, optional Semantics and Details; required formal constraints in existing sources were preserved.

**Q-TERM-TARGET is resolved from Current authority.** CA-R-1318 establishes the Term kind; CA-R-2229 establishes the distinct Term Definition Type; CA-R-1194@29 permits a defining Atom to introduce its target; CA-R-1931@15 and CA-R-2002@15 admit named-instance `K//Name` syntax. Accordingly, the explicit ID Term Definition introduces and governs `Entity/Object/Continuant/Term//ID`. That lexical Term object is distinct from Atom or Projection property entities. Parsing property names does not create it, invent Unit/domain objects or implement a Terms Graph. Existing Term placement is not reclassified.

The Type Draft was merged into existing CA-R-2229, not allocated as a duplicate Type. Entity Definition of the Term kind remains distinct from lexical Term Definition ownership; the former does not silently grant Governed Term status to every word in its text.

### Original seventeen-RMED packet — Current source register

| Role | Current Atom version | Source |
|---|---|---|
| Requirement | CA-R-1318@29 | [CA-R-1318-CORE_META_MODEL-DEFINITION--define-term](../../04_requirement/CA-R-1318-CORE_META_MODEL-DEFINITION--define-term.md) |
| Requirement | CA-R-2229@2 | [CA-R-2229-CORE_META_MODEL-ENTITY_DEFINITION--define-requirement-type-term-definition](../../04_requirement/CA-R-2229-CORE_META_MODEL-ENTITY_DEFINITION--define-requirement-type-term-definition.md) |
| Requirement | CA-R-2275@1 | [CA-R-2275-CORE_META_MODEL-TERM_DEFINITION--define-id](../../04_requirement/CA-R-2275-CORE_META_MODEL-TERM_DEFINITION--define-id.md) |
| Requirement | CA-R-1319@24 | [CA-R-1319-CORE_META_MODEL--define-governed-term](../../04_requirement/CA-R-1319-CORE_META_MODEL--define-governed-term.md) |
| Requirement | CA-R-2276@1 | [CA-R-2276-CORE_META_MODEL-RULE--require-one-to-one-canonical-entity-names-with-reusable-terms](../../04_requirement/CA-R-2276-CORE_META_MODEL-RULE--require-one-to-one-canonical-entity-names-with-reusable-terms.md) |
| Requirement | CA-R-1346@24 | [CA-R-1346-CORE_META_MODEL-RULE--permit-reused-terms-in-qualified-value-domains](../../04_requirement/CA-R-1346-CORE_META_MODEL-RULE--permit-reused-terms-in-qualified-value-domains.md) |
| Requirement | CA-R-1247@22 | [CA-R-1247-CORE_META_MODEL-RULE--identify-dependent-entity-occurrences-by-complete-subject-path](../../04_requirement/CA-R-1247-CORE_META_MODEL-RULE--identify-dependent-entity-occurrences-by-complete-subject-path.md) |
| Requirement | CA-R-1321@31 | [CA-R-1321-CORE_META_MODEL--define-subject-expression](../../04_requirement/CA-R-1321-CORE_META_MODEL--define-subject-expression.md) |
| Requirement | CA-R-1946@14 | [CA-R-1946-CORE_META_MODEL--define-atom-semantics](../../04_requirement/CA-R-1946-CORE_META_MODEL--define-atom-semantics.md) |
| Method | CA-M-113@37 | [CA-M-113-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-claims-in-caprmedio-controlled-english](../../05_method/CA-M-113-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-claims-in-caprmedio-controlled-english.md) |
| Method | CA-M-294@23 | [CA-M-294-CORE_META_MODEL-IMPLEMENTATION_METHOD--use-simpler-words-without-losing-meaning](../../05_method/CA-M-294-CORE_META_MODEL-IMPLEMENTATION_METHOD--use-simpler-words-without-losing-meaning.md) |
| Method | CA-M-439@1 | [CA-M-439-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-term-definition-content](../../05_method/CA-M-439-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-term-definition-content.md) |
| Evaluation | CA-E-444@32 | [CA-E-444-CORE_META_MODEL-EVAL_CASE--validate-project-specific-term-meaning](../../06_evaluation/CA-E-444-CORE_META_MODEL-EVAL_CASE--validate-project-specific-term-meaning.md) |
| Evaluation | CA-E-472@26 | [CA-E-472-CORE_META_MODEL-POLICY--check-simple-wording-without-meaning-loss](../../06_evaluation/CA-E-472-CORE_META_MODEL-POLICY--check-simple-wording-without-meaning-loss.md) |
| Evaluation | CA-E-382@47 | [CA-E-382-CORE_META_MODEL-POLICY--validate-terms-graph](../../06_evaluation/CA-E-382-CORE_META_MODEL-POLICY--validate-terms-graph.md) |
| Evaluation | CA-E-659@1 | [CA-E-659-CORE_META_MODEL-EVAL_CASE--check-term-definition-well-formedness](../../06_evaluation/CA-E-659-CORE_META_MODEL-EVAL_CASE--check-term-definition-well-formedness.md) |
| Delivery | CA-D-655@1 | [CA-D-655-CORE_META_MODEL-POLICY--carry-term-definition-and-staged-review-evidence](../../07_delivery/CA-D-655-CORE_META_MODEL-POLICY--carry-term-definition-and-staged-review-evidence.md) |

All seventeen original RMED entries now resolve to Current Active sources. The fourteen remaining packet Drafts were consumed in this promotion. M113 and M294 received only notation compatibility updates after their earlier promotion; M439 remains at version 1. The original Analysis tracker is not an additional promoted RMED Atom.

### Necessary consumer compatibility

CA-R-1454 and CA-M-114 now select active dedicated Term Definitions for lexical meaning when their optional terminology views are requested. They retain exact source Claim, GOVERNS target, revision, source Relation authority, coverage and fidelity boundaries. These are source contracts only; no optional Projection was generated. M114 inspects named-component coverage but extracts only evidenced reusable Project Terms, preserving instance labels and unresolved classification separately. Current Entity Definition constraints and endpoint authority remain distinct from lexical meaning ownership.

M113 and M294 no longer present unsupported `::` as an admitted operator. This repair preserved the naming policy and other authoring instructions. No Core Method retyping was inferred from the PROGRAMMATIC-only Type restriction; the Delivery evidence contract uses the Current reusable Policy Type.

### Review and effect receipt

Manual source promotion completed at 2026-10-29 14:12:43 +0400. Eighteen source effects comprise the fourteen remaining packet entries plus four focused compatibility updates. Four new canonical identities were allocated; fourteen actual Current predecessors were archived with version-qualified IDs, Archived status, old numeric Version, old Updated At and otherwise preserved content. Every existing successor advanced from its actual Current N to N+1. The canonical identity lock covered fresh-role inventory and publication; Current, retained archives, retained Git filenames and reservations were checked without inventing a counter file.


Two independent review lanes passed all eighteen candidates. Focused findings were repaired before effects: stale syntax coverage, an unsupported legacy Method target fixture, confusing Term-kind definition with dedicated lexical authority, and automatic Term classification of instance names. Source pins, candidate hashes, Current Summaries, role/type metadata, layout and preserved formal cardinalities were checked before mutation. Actual source observations are appended to the Journal independently. This is an Operator-authorized manual source promotion, not a successful Project MCP execution.

### Evidence limits

Source promotion does not prove that all authored content already satisfies the new rules. Missing Term definitions, unknown component segmentation, uncertain entity identity and incomplete population or occurrence coverage remain explicit review outcomes. No global naming inventory, full staged occurrence campaign, runtime behavior, parser compatibility, generated graph or release was validated by this source operation. The promoted Evaluations specify those checks; their presence is not evidence that every check has been executed.

## TLDR

All seventeen RMED entries from the original packet are Current Active sources. The new Subject system supplies the lexical ID binding; explicit Term Definition ownership and staged checks replace the mandatory dictionary proposal. Required source consumers and stale notation were reconciled, with real predecessors archived. Runtime and complete vocabulary/occurrence coverage remain unverified.
