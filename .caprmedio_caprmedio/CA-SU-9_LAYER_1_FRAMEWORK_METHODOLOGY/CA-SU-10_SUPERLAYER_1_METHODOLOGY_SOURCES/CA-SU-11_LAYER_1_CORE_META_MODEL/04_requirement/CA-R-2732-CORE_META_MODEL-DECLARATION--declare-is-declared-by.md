---
atom_id: CA-R-2732
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_DECLARED_BY
relations: {}
version: 1
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-2732-CORE_META_MODEL-DECLARATION--declare-is-declared-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare IS_DECLARED_BY

## Claim

### Formal Claim

```CFEL
Relation//IS_DECLARED_BY ((HAS_CLASSIFICATION)) Derivation == Derived;
Relation//IS_DECLARED_BY ((IS_DERIVED_RELATION_OF)) Relation//GOVERNS;
$declared_subject ((IS_DECLARED_BY)) Atom/(.Header.Role: Requirement)/(.Header.Form: Declaration)//
```

### Prose Claim

IS_DECLARED_BY relates a declared model entity or instance to its canonical declaring Atom, qualified by CA-R-2278. The Target has Header.Role Requirement and Header.Form Declaration. Derive this view only when that Atom's GOVERNS link identifies the declared Subject and the declaring ownership qualification is satisfied in the selected effective MODEL. An arbitrary GOVERNS link from another role or form does not produce IS_DECLARED_BY.

The Host is the qualified Declaration's governed Subject; it may be outside the Node branch. The Target is the qualified declaring Atom. This view reuses the existing direct GOVERNS fact and adds no independently stored reverse fact. Its direction reverses the selected, qualified GOVERNS fact; it is not an unconditional HAS_INVERSE binding for GOVERNS.

Forward `Host ((IS_DECLARED_BY)) Target` and reverse `Target <((IS_DECLARED_BY)) Host` are written views of that same derived fact. CA-R-1199 retains the general GOVERNS meaning. CA-R-2278 supplies the declaring ownership qualification; this Declaration retains the qualified endpoint transformation. Neither a derivation reference nor a displayed view grants permission or cardinality.
