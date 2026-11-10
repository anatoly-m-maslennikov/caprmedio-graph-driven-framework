---
identity:
  id: CA-P-2767
  ref_id: CA-P-2767@19
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
  version: 19
  updated_at: 2026-11-09 23:46:00 +0400
destination:
  file:
    name: CA-P-2767@19-EPIC--engine-spec-refinement-stage-two.md
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

- [x] [Review Decision promotion candidates](CA-P-2767-EPIC--engine-spec-refinement-stage-two/CA-P-2833-TASK--review-decision-promotion-candidates.md)
- [x] [Review Decision merge candidates](CA-P-2767-EPIC--engine-spec-refinement-stage-two/CA-P-2834-TASK--review-decision-merge-candidates.md)

## Definition of Done

The admitted Current MED corpus is accounted for and grouped by Engineering topic; Claim-versus-Role, owning Scope Unit and broader/narrower placement are explicitly checked; every requested review point has recorded review-and-fix passes, followed by a combined recheck. Accepted specification Drafts are adopted and queried back; every retained or deferred source is explicit. Related R/O corrections stay bounded. Revised Code Synopses identify what should be adopted into RMEDO and what should change in code, with actual code evidence. A separate implementation Epic contains the accepted code work. Each worked Task has a small Work Report; unresolved Questions remain visible. Existing Archived sources, the benchmark corpus and unrelated work are preserved. No code implementation or release is claimed by this Epic.

## Completion

Completed the bounded source refinement on 9 November 2026. Adopted 256 Current Atoms and retired 9 predecessors; The original phase held 75 MED and seven additional C707–C710 sources. The later approved follow-ups resolved those handoffs; 69 MED remain deferred after C707 resumed six Evaluations. I7–I9 and implementation-map.tsv describe actual code evidence. CA-P-2791 carries the subsequent implementation work, including C711. No code implementation, local release, native Workflow execution or native Codex rendering is claimed here.

## Resolved Questions and Operator decisions

- C707 — Resolved: M417 is absorbed by M284@30 and M426 by M425@14. Adopted the six resumed Evaluations and repaired already-reviewed M399/E648 links and Tiers. All ten Current changes and both retirements were queried back after a derived-index reread. The remaining prior hold is 69 MED; every other source deferral is unchanged.
- C708 — Resolved: M327@13 and M328@15 are owned by FRAMEWORK_ENGINE; R2653@2 grants their receiving Scope admission and preserves the structural tree. Legacy Forms became default Decision. P2833 subsequently promoted both Methods to Direct Policy and adopted the matching R2653 admission.
- C709 — Resolved: D576@14 and E582@15 are Archived without replacements; C470 is Resolved as obsolete. C496/C497 remain byte-for-byte unchanged. Current R1847/D547 release contracts and runtime code were not altered by this cleanup.
- C710 — Resolved: FRAMEWORK_DELIVERY reuses CA-SU-27 at Project level. The complete local/public release specification families have moved; all 80 ownership changes and the stable Scope Unit were queried back. Runtime/code relocation is deferred to P2839 in P2791.
- C706 is Resolved. C711 is a confirmed editor code defect carried by implementation Epic CA-P-2791, not an unanswered specification Question.

Resolve the Questions one at a time with context, proposed disposition and impact. The Operator approved adding and executing Decision-promotion and merge reviews (P2833/P2834), but asked to settle these Questions first. Do not automatically promote all Decisions, change a Form because its Atom is large, or resume unrelated deferred sources. New review decisions belong in RMED Drafts; Tasks and Work Reports track actual work.

## Reopened work

The Operator reopened Stage 2 for Decision promotion and merge reviews. Resolve the existing Questions one at a time first. C707 resumes only E260/E261/E360/E361/E366/E454 and their two approved Method absorptions; every other deferral remains unchanged.

## C707 completion

