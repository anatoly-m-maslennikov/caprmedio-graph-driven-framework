---
atom_id: CA-C-464
content_role: Concern
type: Problem
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 01:47:30 +0400
subjects:
  governs: Subject/Engineering/MCP/Status Route Fixture Compatibility
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Engineering/Manifest
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
relations:
  concern_about: [CA-P-1695, CA-P-1692]
---
# Summary

Record obsolete status-route golden inputs

## Concern

Two existing MCP fixtures still submit route_input for Change Atom Status while current admitted lifecycle input requires actual target and status. P1692's combined twenty-seven development tests failed these two old cases; its seven new loader and eight source-admission tests passed. P1695 repairs only actual fixture inputs and preserves current source/status/preview guards; no production bypass or weakened assertion is admitted.

## Evidences

test_every_selected_route_forwards_one_mutation_free_preview patches the loader before its obsolete status request. test_current_physical_manifest_freezes_original_thirteen_through_queue fails carrier-fields-invalid from unchanged APP preflight. The production manifest remains unchanged.

## Blast radius

MCP regression evidence for the already updated status route, not a new capability or actual queue/image proof.

## Resolution

P1695 corrects the disposable inputs without production changes or weakened assertions. Root ran all twelve MCP fixture tests in the permitted development worker, including both previously failing cases; all pass. Actual queue-process/image proof remains separate.
