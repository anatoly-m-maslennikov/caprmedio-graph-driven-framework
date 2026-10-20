---
subjects:
  governs: "Entity/Node/Continuant/Actor/Type: AI Agent"
  depends_on:
    ["Entity/Node/Continuant/Actor/Type: AI Agent", "Entity/Node/Continuant/Actor/Type: Operator", "Exploration Mode", "Artifact", "Entity/Node/Continuant/Atom.Substance"]
version: 7
updated_at: "2026-10-19 15:53:29 +0400"
relations: {}
atom_id: "CA-R-1558"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1558-CORE_META_MODEL-CORE-REQUIREMENT--route-questions-and-ideas-through-exploration-mode.md
  source_atom_id: CA-R-1558
  source_atom_revision: 7
  source_sha256: 18c8275505daac8d6ab12895d0d6719b6f9143a970b176c814b0bb9fe86f6f7c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Route questions and ideas through Exploration Mode

## Scope

exploratory Operator input and its promotion from Exploration Mode.

## Claim

an AI Agent **must** handle exploratory Operator input **in** Exploration Mode under the following participation policy:

- Exploration Mode permits brainstorming, discussion, research, analysis, comparison, terminology work, **and** structural modeling **without** creating **or** changing governed Artifacts.
- input is exploratory **when** it primarily asks for information, explanation, comparison, critique, alternatives, **or** a recommendation, **or** introduces an idea, explores it, **or** asks for feedback on it.
- an explicit Operator request **to** create **or** change governed state takes precedence over question-shaped wording.
- **otherwise**, Exploration Mode ends **only** **when** the Operator explicitly accepts a conclusion **or** requests its promotion. the AI Agent **must** **then** create **only** the minimum Artifacts required **to** preserve the accepted meaning within the authorized change.
- whether a mode transition is announced is an interaction-reporting choice; it does **not** change this participation policy.

## Details
