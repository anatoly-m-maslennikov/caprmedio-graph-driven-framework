---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Manage Installed Extensions"
  depends_on:
    - "Action"
    - "Extension"
    - "Artifact/Carrier"
    - "Artifact/Revision"
version: 3
updated_at: 2026-10-23 03:17:34 +0400
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
atom_id: CA-O-042@3
status: Archived
---
# Manage installed Extensions

Manage Installed Extensions **means** the reusable Action that produces one complete authorized Extension installation-state transition by exact source **and** version, **or** restoration of the complete prior installed state under CA-R-1152. its modeled boundary is the complete selected mutable-state transition; a partial application is **not** an independently accepted result.

## Applicable when

use this Action **when** one Extension **must** be installed, uninstalled, updated, **or** downgraded by exact declared source **and** version.

## Action

1. resolve the requested operation, Extension identity, exact source, exact package version, **and** current installed-state inventory.
2. verify that the selected source **and** version identify one package **and** compute the target installed-state inventory.
3. produce a complete transition plan with affected files, previous installed state, **and** rollback actions.
4. on explicit authorization, apply the unchanged plan atomically **and** restore the previous state **if** **any** operation fails.
5. report the resulting Extension identity, source, version, file inventory, **and** verification status.

## Outcome

one exact Extension lifecycle operation produces an attributable resulting installed state **or** restores the prior state completely.

## Failure or stop

stop **or** roll back on an unresolved source **or** version, identity mismatch, collision, incomplete plan, failed effect, **or** unverifiable resulting state.
