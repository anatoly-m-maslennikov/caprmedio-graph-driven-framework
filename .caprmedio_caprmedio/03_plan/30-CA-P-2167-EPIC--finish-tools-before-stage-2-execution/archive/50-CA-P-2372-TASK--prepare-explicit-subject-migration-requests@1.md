---
atom_id: CA-P-2372
content_role: Plan
type: Plan
label: Task
work_sequence_number: 50
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Projection, Plan]
version: 1
updated_at: "2026-10-14 05:59:01 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
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
