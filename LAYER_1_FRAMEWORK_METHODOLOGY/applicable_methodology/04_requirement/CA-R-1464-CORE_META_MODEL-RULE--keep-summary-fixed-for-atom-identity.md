---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content.Summary
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.ID
  - CAPRMEDIO_MODEL <+ Atom.Content
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1464
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1464-CORE_META_MODEL-RULE--keep-summary-fixed-for-atom-identity.md
  source_atom_id: CA-R-1464
  source_atom_revision: 22
  source_sha256: 16eb3243f62a6561dfe42868a149dcf10871ab148e2b7e62f758d0c22dcc898e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Summary fixed for Atom identity

## Claim

### Prose Claim


the Summary of an Atom across its Revisions.


an Atom **must** keep the Summary created with it across **all** of its Revisions. **if** its Summary needs a change, **then** it **must** be replaced by a new Atom with a new Atom ID, even **if** its Claim is unchanged.
