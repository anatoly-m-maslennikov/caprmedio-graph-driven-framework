---
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Atom
version: 22
updated_at: 2026-10-24 05:56:25 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
  - CA-R-1070
atom_id: CA-M-149@22
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: PROJECTION_ACTIONS
type: Eng Decision
tier: 2
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
