---
atom_id: CA-R-2456@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
version: 2
updated_at: 2026-10-30 14:16:10 +0400
subjects:
  governs: Entity/Carrier/File/Markdown
  depends_on:
  - Entity/Carrier/File
  - Entity/Carrier/File.Format
relations: {}
---
## Summary

Define Markdown File Carrier

## Claim scope

Markdown File Carriers and their File-Carrier Format.

## Claim

A Markdown File Carrier **means** a File Carrier whose Format is Markdown.

### Formal claim

```text
Entity/Carrier/File/Markdown
```

## Semantics

`Entity/Carrier/File/Markdown` is an Entity kind. Its `/` path expresses
specialization and inheritance from `Entity/Carrier/File`; it is not a lexical
Term hierarchy. Names in the path may reuse lexical Terms. The existing File Carrier definition
supplies inherited File-Carrier structure, while the registered Markdown
Format supplies Markdown encoding and interpretation rules.

YAML Frontmatter is optional for a Markdown File Carrier under the existing
File-region Rule. This definition therefore does not require YAML Frontmatter
for every Markdown file. It does not define a filename, extension, identifier,
section, field, lifecycle, or a separate Carrier for a Markdown region.

## Details

This role-only Draft defines one new structural target and allocates no
canonical Requirement identity. It does not automatically introduce a lexical
Term or a Method Term Definition. The more specific Markdown Atom Carrier kind
is a separate target with separate defining authority.

### Source pins

- [Current CA-R-1957@10 — File Carrier](../CA-R-1957-CORE_META_MODEL-DEFINITION--define-entity-carrier-file-carrier.md), SHA-256 `3bac462c2628e3a5fa9f4d96da41610078c2c99a6f676c782ed425c2b10802f8`.
- [Current CA-R-2346@1 — File Format](../CA-R-2346-CORE_META_MODEL-ENTITY_DEFINITION--define-file-format.md), SHA-256 `0c06778e097a1e61c4f1adfaa74150113c2433fb8ed00d2e046ae206981308b0`.
- [Current CA-R-2269@2 — File regions](../CA-R-2269-CORE_META_MODEL-ENTITY_DEFINITION--define-markdown-and-yaml-regions-in-a-file-carrier.md), SHA-256 `66af3fb6f016f013f4cdeefe945fa4dfcddd9a203c43c5a9febcf5c1b0d1e2f8`.
- [Current CA-D-262@26 — registered File Carrier Formats](../../07_delivery/CA-D-262-CORE_META_MODEL-ENG_DECISION--register-current-file-carrier-formats.md), SHA-256 `a37ec12e408004abf4861a123755aa8f0b332bb0579868907824ba4a025d898d`.

These sources remain Current and unchanged. This Draft performs no promotion,
retirement, implementation, or runtime change.
