---
identity:
  id: CA-P-2715
  ref_id: CA-P-2715
context:
  container:
    scope_unit: CA-SU-14
  role: Plan
  form: Plan
  label: Epic
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Done
  version: 5
  updated_at: 2026-11-09 02:11:53 +0400
destination:
  file:
    name: CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done
author: Anatoly Maslennikov
---

## Summary

ENGINE Spec and implementation refinement and derived relations fixes

## Objective

Align Workbench and its tools with the active model, fix derived relations using generated declarations, refine the selected RMEDO and reconcile the implementation with the promoted specification.

## Scope

- WORKBENCH and its declared descendants.
- Workbench tools, including query_run and related query, View, Workspace and service capabilities, wherever their current RMEDO is owned.
- PROGRAMMATIC-local and APPS-local RMEDO.
- Shared relation declarations and report/replacement contracts only as necessary prerequisites, coordinated with their source owners.

The 500 benchmark Atoms in WORKBENCH_BURST_500_RENAMED are excluded and preserved unchanged. Their migration is deferred.

Older non-Workbench tools are excluded. They are to be rebuilt from scratch separately. Do not rebuild or restore them in this Epic. Existing Current source files are the baseline; Drafts and Archives remain separate from adopted source.

## Work order

Relations and Draft preparation can proceed independently after scope review. The relation branch has its own two-pass review, promotion, code-comparison and correction gate before implementation; it does not wait on the later bulk-migration gate. Use IS_BLOCKED_BY for actual prerequisites; do not serialize independent branches. Two review-improve passes precede promotion. Compare the promoted specification with code before deciding implementation or RMEDO corrections. Specifications belong in RMEDO, not in Task text.

## Working procedure

Before starting or continuing a Task or subtask, review its next work unit and fix missing inputs or acceptance criteria first. If confidence is below 90%, re-read the Operator input. If still below 90%, ask the Operator and continue independent unblocked work.

Keep one small P / Work Report per Task and update it during execution. Use the adopted Work Report contract CA-R-970308624@2 and IS_WORK_REPORT_FOR CA-R-970308626@2; reports are separate from Tasks and do not establish new specification authority.

## Details

Subtasks below are work units, each with an estimated 10–20 minutes. Split a larger unit before starting it. For Atom batches, select a small number that fits the time box and repeat by batch; do not treat the whole inventory as one subtask. Assign at most one Scope Unit to each worker. Terra and Luna may handle bounded work; main judgments and final review use GPT-6.1 Sol at High effort.

## Inputs and shared prerequisites

- Current Forms: CA-R-3002 (Solution), CA-R-3003 (Direct Policy), CA-R-3004 (Approach Policy), CA-R-3005 (Decision). Classify from meaning and applicability, not from an old filename. Role and Form remain independent; do not force every Requirement or structural Declaration into a MEDO Form.
- Existing CA-P-2712 owns Work Report model adoption. Use it instead of creating a competing definition task. I / Code Synopsis model work under CA-P-2713 is Done.
- The Operator requested IS_REPLACEMENT_FOR. Current CA-R-3011 is named REPLACEMENT_FOR. Resolve this explicitly with the source owner before replacement promotion; do not silently choose a spelling.
- Reuse or update related Method Policies from PROGRAMMATIC through the selected Scope Unit before implementation. Gather accepted REDO and non-Policy M separately for the implementation input.
- The pending Project-root-ID and Header.Context.Container-column fixes belong to relation/Workbench verification, not proof of an already deployed release.

## Tasks

- [x] [CA-P-2716 — Confirm the refinement scope and task inputs](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/01-CA-P-2716-TASK--confirm-the-refinement-scope-and-task-inputs.md).
- [x] [CA-P-2717 — Prepare and review the relation specifications](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/02-CA-P-2717-TASK--prepare-and-review-the-relation-specifications.md).
- [x] [CA-P-2718 — Generate the canonical relation registry from declarations](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/03-CA-P-2718-TASK--generate-the-canonical-relation-registry-from-declarations.md).
- [x] [CA-P-2719 — Fix relation materialization with the generated registry](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/04-CA-P-2719-TASK--fix-relation-materialization-with-the-generated-registry.md).
- [x] [CA-P-2720 — Generate relations during image builds and local release](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/05-CA-P-2720-TASK--generate-relations-during-image-builds-and-local-release.md).
- [x] [CA-P-2721 — Verify and release the relation fixes](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/06-CA-P-2721-TASK--verify-and-release-the-relation-fixes.md).
- [x] [CA-P-2722 — Verify shared model prerequisites for adoption](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/07-CA-P-2722-TASK--verify-shared-model-prerequisites-for-adoption.md).
- [x] [CA-P-2723 — Prepare Drafts for Workbench tool specifications](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/08-CA-P-2723-TASK--prepare-drafts-for-workbench-tool-specifications.md).
- [x] [CA-P-2724 — Prepare Drafts for WORKBENCH and its descendants](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/09-CA-P-2724-TASK--prepare-drafts-for-workbench-and-its-descendants.md).
- [x] [CA-P-2725 — Review and improve the specification Drafts: pass one](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/10-CA-P-2725-TASK--review-and-improve-the-specification-drafts-pass-one.md).
- [x] [CA-P-2726 — Review and improve the specification Drafts: pass two](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/11-CA-P-2726-TASK--review-and-improve-the-specification-drafts-pass-two.md).
- [x] [CA-P-2727 — Promote the reviewed specification Drafts](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/12-CA-P-2727-TASK--promote-the-reviewed-specification-drafts.md).
- [x] [CA-P-2728 — Compare promoted specifications with code and write Code Synopses](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/13-CA-P-2728-TASK--compare-promoted-specifications-with-code-and-write-code-synopses.md).
- [x] [CA-P-2729 — Review and resolve specification versus code differences](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/14-CA-P-2729-TASK--review-and-resolve-specification-versus-code-differences.md).
- [x] [CA-P-2730 — Implement and refactor the accepted specification](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/15-CA-P-2730-TASK--implement-and-refactor-the-accepted-specification.md).
- [x] [CA-P-2731 — Verify and locally release the refined Engine](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/16-CA-P-2731-TASK--verify-and-locally-release-the-refined-engine.md).
- [x] [CA-P-2733 — Prepare Drafts for PROGRAMMATIC-local RMEDO](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/17-CA-P-2733-TASK--prepare-drafts-for-programmatic-local-rmedo.md).
- [x] [CA-P-2734 — Prepare Drafts for APPS-local RMEDO](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/18-CA-P-2734-TASK--prepare-drafts-for-apps-local-rmedo.md).

