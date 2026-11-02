---
subjects:
  active: Atom/(.Role := Evaluation)
  passive:
  - Entity/Object/Continuant/Package/Project Implementation
  - Aspects <+ Engineering <+ Traceability
  - Entity/Object/Continuant/History/Journal > Event Record
  - Atom/(.Role := Evaluation)
  - Atom/(.Role := Operations)
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
