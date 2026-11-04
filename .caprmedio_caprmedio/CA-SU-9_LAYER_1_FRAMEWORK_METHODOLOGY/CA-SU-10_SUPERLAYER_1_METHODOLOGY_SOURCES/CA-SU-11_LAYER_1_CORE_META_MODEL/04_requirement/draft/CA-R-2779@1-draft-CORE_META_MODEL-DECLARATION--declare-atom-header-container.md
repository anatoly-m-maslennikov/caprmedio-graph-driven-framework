---
atom_id: CA-R-2779
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Container
version: 1
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 01:52:14 +0400
carrier_destination:
  file:
    name: CA-R-2779@1-draft-CORE_META_MODEL-DECLARATION--declare-atom-header-container.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Declare Atom.Header.Container

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Container{::1} :: [string]{::1};

Atom.Header.Container.*[]{::0};

# instances
Atom//$atom;
$atom.Header.Container{::1}
```

### Prose Claim

Header.Container identifies the Atom's immediate Container.

Allowed values:

1. A full canonical Scope Unit path.
2. The base Atom ID of the containing Atom.
3. `world`, for a root Project Declaration Atom.

A base Atom ID selects Current by default.

For a root Project Declaration Atom, an omitted Header.Container has the effective default `world`. An explicit valid value overrides that default.

Header.Container is the sole stored Atom-containment value.
