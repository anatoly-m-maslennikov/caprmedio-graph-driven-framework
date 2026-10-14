---
atom_id: CA-P-2377
content_role: Plan
type: Plan
label: Task
work_sequence_number: 55
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Plan]
version: 2
updated_at: "2026-10-14 10:24:40 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Verify direct Subject lookup MCP

## Objective

Independently test the registered provider through a real MCP transport with actual source fixtures and no fabricated freshness. Check selected PRMEDO behavior, currentness and no writes. Record installed-runtime verification separately.

## Details

Prepare fixtures independently; production edits require the accepted CA-P-2374 rule packet, and final protocol execution requires the ready CA-P-2375/2376 implementation. These are stage-specific gates, not a whole-Task start BLOCKS relation or an Artifact depends_on relation.

Estimated own work: up to 15 minutes; split before exceeding this bound. Follow the independently reviewed lookup-exposure proposal. Root owns integration and Git. Preserve unrelated changes. Core Subject migration, ordinary content migration, broader connector rebuilding and live publication remain outside this Task.

### Acceptance — 2026-10-14

All 10 real production-server MCP transport tests passed on final reviewed reader and provider code in 2.416 seconds. Actual source/grammar fixtures, strict inputs, no-write inventories, source drift and selected-source refusals were checked without mocked freshness. Adjacent registry/descriptor/server tests passed 26 of 30; four unchanged O199 tests fail before invocation because their old fixture file is missing. That unrelated failure is not waived. Installed Docker activation and connected-service acceptance remain separate and unperformed.

Implementation: commit `2a40cb4c8`. [Local completion receipt](../../../../_projection/core-entity-review/stage2/tools-first/direct-subject-lookup-local-completion.md). No Core Subject migration or ordinary content update was performed.

### Definition of Done

Real tools/list and tools/call pass with truthful pins and no Session/Journal effects on success and refusal. Report unavailable installed activation rather than claiming it.

