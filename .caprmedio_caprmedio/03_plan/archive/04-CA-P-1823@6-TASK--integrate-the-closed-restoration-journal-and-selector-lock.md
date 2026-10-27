---
atom_id: CA-P-1823@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 6
updated_at: 2026-10-24 08:10:13 +0400
subjects:
  governs: Integrate the closed restoration Journal and selector lock
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Engineering/Tool
  - Framework Package
  - Docker Image
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
relations:
  is_decomposition_of:
  - CA-P-1820
  blocks:
  - CA-P-1623
tier: 3
---
# Summary

Integrate the closed restoration Journal and selector lock

## Objective

Admit only the new O187 direct Action alongside unchanged O180 and add one shared selector publication lock protecting restoration and normal promotion.

## Details

The Operator explicitly approved rebuilding the missing selected image from verified retained N and registering its verified image digest. Preserve N's package, Version, public ca Skill, original proof and historical Journal. N21 remains unknown and is not replayed. No release gate is waived. Root owns Git, source admission and serialized runtime effects; independent workers own their assigned source scopes.

Work estimate: <=15 minutes; add a necessary remainder before expanding beyond this bound. Source RMED is reviewed before implementation. Test-first acceptance uses honest local doubles separately from actual Docker proof.

## Definition of Done

Source-pinned O187 intent/events, deterministic identity, no-replay and exact pending-record recovery tests pass. Existing O180 and promotion regressions pass; shared locking refuses concurrent publication without changing required gates.

## Current dependency

The closed Journal and publication-lock implementations are independently accepted, with fifteen direct-Action tests, twenty unchanged initialization tests and two public promotion-lock tests passing. Full original promotion and directory-replacement tests remain required before the fresh Release. Their isolated executor needs the selected immutable N image, so they run after CA-P-1826 restores it. This Task therefore blocks CA-P-1623, not the image repair which supplies that test prerequisite. No Release gate or existing regression is removed.
