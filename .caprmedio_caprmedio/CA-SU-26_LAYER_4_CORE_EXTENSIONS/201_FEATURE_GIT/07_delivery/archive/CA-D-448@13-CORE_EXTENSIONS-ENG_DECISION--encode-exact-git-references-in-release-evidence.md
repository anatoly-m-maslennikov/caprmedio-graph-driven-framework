---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: Subject/Graph Node/Carrier/Git Commit
  depends_on:
  - Subject/Graph Node/Carrier
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Product/Extension
version: 13
updated_at: 2026-10-27 06:04:45 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
content_role: Delivery
current_scope_unit: CORE_EXTENSIONS
status: Archived
author: Anatoly Maslennikov
atom_id: CA-D-448@13
type: Eng Decision
tier: 1
---
# Encode exact Git references in release evidence

**when** the GIT Extension supplies the Git binding for a selected release candidate, its evidence references **must** identify the repository **and** the full immutable commit object ID representing the checked content.

- a branch name, HEAD, **or** a tag name alone is **not** an exact Revision reference. retain a selected tag as a label **only** alongside its resolved commit ID.
- a commit ID **must not** represent uncommitted content as evaluated committed content; material working-tree differences **must** remain explicit under the applicable candidate binding.
- a release manifest **must** bind the released candidate **to** that exact reference; a later branch movement does **not** rebind earlier evidence.
- use the existing proof-frontier **and** Journal Carriers. do **not** create a second authoritative release log **or** redefine the generic Journal schema.

this Git-specific encoding does **not** select a branch strategy, require Git outside the selected Extension capability, **or** authorize commit, merge, tag, push, **or** publication.
