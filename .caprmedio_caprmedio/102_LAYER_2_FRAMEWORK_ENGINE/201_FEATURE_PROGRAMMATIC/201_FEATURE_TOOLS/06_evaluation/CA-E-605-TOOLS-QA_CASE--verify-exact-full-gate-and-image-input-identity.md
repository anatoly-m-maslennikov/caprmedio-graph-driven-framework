---
atom_id: CA-E-605
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
  governs: "Framework Installation contribution/Full Gate identity"
  depends_on: [Tool, Framework Package, Test Suite, Docker Image, Manifest]
relations:
  evaluation_for: [CA-R-1909, CA-R-1910, CA-M-360, CA-D-597]
---
# Summary

Verify exact Full Gate and image input identity

## Scope

the sealed candidate gate and immutable image acceptance boundary.

## Claim

the QA case **must** accept promotion **only** when the existing Full Gate, exact image inspection and canary bind the same sealed package bytes, and **must not** accept a synthetic pass field or post-gate mutation.

## Details

The golden asserts every declared Unit module and exact three Docker E2E harnesses, manifest/catalog/version equality and immutable image digest. It changes one package byte or mode, dependency/version input, image input, test phase, receipt or canary output after sealing; each failure keeps `.caprmedio_install/current.toml` unchanged. Actual Docker proof remains distinct from a test double.
