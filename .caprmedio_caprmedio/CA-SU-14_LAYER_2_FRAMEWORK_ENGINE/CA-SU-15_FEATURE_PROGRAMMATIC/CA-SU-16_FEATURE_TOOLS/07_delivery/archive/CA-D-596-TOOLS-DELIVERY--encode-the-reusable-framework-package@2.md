---
atom_id: CA-D-596
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 22:00:55 +0400"
subjects:
  governs: "Framework Installation contribution/Reusable package carrier"
  depends_on: [Tool, Framework Package, Manifest, Methodology, Skill, Extension]
relations:
  delivery_for: [CA-R-1902, CA-R-1903, CA-M-359]
---
# Summary

Encode the reusable Framework package

## Scope

The immutable package tree that is reusable by more than one selected target Project.

## Claim

the INSTALL_TOOLS facade **must** deliver **=1** manifest-addressed reusable package at `.caprmedio_install/releases/<package_manifest_sha256>/` and **must not** use an installer checkout as a package carrier.

## Details

`manifest.toml` has exactly `schema_version = 1`, `package = "caprmedio-framework"`, `framework_version`, `version_toml_sha256`, `source_catalog_sha256` and ordered `[[files]]` rows with exactly `path`, `sha256`, `mode` and `role`. `manifest.toml` itself is explicitly excluded from `[[files]]`, so its exact bytes SHA-256 can name the release directory without a self hash. The tree contains the complete `102_FRAMEWORK_ENGINE/`, exact `pyproject.toml`, `uv.lock` and `version.toml`, admitted defaults, `SKILLS/ca/`, active Methodology source catalog and its declared support. A candidate-release digest alone is not the version carrier. It also contains `catalog.toml`, whose every support-member path is enumerable and closed. Catalog records list only explicitly admitted distributable Core, optional extension or configuration sources with identity, immutable revision, digest, admission status and visibility; no private personal configuration, Operator registry or runtime state is shipped. An admitted optional entry is available package content, **not** an instruction to autoload it for a target Project.

Every delivered member is a regular package-contained carrier named by a manifest row. Secrets, host environment files, checkout paths, temporary state, mutable tags, generated target state and undeclared extensions are excluded. The package digest is the SHA-256 of exact `manifest.toml` bytes; a package directory whose name, rows, bytes or modes disagree is not reusable.

Actual catalog admission proof members belong at `admissions/<receipt_sha256>.json`, with manifest role `source-admission`. Every referenced receipt is included exactly once as a package member; admission records remain separate from the admitted source trees, avoiding a receipt/source self-hash cycle. Receipt presence grants no test pass, image admission, installation or release execution.
