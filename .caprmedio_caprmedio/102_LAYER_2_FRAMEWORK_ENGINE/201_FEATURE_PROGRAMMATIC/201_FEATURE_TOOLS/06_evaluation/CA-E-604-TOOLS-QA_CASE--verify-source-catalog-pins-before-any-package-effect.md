---
atom_id: CA-E-604
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 10:17:20 +0400"
subjects:
  governs: "Framework Installation contribution/Source catalog refusal"
  depends_on: [Tool, Framework Package, Methodology, Extension, Configuration, Projection]
relations:
  evaluation_for: [CA-R-1908, CA-M-359, CA-D-602]
---
# Summary

Verify source catalog pins before any package effect

## Scope

the unknown-revision, binding-projection and catalog-binding refusal boundary.

## Claim

the QA case **must** prove that an unknown, mutable, duplicate or mismatched catalog revision, or an incomplete or stale binding-projection frontier, fails **before** candidate, image, package selector or target runtime effect.

## Details

1. Fixtures alter each catalog field separately and snapshot effect roots before and after refusal.
2. Receipt fixtures cover a missing regular carrier, a symlink, altered bytes, a malformed or noncanonical record, a wrong source-snapshot checksum and a descriptor that differs from its catalog record. A coherent digest string alone is not admission evidence.
3. Source-admission fixtures use a real pre-catalog snapshot and an explicitly admitted Operator command. Missing admission or an invocation bound to a different snapshot produces no catalog or receipt write. Matching admission retains actual receipt bytes and catalog references; reopening verifies them before packaging.
4. Binding fixtures vary Atom IDs, Versions, original paths and raw source hashes without relying on a fixed Tool list. They prove that every explicitly selected package-owned binding has one exact `binding_atoms` pin, one canonical projected Carrier, one covering `kind = "binding"` descriptor and retained admission evidence. Omitted required bindings, extra projections, duplicate Tool/action claims, support-role substitution, Configuration classification, noncanonical projection metadata or inverse-source mismatch refuse before packaging. An empty frontier is valid only for a sealed source selection with no package-owned Tool binding.
5. Positive downstream evidence proves the identical catalog digest in manifest, candidate seal, Full Gate/image proof, `.caprmedio_install/current.toml` and target result. A focused admission or package test does not substitute for those downstream gates.
6. An available private Extension is proven non-autoloaded. A binding descriptor is separately proven non-selectable by Extension or `[methodology.configuration]` settings. Receipt availability, binding discovery and admission completion do not start a release Workflow or direct Action.
