---
atom_id: CA-P-2670
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
work_sequence_number: 5
---
# Summary

Verify Engineering Subject branch and refresh views

## Objective

Verify applied Candidate #9 sources and regenerate the four Current Subject views.

## Details

Use actual Current sources and Versions after P2669, including promoted definitions. Preserve the four-section layout: primary Subjects; properties with inherited markers; instances; dependency-only Subjects with referring IDs. Check kind versus containment versus property notation and retain explicit unresolved source cases. Do not silently remap the projection independently of source Atoms.

## Definition of Done

- The four views reflect the actual applied source heads and new definitions.
- Candidate #9 branches are represented consistently; unresolved cases are reported.
- No Draft or file-count result is presented as Current-source acceptance or runtime validation.

## Completion

Completed in Candidate #9: reviewed Drafts were promoted with predecessor archives; the four Current-source Subject views were rebuilt and checked. See the parent Epic for the applied counts and retained exclusions.
