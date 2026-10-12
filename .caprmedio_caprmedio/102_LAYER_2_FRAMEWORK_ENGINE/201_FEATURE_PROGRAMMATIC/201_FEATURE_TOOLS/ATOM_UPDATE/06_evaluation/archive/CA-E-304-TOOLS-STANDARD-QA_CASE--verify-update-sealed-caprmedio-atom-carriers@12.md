---
atom_id: CA-E-304
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_UPDATE"
  depends_on: ["Atom", "Atom/Revision", "Atom/Summary", "Atom/Revision/Updated At", "Update Sealed Atom Carriers", "Artifact/Carrier", "Journal/Record"]
version: 12
updated_at: "2026-10-10 23:57:17 +0400"
relations:
  evaluation_for: [CA-R-866, CA-O-030, CA-R-1464, CA-R-1415, CA-R-1371]
  relates_to: [CA-O-067, CA-R-1432, CA-R-1788, CA-R-1662]
---
# Summary

Verify update sealed caprmedio atom carriers

## Scope

The sealed single/bulk ATOM_UPDATE capability, including identity-preserving change classes, exact current source state, prior semantic history and honest failed recovery.

## Claim

ATOM_UPDATE follows CA-R-866 **and** CA-O-030 **to** apply the sealed set atomically, preserving identity, Summary, placement, **and** exact prior semantic history with class-specific Version **and** actual edit-time results.

## Details

### Test cases

1. prepare an isolated fixture with a valid single-Atom semantic content update, a frozen two-Atom frontmatter-and-content update, **and** an unassigned Draft update. include a mixed-class bulk set. seal paths, filenames, assigned IDs **when** present, Versions, Updated At values, digests, exact proposals **and** admitted change classes. record exact dry-run previews.
2. submit repeated, missing, ambiguous, invalid, unauthorized, **and** stale requests, including a bulk source changed **after** dry run **or** an uncertain class. reject **without** changing the fixture. restore the sealed source **and** apply valid single **and** bulk requests through sealed Initiative envelopes.
3. request a Summary change while retaining the Atom ID, including a changed heading **and** a filename Summary Slug change. reject it as a same-ID update even **if** the Claim is unchanged; report the need for replacement **without** silently allocating **or** applying a successor.
4. apply formatting-only, lossless Subject-serialization **and** demonstrably equivalent refinement changes. compare interpreted values, applicability, Subjects, Relations, Summary **and** acceptance meaning **before** **and** **after**. require unchanged Version **and** actual refreshed Updated At for each accepted edit, with existing history unaltered **and** no fabricated semantic Revision. apply a semantic change to the same primary Claim with fixed Summary: require **`=1`** next Version **and** exact preservation of the prior semantic Revision. a changed Claim, applicability, Subject target **or** Relation meaning is **not** carrier-only **or** equivalent refinement merely because its serialization is lossless.
5. inject a failure **after** **`>=1`** selected effect, **or** **after** atomic publication **and** **before** final verification; also exercise failed post-write validation. compare the complete changed-then-restored mutable frontier, including current Carriers **and** newly created semantic archive destinations.
6. request an evidenced unchanged result. distinguish actual no-op from an accepted carrier edit: require no invented Version, Updated At **or** archive mutation. retain the actual no-op/result evidence for the governing Run receipt; file equality alone does **not** establish that receipt.

### Subject-only update cases

Use an independently authored before/after byte ledger, not the graph builder, with complete valid Atom carriers. The canonical Subject-only request is `atoms: [{selector, expected: {atom_id, version, sha256}, subject_patches: [{field: governs|depends_on, index?: integer, old: exact value, new: explicit value}]}]`. Use an explicit index for list items; omit it only for the scalar `governs` value. Reject duplicate-file selectors and any request that mixes this mode with full `frontmatter` or `content` replacement; `both` is a lookup selector, not an update field.

Apply valid exact list-item changes in each direction and at each explicit index. The update must replace the selected Subject value only; a same value in body text does not satisfy `old`. Prefix matching is not a replacement operation: the lookup Evaluation covers exact and delimiter-boundary `/` and `:` cases, while this operation requires the exact old value and explicit new value. Do not reinterpret the pending relation grammar.

Reject before writing when the Atom ID, Version, SHA-256, field/index, or old value is stale or wrong; when Subjects are malformed, nested, missing, duplicated ambiguously, or the final dependency list would contain duplicate values; or when the requested path is absolute, escapes the approved root, is a symlink, a projection, or is missing. Do not repair any rejected carrier. Validate the complete resulting carrier, including frontmatter schema, identity, Subjects, and list indexes, before publication.

For an accepted non-no-op Subject change, require Version `+1` and an actual edit-time Updated At. Preserve all unrelated frontmatter and body bytes, unknown keys, formatting, and CRLF/LF line endings; only the explicit Subject list item and required Version/Updated At may differ. A local preview is deterministic and writes nothing; do not claim a new MCP binding. An old value equal to the new value, or a semantically unchanged resulting list, is a no-op: report it without a new Version, timestamp, archive, Revision, or Journal effect. Recheck the expected pins at apply time, and prove the unchanged standalone `ATOM_UPDATE --apply` guard still rejects unsupported direct apply. Inject a failed validation or publication and prove the fixture returns byte-for-byte to its before ledger.

### Acceptance criteria

- valid applies match their sealed previews **and** admitted classes: `carrier_only` **and** equivalent `refinement` keep Version, while `semantic_revision` advances it **`=1`** time **and** preserves its exact prior semantic Revision. **every** accepted edit refreshes actual Updated At under CA-R-1788. retain identity, Summary, path **and** filename; the unassigned Draft remains unassigned.
- dry runs **and** rejected requests change nothing. no temporary, mixed, **or** partially updated state remains **after** a successful apply. an actual no-op is not a fictitious accepted edit **or** semantic Revision.
- successful recovery restores the entire mutable before-state, preserves pre-existing history **and** accepted Journal evidence, **and** reports the failed attempt rather than update success.
- preflight-only rejection does **not** prove recovery. incomplete **or** unverified restoration fails the Evaluation.

### Failure disposition

reject a realization that violates **any** required case. preserve sealed preconditions, authority **and** classification result, exact previews, rejection evidence, prior **and** final Carriers, fault position, **and** actual recovery result.
