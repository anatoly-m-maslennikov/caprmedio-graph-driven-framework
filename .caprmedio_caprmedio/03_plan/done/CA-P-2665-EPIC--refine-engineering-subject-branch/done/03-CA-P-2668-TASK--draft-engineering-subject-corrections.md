---
atom_id: CA-P-2668
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Node/Engineering
version: 3
updated_at: 2026-10-27 06:19:16 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2665
tier: 4
work_sequence_number: 3
---
# Summary

Draft Engineering Subject corrections

## Objective

Prepare Candidate #9 Subject corrections and missing R/Definition Atoms as real Drafts, with Governs reviewed before Depends On.

## Details

Use the Candidate #9 decision record in P2667. Refine the supported preceding Drafts rather than discarding their corrections. Preserve unrelated Drafts and source content.

Maintain only the four-column Candidate #9 table linked from the Epic. Record Planned, Drafted, Applied or Needs decision from actual work. Store proposed content in its Draft, not a second mapping report.

Reuse existing File, Directory, Database and Journal definitions. Release and its ID already have Draft definitions that need the new History placement. Add thin definitions for missing Implementation, Code, Prompt, Documentation, Resource and Runtime kinds. Technology-specific Carrier definitions belong in PROJECT_CONFIGURATION. Check meaning rather than assuming that an existing Type: Definition header defines the required kind.

## Definition of Done

- Each supported correction has an identifiable successor Draft and a thin-table row.
- Missing kinds have R/Definition Drafts; existing same-meaning definitions are reused.
- Current source heads remain unchanged during preparation, and unresolved mappings are explicit.

## Completion

Completed in Candidate #9: reviewed Drafts were promoted with predecessor archives; the four Current-source Subject views were rebuilt and checked. See the parent Epic for the applied counts and retained exclusions.
