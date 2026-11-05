---
atom_id: CA-D-039
ref_id: CA-D-039
container:
  scope_unit: CA-SU-17
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout
tier: 3
relations:
  delivery_for:
  - CA-R-2690
status: Active
version: 24
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-039-CONNECTOR_TOOLS-ENG_DECISION--bind-atom-read-delivery-place.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-17_FEATURE_CONNECTOR_TOOLS/07_delivery
claim_target_scope_unit: CONNECTOR_TOOLS
current_scope_unit: CONNECTOR_TOOLS
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
---
# Summary

Bind ATOM_READ Delivery place

## Scope

Bind the rebuilt ATOM_READ operation's source authority under CONNECTOR_TOOLS while retaining its existing executable Delivery location. This carrier does not establish a new transport or runtime admission.

## Claim

CONNECTOR_TOOLS owns the current ATOM_READ contracts flattened into its role directories at `.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-17_FEATURE_CONNECTOR_TOOLS/`. The explicit executable binding remains `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/ATOM_READ/atom_read.py`; its Delivery directory remains `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/ATOM_READ/`.

## Details

- The new FEATURE Delivery root is future/unmaterialized. It does not relocate, copy or reinterpret this existing code binding.
- CA-D-423 supplies the rebuilt operation contract. The authority location is not an independently registered ATOM_READ Scope Unit or a derivation rule for the executable path.
- This primitive uses CA-D-625's coherent logical connector interface. The bound caller context supplies the requested scope, source view, permission and applicable validation authority; the connector checks them mechanically. It does not choose Atom identity, Version changes, lifecycle, defaults or a configuration schema.
- Re-pin changed current source locations and Versions before consumption. Existing receipts, historical pins and installed copies retain their original evidence; this source revision neither refreshes nor admits them.
