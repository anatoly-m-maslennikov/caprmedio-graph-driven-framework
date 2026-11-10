---
identity:
  atom_id: CA-E-649
  ref_id: CA-E-649@15
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
      Control/Effect Authorization
  tier: 5
relations:
  evaluation_for:
  - CA-M-191
state:
  status: Archived
  version: 15
  updated_at: 2026-11-09 07:45:14 +0400
destination:
  file:
    name: CA-E-649@15-PROGRAMMATIC-DIRECT_POLICY--verify-initiative-binding-before-mutation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Verify initiative binding before mutation

## Claim

### Prose Claim

A mutation passes only when it carries both a sealed Initiative ID and a stable Action ID, together with its short human-derived summary and any qualified Plan artifact or ephemeral P/session context, before Hook, queue, worker, retry, Git, Journal or reconcile processing. Both IDs are validated before the first effect, propagated unchanged across every handoff, and an Action ID is never reused for another Initiative. A commit parent or implementation detail is not an initiative or action identity.

## Details

### Scope

Every PROGRAMMATIC mutation, including direct Tools, container operations and workflow steps that can change Project or runtime state.

- Submit a mutation with both sealed Initiative and stable Action IDs, a human summary and optional Plan or P/session context; verify both IDs before Hook or queue admission and in every operation record.
- Submit a missing, empty, malformed, mutable, mismatched or reused identity and verify rejection before any effect.
- Verify workers, retries, Git, Journal and reconcile handoffs preserve both IDs unchanged.
- Verify a child or batch action cannot reuse an Action ID belonging to another Initiative, and that commit parents, filenames, tool names or scheduler identifiers cannot substitute for either identity.
- Keep this case focused on identity and pre-effect validation; it adds no Journal-history prerequisite or approval gate.
