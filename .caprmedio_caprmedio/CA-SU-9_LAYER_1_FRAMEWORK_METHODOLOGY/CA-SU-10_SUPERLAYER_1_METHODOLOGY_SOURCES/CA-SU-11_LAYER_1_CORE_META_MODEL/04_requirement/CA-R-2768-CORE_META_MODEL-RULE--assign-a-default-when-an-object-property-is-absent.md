---
atom_id: CA-R-2768
ref_id: CA-R-2768
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Active
version: 2
updated_at: 2026-11-04 20:33:16 +0400
carrier_destination:
  file:
    name: CA-R-2768-RULE--assign-a-default-when-an-object-property-is-absent.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Assign a default when an Object Property is absent

## Claim

### Prose Claim



- `p ?== e1 ?== e2` is one ordered conditional-assignment chain. Keep p when it has an authored value; when p is absent, use the first available valid expression from left to right and set that missing Object Property value in the Model. An authored invalid value is an error, not absence. Omission is Property absence, not null, an empty string, zero or false.

- Expressions may be literals, same-bearer Property paths, explicit bound Property reads, or `LOOKUP(R, q)`. An explicit foreign-bearer read must resolve one target in the declared evaluation context; zero or multiple targets are errors.

- `LOOKUP(R, q)` is an admitted fallback expression; its value and traversal semantics are defined by the Operator//Lookup Declaration.

- Evaluate fallback expressions lazily from left to right; stop at the first valid available value. Later branches are not evaluated. Missing final values, evaluated fallback-expression cycles, and more than one applicable fallback chain are errors. Independent Declaration constraints still apply.

- The conditional assignment sets the missing Object Property value in the Model and the result must satisfy p’s declared value Format and cardinality, including required effective cardinality. It does not itself write a Carrier, persist a file, or create an authored Carrier occurrence; Carrier I/O remains the responsibility of an adapter or Delivery rule. Property-declaration inheritance is unchanged; recursive instance-value lookup occurs only through explicit LOOKUP.
### Formal Claim

```CFEL
# model
p ?== expression
```

## Details

```CFEL
# model
Atom.Header.Label ?== Atom.Header.Form
```
