---
atom_id: CA-P-2374@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 52
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 6
updated_at: 2026-10-24 08:10:13 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
tier: 3
---
# Summary

Align direct Subject lookup rules

## Objective

Amend only R863, M370, E301, D424, O046, R1936, M376 and D625 for the approved direct read-only Subject lookup. Preserve CLI and Session-based behavior, exact previous bytes and all mutation admission. No Session or Journal is required for this bounded direct observation.

## Details

The independently accepted CA-P-2369 proposal is the input to this rule packet. Stage-specific work gates remain in the Epic; they are not Artifact depends_on Relations or whole-Task start blockers.

Estimated own work: up to 15 minutes; split before exceeding this bound. Follow the independently reviewed lookup-exposure proposal. Root owns integration and Git. Preserve unrelated changes. Core Subject migration, ordinary content migration, broader connector rebuilding and live publication remain outside this Task.

### Acceptance — 2026-10-14

Independent source review passed for all eight rules. Exact predecessor bytes, unchanged Summary/identity/Subjects and Version+1 were verified. The only review correction removed an unsupported Workflow association from D424; its final v14 SHA-256 is `1c956aecac1b3cfb55b90cf32aa03ea44ca029289e0e1ab49ecf6d946237564a`. The direct exception preserves generic Session and mutation behavior. This is rule acceptance only; implementation, affected pin refresh and MCP verification remain in CA-P-2375–2377.

### Definition of Done

Independent review accepts the eight-source packet, exact archives, closed logical request/result, selected-source/currentness checks and no broader exemptions.

