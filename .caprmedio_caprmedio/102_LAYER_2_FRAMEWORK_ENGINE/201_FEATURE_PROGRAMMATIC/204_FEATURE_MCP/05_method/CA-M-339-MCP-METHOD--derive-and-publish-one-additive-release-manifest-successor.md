---
atom_id: CA-M-339
content_role: Method
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-11 04:45:05 +0400"
subjects:
  governs: "MCP/selected Release manifest publication"
  depends_on: [MCP, Projection, Manifest, Workflow, Step, Action, Operator, Run, Journal]
relations:
  method_for: [CA-R-1882]
---
# Summary

Derive and publish one additive Release manifest successor

## Scope

the deterministic plan and guarded publication of the one registered CA-O-030 source Pin in the current canonical selected-workflow Manifest.

## Claim

the publisher **must** derive and publish the exact registered CA-O-030 v6-to-v7 Manifest successor through the existing trusted lifecycle adapter, binding its single allowed occurrence, exact canonical input, active current source, candidate bytes and canonical Journal evidence.

## Details

1. load only the canonical `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` through the narrow schema-5 registration reader. Reject a missing, malformed, noncanonical, raw-byte or canonical-digest-mismatched input, any route order/count other than the registered seventeen rows, or changed admission count.
2. verify the archived O030 v6 Carrier is byte-identical to the registered prior Pin's exact digest, ID and Version, then verify the active O030 v7 source carrier against its registered identity, Version, source path and digest. The archive is evidence for this one prior Pin, not a general source-selection authority; its Active historical status is not independently constrained.
3. locate one `update_atom.native_action_calls[0]`. Require it to equal the registered O030 v6 prior Pin and replace it with only its registered active current O030 v7 Pin. Reject a missing, repeated, reordered, already-current, identity-changed, path-changed, or any other stale Pin.
4. deep-copy every other value unchanged, including all seventeen route rows apart from the one O030 occurrence, every Release-admission Pin, query-source admission, public-Release admission, registry reference, registry Version and registry digest. Recompute only `source_freshness.selected_binding_digest` and `canonical_manifest_sha256`; require both and the deterministic serialized candidate SHA-256 to equal the registration.
5. return a byte-preserving plan by default. The trusted host validates the registered human Operator and seals the Project root, raw input digest, current O030 source Pin, exact candidate serialization, and operation marker. Caller booleans or callbacks do not grant authority.
6. acquire the existing canonical carrier Journal lock; freshly recheck input and the current O030 source Pin; store one closed pending intent; freshly recheck them again **before** same-directory atomic replacement. The operation marker is strictly this single-Pin repair and cannot authorize a Release or other refresh.
7. strictly reopen the complete published bytes through the normal loader, then finalize the existing completed governed-project-change event and its prior-event link. The Journal carrier revision does not give the Projection an independent Version.
8. **after** a recording failure or restart, reopen the exact pending intent and physical target. Matching candidate bytes permit finalizing that same event once without a replacement. Nonmatching bytes or changed sources retain pending evidence and a truthful blocked/ambiguous result. Recovery never grants pre-write authority.
