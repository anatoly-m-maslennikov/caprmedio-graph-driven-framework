---
atom_id: CA-P-920@5
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit//CORE_META_MODEL
  - Subject/Domain/Node/Continuant/Atom.Content
  - CA-P-919
  - Local Configuration Atom Normalization
  - Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
version: 5
updated_at: 2026-10-24 19:39:48 +0400
autonomous_confidence_threshold: 99
relations: {}
status: Archived
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Normalize Local Configuration Atoms

**when** CA-P-919 is Done, **then** the Assignee **must** make **every** active Local Configuration Atom **in** Task Scope comply with the normalized Core Meta-Model **and** the complete current authority accepted through CA-P-915.

## Scope

`((all CA-P-917 frontier entries whose owning Scope Unit is LOCAL_CONFIGURATION) union (every replacement or new Local Configuration Atom required solely to resolve a recorded noncompliance))`

## Definition of Done

the Task is **not done if** (**any** in-scope Atom violates a normalized Core invariant **or** **any** Claim, Claim Scope, Claim-Subject relation, Subject Expression, qualified Type **or** Status domain, Term use, CCE form, Summary, filename, frontmatter, H1, revision, **or** archive relation violates current authority **or** Local Configuration redefines a Core Term **or** primitive relation **or** a project choice is promoted into Core authority **or** an unreported active Local Configuration Definition conflict, Term-system violation, **or** cycle in a graph governed as acyclic remains **or** an unresolved conflict is changed, selected, **or** omitted before CA-P-921 **or** Installed Extensions contributes authority **or** **any** repair introduces an unapproved model decision).

## Details

keep Local Configuration responsible for CAPRMEDIO-specific choices, activation, compatibility, replacement, priority, **and** Project-local methodology resolution. preserve **every** valid Core invariant **and** use qualified Subjects rather than creating role-specific Property Terms. pass **every** unresolved conflict unchanged **to** CA-P-921 for deterministic reporting **and** CA-P-922 for Operator disposition.
