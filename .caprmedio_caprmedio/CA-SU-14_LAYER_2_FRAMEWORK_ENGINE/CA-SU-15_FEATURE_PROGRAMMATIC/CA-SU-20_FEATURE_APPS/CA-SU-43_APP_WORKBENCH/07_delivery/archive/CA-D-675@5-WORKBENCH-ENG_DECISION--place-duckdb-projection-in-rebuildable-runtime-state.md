---
atom_id: CA-D-675
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 5
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2723
  - CA-R-2728
carrier_destination:
  file:
    name: CA-D-675@5-WORKBENCH-ENG_DECISION--place-duckdb-projection-in-rebuildable-runtime-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
updated_at: 2026-11-04 16:35:58 +0400
---

## Summary

Place the DuckDB Projection in rebuildable runtime state

## Claim scope

The in-memory placement, direct model parsing, and trusted-query boundary of the Workbench query Projection.

## Claim

### Prose Claim

The existing application must own the rebuildable DuckDB Projection and direct Current-model reader in memory. Source files are read directly; no DuckDB database file, derived database path, on-disk schema, cache, stored intermediate source or materialized data, or spill file is delivered. The public table surface remains exactly the in-memory `atoms` and `scope_units` tables. Ordinary internal cache updates are runtime maintenance, not logical Projection mutations.

Deliver DuckDB `2.0.0` with an image-bundled DuckPGQ extension in the WORKBENCH Docker image. The image contains the selected pair; startup does not download an extension or require a separate database server. Trusted startup loads the extension, enables the selected version's native SQL/PGQ grammar, builds the in-memory graph, and only then accepts public queries.

The Trusted SQL MVP admits exactly one native `SELECT` and executes it inside a native `BEGIN TRANSACTION READ ONLY` boundary. External access is disabled and the relevant configuration is locked for public requests. The contract requires no spill to disk and no file-based read-only connection switch. DuckPGQ native graph queries remain available through the selected extension; no custom SQL parser or traversal API is added.

DuckPGQ internal management calls are unsupported for public requests. Even under a read-only transaction, an unsupported internal call may invalidate the connection. Report an explicit engine error that says restart is required; do not promise a capability sandbox or automatic query retry. An ordinary SQL error leaves the connection usable for the next request. Source files remain the authority, and a failed source or graph refresh is reported rather than repaired or hidden.

The in-memory Projection and property graph are rebuildable and do not edit, move, archive, promote, or replace source Atoms. Publish source rows, materialized outgoing Relations, row hashes, and graph mappings as one synchronized state. Restart WORKBENCH after code changes; hot-reload owner handoff is outside this MVP.

Use the single in-memory connection directly. Complete successful native transactions with COMMIT. Do not add application rollback, candidate-database swapping, retries, or automatic connection recovery. Report failures to stderr and the originating caller; a failed owner may require explicit restart.

For the current caprmedio Project inventory, allocate `1536m` to the Project MCP container, including the existing MCP/HTTP process, parsed rows, DuckDB/DuckPGQ mappings and refresh peak. Reassess capacity as the inventory grows; do not enable disk spill or silently discard valid rows to fit a smaller limit. The public health endpoint is `/caprmedio/health`.
