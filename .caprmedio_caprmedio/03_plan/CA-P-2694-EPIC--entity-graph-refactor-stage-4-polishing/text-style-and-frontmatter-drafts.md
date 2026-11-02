# Text writing style, carrier terminology and classification Drafts

Latest Operator decisions override the earlier D interpretation: readable model language is M, and key-name conversion in the Markdown/TOML adapter is also M. Both govern Entity/Aspect/Text Writing Style. Local Scope Unit and Claim Scope distinguish their application. Delivery retains existing carrier field mappings and serialization. The mistakenly created D Draft was replaced by the adapter M Draft, not promoted.

CLASSIFIES (::>) and IS_CLASSIFIED_BY (<::) are the approved classification relation names. The direct classified-to-classifier Definition holds the full meaning; the inverse is a short reference. Classification carries inheritance: the classified Entity inherits the applicable features, Properties and constraints of its classification. It is not structural containment. This later Operator clarification supersedes the earlier no-inheritance wording. Status Group distinguishes Draft, Current and Archived from specific Status values.

| Role / Type | Governs | Draft | Status |
| --- | --- | --- | --- |
| Requirement / Entity Definition | Entity/Aspect/Text Writing Style | [define-text-writing-style](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2441-CORE_META_MODEL-ENTITY_DEFINITION--text-writing-style-concerns-how-textual-names-and-statements-are-written-and-represented.md) | Applied as CA-R-2441 |
| Method / Eng Policy | Entity/Aspect/Text Writing Style | [use-readable-model-names](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/05_method/CA-M-445-METHODOLOGY_SOURCES-ENG_POLICY--model-concepts-use-their-readable-names-in-authored-methodology.md) | Applied as CA-M-445 |
| Method / Term Definition | Entity/Term//Frontmatter | [define-frontmatter](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/text-writing-style-and-format/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-frontmatter.md) | Drafted |
| Method / Term Definition | Entity/Term//Content | [define-content](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/text-writing-style-and-format/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-content.md) | Drafted |
| Method / Term Definition | Entity/Term//Property | [define-property](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/text-writing-style-and-format/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-property.md) | Drafted |
| Method / Eng Decision | Entity/Aspect/Text Writing Style | [normalize-metadata-key-spelling-in-file-adapters](../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/007_FEATURE_GROUP_ADAPTERS/05_method/draft/text-writing-style/CA-M-draft-ADAPTERS-ENG_DECISION--normalize-metadata-key-spelling-in-file-adapters.md) | Drafted |
| Requirement / Relation Definition | Entity/Graph Syntax > Relation//IS_CLASSIFIED_BY | [define-is-classified-by-relation](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/classification-and-status-groups/CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-is-classified-by-relation.md) | Drafted |
| Requirement / Relation Definition | Entity/Graph Syntax > Relation//CLASSIFIES | [define-classifies-relation](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/classification-and-status-groups/CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-classifies-relation.md) | Drafted |
| Requirement / Entity Definition | Entity/Object/Continuant/Governing Objects/Atom.Status Group | [define-atom-status-group](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/classification-and-status-groups/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-status-group.md) | Drafted |

No Current Atom, pre-existing Draft, carrier field, projection or runtime code was changed. The nine new Drafts are not promoted. Term Drafts depend on the separate pending Term-root and Method Type migration. The reusable naming Policy uses METHODOLOGY_SOURCES ownership and its actual children; the scoped adapter Method uses ADAPTERS and Eng Decision under the existing leaf rule.

The proposed Object / Aspect / Carrier Subject facets remain a design discussion; no multiple-Governs schema was introduced. Model names remain readable abstractions. YAML and TOML details stay in the scoped adapter Method and existing Delivery encodings.

Verification: nine Drafts parse with one direct Claim each; both naming Methods have the same Subject; Relation Definitions have fenced Notation for subject; only Requirements contain Formal claims. Draft IDs remain unallocated.

## P2703 review update

The preparation claims above are historical context. Two sources are now Current, with established authoring Methods applied; remaining exact dispositions and shared-Draft dependencies are recorded in the [review](deferred-draft-review.md) and [thin register](deferred-draft-dispositions.tsv). The nested Property preparation is withdrawn, the shared classification/Term packet is not promoted here, and Engine adapter realization stays separate.
