---
atom_id: "CA-D-614"
content_role: "Delivery"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release material source proof"
  depends_on: [README, Pull Request, Version History, Source Proof, Version, Local Release]
version: 4
updated_at: "2026-10-10 18:14:20 +0400"
relations:
  delivery_for: [CA-R-1922]
---
# Summary

Serialize public material source proof

## Scope

the material proof of one public documentation closure.

## Claim

public material Source Proof **must** carry only repository-relative README, full PR body, Version History references and raw-byte SHA-256 values; the D566 candidate snapshot SHA-256; canonical Version value and `version.toml` SHA-256; and canonical `public_document_closure_sha256`, with no source contents, credentials, or secret values. The bound host separately retains and reopens typed local-release gate, promotion, and live-verification proof references; they are not serialized Source Proof fields.

## Details

The Version History hyperlink is represented only after its actual PR URL is known and is checked against that remote result. The Source Proof serializes CA-R-1922's closed public-document-closure fields and digest. The closed serialized fields are exactly `candidate_snapshot_manifest_sha256`, `framework_version`, `version_toml_sha256`, `readme_ref`, `readme_sha256`, `pr_body_ref`, `pr_body_sha256`, `version_history_ref`, `version_history_sha256`, `version_history_summary`, `version_history_pr_url`, `version_history_pr_number`, and `public_document_closure_sha256`; the last field is locally recomputed from the preceding fields and their reread raw carriers, never taken from a request. Its resulting Source Proof has a new public-document-closure binding while retaining the same D566 candidate snapshot binding. It contains no local-release proof reference. When its canonical Version value and `version.toml` digest remain unchanged, the bound host separately reopens the original local-release promotion and live-verification proof references without a new Full Gate or bridge for that metadata-only closure.

The Tool reopens the Source Proof carriers and the separately bound typed local-release proofs before public effects. The canonical Version value and byte digest must equal the verified local-release identity; a changed executable candidate, Methodology, package, Version, or `version.toml` requires the renewed local cycle governed by CA-R-1922-TOOLS-REQUIREMENT--bind-public-materials-to-the-selected-source-snapshot. Metadata-only finalization neither installs nor promotes a Framework Package or runtime.
