---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Rename Generic Artifact Carrier'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Term//Artifact
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Domain/Continuant/History
  - Subject/Graph Relation
version: 19
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-R-1133
  - CA-O-040
  - CA-R-1491
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-411@19
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Verify rename one generic Artifact carrier

## Claim checked

CA-O-040 performs a grammar-valid generic carrier rename with complete canonical-reference rewrites **or** rolls back entirely.

## Applicable when

apply whenever generic filename grammar, canonical-reference discovery, **or** rename transaction mechanics change.

## Test case

prepare one generic Artifact with two current mutable governed canonical references **and** immutable historical evidence of its old identity. request a valid new filename; repeat using a filename that collides with another carrier.

## Acceptance criteria

the valid case changes the carrier name, records one old-to-new identity mapping, **and** rewrites both current mutable canonical references with **none** retaining the old identity. accepted Journal Records **and** exact historical Revisions remain byte-for-byte unchanged under CA-R-1491; their old identity is **not** a missed current rewrite. the collision case changes no carrier **or** reference.

## Failure disposition

reject the realization **and** preserve source **and** target names, grammar result, mapping, reference inventory, transaction evidence, **and** collision finding.

## Post-effect failure coverage

from an independent recorded before-state, inject a failure **after** the Carrier rename **and** **before** completion of **all** required reference rewrites **and** **before** the complete transition is accepted.

- verify restoration of **every** selected mutable Carrier, metadata value, **and** canonical reference **to** the exact before-state, including the prior existence **or** absence of owned destination paths. unrelated Carriers remain unchanged.
- distinguish failed preflight, failed apply, successful restoration, **and** incomplete restoration. **none** is an accepted successful transition.
- retain evidence that the injected failure followed a real selected effect. preflight rejection alone does **not** prove recovery; incomplete **or** unverified restoration fails the rollback guarantee.
