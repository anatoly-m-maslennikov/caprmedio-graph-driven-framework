---
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-006
  - CA-E-001
  evaluation_for:
  - CA-R-2426
  - CA-R-706
  - CA-R-2425
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: CORE_META_MODEL
status: Active
atom_id: CA-E-668
tier: 3
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-668-CORE_META_MODEL-EVAL_POLICY--check-the-selected-scope-against-active-project-wide-invariants.md
  source_atom_id: CA-E-668
  source_atom_revision: 2
  source_sha256: a58622d1f96e2e926da5c3142c793960a4cb83f125aa4247e45841bd4ec3566f
  original_relations_sha256: 2b188f62feb322f2869bf3a79743b4520e1e3d3338b37cbbfe450f1eb7db7b03
---
## Summary

Check the selected Scope against active Project-wide invariants

## Claim

### Prose Claim


For **every** selected Scope, the complete set of active Atoms **must** align with **every** active Project-wide foundational invariant.

## Check

Load the complete active Project-wide foundational invariant set first. Resolve the Scope **and** collect the complete active Atom set, including Methodology source Atoms within the selected Scope. Evaluate **every** Atom against **every** Project-wide foundational invariant **before** applying lower-tier authority.

## Acceptance

Pass **only** **when** **both** of the following hold:

- no Atom conflicts with a Project-wide foundational invariant; **and**
- no lower-tier interpretation weakens **or** overrides a Project-wide foundational invariant.

## Failure

Report **every** conflicting Atom **and** Project-wide foundational invariant pair. Route **every** conflict between active Project-wide foundational invariants **to** the Operator under `CA-R-2425-CORE_META_MODEL-RULE--reserve-project-wide-invariant-conflict-resolution-to-the-operator`.
