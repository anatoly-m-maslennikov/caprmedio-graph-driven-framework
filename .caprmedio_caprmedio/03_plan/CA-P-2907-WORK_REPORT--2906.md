---
identity:
  id: CA-P-2907
  ref_id: CA-P-2907
context:
  container:
    scope_unit: CA-SU-00
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-11 00:22:28 +0400
destination:
  file:
    name: CA-P-2907-WORK_REPORT--2906.md
    path: .caprmedio_caprmedio/03_plan
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2906
author: Anatoly Maslennikov
---

## Summary

Align Workflow RMEDO with SQL scripts and Atom lifecycle

## Details

The Operator authorized correction of the reported RMEDO gaps. Work is proceeding through exclusive Core model, lifecycle, Workbench and MCP help source lanes, with independent Workbench and lifecycle/model review. The implementation chat owns its Epic and Task records and has granted this change exclusive ownership of the overlapping Workbench source contracts.

MCP tools are not available in this chat. The Operator's standing instruction permits manual work when MCP is unavailable. Exact source preimages, change manifests and review records are retained under `.caprmedio_tmp/workflow-rmedo-fix-20261111/`.

Current source corrections preserve existing identity, Version and Updated At for in-place edits. The selected identified model Drafts are adopted only with their approved dependency closure. New lifecycle and specification-work Workflow definitions remain WIP Drafts. Historical duplicate trees and generated projections are outside this source change.

The initial independent review found missing read-after-write semantics, stale neighboring one-query rules, incomplete lifecycle version/timestamp rules, lost Move/containment behavior, public-schema help admission gaps and incomplete Workflow handoffs. All findings from the bounded Workbench, lifecycle/model and help/specification-Workflow reviews were corrected and independently re-reviewed to PASS.

The Operator confirmed that statements execute one by one and later statements see earlier writes. Both SQL modes now require this behavior. Draft mode reuses the evolving Draft state within the Run while Current Atoms remain unchanged; promotion is separate. Failures stop the script and report completed results and effects, without retries, rollback or recovery.

Workbench contracts now define Tabs containing multi-statement SQL scripts, source-backed changes, change previews, explicit Draft/in-place modes and discoverable issue-table metadata. R2728 delegates the three audit predicates to the independently adopted R970308648–650 rather than duplicating them. The separate implementation lane owns those six audit RMED source records and implementation; its adoption manifest is referenced in the handoff.

Core adopted the approved Workflow Claim declarations R2961–2964 and optional Step diagram declaration R2969, and added Step Kind/Inputs/Fixed Parameters/Outputs declarations R970308643–646. Existing RUNS authority is reused. R1432/R1788 and directly affected lifecycle Operations/Evaluations now agree on identity, one successor Version assignment, metadata-preserving in-place changes, archive-before-publish, all replacement targets, Move and containment behavior.

The four shared MCP help contracts are R970308647, M548, E820 and D714. They require help-only admission at the public schema boundary, Tool-specific documentation, trusted Project binding and blacklist enforcement without business effects.

Four new specification-work Workflow definitions, their Steps and one shared review Action are saved as 34 WIP Draft carriers. They cover review/refinement, model change, consistency corrections through queries, and consolidation. They include real SQL/mode/data bindings, separate Check/preview/apply calls and explicit decision and lifecycle loops. They do not recreate the retired Workflow Orchestrator. A required projection rebuild remains pending when no admitted builder Action is available; it is never reported as executed.

Final verification covers 119 source carriers: unique YAML keys, declared carrier destinations where present, Workflow Claim heading cardinality/order, and 201 local Markdown/Mermaid links. There were 117 comparisons preserving base identity, Version and Updated At across preimages; 52 affected identified Current Atoms were checked for duplicate Current identity. Source-scoped whitespace checks pass after one EOF-only formatting correction. These checks are narrower than a full model/CFEL or runtime validation.

The exact Current IDs, Versions, hashes, file paths, dependent audit adoption and WIP exclusions are recorded in `.caprmedio_tmp/p2791-implementation-20261111/source-handoff.md`. The old O239/O230 and shared-context frontier are outside this Task; the implementation chat retains their separate Concerns. This Task does not settle that chat's runtime-scope question.

No implementation code, test suite, Docker image, installed MCP, Git commit or deployment was changed by this Task.
