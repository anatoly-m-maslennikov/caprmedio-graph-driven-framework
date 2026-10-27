---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/History/Journal.Record
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Domain/Continuant/Project
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
version: 24
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-R-1491
atom_id: CA-D-340@24
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Eng Decision
---
# Summary
Serialize Work Journal Event Properties

## Scope
Serialization **and** reading of supplied Work Journal Event properties.

## Claim
Work Journal Event serialization **must** preserve the properties actually supplied as observations through safe encoding; reading **must** return stored properties as recorded.

- preserve supplied identities, Types, action Kinds, Authors, times, session provenance, Scope, identifiers, filenames, paths **and** other values **when** present. do **not** invent missing values **or** rewrite them **to** satisfy current naming **or** classification rules.
- an Atom ID **or** other observed property is payload data, **not** a Project-conformance judgment, permission **or** proof of correct execution.
- do **not** impose required-field, event-identity, schema, digest, prior-history, chain, receipt, deduplication, retry **or** recovery admission **to** append/read.
- retain existing historical representations **and** bytes **without** migration, repair **or** synthetic baselines. ordinary serialization/read failure is reported truthfully, **not** converted into fabricated data.

## Details
