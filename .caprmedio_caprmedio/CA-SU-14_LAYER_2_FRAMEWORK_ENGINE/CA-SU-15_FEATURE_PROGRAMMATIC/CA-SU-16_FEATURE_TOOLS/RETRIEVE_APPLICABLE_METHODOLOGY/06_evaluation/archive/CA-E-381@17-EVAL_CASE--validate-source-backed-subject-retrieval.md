---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/Evaluation
  depends_on:
  - Applicable Methodology Retrieval Tool
  - Applicable Methodology Retrieval Tool/Execution
version: 17
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-M-227
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-381@17
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
---
# Validate Source-Backed Subject Retrieval

## Test case

the Applicable Methodology Retrieval Tool Validation **must not pass** **if** (a Subject query matches a non-governing Carrier **or** a Process query matches a non-occurrent governed Subject Path **or** a prerequisite governor is omitted **or** compilation order changes **or** an unresolved prerequisite passes silently **or** a projected Carrier differs from its exact current Source Carrier **or** the source binding is missing **or** ambiguous **or** the same frontier **and** query produce different results **or** retrieval writes a persistent Subject Index Carrier, cache, Source Carrier, **or** generated methodology Carrier).

## Sources

- [CA-M-227 — Retrieve Subject Authority Without Persistent Indexes](../05_method/CA-M-227-RETRIEVE_APPLICABLE_METHODOLOGY-ENG_DECISION--retrieve-subject-authority-without-persistent-indexes.md)
- [CA-R-1241 — Require Source-Backed Subject Retrieval](../04_requirement/CA-R-1241-RETRIEVE_APPLICABLE_METHODOLOGY-RULE--require-source-backed-subject-retrieval.md)
