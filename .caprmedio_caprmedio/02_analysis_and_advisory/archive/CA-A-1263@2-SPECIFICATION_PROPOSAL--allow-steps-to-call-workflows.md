---
atom_id: CA-A-1263@2
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 2
updated_at: 2026-10-29 21:51:04 +0400
relations: {}
tier: 3
---
# Summary

Allow Steps to call Workflows

## Decision

A leaf Step calls exactly one Action with parameters or exactly one Workflow with parameters. A Step containing Substeps makes neither kind of call itself. Calling a reusable Workflow is distinct from containing that Workflow definition; the caller contains its Steps, not the called Workflows. No wrapper Action or new invocation entity is introduced.

## Operator example

Update Atom Workflow:
1. Step: call Create Draft Workflow with parameters.
2. Step: call Archive Atom Workflow with parameters.
3. Step: call Promote Draft Workflow with parameters.

These names illustrate the call structure only. No new project-specific Workflow Atom is created by this example. Workflow call-cycle rules are not decided by this increment.

## State

Definition Draft preparation only. Current sources, Workflow instances and Engine implementation are unchanged.
