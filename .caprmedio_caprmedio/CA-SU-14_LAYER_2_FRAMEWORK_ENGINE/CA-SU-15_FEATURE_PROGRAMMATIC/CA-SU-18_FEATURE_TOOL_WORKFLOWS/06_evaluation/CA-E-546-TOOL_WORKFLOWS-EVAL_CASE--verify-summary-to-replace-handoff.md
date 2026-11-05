---
atom_id: CA-E-546
ref_id: CA-E-546
container:
  scope_unit: CA-SU-18
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
tier: 3
relations:
  evaluation_for:
  - CA-R-1825
  - CA-R-1826
status: Active
version: 14
updated_at: 2026-10-27 19:59:37 +0400
carrier_destination:
  file:
    name: CA-E-546-TOOL_WORKFLOWS-EVAL_CASE--verify-summary-to-replace-handoff.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/06_evaluation
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
---
# Summary

Verify Summary-to-Replace handoff

## Scope

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

One sealed Update request that changes its Summary.

## Claim

Use one sealed CA-D-527 Update request whose proposed Summary differs, including a wording-only edit with unchanged Claim. Verify it ends as a terminal non-effect `replace_handoff` with the exact predecessor and complete proposed successor inputs, performs no same-ID Update, invokes no Replace, and preserves the predecessor unchanged. Verify that a separately admitted new CA-D-527 Replace request needs fresh exact definition, input, currentness, and permission bindings before the native Tool applies it; the Update request's permission cannot authorize that Replace. Verify the separately admitted replacement creates a fresh successor ID and archives the previous Atom, preserving explicit predecessor/successor lineage and observed history. For illustrative target 100, require truthful target 100, created 200 and archived 100 results; no incoming reference is automatically rewritten. Find and Modify referrers are separate workflows. Verify an unchanged Summary selects Update only when its native class permits it.

## Details

### Acceptance criteria

No Summary-changing request silently mutates the existing Atom identity or inherits Replace permission. The terminal handoff has no applied effect; a successful separately admitted Replace names the predecessor and every successor Carrier. Preview has neither mutation nor invented history. These are required future cases; they establish no implementation pass, new route or new resume/retry capability.
