---
subject_scopes:
  - feature-boundary
tier: core
version: 1
updated_at: 2026-08-21 00:02:19
relations:
  method_for:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-709--define-adopt-reconcile-tool-unit
---
# Derive structural CRMED drafts from the Inventory

Consume the exact current Implementation Inventory Projection produced by `CA-M-101` and apply the structural-adoption heuristic to the selected adoption frontier: a folder containing folders proposes an Area draft, a folder containing files proposes a Feature draft, and a language-native module or source file fallback proposes a Module draft. Preserve ambiguity explicitly when the observed structure does not support one unambiguous proposal.

Produce only CRMED drafts and their draft relations for operator review; do not convert Inventory observations directly into authority. The structural CRMED draft set is the primary adoption result, while the consumed Inventory remains an independently useful Step 1 result.
