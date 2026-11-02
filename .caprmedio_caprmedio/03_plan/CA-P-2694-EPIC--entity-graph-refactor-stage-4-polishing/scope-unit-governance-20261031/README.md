# Scope Unit governance amendment

Updated proposal: [A1313 v8 Draft](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/draft/CA-A-1313@8-draft-SPEC_PROPOSAL--goals-outside-and-scope-contracts-at-tier-zero.md). The adopted v7 remains unchanged.

Latest rule: **one Declaration and one or more separate Goals outside; Tier-0 Scope Contract Atoms inside**. Scope Constraints are external and may be part of the Declaration. Goals embedded in a Declaration are superseded.

## Drafts

| Atom | Draft | Status |
| --- | --- | --- |
| CA-A-1313@8-draft | [CA-A-1313@8-draft-SPEC_PROPOSAL--goals-outside-and-scope-contracts-at-tier-zero.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/draft/CA-A-1313@8-draft-SPEC_PROPOSAL--goals-outside-and-scope-contracts-at-tier-zero.md) | Reviewed; questions resolved; adoption pending |
| CA-R-draft | [CA-R-draft-CORE_META_MODEL-DECLARATION--declare-requirement-declaration-form.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/scope-unit-governance-20261031/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-requirement-declaration-form.md) | Reviewed; questions resolved; adoption pending |
| CA-R-draft | [CA-R-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-governance.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/scope-unit-governance-20261031/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-governance.md) | Reviewed; questions resolved; adoption pending |
| CA-M-draft | [CA-M-draft-CORE_META_MODEL-ENG_POLICY--author-scope-unit-declarations-and-contracts.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/scope-unit-governance-20261031/CA-M-draft-CORE_META_MODEL-ENG_POLICY--author-scope-unit-declarations-and-contracts.md) | Reviewed; questions resolved; adoption pending |
| CA-E-draft | [CA-E-draft-CORE_META_MODEL-EVAL_POLICY--check-scope-unit-declarations-goals-and-contracts.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/draft/scope-unit-governance-20261031/CA-E-draft-CORE_META_MODEL-EVAL_POLICY--check-scope-unit-declarations-goals-and-contracts.md) | Reviewed; questions resolved; adoption pending |
| CA-D-draft | [CA-D-draft-CORE_META_MODEL-DECISION--carry-scope-unit-declarations-as-governing-atoms.md](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/scope-unit-governance-20261031/CA-D-draft-CORE_META_MODEL-DECISION--carry-scope-unit-declarations-as-governing-atoms.md) | Reviewed; questions resolved; adoption pending |

## Superseded preparation

Old Scope Definition/Goal-retirement trials and one-Contract alternatives must not be adopted unchanged. They remain historical preparation; this amendment replaces their proposed direction without modifying Current sources. Existing generic structural Scope Unit declarations describe the kind, not one declaration for each actual unit.

## Review order

1. Review against the latest Operator decisions; later messages override earlier ones.
2. Review for coherence and gaps.
3. Fix defects supported by those decisions. Keep unresolved choices explicit; no promotion.

## Review outcome

[Both reviews, fixes and open decisions](review-results.md). Latest-input alignment and coherence reviews are complete. All three Operator choices are resolved; two adoption checks remain; no promotion or Current-source change is claimed.

Project Declaration clarification: **outside the Project, like the Project Goal**. The project-root carrier suggestion is not adopted.

Local Contract minimum resolved: **no minimum; zero or more local Tier-0 Contract Atoms**.

Latest numbering decision: **Scope Units have no Navigation Number; Local Order remains. Navigation Number is retained only for Steps and P Atoms.**

## Fresh review after answers

[Fresh review](fresh-review.md): latest-input alignment passed, and its binding gap is now resolved: the Declaration’s Governs Subject identifies the specific Scope Unit. Exactly one matching Scope Unit Declaration has Role Requirement, Form Scope Unit Declaration and the specific unit as its active Subject. Draft content is unchanged by this review.

Declaration binding resolved: **Governs = the specific Scope Unit**. No new Content Role or duplicate binding field is introduced.

Latest expression mapping: **Role = Requirement; Form = Scope Unit Declaration; subjects.active = the specific Scope Unit instance**. No new Content Role or Atom.Status filter is introduced.

## Adoption preparation

[Concrete adoption steps](adoption-plan.md): the source inventory has 44 non-root rows plus the implicit Project root; the proposed structure retains 43 non-root units and the root after retiring the APPLICABLE_METHODOLOGY hosting Scope Unit. Current governing TOML and runtime remain untouched. The old 13-row Projection is not treated as the authoritative unit inventory.

The later numbering correction supersedes earlier Scope Unit Navigation Number expressions and the associated shared property Draft. See [withdrawn preparation](withdrawn-scope-unit-navigation-number.md).

## Instance Drafts prepared

[Review the 44 retained Declaration Drafts](instance-drafts.md). Their existing Names, Parents, Labels, classifications, nine Local Order values, Carrier places and five explicit authority-mode overrides are preserved. The withdrawn Projection-hosting Scope Unit had the other Local Order value and override. Scope Unit Navigation Number is omitted. [Source checks passed](instance-draft-verification.json); no promotion or runtime acceptance is claimed.

[Goal coverage](goal-coverage.md) records the original source inventory. Among the 44 retained units, 18 have explicit Goal targets and 26 have none observed. No missing Goal is invented. The field map keeps logical Scope Unit.Path distinct from Carrier places. Engine Goal gaps remain with the separate Engine work.

[Three existing-source amendment Drafts](source-amendments.md) cover R1484, D442 and D297. They remove the superseded Scope Unit Navigation Number requirement and prepare the Declaration source change. Their predecessor Summaries are preserved. Remaining TOML-only source rules still require review before complete adoption; this subset is not published as a complete replacement.

The Operator resolved the Methodology-side question: Applicable Methodology is a special Projection. Its separate hosting Scope Unit Declaration Draft is withdrawn, and retirement of that Scope Unit is planned for adoption. [Decision and boundary](applicable-methodology-scope-question.json). Current TOML and delivered Projection files remain unchanged.
