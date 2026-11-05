---
atom_id: CA-R-2483
ref_id: CA-R-2483
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE
tier: 3
status: Active
version: 6
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-2483-CORE_META_MODEL-RULE--separate-the-caprmedio-model-from-project-structure.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Separate the CAPRMEDIO model from Project structure

## Claim

### Prose Claim


CAPRMEDIO's PROJECT STRUCTURE has:

- Scope Structure.
- Aspect instances, including Product.
- Other declared components.


Its Scope Structure retains the proposed ordered Units:

1. META_MODEL.
2. ENGINE.
3. CORE EXTENSIONS.
4. DOCUMENTATION.

Its Core Meta-Model Unit contains the Atoms defining MODEL//CAPRMEDIO, including the Declarations for MODEL and PROJECT STRUCTURE. The MODEL and its defining Scope Unit have separate identities.

Each constrained Unit's formal Scope is declared outside that Unit. It states permitted active and passive Subjects, Relations, endpoints and cardinalities.

CAPRMEDIO's PROJECT STRUCTURE records ENGINE's base formal Scope:

- Implementation RMED uses ENGINE's declared implementation Subjects.
- Instance creation follows that Scope's permissions.
- ENGINE references metamodel Declarations only through passive Subjects.
- Active metamodel definitions use the declared model-defining Scope.
- A local MODEL changes ENGINE's Scope only through an explicit Scope-contract replacement.

Declared Unit order governs this Scope Structure.

### Formal Claim

```CFEL
# model
Aspects <+ Product
```

## Details

The two root kinds are MODEL and PROJECT STRUCTURE. Their CAPRMEDIO instance roots are MODEL//CAPRMEDIO and PROJECT STRUCTURE//CAPRMEDIO. A consumer Project has its own PROJECT STRUCTURE instance root and may have a local MODEL instance root.

This Draft does not move directories. Exact instance registration and mapping from existing Scope Units remain adoption work. The earlier PROJECT//CAPRMEDIO Framework wrapper is superseded by the separate typed roots. CAPRMEDIO's actual Unit names are not universal values.

