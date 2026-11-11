---
identity:
  id: CA-A-1336
  ref_id: CA-A-1336@1-draft
context:
  container:
    scope_unit: CA-SU-14
  role: analysis_and_advisory
  form: specification_proposal
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FRAMEWORK_ENGINE
    dependencies:
    - CAPRMEDIO_MODEL <+ Scope Unit
    - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Workflow
  tier: 3
state:
  status: draft
  version: 1
  updated_at: '2026-11-11T17:34:26+04:00'
destination:
  file:
    name: CA-A-1336@1-draft-FRAMEWORK_ENGINE-SPECIFICATION_PROPOSAL--decide-the-remaining-atom-lifecycle-rules.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory/000_draft
---

## Summary

Decide the remaining Atom Lifecycle rules

## Proposal

This Draft records the Scope Delegation decision and the remaining options for CA-C-730. The Current contracts govern until the decisions are adopted. [CA-C-730](../../01_concern/CA-C-730-QUESTION--admit-the-atom-lifecycle-tool-contract.md) · [CA-P-2934](../../03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/CA-P-2934-TASK--implement-the-new-atom-lifecycle-tools.md)

### 1. Scope Delegation admission

**Decision for now.** Scope Unit Declarations state structural facts in their Formal Claims. Scope Delegations state responsibilities, admitted local Role/Form pairs, and allowed active Subjects in prose. When an Atom requires an explicit admission, its Role/Form pair and exact active Subject must come from the same Scope Delegation. Each target admits the resolved entity or instance at that address. Admit descendants and other instances explicitly.

- Resolve nested Atom Containers to their owning Scope Unit. Apply the Project's root Subject authority separately.
- Keep the default local Forms and Role limits in CA-R-3008. Solution, Direct Policy and Approach Policy require an explicit pair. Code Synopsis has its existing default admission within the applicable Subject and Container boundaries. Apply the applicable Subject check to defaults too.
- Admit Work Report only for an admitted Task linked by its base Atom ID. Check the report’s own ID, matching Summary and Container, and the applicable Subject boundary.
- Evaluate exact targets, same-named targets at other addresses, unresolved targets, descendants, and permissions drawn from different Delegations. The 84 existing formal Role/Form pairs are inputs to the version 0.7 review under CA-P-3000.

CA-P-3000 tracks the version 0.7 review of formal admission. [CA-R-3006](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-3006-CORE_META_MODEL-DECLARATION--declare-scope-delegation.md) · [CA-R-3008](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-3008-CORE_META_MODEL-REQUIREMENT--establish-project-and-non-project-scope-unit-declarations-and-delegations.md) · [CA-R-2618](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2618-CORE_META_MODEL-DECLARATION--declare-has-active-subject.md) · [CA-R-2763](../../CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/CA-R-2763-WORKBENCH-SCOPE_DELEGATION-WORKBENCH_BACKEND--declare-workbench-backend.md) · [CA-R-970308624](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-970308624-CORE_META_MODEL-DECLARATION--declare-work-report-form.md)

### 2. Reopen a terminal Plan tree

**Choose** parent-first reopening with the existing cascade, or continue to refuse reopening through this Workflow.

For parent-first reopening, set the selected Plan to the requested nonterminal Status first. Then set its selected descendants from outermost to innermost. Check any terminal ancestor outside the selected tree before making changes. Re-resolve descendant paths after an ancestor’s directory moves and verify their identities. Stop at the first failure and report completed effects and remaining targets.

Example. Epic Done, Task Done, Subtask Canceled. For an authorized change to Active, apply Epic, then Task, then Subtask. If Task fails, Epic stays Active and the two descendants stay terminal. Every completed action satisfies the terminal-ancestor invariant. Closing a tree still proceeds descendant-first.

Update the status Workflow and its bound Action or evaluation as needed. The Model invariant already states the required final states. [CA-R-2511](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2511-CORE_META_MODEL-DECLARATION--declare-plan.md) · [CA-R-1521](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1521-CORE_META_MODEL-RULE--resolve-lifecycle-changes-from-applicable-status-models.md) · [CA-O-10011](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10011-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-change-current-status.md)

### 3. Update a folder-backed Atom

**Choose** keep composed Update for leaves, or support a subtree-preserving update for a successor with the same ID.

- **Leaves.** Refuse a folder-backed target before creating its Draft or archiving anything. This keeps the existing leaf flow usable.
- **Same-ID successor.** Keep the Current subtree under the successor. Immediate children keep their base Container ID. Preserve descendants’ Status, Version, Updated At and Content. Recalculate destination fields when placement changes. Define how publication keeps the Current parent reference resolvable, including failure between archiving the predecessor and publishing the successor.
- **Fresh-ID successor.** If needed, decide separately whether to archive the old subtree or reparent its Current children. Carryover requires authorized changes to immediate children’s Container references, with explicit versioning, event and failure rules. A replacement covering several predecessors also needs a subtree selection rule.

The existing composed Update calls Archive and then Promote. Archive covers the entire Current subtree, and the Promote Action accepts a non-container Draft. A subtree-preserving Update needs a different predecessor-archive and publication contract. [CA-O-10024](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10024-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom.md) · [CA-O-10009](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10009-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-archive-atom.md) · [CA-O-10005](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-10005-PROJECT_CONFIGURATION-ACTION--promote-one-atom-draft.md) · [CA-R-1432](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1432-CORE_META_MODEL-RULE--govern-atom-lifecycle-identity-and-version.md) · [CA-R-2779](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2779-CORE_META_MODEL-DECLARATION--declare-atom-header-container.md) · [CA-D-480](../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-480-CORE_META_MODEL-ENG_DECISION--keep-atom-addresses-consistent-with-carried-properties.md)
