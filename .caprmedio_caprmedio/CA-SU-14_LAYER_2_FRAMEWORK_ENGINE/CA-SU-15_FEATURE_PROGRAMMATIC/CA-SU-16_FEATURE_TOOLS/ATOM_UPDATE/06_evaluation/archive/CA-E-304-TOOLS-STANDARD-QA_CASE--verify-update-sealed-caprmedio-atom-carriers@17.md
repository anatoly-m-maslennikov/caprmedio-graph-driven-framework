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
version: 17
updated_at: "2026-10-12 05:39:01 +0400"
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

For an accepted non-no-op Subject change, require Version `+1` and an actual edit-time Updated At. Preserve all unrelated frontmatter and body bytes, unknown keys, formatting, and CRLF/LF line endings; only the explicit Subject list item and required Version/Updated At may differ. The default local preview is deterministic and writes nothing; opt-in staging writes only derived candidates under CA-D-425. Do not claim a new MCP binding. An old value equal to the new value, or a semantically unchanged resulting list, is a no-op: report it without a new Version, timestamp, archive, Revision, or Journal effect. Recheck the expected pins at apply time, and prove the unchanged standalone `ATOM_UPDATE --apply` guard still rejects unsupported direct apply. Inject a failed validation or publication and prove the fixture returns byte-for-byte to its before ledger.

Use valid stable-ID non-archived originals under their admitted Status models, including correctly placed Plan Done and Backlog carriers. Prove both source and result pass the real complete-carrier validator without mocking it; retain the Active case. Verify exact Status, Summary, identity, placement, unrelated frontmatter, body bytes, and line endings remain unchanged in the proposed Carrier except for the declared Subject and required Version/Updated At spans. Reject Draft or archived Status/placement, invalid role-specific Status, status-folder mismatch, unavailable or ambiguous validation authority, and any otherwise invalid complete source or result without repair or writes. A no-op retains Status and creates no Revision or effect.

### Subject-profile preview cases

The closed Subject-only root envelope is exactly `{atoms, subject_profile?}`; each atom item remains exactly `{selector, expected, subject_patches}`. The exact path selector is a source locator, not Subject syntax. Exercise omission and explicit `legacy`, and explicit `approved`; each preview checks both its pinned source and proposed result with that one profile. Unknown or malformed profiles, extra root/item/patch keys, mixed Subject-only/full-carrier modes, cross-profile conversion, inferred profile selection, escaping, conjunctions, selectors inside a Subject value other than the approved initial form, and grammar migration fail.

Legacy keeps dots literal, uses `/` for bearer qualification and `:` for allowed values, and rejects every `atom(...)` selector. Approved recognizes `/` as broader-to-narrower, `.` as bearer-to-dependent, and `:` as Property-to-allowed-value, and accepts only the exact positive selector literals in CA-E-301. Prove that `Atom` and `atom` never normalize; reject `@`, empty/type-only/mixed-key/unknown-key/duplicate-key/positional/nested/later-position selectors and unquoted/escaped/wildcard/evaluated/aliased values. In `atom(...).Status`, prove the selected Atom remains Status's bearer and neither content_role nor type becomes Status's allowed value. Selector checks neither enumerate a concrete Atom row nor admit target semantics. For a non-no-op, verify exact selected scalar replacement, Version `N+1`, illustrative Updated At, full before/after digests, byte preservation outside Subjects/Version/Updated At, and deterministic `preview_sha256`.

The preview result includes its `subject_profile` and `subject_profile_evidence` with exactly `grammar_pins` and `native_admission: not_performed`; each grammar pin contains `atom_id`, `version`, `path`, and `sha256`, and these fields are included in the digest. Assert lexical syntax/direction validation only: no native endpoint, typed edge, target conformance, history, archive, Journal, MCP, source effect, or source migration is claimed.

### Admitted one-target Subject application cases

Exercise CA-D-531's exact Subject variant through the existing selected `update_atom` envelope and real shared Run/lifecycle composition, retaining generic-route regression cases. Use CA-D-425's deterministic intent and real complete-carrier/status validation with independently authored LF/CRLF before/intended/actual/history byte ledgers. Include Active, correctly placed non-Active current originals and no-op. Reject multiple independent targets, extra or mixed fields, caller authorization Booleans, fabricated starts/assessment, stale intent, grammar/report/definition/source drift, owner/path mismatch, projection/delivered copies, duplicate non-archived originals including unsafe or malformed competing claims, symlink/ancestor/inode swaps and archive collision.

