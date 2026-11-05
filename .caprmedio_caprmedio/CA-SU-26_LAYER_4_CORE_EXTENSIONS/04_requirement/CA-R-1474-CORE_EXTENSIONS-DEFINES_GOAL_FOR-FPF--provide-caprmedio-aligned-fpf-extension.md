---
atom_id: CA-R-1474
ref_id: CA-R-1474
container:
  scope_unit: CA-SU-26
role: Requirement
form: Goal
topics:
  main_subject: Subject/caprmedio/Extension//FPF
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
tier: 1
status: Active
version: 14
updated_at: 2026-10-27 19:59:55 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: CORE_EXTENSIONS
author: Anatoly Maslennikov
---
# Provide a CAPRMEDIO-aligned FPF Extension

FPF **must** provide an optional CAPRMEDIO Extension that installs one directly invokable project-local `fpf` Skill, conforms **to** the current Applicable Methodology **and** Project Configuration, **and** consumes canonical Tools through MCP **without** requiring a separate `ca` wrapper **or** modifying Core Meta-Model authority.
