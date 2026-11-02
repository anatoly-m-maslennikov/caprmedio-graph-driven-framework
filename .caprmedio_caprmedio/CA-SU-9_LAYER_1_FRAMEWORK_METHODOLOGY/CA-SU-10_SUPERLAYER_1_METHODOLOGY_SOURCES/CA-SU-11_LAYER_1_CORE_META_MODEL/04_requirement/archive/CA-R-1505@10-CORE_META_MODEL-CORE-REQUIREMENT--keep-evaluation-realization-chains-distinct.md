---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  depends_on:
  - Implementation
  - Implementation Binding
  - Evidence
  - Entity/Node/Continuant/History/Journal.Record
  - Verification
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations'
version: 10
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
atom_id: CA-R-1505@10
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Keep Evaluation realization chains distinct

## Scope

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
