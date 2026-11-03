---
atom_id: CA-R-2279
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_DEFINED_BY
relations: {}
version: 4
updated_at: 2026-11-02 08:06:47 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2279-CORE_META_MODEL-DECLARATION--define-derived-is-defined-by-relation.md
  source_atom_id: CA-R-2279
  source_atom_revision: 4
  source_sha256: afe53bafc767cf429778688cc32228e9772772ac5402700513853ed77cacec63
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Derived IS_DEFINED_BY Relation

## Claim

IS_DEFINED_BY is the derived counterpart of the defining GOVERNS links qualified by the Entity Definition ownership rule. It reuses that main link and its qualification; it adds no independently stored reverse fact.

```CFEL
((IS_DEFINED_BY)) >| Derivation == Derived;
((IS_DEFINED_BY)) ((IS_DERIVED_RELATION_OF)) ((GOVERNS));

$definition_subject ((IS_DEFINED_BY)) Atom//
```

## Semantics



The Host is the Subject of a defining Atom; the link is limited to GOVERNS facts satisfying the Entity Definition ownership rule.
Forward `Host ((IS_DEFINED_BY)) Target` and reverse `Target <((IS_DEFINED_BY)) Host` are views of the same Relation fact.
IS_DEFINED_BY relates Entity Definition subject to qualified defining Atom; not an unconditional inverse of GOVERNS.

## Details

The main GOVERNS meaning is defined by CA-R-1199. CA-R-2278 qualifies which GOVERNS links define an Entity. The counterpart references those sources instead of repeating their meanings or constraints; the inverse is derived only from that qualified main link.
