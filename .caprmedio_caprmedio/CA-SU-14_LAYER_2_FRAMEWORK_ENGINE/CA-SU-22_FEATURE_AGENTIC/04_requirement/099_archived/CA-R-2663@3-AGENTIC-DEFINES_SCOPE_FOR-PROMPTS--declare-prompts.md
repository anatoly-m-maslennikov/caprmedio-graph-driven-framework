---
atom_id: CA-R-2663
ref_id: CA-R-2663@3
role: Requirement
form: Scope Delegation
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//PROMPTS
tier: 3
status: archived
version: 3
updated_at: 2026-11-10 20:47:54 +0400
container:
  scope_unit: CA-SU-22
destination:
  file:
    name: CA-R-2663@3-AGENTIC-DEFINES_SCOPE_FOR-PROMPTS--declare-prompts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/04_requirement/099_archived
author: Anatoly Maslennikov
---

## Summary

Declare PROMPTS

## Claim

### Prose Claim

The receiving Scope Unit is PROMPTS. The additional local Role/Form pairs are exactly:

- Method / Solution;
- Requirement / Goal;
- Requirement / Rule;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Prompt Authoring`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Documentation <+ Traceability`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Output Publication`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Failure Handling`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Directory Layout`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Traceability`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Coverage`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Data <+ Golden Corpora`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Design`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction <+ Decision`;
- `MODEL//CAPRMEDIO <+ Execution/Step Run`;

Each address selects one endpoint object, not its descendants or all members of its kind. An unresolved address is diagnostic and grants no admission. These permissions apply only to local Atoms whose Header.Container resolves to PROMPTS. Its existing identity, Name, Label, Parent and responsibility remain unchanged.

### Formal Claim

```CFEL
# instances
Scope Unit//PROMPTS.ID == "CA-SU-24";

Scope Unit//PROMPTS.Name == "PROMPTS";

Scope Unit//PROMPTS.Label == "FEATURE";

Scope Unit//PROMPTS.order.ordered == false;

Scope Unit//PROMPTS ((IS_CONTAINED_BY)) Scope Unit//AGENTIC
```
