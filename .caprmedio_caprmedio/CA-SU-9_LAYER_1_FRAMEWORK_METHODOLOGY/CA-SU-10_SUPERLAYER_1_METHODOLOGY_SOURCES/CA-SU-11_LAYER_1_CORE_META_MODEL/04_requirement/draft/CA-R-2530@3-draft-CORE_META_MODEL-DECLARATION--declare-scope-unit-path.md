---
atom_id: CA-R-2530
ref_id: CA-R-2530@3-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.Path
tier: 3
status: Draft
version: 3
updated_at: 2026-11-05 03:32:34 +0400
carrier_destination:
  file:
    name: CA-R-2530@3-draft-DECLARATION--declare-scope-unit-path.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare Scope Unit Path

## Claim

### Prose Claim


Each Scope Unit Path is exactly one string. The Project root has Path `/`. For every nonroot Scope Unit, its Path is `/` followed by the exact Scope Unit.Name values for its complete declared immediate-parent chain, in root-to-target order and separated by `/`. The root Project name is not an additional path segment. Build the chain from the Scope Unit Declaration Names and their declared IS_CONTAINED_BY parents; do not substitute Scope Unit IDs, Atom filenames, carrier-folder names, or shorthand aliases. For example, CA-R-2653 declares FRAMEWORK_ENGINE directly under Project//caprmedio, so its Path is `/FRAMEWORK_ENGINE`; CA-R-2648 → CA-R-2649 → CA-R-2650 declare FRAMEWORK_METHODOLOGY → METHODOLOGY_SOURCES → CORE_META_MODEL, so the CORE_META_MODEL Path is `/FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/CORE_META_MODEL`.

### Formal Claim

```CFEL
# model
Scope Unit.Path{::1} :: [string]{::1};

Scope Unit.Path.*[]{::0}
```

