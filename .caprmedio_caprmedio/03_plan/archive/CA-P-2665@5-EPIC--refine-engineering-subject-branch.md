---
atom_id: CA-P-2665@5
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering
version: 5
updated_at: 2026-10-27 01:05:49 +0400
relations: {}
tier: 3
---
# Summary

Refine Engineering Subject branch

## Objective

Make the Engineering Subject branch coherent and readable by correcting the source Subjects, then rebuilding the derived views.

## Details

### Accepted structure and meaning

- Engineering currently uses Continuant, Occurrent and Aspect. The category list remains open. Technical things, actual technical activity and topics have different meanings.
- Subjects name the governed thing or topic, independently of Content Roles, owning Scope Units and tool names. Do not merely relocate a copied Scope Unit or module name into the tree. Use reusable topics from the actual Claim. A particular object remains legitimate where the Claim truly governs it.
- Reuse the accepted Architecture, Authoring, Verification, Delivery, Storage, Data Handling and Execution Control topics. Check all loose Engineering Subjects, not only the initial Git and Implementation examples.
- Git commit objects and committing policy are distinct; duplicated meanings are consolidated without conflating them.
- `Engineering/Continuant/Implementation` is accepted for actual realization, including code, tests and configuration. Implementation remains a Content Role. Authoring and verification topics stay separate.
- `Engineering/Aspect/Traceability` covers evidence-to-realization and authority-to-target links. Preserve Authoring and Static Analysis where those are the actual governed aspects.
- General confidence rules use `Engineering/Aspect/Execution Control/Decision Confidence`. Concrete Plan and Settings properties remain under their own bearers.
- Framework capability promises use the existing `Product: CAPRMEDIO Framework` Subject. Installation, configuration and runtime details use their own Engineering Subjects.
- Release is `Engineering/Continuant/Release`; its ID is called Version. This supersedes the proposed Product.Version placement. Local and public release are Workflows, not Release Types. Use the exact named Workflow Subjects `Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow//Local Release` and `...//Public Release`. Workflow-specific RMED and these concrete Workflow definitions belong in PROJECT_CONFIGURATION. Do not create another Releasing/Versioning process taxonomy merely to repeat the Workflows.

### Scope and sequence

Use the Current RMEDO sources behind the full Subject graph, regardless of owner. Engineering Subjects are not synonymous with the Engine subtree. Preserve existing Drafts, Archives and unrelated work. No new Domain entity without the Operator.

1. Review Governs meanings first, then Depends On. Ask one question with source context and blast radius only where confidence is below 90%.
2. Create real correction Drafts as soon as supported. Maintain only the thin table: `Atom ID | old Subject | new Subject | status`. Keep proposed Atom content in the Drafts; do not create a large mapping report.
3. Complete the accepted release-model Drafts and bounded Project Configuration placement in P2672. Rename the two Workflow instance references coherently; preserve existing Atom Summaries and IDs. Child Steps and workflow-specific source rules must have coherent ownership before promotion.
4. Review and apply accepted Drafts, preserving normal predecessor history. Summary or Content Role changes require a new Atom ID. Stop on failed changes and record actual progress.
5. Rebuild the four Current-source views and verify meanings, duplicate removal, operator use, properties, instances and coverage. Zero unmapped Subjects alone is insufficient.

No code, tools, runtime, release execution, general Scope Unit restructure or Terms Graph implementation. The release-model placement above is the explicit bounded ownership exception; it does not start the broader Engine migration. Broader content migration remains separate. Update defining content only where needed for an accepted model or the two Workflow names; do not add operational policy while remapping.

### Dependency-only graph section

P2671 adds a fourth section reporting exact Subject values present in `subjects.depends_on` but absent from every selected `subjects.governs`. Use the view's own Current source set, exact full-string equality, sorted paths and sorted deduplicated referring Atom IDs. Do not propagate ancestors or remove targets from the other sections. The four Current views now include this section; counts are 54 / 107 / 248 / 236 for Core / Project Methodology / Engine / Full before Draft promotion. This is a review aid, not an automatic missing-definition verdict.

### Evidence and coordination

Initial inventory: 2,363 Engineering links, 300 distinct Subjects, 1,347 Current source Atoms. The tracker is `.caprmedio_tmp/engineering-subject-review/subjects.md`; source proposals are canonical Draft Atoms. Independent batch checks and projection receipts live beside the tracker. Current RMEDO source heads remain unchanged during preparation. Draft preparation, source application and projection verification are separate states; this Epic is not complete.

P2639 remains Done for its bounded FPF findings. [P2637](CA-P-2637-EPIC--migrate-engine-rmed-atoms.md) consumes this Engineering branch rather than repeating the review. No runtime or code completion is implied.

## Definition of Done

- Every selected Engineering occurrence has an evidenced disposition: retained, mapped, or explicitly unresolved with an Operator decision needed.
- Accepted category and topic meanings appear in Current sources after reviewed promotion.
- Git, Implementation, Traceability, Decision Confidence and release-model decisions are applied without losing distinct meanings or obligations.
- Workflow-specific release definitions and RMED have coherent PROJECT_CONFIGURATION ownership; two Workflow names resolve to their real definitions without duplicate identities.
- Supported changes have checked Drafts, successors and predecessor archives; unrelated sources/history remain intact.
- Four rebuilt views reflect Current source pins and the exact dependency-only section; remaining gaps are explicit.
- No unrelated source, implementation, test-suite, release or Git work is claimed complete.