Ten Current Atoms adopted and two duplicate predecessors retired, with preserved history and replacement links. C707 is Resolved; C709 and C710 were resolved by the subsequent approved tasks. C712 records the observed stale-delete indexing defect for the implementation Epic. General Decision promotion and merge reviews were subsequently completed under P2833/P2834; settling C707 alone did not complete them.

## C708 completion

The approved Method moves and receiving delegation are adopted and queried back. C707–C710 are now Resolved. P2833 and P2834 are Done after a fresh post-release inventory, two review passes, reviewed Draft adoption and Current query readback.

## Whole-project release ownership

The Operator approved FRAMEWORK_DELIVERY as the peer responsibility for local and public release, including their complete Workflow/specification families. Existing RELEASES / CA-SU-27 is the unit to reuse; do not create a duplicate responsibility. Preserve its ID and history. Record the related Scope declaration, Goal and affected RMEDO in Drafts before adoption. The Operator chose specification adoption now and code/test relocation in P2791, Task P2839. No code relocation is part of this source pass.

## Additional ownership task

- CA-P-2837 — Establish FRAMEWORK_DELIVERY and move release families. Done; resolves C710 and the Operator-approved complete local/public release ownership. The reviewed specifications are now Current RMEDO.

## Verified release ownership result

Moved 80 Current release-specific RMEDO Atoms into FRAMEWORK_DELIVERY / CA-SU-27, including all 26 release Operations and both complete registered Workflow graphs. Replaced R2666@1 with R3012@1 as the Project-owned Scope Delegation; kept order 5, the 48-unit census and the external R1181 Goal. Adopted five supporting corrections. All 86 predecessors are archived, with their original Markdown payloads preserved. Query readback verifies every adopted ID, Version, path and owner. All 69,409 original protected files are unchanged. Generic Engine policies and integration checks stayed with their owners. No code, tests, runtime execution or publication changed. P2839 queues implementation/test relocation. Pre-existing content references O184/O186 and archive-only D572 remain explicit follow-up, not invented replacements; legacy unreadable D021 is unchanged.

P2833 and P2834 are Done. Resolving the original Questions was followed by the full refreshed Decision review and verified adoption recorded below.

## Earlier Decision-only review result

Reviewed all 89 Current MED Decisions in ten eligible Engine Scope Units with local and ancestor policy context. Pass two corrected an overly broad full-Scope test for Solution: a coherent responsibility contribution need not cover every feature in one Atom. Promoted 16: M327/M328 to Direct Policy; M153/M175/M193/M302/M317/M401/M466/M506 and D547/D548/D593/D675/D681/D704 to Solution. Seven receiving Scope Delegations now admit those exact Forms and existing Subject endpoints; the PROMPTS declaration is normalized to its parent-owned delegation without changing the Scope Unit tree. Adopted 24 sources in total, including the E067 carrier-link repair. Query readback verified every changed and retained ID, Version, Form, owner and path. No native UI, code implementation or release is claimed.

Reviewed all 89 Decisions against the readable local/ancestor Solutions and Policies. The earlier Decision-only review found no additional merge under its then-current criterion: architecture, specific choices, Method and Delivery, machine/human reports and per-invocation carriers preserve distinct claims or consumers. The two earlier C707 duplicate Method absorptions remain verified. Removed only two duplicated HTTP/delivery paragraphs from M466; their actual delivery authorities remain D674/D673/D639, with D674 unchanged. No new retirement or successor ID was needed. All 69 held MED and original protected files are unchanged.

All 21 worked Tasks in this Epic are Done. The 48-unit structural tree is unchanged. CA-I-7, CA-I-8 and CA-I-9 still describe the inspected implementation: these Form and permission changes introduce no new implementation behavior, so their factual code observations remain valid. Their old source/module pins and the confirmed C711/C712 code defects remain for CA-P-2791, as does release implementation/test relocation P2839. No implementation task was started while closing this specification Epic.

