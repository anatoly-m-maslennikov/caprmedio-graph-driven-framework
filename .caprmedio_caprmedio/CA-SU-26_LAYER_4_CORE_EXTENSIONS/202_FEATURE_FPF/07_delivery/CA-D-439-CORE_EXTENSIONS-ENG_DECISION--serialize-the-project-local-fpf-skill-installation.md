---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout
  - Subject/caprmedio/Extension//FPF
  - Subject/CAPRMEDIO/Carrier
version: 16
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Delivery
current_scope_unit: CORE_EXTENSIONS
status: Active
author: Anatoly Maslennikov
atom_id: CA-D-439
type: Eng Decision
tier: 1
---
# Serialize the project-local FPF Skill installation

the activated Codex-facing FPF Skill **must** use project-local installation path `.agents/skills/fpf/`, package identity `fpf`, **and** direct invocation `$fpf`; no `ca` Skill, `ca` wrapper, user-global FPF mutation, **or** alternate Skill identity belongs **to** this Extension installation.
