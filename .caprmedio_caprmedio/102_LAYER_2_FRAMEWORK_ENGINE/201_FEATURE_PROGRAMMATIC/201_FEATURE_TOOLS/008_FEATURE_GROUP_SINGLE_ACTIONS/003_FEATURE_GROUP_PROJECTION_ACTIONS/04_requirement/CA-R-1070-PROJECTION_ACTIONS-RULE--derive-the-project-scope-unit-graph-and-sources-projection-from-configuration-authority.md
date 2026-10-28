---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
version: 24
updated_at: 2026-10-27 19:59:50 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
atom_id: CA-R-1070
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: PROJECTION_ACTIONS
type: Rule
tier: 1
claim_target_scope_unit: PROJECTION_ACTIONS
---
# Derive the Project Scope Unit Graph and Sources Projection from Configuration Authority

the Project Scope Unit Graph generator **must** use the authoritative Project Structure Artifact under CA-R-1483, CA-R-1484, **and** CA-D-440 as the source of accepted Scope Unit declarations **and** concrete bindings.

- Project Atoms, actual Directory Carriers, Settings, **and** Journal evidence **may** supply observations **and** checks against those declarations; they **must not** independently redefine them.
- a generated Graph **or** Sources Projection **must not** become Project Structure authority, select settings, **or** become a semantic input **to** its own generation.
- show a declared Scope Unit even **when** its folder **or** active Goal is absent. report observed undeclared folders **and** mismatches separately **without** accepting them as declarations.
- **if** the Project Structure Artifact is missing **or** invalid, report the unresolved authority; do **not** claim that an observed folder graph reconstructs accepted Project Structure.
