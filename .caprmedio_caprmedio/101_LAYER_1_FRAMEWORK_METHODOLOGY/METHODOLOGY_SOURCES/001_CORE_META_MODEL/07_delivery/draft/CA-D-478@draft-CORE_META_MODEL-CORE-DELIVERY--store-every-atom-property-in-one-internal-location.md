---
subjects:
  governs: "Atom.Property"
  depends_on:
    ["Atom.Property", "Markdown Atom Carrier", "Markdown Atom Carrier.YAML Frontmatter", "Atom.Substance", "Atom.Summary", "Relation"]
version: 6
updated_at: "2026-10-15 12:06:24 +0000"
relations: {"delivery_for": ["CA-R-1598"], "relates_to": ["CA-D-479", "CA-D-268", "CA-R-1470"]}
atom_id: "CA-D-478@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
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
