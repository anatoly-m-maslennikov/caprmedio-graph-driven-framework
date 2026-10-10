---
atom_id: CA-D-600
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 05:17:00 +0400"
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

`.caprmedio_runtime/installation/contexts/<target_project_context_sha256>.toml` has `schema_version = 2`, `mode`, `target_project_identity`, `control_child_relpath`, `settings_sha256`, `project_structure_sha256`, `registry_sha256`, `framework_instance_settings_sha256`, `source_catalog_sha256`, `methodology_source_identities`, `repository_identity`, `root_locator` and optional `relocates_context_sha256`. `mode` is exactly `bootstrap` or `adopt`; a non-git Project records `repository_identity = false`, while a repository may hold two contexts only when their target identities and control children are distinct. The source identities form a nonempty, uniquely sorted array of exact admitted catalog identities, not a parallel source authority.

The digest is calculated from canonical UTF-8 TOML bytes excluding its own digest field. Relocation creates a new context linked to the prior context after validating the same declared Project identity and current controls; it does not reuse an absolute checkout path as identity. Missing, ambiguous, changed or non-Project inputs refuse before runtime state is written. `settings_sha256` binds Project Settings only; the separate Framework Instance Settings hash binds the canonical carrier required by CA-D-359-CORE_META_MODEL--bind-framework-settings-to-its-authoritative-toml-carrier. Package availability is not target applicability: reopen the entire catalog and resolve this target's choice before producing the context. Core Methodology and declared support are included; enabled Extension identity/revision pairs and the optional explicit Configuration selection follow CA-D-561-TOOLS-DELIVERY--bind-release-source-compilation-and-package-carriers. No unselected releasing-Project Configuration is added. Every selected identity must have exact admitted package members.

### Candidate context and adoption

Binding the context reads the declared target controls and actual package evidence; it is not installation permission. `bootstrap` requires no active native or legacy runtime or installed ca. `adopt` can prepare a context beside existing state; before any replacement, the publisher must independently reopen that exact selected state and its migration/quiescence proof. Adoption never treats arbitrary existing files as an admitted runtime.

The shared installation lock owns an immutable writer for `contexts/<digest>.toml`. The writer validates the closed canonical schema, recomputes the self-excluding digest, reopens the exact Project Settings, Framework Instance Settings, structure, registry and admitted catalog bytes, recomputes their selected identities, and writes only the exact digest-named carrier. Existing identical bytes can be reused; conflicting or aliased carriers refuse. A retained prospective context alone does not activate a generation, overwrite configuration or authorize deletion. The same physical context reader is used before staging and after installation. A prior schema-1 context is historical evidence, not a schema-2 context with invented settings or selection values.
