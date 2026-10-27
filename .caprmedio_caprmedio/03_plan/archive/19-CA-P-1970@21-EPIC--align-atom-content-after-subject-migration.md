---
atom_id: CA-P-1970@21
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 19
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Engineering/Tool
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 21
updated_at: 2026-10-25 16:29:30 +0400
relations: {}
tier: 3
---
# Summary

Align Atom content after Subject migration

## Objective

Align Summary, Substance, Substance Scope and Details with the verified Subject model, only after Step 1.

## Details

### Known content follow-ups from Methodology verification

Source audit950 records E383/E444's old Method-root fixtures, R1947's stale
later-status-alignment note, and D393's unresolved default external-Type branch.
Review their exact meanings in this existing Content Epic; do not restore R2005,
invent a Domain entity, alter historical fixtures blindly, or reopen the frozen
Terms Graph. This handoff does not rewrite any RMED body or expand P1959.

### Latest Epic boundary — 2026-10-25

Finish Methodology first in CA-P-1959 and its retained work. All Engine RMED
migration belongs to the separate Backlog Epic CA-P-2637, including PROGRAMMATIC,
APPS, TOOLS and other Engine descendants. Do not execute that migration here.
The later Engine Epic starts with Subject-system and Scope Unit review.

No code/runtime implementation is included in either migration. Preserve
Engine work already applied or proposed; do not undo it or promote more Engine
proposals ahead of the Methodology gate. Earlier combined-pass wording and
all-pass completion gates below are superseded by this boundary.

Methodology keeps the approved order: Subjects → missing Atoms → archive
obsolete Atoms → properties → Content. General Content work stays under
CA-P-1970@21. Terms, instance naming, conflict-workflow updates and protected
owners retain their explicit deferrals.


### Latest Operator order — 2026-10-25

Run these stages in order:

1. Migrate Subjects.
2. Add missing Atoms.
3. Archive obsolete Atoms.
4. Fix properties.
5. Update Atom content last, under CA-P-1970@21.

Complete the Methodology pass first. Then repeat the sequence for PROGRAMMATIC
RMED Atoms only. No PROGRAMMATIC code or runtime implementation is authorized.
Do not interleave new PROGRAMMATIC corrections ahead of Methodology's pass.
Preserve work already applied or staged; this order is not a rollback.

Create new proposed revisions as Drafts and refine them in iterations. Keep
Current originals unchanged until a proposal is ready and applied. Preserve
existing Drafts, Archives, protected owners and explicit deferrals. Stage a
concrete uncertain proposal without claiming it is approved; ask the Operator
only where refinement still requires a real decision.

Stage 1 changes Subjects, not ordinary Content, properties or lifecycle state.
Later-stage gaps may be inventoried now, but are not permission to execute them
early. Normal maintenance of these execution Plans records the new order; it
does not count as migration of a model Atom's Content.

Mapping, application and verification are per-pass milestones. Methodology
completion opens Methodology content work; it must not wait on the later
PROGRAMMATIC pass. Verify each pass separately before its content stage.
Keep CA-P-1959 Active while its retained work remains unproved. Earlier mixed
increment schedules and global all-pass wording below are historical where
they conflict with this order.


### Shared storage policies — Operator decision, 2026-10-14

Use the carried property as the Subject of its D storage rule: `Atom.Status`
plus Content Role D means how Status is represented, for example `status` in
YAML. A per-property Carrier Subject or entity is unnecessary. Keep Carrier
Subjects for rules about actual files, folders and their components.

After the Subject-migration gate, consolidate repeated storage definitions
into shared D policies for YAML frontmatter in Markdown. Do not require one
D Atom for each Property, Content Role or Type. Preserve real exceptions and
constraints; identify redundant rules before any authorized retirement. This
records the requested direction, not new storage syntax, immediate deletions
or permission to start the deferred content migration.

### Narrow Tools prerequisite authorized separately

The Operator separately authorized alignment of only two existing rules needed by the rebuilt Tools: every actual same-ID update increments Version by exactly +1 (an exact no-op preserves Version/time), and retained predecessor history preserves its exact old bytes. This permits the directly contradictory Core Requirements, Operations and Evaluation clauses to be aligned, including retiring the obsolete carrier-only Version-preservation exception. It does not authorize Candidate #4 content adoption, Subject migration, Terms work, filename/schema migration or the rest of this Epic. Independent source acceptance and affected review/consumer verification remain required before use.

The deferred gates below continue to apply to all broader content work; this narrow prerequisite is not completion of CA-P-1969 or this Epic.


