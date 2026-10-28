---
version: 27
updated_at: 2026-10-26 05:59:45 +0400
relations:
  child_of:
  - CA-M-001
  - CA-M-002
  - CA-E-001
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project.Principle Universe
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations'
  - Subject/Graph Node/Domain/Continuant/Actor
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-210@27
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Policy
tier: 1
---
# Evaluate the current Principle and Core set

the Principle **and** Core set Evaluation **must** return `fail` **if** a known Project-wide invariant has no canonical owner, a Principle is **only** a narrow application rather than a broad commitment, a required supporting Core Claim is absent, Claims conflict **or** independently duplicate authority **in** the same context, **or** an Atom has an incompatible Local Tier **or** Content Role; **otherwise**, it **may** return `pass` for the reviewed frontier **without** claiming that undiscovered gaps are impossible. evaluate Principle Content Roles under CA-E-482; the former Actor-policy interpretation of Plan does **not** create an exception **to** current Content Role authority. faithful Core specialization **must not** count as duplicate authority; fixed child counts, a universal RMED checklist per Principle, expansion from Intent, **and** formula/text equivalence **must not** be acceptance conditions. report missing support **and** conflicting owners **to** the Operator **without** silently selecting a winner.
