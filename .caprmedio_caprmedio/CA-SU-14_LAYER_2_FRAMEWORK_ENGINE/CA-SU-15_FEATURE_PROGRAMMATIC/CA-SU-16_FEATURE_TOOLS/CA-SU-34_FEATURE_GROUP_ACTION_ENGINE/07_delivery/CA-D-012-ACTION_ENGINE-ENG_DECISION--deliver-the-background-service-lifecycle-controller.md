---
atom_id: CA-D-012
ref_id: CA-D-012
container:
  scope_unit: CA-SU-34
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
tier: 3
relations:
  delivery_for:
  - CA-R-2154
  - CA-M-104
  - CA-R-1124
  - CA-R-1064
  - CA-R-1065
status: Active
version: 28
updated_at: 2026-11-02 19:46:47 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: ACTION_ENGINE
claim_target_scope_unit: ACTION_ENGINE
---
# Deliver the background-service lifecycle controller

Realize START_BACKGROUND_SERVICES through LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/START_BACKGROUND_SERVICES/start_background_services.py. Install the Tool **and** background_services.toml **in** the same selected release. Expose machine-readable describe, read-only status, **and** dry-run plus explicit apply forms of pause, resume, stop, start, **and** reload.

Give each service one .caprmedio_runtime/services/<service-id> directory for process state, lifecycle state, logs, budgets, circuit state, **and** dead-letter references. Keep queue **and** action state **in** its declared Runtime state root so lifecycle commands never delete accepted work. Stop **and** reload use cooperative bounded shutdown **and** preserve an active mutation **until** a declared recoverable boundary. Platform-specific supervision remains behind a replaceable adapter.

the registry includes COMMIT_AUTOMATION **only** **when** its accepted Delivery **and** installed launcher exist. Status for that service reports selected release, process identity, admission, queue count **and** bytes, current action **and** phase, pending state, Git lease, last success **and** failure, budget usage, circuit state, **and** dead-letter count.
