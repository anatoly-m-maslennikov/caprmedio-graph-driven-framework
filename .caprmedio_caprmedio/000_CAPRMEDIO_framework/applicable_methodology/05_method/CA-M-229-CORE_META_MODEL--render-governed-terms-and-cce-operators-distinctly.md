---
subjects:
  governs: "Governed Term Rendering"
  depends_on:
    ["CCE Operator", "General Term", "Governed Term", "Entity/Node/Continuant/Scope Unit.Name", "Author", "Markdown Atom Carrier.Main Content.CCE Operator"]
version: 15
updated_at: "2026-10-19 15:54:41 +0400"
relations:
  relates_to:
    - CA-D-280
    - CA-M-299
atom_id: "CA-M-229"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-229-CORE_META_MODEL--render-governed-terms-and-cce-operators-distinctly.md
  source_atom_id: CA-M-229
  source_atom_revision: 15
  source_sha256: 8ce02a9e35f1a5f854182e8c5f8d0bacb8f9e588c25eed6334038bfb7b7a2533
  original_relations_sha256: 1688c39b708a59bcad7890b4c32f25bce023d273ed253b9cb7eff3c5e5ab7c49
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
