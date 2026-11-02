---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
version: 19
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-R-1519@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Require conforming Workflow execution

## Scope

Workflow execution.

## Claim

an executor of a Workflow **must** conform **to** the applicable methodology execution rules rather than inventing behavior that is absent from its governing definitions.

## Details

- resolve the Workflow, referenced Actions, Step bindings, declared Step structure, terminal outcomes, **and** applicable execution rules **before** their use. bind definition Revisions **and** revalidate definition changes under CA-R-1525 rather than silently resolving a different Revision during the same Run.
- preserve supplied inputs, returned results, **and** actual Run identities under CA-R-1509, CA-R-1510, **and** CA-R-1511.
- admit work **only** within the applicable authorization, Operator-approval, retry, waiting, **and** recovery conditions. a missing capability **or** unresolved rule blocks the affected execution rather than granting permission. a well-formed definition remains valid **when** a selected executor lacks a required capability; definition validation **and** execution admission are distinct checks.
- a Workflow **may** assume these declared capabilities; it **must not** require a particular executor product merely **to** define its behavior.

this conformance boundary does **not** select a server, programming language, storage technology, **or** a Workflow for building the executor itself.
