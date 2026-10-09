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
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  delivery_for: [CA-R-1923, CA-R-1924]
---
# Summary

Retain public Full Gate receipt references

## Scope

the Full Gate evidence used by one public release.

## Claim

public-release gate evidence **must** retain the existing typed FullGateEvidence durable receipt reference with its candidate snapshot binding as report evidence on the parent public Action Run.

## Details

This Delivery does not copy, synthesize, or replace `RELEASE_VERSION` evidence carriers. A final Version History source change requires a second retained reference.
