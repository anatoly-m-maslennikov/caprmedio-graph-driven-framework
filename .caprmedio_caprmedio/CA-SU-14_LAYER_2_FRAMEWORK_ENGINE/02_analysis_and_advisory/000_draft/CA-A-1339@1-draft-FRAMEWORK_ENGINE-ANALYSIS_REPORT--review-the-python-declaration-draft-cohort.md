---
identity:
  atom_id: CA-A-1339
  ref_id: CA-A-1339@1-draft
context:
  role: analysis_and_advisory
  form: Analysis Report
  tier: 3
  container:
    scope_unit: CA-SU-14
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution
      Control
state:
  version: 1
  status: draft
  updated_at: '2026-11-12T12:37:45.390236+00:00'
destination:
  file:
    name: CA-A-1339@1-draft-FRAMEWORK_ENGINE-ANALYSIS_REPORT--review-the-python-declaration-draft-cohort.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory/000_draft
---
## Summary

Review the Python declaration draft cohort

## Evidence

Workbench MCP returned all 50 exact Draft references and their Python Formal Claims. The packet includes 24 Property Drafts, 13 Primary Entity Drafts, and 13 Relation Drafts from 47 Current source Atoms. The four Role-qualified Decision Declarations share CA-R-3005 as their source. All 50 Python blocks compiled as Python syntax. The source hashes matched the recorded Current sources.

The three API Drafts are [CA-R-3081@1-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3081@1-draft-CORE_META_MODEL-REQUIREMENT--specify-python-entity-declarations.md), [CA-R-3082@1-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3082@1-draft-CORE_META_MODEL-REQUIREMENT--specify-python-relation-declarations.md), [CA-R-3083@1-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3083@1-draft-CORE_META_MODEL-REQUIREMENT--specify-python-declaration-support.md). The prototypes use proposed module bindings. Runtime compilation through those bindings remains open.

## What to use from Python

1. Use ordinary class bases for narrower Primary Entities. Python's MRO already gives the inheritance order. Use `dataclasses.fields()` to obtain inherited data fields. The Model still resolves accumulated rule constraints and explicit local MODEL overrides using their declaring Atom references.
2. Use type annotations and nested dataclasses for typed fields. Each Property Atom declares its own field once. Materialize the field on its bearer using the standard dataclass machinery. Use `make_dataclass` for nested records generated from Property declarations. Use keyword-only constructors where required and optional inherited fields would otherwise constrain constructor order.
3. Use ordinary `str`, `int`, `bool`, `datetime`, unions and collections for field types. Keep domain constraints such as exact or bounded cardinality, approved Atom ID syntax, and recursive Property rules in declaration metadata. Use `TypedDict` and `NotRequired` where a dictionary interface needs to express key shape and presence.
4. Use Python predicates and built-ins for comparisons, filtering, uniqueness and reduction. Use `ast` for syntax checking and reference discovery, and the existing Markdown parser for fenced Claims and heading structure. Bind reviewed checks to Model data when evaluating them.
5. Keep a Project and its root Project Package as normal classes. Their two Drafts specify an instance population of one per Project. The class constructor remains ordinary Python.

A local standard-library test exercised a nested Atom Header and Context, inherited fields through `class Method(Atom)` and `class Decision(Method)`, and optional nested field typing.

## Adjustments indicated by the drafts

- Keep `declare_entity` and `declare_relation` as the two declaration functions. The binder must register the full Model address, so the four local `Decision` class names remain distinct. Record the four-to-one replacement lineage to CA-R-3005 and adopt those replacements together.
- Separate field presence, direct value count, and dependent Property count. CA-R-2572 has an optional Object Input record with zero direct scalar values and two or three declared children. The Destination File rule CA-R-2716 gives direct dependent fields an inherited string format. Specify immediate selection as the default and require explicit recursive selection. Carry the recursive Content format from CA-R-2498 to separately declared descendants.
- Preserve mixed Markdown in CA-R-2503. Use a nested record that can retain a direct Markdown value and its declared dependent Properties. The existing Markdown parser should preserve the authored heading tree, while only declared headings bind to Model Properties.
- Resolve an omitted occurrence constraint through the effective Model. Specify the remaining fallback separately from value cardinality, especially for nested records and optional scalars.
- Tighten the Relation endpoint contract before adoption. CA-R-2477 targets an applicable classification axis and needs an endpoint selector in place of the unsupported named axis address. CA-R-1993 requires a non-ephemeral target. CA-R-1639, CA-R-2951 and CA-R-3054 need explicit reference encodings for represented-content versions, inverse alias addresses and base Atom IDs. Define the Direct classification for canonical Relation declarations.
- Keep Python class inheritance and CAPRMEDIO rule composition as separate responsibilities. Preserve inherited Relation bounds and permissions, resolve Model and instance whitelists separately, and retain the original declaring Atom for each rule.

