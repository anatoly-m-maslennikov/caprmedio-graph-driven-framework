---
atom_id: CA-A-1321
version: 1
status: Draft
role: Analysis
form: Specification Proposal
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
updated_at: 2026-11-05 06:06:44 +0400
carrier_destination:
  file:
    name: CA-A-1321@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--unify-declarative-cfel-paths-and-instance-formats.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft
---
## Summary

Unify declarative CFEL paths and instance Formats

## Proposal

CFEL is declarative: Claims state participants, scope, constraints and required values; they do not perform I/O or business actions. A Formal Claim is self-contained. `subjects.active` remains the declared focus and is not an implicit operand or binding.

- `X//Y` selects a narrower kind with inheritance; `Whole/Part` expresses immediate containment. The coordinated source and consumer migration is not yet adopted.
- `<Kind>` identifies a Model kind used as an object Format. `$x[<Kind>, (conditions)]` selects a named participant, and `$<Kind>` an anonymous instance; selection creates nothing.
- `$x[<KindA> OR <KindB>]` binds one participant drawn from either kind; a following count applies to the combined selection. Kind alternatives remain Formats, not new graph Nodes.
- `VALUES(p)` selects the actual direct Property value occurrences, preserving duplicates without traversing nested Properties or treating constraints as stored values. CA-R-2904@1-draft declares this construct.
- `FOR EACH $x[<Kind>, (conditions)]: ( ... )` expresses universal quantification. The body contains semicolon-separated expressions; no `WITH` or `IN` header keyword is used. Existing bounded IF binding and no-shadowing remain.
- Formal Claims use `# model` before `# instances` when both groups occur. `=` tests a condition, `==` states a required or derived value, and `?==` supplies a default under its own rule.
- HAS_ALLOWED_VALUE (`:=`, CA-R-2826) supplies allowed literal alternatives; applicable local and inherited alternatives combine by OR. HAS_VALUE_CONSTRAINT (`::`, CA-R-2828) supplies applicable local and inherited constraints combined by AND. Final admissibility is the allowed-value OR group AND the constraint AND group. When no allowed-value group exists, omit it (true): there is no enumeration restriction. Qualified Subjects retain `:=`.
- The staged CA-R-2827@1 and CA-R-2829@1 pure-inverse Declarations are superseded for coordinated withdrawal; their Draft files remain until migration and are not proposed for adoption. Literal values remain values, not newly invented Nodes.
- An inverse alias is a phantom reverse-view name of its canonical Relation, not a literal or a separate Alias kind. Fixed Model Relation references require no `$` binding: `Relation//CONTAINS ((IS_INVERSE_ALIAS_FOR)) Relation//IS_CONTAINED_BY;`. `IS_INVERSE_ALIAS_FOR` is declared in staged Draft CA-R-2951@1.
- Atom Header storage concerns the Atom itself: outgoing Relation facts default to `Atom.Header.Relations`, while `IS_CONTAINED_BY` is stored only in `Atom.Header.Container`. This Atom schema rule does not add storage Properties to Relation.
- CFEL has no modeled Operator descriptor catalog in this proposal. Actor Operator and AI Agent remain distinct Actor kinds.

## Rationale

One declarative notation separates value admission, value constraints and required results while retaining source identity and inherited meaning. Model kinds, instances and Relation facts remain distinct.

## Staged Draft cohort

The following **51 actual Draft Atoms** are the pinned language and value-Relation cohort. They are staged evidence, not Current authority or implementation.

### Value and arithmetic Rules

CA-R-2904@1, CA-R-1346@29, CA-R-2794@1, CA-R-2795@1, CA-R-2796@1, CA-R-2797@1, CA-R-2798@1, CA-R-2799@1, CA-R-2800@1, CA-R-2801@1

### Path and binding Rules

CA-R-2248@6, CA-R-2802@1, CA-R-2803@1, CA-R-2804@1, CA-R-2805@1, CA-R-2806@1, CA-R-2807@1, CA-R-2808@1, CA-R-2809@1, CA-R-2811@1, CA-R-2812@1, CA-R-2778@1

### Control and expression Rules

CA-R-2813@1, CA-R-2814@1, CA-R-2815@1, CA-R-2816@1, CA-R-2817@1, CA-R-2818@1, CA-R-2819@1, CA-R-2820@1, CA-R-2821@1

### Consumers

CA-E-383@47, CA-E-402@34, CA-E-403@37, CA-E-449@46, CA-M-228@38, CA-M-237@34, CA-R-1358@36, CA-R-1359@31, CA-R-1405@30, CA-R-1456@40, CA-R-2487@15, CA-R-2552@5, CA-R-2618@4, CA-R-2768@3

### Model Declarations

CA-R-2247@12, CA-R-2462@5

### Value Relations

CA-R-2826@1, CA-R-2827@1, CA-R-2828@1, CA-R-2829@1

## Staged inverse-alias Drafts

CA-R-2951@1 declares IS_INVERSE_ALIAS_FOR. Canonical Relation Drafts CA-R-2478@6, CA-R-2762@3, and CA-R-2766@3 adopt the inverse-alias approach; CA-R-2817@1 and CA-R-2247@12 are rebased grammar Drafts. These six Drafts do not constitute a complete canonical Relation inventory and are not Current authority.

## Integration boundary

The predecessor allowed-value `::` Rule Draft CA-R-2810 was withdrawn and preserved as evidence; do not recreate it. Complete and review the CFEL source cohort first, including the pending candidate 55-authority review manifest; this is not Current authority or proof of complete language coverage. Then migrate applicable Current and Draft sources in place mechanically, preserving their content and identity under the reviewed migration. After that source migration, hand off implementation, adapters, data conversion, fixtures and tests to CA #3. Preserve Current grammar until coordinated adoption. Rebuild affected MODEL projections after source acceptance.
