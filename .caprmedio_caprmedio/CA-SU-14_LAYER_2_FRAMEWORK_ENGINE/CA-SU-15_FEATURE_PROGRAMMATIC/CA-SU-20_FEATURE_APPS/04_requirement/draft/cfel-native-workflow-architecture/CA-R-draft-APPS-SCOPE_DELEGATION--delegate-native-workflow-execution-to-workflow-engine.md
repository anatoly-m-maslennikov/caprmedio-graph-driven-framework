---
identity:
  atom_id: CA-R-draft
context:
  container:
    scope_unit: CA-SU-20
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKFLOW_ENGINE
  tier: 3
state:
  status: Draft
  version: 1
  updated_at: 2026-11-11 04:14:10 +0400
destination:
  file:
    name: CA-R-draft-APPS-SCOPE_DELEGATION--delegate-native-workflow-execution-to-workflow-engine.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/draft/cfel-native-workflow-architecture
author: Anatoly Maslennikov
---

## Summary

Delegate native Workflow execution to WORKFLOW_ENGINE

## Claim

### Prose Claim

The proposed receiving Scope Unit WORKFLOW_ENGINE is an unordered APP under APPS. Its responsibility is generic native execution of the adopted executable Workflow language, including Action dispatch, nested Workflow calls, execution position, waiting interactions and actual outcomes. It consumes Core CFEL/Workflow meaning and the installed Action interfaces; it does not redefine either, own Tool business implementations or own MCP transport.

Keep global default Role/Form admissions. The additional local pairs are exactly Requirement / Goal, Requirement / Rule, Requirement / Definition, Method / Solution and Delivery / Solution. Evaluation / Eval Case remains covered by the global default.

The admitted active Subject targets are exactly the declared objects resolved at:

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Data Validation`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Output Publication`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage`.

Each endpoint is exact; an unresolved endpoint grants no permission. Workflow, Step, Action and language-model entities may be consumed as passive contract references. Core methodology retains ownership of their definitions.

### Formal Claim

```CFEL
# instances
Scope Unit//WORKFLOW_ENGINE.Name == "WORKFLOW_ENGINE";
Scope Unit//WORKFLOW_ENGINE.Label == "APP";
Scope Unit//WORKFLOW_ENGINE.order.ordered == false;
Scope Unit//WORKFLOW_ENGINE ((IS_CONTAINED_BY)) Scope Unit//APPS
```

## Details

No new Scope Unit ID is assigned by this Draft. Before Current adoption, allocate a fresh ID, complete the required structural declaration and validate the exact subjects, role permissions and Goal ownership together with the parent delegation candidate. The receiving Scope Unit endpoint is a proposed instance until this resolves; its spelling alone grants no Current permission. Do not reuse retired CA-SU-2 or restore its old implementation. Saving this proposed declaration creates no Current unit or delivery folder.
