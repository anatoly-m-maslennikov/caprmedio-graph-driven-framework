---
atom_id: CA-P-1970
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 19
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 9
updated_at: "2026-10-12 18:07:04 +0400"
relations: {}
---
# Summary

Align Atom content after Subject migration

## Objective

Align Summary, Substance, Substance Scope and Details with the verified Subject model, only after Step 1.

## Details

This is the separate retained content Epic, no longer a decomposition of CA-P-1959. It remains Active and deferred. The current Operator request authorizes only staged Subject migration; it does not authorize preparing or applying this Epic's content/consumer changes. Obtain separate execution authority and the relevant Subject/live gates before its future work.

Receive the explicit future-work queue required by the [approved content-conflict exclusions](../../.caprmedio_tmp/stage2-migration-20261012/model/content-conflict-decision.md), SHA-256 `6f5bdf81ae3861bd2141df69ba7ffa936f78cf7fef0ac0b8f2ae8290c17d09fc`: each whole original Atom whose content is independently confirmed to contradict the new model remains unchanged during Subjects-only staging and retains its ID, Version, source hash, contradictory source and candidate/Operator evidence, and reason. The complete Subject ledger must keep those owners visible in inventory/graph coverage and distinguish them from uncertain mappings or unreviewed omissions. Listing that queue does not start this Epic, prepare its deferred child work, authorize body changes or waive CA-P-1969 and separate execution authority. Reopen current source pins and the additive compact scope-reference decision before any later content review; old queue/report acceptance is not current content-patch approval.

Reviewed unresolved whole owners follow the [separate unchanged-owner decision](../../.caprmedio_tmp/stage2-migration-20261012/model/unresolved-owner-decision.md), SHA-256 `d325383d4d4b049347bc77381e3f17616d3a473d93fce587c6b23a11e0ad9912`. They stay wholly unchanged and unstaged with exact pins, affected occurrences, reason and open question; they are not confirmed content conflicts or automatically this Epic's queue. Subjects-only staging still requires complete 907-owner/4534-occurrence review and current independent acceptance of every disposition. No content edit or completion is authorized by this guidance update.

The detailed identity/Terms planning formerly embedded in the parent remains in [historical CA-P-1959 v54](archive/18-CA-P-1959-EPIC--improve-entity-model-stage-2@54.md). Retain that context for this Epic's future review alongside current governing RMEDO and later Operator decisions; historical scope wording grants no execution authority.

This grouping Plan has no own implementation work. It is blocked by CA-P-1969. Do not prepare or apply content replacements before that gate passes.

After the gate, inventory current **NON-ARCHIVED** eligible RMEDO source versions and create disjoint, at-most-15-minute child Tasks by role and source batch. Review and propose exact changes before applying them; resolve concrete conflicts below 90% confidence with the Operator. Task creation does not approve the content patches.

Use Substance as the umbrella: RMED contains Claims; O contains Operations. Keep Summary short and distinct from Substance. Substance Scope means applicability, not owning Scope Unit. Omit it only when the Substance concerns the whole Subject AND the whole owning Scope Unit. Details are optional where the Type permits them; preserve conditional/type-specific requirements.

