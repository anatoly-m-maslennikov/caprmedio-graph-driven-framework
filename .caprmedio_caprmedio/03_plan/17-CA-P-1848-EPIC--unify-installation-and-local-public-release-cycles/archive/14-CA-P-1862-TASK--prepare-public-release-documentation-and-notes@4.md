---
atom_id: CA-P-1862
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-10 18:08:27 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Version, Framework Package, Workflow Run, Workflow, Action, Journal, Evaluation]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1863]
---
# Summary

Prepare public release documentation **and** notes

## Objective

the AI Agent prepares accurate public release documentation **and** a full PR description for the validated release.

## Details

1. The Public release command updates documentation programmatically from actual changes and the canonical Version; documentation that changes the product closure requires its fresh complete suite before publication.
2. Ask one content prompt only. It returns the full PR description with complete “What's new” and “What's fixed” lists and the concise Version History bullet summary. Do not prompt for README text, approval retries or a second description.
3. Use the matching PR URL when it is already known. For a new PR, append its returned actual URL to Version History in a mechanical metadata-only follow-up commit/push; that link-only change does not require a second complete suite.
4. Retain only the concise summary and actual PR URL in `VERSION_HISTORY.md`; the complete description belongs to the PR. Do not claim a push, PR, merge or release that has not occurred.

### Definition of Done

the Plan is **not** Done **if** documentation is stale, package/version identity disagrees, the one prompt does not yield both required outputs, Version History duplicates full PR lists, or the recorded URL is not actual.
