---
atom_id: CA-O-208@6
content_role: Operations
type: Step
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Occurrent/Execution/Step Run
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Continuant/Atom
version: 6
updated_at: 2026-10-24 00:51:05 +0400
relations:
  relates_to:
  - CA-O-202
  - CA-O-030
  - CA-R-1509
  - CA-R-1511
  - CA-M-305
  - CA-M-372
tier: 3
---
# Summary

Modify one explicit Atom target

## Operation

This Step invokes exactly CA-O-030 for one distinct explicit target selected by O202's success-only progression. It never invokes discovery, creation, replacement or archival.

### Input and parameter binding

Bind exact target Atom ID/Version, owning Scope Unit, current source/proposal pins, one explicit Property/list or Section operation and its old/current-value evidence from the supplied target item. Bind O030's applicable full-Atom validation/identity assessment, exact preview, effect permission, actual selected Session/Run recording context and current Action/Step/Workflow definition pins from the admitted receiving route. No missing input is inferred from a search or previous target.

Reject Summary or Type replacement requests, indexes, stale or unsupported bindings before dispatch. Return the exact O030 result and its actual target/effect/recording evidence. Only O202 chooses the next already supplied distinct target after confirmed success; failed-action retry or resume is not a Step behavior.

## Details

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
