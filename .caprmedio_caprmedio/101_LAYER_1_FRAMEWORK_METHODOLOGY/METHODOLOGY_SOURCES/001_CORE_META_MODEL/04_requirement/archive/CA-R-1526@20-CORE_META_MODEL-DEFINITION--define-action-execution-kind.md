---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action.Execution Kind'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - Entity/Object/Continuant/Actor/AI Agent
  - Entity/Aspect/Engineering/Execution Control/Effect Authorization
  - Entity/Object/Continuant/Actor/Operator
version: 20
updated_at: 2026-10-29 09:55:37 +0400
relations: {}
atom_id: CA-R-1526@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Entity Definition
tier: 2
---
## Summary

Define Action Execution Kind

## Claim scope

the distinction between execution by code **and** execution requiring AI Agent judgment for an Action's declared responsibility.

## Claim

Action Execution Kind **means** the distinction between execution by code **and** execution requiring AI Agent judgment for an Action's declared responsibility.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action.Execution Kind[string]{1}
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action.Execution Kind: Programmatic
Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action.Execution Kind: Agentic
```

## Details

- Programmatic: code performs the Action according **to** its specified behavior, **without** delegating interpretation **or** judgment **to** an AI Agent. programmatic interaction with the Operator does **not** by itself make the Action Agentic.
- Agentic: an AI Agent interprets the supplied context **and** instructions **to** perform the Action. the AI Agent **may** call Tools within its admitted authority.
- classify an invocation by the responsibility actually delegated, **not** by whether its transport **or** surrounding executor is implemented **in** code. code that delegates the Action's judgment **to** an AI Agent does **not** make that Action Programmatic.
- the distinction does **not** select the Agent's execution context, grant permissions, **or** change the Action's semantic boundary. Tool calls **do not** by themselves create additional Actions **or** Workflow Steps.
