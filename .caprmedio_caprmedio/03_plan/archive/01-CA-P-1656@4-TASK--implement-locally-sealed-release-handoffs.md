---
atom_id: CA-P-1656@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
subjects:
  governs: Implement locally sealed Release handoffs
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Status
  - Subject/Engineering/Carrier
  - Subject/Engineering/Tool
  - Manifest
  - Methodology
  - Evaluation
  - Subject/Domain/Node/Continuant/History/Journal
version: 4
updated_at: 2026-10-24 08:10:13 +0400
relations:
  is_decomposition_of:
  - CA-P-1654
  blocks:
  - CA-P-1658
  - CA-P-1650
tier: 3
---
# Summary

Implement locally sealed Release handoffs

## Objective

Within <=15 minutes, implement locally sealed Release handoffs.

## Details

Own RELEASE_VERSION/release_contract.py and one new release_handoff.py only. Implement accepted D566/D567/E572@2: strict canonical candidate.v2 with self-excluding checksum, full locally observed inventory/modes, expected future digests, internal pre-compiler validated candidate, and post-copy/post-compiler SealedCandidateCompilation. Current sources/selection/currentness are locally read and compared; caller authority mappings are not gates. Bind all reported fields and preserve N. No actual copy, compile, package, Skill, image, selector or Journal effects. Coordinate P1657 independent golden tests; source gaps choose best safe option and record C/Question.

Read exact accepted sources and current files. You are not alone: preserve unrelated edits. Do not bypass C447/C449 or count a development worker as immutable-image/MCP/queue proof. Record actual saved output and remaining coverage.

## Definition of Done

The bounded assigned output, exact frontier and genuine focused evidence are saved. Source-only, mocked, partial or rejected work does not complete the composite, required runtime gates or Epic.

## Result

Implemented the v2 local candidate validator and typed source-copy/compiler handoffs. Candidate checksum, full local inventories and actual byte/mode rereads are bound to current structure/settings/source/selection; raw caller authority or package mappings are rejected. release_contract.py SHA-256 6dc7f9502f264368fd8e83c167bceaf4a59ec36fe69b101b6d08e4e19f2cc423; release_handoff.py 17c66c4ead4989d5908cd6642cf667b0e3347c39572b8d3716b03447f57f4647. Root reran fourteen codec and thirteen handoff tests in the existing development worker: all twenty-seven passed, no skips. Positive compiler evidence is explicitly mocked; actual compilation, staging, full suite, runtime, image and promotion remain unfinished.
