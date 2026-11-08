---
identity:
  atom_id: CA-R-2655
  ref_id: CA-R-2655
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//TOOLS
  tier: 3
state:
  status: Active
  version: 2
  updated_at: 2026-11-08 23:18:49 +0400
destination:
  file:
    name: CA-R-2655-PROGRAMMATIC-SCOPE_DELEGATION--declare-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
---
## Summary

Declare TOOLS

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//TOOLS.ID == "CA-SU-16";

Scope Unit//TOOLS.Name == "TOOLS";

Scope Unit//TOOLS.Label == "FEATURE";

Scope Unit//TOOLS.order.ordered == false;

Scope Unit//TOOLS ((IS_CONTAINED_BY)) Scope Unit//PROGRAMMATIC
```


### Prose Claim

The explicit default Role/Form pairs below are: `Requirement/Requirement`, `Requirement/Declaration`, `Requirement/Scope Delegation`, `Method/Decision`, `Evaluation/Decision`, `Evaluation/Eval Case`, `Delivery/Decision`, `Operations/Decision`, `Operations/Workflow`, `Operations/Step`, `Operations/Action`. Existing global default admissions, including existing Declaration families, remain unchanged; no additional pairs are granted. No exact Current Solution, Direct Policy, or Approach Policy Role/Form pair is selected. Implementation / Code Synopsis remains admitted by the global default, and Plan / Work Report remains admitted only for an already admitted Task with the same Container and within the selected target boundary.

For every admitted local Atom, the Header.Container-derived IS_CONTAINED_BY target must be exactly `Scope Unit//TOOLS` (`CA-SU-16`). Its HAS_ACTIVE_SUBJECT target is closed to exactly the declared model entities or declared instances resolved at these Current local main Subject addresses:
- `Scope Unit`
- `Subject/CAPRMEDIO/Carrier/File`
- `Subject/CAPRMEDIO/Carrier/File.Extension`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Transformation`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Output Publication`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Parsing`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery/Extension Lifecycle`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Failure Handling`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Coverage`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing`
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.ID`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Status`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Subjects`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Type`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Version Number`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Event`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Execution`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Execution.Outcome`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Provenance`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run.Source Admission`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Governing Configuration`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool.Effect Result`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool.Self Description`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Project`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Projection`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Catalog`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Path`
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Selection`
- `Subject/CAPRMEDIO/Graph/Relation`
- `Subject/CAPRMEDIO/Graph/Relation.Target Reference`
- `Subject/CAPRMEDIO/Graph/Relation/Type`
- `Subject/CAPRMEDIO/Graph/Relation/Type: child_of`
- `Subject/CAPRMEDIO/Graph/Relation/Type: structural_parent`
- `Subject/CAPRMEDIO/Graph/Rule`

The selection contains exact objects only, not strings, type members, or descendants; an unresolved address grants no admission.