- [x] [CA-P-2735 — Adopt the reviewed relation packet before implementation](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/19-CA-P-2735-TASK--adopt-the-reviewed-relation-packet-before-implementation.md).

- [x] [CA-P-2736 — Expose missing declared Content through query_run](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/20-CA-P-2736-TASK--expose-missing-declared-content-through-query-run.md).

- [x] [CA-P-2737 — Map adopted Atoms to implementation modules](CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done/21-CA-P-2737-TASK--map-adopted-atoms-to-implementation-modules.md).

## Acceptance

- The canonical relation registry is generated from accepted declarations on every image rebuild, including local release, and is used by the actual consumer.
- Direct and derived relations are verified against source declarations in SQL and GRAPH_TABLE; source-data repairs remain explicit.
- Every selected Current RMEDO Atom is accounted for, reviewed and improved twice, then promoted/replaced or explicitly held.
- Confirmed post-promotion specification/code differences have I / Code Synopsis and an accepted correction decision.
- A thin Atom ID@Version-to-module map records actual implementation evidence, unmapped Atoms and stale or unsupported module pins.
- Implemented changes pass their E2E and unchanged performance/resource gates, and the installed local release is checked.
- Every worked Task has a small Work Report. Claims of Drafting, adoption, implementation, testing and deployment stay distinct.

## Atom access

Fetch and analyze Atoms with query_run. Source-copy Draft creation waits for the missing declared Content exposure; the Operator did not approve a raw-file fetch fallback.

## Tracking

CA-P-2716 assigns one drafting owner per Atom. Workbench tool candidates already owned by WORKBENCH are handled by CA-P-2724, not duplicated by CA-P-2723. PROGRAMMATIC-local and APPS-local candidates are owned only by CA-P-2733 and CA-P-2734.

Keep inventories thin: Atom ID | Draft ID | Owner Task | Status. Store file paths in a separate local execution cache when needed; the tracking file is not a second source/specification. Use small report files and the Task/Work Report Atoms for execution tracking; do not create a second large specification in mapping files.


## Current scope checkpoint

The Operator approved updating the affected Scope Delegations and their local permissions without changing the Scope Unit tree. Complete this prerequisite before affected Draft promotions.

Preserve and exclude the 500 benchmark Atoms and their synthetic Scope Declaration. Defer the 78 content-unavailable RMEDO Atoms: 64 PROGRAMMATIC-local, 12 APPS-local and O240/O241. Do not add a full-document SQL helper for them.

Prepare, review and adopt the required Scope Delegation Drafts; verify the mixed Declaration/Delegation reader before promotion. Review the corrected R1186/R1187 and D673 Drafts. Keep specification in RMEDO; these are work items, not substitute contracts.


## Completion

Deployed and verified local release 0.4.4.40. All 251 selected tests and eight isolated Docker E2E cases passed; the separate profiler-off short CPU/RAM and View-result lifecycle gate passed without changed limits. All 105 checked installed production Python modules and both generated schema/relation assets match the release package. Live query_schema exposes dotted paths with snake_case segments, including header.identity.atom_id and content.claim.formal_claim; Mode 2 is enabled. The 171 expected Current source versions match; R2731 is retired. Declared direct/derived bindings have no missing inverse facts. The real-project canary passed all Atom and Scope Unit operations and removed its temporary sources: 48 Scope Units remain, no canary rows or files remain, and all 500 benchmark Atoms are preserved. Ordinary live edit/rename/move visibility was 0.338–0.439 seconds; first/last schema and structural rebuilds took 31.645–40.163 seconds. Release cleanup retained an image without proven Project ownership; deployment itself is healthy. The 78 legacy Atoms, older non-Workbench Tools, standalone chat and native Codex rendering remain explicitly deferred. Code Synopses I4/I5/I6 remain historical Draft reports, not Current implementation authority. Detailed acceptance evidence is in inventory/implementation-evidence.json.
