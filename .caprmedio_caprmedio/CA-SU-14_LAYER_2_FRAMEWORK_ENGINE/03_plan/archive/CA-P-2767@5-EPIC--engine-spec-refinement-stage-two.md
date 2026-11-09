---
identity:
  id: CA-P-2767@5
  ref_id: CA-P-2767@5
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
  status: Archived
  version: 5
  updated_at: 2026-11-09 14:24:58 +0400
destination:
  file:
    name: CA-P-2767@5-EPIC--engine-spec-refinement-stage-two.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/archive
author: Anatoly Maslennikov
---

## Summary

ENGINE Spec refinement stage 2

## Objective

Refine Engine MED topics, claims, Roles, Forms, Scope ownership, relations and Tiers; review Code Synopses and prepare a separate implementation Epic.

## Scope

All FRAMEWORK_ENGINE local sources and its descendants, including PROGRAMMATIC-local and APPS-local Atoms, AGENTIC and its eligible descendants, MCP, WORKBENCH and its descendants, and Workbench query/View/Workspace/service capabilities wherever their specification is owned.

Exclude older non-Workbench Tool specifications: TOOLS and its descendants, CONNECTOR_TOOLS, TOOL_WORKFLOWS and PROJECT_TOOLS, except Atoms that actually specify Workbench capabilities. Do not classify an entire mixed Scope Unit as Workbench merely because one Atom is included. Confirm exact membership in the first Task.

The review corpus is Current MED. Related R and O, the model, principles and inherited policies are context and may receive only necessary connected specification corrections through reviewed Drafts. I / Code Synopsis is the final evidence/disposition lane. Existing Archived Atoms are never edited. Existing unrelated Drafts are preserved; new refinement Drafts remain separate until adoption.

Preserve the 500 synthetic Atoms and their Scope Declaration in WORKBENCH_BURST_500_RENAMED. Retain the prior 78 content-unavailable Atom deferral explicitly; account for them as held, not reviewed or migrated. Reassess readability through query_run before reporting the final held count, without expanding into reader implementation.

No runtime, tool, code, deployment or release implementation belongs to this Epic. Its final output includes a separate Epic for accepted code changes.

## Inputs

- The Current sources after CA-P-2715, and the applied Engineering topic regrouping from this session. Do not replay the completed 740-Atom topic-only edit.
- Active model and principles, including CA-M-446 (DRY), CA-M-447 (MECE), and the latest Operator input.
- Current Form declarations CA-R-3002 (Solution), CA-R-3003 (Direct Policy), CA-R-3004 (Approach Policy), CA-R-3005 (Decision); Role and Form remain independent.
- CA-R-3010 for I / Code Synopsis, CA-R-970308624 for Work Report and CA-R-970308626 for IS_WORK_REPORT_FOR; active relation, Tier, Topic, Summary and Claim declarations.
- Discovery and analysis use query_schema/query_run/query_page with the explicit Project root. Missing readable content is a recorded hold, not evidence of complete review.

## Working procedure

Before each Task or subtask, review its inputs, scope and acceptance check; fix missing preparation first. Work in same-Scope batches of at most 15 minutes per assigned Agent, splitting or repeating a batch when needed. Use Terra and Luna where efficient, with at most one Scope Unit per subagent. Keep main judgments and final integration with the primary reviewer. Independent read-only reviews may run in parallel; overlapping source edits have one owner.

For each review point, run pass one → fix → pass two → fix/recheck. Then run the combined review again. If unsure, check the model, principles and latest Operator input. If still unsure, make the best bounded choice, create a C / Question with the context and consequence, and continue independent work. A Question records uncertainty; it does not silently override the model or Operator decisions.

Keep a small P / Work Report for every worked Task, using IS_WORK_REPORT_FOR, the same Summary and Container, and actual changes/checks/results/gaps. Do not create reports claiming work before it happens.

## Specification and tracking

Tasks describe work and acceptance. Changes to design, policy, behavior or delivery belong in RMEDO Drafts and adopted Atoms, never only in this Epic or a mapping file.

Use thin tracking: Atom ID | old topic | new topic | status. For non-topic changes, use a separate short Atom ID | Draft ID | Task | status index if needed. Create the updated Atom Draft when a concrete correction is ready. Keep findings and decisions in small Work Reports and, where needed, A / Spec Proposal or C / Question Atoms. Do not create a large duplicate specification or mapping document.