This is the separate retained content Epic, no longer a decomposition of CA-P-1959. It remains Active and deferred. The current Operator request authorizes only staged Subject migration; it does not authorize preparing or applying this Epic's content/consumer changes. Obtain separate execution authority and the relevant Subject/live gates before its future work.

Receive the explicit future-work queue required by the [approved content-conflict exclusions](../../.caprmedio_tmp/stage2-migration-20261012/model/content-conflict-decision.md), SHA-256 `6f5bdf81ae3861bd2141df69ba7ffa936f78cf7fef0ac0b8f2ae8290c17d09fc`: each whole original Atom whose content is independently confirmed to contradict the new model remains unchanged during Subjects-only staging and retains its ID, Version, source hash, contradictory source and candidate/Operator evidence, and reason. The complete Subject ledger must keep those owners visible in inventory/graph coverage and distinguish them from uncertain mappings or unreviewed omissions. Listing that queue does not start this Epic, prepare its deferred child work, authorize body changes or waive CA-P-1969 and separate execution authority. Reopen current source pins and the additive compact scope-reference decision before any later content review; old queue/report acceptance is not current content-patch approval.

Reviewed unresolved whole owners follow the [separate unchanged-owner decision](../../.caprmedio_tmp/stage2-migration-20261012/model/unresolved-owner-decision.md), SHA-256 `d325383d4d4b049347bc77381e3f17616d3a473d93fce587c6b23a11e0ad9912`. They stay wholly unchanged and unstaged with exact pins, affected occurrences, reason and open question; they are not confirmed content conflicts or automatically this Epic's queue. Subjects-only staging still requires complete 907-owner/4534-occurrence review and current independent acceptance of every disposition. No content edit or completion is authorized by this guidance update.

The detailed identity/Terms planning formerly embedded in the parent remains in [historical CA-P-1959 v54](archive/18-CA-P-1959-EPIC--improve-entity-model-stage-2@54.md). Retain that context for this Epic's future review alongside current governing RMEDO and later Operator decisions; historical scope wording grants no execution authority.

This grouping Plan has no own implementation work. It is blocked by CA-P-1969. Do not prepare or apply content replacements before that gate passes.

After the gate, inventory current **NON-ARCHIVED** eligible RMEDO source versions and create disjoint, at-most-15-minute child Tasks by role and source batch. Review and propose exact changes before applying them; resolve concrete conflicts below 90% confidence with the Operator. Task creation does not approve the content patches.

Use Substance as the umbrella: RMED contains Claims; O contains Operations. Keep Summary short and distinct from Substance. Substance Scope means applicability, not owning Scope Unit. Omit it only when the Substance concerns the whole Subject AND the whole owning Scope Unit. Details are optional where the Type permits them; preserve conditional/type-specific requirements.

