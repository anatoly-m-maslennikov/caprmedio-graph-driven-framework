---
atom_id: CA-A-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
version: 2
relations: {}
tier: 3
subjects:
  active: Atom.Carrier Destination
role: Analysis & Advisory
form: Specification Proposal
updated_at: 2026-11-02 22:59:57 +0400
---
## Summary

Declare stored Atom carrier destinations

## Changes

- Declare `Atom.Carrier Destination.File.Name` and `.Path` as mandatory Properties, each with `[string]{:1}`.
- Name is the full calculated filename, including its extension.
- Path is the calculated containing directory, relative to the repository root.
- Store the calculated values in the nested `carrier_destination.file.name` and `carrier_destination.file.path` keys in Atom frontmatter.
- Deliver using those values.

## Rationale

The Operator requested calculated destination Properties to simplify Delivery. The latest clarification makes both Properties mandatory. Existing filename, placement and Carrier rules keep their meaning.

The intermediate Properties declare the complete paths. Each container has zero direct values. File has exactly Name and Path. Each leaf has no dependent Properties.

## Drafts

| Draft marker | Active Subject | Carrier |
| --- | --- | --- |
| `CA-R-draft` | `Atom.Carrier Destination` | [CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination.md](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination.md) |
| `CA-R-draft` | `Atom.Carrier Destination.File` | [CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file.md](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file.md) |
| `CA-R-draft` | `Atom.Carrier Destination.File.Name` | [CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file-name.md](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file-name.md) |
| `CA-R-draft` | `Atom.Carrier Destination.File.Path` | [CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file-path.md](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file-path.md) |
| `CA-D-664@4-draft` | `Atom` | [CA-D-664@4-draft-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md](../../07_delivery/draft/CA-D-664@4-draft-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md) |

New Drafts use ID-free markers. Their complete carrier paths distinguish them. Stable IDs are allocated on promotion.

## Adoption

Before promotion:

1. Review the packet and specify the affected Carrier boundary.
2. Apply the canonical YAML encoding in the Delivery Draft.
3. Populate and validate the mandatory Properties on every affected Carrier, or cover deferred work with an explicit governed transition boundary.

Runtime calculation, frontmatter population and migration remain separate work that must satisfy these conditions.
