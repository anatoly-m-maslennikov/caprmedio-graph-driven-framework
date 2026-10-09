---
atom_id: CA-E-604
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Source catalog refusal"
  depends_on: [Tool, Framework Package, Methodology, Extension, Configuration]
relations:
  evaluation_for: [CA-R-1908, CA-M-359, CA-D-602]
---
# Summary

Verify source catalog pins before any package effect

## Scope

the unknown-revision and catalog-binding refusal boundary.

## Claim

the QA case **must** prove that an unknown, mutable, duplicate or mismatched catalog revision fails **before** candidate, image, package selector or target runtime effect.

## Details

Fixtures alter each catalog field separately and snapshot all effect roots before and after. Positive evidence proves the identical catalog digest in manifest, candidate seal, Full Gate/image proof, `.caprmedio_install/current.toml` and target result. An available private extension is proven non-autoloaded.
