---
subjects:
  governs: Entity/Object/Continuant/Term
  depends_on:
  - Entity/Aspect/Engineering/Authoring/Controlled English
  - Entity/Object/Continuant/Term
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Name
  - Entity/Object/Continuant/Actor
  - Entity/Carrier/File.Main Content.CCE Operator
version: 28
updated_at: 2026-10-29 07:45:29 +0400
relations: {}
atom_id: CA-M-229@28
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
## Summary

Render Governed Terms and CCE Operators Distinctly

## Claim scope

CAPRMEDIO content lexical-case rendering.

## Claim

**to** render CAPRMEDIO content, the Author **must** apply the following lexical-case rules:

- start **every** Governed Term with a capital letter.
- start **every** General Term with a lowercase letter.
- preserve the lowercase spelling of **every** ordinary English word at the start of a sentence **or** list item **unless** an active rule requires an exact-case token.
- preserve the required case of canonical Terms, Scope Unit Names, **and** exact registered references, including at sentence **and** list-item starts.
- preserve the canonical spelling of **every** registered CCE Operator. use CA-D-280 for its representation **in** Markdown Atom Carrier Main Content.

## Details
