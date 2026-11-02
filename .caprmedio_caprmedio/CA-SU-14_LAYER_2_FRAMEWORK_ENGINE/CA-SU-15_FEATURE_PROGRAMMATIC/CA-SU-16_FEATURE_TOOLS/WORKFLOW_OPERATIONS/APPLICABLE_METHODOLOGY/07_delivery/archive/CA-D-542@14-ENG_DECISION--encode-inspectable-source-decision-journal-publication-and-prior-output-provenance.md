---
atom_id: CA-D-542@14
content_role: Delivery
type: Eng Decision
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Architecture/Communication
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Domain/Continuant/Selection//Methodology Sources
  - Atom Revision
  - Subject/Graph Node/Domain/Continuant/Projection
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
relations:
  delivery_for:
  - CA-R-1840
  - CA-R-2118
  - CA-R-1842
tier: 4
---
# Summary

Encode inspectable source, decision, Journal, publication, and prior-output provenance.

## Scope

The result/receipt Carrier contract for dry run, blocked result, atomic publication, and recovery.

## Claim

The compiler result **must** make exact source, decision, optional Journal observation, output, and prior-output state independently inspectable without treating a Projection or configuration index as source authority. The actual Operator decision and independently verified admitted Run/effect evidence remain required; a Journal record alone cannot authorize.

## Details

Every result contains `outcome`, `operation`, `source_frontier_digest`, `source_frontier`, `conflicts`, `decision_provenance`, `publication`, `evidence_refs`, and shared `run_receipt_refs`. Every frontier row contains `source_layer`, optional `extension_id` and `extension_revision`, `source_carrier_path`, `source_atom_id`, `source_atom_revision`, `source_sha256`, and `original_relations_digest`. Every decision row contains conflict ID, proposal/selection, Operator identity, independently verified admitted Run/effect evidence, optional Journal observation reference and digest, and the bound frontier digest; an optional configuration-index reference is marked `non_authoritative`.

For each published Carrier, `publication.output` records output path, output digest, and the exact original-source binding. The rendered Carrier preserves the original source frontmatter/body/Relations and records only its generated projection binding. A blocked/failed result includes `prior_output_state: "preserved" | "not_started" | "uncertain"`, exact findings, and no success receipt. A successful result contains atomic transaction ID, complete output digest, and independently verified publication/effect evidence, with an optional Journal publication reference. A failed Journal append is surfaced as a `recording_error` diagnostic and does not roll back or invalidate a successful publication. Journal append remains a plain explicit business-record operation; repeating it neither establishes identity nor authorizes or blocks the operation. It never reports a source mutation as a compiler effect.

### Sources

- CA-R-1840, CA-R-2118, CA-R-1842; CA-O-155 v2 and CA-O-157 v2.
- CA-P-1442 v1, fidelity and canonical-Journal boundary.
