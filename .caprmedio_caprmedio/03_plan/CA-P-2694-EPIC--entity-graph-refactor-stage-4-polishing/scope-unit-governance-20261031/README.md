# Scope Unit Declaration Draft package

The package contains **44 formal instance Drafts**, **43 non-root Scope Unit IDs**, and shared model/Carrier Drafts. No Current source, governing TOML, runtime or physical folder has been changed by this conversion.

[Review the 44 instance Drafts](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/scope-unit-governance-20261031/instance-drafts.md>). The Project root has no Scope Unit ID. Applicable Methodology is a special Projection; its separate Scope Unit Draft is withdrawn.

## Latest model

- ID, Name and optional Label describe each non-root unit; IDs remain stable through moves and renames.
- Ordering uses Boolean `order.ordered` and sibling `order.number`, required only when ordered is true.
- The shared Project model sets Unordered, no order.number and no Scope Unit ID. The instance inherits these facts.
- Scope Unit Parent is a direct `IS_CONTAINED_BY` fact. The Project root has no parent.
- Authority and Delivery paths are derived. Only non-root Authority names include the ID prefix.
- Project Authority is `.caprmedio_<project name>`, without an ID.
- One external Declaration and 1+ separate external Goals; optional internal Tier-0 Scope Contracts.

## Shared Drafts

| Atom | Draft | Status |
| --- | --- | --- |
| CA-A-1313@9-draft | [CA-A-1313@9-draft-SPEC_PROPOSAL--goals-outside-and-scope-contracts-at-tier-zero.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/draft/CA-A-1313@9-draft-SPEC_PROPOSAL--goals-outside-and-scope-contracts-at-tier-zero.md>) | Prepared; review pending |
| CA-R-draft | [CA-R-draft-CORE_META_MODEL-DECLARATION--declare-requirement-declaration-form.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/scope-unit-governance-20261031/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-requirement-declaration-form.md>) | Prepared; review pending |
| CA-R-draft | [CA-R-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-governance.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/scope-unit-governance-20261031/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-governance.md>) | Prepared; review pending |
| CA-M-draft | [CA-M-draft-CORE_META_MODEL-ENG_POLICY--author-scope-unit-declarations-and-contracts.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/05_method/draft/scope-unit-governance-20261031/CA-M-draft-CORE_META_MODEL-ENG_POLICY--author-scope-unit-declarations-and-contracts.md>) | Prepared; review pending |
| CA-E-draft | [CA-E-draft-CORE_META_MODEL-EVAL_POLICY--check-scope-unit-declarations-goals-and-contracts.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/06_evaluation/draft/scope-unit-governance-20261031/CA-E-draft-CORE_META_MODEL-EVAL_POLICY--check-scope-unit-declarations-goals-and-contracts.md>) | Prepared; review pending |
| CA-D-draft | [CA-D-draft-CORE_META_MODEL-DECISION--carry-scope-unit-declarations-as-governing-atoms.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/scope-unit-governance-20261031/CA-D-draft-CORE_META_MODEL-DECISION--carry-scope-unit-declarations-as-governing-atoms.md>) | Prepared; review pending |
| CA-D-draft | [CA-D-draft-CORE_META_MODEL-POLICY--derive-scope-unit-authority-and-delivery-folders.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/draft/scope-unit-governance-20261031/CA-D-draft-CORE_META_MODEL-POLICY--derive-scope-unit-authority-and-delivery-folders.md>) | Prepared; review pending |
| CA-R-2524@3-draft | [CA-R-2524@3-draft-CORE_META_MODEL-DECLARATION--declare-project.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/scope-unit-governance-20261031/CA-R-2524@3-draft-CORE_META_MODEL-DECLARATION--declare-project.md>) | Prepared; review pending |
| CA-R-draft | [CA-R-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-ordered.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/scope-unit-governance-20261031/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-ordered.md>) | Prepared; review pending |
| CA-R-draft | [CA-R-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-number.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/scope-unit-governance-20261031/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-number.md>) | Prepared; review pending |
| CA-R-2526@3-draft | [CA-R-2526@3-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-id.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/scope-unit-governance-20261031/CA-R-2526@3-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-id.md>) | Prepared; review pending |

## Review and adoption

[Field mapping](field-mapping.md) · [Formal conversion](formal-instance-conversion.json) · [Folder derivation](folder-derivation.json) · [Source amendments](source-amendments.md) · [Adoption plan](adoption-plan.md).

The five obsolete authority-mode overrides are retired by Operator decision. Older validation reports describe earlier snapshots; this updated package needs fresh review. The 26 retained Goal gaps are Engine-side, outside this Methodology adoption.

The `order` group has no direct value. Its children are `order.ordered` (one Boolean value) and `order.number` (one positive integer when Ordered, no value otherwise). [Grouping Declaration](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/scope-unit-governance-20261031/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-order.md>).
