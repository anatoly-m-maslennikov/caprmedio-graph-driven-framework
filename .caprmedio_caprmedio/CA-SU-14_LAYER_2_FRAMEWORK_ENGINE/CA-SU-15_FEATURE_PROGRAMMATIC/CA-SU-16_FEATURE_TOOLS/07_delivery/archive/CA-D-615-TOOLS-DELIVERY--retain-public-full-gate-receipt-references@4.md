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
version: 4
updated_at: "2026-10-10 18:14:20 +0400"
relations:
  delivery_for: [CA-R-1923, CA-R-1924]
---
# Summary

Retain public Full Gate receipt references

## Scope

the local Full Gate evidence reused by one public release.

## Claim

public-release gate evidence **must** retain one reopened reference to the verified local Full Gate evidence for the stable selected candidate before public effects. Public-document closures bind their own carriers to that candidate; they do not create a closure-specific Full Gate receipt or bridge.

## Details

This Delivery does not copy, synthesize, or replace `RELEASE_VERSION` evidence carriers. The Tool derives the candidate and package identity locally from the reread Source Proof and verified typed local Full Gate result; it accepts no caller-supplied receipt, package identity, pass result, or digest. The evidence root and receipt reference are safe Project-relative recorded carriers, and every SHA-256 is lowercase 64-hexadecimal.

The reopened evidence remains bound to the exact D566 candidate snapshot, framework version, `version.toml` digest, package identity, complete suite evidence, promotion, and live verification. It is read-only for public release. A changed executable candidate, Methodology, package, Version, or `version.toml` cannot reuse it; actual PR URL and concise Version History metadata can.
