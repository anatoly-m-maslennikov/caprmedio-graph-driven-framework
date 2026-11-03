---
atom_id: CA-R-2457
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
version: 3
updated_at: 2026-11-02 00:18:22 +0400
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File/Markdown/Markdown Atom Carrier
  passive:
  - CAPRMEDIO_MODEL <+ Carrier/File/Markdown
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Carrier/File.YAML Frontmatter
  - CAPRMEDIO_MODEL <+ Carrier/File.Main Content
relations: {}
role: Requirement
form: Entity Definition
---
## Summary

Define Markdown Atom Carrier

## Claim scope

Markdown File Carriers that represent Atoms.

## Claim

A Markdown Atom Carrier **means** a Markdown File Carrier that represents an
Atom.

### Formal claim

```text
Carrier/File/Markdown/Markdown Atom Carrier
```

## Semantics

`Carrier/File/Markdown/Markdown Atom Carrier` is an Entity kind. Its
`/` path expresses specialization and inheritance from Markdown File Carrier;
it is not a lexical Term path. For an authoritative Markdown Atom Carrier,
the existing Delivery policy requires YAML Frontmatter followed by Main
Content. Existing Delivery policies govern the representation of an Atom's
Role, Type, Status, and other applicable properties.

The YAML Frontmatter and Main Content are existing logical regions of the File
Carrier, not new per-section Carriers. This definition does not restate their
field definitions, create identifiers or extensions, or define lifecycle
behavior. It does not make YAML Frontmatter mandatory for Markdown File
Carriers that do not represent Atoms.

## Details

This role-only Draft defines one new structural target and allocates no
canonical Requirement identity. It does not automatically introduce a lexical
Term or a Method Term Definition. The inherited File and Markdown kinds remain
separately governed; this Draft does not duplicate their structure.

### Pending parent Definition

- [Markdown File Carrier](CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-markdown-file-carrier.md). This parent Definition is pending, not Current authority.

### Source pins

- [Current CA-R-1957@10 — File Carrier](../CA-R-1957-CORE_META_MODEL-DEFINITION--define-entity-carrier-file-carrier.md), SHA-256 `3bac462c2628e3a5fa9f4d96da41610078c2c99a6f676c782ed425c2b10802f8`.
- [Current CA-R-2269@2 — File regions](../CA-R-2269-CORE_META_MODEL-ENTITY_DEFINITION--define-markdown-and-yaml-regions-in-a-file-carrier.md), SHA-256 `66af3fb6f016f013f4cdeefe945fa4dfcddd9a203c43c5a9febcf5c1b0d1e2f8`.
- [Current CA-D-356@21 — Markdown Atom Carrier structure](../../07_delivery/CA-D-356-CORE_META_MODEL-ENG_DECISION--structure-markdown-atom-carriers.md), SHA-256 `2ab6eef7fbae8cb02c168838b6a377e5b92f6a9547d9504c5e5620304d6fde37`.
- [Current CA-D-478@29 — Atom-property locations](../../07_delivery/CA-D-478-CORE_META_MODEL-ENG_DECISION--store-every-atom-property-in-one-internal-location.md), SHA-256 `7ad522f00eb7af8995c0f97519b74dfd89c90b00defbac0bc20bc2e041c23ec3`.

These sources remain Current and unchanged. This Draft performs no promotion,
retirement, implementation, or runtime change.
