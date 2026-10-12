---
atom_id: CA-D-596
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 10:17:20 +0400"
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

Newly assembled packages use `manifest.toml` `schema_version = 2`, with exactly `package = "caprmedio-framework"`, `framework_version`, `version_toml_sha256`, `source_catalog_sha256`, closed ordered `binding_atoms` pins, and ordered `[[files]]` rows with exactly `path`, `sha256`, `mode` and `role`. Each `binding_atoms` member has exactly D561's `atom_id`, positive integer `version`, safe Project-relative `source_path`, and lowercase raw-source `sha256`; it is a sealed projection lineage pin, not an authoring Atom, Action grant, or target-selection input. `binding_atoms` is empty exactly when D561's eligible binding frontier is empty. `manifest.toml` itself is explicitly excluded from `[[files]]`, so its exact bytes SHA-256 can name the release directory without a self hash. The tree contains the complete `102_FRAMEWORK_ENGINE/`, exact `pyproject.toml`, `uv.lock` and `version.toml`, admitted defaults, `SKILLS/ca/`, active Methodology source catalog and its declared support. A candidate-release digest alone is not the version carrier. It also contains `catalog.toml`, whose every support-member path is enumerable and closed. Catalog records list only explicitly admitted distributable Core, optional extension or configuration sources with identity, immutable revision, digest, admission status and visibility; no private personal configuration, Operator registry or runtime state is shipped. An admitted optional entry is available package content, **not** an instruction to autoload it for a target Project.

`schema_version = 1` retains exactly its former manifest shape for historical read only: it has no `binding_atoms` field or `binding-projection` package role, cannot assemble a new package, and cannot supply a fallback for a schema-2 package. Catalog and package/current runtime selector schemas remain schema 1 and unchanged; their readers do not infer a manifest schema conversion.

Every delivered member is a regular package-contained carrier named by a manifest row. Secrets, host environment files, checkout paths, temporary state, mutable tags, generated target state and undeclared extensions are excluded. The package digest is the SHA-256 of exact `manifest.toml` bytes; a package directory whose name, rows, bytes or modes disagree is not reusable.

Actual catalog admission proof members belong at `admissions/<receipt_sha256>.json`, with manifest role `source-admission`. Every referenced receipt is included exactly once as a package member; admission records remain separate from the admitted source trees, avoiding a receipt/source self-hash cycle. Receipt presence grants no test pass, image admission, installation or release execution.
