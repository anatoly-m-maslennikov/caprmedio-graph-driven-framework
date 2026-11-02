---
atom_id: CA-O-202@8-draft
content_role: Operations
type: Workflow
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Draft
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Domain/Node/Continuant/Atom.Content
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
version: 8
updated_at: 2026-10-24 23:59:51 +0400
relations:
  relates_to:
  - CA-O-208
  - CA-O-030
  - CA-M-372
  - CA-R-1933
  - CA-R-1934
  - CA-M-305
tier: 3
---
# Summary

Modify explicit Atom targets

## Operation

Modify Explicit Atom Targets **means** the independent Workflow that applies explicit same-ID edits to an ordered list of distinct logical Atom targets through Step CA-O-208. Every target includes its exact Atom ID, Version, owning Scope Unit and complete explicit one-family proposal; there is no hidden Find, inferred successor or automatic reference retargeting.

### Workflow graph

Entry: CA-O-208 for the first explicit target. On a confirmed successful result and another supplied distinct target, transition to CA-O-208 bound to that next target. On confirmed success with no remaining target, terminate complete. On the first rejection, stale binding, failed, partial or unknown effect, incomplete recording or other unconfirmed success, terminate stopped, preserving evidence and leaving later targets untouched. This success-only progression is not a retry or resume of a failed Action.

### Request and result

Property/list and Section edits follow R1934/M374 and R1933/M373 through O030; list replacement is by unique current value or whole set, never caller index. Any Summary change, including wording-only, or Type change returns replacement-required rather than editing under the same ID. Reference modification is one explicit Property receiving use of this Workflow, not another duplicated Workflow family.

A requested batch is an ordered list of independently authorized Atom Actions. Invoke one Action at a time; advance to the next distinct explicit Atom only after confirmed success. On the first failure, stop, retain all earlier successful effects and their evidence, and leave the remaining targets untouched. Never roll back earlier successful Atoms to simulate a cross-Atom transaction. Validation, stale-source checks, permissions, safe effects and recovery within the failing Atom Action remain required. Automatic retry or resume of this new batch policy is deferred; existing recording-only recovery must not replay a performed Action.

Return each actual successful target ID/Version and the exact stopped-target outcome, not a cross-Atom all-or-nothing claim. Every actual same-ID edit advances Version once and records actual Project time; no-op retains Version/time. New Atom creation O032, Scope Unit creation O203 and archival O029 remain separate explicit Actions, not hidden O030 effects.

## Details

These are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.
