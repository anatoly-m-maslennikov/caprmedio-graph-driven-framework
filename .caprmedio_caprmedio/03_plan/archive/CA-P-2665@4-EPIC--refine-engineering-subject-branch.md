---
atom_id: CA-P-2665@4
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering
version: 4
updated_at: 2026-10-26 23:58:51 +0400
relations: {}
tier: 3
---
# Summary

Refine Engineering Subject branch

## Objective

Make the Engineering Subject branch coherent and readable by correcting the source Subjects, then rebuilding the derived views.

## Details

### Why this is a new Epic

P2639 completed its bounded FPF findings. Zero unmapped Subjects did not establish semantic coherence. The Operator identified remaining duplicates and mixed categories in Engineering. This Epic addresses those problems without reopening the completed review or starting the broader Engine migration.

### Accepted direction

- Organize the current Engineering branch under Continuant, Occurrent and Aspect. These are the current organizing categories, not a closed universal list.
- Continuant covers persistent technical things; Occurrent covers actual technical activity; Aspect covers topics such as Architecture, Authoring, Verification, Delivery and Storage. Do not classify a topic as a running process merely because its name contains an action.
- Subjects name the governed thing or topic. Keep Subjects independent from Content Roles, owning Scope Units and tool names. No new Domain entity without the Operator. A correction is not complete if it merely moves a copied Scope Unit, Tool or module name under Continuant or Aspect. Use shared topics from the actual Claim; ownership already supplies the local context. Retain a particular technical object or instance only when the Atom truly governs it, not merely because the work occurs in that Scope Unit.
- Review `Git/Commit`, `Git Commit` and `Aspect/Delivery/Git Commits` together. Merge duplicate meanings; preserve a real distinction between a commit object, a running operation and a policy topic where the source content supports it.
- Review Implementation, Implementation Authorization, Binding, Cohesion, Evaluation, Failure Diagnosis, Folder, Preparation and Reconstructability. Map by meaning, not their shared prefix. Reuse accepted Aspect topics before proposing another branch.
- Inspect the remaining Engineering branch too, so this is not merely a cosmetic fix for those examples. Detect duplicate meanings, mixed classification axes, wrong `/` versus `.`, and names that merely copy a tool or Scope Unit.

### Scope and order

Use the Current RMEDO sources behind the full Subject graph, regardless of owning Scope Unit. Engineering Subjects are not synonymous with the Engine Scope Unit subtree.

1. Inventory Governs and group actual source meanings; then inspect Depends On.
2. Confirm the target branch and record only concrete unresolved choices with context and blast radius. Ask one question at a time when confidence is below 90%.
3. Create correction Drafts immediately for supported mappings. Use a thin register: `Atom ID | old Subject | new Subject | field | status`. Do not create a large mapping framework.
4. Review Drafts, archive predecessors and promote accepted corrections. Keep summaries and obligations unless a separately reviewed correction requires changing them. Summary or Content Role changes require a new ID.
5. Rebuild the four existing Subject views and check semantic placement, duplicates, rooting, properties, instances and source coverage. Zero unmapped Subjects alone is insufficient.

Preserve existing Drafts, Archives and unrelated work. No code, tools, runtime, release, general Scope Unit restructure or Terms Graph implementation. Broader content migration remains separate; change defining content only when needed for an accepted Subject-model correction. Do not invent missing policy while remapping.

Coordinate with [P2637](CA-P-2637-EPIC--migrate-engine-rmed-atoms.md): this Subject cleanup supplies its Engineering branch; do not repeat it there. The work begins with source review, not with an automatic bulk rewrite.

### Projection addition — dependency-only Subjects

P2671 adds a fourth section: Subjects explicitly present in `subjects.depends_on` but absent from `subjects.governs` in the view's source selection. Use exact canonical values, list referring Atom IDs and sort alphabetically. Do not infer an explicit Governs occurrence from hierarchy membership. Preserve the existing three sections and update the relevant methodology Drafts before the local rebuild. This is a review aid, not another Subject root or an automatic missing-definition verdict.

### Preparation evidence

The initial review inventory covers 2,363 Engineering links, 300 distinct Subjects and 1,347 Current Atoms. Thirteen Drafts are prepared; their initial independent check passed. The thin tracker is `.caprmedio_tmp/engineering-subject-review/subjects.md`. Current RMEDO sources have not been changed by this preparation. Remaining mappings and questions are still under review; this is not migration completion.

### Implementation placement — latest Operator decision

The Operator accepted `Subject/Graph Node/Engineering/Continuant/Implementation` for now. It names the actual realization, including code, tests and configuration. Implementation remains a Content Role; authoring, verification and other policy topics still use their own Aspect Subjects. Apply this by source meaning, not as a blanket rename of Implementation Binding or Reconstructability. R1504, R1610 and R1873 have corresponding Draft corrections.

### Current preparation state

The thin four-column tracker now covers 109 changed Atom IDs; three additional layout/taxonomy definition Drafts bring the prepared total to 112. The first 13 passed independent review; the expanded batch is under independent review. No Current RMEDO Atom has been changed. The fourth dependency-only section has been generated from Current sources in all four views, with 54 / 107 / 248 / 236 targets for Core / Project Methodology / Engine / Full respectively. Those counts describe Current sources, not the proposed Draft tree. Framework Instance versus Product placement remains an Operator question; no conclusion is inferred.

## Definition of Done

- Every selected Engineering Subject occurrence has an evidenced disposition: retained, mapped, or explicitly unresolved with an Operator decision needed.
- The agreed categories and topic meanings are reflected in Current source Subjects, not only a proposed tree.
- Duplicate Git meanings and scattered Implementation topics are corrected without losing real distinctions or obligations.
- Supported changes passed Draft review, predecessor archival and successor readback.
- The four projections are rebuilt from the actual Current sources; remaining gaps are explicit.
- No unrelated source or implementation work is claimed complete.
