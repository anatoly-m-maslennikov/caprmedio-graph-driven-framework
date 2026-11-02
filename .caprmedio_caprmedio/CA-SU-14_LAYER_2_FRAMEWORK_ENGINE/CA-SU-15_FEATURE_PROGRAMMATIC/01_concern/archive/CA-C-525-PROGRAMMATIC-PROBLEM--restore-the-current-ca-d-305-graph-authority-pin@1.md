---
atom_id: CA-C-525
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-D-305]
version: 1
updated_at: "2026-10-20 15:30:14 +0400"
---
# Summary

Restore the current CA-D-305 graph-authority pin

## Concern

Complete-carrier validation is blocked by a stale CA-D-305 source binding in the validator's graph_authority.json. This is a confirmed current source-level Problem, not a claim that CA-D-305 itself is invalid or that deployed MCP creation has been reproduced as failing.

## Evidences

On 2026-10-20 the unchanged prepare_create_atom_revision preflight stopped before admission with `required source is unreadable, changed, or inactive`. Passive traceback inspection identified CA-D-305. The manifest at 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/graph_authority.json pins v12 / 06c141a93b14965614f93f88e522f21ec73790571676cc65e98265a310f447b5 under METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery; that exact pinned carrier path is absent. The current Active carrier is METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/07_delivery/CA-D-305-PROJECT_CONFIGURATION-CORE--carry-projected-atoms-without-new-identity.md, v16 / 7b1c4f96426e7907c90e5a949b037f26f39458fd769ed04e2b451a16376cdd39.

Current source inspection and the five-day audit are retained in .caprmedio_tmp/mcp-audit-20261020/{current-observations.md,report.md}. Existing C221/C443/C444/C521/C523 were reviewed and do not identify this graph-authority pin mismatch. C521 is a resolved historical selected-route private-source binding Problem, not proof of this validator's current source admission.

## Blast radius

The observed preflight cannot establish complete-carrier validity for the proposed relation-bearing Task. Other paths and deployed impact remain unverified; no pin, source or implementation was repaired. Reconcile the validator with applicable current authority and verify the affected behavior on isolated fixtures. Do not relocate or weaken the governed source merely to satisfy the stale manifest.
