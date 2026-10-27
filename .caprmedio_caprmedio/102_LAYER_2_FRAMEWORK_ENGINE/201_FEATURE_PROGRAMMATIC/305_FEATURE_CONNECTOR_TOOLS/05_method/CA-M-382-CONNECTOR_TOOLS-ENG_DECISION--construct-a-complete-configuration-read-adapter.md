---
atom_id: CA-M-382
content_role: Method
type: Eng Decision
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Data Handling/Source Retrieval
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Governing Configuration
relations:
  depends_on:
  - CA-M-376
tier: 3
---
# Summary

Construct a complete configuration read adapter

## Scope

construction of the complete Configuration Read operation on the shared TOML connector.

## Claim

**to** construct Configuration Read, the Implementer **must** refine CA-M-376:

- resolve the explicit logical target through the supplied Project/source/schema context **and** read permission; keep physical locations private. do **not** search for a fallback target, infer authority from a filename **or** invoke Modify.
- obtain complete exact source bytes **and** parse them with duplicate-key rejection. check the complete source against the supplied applicable schema **and** declared schema-version constraints; do **not** select **or** weaken the schema.
- bind the returned source bytes, parsed values **and** actual state evidence **to** the same observed source. reject a changed source **when** this consistency cannot be established; do **not** combine values from different reads.
- enforce supplied pins **and** historical source views exactly. return actual current evidence for unpinned Read **without** inventing an Atom Version **or** new retention guarantees.
- return CA-D-631's complete data **and** truthful common errors/effects. do **not** repair, normalize, persist, record a configuration revision **or** activate a runtime as a side effect of reading.

## Details

source acceptance **and** later functional verification are separate. this Method adds no transport, workflow wrapper, retry, publication **or** concurrency design.
