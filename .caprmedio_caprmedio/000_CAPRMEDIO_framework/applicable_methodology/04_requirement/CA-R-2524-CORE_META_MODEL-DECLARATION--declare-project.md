---
atom_id: CA-R-2524
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project
version: 3
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2524-CORE_META_MODEL-DECLARATION--declare-project.md
  source_atom_id: CA-R-2524
  source_atom_revision: 3
  source_sha256: 19bcc51fd4d3b34ac705cd9bad108a17cc816820c95ec4505485c900525151db
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Project

## Claim

### Formal Claim

```CFEL
# model
Scope Unit/Project;

Project >| (Container == yes);

Project ((NARROWER_THAN)) Scope Unit;

# instances
Scope Unit/Project//$scope_unit{:1};

Project//$project {:0}((IS_CONTAINED_BY)) Scope Unit//$scope_unit_2;

Project//$project_2.order.ordered == false;

Project//$project_3.order.number: []{:0};

Project//$project_4.ID: []{:0}
```

### Prose Claim


A Project uses CAPRMEDIO's MODEL.


## Semantics

A Project is the root Scope Unit. The Project is not renamed or moved through Scope Unit operations. It has no Scope Unit ID. The shared model makes it Unordered with no order.number; individual Project Declarations inherit these facts.