For a non-no-op, verify the existing Done Analysis Report binds the Subject-only intended proposal with old Version/time, and O145/O129 independently reopen exact evidence. Missing, non-Done, malformed, stale, replacement-required, uncertain or wrong-class assessment prevents publication. Changing only illustrative preview time leaves the intent hash unchanged; changing a target/patch/profile pin/history destination or metadata rule changes it or refuses the request. Wrong expected intent or output must fail an independently authored check.

Verify actual canonical O030 start and exact selected execute authorization precede effects; no direct call with an authorization Boolean can write. Require current Version `N+1`, one actual Project-time Updated At within the observed effect interval, exact intended Status/placement/identity/Summary/unrelated-byte preservation, exact predecessor bytes at `N` classified archived by placement, no second predecessor bump/time/status edit, and actual readback hashes bound to the intended hash. Require real prior/change/Run receipts and actual current/history effect references; queue acceptance alone is not completion.

Inject failure after history publication, after current publication and during post-write validation, then prove exact current byte/mode restoration and removal of attempt-owned history while preserving pre-existing history and accepted Journal evidence. Inject failed restoration and verify partial/unknown recovery, retained evidence and no automatic replay. Inject change or terminal recording failure after a real effect; verify visible pending/partial disposition and that recording-only recovery preserves the same event payload without invoking publication again. Repeating the same admitted request never creates another update. Default local Subject preview remains mutation-free, staged preview changes no authoritative source, history or Journal, and standalone `ATOM_UPDATE --apply` remains rejected; none of these cases admits a new MCP route or bulk effect.

### Opt-in staged-preview cases

Exercise `run --stage-preview` with the unchanged closed Subject-only payload, omission/explicit Profiles, successful multi-target batches with distinct stable IDs, LF/CRLF, a non-no-op and a no-op in one batch. Distinct source paths sharing an eligible source basename claim the same stable ID: reject that competing-original case before staging rather than treating numbered output folders as identity admission. Prove default dry-run output/digest and zero-write behavior remain unchanged. Reject generic input, mixed input, `--apply`, unknown payload fields and invalid preflight before staging. The pure planner must still perform no filesystem writes.

Independently compare each staged full UTF-8 file with the original preview bytes/hash, retaining its source filename under the deterministic payload-order directory. Verify illustrative Version/time only, unchanged no-op metadata, and real complete-carrier validation using the ORIGINAL logical source path and applicable Status/placement. Verify the closed manifest's exact original preview hash, per-target source pins/intent hash, actual candidate path/measured hash and validation evidence. Require explicit staging-only/illustrative/sources-unchanged result flags, generated batch/manifest paths and measured manifest hash; the manifest is not an approval token.

Reject symlinked/escaping staging ancestors, destination substitution, reused or occupied batch/file/manifest destinations and any overwrite. Inject partial write, candidate readback/hash/validation failure, source or competing-identity drift, and grammar drift before the final check. Recheck with the SAME illustrative time: mismatched preview/pins/intent refuses success, not a refreshed preview. Failures report actual retained artifacts with no success seal or unsafe cleanup. Prove original bytes/modes, existing history and Journal remain unchanged in all cases, with no promotion or MCP call. Editing a candidate later invalidates its measured hash; no ongoing monitor is implied.

### Acceptance criteria

- valid applies match their sealed previews **and** admitted classes: `carrier_only` **and** equivalent `refinement` keep Version, while `semantic_revision` advances it **`=1`** time **and** preserves its exact prior semantic Revision. **every** accepted edit refreshes actual Updated At under CA-R-1788. retain identity, Summary, path **and** filename; the unassigned Draft remains unassigned.
- default dry runs change nothing; opt-in staging changes only its derived temporary batch. rejected requests change no authoritative source, history **or** Journal, and failed staging discloses any retained partial artifacts. no temporary, mixed, **or** partially updated authoritative state remains **after** a successful apply. an actual no-op is not a fictitious accepted edit **or** semantic Revision.
- successful recovery restores the entire mutable before-state, preserves pre-existing history **and** accepted Journal evidence, **and** reports the failed attempt rather than update success.
- preflight-only rejection does **not** prove recovery. incomplete **or** unverified restoration fails the Evaluation.

### Failure disposition

reject a realization that violates **any** required case. preserve sealed preconditions, authority **and** classification result, exact previews, rejection evidence, prior **and** final Carriers, fault position, **and** actual recovery result.
