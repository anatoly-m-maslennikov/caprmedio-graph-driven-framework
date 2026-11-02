---
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Carrier/File Carrier.Filename.Scope Unit Token
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Name
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
version: 22
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-D-302@22
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary
Serialize Scope Unit References as Filename Tokens

## Scope
Scope Unit references serialized **in** Atom filenames.

## Claim

**every** Scope Unit reference serialized **in** an Atom filename **must** use **`=1`** stable uppercase token selected from its Scope Unit Name by Project Configuration.

## Details
