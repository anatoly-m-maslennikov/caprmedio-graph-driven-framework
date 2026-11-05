---
atom_id: CA-E-649
ref_id: CA-E-649
role: Evaluation
form: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-11-02 19:44:26 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
relations:
  evaluation_for:
  - CA-M-191
tier: 5
container:
  scope_unit: CA-SU-15
carrier_destination:
  file:
    name: CA-E-649-PROGRAMMATIC-POLICY--verify-initiative-binding-before-mutation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
# Summary

Verify initiative binding before mutation

## Scope

Every PROGRAMMATIC mutation, including direct Tools, container operations and workflow steps that can change Project or runtime state.

## Claim

A mutation passes only when it carries both a sealed Initiative ID and a stable Action ID, together with its short human-derived summary and any qualified Plan artifact or ephemeral P/session context, before Hook, queue, worker, retry, Git, Journal or reconcile processing. Both IDs are validated before the first effect, propagated unchanged across every handoff, and an Action ID is never reused for another Initiative. A commit parent or implementation detail is not an initiative or action identity.

## Details

- Submit a mutation with both sealed Initiative and stable Action IDs, a human summary and optional Plan or P/session context; verify both IDs before Hook or queue admission and in every operation record.
- Submit a missing, empty, malformed, mutable, mismatched or reused identity and verify rejection before any effect.
- Verify workers, retries, Git, Journal and reconcile handoffs preserve both IDs unchanged.
- Verify a child or batch action cannot reuse an Action ID belonging to another Initiative, and that commit parents, filenames, tool names or scheduler identifiers cannot substitute for either identity.
- Keep this case focused on identity and pre-effect validation; it adds no Journal-history prerequisite or approval gate.
