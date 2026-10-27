---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Term
  depends_on:
  - Subject/Graph Node/Engineering/CCE Operator
  - Subject/Graph Node/Domain/Continuant/Term
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Name
  - Subject/Graph Node/Domain/Continuant/Actor
  - Subject/Graph Node/Engineering/Continuant/Carrier/File Carrier.Main Content.CCE Operator
version: 24
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-M-229@24
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
# Summary

Render Governed Terms and CCE Operators Distinctly

## Scope

CAPRMEDIO content lexical-case rendering.

## Claim

**to** render CAPRMEDIO content, the Author **must** apply the following lexical-case rules:

- start **every** Governed Term with a capital letter.
- start **every** General Term with a lowercase letter.
- preserve the lowercase spelling of **every** ordinary English word at the start of a sentence **or** list item **unless** an active rule requires an exact-case token.
- preserve the required case of canonical Terms, Scope Unit Names, **and** exact registered references, including at sentence **and** list-item starts.
- preserve the canonical spelling of **every** registered CCE Operator. use CA-D-280 for its representation **in** Markdown Atom Carrier Main Content.

## Details
