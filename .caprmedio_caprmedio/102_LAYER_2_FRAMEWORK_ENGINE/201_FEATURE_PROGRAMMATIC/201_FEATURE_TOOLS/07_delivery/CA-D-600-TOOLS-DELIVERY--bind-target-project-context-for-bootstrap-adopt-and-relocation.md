---
atom_id: CA-D-600
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Target Project context"
  depends_on: [Tool, Project, Project Structure, Settings, Registry]
relations:
  delivery_for: [CA-R-1904, CA-R-1906, CA-R-1907, CA-M-361]
---
# Summary

Bind target-Project context for bootstrap, adopt and relocation

## Scope

One declared target Project identity and its admissible control inputs.

## Claim

the INSTALL_TOOLS facade **must** retain a content-addressed target context for every bootstrap, adoption or relocation and **must not** invent an Operator, target root, control child, settings, Project Structure or registry.

## Details

`.caprmedio_runtime/installation/contexts/<target_project_context_sha256>.toml` has `schema_version = 1`, `mode`, `target_project_identity`, `control_child_relpath`, `settings_sha256`, `project_structure_sha256`, `registry_sha256`, `repository_identity`, `root_locator` and optional `relocates_context_sha256`. `mode` is exactly `bootstrap` or `adopt`; a non-git Project records `repository_identity = false`, while a repository may hold two contexts only when their target identities and control children are distinct.

The digest is calculated from canonical UTF-8 TOML bytes excluding its own digest field. Relocation creates a new context linked to the prior context after validating the same declared Project identity and current controls; it does not reuse an absolute checkout path as identity. Missing, ambiguous, changed or non-Project inputs refuse before runtime state is written.
