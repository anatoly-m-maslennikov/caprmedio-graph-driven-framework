---
subjects:
  active: Atom/(.Role := "Analysis & Advisory")
version: 33
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-1725
atom_id: CA-R-1648
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1648-CORE_META_MODEL-RULE--use-external-analysis-atoms-as-review-envelopes.md
  source_atom_id: CA-R-1648
  source_atom_revision: 33
  source_sha256: 31e04af6c659de1023d4da4f716d2b422d002bd30878b30e51ad1b020d7425a5
  original_relations_sha256: 283945f34348b7aa7ef1af4a929db6aa2a06c96c9020511b235df82b91bc29ff
---
## Summary

Use external Analysis Atoms as review envelopes

## Claim scope

external reviews, their imported External Analysis Report Atoms, and the internal Analyses derived from them.

## Claim

an external review **must** be imported as an External Analysis Report Atom whose governed envelope identifies its source, provenance, reviewed scope, original body, **and** native attachments **without** requiring a provider-specific finding schema. one internal Analysis derives from that Atom, records the project's finding-level interpretation **and** dispositions, **and** becomes the **only** Analysis source from which project-owned Concern, Plan, Requirement, Method, Evaluation, **or** Delivery Atoms are derived. **every** accepted disposition that changes project meaning **or** work is materialized **in** its owning CAPRMEDIO Content Role; rejected **or** non-actionable findings remain **only** **in** the internal Analysis.
