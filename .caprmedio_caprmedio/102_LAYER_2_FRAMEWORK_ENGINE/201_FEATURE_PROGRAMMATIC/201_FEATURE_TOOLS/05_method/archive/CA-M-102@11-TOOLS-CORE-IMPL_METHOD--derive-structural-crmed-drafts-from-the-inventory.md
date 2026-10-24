---
subjects:
  governs: feature-boundary
  depends_on: []
version: 11
updated_at: 2026-10-24 00:28:02 +0400
relations:
  method_for:
  - CA-R-1072
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-102@11
status: Archived
---
# Derive structural CRMED drafts from the Inventory

consume the exact current Implementation Inventory Projection produced by `CA-M-101` **and** apply the structural-adoption heuristic **to** the selected adoption frontier: a folder containing folders proposes an Area draft, a folder containing files proposes a Feature draft, **and** a language-native module **or** source file fallback proposes a Module draft. preserve ambiguity explicitly **when** the observed structure does **not** support one unambiguous proposal.

produce **only** CRMED drafts **and** their draft relations for operator review; do **not** convert Inventory observations directly into authority. the structural CRMED draft set is the primary adoption result, while the consumed Inventory remains an independently useful Step 1 result.
