---
atom_id: CA-D-585@15
content_role: Delivery
current_scope_unit: TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Data Handling/Serialization
version: 15
updated_at: 2026-10-27 06:04:45 +0400
relations:
  delivery_for:
  - CA-R-1892
type: Eng Decision
tier: 4
---
# Summary

Serialize semantic assessment report reference

## Scope

The optional external evidence field of one lifecycle Update request and its retained O145/O129 result evidence.

## Claim

The request representation of external semantic evidence **must** be `semantic_assessment_report: {path, digest}`, with `path` a canonical Project-relative path and `digest` its lowercase SHA-256, bound to one of the evidence representations below.

## Details

A shared JSON review package stores exactly `{"assessments": [...]}` with a nonempty list of assessment objects. Exactly one object must match the requested Atom; the same package may support multiple independent updates without separate Analysis Atoms. Alternatively, a Done Analysis Report stores one assessment object at `## Results` / `### Update assessment evidence` as one JSON block, with no aliases.

Each assessment object contains exactly `target`, `proposal`, `authorityPins`, `admittedChangeClass`, `primaryClaimIdentityPreserved`, `declaredDelta` and `lineageEvidencePins`. The target is `{atom_id, path, digest}`; the proposal is `{frontmatter_digest, content_digest}`. Authority pins contain exactly `r1432` and `r1464`; each authority or lineage pin is `{path, digest}`. Preserve the existing admitted class, `primaryClaimIdentityPreserved: true`, nonempty declared delta and nonempty lineage-evidence list. The same exact target/proposal/authority/lineage checks apply to both carriers.

For CA-D-531's ordinary Subject-only variant outside CA-R-866's instructed batch branch, the selected assessment's `proposal` pins bind the exact UTF-8 frontmatter and body of the complete intended Carrier produced by CA-M-371: only declared Subject spans change, while old Version and Updated At remain. Compare the selected assessment's existing `frontmatter_digest` and `content_digest` to CA-D-425's corresponding intended-proposal pins. The separately bound `subject_intent_sha256` seals the fixed `N+1`/actual-effect-time materialization rule and exact predecessor history; illustrative preview metadata and future actual timestamps/hashes are not report proposal pins. O145 and O129 reopen the same current report or shared package, authority, lineage and intended-proposal evidence. Materializing the admitted Version/time rule at the actual effect does not silently replace that assessed Subject delta; any other proposal or intent change requires fresh assessment/preview/authorization. A value change still requires the admitted `semantic_revision` and preserved primary-Claim identity; this ordinary variant grants no assessment exception. The instructed Subjects-only batch uses its exact packet/member evidence and existing request Initiative/Operator authorization instead, with no separate form, review/pause response, content-review/confirmation round, fabricated receipt, per-Atom report or invented O145 result. It retains normal operation checks without a redundant full-candidate validation or public initial intent-metadata gate; this Delivery introduces no replacement report format.

The request reference accepts no identifier alias, inline assessment, caller-supplied class, Status, authority pin or approval field. O145 returns normalized verified report observations; O129 returns the verified evidence with the actual lifecycle outcome. The shared Run result retains those Action facts under its existing Journal contract; this Delivery adds no Event schema or authorization grant.