The prior in-place authorization applied to topic values only. Content, Form, relation and Tier changes in this refinement use reviewed Drafts and normal adoption; it does not authorize silent unversioned rewrites of those fields. Existing Archives stay unchanged. Normal new predecessor archives, if required on adoption by the active lifecycle model, are distinct from editing historical sources.

## Work order

Inventory → Engineering grouping → Draft preparation → one-claim and Claim-versus-Role review. MECE, DRY and Form reviews may use independent read-only lanes after that boundary check. Recheck topics after split/merge fixes; review owning Scope Units and broader/narrower placement after Form decisions; review relations after placement decisions; then policy alignment and Tiers. Correct combined findings twice before adoption. Finally revise Code Synopses, decide specification versus code corrections, and create the next Epic.

IS_BLOCKED_BY records actual prerequisites in the child Headers; the Epic does not duplicate inverse BLOCKS or CONTAINS lists. Parallel reviewers do not concurrently edit the same Atom.

## Role and Scope placement review

Check the actual Claim against its Role, and check owning Scope Unit against its responsibility, Scope Delegation and Scope Contract. Review Methodology-versus-Engine mismatches explicitly. Find candidates for promotion to a broader Scope Unit or demotion to a narrower one; preserve actual applicability, permissions and inherited constraints. Prepare in-scope changes in Drafts. Record out-of-scope moves as handoffs; do not silently expand this Epic. Recheck Form, topics, relations and Tiers after any supported Role or ownership correction.

## Tasks

- [x] [CA-P-2768 — Confirm the Engine refinement scope and inventory](CA-P-2767-EPIC--engine-spec-refinement-stage-two/01-CA-P-2768-TASK--confirm-the-engine-refinement-scope-and-inventory.md).
- [x] [CA-P-2769 — Group MED topics in the Engineering Aspect branch](CA-P-2767-EPIC--engine-spec-refinement-stage-two/02-CA-P-2769-TASK--group-med-topics-in-the-engineering-aspect-branch.md).
- [x] [CA-P-2770 — Prepare MED topic and content Drafts](CA-P-2767-EPIC--engine-spec-refinement-stage-two/03-CA-P-2770-TASK--prepare-med-topic-and-content-drafts.md).
- [x] [CA-P-2771 — Review and fix one-Atom one-claim boundaries](CA-P-2767-EPIC--engine-spec-refinement-stage-two/04-CA-P-2771-TASK--review-and-fix-one-atom-one-claim-boundaries.md).
- [x] [CA-P-2772 — Review and fix MED coverage with MECE](CA-P-2767-EPIC--engine-spec-refinement-stage-two/05-CA-P-2772-TASK--review-and-fix-med-coverage-with-mece.md).
- [x] [CA-P-2773 — Review and fix MED duplication with DRY](CA-P-2767-EPIC--engine-spec-refinement-stage-two/06-CA-P-2773-TASK--review-and-fix-med-duplication-with-dry.md).
- [x] [CA-P-2774 — Recheck and fix main topics and dependencies](CA-P-2767-EPIC--engine-spec-refinement-stage-two/07-CA-P-2774-TASK--recheck-and-fix-main-topics-and-dependencies.md).
- [x] [CA-P-2775 — Review and fix MED Forms](CA-P-2767-EPIC--engine-spec-refinement-stage-two/08-CA-P-2775-TASK--review-and-fix-med-forms.md).
- [x] [CA-P-2776 — Review and fix MED relations with Requirements](CA-P-2767-EPIC--engine-spec-refinement-stage-two/09-CA-P-2776-TASK--review-and-fix-med-relations-with-requirements.md).
- [x] [CA-P-2777 — Review and fix alignment with related MED policies](CA-P-2767-EPIC--engine-spec-refinement-stage-two/10-CA-P-2777-TASK--review-and-fix-alignment-with-related-med-policies.md).
- [x] [CA-P-2778 — Review and fix MED tiers](CA-P-2767-EPIC--engine-spec-refinement-stage-two/11-CA-P-2778-TASK--review-and-fix-med-tiers.md).
- [x] [CA-P-2779 — Review and fix the combined MED Draft set](CA-P-2767-EPIC--engine-spec-refinement-stage-two/12-CA-P-2779-TASK--review-and-fix-the-combined-med-specification.md).
- [x] [CA-P-2780 — Promote the reviewed MED specification](CA-P-2767-EPIC--engine-spec-refinement-stage-two/13-CA-P-2780-TASK--promote-the-reviewed-med-specification.md).
- [x] [CA-P-2781 — Revise Code Synopses against the refined specification](CA-P-2767-EPIC--engine-spec-refinement-stage-two/14-CA-P-2781-TASK--revise-code-synopses-against-the-refined-specification.md).
- [x] [CA-P-2782 — Create the follow-up Engine implementation Epic](CA-P-2767-EPIC--engine-spec-refinement-stage-two/15-CA-P-2782-TASK--create-the-follow-up-engine-implementation-epic.md).

