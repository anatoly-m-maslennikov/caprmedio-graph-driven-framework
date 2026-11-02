---
atom_id: CA-M-339
content_role: Method
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-11 02:48:54 +0400"
subjects:
  governs: "MCP/selected Release manifest publication"
  depends_on: [MCP, Projection, Manifest, Workflow, Step, Action, Operator, Run, Journal]
relations:
  method_for: [CA-R-1882]
---
# Summary

Derive and publish one additive Release manifest successor

## Scope

the deterministic plan and guarded publication of the three registered source Pins in the current canonical selected-workflow Manifest.

## Claim

the publisher **must** derive and publish the exact registered CA-O-030, CA-M-343, and CA-D-579 Manifest successor through the existing trusted lifecycle adapter, binding the three allowed occurrences, exact canonical input, active current sources, candidate bytes and canonical Journal evidence.

## Details

1. load only the canonical `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` through the narrow schema-4 registration reader. Reject a missing, malformed, noncanonical, raw-byte or canonical-digest-mismatched input, any route order/count other than the registered seventeen rows, or changed admission count.
2. verify the CA-P-1987 receipt's exact O030 v5 prior Pin and the archived M343 v5 and D579 v7 prior Carriers, then verify every active current source carrier against its registered identity, Version, source path and digest. The receipt and archives are evidence for these three prior Pins, not a general source-selection authority.
3. locate one `update_atom.native_action_calls[0]`, one `release_source_admissions[0].rmed_frontier[11]`, and one `release_source_admissions[0].rmed_frontier[31]`. Require each to equal its registered prior Pin and replace it with only its registered active current Pin. Reject a missing, repeated, reordered, already-current, identity-changed, path-changed, or any other stale Pin.
4. deep-copy every other value unchanged, including all seventeen route rows apart from O030, every other Release-admission Pin apart from M343 and D579, query-source admissions, public-Release admission, registry reference, registry Version and registry digest. Recompute only `source_freshness.selected_binding_digest` and `canonical_manifest_sha256`; require both and the deterministic serialized candidate SHA-256 to equal the registration.
5. return a byte-preserving plan by default. The trusted host validates the registered human Operator and seals the Project root, raw input digest, three active current source Pins, exact candidate serialization, and operation marker. Caller booleans or callbacks do not grant authority.
6. acquire the existing canonical carrier Journal lock; freshly recheck input and all three current source Pins; store one closed pending intent; freshly recheck them again **before** same-directory atomic replacement. The operation marker is strictly this three-Pin repair and cannot authorize a Release or other refresh.
7. strictly reopen the complete published bytes through the normal loader, then finalize the existing completed governed-project-change event and its prior-event link. The Journal carrier revision does not give the Projection an independent Version.
8. **after** a recording failure or restart, reopen the exact pending intent and physical target. Matching candidate bytes permit finalizing that same event once without a replacement. Nonmatching bytes or changed sources retain pending evidence and a truthful blocked/ambiguous result. Recovery never grants pre-write authority.