The prospective model is [Candidate #4](../_projection/core-entity-review/presentation/operator.model.candidate-4.md), SHA-256 `6e63d7362514ef20c2551366777073c22300b35a9cef5ad79531ad56b770763d`. Entity is only the umbrella. The three top-level branches are Occurrent, Continuant and Carrier. Continuant explicitly excludes Carrier and contains Object, Actor, History, Projection and Selection. Object is authoritative content about what/how; Actor is who. Actual executions and sessions are Occurrents, not their Journal records. History contains Journals, records and Revisions; Projections are derived content, including Terms Graph. A Selection is a rule/expression; running it is an Occurrent, and a saved/tracked result is a Projection. A Carrier bears a representation without becoming that content. Term annotations preserve source meanings, allowed values and derived vocabulary, not another root. No new native Relation semantics, parser/schema change or Core adoption follows from this candidate. Before execution, inherit CA-P-1959's Candidate #4 review and repair gate, including the completed historical review, Operator dispositions and bounded independent consistency verification of the authorized repairs against the revised target. Affected work waits for that parent check; revised bytes do not inherit the historical analytical PASS. The unchanged full FPF review is not rerun, and no Core adoption or migration is implied. Earlier descendant references and historical receipts do not establish current acceptance. Reopen current evidence and obtain separate authority before deferred content work. R describes the skeleton and required outcomes; M methods; E checks; D carriers/storage/delivery; O repeatable actions/workflows. M/E are views, not new roots. Keep general D policies, not per-property Carrier registries. Preserve internal/external/relational distinctions and meaningful constraints.

Adopt the semantic names `Atom.ID` and `Scope Unit.ID` while retaining the existing storage keys. Keep `Atom` distinct from lowercase `atom`. For an ordinary identity-preserving update, select the current original NON-ARCHIVED Atom, create exactly Version `+1`, and archive the previous original without a second version bump; the original need not be Active. A Type change instead creates an entirely new Atom and new ID, then archives the old Atom. Any Summary change, including wording-only, creates a new Atom with a new ID and archives the previous Atom; Type is not the sole replacement trigger. Stored IDs remain bare; archived originals share the ID at distinct Versions. Atom filenames in all statuses use `AtomID@Version-SCOPE_NAME--summary.md`, with `@` filename-only; references use ID plus Version.

Put the affected Tools first within Step 2: review/update and independently verify RMEDO, align and independently verify the existing D-approved carrier/reference and identity consumers, Applicable Methodology compiler and Terms builder, then use them in affected content/consumer work. CA-P-1974 creates the bounded children after the Subject gate. Do not perform renames during this Plan edit; this Plan does not authorize an automatic runtime or release rebuild.

For Applicable Methodology, select current NON-ARCHIVED eligible source versions and preserve source ID, Version and authored content. Only projected Status and provenance may differ. Project Configuration authors corrections first; then select and project one whole lifecycle, with no independently versioned member. A projection is reusable and non-authoritative.

Classify each proposed change before writing under current authority. A changed Summary requires replacement with a new Atom ID and recorded predecessor/successor lineage; do not perform a same-ID Summary update. Same-Summary Substance/Scope/Details changes use the applicable semantic-revision or refinement route. Every accepted same-ID update still uses exact Version +1 and actual updated_at under the Operator's latest rule. Preserve meaning, status/history and actual recording. No schema or YAML heading/key rename, Scope Unit folder/ID migration, entity deletion or Term change is silently authorized.

Output: reviewed and authorized source changes, exact before/after pins and batch receipts.

### Terms Graph work after the Subject gate

Include the Terms Graph decisions recorded in CA-P-1959 and Candidate #4. Definitions are derived from source cases and optional Semantics, without a separate definition-owning layer. Preserve source authority, reusable derived output, shared meaning with locally constrained allowed values, scoped meanings and visible conflicts where incompatible meanings apply to the same case.

Use this order for the affected work:

1. Review current Core and Engine graph RMEDO and identify definition-only assumptions, source evidence requirements and affected consumers. Prepare exact revisions/replacements and acceptance cases.
2. Apply and independently verify the accepted RMEDO changes, preserving source Claims, history and admitted Relation meanings. Do not retire every Definition Atom as a blanket migration.
3. Align the existing Terms Graph builder, extraction and diagnostics with those contracts before affected content or consumer usage. Reuse CA-P-1872's graph work; bind affected Engine files and isolated fixtures to disjoint child owners.
4. Independently verify source traceability, reuse, allowed-value differences, scoped conflicts, unresolved evidence and rebuilding after fixture source changes before affected use; supply the results to CA-P-1971. Actual derived Terms compilation remains Step 2 and follows those gates.

CA-P-1974 must decompose these responsibilities into bounded child Tasks only after CA-P-1969's complete current receipt, before execution. A Phase-2 plan is not permission to perform content work during Step 1. Updating this Plan records planning only; it does not start Core adoption or implementation.

CA-P-1974's preparation alone cannot complete this group. Require the generated role/batch review, authorized effect and independent verification children and their actual outputs. Record the Summary replacement policy in each affected patch packet before approval.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Decomposing Plans

- [CA-P-1974 — Prepare post-Subject content update Tasks](19-CA-P-1970@21-EPIC--align-atom-content-after-subject-migration/01-CA-P-1974-TASK--prepare-post-subject-content-update-tasks.md)
- [CA-P-1971 — Verify the Stage 2 entity model](19-CA-P-1970@21-EPIC--align-atom-content-after-subject-migration/02-CA-P-1971-TASK--verify-the-stage-2-entity-model.md)

### Definition of Done

The Plan is **not** Done if broader content work starts before CA-P-1969 passes, affected content/consumer use precedes updated independently verified RMEDO and Tool fixture readiness, content changes lack their required review/authority, meaning or constraints are lost, Scope is confused with ownership, queued content-conflict owners/evidence are hidden or their Subjects-stage exclusion is treated as a completed content repair, or unrelated migrations enter the batches; ordinary-update versus new-Atom lifecycle rules, D/consumer adoption, Applicable Methodology lifecycle or positive and negative checks remain unplanned or unverified; Terms Graph contracts, affected consumers or required acceptance cases remain unaligned or unverified; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
