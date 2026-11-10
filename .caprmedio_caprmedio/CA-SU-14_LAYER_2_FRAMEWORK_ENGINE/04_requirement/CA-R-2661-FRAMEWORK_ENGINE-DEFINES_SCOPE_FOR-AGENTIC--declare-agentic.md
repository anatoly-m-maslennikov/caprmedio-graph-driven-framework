---
atom_id: CA-R-2661
ref_id: CA-R-2661
role: Requirement
form: Scope Delegation
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//AGENTIC
tier: 3
status: Active
version: 2
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-R-2661-FRAMEWORK_ENGINE-DEFINES_SCOPE_FOR-AGENTIC--declare-agentic.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement
container:
  scope_unit: CA-SU-14
current_scope_unit: FRAMEWORK_ENGINE
claim_target_scope_unit: AGENTIC
author: Anatoly Maslennikov
---
## Summary

Declare AGENTIC

## Claim

### Prose Claim

The receiving Scope Unit is AGENTIC. It owns agent-facing methodology-application procedures. The additional local Role/Form pairs are:

- Requirement / Rule;
- Requirement / Goal.

The direct Parent retains its wider responsibility; AGENTIC owns its realization. Its existing identity, Parent and Scope Unit tree are unchanged.


Additional HAS_ACTIVE_SUBJECT permissions for local Atoms in AGENTIC are exactly these endpoint objects:

- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//PROMPTS`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//SKILLS`;


- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Prompt Authoring`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Entry`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Documentation <+ Traceability`;

No descendants or other type members are admitted. An unresolved address grants no admission.

### Formal Claim

```CFEL
# instances
Scope Unit//AGENTIC.ID == "CA-SU-22";

Scope Unit//AGENTIC.Name == "AGENTIC";

Scope Unit//AGENTIC.Label == "FEATURE";

Scope Unit//AGENTIC.order.ordered == false;

Scope Unit//AGENTIC ((IS_CONTAINED_BY)) Scope Unit//FRAMEWORK_ENGINE
```
