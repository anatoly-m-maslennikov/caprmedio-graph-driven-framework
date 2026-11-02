---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/Engineering/Extension
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Concern'
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom.Subjects
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/Continuant/Carrier
version: 13
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: CORE_EXTENSIONS
status: Archived
author: Anatoly Maslennikov
atom_id: CA-R-1478@13
type: Rule
tier: 1
---
# Create proper Concern Atoms on explicit request

**when** the Operator explicitly asks FPF **to** persist a concern, FPF **must** create one **or** more independently replaceable `CA-C` Concern Atoms that classify **every** concern with an applicable registered Concern Type, give **every** Atom **`=1`** primary Claim **and** **`=1`** direct governed Subject, serialize current CCE frontmatter **and** Carrier naming, **and** place it **in** the `01_concern/` Folder of the narrowest resolved owning Scope Unit; ordinary questions, ideas, **and** analysis **must not** become persistent Concern authority **without** that explicit request.
