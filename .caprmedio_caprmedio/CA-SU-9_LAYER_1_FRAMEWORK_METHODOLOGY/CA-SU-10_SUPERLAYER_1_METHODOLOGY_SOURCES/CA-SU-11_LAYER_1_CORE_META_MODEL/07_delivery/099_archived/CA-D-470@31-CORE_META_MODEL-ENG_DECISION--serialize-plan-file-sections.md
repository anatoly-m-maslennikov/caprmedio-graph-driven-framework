---
atom_id: CA-D-470
ref_id: CA-D-470@31
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Content.Definition of Done
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Content.Details
  - CAPRMEDIO_MODEL <+ Carrier/File
tier: 3
status: archived
version: 31
updated_at: 2026-11-08 19:06:46 +0400
carrier_destination:
  file:
    name: CA-D-470@31-CORE_META_MODEL-ENG_DECISION--serialize-plan-file-sections.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Serialize Plan file sections

## Claim

### Prose Claim


Plan Markdown File Carriers and their body-section layout.

For Work Report, serialize YAML Frontmatter followed by `## Summary` and `## Details`. Details contains the actual changes, checks, results and remaining gaps. Subheadings within this Markdown value are text, not additional modeled Properties.

The following intended-work layout applies to other Plan Forms.


**every** Plan Markdown File Carrier **must** contain YAML Frontmatter followed by the Plan layout registered **in** CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties:

1. `# Summary` carries the Summary value.
2. `## Objective` carries the intended work **or** outcome Claim, including its applicability restrictions.
3. `## Details` carries supporting information **and** **`=1`** nested `### Definition of Done` section with the Plan's falsifying Condition Expression.

the Definition of Done is the Plan's existing Property, **not** a second completion Claim **or** an optional detail. carry its value **only** **in** that nested section. **any** other supporting Details **must** stay within the Objective. use CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties for section boundaries; do **not** duplicate these Properties **in** frontmatter **or** add a separate Scope section duplicating restrictions **in** the Objective. a Hub uses this same mandatory file, **not** an additional Objective Atom.
