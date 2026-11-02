---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Evaluation"
  depends_on:
    ["Implementation", "Implementation Binding", "Evidence", "Entity/Node/Continuant/History/Journal.Record", "Verification", "Entity/Node/Continuant/Atom/Content Role: Operations"]
version: 9
updated_at: "2026-10-19 15:53:17 +0400"
relations: {}
atom_id: "CA-R-1505"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1505-CORE_META_MODEL-CORE-REQUIREMENT--keep-evaluation-realization-chains-distinct.md
  source_atom_id: CA-R-1505
  source_atom_revision: 9
  source_sha256: 60e2b2b843508c84c76882c22c9ec9306be435b1497458cafa54b5fb44dba321
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
