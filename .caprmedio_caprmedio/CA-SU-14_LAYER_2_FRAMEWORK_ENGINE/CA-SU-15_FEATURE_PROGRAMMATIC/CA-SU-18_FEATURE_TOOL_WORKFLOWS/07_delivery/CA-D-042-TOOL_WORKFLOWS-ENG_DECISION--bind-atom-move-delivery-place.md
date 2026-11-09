---
atom_id: CA-D-042
ref_id: CA-D-042
container:
  scope_unit: CA-SU-18
role: Delivery
form: Eng Decision
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Directory Layout"
tier: 3
relations:
  delivery_for:
  - CA-R-2690
status: Active
version: 24
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-042-TOOL_WORKFLOWS-ENG_DECISION--bind-atom-move-delivery-place.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/07_delivery
claim_target_scope_unit: TOOL_WORKFLOWS
current_scope_unit: TOOL_WORKFLOWS
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
---
# Summary

Bind ATOM_MOVE Delivery place

## Scope

Bind the rebuilt ATOM_MOVE operation's source authority under TOOL_WORKFLOWS while retaining its existing executable Delivery location. This carrier does not establish a new transport or runtime admission.

## Claim

TOOL_WORKFLOWS owns the current ATOM_MOVE contracts flattened into its role directories at `.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/`. The explicit executable binding remains `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/ATOM_MOVE/atom_move.py`; its Delivery directory remains `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/ATOM_MOVE/`.

## Details

- The new FEATURE Delivery root is future/unmaterialized. It does not relocate, copy or reinterpret this existing code binding.
- CA-E-305 supplies the rebuilt operation contract. The authority location is not an independently registered ATOM_MOVE Scope Unit or a derivation rule for the executable path.
- Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.
- Re-pin changed current source locations and Versions before consumption. Existing receipts, historical pins and installed copies retain their original evidence; this source revision neither refreshes nor admits them.
