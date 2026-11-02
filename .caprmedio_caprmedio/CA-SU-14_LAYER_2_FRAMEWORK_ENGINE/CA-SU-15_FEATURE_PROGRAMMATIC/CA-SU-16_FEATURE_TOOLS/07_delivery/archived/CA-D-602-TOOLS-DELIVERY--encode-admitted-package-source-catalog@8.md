---
atom_id: CA-D-602
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 8
updated_at: "2026-10-10 18:27:21 +0400"
subjects:
  governs: "Framework Installation contribution/Admitted source catalog"
  depends_on: [Tool, Framework Package, Methodology, Extension, Configuration, MCP, Workflow Run, Action, Operator, Journal, Source Carrier, Projection]
relations:
  delivery_for: [CA-R-1902, CA-R-1908, CA-M-359]
---
# Summary

Encode the admitted package source catalog

## Scope

The package-owned catalog that binds Core, optional extensions, configuration, active Methodology, support and non-authoritative Tool-binding projections to immutable admitted revisions.

## Claim

the INSTALL_TOOLS facade **must** include an admitted `catalog.toml` with a pinned revision and digest for every selected source and every retained binding-projection source, and an unknown revision **must** fail before any package, image or target effect.

## Details

Each ordered `[source.<identity>]` record contains `kind`, `revision`, `sha256`, `admission_receipt_sha256`, `visibility`, `selection_default` and package-relative `path`. Core is required; optional extensions and configuration may be catalogued as available. `selection_default = false` and `visibility = private` never cause target autoloading; target selection is an explicit validated target-context choice.

`kind = "binding"` designates only the D561 sealed `binding-projection` tree at `methodology/bindings/`. Its descriptor is required exactly when the frozen `binding_atoms` frontier is nonempty and forbidden when that frontier is empty. It has `selection_default = false`; it is not eligible for Framework Instance Settings selection, Extension activation, Project Configuration selection or compiler Atom input. Its identity and cardinality are derived from the explicit frozen frontier rather than a hardcoded Tool or Atom list. Every frontier member has exactly one package projection and every projection has exactly one frontier member; missing, extra, duplicate or overlapping binding descriptors refuse before packaging.

For the explicitly admitted local Core, selected active Methodology, declared support and binding-projection snapshots, `revision` may equal their exact lowercase 64-hex content digest. `admission_receipt_sha256` hashes the retained internal source-validation record for the Operator-commanded local-release workflow, which binds the selected source identity and exact snapshot digest. It is not the source digest repeated as a substitute for a validation record.

The retained record is canonical UTF-8 JSON with sorted object keys, compact separators, `ensure_ascii=false` and `allow_nan=false`, without a self-checksum member or trailing newline. It has exactly `schema_version = 1`, `operation = "admit_package_sources"`, `operator`, `command_ref`, `action_run_id`, `snapshot_sha256` and `sources`. `operator`, `command_ref` and `action_run_id` identify the verified parent Operator command and its release Action Run; they contain references, not raw command text or credentials.

Each identity-ordered `sources` member has exactly `identity`, `kind`, `revision`, `sha256`, `visibility`, `selection_default` and `path`, matching the corresponding catalog descriptor except for its receipt hash. Identities are unique. `snapshot_sha256` is the SHA-256 of the canonical JSON `sources` array. The shared record may validate Core, selected active Methodology, declared support and the binding-projection tree within one commanded local release; their catalog records reference the same receipt rather than duplicating it.

The actual receipt bytes are retained at `admissions/<admission_receipt_sha256>.json` and included in the package manifest. A package reader reopens that exact regular member, checks its byte hash, closed schema and source-snapshot checksum, then matches every catalog record to exactly one receipt source descriptor. For `kind = "binding"`, it additionally reopens the frozen `binding_atoms` frontier and each canonical projection, verifies projection ownership metadata and proves that removing only the canonical metadata insertion yields the exact raw bytes named by that member's Atom ID, Version, source path and SHA-256. Missing records, malformed records, hash-only substitutes, copied authority sources, lineage mismatches or mismatched descriptors fail before package reuse. This proof carrier references the canonical parent Action/Journal evidence; it is not another Journal, authority registry, separately executable source-admission workflow, or test result.

The catalog SHA-256 is carried by the package manifest, candidate seal, package-current selector and target installation result. Empty, symbolic, mutable-tag, unresolved, duplicate or content-mismatched revisions are not pins. No caller-provided catalog replaces the sealed catalog.

### Internal source validation

The Operator-commanded local-release workflow derives, catalogs and reopens the exact source snapshot as internal preparation. It does not start CA-O-199, expose direct source admission through MCP, require a second Operator command, or make source validation an independently executable workflow.

The internal validation physically reopens the sealed candidate, Methodology export, private compilation, binding projections and pre-catalog source snapshot through their physical readers. Caller-provided typed objects or expected hashes do not replace those observations. The source snapshot remains bound to the retained candidate Run. Missing, partial, uncertain, stale, aliased, duplicate or differently bound sources refuse before package, image, target, or runtime effects; uncertainty remains recorded and is not replayed. It is preparation and cannot replace the one complete local suite before local release effects.
