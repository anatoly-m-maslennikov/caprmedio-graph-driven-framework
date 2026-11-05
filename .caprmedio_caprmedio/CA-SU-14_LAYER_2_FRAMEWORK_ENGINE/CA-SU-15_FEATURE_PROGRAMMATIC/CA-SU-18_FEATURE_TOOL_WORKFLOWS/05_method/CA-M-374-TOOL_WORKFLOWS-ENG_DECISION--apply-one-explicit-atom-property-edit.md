---
atom_id: CA-M-374
ref_id: CA-M-374
role: Method
form: Eng Decision
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 19:59:42 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
tier: 3
container:
  scope_unit: CA-SU-18
carrier_destination:
  file:
    name: CA-M-374-TOOL_WORKFLOWS-ENG_DECISION--apply-one-explicit-atom-property-edit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/05_method
---
# Summary

Apply one explicit Atom Property edit

## Scope

Explicit Property and list-entry edits within one Atom Action.

## Claim

**To** edit Atom Properties, the Action **must**:

1. Bind the explicit Atom identity and expected Version or source pin, declared Property edits and proposed values where required; read the complete current source through its connector.
2. Resolve each declared Property under its applicable schema. For an entry replacement or removal selected by current value, require exactly one existing equal value. Reject absent or ambiguous current values and caller-supplied replacement indexes.
3. Derive only explicit add, replace or remove deltas. For list Properties, support entry add/remove, replacement by unique current value or whole-set replacement; preserve unrelated entries and governed order and validate the complete proposed list and Atom.
4. Reject any same-ID Summary or Type value change and require replacement with a new Atom ID and predecessor archival. A verified unchanged requested state is a no-op without edit, Version, timestamp or history effects.
5. Every actual changed same-ID Atom update advances Version by **`=1`** and uses actual Updated At; retain its exact before-Revision evidence. Reuse admitted change-class, preview and permission checks, then recheck current source before the authorized effect. Verify the actual resulting source and report its exact outcome.

Preserve one-Atom storage-effect safeguards. A failed or uncertain Action stops the containing several-Atom Workflow, retains earlier completed Actions and leaves the remainder untouched.

## Details

Historical scalar-index fixtures do not validate this required current-value contract. Resume and retry policy is deferred; no implementation or live publication is established here.
