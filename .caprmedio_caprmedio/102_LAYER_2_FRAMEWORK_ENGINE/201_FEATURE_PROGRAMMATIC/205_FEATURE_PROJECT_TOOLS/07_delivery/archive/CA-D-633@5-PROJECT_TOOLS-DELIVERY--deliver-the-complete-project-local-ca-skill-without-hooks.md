---
atom_id: CA-D-633@5
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Subject/Engineering/Release Version/Project-Local Skill Delivery
  depends_on:
  - Subject/Engineering/Release Version/Project-Local Skill Delivery
  - Skill
  - Subject/Engineering/Runtime
  - Project Configuration
relations:
  delivery_for:
  - CA-M-332
type: Eng Decision
tier: 3
---
# Summary

Deliver the complete project-local ca Skill without hooks

## Scope

The canonical ca Skill payload and its project-local Codex target in direct Release Version delivery.

## Claim

Direct Release Version delivery **must** install the complete canonical `102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/` directory at the selected Project's `.agents/skills/ca/`, including `SKILL.md`, `agents/openai.yaml`, and every declared resource, while retaining its `caprmedio` Project-MCP dependency and changing no host hooks or global configuration.

## Details

Prepare and verify the complete Skill payload with the local runtime package before clearing any installed target; install those same prepared bytes and independently compare actual destination paths, bytes and modes. A failed or uncertain copy retains its truthful source-effect result and does not permit automatic replay. The installed Skill belongs to the same local release delivery as the installed Project runtime. Release Version does not register MCP, change Codex permissions, change Codex or Git Hook carriers or hook configuration, or alter unrelated Skills or user directories. Engine runtime `--without-hooks` does not substitute for complete Skill delivery. This Delivery defines neither a candidate-snapshot carrier nor a full-suite gate or N+1 Skill-selection protocol. Plain Journal append/read records supplied actual observations without baseline, prior-history, chain, validation, receipt, deduplication, retry or recovery prerequisites; neither a log entry nor logging failure certifies or changes the observed Skill installation outcome.
