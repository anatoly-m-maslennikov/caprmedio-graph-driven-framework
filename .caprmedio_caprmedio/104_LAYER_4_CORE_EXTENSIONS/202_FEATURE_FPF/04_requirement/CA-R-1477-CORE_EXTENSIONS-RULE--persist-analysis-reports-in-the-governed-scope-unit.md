---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Output Publication
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Analysis/Type: Analysis Report'
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
atom_id: CA-R-1477
type: Rule
tier: 1
---
# Persist Analysis Reports in the governed Scope Unit

**when** an executable FPF analysis produces a persistent Project artifact, FPF **must** by default create a correctly formatted `CA-A` Analysis Report Carrier **in** the `02_analysis/` Folder of the narrowest resolved Scope Unit that **contains** the analyzed Claim Scope; routing-only work **must not** persist a report, an explicit non-persistent request **must** remain non-persistent, **and** unresolved identity, admission, topology, **or** placement **must** stop persistence rather than fall back **to** an ad hoc report Folder.
