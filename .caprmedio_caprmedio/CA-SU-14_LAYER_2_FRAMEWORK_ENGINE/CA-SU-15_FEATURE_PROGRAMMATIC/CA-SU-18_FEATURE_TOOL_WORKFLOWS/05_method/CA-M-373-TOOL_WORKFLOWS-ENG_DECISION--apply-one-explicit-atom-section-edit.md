---
atom_id: CA-M-373
ref_id: CA-M-373
container:
  scope_unit: CA-SU-18
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
tier: 3
status: Active
version: 11
updated_at: 2026-10-27 19:59:42 +0400
carrier_destination:
  file:
    name: CA-M-373-TOOL_WORKFLOWS-ENG_DECISION--apply-one-explicit-atom-section-edit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/05_method
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
---
# Summary

Apply one explicit Atom section edit

## Scope

One explicit section add, replace, remove, rename-title or reorder Action.

## Claim

**To** edit one section, the Atom Action **must**:

1. Bind the explicit Atom identity and expected Version or source pin, **`=1`** selected section operation and its requested value, title or position as applicable.
2. Read the complete current source through its storage connector. Resolve the selected existing section or explicit insertion location uniquely; reject missing, ambiguous or stale selections.
3. Derive only the declared edit. Preserve unrelated sections and Properties and the selected section's nested content when renaming or reordering. Validate the complete proposed Atom under its applicable structure and Property rules.
4. Reject any same-ID Summary or Type value change and require the replacement Workflow. If the validated requested state is unchanged, return a no-op without edit, Version, timestamp or history effects.
5. Bind the exact proposal to the admitted change class and preview. Every actual changed same-ID Atom update advances Version by **`=1`** and uses actual Updated At; retain its exact before-Revision evidence. Recheck current source and permission before an authorized effect; verify the actual resulting source and report the Action outcome truthfully.

Preserve each Action's existing storage-effect safeguards. A failure or uncertain outcome stops the containing several-Atom Workflow, retains earlier completed Actions and leaves the remainder untouched.

## Details

This Method states required behavior; source authoring alone is not implementation or acceptance. Resume and retry policy is deferred.
