---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Summary
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Content.Definition of Done'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Content.Details'
  - CAPRMEDIO <+ MODEL <+ Carrier/File
version: 29
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-470
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-470-CORE_META_MODEL-ENG_DECISION--serialize-plan-file-sections.md
  source_atom_id: CA-D-470
  source_atom_revision: 29
  source_sha256: 8430a426a21329d1177bde2817f1d3264dff899f65bfa3fede07ee002d1e6490
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Plan file sections

## Claim scope

Plan Markdown File Carriers and their body-section layout.

## Claim

**every** Plan Markdown File Carrier **must** contain YAML Frontmatter followed by the Plan layout registered **in** CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties:

1. `# Summary` carries the Summary value.
2. `## Objective` carries the intended work **or** outcome Claim, including its applicability restrictions.
3. `## Details` carries supporting information **and** **`=1`** nested `### Definition of Done` section with the Plan's falsifying Condition Expression.

the Definition of Done is the Plan's existing Property, **not** a second completion Claim **or** an optional detail. carry its value **only** **in** that nested section. **any** other supporting Details **must** stay within the Objective. use CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties for section boundaries; do **not** duplicate these Properties **in** frontmatter **or** add a separate Scope section duplicating restrictions **in** the Objective. a Hub uses this same mandatory file, **not** an additional Objective Atom.
