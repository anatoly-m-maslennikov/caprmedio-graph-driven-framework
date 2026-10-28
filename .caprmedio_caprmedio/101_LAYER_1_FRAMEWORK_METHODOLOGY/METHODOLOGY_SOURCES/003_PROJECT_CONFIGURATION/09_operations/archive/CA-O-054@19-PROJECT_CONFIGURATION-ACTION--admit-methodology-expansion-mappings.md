---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Admit Methodology Expansion Mapping'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Expansion Boundary
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Product/Extension
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Graph Node/Domain/Continuant/Scope Unit//CORE_META_MODEL
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
version: 19
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-O-054@19
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Action
tier: 3
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
