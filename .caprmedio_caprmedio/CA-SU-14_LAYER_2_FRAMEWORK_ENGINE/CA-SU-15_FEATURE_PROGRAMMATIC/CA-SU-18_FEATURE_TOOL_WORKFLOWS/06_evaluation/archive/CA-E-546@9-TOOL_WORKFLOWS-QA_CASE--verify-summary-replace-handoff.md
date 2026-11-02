---
atom_id: CA-E-546@9
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Tool//ATOM_LIFECYCLE.Summary Handoff
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Summary
  - Subject/Domain/Node/Continuant/History/Journal.Record
version: 9
updated_at: 2026-10-24 10:48:25 +0400
relations:
  evaluation_for:
  - CA-R-1825
  - CA-R-1826
tier: 3
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
