---
atom_id: CA-D-597
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-09 22:34:21 +0400"
subjects:
  governs: "Framework Installation contribution/Sealed candidate and promotion proof"
  depends_on: [Tool, Framework Package, Manifest, Test Suite, Docker Image, Journal]
relations:
  delivery_for: [CA-R-1909, CA-R-1910, CA-M-360]
---
# Summary

Retain sealed package candidate and promotion proof

## Scope

One private candidate package and its exact suite, image and promotion evidence.

## Claim

the INSTALL_TOOLS facade **must** stage and seal every candidate beneath `.caprmedio_tmp/release_candidates/<run_id>/` **before** it may be promoted, and the promoted package **must** have the same manifest bytes as the tested image input.

## Details

The candidate root contains `package/`, `seal.toml`, `full-gate.toml`, `image-proof.toml` and `promotion.toml`. `seal.toml` binds run ID, package manifest SHA-256, source-catalog digest and ordered package rows. `full-gate.toml` names the existing closed Full Gate receipt and its exact package manifest digest; `image-proof.toml` names the immutable inspected image digest, complete-package/MCP canary receipt and the same manifest digest. Neither a Boolean JSON field, mutable tag, cached report nor a second package copy is gate evidence.

The internal package evidence view contains its explicit schema kind, candidate snapshot digest, actual package-manifest digest, source-catalog digest, candidate run ID, input-manifest digest, Framework Version and Version carrier digest, physical package root, complete member inventory and test phase map. Every inventory member contains its package-relative path, byte digest, mode and role. A later consumer reopens the package against the sealed compilation and compares the entire view; a caller-constructed typed value is not sufficient.

For a reusable schema-1 package, image build, image verification, Candidate E2E and the existing Full Gate receipt carry and compare the same package schema, manifest, catalog, run, input-manifest and Version bindings. The Unit Gate remains a pre-package check of the physically revalidated compiled candidate and its sealed source inputs; its receipt binds those inputs, not an invented package result. The aggregate uses the same Unit/image/E2E partition algorithm for both explicit schema kinds. Retained schema-2 evidence remains readable under its original schema; absent legacy catalog fields do not become schema-1 proof or implicit defaults.

### Retained native package evidence

After live source revalidation and complete package-inventory equality, an explicitly invoked retention operation may write `package_evidence/<receipt_sha256>.json` beneath the private candidate root. The immutable sidecar travels with the unchanged package as a separate content-addressed installation-owned carrier. It is outside the closed package inventory and is not stored only in a mutable current selector.

The sidecar is canonical UTF-8 JSON with sorted keys, compact separators, no trailing newline and no self-checksum member. Its exact fields are `schema_version = 1`, `package_schema = "portable-1"`, `candidate_snapshot_manifest_sha256`, `package_manifest_sha256`, `source_catalog_sha256`, `candidate_run_id`, `input_manifest_sha256`, `framework_version`, `version_toml_sha256`, `member_inventory`, `test_bindings` and `phase_map_sha256`. `member_inventory` is path-ordered and each member contains exactly `path`, `sha256`, `mode` and `role`. Source-path-ordered `test_bindings` contain exactly `source_path`, `package_path`, `sha256` and `phase`; they preserve the observed candidate-to-package test mapping and exact Unit/Candidate E2E phase partition. Only the separately typed Skill projection is excluded from duplicate test membership.

A retained reader reopens the actual schema-1 package and sidecar, verifies their exact byte identities, complete inventory, Version/catalog bindings and packaged test projection, and reconstructs the phase map without current checkout, selector or caller-provided compilation authority. Missing, extra, altered or aliased members fail. Image, Candidate E2E and Full Gate receipts bind the sidecar digest and its Project-relative carrier; later installation copies the unchanged sidecar and verifies it against the selected package. This is an original-artifact reader, not live source admission, a test pass, promotion authority or permission to launch a Workflow.

Promotion copies or atomically moves only the sealed package tree to the digest-named release directory, then reopens its exact `manifest.toml` and records source and destination tree digests in `promotion.toml`. A changed byte, mode, source catalog, image input or gate receipt refuses promotion and retains the candidate evidence.
