---
atom_id: CA-E-604
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 22:13:15 +0400"
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

1. Fixtures alter each catalog field separately and snapshot effect roots before and after refusal.
2. Receipt fixtures cover a missing regular carrier, a symlink, altered bytes, a malformed or noncanonical record, a wrong source-snapshot checksum and a descriptor that differs from its catalog record. A coherent digest string alone is not admission evidence.
3. Source-admission fixtures use a real pre-catalog snapshot and an explicitly admitted Operator command. Missing admission or an invocation bound to a different snapshot produces no catalog or receipt write. Matching admission retains actual receipt bytes and catalog references; reopening verifies them before packaging.
4. Positive downstream evidence proves the identical catalog digest in manifest, candidate seal, Full Gate/image proof, `.caprmedio_install/current.toml` and target result. A focused admission or package test does not substitute for those downstream gates.
5. An available private Extension is proven non-autoloaded. Receipt availability and admission completion do not start a release Workflow.
