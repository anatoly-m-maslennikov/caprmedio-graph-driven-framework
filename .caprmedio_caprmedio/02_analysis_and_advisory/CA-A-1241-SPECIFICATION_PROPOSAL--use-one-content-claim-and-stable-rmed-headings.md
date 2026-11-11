---
atom_id: CA-A-1241
ref_id: CA-A-1241
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Formal Model
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1241-CAPRMEDIO-SPECIFICATION_PROPOSAL--use-one-content-claim-and-stable-rmed-headings.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Use one Content Claim and stable RMED headings

## Decision

The Operator accepted content.claim{1} for every complete RMED Atom. The same property carries a natural-language Claim or one complete fenced formal Claim. Frontmatter atom.claim and atom.formal_claim are superseded as alternate Claim locations. A formal Claim can have optional Claim scope, Semantics and Details; it must never be copied into them.

Use this RMED body skeleton, omitting absent optional sections:

````markdown
# Summary
(summary)

## Claim scope
(claim scope, when needed)

## Claim
(exactly one natural-language Claim, or one complete fenced formal Claim)

## Semantics
(meaning or definition, when useful)

## Details
(supporting details, when useful)
````

Summary and Claim occur exactly once; Claim scope, Semantics and Details occur zero or one time. Claim scope remains conditionally required when the Claim does not cover its whole governed topic/thing and owning context. Drafts may be incomplete. The heading is # Summary, with its value underneath, not a heading made from the Summary value.

## Access convention

Keep atom.content.claim for the Markdown part and atom.version_number for a YAML property. Do not add atom.property, property/text subgroups or colon-based property lookup. Getter functions remain separate proposals in CA-A-1237.

## Draft packet

The following successor Drafts preserve their Current predecessor and Summary while aligning only the affected methodology. No Current source, code or runtime is changed:

- [CA-R-1269@28-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1269@28-draft-CORE_META_MODEL-DEFINITION--define-claim.md)
- [CA-R-2102@10-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2102@10-draft-CORE_META_MODEL-RULE--require-the-base-properties-of-every-current-atom.md)
- [CA-R-2001@12-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2001@12-draft-CORE_META_MODEL--define-atom-content-role-requirement-type-graph-rule.md)
- [CA-R-1465@23-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-1465@23-draft-CORE_META_MODEL--define-summary-as-an-atom-property.md)
- [CA-R-2160@4-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2160@4-draft-CORE_META_MODEL-DEFINITION--define-atom-content-scope.md)
- [CA-D-479@23-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/CA-D-479@23-draft-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md)
- [CA-D-495@21-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/CA-D-495@21-draft-CORE_META_MODEL-ENG_DECISION--carry-applicability-in-the-registered-body-sections.md)
- [CA-D-637@21-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/CA-D-637@21-draft-CORE_META_MODEL-ENG_DECISION--carry-a-formal-graph-rule-as-yaml-with-a-readable-summary.md)
- [CA-M-394@18-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/CA-M-394@18-draft-CORE_META_MODEL--author-one-formal-graph-rule-and-its-readable-summary.md)
- [CA-M-111@42-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/CA-M-111@42-draft-CORE_META_MODEL-IMPLEMENTATION_METHOD--author-one-cce-claim-and-derived-summary.md)
- [CA-E-384@36-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/draft/CA-E-384@36-draft-CORE_META_MODEL-POLICY--validate-composite-claims-and-derived-summaries.md)
- [CA-E-520@24-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/draft/CA-E-520@24-draft-CORE_META_MODEL-POLICY--check-rmed-atom-coherence.md)
- [CA-R-2003@11-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2003@11-draft-CORE_META_MODEL--require-exactly-one-immediate-bearer-for-each-dependent-entity-occurrence.md)
- [CA-R-2149@10-draft](../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-R-2149@10-draft-CORE_META_MODEL--constrain-governing-rmed-relation-targets-by-numeric-tier-and-scope-ancestry.md)

## Boundaries

Current Graph Rule mappings are copied unchanged into their successor Claim blocks; their logic and names are not redefined by this carrier move. Other Content Roles keep their primary-contribution layouts. The new Format branch and ID-format proposal remain separate changes. Existing consumers still need a later implementation/migration task; preparing this packet does not claim they can read the new layout.
