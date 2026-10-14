---
atom_id: CA-R-1882
content_role: Requirement
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-11 04:45:05 +0400"
subjects:
  governs: "MCP/selected Release manifest publisher"
  depends_on: [MCP, Projection, Manifest, Workflow, Step, Action, Operator, Run, Journal]
relations:
  relates_to: [CA-R-1847, CA-R-1848, CA-D-572, CA-P-1622]
---
# Summary

Publish only the admitted additive Release manifest successor

## Scope

the one exact Project-local selected-workflow binding repair that advances CA-O-030 from its recorded v6 native Action Pin to its active v7 Pin in the current canonical seventeen-route Projection.

## Claim

MCP **must** provide plan-first, Operator-authorized publication for **only** the registered single-Pin repair at `update_atom.native_action_calls[0]`, preserving every one of the seventeen route records, every other Pin and admission, and all unregistered source-freshness authority.

## Details

1. admission requires only the exact schema-5 CA-D-588 registration, its exact raw and canonical input Manifest hashes, the byte-identical archived CA-O-030 v6 Carrier, and the active current CA-O-030 v7 source Pin. Missing, stale, changed, substituted, or non-identical evidence blocks before any effect.
2. the candidate replaces **only** `routes[update_atom].native_action_calls[0]` when that sole occurrence equals the registered O030 v6 Pin. It retains the registered identity and source path; only its registered Version and digest advance to the active current O030 v7 Pin.
3. the candidate preserves the complete ordered seventeen-route registry, every other route Pin, all query, Release and public-Release admissions, the D572 Pin, and every source-freshness field except the derived selected-binding digest. It recomputes only that digest and the canonical Manifest digest through the existing algorithms. The registered successor raw-byte hash and both derived digests must match exactly.
4. normal discovery, dispatch and Manifest loading remain strict. This closed repair input validator admits no caller-selected loose mode, general source refresh, route/admission refresh, release-frontier update, or wider repair authority.
5. planning writes nothing. execution requires a trusted, operation-specific Operator context sealed to the Project root, exact observed input bytes, the current O030 source Pin, and exact candidate bytes. A prior Release publication or refresh grant cannot substitute for this repair.
6. the existing lifecycle adapter seals a pending intent, holds the canonical carrier lock through the final freshness check and atomic replacement, strictly reopens the output and finalizes the existing Journal event. Recovery records **only** matching already-published candidate bytes; it never replays a replacement.
7. this private source-projection capability does not execute a Workflow, dispatch an MCP Tool, change a runtime, or grant future repairs. The canonical Applicable Methodology location remains unchanged.
