---
atom_id: CA-E-draft
content_role: Evaluation
form: Eval Policy
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
version: 1
relations: {}
tier: 3
updated_at: 2026-10-31 18:43:05 +0400
---
## Summary

Check Scope Unit Declarations, Goals and Contracts

## Claim

Identify Scope Unit Declaration Atoms by Role Requirement, Form Scope Unit Declaration and active Subject (`subjects.active`) naming the specific Scope Unit. Count exactly one matching Declaration for each unit; do not count other requirements about that unit as Declarations. Check the selected sources for alignment with the governing Scope Unit Declaration: one external Declaration for each declared Scope Unit; one or more separate Goals outside that Scope Unit; and Scope Contract Atoms owned inside it at Tier 0, using RMEDO roles as applicable. Other local Atoms may occupy higher Tiers. Do not report a missing local Contract as a violation: no minimum count is required. Check that no additional per-unit Definition Atom is required and that a Scope Constraint, when carried by the Declaration, is external to the governed Scope Unit and that links do not duplicate Goal content.

Check that the Project Declaration is outside the Project, like the Project Goal, with the same external Operator ownership. Do not infer a carrier path from this ownership decision. Check that Scope Units have no Navigation Number and that their existing Local Order semantics are retained. Navigation Number is retained only for Steps and P Atoms; no additional numbering rule is introduced here. Do not invent an owner, minimum Contract count, number format or other undeclared rule. Report source alignment, adoption, carrier conformance, and runtime behavior separately; this Draft records no result.
