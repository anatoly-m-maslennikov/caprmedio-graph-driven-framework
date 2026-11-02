---
atom_id: CA-D-602
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-10 07:16:06 +0400"
subjects:
  governs: "Framework Installation contribution/Admitted source catalog"
  depends_on: [Tool, Framework Package, Methodology, Extension, Configuration, MCP, Workflow Run, Action, Operator, Journal, Source Carrier]
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

### Retained Release frontier input

The host bridge in `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/source_admission_host_command.py` reopens one explicitly named retained Release Run at its completed delivery frontier. It reads the frozen selected request, current graph/source bindings, actual first three Step/Action start and completed-terminal records, and the private checkpoint. Those records must agree on the Project, source definitions, parentage, candidate and exact completed O172 occurrence. Missing, partial, uncertain, differently bound or advanced frontiers refuse before source admission.

The bridge reconstructs the actual sealed candidate, Methodology export, private compilation and pre-catalog source snapshot through their physical readers. Caller-provided typed objects or expected hashes do not replace those observations. Reopening is read-only: it never starts, resumes or replays a Release phase. The source snapshot remains bound to the retained candidate Run. Its existing digest and the direct command receipt provide traceability; no extra Release-to-admission registry is created.

### Direct MCP binding

The Project MCP advertises `admit_package_sources` as the direct execution binding for CA-O-199. The server fixes the Project root. A closed preview request has exactly `operation = "preview"` and `release_run_id`; it observes that explicit retained frontier without an Action start or catalog write. It does not select a latest Run implicitly.

A closed execute request has exactly `operation = "execute"`, `command_id`, `release_run_id`, `operator`, `authorization_ref` and `observed_snapshot_sha256`. The observed digest must equal the physically reopened snapshot before effects. The exact O172 occurrence, current Operator registry reference and frozen Release authorization reference are derived from the retained Run and Project, not independent caller overrides.

The Operator command carrier is canonical UTF-8 JSON using the byte rules above, retained at a safe Project-relative regular path. It has exactly `schema_version = 1`, `operation = "admit_package_sources"`, `command_id`, `release_run_id`, `operator`, `journal_author`, `snapshot_sha256`, `operators_registry_sha256` and `action_source`. These values bind the actual request, exact snapshot, current registered Operator/account and current CA-O-199 source. Its raw bytes are invocation evidence, not a permission Boolean, admission result or test pass. Unknown or duplicate fields, noncanonical bytes, aliases, secret paths, missing evidence or stale/mismatched bindings refuse before a direct Action start.

Execute invokes the existing source-admission command once through a real direct Action Session. It returns actual snapshot, command/admission receipts, catalog identities and outcome. Failed or uncertain effects retain their actual evidence and are not replayed. Discovery exposes the exact admitted binding and request schema; source availability alone is not executable admission.

```toml
[tool_binding]
name = "ADMIT_PACKAGE_SOURCES"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/source_admission_mcp.py"
mcp_name = "admit_package_sources"
action_ids = ["CA-O-199"]
```
