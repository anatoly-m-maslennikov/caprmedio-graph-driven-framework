---
atom_id: CA-M-102
ref_id: CA-M-102
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Decision
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component Structure"
tier: 2
relations:
  method_for:
  - CA-R-1072
status: Active
version: 22
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Derive structural CRMED drafts from the Inventory

consume the exact current Implementation Inventory Projection produced by `CA-M-101` **and** apply the structural-adoption heuristic **to** the selected adoption frontier: a folder containing folders proposes an Area draft, a folder containing files proposes a Feature draft, **and** a language-native module **or** source file fallback proposes a Module draft. preserve ambiguity explicitly **when** the observed structure does **not** support one unambiguous proposal.

produce **only** CRMED drafts **and** their draft relations for operator review; do **not** convert Inventory observations directly into authority. the structural CRMED draft set is the primary adoption result, while the consumed Inventory remains an independently useful Step 1 result.
