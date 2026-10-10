---
atom_id: "CA-D-615"
content_role: "Delivery"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Full Gate receipt reference"
  depends_on: [Full Gate, Source Proof, Journal]
version: 3
updated_at: "2026-10-10 12:56:30 +0400"
relations:
  delivery_for: [CA-R-1923, CA-R-1924]
---
# Summary

Retain public Full Gate receipt references

## Scope

the Full Gate evidence used by one public release.

## Claim

public-release gate evidence **must** retain one canonical `PublicDocumentClosureGateBridgeV1` report carrier for **each** O194 initial source closure and O198 post-history-link closure before that phase's public push. Each bridge joins the current typed producer receipt, selected N+1 same-Version package identity, and exact locally derived `public_document_closure_sha256` on the parent public Action Run.

## Details

This Delivery does not copy, synthesize, or replace `RELEASE_VERSION` evidence carriers. A bridge is canonical UTF-8 JSON with sorted object keys, compact separators, `ensure_ascii=false`, and `allow_nan=false`, and has exactly these fields: `schema` with literal value `caprmedio.public_release.document_closure_gate_bridge.v1`; `phase` with literal `initial` or `history_link`; `candidate_snapshot_manifest_sha256`; `framework_version`; `version_toml_sha256`; `package_manifest_sha256`; `full_gate_candidate_run_id`; `full_gate_evidence_root`; `full_gate_receipt_sha256`; `producer_result_ref`; and `public_document_closure_sha256`. The Tool derives all fields locally from the reread Source Proof and the returned current typed native Full Gate result from that same phase; it does not accept any bridge field, digest, receipt, package identity, or pass result from the request caller. `full_gate_evidence_root` and `producer_result_ref` are safe Project-relative recorded carriers; all SHA-256 fields are lowercase 64-hexadecimal values.

The O194 bridge carries the fresh current producer receipt for its initial closure. The O198 bridge carries a distinct fresh current producer receipt for the post-link closure and the same candidate/package identity only when the reread source establishes that its Version, `version.toml`, and D566 candidate snapshot are unchanged. Neither bridge substitutes the other, revives an earlier receipt, or creates another Operator authorization.
