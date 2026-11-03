---
atom_id: CA-M-451
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Term//Entity
  passive:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Entity/Property
  - CAPRMEDIO_MODEL <+ Term
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Method)/(.Type: Term Definition)'
version: 4
updated_at: 2026-11-02 19:46:47 +0400
relations: {}
tier: 1
role: Method
form: Term Definition
---
## Summary

Define Entity

## Claim scope

The reusable lexical Term `Entity` in canonical entity names and authored model statements.

## Claim

Entity **means** the common category for every primary graph node and every dependent property in the framework, as structurally defined by CA-R-2462. This Claim explicitly introduces the lexical Term instance named Entity at `Term//Entity`.

## Semantics

The modeled Entity at Subject `Entity` is defined by an R / Entity Definition. The lexical instance `Term//Entity` is defined by this M / Term Definition. Entity is the sole exception outside the Term branch whose complete canonical name is also one registered Term, because it is the Subject root. Other entities outside that branch require their complete source-admitted expressions; a component Term alone is not their complete canonical name. The exception does not merge the modeled Entity and the lexical Term instance.

The Term Entity is reusable in a name such as `Entity/Property` and in model statements. That lexical composition does not by itself establish specialization, containment, bearer dependence, or another entity identity. The applicable structural Definitions and Relations establish those facts.

## Details

The Operator explicitly confirmed Entity as the sole Subject-root exception with both its structural Entity Definition and its reusable Term Definition. This does not require a new Term Definition for every Entity Definition or every complete entity name. Other complete entity expressions may reuse existing Terms as components. The distinction concerns definition targets; it introduces no general exemption from parentage or naming constraints for roots.

The lexical meaning remains consistent with the structural Entity authority. Current source: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2462-CORE_META_MODEL-DEFINITION--define-entity.md`, CA-R-1248@23, SHA-256 `ace51485e016e84415c0a96cdf1ee23abcb57dfea5882f653aac26ea4fe8b152`. The pending successor preserves that category while extending the explicit root structure. This Method does not replace the structural Requirement, copy its whole specification, or establish a second Entity-kind definition.

This role-only Draft allocates no canonical Method identity and performs no promotion. The Term branch, specialized Method Type and ownership convention remain pending Draft dependencies.

### Pending governing declarations

- [Entity structure](../../04_requirement/draft/CA-R-1248@24-draft-CORE_META_MODEL-DEFINITION--define-entity.md).
- [Term kind and naming distinction](../../04_requirement/draft/CA-R-1318@30-draft-CORE_META_MODEL-DEFINITION--define-term.md).
- [Method Type Term Definition](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-method-type-term-definition.md).
- [Dedicated Method meaning owner](../../04_requirement/draft/CA-R-1319@26-draft-CORE_META_MODEL--define-governed-term.md).

These links identify pending Draft dependencies, not Current admission.
