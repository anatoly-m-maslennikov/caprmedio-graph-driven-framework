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
