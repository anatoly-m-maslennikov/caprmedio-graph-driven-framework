---
atom_id: CA-D-424
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: delivery
subjects:
  governs: "Tool/ATOM_SEARCH/Carrier"
  depends_on:
    - "Tool/ATOM_SEARCH"
version: 8
updated_at: "2026-10-10 23:57:23 +0400"
relations: {"delivery_for":["CA-R-863"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Deliver ATOM_SEARCH Tool

## Scope

This Delivery carrier defines the public file-operation contract of the canonical `ATOM_SEARCH` wrapper under owner `TOOLS`. The `ATOM_SEARCH` folder is an artifact collection below `TOOLS`, not an independently registered Scope Unit. It retains the existing generic search interface and adds one small read-only, field-aware Subject lookup for already-correct Atom files. It does not define Core semantics, grammar adoption, migration decisions, source repair, graph publication, or a live MCP route.

## Claim

the `ATOM_SEARCH` Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/atom_search.py`; that Carrier realizes `CA-R-863` through the Action `CA-O-046`.

The delivered `ATOM_SEARCH` wrapper **must** support the existing `--under PATH` and `--lifecycle VALUE` filters and the following Subject lookup options:

- one `--subject VALUE` criterion per request;
- `--subject-field governs|depends_on|both` to select the flat Subject field;
- `--subject-match exact|prefix` for literal equality or delimiter-aware lexical prefix matching;
- repeatable `--content-role ROLE` values as an OR set within the valid-file filter, and `--scope-unit OWNER` as a conjunctive owner filter.

Each result **must** identify the source pin and exact occurrence: `atom_id`, `version`, `status`, `owner`, `relative_path`, `sha256`, `updated_at`, `field`, `index`, and `value`. `index` is the list index for `depends_on` and is null for the scalar `governs` field. Results are deterministic and path/field/index ordered. Malformed, unreadable, duplicate, or rejected selected files appear in a separate `diagnostics` collection; a valid empty match is returned as an empty result and is not a diagnostic. The lookup never infers ontology relations from text or from the pending grammar profile.

## Details

The request resolves the configured Project control root and an optional declared subtree before traversal. Existing path, filename, frontmatter, content, exact-selector, output-view, and lifecycle behavior remains available. Subject lookup reads only valid current Atom files with a canonical flat `subjects` block; invalid source paths, symlink targets, projections, malformed carriers, duplicate fields/values, and owner/path disagreements are rejected or diagnosed without widening selection. Prefix matching ends only at a declared Subject delimiter, so a value such as `Artifact/Atom` does not match `Artifact/Atomology`.

The output carries one source pin per occurrence and no inferred target or native graph edge. The wrapper is local and mutation-free: it performs no write, rename, repair, migration, Projection rebuild, history/Journal effect, or MCP invocation. No unsupported MCP delivery or live execution capability is claimed. CA-R-863 and CA-O-046 remain the governing Requirement and Action; CA-M-370 supplies the focused authoring method when that Method carrier is delivered.
