---
atom_id: CA-E-626
content_role: Evaluation
type: QA Case
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Core
global_tier: 9
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool"
  depends_on: ["Atom","Workflow"]
version: 2
updated_at: "2026-10-12 23:54:41 +0400"
relations:
  evaluation_for: ["CA-R-1093","CA-R-1041","CA-R-1067"]
  relates_to: ["CA-M-372","CA-O-201","CA-O-202","CA-E-247","CA-E-546"]
---
# Summary

Verify independent Atom workflow effects

## Scope

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

Required future checks for ordered independent Atom workflows, fresh-ID Summary replacement and explicit reference handoffs.

## Claim

A workflow stops at its first failed Atom action, retains earlier completed actions and leaves the remaining targets untouched. Safety/all-or-nothing within one admitted Atom action remains required; there is no cross-Atom transaction.

## Details

1. Prepare ordered explicit targets A, B and C with exact ID/Version/source pins. Complete A, then make B fail validation, currentness, permission or publication. Independently observe A's retained effect, B's truthful failure/uncertainty and C's unchanged bytes with no invocation.
2. Test successful actions and truthful no-ops without implicit rollback, widened selection or invented results. An action-local failure must honor that action's admitted restoration boundary; it cannot undo A. A claimed restoration needs observed proof.
3. Apply a wording-only Summary replacement using full Atom IDs corresponding to illustrative target 100 and successor 200. Require a fresh ID and predecessor archival; ordinary same-ID Modify fails. Completed output identifies target 100, created 200 and archived 100 with exact observed state evidence. A changed predecessor archival state is N+1; exact prior history remains at N. A fresh successor starts at its admitted initial Version.
4. Make independent successor Create complete and predecessor Archive fail. Retain the observed created successor and report incomplete replacement; do not serialize a proposed archive as completed or erase the earlier action.
5. Keep incoming references to 100 unchanged. Use a separate Find workflow for actual referrers and a separate Modify workflow for explicit referrer targets with their own source pins/permission. A replacement result alone cannot authorize those changes.
6. A requested new-workflow resume/retry is explicitly deferred. Existing shared recording-only handling never authorizes replay of an Atom effect. Do not assert concurrent publication or stronger backend guarantees without separate proof.

### Acceptance and failure disposition

Compare independent invocation/effect ledgers and source/history observations. Retain completed actions, the first failure and unperformed remainder with currentness/permission and known/unknown effect evidence. Reject false batch atomicity, automatic reference rewriting, implicit retries and completion without actual effects/recording. These are required cases, not observed test passes or implementation claims.
