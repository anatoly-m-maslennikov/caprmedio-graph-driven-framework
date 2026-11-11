---
atom_id: CA-E-502
ref_id: CA-E-502@29
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
  - CAPRMEDIO_MODEL <+ Carrier/File
  - CAPRMEDIO_MODEL <+ Carrier/Directory
  - CAPRMEDIO_MODEL <+ Atom.Header.Identity.ID
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.Context.Plan.Work Sequence Number
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.Context.Label'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Content.Definition of Done'
tier: 4
relations:
  evaluation_for:
  - CA-D-460
  - CA-D-461
  - CA-D-469
  - CA-D-470
  - CA-D-472
  - CA-D-475
  - CA-R-1534
  - CA-R-1599
  - CA-R-997
status: Archived
version: 29
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-E-502@29-CORE_META_MODEL-EVAL_CASE--validate-plan-carrier-identity-and-placement.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary
Validate Plan Carrier identity **and** placement

## Claim

### Prose Claim

Plan Carrier identity **and** placement.

the Plan Carrier Evaluation **must** reject Carrier facts that create duplicate identity **or** contradict the shared Plan model.

- accept a mandatory Markdown file **with** **or** **without** a matching optional Hub directory under `CA-D-460-CORE_META_MODEL-CORE-DELIVERY--serialize-plan-atom-carrier-bundles`; reject a directory **without** that file.
- count a matching pair once; reject two IDs, divergent stems, conflicting Status, a separate Epic identity, **or** an Objective file that claims **to** be another Atom for the same Hub.
- require DoD **in** **every** supplied Plan file, even **when** it carries contained child Plans **or** explicit overrides.
- validate leading navigation numbers **before** Atom IDs, their local uniqueness, mutable Label tokens, **and** canonical Summary slugs. changing a number **or** Label **must not** change identity **or** scheduling.
- read Plan Status from its own file **and** check its local placement; reject read-time inference from a containing Hub **or** path.
- change a parent Plan's Status to Active, Backlog, Done, Canceled **or** Archived as admitted by its model: require independent single-Atom Actions for the selected latest descendants under CA-R-1521, without an optional descendant mode. For a containing Plan Atom requested Done **or** Canceled, preserve selected latest contained Plans already Done **or** Canceled and request Canceled for every other selected latest contained Plan. After the cascade, every selected latest contained Plan must be Done **or** Canceled; mixed terminal statuses are allowed, and no child is forced to match the parent's requested Status merely because the parent is Done **or** Canceled. For target Archived, every contained latest Atom is requested as Archived, including Done Plans. Other admitted targets retain the same-Status cascade. Check each Atom's own model; reject an invented target value **or** a multi-target Action.
- retain each Current descendant inside its parent Carrier tree with the local Status mapping under CA-D-461; for a contained Current Plan, validate its Status placement relative to its immediate containing Plan's Directory Carrier. For example, a Done child is in `<parent-directory>/done/<child>.md`, using its canonical matching stem. Validate Draft carriers in the owning Scope Unit's shared `03_plan/draft` area. Validate each Archived Plan Markdown Carrier directly in the shared `03_plan/archived` area, without parent/child Plan directory nesting, and with CA-D-289's Version suffixes.
- leave referenced Plans outside the tree **and** older archived Revision bytes, Version **and** Status unchanged; reject older Revisions as cascade targets. Allow retained-history subtrees and non-Atom assets to accompany the matching Directory Carrier byte-for-byte unchanged, without inferring Status effects. No independent migration of noncanonical legacy `archive/` trees is implied.
- accept root Backlog Plans **in** `03_plan/001_backlog`; reject `031_backlog` as the canonical new encoding **and** reject a `version-<VERSION>` directory substituted for a Version-labeled Plan identity.
- retain one identity **when** contained work is added, removed, **or** reordered; a changed Summary follows Atom replacement authority rather than independent filename editing.

report the invalid Carrier Bundle, source fact, **and** violated Delivery rule.
