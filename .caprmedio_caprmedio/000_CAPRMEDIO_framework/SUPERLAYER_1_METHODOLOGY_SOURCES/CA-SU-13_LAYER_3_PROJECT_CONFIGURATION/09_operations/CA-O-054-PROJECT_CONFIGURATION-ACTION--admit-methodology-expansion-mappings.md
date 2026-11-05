---
atom_id: CA-O-054
ref_id: CA-O-054
container:
  scope_unit: CA-SU-13
role: Operations
form: Action
topics:
  main_subject: Subject/caprmedio/Action//Admit Methodology Expansion Mapping
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Expansion Boundary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//CORE_META_MODEL
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
tier: 3
status: Active
version: 20
updated_at: 2026-10-27 19:59:45 +0400
carrier_destination:
  file:
    name: CA-O-054-PROJECT_CONFIGURATION-ACTION--admit-methodology-expansion-mappings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
---
# Summary

Admit methodology expansion mappings

## Operation

Admit Methodology Expansion Mapping **means** the reusable Action that returns an admission decision for **`=1`** explicitly described expansion mapping **before** its activation **or** use. its boundary is the mapping's conformance decision, **not** choosing an Extension **or** changing activation Settings.

1. obtain the mapping description under CA-M-298 **before** an Extension **or** Project Configuration relies on the mapped element. preserve its source provenance.
2. evaluate that mapping under CA-E-249 **before** activation **or** reliance **and** **after** a material change **to** its source, target, mapping rule, application scope, **or** governing authority. source provenance does **not** select a different admission procedure.
3. **if** canonical ownership **or** preservation of applicable Core authority remains unresolved, **then** stop the affected application **and** return the evidence **to** the Operator. an Operator approval **must not** turn loss **or** reinterpretation of Core Meta-Model authority at **any** Local Tier into conformance.
4. return the Evaluation result for the exact mapping **and** authority assessed. a failed **or** unresolved mapping **must not** be treated as admitted; a successful mapping check does **not** itself activate a source **or** grant additional authority.

the admission boundary preserves CA-R-1375. CA-R-1207 continues **to** separate expansion rules from current Settings selections.

## Details
