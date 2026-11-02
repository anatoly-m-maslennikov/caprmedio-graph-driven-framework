---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Concern'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Subjects
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Carrier
version: 15
updated_at: 2026-10-27 19:59:55 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: CORE_EXTENSIONS
status: Active
author: Anatoly Maslennikov
atom_id: CA-R-1478
type: Rule
tier: 1
---
# Create proper Concern Atoms on explicit request

**when** the Operator explicitly asks FPF **to** persist a concern, FPF **must** create one **or** more independently replaceable `CA-C` Concern Atoms that classify **every** concern with an applicable registered Concern Type, give **every** Atom **`=1`** primary Claim **and** **`=1`** direct governed Subject, serialize current CCE frontmatter **and** Carrier naming, **and** place it **in** the `01_concern/` Folder of the narrowest resolved owning Scope Unit; ordinary questions, ideas, **and** analysis **must not** become persistent Concern authority **without** that explicit request.
