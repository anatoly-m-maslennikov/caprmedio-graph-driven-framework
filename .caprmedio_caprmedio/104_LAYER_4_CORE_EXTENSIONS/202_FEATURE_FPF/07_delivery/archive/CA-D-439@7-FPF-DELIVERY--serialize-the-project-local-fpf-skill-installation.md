---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: FPF
  depends_on:
  - Skill
  - Extension Candidate
  - Subject/Engineering/Carrier
version: 7
updated_at: 2026-10-24 05:34:30 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Delivery
current_scope_unit: CORE_EXTENSIONS
status: Archived
author: Anatoly Maslennikov
atom_id: CA-D-439@7
type: Eng Decision
tier: 1
---
# Serialize the project-local FPF Skill installation

the activated Codex-facing FPF Skill **must** use project-local installation path `.agents/skills/fpf/`, package identity `fpf`, **and** direct invocation `$fpf`; no `ca` Skill, `ca` wrapper, user-global FPF mutation, **or** alternate Skill identity belongs **to** this Extension installation.
