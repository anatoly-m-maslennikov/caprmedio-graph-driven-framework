---
atom_id: CA-P-2381
content_role: Plan
type: Plan
label: Task
work_sequence_number: 59
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Subjects
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject
  - Subject/Graph Node/Domain/Continuant/Projection
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 6
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
tier: 3
---
# Summary

Prepare logical Subject preview request

## Objective

Adapt CA-P-2372's exact accepted 611-owner request to the now-delivered direct MCP preview schema without invoking preparation or mutation.

## Details

Keep the original request and manifest unchanged. Verify their exact hashes and source pins; convert only the transport envelope to operation preview_subjects, explicit profile and logical Atom ID/Version/SHA-256 with the existing explicit patches. Preserve payload order, all 848 patches, exclusions and reviewed mappings. Physical selectors belong only in the provenance sidecar, never the public request. Validate the closed canonical input model without invoking its adapter. No preview seal, candidate Atom bytes, stage, approval or source effect is produced.

Own only derived scripts, tests and request/provenance files under .caprmedio_tmp/stage2-migration-20261014/public-request. Estimated work: up to 15 minutes. Root owns integration and Git; preserve unrelated work and all original sources.

### Definition of Done

Focused checks prove exact transport conversion, unchanged order/patches, preserved owner exclusions and stale-input/source refusal. An independent reviewer accepts the emitted request and its pins. Readiness states that connected MCP activation, actual preview and staging remain unperformed. This does not complete the parent Epic.

## Completion evidence

The derived public request preserves all 611 owners and 848 ordered patches (346 governs, 502 dependency-set replacements), exact source pins and 29 exclusions. Four focused tests passed; independent review rechecked all 906 source hashes, the complete roundtrip and canonical closed DTO. Original request artifacts remain unchanged. Request SHA-256: `b78ec349a222f2b51c8cf62a80b42a7b829807a97e629275e9463133fe38d6aa`. Independent review: `.caprmedio_tmp/stage2-migration-20261014/public-request/independent-review.md`. This Task produced no preview, candidate Atom bytes or staging; subsequent connected execution is separate.

