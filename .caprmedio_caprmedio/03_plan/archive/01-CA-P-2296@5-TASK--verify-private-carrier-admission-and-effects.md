---
atom_id: CA-P-2296@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Workflow
  - Configuration
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 07:52:46 +0400
relations:
  is_decomposition_of:
  - CA-P-2255
tier: 3
---
# Summary

Verify private carrier admission and effects

## Objective

Bind private carrier mechanics to exact existing admission and source/destination observations. Independently exercise no-overwrite, unsafe paths, symlinks, Atom removal protection, exact cleanup inventory and truthful uncertain effects. Do not enable deferred concurrent publication.

## Details

Estimated own work: 15 minutes. Split larger work into bounded children before execution. Inherit the parent Task's accepted contracts, current-source checks and authority boundaries. Internal helpers are not newly admitted Tools. Keep parsing, reading, writing and CLI responsibilities separate. The integration owner controls Plans and Git; parallel implementation owns disjoint files only.

### Field-only verification checkpoint

The private carrier adapter now preserves the field supplied by a structured admission error, including null; unstructured failures retain the generic message and context field. This does not change admission, enable a carrier write or repair publication concurrency.

The five new isolated tests exercise actual RunTracker and SelectedOperationAdmission mechanisms for preview refusal, permission-reference mismatch, stale authority, a structured null field and a nonstructured diagnostic. The old adapter fails four field assertions; the corrected adapter passes all five. Carrier checks pass 20 tests; the complete connector suite passes 167. Independent review accepted these exact pins after 38 focused tests and eight additional refusal checks; this is not live receiver acceptance.

- Adapter: `connector_carrier_adapter.py`, SHA256 `dc28172f24917f7267896b3fef280ed5bbd44ac4a67e83fece2aa87ec9d9e9ca`.
- Regression: `tests/test_connector_carrier_admission.py`, SHA256 `60e55b3e20cd64291065316e4e65889584e57a618642f4018dde29609426c0c0`.

This Task remains Active. Actual positive receiving admission and effect-boundary safety are not accepted: source substitution immediately before unlink can delete an unapproved Atom and report success; move detects a substituted source only after the effect. Another last-moment check is not a concurrency guarantee. The selected publication model still needs its own accepted binding and proof; no live Core migration is included.

### Definition of Done

The Plan is not Done until exact implementation/source pins, focused positive/refusal/no-op checks and an independent review establish this child's bounded outcome. Preparation alone, invented public bindings, source-policy changes, deferred publication or live Core migration do not satisfy it. Parent-wide and runtime completion remain separate.
