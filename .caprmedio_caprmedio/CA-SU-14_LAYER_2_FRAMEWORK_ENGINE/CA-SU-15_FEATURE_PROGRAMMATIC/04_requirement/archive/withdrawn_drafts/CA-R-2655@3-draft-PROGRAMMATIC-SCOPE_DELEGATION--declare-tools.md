---
identity:
  atom_id: CA-R-2655
  ref_id: CA-R-2655@3-draft
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//TOOLS
  tier: 3
state:
  status: Draft
  version: 3
  updated_at: 2026-11-10 17:28:03 +0400
destination:
  file:
    name: CA-R-2655@3-draft-PROGRAMMATIC-SCOPE_DELEGATION--declare-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/draft
---
## Summary

Declare TOOLS

## Claim

### Formal Claim

```CFEL
# instances
PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//TOOLS.ID == "CA-SU-16";

PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//TOOLS.Name == "TOOLS";

PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//TOOLS.Label == "FEATURE";

PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//TOOLS.order.ordered == false;

PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//TOOLS ((IS_CONTAINED_BY)) PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//PROGRAMMATIC
```


### Prose Claim

The explicit default Role/Form pairs below are: `Requirement/Requirement`, `Requirement/Declaration`, `Requirement/Scope Delegation`, `Method/Decision`, `Evaluation/Decision`, `Evaluation/Eval Case`, `Delivery/Decision`, `Operations/Decision`, `Operations/Workflow`, `Operations/Step`, `Operations/Action`. Existing global default admissions, including existing Declaration families, remain unchanged; no additional pairs are granted. No exact Current Solution, Direct Policy, or Approach Policy Role/Form pair is selected. Analysis & Advisory / Code Synopsis remains admitted by the global default, and Plan / Work Report remains admitted only for an already admitted Task with the same Container and within the selected target boundary.

For every admitted local Atom, the Header.Container-derived IS_CONTAINED_BY target must be exactly `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//TOOLS` (`CA-SU-16`). Its HAS_ACTIVE_SUBJECT target is closed to exactly the declared model entities or declared instances resolved at these Current local main Subject addresses:
- `MODEL//CAPRMEDIO <+ Scope Unit`
- `MODEL//CAPRMEDIO <+ Carrier/File`
- `MODEL//CAPRMEDIO <+ Carrier/File.Extension`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Data Transformation`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Data Validation`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Output Publication`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Parsing`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Serialization`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Retrieval`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Selection`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Extension Lifecycle`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Failure Handling`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Directory Layout`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Coverage`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Dynamic Testing`
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Static Analysis`
- `MODEL//CAPRMEDIO <+ Atom.Content`
- `MODEL//CAPRMEDIO <+ Atom.ID`
- `MODEL//CAPRMEDIO <+ Atom.Status`
- `MODEL//CAPRMEDIO <+ Atom.Subjects`
- `MODEL//CAPRMEDIO <+ Atom.Content.Summary`
- `MODEL//CAPRMEDIO <+ Atom.Tier`
- `MODEL//CAPRMEDIO <+ Atom.Type`
- `MODEL//CAPRMEDIO <+ Atom.Version Number`
- `MODEL//CAPRMEDIO <+ Atom/Content Role: Evaluation`
- `MODEL//CAPRMEDIO <+ Atom/Content Role: Plan`
- `MODEL//CAPRMEDIO <+ Event`
- `MODEL//CAPRMEDIO <+ Execution`
- `MODEL//CAPRMEDIO <+ Execution.Outcome`
- `MODEL//CAPRMEDIO <+ Execution/Workflow Run`
- `MODEL//CAPRMEDIO <+ Execution/Workflow Run.Provenance`
- `MODEL//CAPRMEDIO <+ Execution/Workflow Run.Source Admission`
- `MODEL//CAPRMEDIO <+ Governing Configuration`
- `MODEL//CAPRMEDIO <+ Journal`
- `MODEL//CAPRMEDIO <+ Event Record`
- `MODEL//CAPRMEDIO <+ Package/Project Package`
- `MODEL//CAPRMEDIO <+ Implementation/Code/Tool`
- `MODEL//CAPRMEDIO <+ Implementation/Code/Tool.Effect Result`
- `MODEL//CAPRMEDIO <+ Implementation/Code/Tool.Self Description`
- `MODEL//CAPRMEDIO <+ Project`
- `MODEL//CAPRMEDIO <+ Project.Settings`
- `MODEL//CAPRMEDIO <+ Projection`
- `MODEL//CAPRMEDIO <+ Projection/Type: Catalog`
- `MODEL//CAPRMEDIO <+ Scope Unit.Path`
- `MODEL//CAPRMEDIO <+ Selection`
- `Subject/CAPRMEDIO/Graph/Relation`
- `Subject/CAPRMEDIO/Graph/Relation.Target Reference`
- `Subject/CAPRMEDIO/Graph/Relation/Type`
- `Subject/CAPRMEDIO/Graph/Relation/Type: child_of`
- `Subject/CAPRMEDIO/Graph/Relation/Type: structural_parent`
- `Subject/CAPRMEDIO/Graph/Rule`

The selection contains exact objects only, not strings, type members, or descendants; an unresolved address grants no admission.