---
atom_id: CA-C-448
ref_id: CA-C-448@3
container:
  scope_unit: CA-SU-15
role: Concern
form: Question
topics:
  main_subject: Legacy GRAPH_UI Delivery Identity Mapping
  dependencies:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Engineering/Carrier
relations:
  concern_about:
  - CA-C-443
  - CA-R-1048
  - CA-R-1432
status: Archived
version: 3
updated_at: 2026-10-23 03:14:50 +0400
carrier_destination:
  file:
    name: CA-C-448@3-PROGRAMMATIC-QUESTION--which-canonical-identity-should-the-legacy-graph-ui-delivery-use.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/01_concern/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
---
# Summary

Which canonical identity should the legacy GRAPH_UI Delivery use?

## Question

Should the valid legacy identity CAPRMEDIO-FRAMEWORK-ENGINE-DELV-005 be explicitly mapped to the next unused project-wide CA-D number, retaining the exact original carrier, its Summary and Claim lineage, and the old-to-new identity binding?

## Evidence

The active carrier is under GRAPH_UI/07_delivery with basename CAPRMEDIO-FRAMEWORK-ENGINE-DELV-005-GRAPH_UI-DELIVERY--deliver-the-requirement-projection-browser-locally.md. It still prescribes .caprmedio/mrt_atoms.html and per-structural-unit STGs. No recorded current canonical identity mapping was found. CA-R-1048 requires approved legacy identity and explicit target mapping; the current sealed Update route preserves assigned CA IDs and does not assign a new identity or recode this valid legacy one. CA-R-1432 prohibits treating a meaning-preserving update as an arbitrary replacement. The Operator was asked this one mapping question on 2026-10-05.

## Disposition

Keep the original carrier unchanged while the mapping is unresolved. Do not reuse its legacy 005 component as a project-wide canonical number, infer an alias, or claim CA-C-443 is fully resolved. After an explicit decision, use the governed sealed migration boundary and preserve original evidence and Journal provenance; no direct carrier-edit bypass is authorized.
