---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: FPF
  depends_on:
  - Subject/Engineering/Tool
  - Subject/Engineering/MCP
  - Subject/Engineering/Skill
version: 10
updated_at: 2026-10-24 11:58:20 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: CORE_EXTENSIONS
status: Archived
author: Anatoly Maslennikov
atom_id: CA-R-1479@10
type: Rule
tier: 1
---
# Preserve the Tool-MCP-Skill authority chain

the FPF Extension **must** realize deterministic behavior first **in** canonical project-local Tools, expose admitted Tool contracts through the project-local provider-neutral MCP service **without** changing their meaning, **and** make the `fpf` Skill a thin direct consumer of that MCP surface; the Skill **must not** duplicate Tool mechanics, MCP transport, lifecycle control, **or** a `ca` routing wrapper, **and** Consumer-owned Demands **must not** be admitted **before** they target **`=1`** identified current MCP Implementation result.
