---
atom_id: CA-R-2662
ref_id: CA-R-2662
role: Requirement
form: Scope Delegation
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//SKILLS
tier: 3
status: Active
version: 2
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-R-2662-AGENTIC-DEFINES_SCOPE_FOR-SKILLS--declare-skills.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/04_requirement
container:
  scope_unit: CA-SU-22
author: Anatoly Maslennikov
---
## Summary

Declare SKILLS

## Claim

### Prose Claim

The receiving Scope Unit is SKILLS. The additional local Role/Form pairs are:

- Method / Solution;
- Delivery / Solution;
- Requirement / Rule.


The additional admitted HAS_ACTIVE_SUBJECT targets are exactly:

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Retrieval`;


- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Packaging`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Prompt Authoring`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Selection`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Guidance`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Performance <+ Measurement and Profiling`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction <+ Decision`;
- `MODEL//CAPRMEDIO <+ Actor/AI Agent`;
- `MODEL//CAPRMEDIO <+ Carrier`;

Each address selects one endpoint object, not other members of its kind or descendants. An unresolved address is diagnostic and grants no admission. These permissions apply only to local Atoms whose Header.Container resolves to SKILLS. Identity, Parent, responsibility and the Scope Unit tree are unchanged.

### Formal Claim

```CFEL
# instances
Scope Unit//SKILLS.ID == "CA-SU-23";

Scope Unit//SKILLS.Name == "SKILLS";

Scope Unit//SKILLS.Label == "FEATURE";

Scope Unit//SKILLS.order.ordered == false;

Scope Unit//SKILLS ((IS_CONTAINED_BY)) Scope Unit//AGENTIC
```