The prospective model is [Candidate #3](../_projection/core-entity-review/presentation/operator.model.candidate-3.md), SHA-256 `b0ad3f0d803112bf5e2d16c3f882cd0b01032273474c41cf6045db9ee86e40b7`, plus the [approved five-branch decision](../../.caprmedio_tmp/stage2-migration-20261012/model/root-branches-decision.md), SHA-256 `fd265d787544d4c16f395c920cf6a634ec32285431ee28dad4d52083fee85ba7`: Entity has Object, History, Projection, Selection and Actor sibling branches. Only Object divides into Continuant and Occurrent. Source Atoms and source-authoritative non-Atom governing configurations, including `project_structure.toml`, are Continuants; actual live Executions and existing Sessions are Occurrents. Revision and Journal belong to History; Journal contains records ABOUT what actually happened in Executions, never the Executions themselves. Projection covers derived artifacts including Terms Graph; Actor remains who, outside Object; Selections choose existing items. Artifact is a cross-branch lifecycle description, not an Object superclass. Source meanings, registered allowed values and derived Terms Graph entries remain; Term annotations are not a root, an authoritative definitions layer or automatic materialized Projection entries. Carrier remains a Continuant. Earlier descendant model references and historical receipts do not establish current acceptance; reopen current evidence explicitly before any separately authorized future content work. This candidate update does not adopt native Relation semantics. R describes the entity skeleton and required outcomes; M describes methods; E specifies checks; D specifies carriers/storage/delivery; O specifies repeatable actions and workflows. M/E are views, not new roots. Keep general D field policies instead of per-property Carrier edge registries or new per-property Carrier nodes. Preserve internal/external/relational distinctions and meaningful constraints.

Adopt the semantic names `Atom.ID` and `Scope Unit.ID` while retaining the existing storage keys. Keep `Atom` distinct from lowercase `atom`. For an ordinary identity-preserving update, select the current original NON-ARCHIVED Atom, create exactly Version `+1`, and archive the previous original without a second version bump; the original need not be Active. A Type change instead creates an entirely new Atom and new ID, then archives the old Atom. A changed Summary requires a new ID unless governing policy separately changes; Type is not the sole replacement trigger. Stored IDs remain bare; archived originals share the ID at distinct Versions. Atom filenames in all statuses use `AtomID@Version-SCOPE_NAME--summary.md`, with `@` filename-only; references use ID plus Version.

Put the affected Tools first within Step 2: review/update and independently verify RMEDO, align and independently verify the existing D-approved carrier/reference and identity consumers, Applicable Methodology compiler and Terms builder, then use them in affected content/consumer work. CA-P-1974 creates the bounded children after the Subject gate. Do not perform renames during this Plan edit; this Plan does not authorize an automatic runtime or release rebuild.

For Applicable Methodology, select current NON-ARCHIVED eligible source versions and preserve source ID, Version and authored content. Only projected Status and provenance may differ. Project Configuration authors corrections first; then select and project one whole lifecycle, with no independently versioned member. A projection is reusable and non-authoritative.

Classify each proposed change before writing under current authority. A changed Summary requires replacement with a new Atom ID and recorded predecessor/successor lineage; do not perform a same-ID Summary update. Same-Summary Substance/Scope/Details changes use the applicable semantic-revision or refinement route. Every accepted same-ID update still uses exact Version +1 and actual updated_at under the Operator's latest rule. Preserve meaning, status/history and actual recording. No schema or YAML heading/key rename, Scope Unit folder/ID migration, entity deletion or Term change is silently authorized.

Output: reviewed and authorized source changes, exact before/after pins and batch receipts.

### Terms Graph work after the Subject gate

Include the Terms Graph decisions recorded in CA-P-1959 and candidate #3. Definitions are derived from source cases and optional Semantics, without a separate definition-owning layer. Preserve source authority, reusable derived output, shared meaning with locally constrained allowed values, scoped meanings and visible conflicts where incompatible meanings apply to the same case.

Use this order for the affected work:

1. Review current Core and Engine graph RMEDO and identify definition-only assumptions, source evidence requirements and affected consumers. Prepare exact revisions/replacements and acceptance cases.
2. Apply and independently verify the accepted RMEDO changes, preserving source Claims, history and admitted Relation meanings. Do not retire every Definition Atom as a blanket migration.
3. Align the existing Terms Graph builder, extraction and diagnostics with those contracts before affected content or consumer usage. Reuse CA-P-1872's graph work; bind affected Engine files and isolated fixtures to disjoint child owners.
4. Independently verify source traceability, reuse, allowed-value differences, scoped conflicts, unresolved evidence and rebuilding after fixture source changes before affected use; supply the results to CA-P-1971. Actual derived Terms compilation remains Step 2 and follows those gates.

CA-P-1974 must decompose these responsibilities into bounded child Tasks only after CA-P-1969's complete current receipt, before execution. A Phase-2 plan is not permission to perform content work during Step 1. Updating this Plan records planning only; it does not start Core adoption or implementation.

CA-P-1974's preparation alone cannot complete this group. Require the generated role/batch review, authorized effect and independent verification children and their actual outputs. Record the Summary replacement policy in each affected patch packet before approval.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Decomposing Plans

- [CA-P-1974 — Prepare post-Subject content update Tasks](19-CA-P-1970-EPIC--align-atom-content-after-subject-migration/01-CA-P-1974-TASK--prepare-post-subject-content-update-tasks.md)
- [CA-P-1971 — Verify the Stage 2 entity model](19-CA-P-1970-EPIC--align-atom-content-after-subject-migration/02-CA-P-1971-TASK--verify-the-stage-2-entity-model.md)

### Definition of Done

The Plan is **not** Done if work starts before CA-P-1969 passes, affected content/consumer use precedes updated independently verified RMEDO and Tool fixture readiness, content changes lack their required review/authority, meaning or constraints are lost, Scope is confused with ownership, queued content-conflict owners/evidence are hidden or their Subjects-stage exclusion is treated as a completed content repair, or unrelated migrations enter the batches; ordinary-update versus new-Atom lifecycle rules, D/consumer adoption, Applicable Methodology lifecycle or positive and negative checks remain unplanned or unverified; Terms Graph contracts, affected consumers or required acceptance cases remain unaligned or unverified; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
