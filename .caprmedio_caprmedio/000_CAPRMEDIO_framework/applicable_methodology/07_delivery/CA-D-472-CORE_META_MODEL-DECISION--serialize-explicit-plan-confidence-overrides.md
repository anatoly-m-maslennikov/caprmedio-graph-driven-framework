---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Plan).Header.AI Agent Confidence Threshold
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  - CAPRMEDIO_MODEL <+ Carrier/File
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Content.Definition of Done'
version: 29
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-D-472
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-472-CORE_META_MODEL-DECISION--serialize-explicit-plan-confidence-overrides.md
  source_atom_id: CA-D-472
  source_atom_revision: 29
  source_sha256: 161c952b42de6a0f6a2fc560bbb14addd2c0aed16f2f7d7bcb8e66720ad92e3d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize explicit Plan confidence overrides

## Claim

### Prose Claim


explicit Plan Autonomous Confidence Threshold overrides in Plan Atom Markdown File Carriers.


an explicit Plan Autonomous Confidence Threshold override **must** use the top-level integer frontmatter field `autonomous_confidence_threshold` **in** that Plan Atom's own mandatory Markdown File Carrier.

- a Hub uses that same file, **not** a separately identified Objective **or** Epic settings file.
- omit an unselected override **without** copying its inherited value; the mandatory file requirement does **not** turn inheritance into a local selection.
- retain an explicit override even **when** it equals the inherited value.
- `epic_overrides` is **not** an alternative canonical encoding.
