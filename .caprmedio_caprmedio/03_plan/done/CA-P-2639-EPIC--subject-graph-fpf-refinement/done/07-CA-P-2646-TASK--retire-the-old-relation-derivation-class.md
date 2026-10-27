---
atom_id: CA-P-2646
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
current_scope_unit: caprmedio
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Relation
version: 2
updated_at: 2026-10-26 06:39:23 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Retire the old Relation Derivation Class

## Objective

Retire the old Relation Derivation Class definition in favor of the accepted
explicit Relation Type derivation and source references, following D07.

## Details

Addresses the classification part of I06. Estimated own work: up to 15 minutes.

- Read Current R1617 and locate its actual Current incoming references and
  source consumers. The audit observed R1617@13; reopen Current bytes.
- Coordinate with P2645 so the concrete CONTAINS derivation from
  IS_CONTAINED_BY is preserved. Do not conflate that type-level fact with
  individual projected links.
- Archive the existing R1617 version without inventing a new Version merely
  for archival, following D05. Preserve existing historical carriers.
- Repair affected Current source references according to their actual
  obligations; do not leave governing links pointing to an Archived Atom.
  Keep useful source references and concrete derivation meanings.
- Do not create another mandatory explicit/resolved/inferred/observed
  classification under a different name, or build an inference mechanism.
- Record exact affected source IDs, dispositions and any concrete unsupported
  consumer meaning requiring an Operator decision. Split wider work into
  another Task rather than exceed the own-work estimate.
- Preserve unrelated content and existing Drafts/Archives. Actual Current
  consumer changes receive normal predecessor archives.

This is source-model retirement and bounded consumer correction only. No
code, tools, runtime, renderer or Terms Graph work is authorized.

### Completion evidence

R1617 and R1613/R1614/R1615/R1618/R1619 retired; R1612@16 preserves its sufficient-evidence rule. No selected Current typed reference targets the retired class. V08 PASS.

Source verification: `.caprmedio_tmp/subject-fpf-refinement/verify.final.md`.
Final source/output pins: `.caprmedio_tmp/subject-fpf-refinement/graph-closure/graph.subject-views.manifest.json`.
Actual effect verified; no production tool/runtime implementation or release is claimed.

## Definition of Done

- R1617 is no longer Current and does not appear as a Relation Type.
- Affected Current source consumers have explicit supported dispositions.
- Explicit derivation between Relation Types and useful source references
  remain intact; no shadow classification replaces the retired concept.
- Actual archival and consumer corrections are recorded separately from this
  Plan, with unresolved concrete obligations not silently dropped.
