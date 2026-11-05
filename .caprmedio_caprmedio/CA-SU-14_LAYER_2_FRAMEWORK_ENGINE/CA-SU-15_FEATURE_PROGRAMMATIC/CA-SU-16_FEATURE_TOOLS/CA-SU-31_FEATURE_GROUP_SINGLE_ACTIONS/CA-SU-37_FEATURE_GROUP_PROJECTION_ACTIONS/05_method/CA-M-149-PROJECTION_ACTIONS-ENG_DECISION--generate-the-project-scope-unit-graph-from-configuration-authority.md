---
atom_id: CA-M-149
ref_id: CA-M-149
container:
  scope_unit: CA-SU-37
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  dependencies:
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
tier: 2
relations:
  method_for:
  - CA-R-1070
status: Active
version: 27
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
author: Anatoly Maslennikov
current_scope_unit: PROJECTION_ACTIONS
claim_target_scope_unit: PROJECTION_ACTIONS
---
# Generate the Project Scope Unit Graph from Configuration Authority

**to** generate the Project Scope Unit Graph **and** Sources Projections:

- use the owning Project's authoritative Project Structure Artifact as the sole source of accepted Scope Unit declarations **and** concrete bindings.
- use Project Settings for Project identity **and** Framework Instance Settings for selected framework behavior, under their governing authority.
- preserve the distinction between accepted declarations, Atom Claims, Directory Carrier observations, **and** Journal evidence.
- derive the generated views deterministically from the selected source revisions **without** using previous generated views as authority **or** writing accepted declarations.
- keep Goal coverage, folder materialization, undeclared folders, **and** declaration mismatches visible as separate observations.
- **if** the required authoritative input is missing, invalid, **or** cannot be read completely, report incomplete coverage **and** do **not** claim a complete accepted Project Structure.
