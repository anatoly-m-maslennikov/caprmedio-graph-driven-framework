---
atom_id: CA-R-3012
ref_id: CA-R-3012@1
role: Requirement
form: Scope Delegation
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FRAMEWORK_DELIVERY
tier: 3
status: archived
version: 1
updated_at: 2026-11-09 15:54:30 +0400
container:
  scope_unit: CA-SU-00
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-2666
destination:
  file:
    name: CA-R-3012@1-caprmedio-DEFINES_SCOPE_FOR-FRAMEWORK_DELIVERY--declare-framework-delivery.md
    path: .caprmedio_caprmedio/04_requirement/099_archived
---

## Summary

Declare FRAMEWORK_DELIVERY

## Claim

### Prose Claim

Project delegates whole-project local and public release to FRAMEWORK_DELIVERY. It owns their Workflow definitions, release-specific Requirements, Methods, Evaluations and Delivery contracts, including recovery and release aftermath. Shared Engine implementation and generic contracts remain separate dependencies. The Project retains its external Goal and wider accountability.

The admitted local Role/Form pairs are exactly:

- Delivery / Decision;
- Evaluation / Eval Case;
- Method / Decision;
- Operations / Action;
- Operations / Step;
- Operations / Workflow;
- Requirement / Rule;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the endpoint objects at these addresses:

- `CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Release.ID`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering`;
- `Subject/CAPRMEDIO/Carrier/Pull Request`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Validation`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Serialization`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Directory Layout`;
- `Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic Testing`;
- `Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record`;
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation`;
- `Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool`;
- `Subject/caprmedio/Action//Aggregate the full Release Gate`;
- `Subject/caprmedio/Action//Finalize actual public Version History link`;
- `Subject/caprmedio/Action//Prepare bound public release materials`;
- `Subject/caprmedio/Action//Run host-capable Candidate E2E`;
- `Subject/caprmedio/Action//Validate local release inputs`;
- `Subject/caprmedio/Step//Finalize the actual public history link`;
- `Subject/caprmedio/Step//Public release/Step: discover matching main PR`;
- `Subject/caprmedio/Step//Public release/Step: prepare materials`;
- `Subject/caprmedio/Step//Public release/Step: push and upsert main PR`;
- `Subject/caprmedio/Step//Release Version/Step: build candidate image`;
- `Subject/caprmedio/Step//Release Version/Step: compile applicable Methodology`;
- `Subject/caprmedio/Step//Release Version/Step: deliver active sources`;
- `Subject/caprmedio/Step//Release Version/Step: install product and refresh Project MCP`;
- `Subject/caprmedio/Step//Release Version/Step: retire exact prior image`;
- `Subject/caprmedio/Step//Release Version/Step: run closed candidate Unit gate`;
- `Subject/caprmedio/Step//Release Version/Step: run host-capable Candidate E2E`;
- `Subject/caprmedio/Step//Release Version/Step: stage candidate package and Skill`;
- `Subject/caprmedio/Step//Release Version/Step: validate local inputs`;
- `Subject/caprmedio/Workflow//Local Release`;
- `Subject/caprmedio/Workflow//Public Release`;

Each address selects one endpoint object, not its descendants or all members of its kind. An unresolved address is diagnostic and grants no admission. These local permissions apply only when Header.Container resolves to FRAMEWORK_DELIVERY. Applicable model defaults remain in force.

### Formal Claim

```CFEL
# instances
Scope Unit//FRAMEWORK_DELIVERY.ID == "CA-SU-27";

Scope Unit//FRAMEWORK_DELIVERY.Name == "FRAMEWORK_DELIVERY";

Scope Unit//FRAMEWORK_DELIVERY.Label == "LAYER";

Scope Unit//FRAMEWORK_DELIVERY.order.ordered == true;

Scope Unit//FRAMEWORK_DELIVERY.order.number == 5;

Scope Unit//FRAMEWORK_DELIVERY ((IS_CONTAINED_BY)) Project//caprmedio
```
