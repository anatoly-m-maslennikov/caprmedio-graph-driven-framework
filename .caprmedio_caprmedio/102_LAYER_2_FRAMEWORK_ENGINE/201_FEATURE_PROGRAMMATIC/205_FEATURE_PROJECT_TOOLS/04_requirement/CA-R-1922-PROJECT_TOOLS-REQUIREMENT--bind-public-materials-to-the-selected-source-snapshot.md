---
atom_id: "CA-R-1922"
content_role: "Requirement"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release material source proof"
  depends_on: [README, Pull Request, Version History, Source Proof, Version, Local Release]
version: 4
updated_at: "2026-10-10 19:05:35 +0400"
relations:
  relates_to: [CA-O-192, CA-O-194, CA-O-198, CA-M-366, CA-E-612, CA-D-614]
---
# Summary

Bind public materials to the selected source snapshot

## Scope

one selected public documentation closure.

## Claim

the public-release Tool **must** bind the README, one full PR description, concise Version History carrier, selected Version, and D566 candidate snapshot to one source proof with one canonical `public_document_closure_sha256`, then pass one fresh complete public suite before its first public effect.

## Details

The full PR description separately states What’s new and What’s fixed. The public-document closure is the lowercase SHA-256 of canonical UTF-8 JSON (sorted object keys, compact separators, `ensure_ascii=false`, and `allow_nan=false`) with exactly `schema: "caprmedio.public_release.document_closure.v1"`, `candidate_snapshot_manifest_sha256`, `framework_version`, `version_toml_sha256`, `readme_ref`, `readme_sha256`, `pr_body_ref`, `pr_body_sha256`, `version_history_ref`, `version_history_sha256`, `version_history_summary`, `version_history_pr_url`, and `version_history_pr_number`. The three references are safe Project-relative regular-file carriers whose raw bytes equal their SHA-256 values. URL and number are both `null` before an actual PR exists, or are one exact matching actual PR identity afterward. A substituted carrier, document byte, summary, PR identity, version, candidate snapshot, or closure digest invalidates gate evidence.

The Tool itself physically rereads the three carriers and canonically re-encodes this exact closed object to derive `public_document_closure_sha256`. It never accepts a caller-supplied closure digest or closure fields as an input or admission parameter. A serialized Source Proof is valid only when its closure field equals that local recomputation.

The selected Version value and exact root `version.toml` byte digest must agree with the reopened verified local-release Version and its retained gate, promotion and live-verification proof. The initial public closure then receives one fresh complete public suite and its retained Public Full Gate before publication. An actual Version History link changes `public_document_closure_sha256`, but only after that first public effect; the exact URL/history-only follow-up reuses that retained Public Full Gate. If public preparation changes executable candidate bytes, Methodology, package contents, Version, or `version.toml`, publication requires a fresh local candidate, one full local suite, same-bytes promotion and live verification first, followed by a new public suite. A public gate cannot substitute for that local release, and a local gate cannot substitute for the initial public suite.
