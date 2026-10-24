---
subjects:
  governs: Governed Change/Change Class
  depends_on:
  - Subject/Engineering/Carrier
  - Subject/Graph/Relation
version: 14
updated_at: 2026-10-23 03:18:40 +0400
relations:
  evaluation_for:
  - CA-R-805
  - CA-M-087
  - CA-R-804
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-171@14
status: Archived
---
# Classify file creation as ADD

## Claim checked

creation of one governed file identity is classified **only** as `ADD`.

## Test case

supply a trigger whose observed candidate result graph bound into the provisional context **contains** one new governed file with no matching identity **in** the committed graph.

## Acceptance criteria

the sealed context reports `ADD`, names the resulting filename **and** version, **and** resolves upstream relations from the observed candidate result graph bound into the provisional context.

## Failure disposition

reject classification **and** report the observed competing **or** missing change set.

## Observation boundary

the candidate result graph is a read-only description of the observed change, **not** an instruction **to** stage it. capture **any** existing Git index separately; do **not** assume that the final gate already staged the candidate. COMMIT_CONTEXT performs no index mutation **and** grants no Git effect permission. COMMIT_CHANGE_SET alone stages the admitted target **and** revalidates its actual complete staged set at the effect boundary under CA-R-805.
