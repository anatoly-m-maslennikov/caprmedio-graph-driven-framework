---
cce_version: cce_1
cce_form: method
version: 13
updated_at: 2026-10-24 01:28:26 +0400
relations:
  child_of:
  - CA-M-002
  - CA-M-006
subjects:
  governs: Entity/canonical definition
  depends_on:
  - Entity
  - Property
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-105@13
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Implementation Method
---
# One concept, one definition

**to** represent a kind of information **in** the Project, use **`=1`** canonical Entity, including a Property, for that kind **in** the same context:

1. reuse its existing canonical definition instead of introducing another Entity **or** Property for the same information.
2. treat mappings, explanations, **and** realizations as representations of that definition rather than additional canonical definitions.
3. **if** choosing between competing canonical definitions requires an unresolved decision, **then** stop the affected mapping **or** adaptation **and** return the alternatives **and** their evidence **to** the Operator.
