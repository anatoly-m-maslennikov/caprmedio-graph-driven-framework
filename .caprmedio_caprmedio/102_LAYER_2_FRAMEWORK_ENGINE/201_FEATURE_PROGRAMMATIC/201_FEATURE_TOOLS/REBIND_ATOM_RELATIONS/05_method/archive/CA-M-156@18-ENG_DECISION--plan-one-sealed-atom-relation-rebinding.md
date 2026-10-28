---
subjects:
  governs: Subject/Graph Node/Implementation/Code/Tool//REBIND_ATOM_RELATIONS
  depends_on: []
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations:
  method_for:
  - CA-R-1049
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-156@18
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eng Decision
tier: 1
---
# Plan one sealed Atom relation rebinding

For one sealed request, resolve the exact active source carrier, verify its digest **and** version, validate **only** the explicitly named direct relation rewrites **or** removals, **and** pass the observed bytes **and** sealed request **to** a pure planner. The planner preserves filename, body, **and** undeclared frontmatter, advances version once, sets the supplied timestamp, derives the result digest, **and** returns one `UPDATE` receipt.

Dry run is mutation-free. `--apply` is accepted **only** through authorized project-local MCP delegation with the sealed Initiative action envelope. The authorized effect atomically replaces **only** the source carrier **and** obtains durable `COMMIT_TRIGGER` intake acknowledgement **before** MCP reports success. It never infers a relation meaning, target mapping, backup, Journal event, staging change, **or** Git action.
