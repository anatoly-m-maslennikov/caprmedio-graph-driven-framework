---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "OPERATOR_PROMPTS/Goal"
  depends_on:
    - "PROMPTS"
    - "Operator"
version: 2
updated_at: 2026-10-23 03:17:34 +0400
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1602@2
status: Archived
---
# Request Operator Decisions and Input

OPERATOR_PROMPTS **must** own user-facing prompts that request an Operator decision, authorization, clarification, **or** input. They **must not** be treated as agent-executable Action implementations **or** as substitutes for the Operator's response.
