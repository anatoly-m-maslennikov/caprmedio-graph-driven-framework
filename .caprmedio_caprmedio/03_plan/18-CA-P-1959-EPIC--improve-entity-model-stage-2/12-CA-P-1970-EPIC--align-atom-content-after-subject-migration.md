---
atom_id: CA-P-1970
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 12
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 5
updated_at: "2026-10-12 03:40:17 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1971]
---
# Summary

Align Atom content after Subject migration

## Objective

Align Summary, Substance, Substance Scope and Details with the verified Subject model, only after Step 1.

## Details

This grouping Plan has no own implementation work. It is blocked by CA-P-1969. Do not prepare or apply content replacements before that gate passes.

After the gate, inventory current **NON-ARCHIVED** eligible RMEDO source versions and create disjoint, at-most-15-minute child Tasks by role and source batch. Review and propose exact changes before applying them; resolve concrete conflicts below 90% confidence with the Operator. Task creation does not approve the content patches.

Use Substance as the umbrella: RMED contains Claims; O contains Operations. Keep Summary short and distinct from Substance. Substance Scope means applicability, not owning Scope Unit. Omit it only when the Substance concerns the whole Subject AND the whole owning Scope Unit. Details are optional where the Type permits them; preserve conditional/type-specific requirements.

The prospective Entity hierarchy is `Entity -> Object | Term | Selection`; Object divides into Occurrent and Continuant. Revision and Journal are under History. Carrier is under Continuant, not a generic root. R describes the entity skeleton and required outcomes; M describes methods; E specifies checks; D specifies carriers/storage/delivery; O specifies repeatable actions and workflows. M/E are views, not new roots. Keep general D field policies instead of per-property Carrier edge registries or new per-property Carrier nodes. Preserve internal/external/relational distinctions and meaningful constraints.

Adopt the semantic names `Atom.ID` and `Scope Unit.ID` while retaining the existing storage keys. Keep `Atom` distinct from lowercase `atom`. For an ordinary identity-preserving update, select the current original NON-ARCHIVED Atom, create exactly Version `+1`, and archive the previous original without a second version bump; the original need not be Active. A Type change instead creates an entirely new Atom and new ID, then archives the old Atom. A changed Summary requires a new ID unless governing policy separately changes; Type is not the sole replacement trigger. Stored IDs remain bare; archived originals share the ID at distinct Versions. Atom filenames in all statuses use `AtomID@Version-SCOPE_NAME--summary.md`, with `@` filename-only; references use ID plus Version.

Plan Step-2 adoption after RMEDO for D-approved carrier/reference changes, identity consumers, Applicable Methodology compiler consumers, and the Terms builder. Do not perform renames during this Plan edit; this Plan does not authorize an automatic runtime or release rebuild.

For Applicable Methodology, select current NON-ARCHIVED eligible source versions and preserve source ID, Version and authored content. Only projected Status and provenance may differ. Project Configuration authors corrections first; then select and project one whole lifecycle, with no independently versioned member. A projection is reusable and non-authoritative.

Classify each proposed change before writing under current authority. A changed Summary requires replacement with a new Atom ID and recorded predecessor/successor lineage; do not perform a same-ID Summary update. Same-Summary Substance/Scope/Details changes use the applicable semantic-revision or refinement route. Every accepted same-ID update still uses exact Version +1 and actual updated_at under the Operator's latest rule. Preserve meaning, status/history and actual recording. No schema or YAML heading/key rename, Scope Unit folder/ID migration, entity deletion or Term change is silently authorized.

Output: reviewed and authorized source changes, exact before/after pins and batch receipts.

### Terms Graph work after the Subject gate

Include the Terms Graph decisions recorded in CA-P-1959 and candidate #3. Definitions are derived from source cases and optional Semantics, without a separate definition-owning layer. Preserve source authority, reusable derived output, shared meaning with locally constrained allowed values, scoped meanings and visible conflicts where incompatible meanings apply to the same case.

Use this order for the affected work:

1. Review current Core and Engine graph RMEDO and identify definition-only assumptions, source evidence requirements and affected consumers. Prepare exact revisions/replacements and acceptance cases.
2. Apply and independently verify the accepted RMEDO changes, preserving source Claims, history and admitted Relation meanings. Do not retire every Definition Atom as a blanket migration.
3. Align the existing Terms Graph builder, extraction and diagnostics with those contracts. Reuse CA-P-1872's graph work; bind affected Engine files and fixtures to disjoint child owners.
4. Independently verify source traceability, reuse, allowed-value differences, scoped conflicts, unresolved evidence and rebuilding after source changes; supply the results to CA-P-1971.

CA-P-1974 must decompose these responsibilities into bounded child Tasks only after CA-P-1969's complete current receipt, before execution. A Phase-2 plan is not permission to perform content work during Step 1. Updating this Plan records planning only; it does not start Core adoption or implementation.

CA-P-1974's preparation alone cannot complete this group. Require the generated role/batch review, authorized effect and independent verification children and their actual outputs. Record the Summary replacement policy in each affected patch packet before approval.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Decomposing Plans

- [CA-P-1974 — Prepare post-Subject content update Tasks](12-CA-P-1970-EPIC--align-atom-content-after-subject-migration/01-CA-P-1974-TASK--prepare-post-subject-content-update-tasks.md)

### Definition of Done

The Plan is **not** Done if work starts before CA-P-1969 passes, content changes lack their required review/authority, meaning or constraints are lost, Scope is confused with ownership, or unrelated migrations enter the batches; ordinary-update versus new-Atom lifecycle rules, D/consumer adoption, Applicable Methodology lifecycle or positive and negative checks remain unplanned or unverified; Terms Graph contracts, affected consumers or required acceptance cases remain unaligned or unverified; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
