---
subjects:
  governs: Project Scope Unit Graph Projection/validation
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Atom
version: 20
updated_at: 2026-10-24 01:18:03 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1070
atom_id: CA-E-168@20
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
---
# Keep operator settings out of the Scope Unit Graph generator

## Test case

change **`=1`** initialization value **in** the authoritative Project Settings Artifact **and** **`=1`** Authority Mode selection **in** Framework Instance Settings, while leaving Project Atoms unchanged. rebuild the Project Scope Unit Graph Projections.

## Acceptance criteria

the generator uses the appropriate Settings revision for **every** exposed value **without** a Project-specific effective-value catalog **or** an Atom-owned current settings selection. output bindings identify the changed Settings Artifacts; the generator **and** the Projection **must not** become their authority.
