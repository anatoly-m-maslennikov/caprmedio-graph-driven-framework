---
atom_id: CA-D-602
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-10 03:33:44 +0400"
subjects:
  governs: "Framework Installation contribution/Admitted source catalog"
  depends_on: [Tool, Framework Package, Methodology, Extension, Configuration]
relations:
  delivery_for: [CA-R-1902, CA-R-1908, CA-M-359]
---
# Summary

Encode the admitted package source catalog

## Scope

The package-owned catalog that binds Core, optional extensions, configuration and active Methodology sources to immutable admitted revisions.

## Claim

the INSTALL_TOOLS facade **must** include an admitted `catalog.toml` with a pinned revision and digest for every selected source, and an unknown revision **must** fail before any package, image or target effect.

## Details

Each ordered `[source.<identity>]` record contains `kind`, `revision`, `sha256`, `admission_receipt_sha256`, `visibility`, `selection_default` and package-relative `path`. Core is required; optional extensions and configuration may be catalogued as available. `selection_default = false` and `visibility = private` never cause target autoloading; target selection is an explicit validated target-context choice.

For the explicitly admitted local Core, selected active Methodology and declared support snapshots, `revision` may equal their exact lowercase 64-hex content digest. `admission_receipt_sha256` hashes the actual retained admission record, which binds the Operator command, selected source identity and exact snapshot digest. It is not the source digest repeated as a substitute for an admission record.

The retained record is canonical UTF-8 JSON with sorted object keys, compact separators, `ensure_ascii=false` and `allow_nan=false`, without a self-checksum member or trailing newline. It has exactly `schema_version = 1`, `operation = "admit_package_sources"`, `operator`, `command_ref`, `action_run_id`, `snapshot_sha256` and `sources`. `operator`, `command_ref` and `action_run_id` identify the verified Operator command and its admitted Action Run; they contain references, not raw command text or credentials.

Each identity-ordered `sources` member has exactly `identity`, `kind`, `revision`, `sha256`, `visibility`, `selection_default` and `path`, matching the corresponding catalog descriptor except for its receipt hash. Identities are unique. `snapshot_sha256` is the SHA-256 of the canonical JSON `sources` array. The shared record may admit Core, selected active Methodology and declared support in one commanded Action; their catalog records reference the same receipt rather than duplicating the command record.

The actual receipt bytes are retained at `admissions/<admission_receipt_sha256>.json` and included in the package manifest. A package reader reopens that exact regular member, checks its byte hash, closed schema and source-snapshot checksum, then matches every catalog record to exactly one receipt source descriptor. Missing records, malformed records, hash-only substitutes or mismatched descriptors fail before package reuse. This proof carrier references the canonical Action/Journal evidence; it is not another Journal or a test result.

The catalog SHA-256 is carried by the package manifest, candidate seal, package-current selector and target installation result. Empty, symbolic, mutable-tag, unresolved, duplicate or content-mismatched revisions are not pins. No caller-provided catalog replaces the sealed catalog.

### Explicit host command evidence

The standalone source-admission command creates a real direct CA-O-199 Action Run; it does not manufacture a selected Workflow context. Its prospective input binds the selected Project, exact source snapshot, registered Operator, Journal account, current Operator registry bytes, and current Action source bytes. The actual Action-start event records that input before catalog publication.

The immutable host-command receipt has exactly `schema_version = 1`, `operation = "admit_package_sources"`, `command_id`, `operator`, `journal_author`, `action_id = "CA-O-199"`, `action_run_id`, `action_start_event_id`, `snapshot_sha256`, `action_source`, and `operators_registry_sha256`. `action_source` has exactly `atom_id`, `version`, `path`, and `sha256`; its path is Project-relative. The nonempty command ID identifies this explicit invocation, not a permission flag. Canonical JSON uses the admission record's byte rules.

The receipt is retained at `.caprmedio_runtime/installation/commands/<receipt_sha256>.json`. The admission record's `command_ref` is the Project-relative reference to that physically reopened receipt. It is derived after the receipt bytes are fixed, so the receipt has no self-reference or self-checksum cycle. Its Action Run and start-event IDs must reopen the actual canonical Journal evidence, with the registered Journal account, exact source binding and prospective input. The host revalidates that evidence, registry, source and snapshot before and after admission.

This receipt proves the particular command and input binding. It is not a source-admission result, permission Boolean, Full Gate pass, second Journal, or command to start another operation. Failed or uncertain effects remain recorded and cannot be silently replayed.
