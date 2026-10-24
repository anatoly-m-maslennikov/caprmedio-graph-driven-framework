---
subjects:
  governs: feature-boundary
  depends_on: []
version: 20
updated_at: 2026-10-24 03:32:22 +0400
relations:
  delivery_for:
  - CA-R-2154
  - CA-M-104
  - CA-R-1124
  - CA-R-1064
  - CA-R-1065
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-D-012
status: Active
content_role: Delivery
author: Anatoly Maslennikov
current_scope_unit: ACTION_ENGINE
type: Eng Decision
tier: 3
claim_target_scope_unit: ACTION_ENGINE
---
# Deliver the background-service lifecycle controller

Realize START_BACKGROUND_SERVICES through 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/START_BACKGROUND_SERVICES/start_background_services.py. Install the Tool **and** background_services.toml **in** the same selected release. Expose machine-readable describe, read-only status, **and** dry-run plus explicit apply forms of pause, resume, stop, start, **and** reload.

Give each service one .caprmedio_runtime/services/<service-id> directory for process state, lifecycle state, logs, budgets, circuit state, **and** dead-letter references. Keep queue **and** action state **in** its declared Runtime state root so lifecycle commands never delete accepted work. Stop **and** reload use cooperative bounded shutdown **and** preserve an active mutation **until** a declared recoverable boundary. Platform-specific supervision remains behind a replaceable adapter.

the registry includes COMMIT_AUTOMATION **only** **when** its accepted Delivery **and** installed launcher exist. Status for that service reports selected release, process identity, admission, queue count **and** bytes, current action **and** phase, pending state, Git lease, last success **and** failure, budget usage, circuit state, **and** dead-letter count.
