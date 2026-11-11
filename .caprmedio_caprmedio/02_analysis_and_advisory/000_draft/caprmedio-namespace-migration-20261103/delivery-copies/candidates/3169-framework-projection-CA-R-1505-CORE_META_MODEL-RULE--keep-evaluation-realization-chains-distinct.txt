---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Package/Project Implementation
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Traceability
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/History/Journal > Event Record
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)
version: 27
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-R-1505
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1505-CORE_META_MODEL-RULE--keep-evaluation-realization-chains-distinct.md
  source_atom_id: CA-R-1505
  source_atom_revision: 27
  source_sha256: 8d3ea8c703f491a879109d7f2d2bc0f6a70301cc551d0dd6dc0897ae15d29e84
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Evaluation realization chains distinct

## Claim scope

Evaluation realization chains and their associated implementation, evidence, and operational contributions.

## Claim

an Evaluation Atom's realization chains **must** remain distinct between deterministic test implementations **and** qualitative, probabilistic, statistical, rubric-based, **or** model-judged evaluation implementations.

**every** chain **must** keep these contributions distinguishable:

- its executable Implementation;
- its configuration **or** rubric;
- its factual execution result;
- its Evidence;
- its Verification judgment.

## Details

a shared runner, prompt, judge, report, **or** gate **must not** merge the chains' meanings, results, **or** coverage. the source authority, executable mechanisms, factual Journal Records, **and** reusable Operations definitions retain their distinct roles under CA-R-1683-CORE_META_MODEL-CORE-REQUIREMENT--authority-evaluation-and-operations-remain-distinct **and** CA-R-1684-CORE_META_MODEL-CORE-REQUIREMENT--separate-analysis-from-factual-execution-records.
