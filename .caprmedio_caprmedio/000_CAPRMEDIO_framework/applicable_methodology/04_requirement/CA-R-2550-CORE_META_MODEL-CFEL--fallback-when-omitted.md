---
atom_id: CA-R-2550
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2550-CORE_META_MODEL-CFEL--fallback-when-omitted.md
  source_atom_id: CA-R-2550
  source_atom_revision: 2
  source_sha256: 96e82be4b859658326c1d2c248615d2e9bc7d8acf7dfa2599ad9d82c9d60f860
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Resolve a fallback when an optional Property is omitted

## Claim

### Formal Claim

```CFEL
# model
p ?= expression
```

### Prose Claim



- `p ?= e1 ?= e2` is one ordered fallback chain. Use p when authored; otherwise use the first available valid expression from left to right. An authored invalid value is an error, not absence. Omission is Property absence, not null, an empty string, zero or false.

- Expressions may be literals, same-bearer Property paths, explicit bound Property reads, or `LOOKUP(R, q)`. An explicit foreign-bearer read must resolve one target in the declared evaluation context; zero or multiple targets are errors.

- `LOOKUP(R, q)` starts from p’s bearer, follows one existing outgoing R link at each step, and returns the nearest compatible authored q value. The starting bearer is excluded. A known end with no applicable authored value returns absence, allowing the next fallback.

- Resolve q by full Property declaration identity and applicability in the effective MODEL. Skip a bearer only when q is inapplicable or its authored occurrence is absent. Do not match unrelated Properties by bare name or invent a slot on an inapplicable kind.

- An invalid present value, unresolved applicability or graph facts, multiple outgoing targets, or a revisited bearer is an error. Follow only the relation direction named by R.

- Lookup is lazy: stop at the first valid available value. Later branches are not evaluated. Missing final values and evaluated fallback-expression cycles are errors. More than one applicable fallback chain is an error. Independent Declaration constraints still apply.

- Resolve the effective value without writing a Carrier or adding an authored occurrence. It must satisfy p’s declared value Format and cardinality. A fallback cannot satisfy a required authored occurrence. Property-declaration inheritance is unchanged; recursive instance-value lookup occurs only through explicit LOOKUP.
## Details

```CFEL
# model
Atom.Header.Label ?= Atom.Header.Form
```
