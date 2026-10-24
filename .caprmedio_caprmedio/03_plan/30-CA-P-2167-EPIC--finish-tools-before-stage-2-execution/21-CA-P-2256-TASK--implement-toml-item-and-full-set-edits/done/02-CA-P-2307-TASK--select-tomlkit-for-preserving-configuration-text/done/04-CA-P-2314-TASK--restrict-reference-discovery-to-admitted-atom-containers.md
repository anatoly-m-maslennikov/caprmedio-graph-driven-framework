---
atom_id: CA-P-2314
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Carrier, Workflow, Step, Action, Plan]
version: 3
updated_at: "2026-10-13 18:41:24 +0400"
relations:
  is_decomposition_of: [CA-P-2307]
---
# Summary

Restrict reference discovery to admitted Atom containers

## Objective

Discover Atom carriers only under declared Scope Unit authority roots and the selected Project root, through declared Content Role folders and their admitted Status or Atom-backed containers. Do not add exclusion Settings or recursively search unknown folders. Keep malformed admitted carriers as errors.

## Details

Estimated own work: up to 15 minutes; split before exceeding this bound.

The Operator chose the recursive Plan-style convention for folder-backed Workflows and Steps: one sibling Markdown file and an optional same-stem Directory Carrier at each level. A Workflow folder contains Steps; a Step folder contains substeps, recursively. Actions remain outside the whole Workflow/Step folder tree; Steps reference those separate reusable Actions. Folder nesting does not define execution order or Action execution; the explicit Workflow graph remains authoritative for that. Revise D467 and the directly affected E500 examples, preserving Summary and identity and archiving their exact prior bytes. Do not relocate existing carriers or change graph meaning or Step ownership during this lookup implementation. The Operator's later decision supersedes the earlier independent-descendant-change wording: a parent Status change cascades to all contained latest P/O Atom versions, preserving nesting, while older historical revisions and referenced Atoms outside the tree remain untouched. This is a lifecycle Workflow policy, not read-time Status inheritance.

The approved read-only FPF design challenge completed under Plan `workflow-carrier-whitelist-d96b9733`, with independently validated final attempt 2. I1/F1 requires admitted-container-only discovery; I2/F2 requires separate traversal, placement and target-status checks. The Operator resolved the follow-up decisions: all Status changes cascade through latest contained P/O Atoms, history does not change, and noncanonical `archive/` layouts are excluded until a separate later migration. The three existing red regressions expose unknown-folder reads and false target/parent admission. Implement the narrow lookup only after the amended source packet is independently accepted. This records a completed review and subsequent decisions, not runtime acceptance.

After review: bind the exact current carrier/status sources; update the inventory and its caller together; verify Plan and Workflow same-stem authentication, malformed-carrier refusal, selected Project and nested Scope Unit roots, bounded no-follow reads, and admitted-frontier currentness. Do not invent Implementation status folders or silently generalize legacy archive placement. Resolve concrete remaining rule conflicts before implementation.

### Completion — 2026-10-13

The bounded lookup and source bindings are independently accepted in commits `c9c22b34d` and `5a1d3171d`. Final focused checks: 55/55 PASS; full validator: 306/308 PASS with two pre-existing graph-path failures; selected lifecycle: 30/30 PASS. Actual current-carrier checks now stop at a malformed Concern inside an admitted folder, not the formerly scanned unknown evidence folder. See `.caprmedio_caprmedio/_projection/core-entity-review/stage2/tools-first/admitted-container-lookup-acceptance.md` for exact pins and limits. That source normalization, full admission, nested Operations authoring and lifecycle cascade execution are not claimed complete.

### Definition of Done

The affected source rules and review are accepted; the complete caller path uses the whitelist; independent tests pass and actual-carrier rechecks report remaining gaps honestly. No broad Core migration, dependency installation, runtime activation, or source normalization is included.
