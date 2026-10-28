---
atom_id: CA-D-038
content_role: Delivery
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout
  depends_on: []
version: 21
updated_at: 2026-10-27 19:59:22 +0400
relations:
  delivery_for:
  - CA-R-862
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
type: Eng Decision
tier: 3
---
# Summary

Bind ATOM_SEARCH Delivery place

## Scope

Bind the rebuilt ATOM_SEARCH operation's source authority under CONNECTOR_TOOLS while retaining its existing executable Delivery location. This carrier does not establish a new transport or runtime admission.

## Claim

CONNECTOR_TOOLS owns the current ATOM_SEARCH contracts flattened into its role directories at `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS/`. The explicit executable binding remains `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/atom_search.py`; its Delivery directory remains `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/`.

## Details

- The new FEATURE Delivery root is future/unmaterialized. It does not relocate, copy or reinterpret this existing code binding.
- CA-D-424 supplies the rebuilt operation contract. The authority location is not an independently registered ATOM_SEARCH Scope Unit or a derivation rule for the executable path.
- This primitive uses CA-D-625's coherent logical connector interface. The bound caller context supplies the requested scope, source view, permission and applicable validation authority; the connector checks them mechanically. It does not choose Atom identity, Version changes, lifecycle, defaults or a configuration schema.
- Re-pin changed current source locations and Versions before consumption. Existing receipts, historical pins and installed copies retain their original evidence; this source revision neither refreshes nor admits them.
