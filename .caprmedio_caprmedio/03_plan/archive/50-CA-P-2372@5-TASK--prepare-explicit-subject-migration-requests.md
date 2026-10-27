---
atom_id: CA-P-2372@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 50
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
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 07:45:09 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
tier: 3
---
# Summary

Prepare explicit Subject migration requests

## Objective

Compile the reviewed current map into explicit source-pinned request files without invoking preview, staging or mutation.

## Details

Use the current map, inventory and Candidate pins. Recheck all 906 owners and 4,530 occurrence dispositions. Select only the 611 mapped-change owners; keep all 266 unchanged and 29 excluded owners wholly untouched. Emit closed D425 Subject request payloads separately from provenance/readiness metadata. Use scalar governs replacement and explicit complete depends_on set replacement; deduplicate only exact explicitly mapped target strings and never infer meaning. Preserve unchanged dependency values. Record any resulting no-op truthfully. Refuse source/map drift; do not update pins silently.

Own only derived preparation scripts, tests and request/manifest files under `.caprmedio_tmp/stage2-migration-20261014/request-preparation/`. No candidate Atom bytes, Tool invocation, authoritative write or execution permission is produced. Estimated own work: up to 15 minutes; split before exceeding it. Root owns integration and Git; preserve other workers' files.

### Definition of Done

Focused checks prove exact coverage, owner exclusion, scalar governs, explicit expansion/convergence, unchanged dependency preservation and stale-source refusal. An independent reviewer verifies the actual emitted requests and bound source hashes. Metadata states that execution readiness and live approval remain separate; the broader Epic is not complete.

### Accepted bounded outcome

The builder, six tests, closed request and separate manifest are saved under the stated temporary preparation directory. They bind the current map/inventory/Candidate and all 906 original source hashes. Deterministic rebuild and independent audit passed: 611 request items; 346 scalar governs and 502 depends_on full-set patches; all 4,530 occurrence dispositions accounted for; 266 unchanged and 29 excluded owners preserved. All 155 excluded-owner occurrences are absent from payloads. 1,997 unchanged dependencies remain; 61 explicit duplicate target strings collapse across 56 owners. No resulting no-ops were found.

Request SHA-256: `a4f6b8b6083e8c054837dc7b03b3ae2f1500f9c429cfaa50917ae48cdac6fade`. Manifest SHA-256: `db9f0cadc1f3f615f6d154f83cb13d8d16c5b07738ea6f6226ee5fceb170d453`. Builder SHA-256: `36d106bfde725cef5c572b93905dc9b25ed8d4faa77bbe93262d7dd51bf0c983`. Six self-tests and independent integrated stale-source refusal passed; exact request bytes reproduced in memory.

The manifest is explicitly non-executable. No Tool invocation, staged Atom bytes, authoritative change or live approval was produced. These derived files remain temporary; any later use must reopen their hashes and all current source pins. This preparation Task is complete, not Tool or migration acceptance.
