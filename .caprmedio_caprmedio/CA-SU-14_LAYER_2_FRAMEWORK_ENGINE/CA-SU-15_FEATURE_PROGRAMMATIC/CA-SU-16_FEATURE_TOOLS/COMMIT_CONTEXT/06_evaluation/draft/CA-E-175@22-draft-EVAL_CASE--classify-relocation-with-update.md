---
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - Subject/Engineering/Carrier
  - Subject/Graph/Relation
version: 22
updated_at: 2026-10-24 23:55:59 +0400
relations:
  evaluation_for:
  - CA-R-805
  - CA-M-087
  - CA-R-804
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-175@22-draft
status: Draft
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
---
# Classify relocation with update

## Claim checked

one file identity that changes Structural location **and** also changes content, filename, **or** other governed carrier state is classified as one `MOVE+UPDATE` change set.

## Test case

supply a trigger for one identity whose directory **and** governed content both change **in** the same working-tree transition.

## Acceptance criteria

the sealed context reports exactly `MOVE+UPDATE`, records both paths **and** the resulting version, **and** resolves upstream relations from the observed candidate result graph bound into the provisional context.

## Failure disposition

reject classification **and** report **any** split into two actions, missing flag, identity split, **or** incorrect relation source.

## Observation boundary

the candidate result graph is a read-only description of the observed change, **not** an instruction **to** stage it. capture **any** existing Git index separately; do **not** assume that the final gate already staged the candidate. COMMIT_CONTEXT performs no index mutation **and** grants no Git effect permission. COMMIT_CHANGE_SET alone stages the admitted target **and** revalidates its actual complete staged set at the effect boundary under CA-R-805.
