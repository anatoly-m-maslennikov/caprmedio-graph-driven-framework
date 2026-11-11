# Scope Unit Declaration adoption

The 44 Scope Unit Declarations and shared model are Current. The live `project_structure.toml` is removed, and Authority and Delivery folders use the adopted naming rules. The retirement task is Done. Overall verification remains Active for the explicit Engine issues below.

## Current model

- 43 non-root units have stable Scope Unit IDs. The root Project has no Scope Unit ID.
- The Project is Unordered and has no `order.number`. Other units retain their declared ordering.
- Non-root Authority folder names include the stable ID. Delivery folder names omit it. Project Authority remains `.caprmedio_<project name>`.
- Applicable Methodology is a special Projection, not a Scope Unit.
- Declarations are the sole structural source. No fallback or generated compatibility TOML is retained.

## Adopted shared Atoms

| Atom | Current source |
| --- | --- |
| CA-A-1313 | [CA-A-1313-SPEC_PROPOSAL--goals-outside-and-scope-contracts-at-tier-zero.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis_and_advisory/020_done/CA-A-1313-SPEC_PROPOSAL--goals-outside-and-scope-contracts-at-tier-zero.md>) |
| CA-R-2516 | [CA-R-2516-CORE_META_MODEL-DECLARATION--declare-atom-role-requirement-form-declaration.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2516-CORE_META_MODEL-DECLARATION--declare-atom-role-requirement-form-declaration.md>) |
| CA-R-2684 | [CA-R-2684-CORE_META_MODEL-RULE--declare-scope-unit-governance.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2684-CORE_META_MODEL-RULE--declare-scope-unit-governance.md>) |
| CA-M-461 | [CA-M-461-CORE_META_MODEL-ENG_POLICY--author-scope-unit-declarations-and-contracts.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-461-CORE_META_MODEL-ENG_POLICY--author-scope-unit-declarations-and-contracts.md>) |
| CA-E-670 | [CA-E-670-CORE_META_MODEL-EVAL_POLICY--check-scope-unit-declarations-goals-and-contracts.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-670-CORE_META_MODEL-EVAL_POLICY--check-scope-unit-declarations-goals-and-contracts.md>) |
| CA-D-666 | [CA-D-666-CORE_META_MODEL-POLICY--carry-scope-unit-declarations-as-governing-atoms.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-666-CORE_META_MODEL-POLICY--carry-scope-unit-declarations-as-governing-atoms.md>) |
| CA-D-667 | [CA-D-667-CORE_META_MODEL-POLICY--derive-scope-unit-authority-and-delivery-folders.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-667-CORE_META_MODEL-POLICY--derive-scope-unit-authority-and-delivery-folders.md>) |
| CA-R-2524 | [CA-R-2524-CORE_META_MODEL-DECLARATION--declare-project.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2524-CORE_META_MODEL-DECLARATION--declare-project.md>) |
| CA-R-2685 | [CA-R-2685-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-ordered.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2685-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-ordered.md>) |
| CA-R-2686 | [CA-R-2686-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-number.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2686-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-number.md>) |
| CA-R-2526 | [CA-R-2526-CORE_META_MODEL-DECLARATION--declare-scope-unit-id.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2526-CORE_META_MODEL-DECLARATION--declare-scope-unit-id.md>) |
| CA-R-2687 | [CA-R-2687-CORE_META_MODEL-DECLARATION--declare-scope-unit-order.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2687-CORE_META_MODEL-DECLARATION--declare-scope-unit-order.md>) |
| CA-R-2688 | [CA-R-2688-CORE_META_MODEL-RULE--establish-scope-units-through-project-structure-declarations.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2688-CORE_META_MODEL-RULE--establish-scope-units-through-project-structure-declarations.md>) |
| CA-D-442 | [CA-D-442-CORE_META_MODEL-ENG_DECISION--encode-scope-unit-declaration-fields.md](</Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-442-CORE_META_MODEL-ENG_DECISION--encode-scope-unit-declaration-fields.md>) |

## Evidence

[44 Current Declarations](instance-drafts.md) · [Adoption results](adoption-results.json) · [Folder moves](folder-migration.md) · [Current source check](current-declaration-check.json).

The earlier preparation reports describe their captured snapshots. Final runtime verification is tracked separately in [P2707](../12-CA-P-2707-TASK--verify-declaration-source-cutover.md). The complete run reported 28 failing modules. Bounded fixture corrections passed focused reruns, and the fresh Docker query/status matrix plus launcher passed. The whole suite is still not claimed green: W10 remains an Engine issue, and the deferred O016 case is one expected failure. [Final verification](verification/final-cutover-verification.json).

[Engine follow-ups](engine-followups.md) records the W10 timestamp/hash and retired D274 authority issues. The unrelated implementation Workflow repair remains in [Engine task P2708](../../001_backlog/CA-P-2708-TASK--align-implementation-workflow-with-current-steps.md). The 26 retained Engine Goal gaps remain deferred.
