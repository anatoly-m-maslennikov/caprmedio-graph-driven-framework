# Review MODEL through the seven Subject projections

Scope corrected at 2026-11-03T15:39:30+04:00, following the Operator's latest instruction: review MODEL, excluding Atom instances and their Properties.

## Scope

Review:

- Declared MODEL entities and their identities.
- Relations, endpoint constraints and classifications.
- Narrowing, inheritance and declared Property contracts: format, allowed values and cardinality.
- Faithfulness and completeness of the MODEL projection.

A Declaration of `Atom.Relations` describes a model Property. A stored `relations` field on a particular Atom is instance data. Only the former belongs to this review. Formulas using instance selectors describe model constraints; this review does not evaluate concrete instances against them. Named Relation declarations remain model vocabulary even when their address uses `Relation//...`.

Source Atom IDs below identify evidence. Their own metadata, values, filenames, lifecycle and carrier serialization are not objects of this audit. Project STRUCTURE instances are also outside the MODEL inventory.

The previous review mixed MODEL findings with instance/carrier migration and source-placement work. Its six-group conclusion and mixed-scope audit totals are superseded by this scope correction.

## Result

SP-01 is resolved by the Operator-authorized mechanical rename to `IS_CONTAINED_BY`. Two MODEL findings (SP-02, SP-03) and two projection findings (SP-04, SP-05) remain. None asserts that a concrete Atom instance is invalid.

| ID | Class | Finding |
| --- | --- | --- |
| SP-01 | Resolved | MODEL Property paths now consistently use the canonical IS_CONTAINED_BY Relation name |
| SP-02 | MODEL identity gap | Retired Entity/Property and old Atom classification vocabulary remain model references |
| SP-03 | MODEL rule conflict | Enabled Relations.Contains and Container classification coexist |
| SP-04 | Projection selection | Existing Scope Unit.order Declaration is omitted |
| SP-05 | Projection scope | STRUCTURE namespace appears in the missing-model-entity audit |

## SP-01 — Resolved: IS_CONTAINED_BY model name

The Operator chose `IS_CONTAINED_BY` throughout MODEL and explicitly authorized the manual in-place patch after the CA route returned incomplete context.

- R2490 declares `Atom.Relations.IS_CONTAINED_BY`.
- R2491 and R2492 declare its `.atom` and `.scope_unit` Properties.
- R2511 and R2520 use the same model paths.
- Three labels in the open model proposal use the canonical name.

The canonical Relation remains `Relation//IS_CONTAINED_BY`, matching R2507's `Relation//` child-name domain. All three Properties retain their original formats and cardinalities and are inherited without extra Declarations. The six edited files contain exactly the approved 20 replacements.

All seven views were rebuilt from a new frontier containing the same 1,132 selected source identities and five refreshed hashes. Their applicable Formal Claims remain verbatim. The original frontier and prior verification receipts were preserved.

[Applied patch and checks](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/02_analysis/draft/subject-projections-20261103/issue-01-is-contained-by/verification.json). Carrier mapping, instance data, runtime and historical sources were excluded.

## SP-02 — Competing model identities

[CA-R-1247@24](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1247-CORE_META_MODEL-RULE--identify-dependent-entity-occurrences-by-complete-subject-path.md:7) and [CA-R-2003@16](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2003-CORE_META_MODEL--require-exactly-one-immediate-bearer-for-each-dependent-entity-occurrence.md:7) still address `Entity/Property`, while [CA-R-2462@2](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2462-CORE_META_MODEL-DECLARATION--declare-node.md:22) establishes the Node/Property model through bearer relations. This presents a retired primary-kind path alongside the accepted dependent-Property model.

[CA-R-924@37](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-924-CORE_META_MODEL-RULE--register-core-relational-atom-classifications.md:7) also refers to `Atom.Type` and old `Atom/Content Role: .../Type: ...` classification paths. The current model Declarations are [CA-R-2494@2](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2494-CORE_META_MODEL-DECLARATION--declare-atom-role.md:21) (`Atom.Role`) and [CA-R-2495@2](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2495-CORE_META_MODEL-DECLARATION--declare-atom-form.md:21) (`Atom.Form`).