## Draft inventory

### Property Drafts

- [CA-R-2502@6-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2502@6-draft-CORE_META_MODEL-DECLARATION--declare-atom-content-semantics.md) from CA-R-2502@5
- [CA-R-2503@6-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2503@6-draft-CORE_META_MODEL-DECLARATION--declare-atom-content-details.md) from CA-R-2503@5
- [CA-R-2527@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2527@3-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-name.md) from CA-R-2527@2
- [CA-R-2528@4-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2528@4-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-label.md) from CA-R-2528@3
- [CA-R-2533@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2533@3-draft-CORE_META_MODEL-DECLARATION--declare-project-settings-name.md) from CA-R-2533@2
- [CA-R-2534@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2534@3-draft-CORE_META_MODEL-DECLARATION--declare-project-settings-prefix.md) from CA-R-2534@2
- [CA-R-2568@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2568@3-draft-CORE_META_MODEL-DECLARATION--declare-event-record-happened-at.md) from CA-R-2568@2
- [CA-R-2569@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2569@3-draft-CORE_META_MODEL-DECLARATION--declare-event-record-inserted-at.md) from CA-R-2569@2
- [CA-R-2572@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2572@3-draft-CORE_META_MODEL-DECLARATION--declare-event-record-object-input.md) from CA-R-2572@2
- [CA-R-2573@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2573@3-draft-CORE_META_MODEL-DECLARATION--declare-event-record-object-input-id.md) from CA-R-2573@2
- [CA-R-2574@4-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2574@4-draft-CORE_META_MODEL-DECLARATION--declare-event-record-object-input-version.md) from CA-R-2574@3
- [CA-R-2575@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2575@3-draft-CORE_META_MODEL-DECLARATION--declare-event-record-object-input-updated-at.md) from CA-R-2575@2
- [CA-R-2576@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2576@3-draft-CORE_META_MODEL-DECLARATION--declare-event-record-object-output.md) from CA-R-2576@2
- [CA-R-2577@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2577@3-draft-CORE_META_MODEL-DECLARATION--declare-event-record-object-output-id.md) from CA-R-2577@2
- [CA-R-2578@4-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2578@4-draft-CORE_META_MODEL-DECLARATION--declare-event-record-object-output-version.md) from CA-R-2578@3
- [CA-R-2579@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2579@3-draft-CORE_META_MODEL-DECLARATION--declare-event-record-object-output-updated-at.md) from CA-R-2579@2
- [CA-R-2685@2-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2685@2-draft-CORE_META_MODEL-DECLARATION--declare-scope-unit-order-ordered.md) from CA-R-2685@1
- [CA-R-2703@2-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2703@2-draft-CORE_META_MODEL-DECLARATION--declare-atom-header-form.md) from CA-R-2703@1
- [CA-R-2704@2-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2704@2-draft-CORE_META_MODEL-DECLARATION--declare-atom-header-version.md) from CA-R-2704@1
- [CA-R-2713@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2713@3-draft-CORE_META_MODEL-DECLARATION--declare-atom-header-subjects.md) from CA-R-2713@2
- [CA-R-2714@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2714@3-draft-CORE_META_MODEL-DECLARATION--declare-atom-header-subjects-active.md) from CA-R-2714@2
- [CA-R-2715@2-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2715@2-draft-CORE_META_MODEL-DECLARATION--declare-atom-header-carrier-destination.md) from CA-R-2715@1
- [CA-R-2716@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2716@3-draft-CORE_META_MODEL-DECLARATION--declare-atom-header-carrier-destination-file.md) from CA-R-2716@2
- [CA-R-2783@2-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2783@2-draft-CORE_META_MODEL-DECLARATION--declare-atom-header-container-atom.md) from CA-R-2783@1

