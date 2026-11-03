---
atom_id: CA-A-1314
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 1
relations: {}
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Carrier Destination
role: Analysis & Advisory
form: Specification Proposal
updated_at: 2026-11-03 00:20:05 +0400
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

## Current Atoms

| Atom | Version | Active Subject | Carrier |
| --- | --- | --- | --- |
| `CA-R-2692` | 1 | `Atom.Carrier Destination` | [CA-R-2692-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination.md](../04_requirement/CA-R-2692-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination.md) |
| `CA-R-2693` | 1 | `Atom.Carrier Destination.File` | [CA-R-2693-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file.md](../04_requirement/CA-R-2693-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file.md) |
| `CA-R-2694` | 1 | `Atom.Carrier Destination.File.Name` | [CA-R-2694-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file-name.md](../04_requirement/CA-R-2694-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file-name.md) |
| `CA-R-2695` | 1 | `Atom.Carrier Destination.File.Path` | [CA-R-2695-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file-path.md](../04_requirement/CA-R-2695-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file-path.md) |
| `CA-D-664` | 5 | `Atom` | [CA-D-664-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md](../07_delivery/CA-D-664-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md) |

## Publication Scope

The Operator approved promotion of this proposal and the five listed source Atoms only.

Carrier population, migration and runtime activation remain separate work. This publication does not claim conformance of existing Carriers to the mandatory Properties. No governed transition or data exception is introduced.

The Property constraints, filename rules and placement rules retain their meaning.
