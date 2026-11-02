---
atom_id: CA-R-2483
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: PROJECT STRUCTURE//CAPRMEDIO
version: 4
updated_at: 2026-11-02 18:21:51 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Separate the CAPRMEDIO model from Project structure

## Claim

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

## Details

The two root kinds are MODEL and PROJECT STRUCTURE. Their CAPRMEDIO instance roots are MODEL//CAPRMEDIO and PROJECT STRUCTURE//CAPRMEDIO. A consumer Project has its own PROJECT STRUCTURE instance root and may have a local MODEL instance root.

This Draft does not move directories. Exact instance registration and mapping from existing Scope Units remain adoption work. The earlier PROJECT//CAPRMEDIO Framework wrapper is superseded by the separate typed roots. CAPRMEDIO's actual Unit names are not universal values.

