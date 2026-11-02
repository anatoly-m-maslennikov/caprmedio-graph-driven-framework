---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
version: 23
updated_at: 2026-10-29 09:55:37 +0400
relations:
  depends_on:
  - CA-D-311
  - CA-R-1750
atom_id: CA-D-398@23
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Encode configuration surfaces **in** owning Atoms

## Claim scope

configuration surfaces carried by their owning Atoms.

## Claim

An owning Atom may carry its explicitly defined machine-readable Properties in YAML frontmatter. Its RMED Claim remains in Markdown, with an optional R-only nested Formal claim; frontmatter is not a second Claim or independent source. legacy `project_scope_unit_graph` **or** `project_graph_state` YAML maps **may** be read as migration evidence; they **must not** own current Scope Unit declarations, paths, Name/order values, Project identity, Atom prefix, **or** selected Authority Modes. Project initialization inputs belong **to** Project Settings; instance defaults belong **to** Framework Instance Settings; unit declarations **and** explicit unit overrides belong **to** Project Structure. this format does **not** require creation **or** consumption of a structural Projection.

## Details
