---
atom_id: CA-R-1558
ref_id: CA-R-1558
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent.Permissions
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Atom.Content
tier: 1
status: Active
version: 23
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1558-CORE_META_MODEL-RULE--route-questions-and-ideas-through-exploration-mode.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1558-CORE_META_MODEL-RULE--route-questions-and-ideas-through-exploration-mode.md
  source_atom_id: CA-R-1558
  source_atom_revision: 23
  source_sha256: 9dadc3210cf7069327aaf7b68b33ee0dc36075a6b5e945844f62c45ecc005f5f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Route questions and ideas through Exploration Mode

## Claim

### Prose Claim


exploratory Operator input and its promotion from Exploration Mode.


an AI Agent **must** handle exploratory Operator input **in** Exploration Mode under the following participation policy:

- Exploration Mode permits brainstorming, discussion, research, analysis, comparison, terminology work, **and** structural modeling **without** creating **or** changing governed Artifacts.
- input is exploratory **when** it primarily asks for information, explanation, comparison, critique, alternatives, **or** a recommendation, **or** introduces an idea, explores it, **or** asks for feedback on it.
- an explicit Operator request **to** create **or** change governed state takes precedence over question-shaped wording.
- **otherwise**, Exploration Mode ends **only** **when** the Operator explicitly accepts a conclusion **or** requests its promotion. the AI Agent **must** **then** create **only** the minimum Artifacts required **to** preserve the accepted meaning within the authorized change.
- whether a mode transition is announced is an interaction-reporting choice; it does **not** change this participation policy.
