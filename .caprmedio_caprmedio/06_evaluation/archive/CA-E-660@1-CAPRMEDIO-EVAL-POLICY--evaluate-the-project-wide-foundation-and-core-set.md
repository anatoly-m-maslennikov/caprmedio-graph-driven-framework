---
version: 1
updated_at: 2026-10-29 22:26:56 +0400
relations:
  child_of:
  - CA-M-001
  - CA-M-002
  - CA-E-001
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Governing Objects/Atom.Tier
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - Entity/Object/Continuant/Governing Objects/Atom
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations'
  - Entity/Object/Continuant/Actor
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-660@1
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Eval Policy
tier: 1
---
## Summary

Evaluate the Project-wide foundation and Core set

## Claim

The Project-wide foundation and Core set Evaluation **must** return `fail` **if** a known Project-wide invariant has no canonical owner, a Project-wide foundational commitment is **only** a narrow application rather than a broad commitment, a required supporting Core Claim is absent, Claims conflict **or** independently duplicate authority **in** the same context, **or** an Atom has an incompatible Local Tier **or** Content Role; **otherwise**, it **may** return `pass` for the reviewed frontier **without** claiming that undiscovered gaps are impossible. Evaluate the Content Roles of Project-wide foundational commitments under CA-E-661; the former Actor-policy interpretation of Plan does **not** create an exception **to** current Content Role authority. Faithful Core specialization **must not** count as duplicate authority; fixed child counts, a universal RMED checklist per Project-wide foundational commitment, expansion from Intent, **and** formula/text equivalence **must not** be acceptance conditions. Report missing support **and** conflicting owners **to** the Operator **without** silently selecting a winner.
