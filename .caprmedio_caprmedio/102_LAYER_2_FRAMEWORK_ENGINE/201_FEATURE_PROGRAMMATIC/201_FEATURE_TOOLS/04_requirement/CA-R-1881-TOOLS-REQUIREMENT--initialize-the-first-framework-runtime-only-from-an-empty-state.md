---
atom_id: CA-R-1881
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-09 16:59:40 +0400"
subjects:
  governs: "Tool/INSTALL_TOOLS/First-initialization variant"
  depends_on: [Tool, Framework Package, Runtime, Skill, Docker Image, Journal, Operator]
relations:
  relates_to: [CA-R-1873, CA-R-1877, CA-R-1878, CA-R-1879, CA-R-1525, CA-R-1720]
---
# Summary

Initialize the first Framework runtime only from an empty state

## Scope

One explicit initial installation of a reusable Framework package and an isolated target-Project runtime, including bootstrap and adoption without treating the checkout as runtime payload.

## Claim

the INSTALL_TOOLS first-initialization variant **must** create the first active target-Project runtime **only** when that runtime installation boundary is empty, even when an existing Project is adopted, and **must not** execute Framework code from the installer checkout. It **must** admit **=1** complete content-addressed package, current package selector, target-Project context, state generation, hook-free project-local `ca` Skill, and independently verified image proof bound to the same sealed package frontier; it records the actual installation Action Run through the canonical Work Journal.

## Details

An existing runtime selector, retained runtime release, project-local Skill, file, symlink, non-directory, nonempty runtime boundary, unsafe process, partial runtime state, changed source, unknown pinned revision, stale or unproven canonical compiled Methodology, incomplete package, mismatched image or unavailable permission **must** stop before overwrite. Existing Project metadata may be adopted only when settings, Project Structure, registry, root and control child are explicitly supplied and verified; it does not relax the empty-runtime condition. The selected package contains the entire `102_FRAMEWORK_ENGINE/`, sealed `pyproject.toml`, `uv.lock` and `version.toml`, admitted defaults, `ca` payload, active Methodology source catalog and required support carriers. The reusable package resides at `.caprmedio_install/releases/<package_manifest_sha256>/`; an admitted `.caprmedio_install/current.toml` package selector may already exist. The target Project receives `.caprmedio_runtime/installation/current.toml`, which binds that package, canonical target-Project context and an incrementing state generation. Runtime state and environment execute package-owned bytes through `uv run --locked --no-sync --no-env-file`; they never select the installer checkout. A private producer stages only under `.caprmedio_tmp/release_candidates/<run_id>/`, seals the package, runs the existing complete Full Gate and builds/canaries the exact sealed bytes before any package or target selector publication. Before selector publication, every failure is blocked or partial and leaves no active first runtime. After actual selector publication, a missing canonical terminal Journal receipt is `recording_pending`: the actual selected bytes are reopened and retained, no rollback or replay occurs, and recovery may append only the missing terminal Event for the original started Run. This initial installation is explicitly Operator-invoked; it is neither a selected-workflow route nor an N-to-N+1 Release Version promotion. It preserves authoring sources, settings, Journals, unrelated Skills, existing images and legacy state.
