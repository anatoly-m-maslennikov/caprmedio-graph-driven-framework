---
atom_id: CA-M-208
ref_id: CA-M-208
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
tier: 1
relations:
  method_for:
  - CA-R-1130
  derived_from:
  - CA-A-058
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Patch generic Artifact metadata

## Applicable when

use this Method **when** a governed Tool needs the shared mechanics for a field-level frontmatter patch on one generic Artifact.

## Procedure

1. resolve **=1** generic Artifact **and** seal its path, revision, digest, schema, current frontmatter, **and** body digest.
2. apply **only** declared add, replace, **or** remove operations **to** registered frontmatter fields.
3. validate the resulting complete frontmatter document **and** reject unknown fields, failed preconditions, **and** **all** relation-target operations.
4. produce the exact field-level dry-run while preserving the original body bytes **and** carrier identity.
5. on authorized apply, recheck the sealed preconditions, atomically replace the carrier, advance governed revision metadata once, **and** prove the unchanged body digest.

## Outcome

the Artifact receives one schema-valid metadata revision while its body **and** identity remain unchanged.

## Failure or stop

stop **or** roll back on stale preconditions, unknown fields, schema failure, failed body preservation, **or** **any** requested relation patch.
