---
atom_id: CA-M-draft
content_role: Method
type: Eng Decision
current_scope_unit: ADAPTERS
claim_target_scope_unit: ADAPTERS
status: Draft
author: Anatoly Maslennikov
tier: 3
version: 1
updated_at: 2026-10-29 17:52:17 +0400
subjects:
  governs: Entity/Aspect/Text Writing Style
relations: {}
---
## Summary

Normalize Metadata Key Spelling in File Adapters

## Claim scope

Key-name conversion performed by the Markdown file adapter for YAML Frontmatter, with the same convention used by the TOML adapter. The rule applies to keys, not values or readable model names.

## Claim

When the adapter converts a readable field name to a technical key name, lowercase its English letters, replace each space with underscore, then remove every remaining character outside lowercase English letters a through z, digits 0 through 9, and underscore. Require a nonempty result and reject collisions between distinct field names in the same destination mapping or table. Convert each declared nested key separately; do not flatten property paths or normalize their values. Apply this same key-spelling convention in Markdown and TOML adapters.

## Semantics

This is how the adapter writes key names, so it is a Method. It governs the same Text Writing Style Aspect as the readable-model naming Method, with a different Local Scope Unit and Claim Scope. For example, Content Role becomes content_role at this implementation boundary; Content Role remains the model name in Subjects and Formal claims.

Frontmatter is the YAML region of a Markdown Atom Carrier, and Content is its Markdown region. TOML does not acquire those Markdown-specific regions. Adapter logic must still use the admitted field mappings and serialization rules: generating a spelling does not create a field or rename an existing one.

## Details

A-B and AB both normalize to ab: report the collision rather than inventing a suffix or alias. YAML and TOML allow broader key syntax than this project convention. Delivery authority, including CA-D-276 and CA-D-366, continues to declare field placement, encodings, quoting and carrier syntax. This Method adds no schema generator, normalization of values, YAML parser change or live rename.

The registered ADAPTERS Scope Unit currently has no child Scope Unit. The scoped Method therefore uses Eng Decision under the existing Method Type rule; no artificial child is introduced just to call it an Eng Policy. The Claim covers the file adapters without adding Scope Units for each format. This is a Draft only: no adapter code or Current RMED is changed.
