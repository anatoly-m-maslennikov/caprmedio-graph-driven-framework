---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Carrier/File Carrier
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom.Summary
  - Subject/Graph Relation
version: 22
updated_at: 2026-10-26 05:59:45 +0400
relations:
  delivery_for:
  - CA-R-1598
atom_id: CA-D-478@22
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Eng Decision
---
# Summary

Store every Atom Property in one internal location

## Scope

applicable Atom Properties and their canonical internal locations.

## Claim

**every** applicable Atom Property **must** have **`=1`** canonical internal location assigned by its Delivery authority:

- use YAML Frontmatter **unless** that Property is assigned **to** a named Main Content section.
- use the named section as the sole value source **when** Main Content carries the Property; do **not** maintain the same Property again **in** frontmatter.
- names, filename tokens, **and** placement are representations checked against the internal value under CA-D-480, **not** alternative authority.
- Atom-to-Atom Relations follow their registered owning direction under CA-D-268; do **not** copy inverse **or** transitive Relations **to** make an Atom self-sufficient.
- the retired top-level fields `cce_version`, `cce_form`, **and** `llm_session_ids` are **not** admitted Atom Properties **and** **must not** be serialized **in** an Atom Carrier. their absence is conforming; their presence is a retired-field finding, **not** a reason **to** select legacy authority. this rule does **not** remove session provenance from its separately governed Journal Carrier.

## Details