### Primary Entity Drafts

- [CA-R-2463@7-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2463@7-draft-CORE_META_MODEL-DECLARATION--declare-operations.md) from CA-R-2463@6
- [CA-R-2512@7-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2512@7-draft-CORE_META_MODEL-DECLARATION--declare-requirement.md) from CA-R-2512@6
- [CA-R-2513@7-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2513@7-draft-CORE_META_MODEL-DECLARATION--declare-method.md) from CA-R-2513@6
- [CA-R-2514@7-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2514@7-draft-CORE_META_MODEL-DECLARATION--declare-evaluation.md) from CA-R-2514@6
- [CA-R-2515@7-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2515@7-draft-CORE_META_MODEL-DECLARATION--declare-delivery.md) from CA-R-2515@6
- [CA-R-2516@7-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2516@7-draft-CORE_META_MODEL-DECLARATION--declare-atom-role-requirement-form-declaration.md) from CA-R-2516@6
- [CA-R-2737@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2737@3-draft-CORE_META_MODEL-DECLARATION--declare-projection-form-catalog.md) from CA-R-2737@2
- [CA-R-2524@7-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2524@7-draft-CORE_META_MODEL-DECLARATION--declare-project.md) from CA-R-2524@6
- [CA-R-3060@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3060@3-draft-CORE_META_MODEL-DECLARATION--declare-project-package.md) from CA-R-3060@2
- [CA-R-3084@1-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3084@1-draft-CORE_META_MODEL-DECLARATION--declare-method-decision-form.md) from CA-R-3005@3
- [CA-R-3085@1-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3085@1-draft-CORE_META_MODEL-DECLARATION--declare-evaluation-decision-form.md) from CA-R-3005@3
- [CA-R-3086@1-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3086@1-draft-CORE_META_MODEL-DECLARATION--declare-delivery-decision-form.md) from CA-R-3005@3
- [CA-R-3087@1-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3087@1-draft-CORE_META_MODEL-DECLARATION--declare-operations-decision-form.md) from CA-R-3005@3

### Relation Drafts

- [CA-R-1016@34-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-1016@34-draft-CORE_META_MODEL-DECLARATION--register-rationale-for-relation.md) from CA-R-1016@33
- [CA-R-1017@32-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-1017@32-draft-CORE_META_MODEL-DECLARATION--register-method-for-relation.md) from CA-R-1017@31
- [CA-R-1018@39-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-1018@39-draft-CORE_META_MODEL-DECLARATION--register-evaluation-targets.md) from CA-R-1018@38
- [CA-R-1019@31-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-1019@31-draft-CORE_META_MODEL-DECLARATION--register-delivery-for-relation.md) from CA-R-1019@30
- [CA-R-1639@39-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-1639@39-draft-CORE_META_MODEL-DECLARATION--register-derived-from-relation.md) from CA-R-1639@38
- [CA-R-1993@21-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-1993@21-draft-CORE_META_MODEL-DECLARATION--define-carries.md) from CA-R-1993@20
- [CA-R-2473@6-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2473@6-draft-CORE_META_MODEL-DECLARATION--define-property-bearing-and-its-inverse.md) from CA-R-2473@5
- [CA-R-2477@6-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2477@6-draft-CORE_META_MODEL-DECLARATION--define-classification-and-its-written-reverse.md) from CA-R-2477@5
- [CA-R-2951@2-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2951@2-draft-CORE_META_MODEL-RELATION_DECLARATION--declare-is-inverse-alias-for.md) from CA-R-2951@1
- [CA-R-2965@2-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-2965@2-draft-CORE_META_MODEL-RELATION_DECLARATION--declare-is-ordered-right-after.md) from CA-R-2965@1
- [CA-R-3001@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3001@3-draft-CORE_META_MODEL-DECLARATION--declare-contributes-to.md) from CA-R-3001@2
- [CA-R-3054@2-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3054@2-draft-CORE_META_MODEL-RELATION_DECLARATION--declare-is-replacement-for.md) from CA-R-3054@1
- [CA-R-3055@3-draft](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/CA-R-3055@3-draft-CORE_META_MODEL-RELATION_DECLARATION--declare-is-work-report-for.md) from CA-R-3055@2
