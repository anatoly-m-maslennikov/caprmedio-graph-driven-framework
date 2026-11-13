---
atom_id: CA-R-2523
ref_id: CA-R-2523
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: active
version: 4
updated_at: 2026-11-05 12:58:42 +0400
carrier_destination:
  file:
    name: CA-R-2523-CORE_META_MODEL-DECLARATION--declare-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---


## Summary

Declare Scope Unit

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Continuant

class ScopeUnit(Continuant):
    pass

declare_entity(entity_class=ScopeUnit, entity_name="Scope Unit", classifications={"Container": "yes"})
```

```CFEL
# instances
Scope Unit//$scope_unit {::0+}((CONTAINS)) Atom//$atom;

Scope Unit//$scope_unit{::0..1}((IS_CONTAINED_BY)) Scope Unit//$scope_unit_2;

Scope Unit//$scope_unit_3{::0+}((CONTAINS)) Scope Unit//$scope_unit_4;

Scope Unit//$unit;

IF (($unit not in (Scope Unit/Project//$scope_unit_5)) AND ($unit.ID != "CA-SU--1"))
THEN ($unit {==1}((IS_CONTAINED_BY)) Scope Unit//$scope_unit_6);
```

## Semantics

A Scope Unit defines a boundary of responsibility for Atoms.
