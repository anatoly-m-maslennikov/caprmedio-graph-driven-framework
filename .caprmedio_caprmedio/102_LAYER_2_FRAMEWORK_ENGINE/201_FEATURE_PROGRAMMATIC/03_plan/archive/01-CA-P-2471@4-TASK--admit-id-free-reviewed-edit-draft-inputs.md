---
atom_id: CA-P-2471@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2463
version: 4
updated_at: 2026-10-24 08:06:50 +0400
tier: 3
---
# Summary

Admit ID-free reviewed edit Draft inputs

## Objective

Fix the independent review finding: source-pinned reviewed edit Drafts may omit atom_id with an aligned empty-number filename; staged output may still prefer version-qualified markers.

## Details

At most 15 minutes own work. Preserve exact packet/source/draft pins, candidate bytes, currentness, no-op semantics and conditional cleanup. No guessed identity, canonical lookup broadening, Journal/history gate, live staging, deployment or replay. Parent P2463 owns the staging increment; this child owns its newly detected compatibility fix.

### Definition of Done

A synthetic round-trip load/candidate/publication case admits the ID-omitted input and preserves exact canonical predecessor, while mismatched markers/filenames and tampered candidates remain rejected. Independent review closes this finding.

### Verified execution checkpoint

ID-free/empty-number reviewed edit Draft support passed the staging focused suites (13 draft checks, 5 contract checks, 10 workflow checks, 9 source checks and 4 manifest checks). Independent review confirmed the optional-ID reconstruction preserves candidate bytes and source pins. A distinct qualified-marker/carried-YAML-Version finding is assigned to P2473, not hidden by this bounded completion.
