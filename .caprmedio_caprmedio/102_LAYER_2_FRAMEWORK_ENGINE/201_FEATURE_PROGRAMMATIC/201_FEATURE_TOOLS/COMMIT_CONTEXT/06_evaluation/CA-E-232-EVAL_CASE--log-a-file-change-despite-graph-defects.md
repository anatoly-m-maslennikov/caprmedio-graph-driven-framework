---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
version: 19
updated_at: 2026-10-27 19:59:30 +0400
relations:
  evaluation_for:
  - CA-R-1491
  - CA-R-804
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-232
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Log a file change despite graph defects

## Claim checked

COMMIT_CONTEXT records an observed file action **without** requiring the surrounding Project graph **or** the changed Carrier **to** conform **to** Applicable Methodology.

## Cases

1. change an Atom while unrelated Carriers share an identity **and** one authored relation names a mismatched **or** missing target.
2. change a Carrier with a broken Atom filename, a legacy ID, invalid lifecycle placement, **or** malformed authored properties.
3. repeat capture for the same observation **without** running a Project-conformance Evaluation.

## Acceptance

- capture returns the actual file action, exact observable path, **and** its observed evidence **without** mutation.
- use unambiguous available classification **and** relation bindings; retain unknown **or** conflicting values as such. do **not** invent a conforming Atom ID, Version, target, **or** graph state.
- preserve a recordable native Carrier observation **when** optional Atom classification fails.
- already available diagnostics **may** accompany the context. their absence **must not** require a conformance scan **or** block the Journal.
- the returned context does **not** assert that the Project passed an Evaluation.

## Failure disposition

reject the logger Implementation **if** it blocks recordable facts on Project-conformance defects, silently repairs observed values, requires a conformance scan, **or** mutates the Project during capture.