- [x] [CA-P-2784 — Review and fix Claim versus Role mismatches](CA-P-2767-EPIC--engine-spec-refinement-stage-two/CA-P-2784-TASK--review-and-fix-claim-versus-role-mismatches.md).
- [x] [CA-P-2785 — Review and fix Scope Unit ownership mismatches](CA-P-2767-EPIC--engine-spec-refinement-stage-two/CA-P-2785-TASK--review-and-fix-scope-unit-ownership-mismatches.md).
- [x] [CA-P-2786 — Review and fix broader and narrower Scope placement](CA-P-2767-EPIC--engine-spec-refinement-stage-two/CA-P-2786-TASK--review-and-fix-broader-and-narrower-scope-placement.md).

## Additional Decision reviews

- [ ] [Review Decision promotion candidates](CA-P-2767-EPIC--engine-spec-refinement-stage-two/CA-P-2833-TASK--review-decision-promotion-candidates.md)
- [ ] [Review Decision merge candidates](CA-P-2767-EPIC--engine-spec-refinement-stage-two/CA-P-2834-TASK--review-decision-merge-candidates.md)

## Definition of Done

The admitted Current MED corpus is accounted for and grouped by Engineering topic; Claim-versus-Role, owning Scope Unit and broader/narrower placement are explicitly checked; every requested review point has recorded review-and-fix passes, followed by a combined recheck. Accepted specification Drafts are adopted and queried back; every retained or deferred source is explicit. Related R/O corrections stay bounded. Revised Code Synopses identify what should be adopted into RMEDO and what should change in code, with actual code evidence. A separate implementation Epic contains the accepted code work. Each worked Task has a small Work Report; unresolved Questions remain visible. Existing Archived sources, the benchmark corpus and unrelated work are preserved. No code implementation or release is claimed by this Epic.

## Completion

Completed the bounded source refinement on 9 November 2026. Adopted 256 Current Atoms and retired 9 predecessors; 75 MED retain the prior Content deferral and seven additional Current sources retain C707–C710 handoffs. I7–I9 and implementation-map.tsv describe actual code evidence. CA-P-2791 carries the subsequent implementation work, including C711. No code implementation, local release, native Workflow execution or native Codex rendering is claimed here.

## Open Questions and Operator decisions

- C707 — Resolved: M417 is absorbed by M284@30 and M426 by M425@14. Adopted the six resumed Evaluations and repaired already-reviewed M399/E648 links and Tiers. All ten Current changes and both retirements were queried back after a derived-index reread. The remaining prior hold is 69 MED; every other source deferral is unchanged.
- C708 — Awaiting Operator decision: where should M327/M328 live: FRAMEWORK_ENGINE (the proposed shared engineering owner), Core methodology, or PROGRAMMATIC only? Review the actual Claims and their consumers before moving anything.
- C709 — Awaiting Operator decision: D576/E582 reference M339/R1882, which do not resolve as Current authorities. Do not invent replacement authority.
- C710 — Awaiting Operator decision: release-specific D577 ownership needs a bounded Project/release handoff.
- C706 is Resolved. C711 is a confirmed editor code defect carried by implementation Epic CA-P-2791, not an unanswered specification Question.

Resolve the Questions one at a time with context, proposed disposition and impact. The Operator approved adding and executing Decision-promotion and merge reviews (P2833/P2834), but asked to settle these Questions first. Do not automatically promote all Decisions, change a Form because its Atom is large, or resume unrelated deferred sources. New review decisions belong in RMED Drafts; Tasks and Work Reports track actual work.

## Reopened work

The Operator reopened Stage 2 for Decision promotion and merge reviews. Resolve the existing Questions one at a time first. C707 resumes only E260/E261/E360/E361/E366/E454 and their two approved Method absorptions; every other deferral remains unchanged.

## C707 completion

Ten Current Atoms adopted and two duplicate predecessors retired, with preserved history and replacement links. C707 is Resolved; C708–C710 remain pending. C712 records the observed stale-delete indexing defect for the implementation Epic. General Decision promotion and merge reviews remain open; settling C707 does not mark P2833/P2834 Done.
