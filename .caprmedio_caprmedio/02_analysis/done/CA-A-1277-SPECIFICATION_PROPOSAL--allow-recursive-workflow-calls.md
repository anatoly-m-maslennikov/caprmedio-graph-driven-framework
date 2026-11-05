---
atom_id: CA-A-1277
ref_id: CA-A-1277
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Operations/Type:
    Workflow'
tier: 3
status: Done
version: 3
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Allow recursive Workflow calls

## Decision

A Workflow may call itself directly, or indirectly through other Workflows. The Workflow-call graph is not required to be acyclic.

Calls remain subject to the accepted Step boundaries: only a leaf Step calls a Workflow, with parameters and input bindings. Substeps call Actions only; a Step containing Substeps makes no call of its own. Referencing a Workflow does not structurally contain or copy its definition.

This decision adds no mandatory recursion-depth limit, termination proof, retry budget or automatic guard. It permits recursive definitions without promising that every possible run terminates.

## State

Workflow and Step Definition Drafts and the Model proposal are updated. Current definitions, concrete Workflows and Engine/runtime behavior are unchanged.