## Reopened Summary merge pass

CA-P-2840 applied the latest Operator merge criterion across the captured Current RMEDO frontier, superseding the earlier narrower merge conclusion. Review, adoption and fresh query acceptance are complete. The 69 prior MED holds remain. The 44 additionally discovered R/O are now query-readable after the approved structure-only repair. Their topic review is complete: 27 corrected in place and 17 retained, with content and non-topic properties unchanged; merge dispositions are complete. The benchmark declaration is excluded with its corpus.

## Verified first Summary merge batch

Five groups are adopted and queried back under P2840: R1605 ← R1522; R1107 ← M169; R1116 ← M178; M509 ← D705; R2782 ← D676/D677. M513 records the merge Method. Fifteen Current sources and 20 predecessor archives are verified. Connected references are repaired. C712 still requires its queued implementation fix; a full reread cleared the stale deleted rows for acceptance. This was the first checkpoint; the final verified result follows.

## Final Summary-merge result

P2840 and its Work Report P2841 are Done. Applied 33 groups and retired 48 predecessor contracts across the two Summary batches. M513 records the Operator's merge criterion; R3013 is the new registry Requirement identity. The final adoption contains 66 Current records, 42 retirements and 107 new predecessor archives, including the three C713-authorized reference-only external caller repairs and the resolved scope Question. Query readback verifies exact Current identities, Versions, paths, Statuses, declared Claim/Operation visibility and repaired relations.

All six remaining proposed groups are explicit holds tied to 20 deferred Evaluation consumers; no part of the 69-MED hold is silently resumed. R1076/M153 are retained as distinct outcome and supporting procedure. The thin summary-merges.tsv contains all 33 applied groups, six holds and that retained pair. The benchmark corpus, 48-unit tree and 69,409 original protected files remain unchanged. C712 and native rendering concerns remain unresolved implementation evidence; a full reread supplied source acceptance only.

P2791 is the next implementation Epic. Its input confirmation follows Current replacement lineage and reconciles factual old Synopsis/module pins. The three requested audit-table tasks P2842–P2844 remain Backlog there. Two concurrent source-lane additions, M514@2/M515@2, were preserved outside this captured merge batch; their missing query Claim extraction is recorded for the existing Backend/input audit work. The latest case-insensitive Current RMEDO census is 395, including those two additions; 393 belong to this pass's resulting captured frontier. No implementation or release task was started to close this specification Epic.

## Reopened Code Synopsis review

The Operator reopened this Epic to review the recently created I / Code Synopsis sources. P2845 reviews I7, I8 and I9 against the Code Synopsis definition, actual code and the final adopted RMED baseline. P2840 remains Done; its Summary merges and explicit holds are not replayed. Source review is active again. Implementation work remains in P2791.

- [x] [CA-P-2845 — Review recent Code Synopses](CA-P-2767-EPIC--engine-spec-refinement-stage-two/CA-P-2845-TASK--review-recent-code-synopses.md)

## Code Synopsis review result

P2845 is Done with an explicit MCP source hold. I7/I8 at Version 2 now expose their code evidence through Prose Claim and preserve their Summaries and ownership. Frontend completion defects are confirmed for P2812; no code change was made. C712 still requires runtime reproduction/acceptance under P2813. I9 remains Current Version 1: concurrent MCP code changes removed its registration location and prevented a stable adoption check. Its owned Draft is held under C714. This Epic remains Active for the follow-up source review.

- [ ] [CA-P-2847 — Refresh the MCP Code Synopsis after refactoring](CA-P-2767-EPIC--engine-spec-refinement-stage-two/CA-P-2847-TASK--refresh-the-mcp-code-synopsis-after-refactoring.md)

The Operator’s Code Synopsis closure decision is recorded in R3010 Version 3 Semantics, including the qualified Resolved allowed value. This was a bounded explicit declaration update; code and existing I statuses were unchanged.