Model-level resolution: reconcile these identities and qualifications against the accepted Node, Role and Form declarations. Retired names do not need new Declarations solely to clear audit rows.

The prior counts of hundreds of carrier Subject-field occurrences and recommendations for bulk metadata migration are excluded. They do not measure the number of MODEL defects.

## SP-03 — Competing containment-enabling rules

[CA-R-1990@12](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1990-CORE_META_MODEL-RULE--enable-containment-for-plan-atoms.md:7) and [CA-R-1991@13](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1991-CORE_META_MODEL-RULE--enable-containment-for-workflow-atoms.md:7) retain model rules about `Atom.Enabled Relations.Contains`. [CA-R-2484@2](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2484-CORE_META_MODEL-RULE--admit-container-classification.md:21) establishes `Node >| Container: yes/no` and explicitly replaces that Property representation.

Model-level resolution: reconcile the old containment-enabling rules with the accepted Container classification, preserving any applicable narrower constraint. Review only the rule meanings and declared model vocabulary here.

Concrete instances, consumer migration and staging-language cleanup are excluded.

## SP-04 — Missing selection of an existing model Declaration

[CA-R-2687@1](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2687-CORE_META_MODEL-DECLARATION--declare-scope-unit-order.md:10) declares the model Property `Scope Unit.order`, including its direct-value and child-name constraints. It is absent from the pinned projection selection. [CA-PROJ-025](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/_projection/CA-PROJ-025-CAPRMEDIO--Map--Subjects-without-Requirement-Declarations.md:1237) and [CA-PROJ-026](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/_projection/CA-PROJ-026-CAPRMEDIO--Map--Entity-Definition-and-Active-Subject-Coverage.md:1255) consequently flag absence within that selection.

A canonical Methodology check found it to be the only omitted Current exact Requirement / Declaration carrier in that inventory. This is not a request to create another Declaration.

Projection resolution: include the existing Declaration in the intended MODEL selection and regenerate.

## SP-05 — STRUCTURE leaks into MODEL absence results

[CA-R-2483@6](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2483-CAPRMedio-RULE--separate-the-model-from-project-structure.md:7) addresses the namespace `CAPRMEDIO <+ STRUCTURE`. [CA-PROJ-020](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/_projection/CA-PROJ-020-CAPRMEDIO--Map--Primary-Entities-Tree.md:1211) retains it as namespace context. [CA-PROJ-026](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/_projection/CA-PROJ-026-CAPRMEDIO--Map--Entity-Definition-and-Active-Subject-Coverage.md:1210) instead reports its final endpoint as an undeclared primary Node `STRUCTURE`.

Projection resolution: exclude the STRUCTURE namespace and its concrete project entities from MODEL absence findings. Recognize namespace-only roots before stripping containment prefixes. No MODEL Declaration for a fabricated `STRUCTURE` Node is indicated.

## Withdrawn from this MODEL review

- Concrete Atom field/value validity, including mandatory-field checks on Active Plans.
- Carrier serialization, relation-key mapping in YAML, file locations and filenames.
- Bulk migration of Subjects metadata on Atom instances.
- The former SP-06 source-placement finding: R/Rule versus R/Declaration placement of the one-Declaration ownership rule. That establishes a projection-authority/completeness question, not a MODEL semantic contradiction; it is not retained as a finding in this review.
- Mixed MODEL/instance counts such as passive-only totals, all missing-definition rows and instance-level ownership flags. No MODEL-only defect count is inferred from them.

## Checks and limits

- The abstract Workflow/Step/Substep/Action declarations agree on their permitted execution and containment relations. No concrete Workflow instance was reviewed.
- No duplicate exact selected Property Declarations or inherited format/cardinality collision was confirmed.
- Inherited Property contracts retain their original Declaration provenance.
- Contract extraction remains restricted to Current Requirement / Declaration sources.
- The earlier review checked all seven output hashes against their manifest and all 1,132 selected source hashes. This revision rechecks those same pins; source drift, if present, is recorded separately.

After the scope review, SP-01 was corrected in five MODEL Declarations and the open proposal, and the seven views were rebuilt. Tools, carrier mapping, instance data and historical sources were unchanged. Runtime and instance conformance remain outside scope.
