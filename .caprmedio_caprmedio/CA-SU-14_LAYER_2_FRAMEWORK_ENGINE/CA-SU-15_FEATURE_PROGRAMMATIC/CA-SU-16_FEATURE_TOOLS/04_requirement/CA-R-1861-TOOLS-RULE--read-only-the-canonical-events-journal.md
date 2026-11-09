---
atom_id: CA-R-1861
ref_id: CA-R-1861
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Retrieval"
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Event
tier: 3
status: Active
version: 14
updated_at: 2026-10-27 20:00:04 +0400
carrier_destination:
  file:
    name: CA-R-1861-TOOLS-RULE--read-only-the-canonical-events-journal.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Read only the canonical Events Journal

## Scope

The FIND_AND_FETCH_JOURNAL_EVENTS Tool source boundary.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** query only canonical Event carriers under the selected Project's `.caprmedio_<project name>/_journal/` root.

## Details

Historical sealed Event references resolve only as immutable references. The source
is raw canonical JSON Event bytes: raw duplicate object keys are rejected before
parse, and no alternate log, derived projection, filename identity, or source
rewrite may substitute for canonical Events.
