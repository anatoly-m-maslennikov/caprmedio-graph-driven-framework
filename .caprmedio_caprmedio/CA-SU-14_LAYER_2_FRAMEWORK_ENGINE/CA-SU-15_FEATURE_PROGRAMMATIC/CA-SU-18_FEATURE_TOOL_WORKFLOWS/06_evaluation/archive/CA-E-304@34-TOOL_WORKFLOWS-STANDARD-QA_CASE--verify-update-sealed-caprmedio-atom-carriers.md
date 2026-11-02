---
atom_id: CA-E-304@34
content_role: Evaluation
type: QA Case
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Tool//ATOM_UPDATE
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Domain/Node/Continuant/Atom.Summary
  - Atom/Revision/Updated At
  - Subject/Engineering/Carrier
version: 34
updated_at: 2026-10-24 00:51:05 +0400
relations:
  evaluation_for:
  - CA-R-866
  - CA-O-030
  - CA-R-1464
  - CA-R-1415
  - CA-R-1371
  relates_to:
  - CA-O-067
  - CA-R-1432
  - CA-R-1788
  - CA-R-1662
tier: 3
---
# Summary

Verify update sealed caprmedio atom carriers

## Scope

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

One sealed Atom Modify action, including identity-preserving change classes, exact current state and prior semantic history; ordered actions remain independent.

## Claim

ATOM_UPDATE follows CA-R-866 and CA-O-030 for one Atom action, preserving identity, Summary, placement and exact prior semantic history with Version +1 for every actual changed same-ID update and actual edit-time results; no-op preserves Version and time. A later failed action cannot undo an earlier completed Atom action.

## Details

### Test cases

1. Prepare valid one-Atom semantic, frontmatter/content and unassigned Draft updates with exact identity, Version, timestamp, digest, proposal and admitted change class. For an ordered list of independent actions, include different classes and record each dry-run preview separately.
2. Reject repeated, missing, ambiguous, invalid, unauthorized, stale or uncertain-class input before the affected action writes. Change the second source after preview: an earlier completed action remains, the second fails and later actions are not started. Apply valid independent actions only with their own sealed permission and source-state evidence.
3. request a Summary change while retaining the Atom ID, including a changed heading **and** a filename Summary Slug change. reject it as a same-ID update even **if** the Claim is unchanged; report the need for replacement **without** silently allocating **or** applying a successor.
4. Apply formatting-only, lossless Subject serialization, equivalent refinement, Status-only and semantic changes with fixed Summary/Type. Every actual changed same-ID update requires exactly Version N+1 and actual refreshed Updated At, preserving exact prior state at N. A no-op keeps Version/time and creates no history effect. A Summary or Type change requires replacement instead. Keep content/class assessment truthful; a changed Claim, applicability, Subject target or Relation meaning is not equivalent merely because serialization is lossless.
5. Inject failure after an effect or publication and before verification within one Atom action. Compare that action's complete admitted restoration boundary, including its current Carrier and new history destination. Preserve earlier completed Atom actions; failed or unverified restoration is not a passing rollback.
6. request an evidenced unchanged result. distinguish actual no-op from an accepted carrier edit: require no invented Version, Updated At **or** archive mutation. retain the actual no-op/result evidence for the governing Run; file equality alone does **not** establish its actual execution.

### Identified legacy Concern repair cases

Use a disposable already identified CA-C Concern under `01_concern` with one nonempty unfenced descriptive first H1. An exact same-value canonical `# Summary` proposal is admitted through the existing full-content route; require normal complete Concern result validation, existing assessment/authorization, unchanged ID/Type/intended Status/path, Version N+1, actual time and exact predecessor bytes. Preserve historical pins when repairing an old note.

Reject missing, blank, ambiguous or fenced-only source headings and noncanonical proposed bodies. A changed Summary value returns replacement-required without writes. Retain refusal for ID/Type drift, stale descriptors and invalid proposed carriers. Test both source-side Summary reads and canonical fence awareness. The ordinary proof-based legacy-ID migration, one-Section edits and full-source Subjects-only preview checks retain their existing behavior. These cases are required checks, not claimed passes.

### Logical modification cases

Required future cases cover CA-R-1933/CA-M-373 section add, replace, remove, title and position; CA-R-1934/CA-M-374 Property add, replace and remove; list entry add/remove, replacement of one entry by its exact current value, and replacement of the complete set. Require unique value resolution, reject caller list indexes, missing/ambiguous values and malformed final state, and preserve unrelated content. Every Summary change, including wording-only edits, rejects same-ID Modify and requires separately authorized fresh-ID replacement. Find and Read do not run implicitly. These cases are specifications, not observed passes.

### Subject-only update cases

Use an independently authored before/after byte ledger, not the graph builder, with complete valid Atom carriers. The required Subject-only replacement request is `atoms: [{selector, expected: {atom_id, version, sha256}, subject_patches: [{field: governs|depends_on, old: exact current value, new: explicit value}]}]`. Resolve a dependency by its unique exact current value; caller indexes are rejected. Subject-only add/remove/full-set changes use CA-D-623's explicit list operation shapes, preserving this mode's separation from generic content edits. Reject duplicate-file selectors and any request that mixes this mode with full `frontmatter` or `content` replacement; `both` is a lookup selector, not an update field.

Apply valid exact list-item changes in each direction by their unique current values; reorder the source list before a fresh request to prove selection does not depend on caller positions. The update must replace the selected Subject value only; a same value in body text does not satisfy `old`. Prefix matching is not a replacement operation: the lookup Evaluation covers exact and delimiter-boundary `/` and `:` cases, while this operation requires the exact old value and explicit new value. Do not reinterpret the pending relation grammar.

Reject before writing when the Atom ID, Version, SHA-256, field or old value is stale, wrong, missing or ambiguous; when Subjects are malformed, nested, missing, duplicated ambiguously, or the final dependency list would contain duplicate values; or when the requested path is absolute, escapes the approved root, is a symlink, a projection, or is missing. Do not repair any rejected carrier. Validate the complete resulting carrier, including frontmatter schema, identity, Subjects and uniquely resolved list values, before publication.

For an accepted non-no-op Subject change, require Version `+1` and an actual edit-time Updated At. Preserve all unrelated frontmatter and body bytes, unknown keys, formatting, and CRLF/LF line endings; only the explicit Subject list item and required Version/Updated At may differ. The default local preview is deterministic and writes nothing; opt-in staging writes only derived candidates under CA-D-425. Do not claim a new MCP binding. A no-op requires the complete intended Carrier to remain byte-for-byte unchanged. An equal replacement value or semantically equal list alone is not sufficient: changed serialization, ordering or any other Carrier bytes are an actual change and require Version +1 with actual time and exact prior history. Report a true no-op without a new Version, timestamp, archive, Revision or Journal effect. Recheck the expected pins at apply time, and prove the unchanged standalone `ATOM_UPDATE --apply` guard still rejects unsupported direct apply. Inject a failed validation or publication and prove the fixture returns byte-for-byte to its before ledger.

Use valid stable-ID non-archived originals under their admitted Status models, including correctly placed Plan Done and Backlog carriers. Prove both source and result pass the real complete-carrier validator without mocking it; retain the Active case. Verify exact Status, Summary, identity, placement, unrelated frontmatter, body bytes, and line endings remain unchanged in the proposed Carrier except for the declared Subject and required Version/Updated At spans. Reject Draft or archived Status/placement, invalid role-specific Status, status-folder mismatch, unavailable or ambiguous validation authority, and any otherwise invalid complete source or result without repair or writes. A no-op retains Status and creates no Revision or effect.

### Subject-profile preview cases

The closed Subject-only root envelope is exactly `{atoms, subject_profile?}`; each atom item remains exactly `{selector, expected, subject_patches}`. The exact path selector is a source locator, not Subject syntax. Exercise omission and explicit `legacy`, and explicit `approved`; each preview checks both its pinned source and proposed result with that one profile. Unknown or malformed profiles, extra root/item/patch keys, mixed Subject-only/full-carrier modes, cross-profile conversion, inferred profile selection, escaping, conjunctions, selectors inside a Subject value other than the approved initial form, and grammar migration fail.

Legacy keeps dots literal, uses `/` for bearer qualification and `:` for allowed values, and rejects every `atom(...)` selector. Approved recognizes `/` as broader-to-narrower, `.` as bearer-to-dependent, and `:` as Property-to-allowed-value, and accepts only the exact positive selector literals in CA-E-301. Prove that `Atom` and `atom` never normalize; reject `@`, empty/type-only/mixed-key/unknown-key/duplicate-key/positional/nested/later-position selectors and unquoted/escaped/wildcard/evaluated/aliased values. In `atom(...).Status`, prove the selected Atom remains Status's bearer and neither content_role nor type becomes Status's allowed value. Selector checks neither enumerate a concrete Atom row nor admit target semantics. For a non-no-op, verify exact selected scalar replacement, Version `N+1`, illustrative Updated At, full before/after digests, byte preservation outside Subjects/Version/Updated At, and deterministic `preview_sha256`.

The preview result includes its `subject_profile` and `subject_profile_evidence` with exactly `grammar_pins` and `native_admission: not_performed`; each grammar pin contains `atom_id`, `version`, `path`, and `sha256`, and these fields are included in the digest. Assert lexical syntax/direction validation only: no native endpoint, typed edge, target conformance, history, archive, Journal, MCP, source effect, or source migration is claimed.

### Instructed Subjects-only batch acceptance

Exercise the existing batch route using actual instruction/Initiative/Operator authorization and an exact ordered packet, with no extra form, review/pause response, content-review round, fabricated confirmation receipt or per-Atom semantic reports. Prove ordinary singleton admission remains unchanged. Test commit-current → create-drafts → commit-drafts → archive/promote → graph composition with actual outcomes; graph execution occurs only after the batch completes. Preserve separately instructed map-only behavior.

Require normal target/draft/patch/layout, exact source-before, archive, N+1/actual-time and conditional-write/readback checks. Prove the public batch frontier has no initial intent-hash metadata requirement and no redundant full-candidate validation gate, while fresh native intent remains internal where needed. Use independent before/actual/history byte ledgers, including self-rule publication followed by a fresh-current-rule next operation. Reject out-of-packet/held targets, forbidden non-Subject deltas, stale source/draft bytes, unsafe layout and archive collision. Inject later failure/uncertainty: earlier completed effects remain, remaining and held sources stay untouched, normal native failed-write restoration remains, and there is no automatic batch rollback/replay/retry/resume. Logging failures are truthful separate observations, not effect-completion gates.

### Ordinary one-target Subject application cases

The report/form cases in this section and Selected publication access cases apply outside CA-R-866's reviewed batch branch.

Exercise CA-D-531's exact Subject variant through the existing selected `update_atom` envelope and real shared Run/lifecycle composition, retaining generic-route regression cases. Use CA-D-425's deterministic intent and real complete-carrier/status validation with independently authored LF/CRLF before/intended/actual/history byte ledgers. Include Active, correctly placed non-Active current originals and no-op. Reject multiple independent targets, extra or mixed fields, caller authorization Booleans, fabricated starts/assessment, stale intent, grammar/report/definition/source drift, owner/path mismatch, projection/delivered copies, duplicate non-archived originals including unsafe or malformed competing claims, symlink/ancestor/inode swaps and archive collision.

For a non-no-op, verify completed bound assessment evidence from a shared review package or a Done Analysis Report binds the Subject-only intended proposal with old Version/time, and O145/O129 independently reopen exact evidence. A separate Analysis Atom is not required. Missing, malformed, stale, replacement-required, uncertain or wrong-class assessment prevents publication; Done/type checks apply only when an Analysis Report is supplied. Changing only illustrative preview time leaves the intent hash unchanged; changing a target/patch/profile pin/history destination or metadata rule changes it or refuses the request. Wrong expected intent or output must fail an independently authored check.

Verify actual O030 start retained in the selected Run and exact selected execute authorization precede effects; no direct call with an authorization Boolean can write. Require current Version `N+1`, one actual Project-time Updated At within the observed effect interval, exact intended Status/placement/identity/Summary/unrelated-byte preservation, exact predecessor bytes at `N` classified archived by placement, no second predecessor bump/time/status edit, and actual readback hashes bound to the intended hash. Require actual selected Run observations and independently verified current/history effect references, not prior Journal records or canonical receipts; queue acceptance or a log entry alone is not completion.

Inject caught errors after history publication, after current publication and during post-write validation, then prove exact current byte/mode restoration and removal of attempt-owned history while preserving pre-existing history and accepted Journal evidence. Inject failed restoration and verify partial/unknown recovery, retained evidence and no automatic replay. Inject Journal I/O failure after a real effect; retain the independently observed source/Run result and truthful append failure without a completion gate, automatic recording retry, recovery machinery or invoking publication again. Repeating the same admitted request never creates another update. Default local Subject preview remains mutation-free, staged preview changes no authoritative source, history or Journal, and standalone `ATOM_UPDATE --apply` remains rejected; none of these cases admits a new MCP route or bulk effect.

### Selected publication access cases

These are required checks of the staged-review and exclusive-window model, not observed passes or permission to remove the live publication guard:

1. Stage and review the exact bound source/delta/intent through existing admission. Reopen source, candidate and intent evidence rather than treating a staging manifest as approval. Preserve illustrative candidate time and governed effect-time materialization; changing only illustrative time does not alter the sealed intent. A no-op remains byte-identical and creates no current/history effect.
2. Establish the short exclusive window for the exact affected current/history/authority frontier, with no manual editing, maintenance/script writes, Git or synchronization changes to it. Resolve the existing `authorization_ref` to the purpose-specific record bound to the exact request, source/delta/intent, selected Session/Run and affected files. Exercise the connected Codex Session's form showing those bindings, the intended change and affected files; an explicit response confirming review and the pause is sufficient without separate identity proof. Reject tool arguments, spoofed client names, model assertions, caller-written JSON/hash and arbitrary callbacks as confirmation. Verify decline, cancel, malformed response, timeout, disconnect, unavailable issuer/resolver, missing or mismatched confirmation and bound-evidence drift refuse before effects. Exercise private same-process issuance and selected dispatch of the nonserializable one-use confirmation; reuse or use for another request/Session/Run/frontier must refuse. Preserve the public API, route and request fields, existing sealed permission, recorded Action start and complete-carrier checks. A missing window refuses before effects. This connection test does not authorize live publication or runtime activation.
3. Verify final source/authority/destination checks before current/history effects, independent readback and every invoked existing Action-local restoration, including restoration failure, within the confirmed window. Change bound evidence before final revalidation and require refusal without effects. Require no project-wide Engine write lock or replacement; other Engine writers are not excluded.
4. Inject the already required caught publication and postcondition faults while the window remains in force. Independently compare current/history bytes and modes, preserving pre-existing history and accepted Journal evidence. Retain the existing exact restoration requirements; failed or unverified restoration is partial/unknown, not success. Journal append/read must not replay an effect or introduce recording retry/recovery.
5. Demonstrate the declared limit: other Engine writers and a writer ignoring the window are not excluded by this model. Do not report universal concurrent-writer protection, crash-atomic multi-Carrier publication or an additional safety guarantee. Observed violated preconditions or uncertain effects retain the existing truthful refusal/failure disposition; this limit does not relax any required safety case.
6. Recheck existing closed API/admission/recording, local standalone-apply rejection and generic-route regressions. Source authoring or isolated preparation checks cannot establish current runtime acceptance, live Core migration permission, a new retry/recovery framework or unconditional guard removal.
7. Interrupt the process abruptly at current/history publication boundaries in an isolated fixture. Do not require crash-atomic restoration: retain interrupted disposition and inspect the actual affected current/history files and Run evidence before any separately admitted continuation. No automatic restoration claim, effect replay or completion receipt may replace observed facts.
8. Exercise the production existing `update_atom` changed Subject-only execute call at the actual outer Gateway request/session. Prove unchanged public schema and exact adapter/preview/manifest/request/lifecycle admission before the form, host-owned exact Operator/stage bindings, private same-process one-use issuance and existing selected dispatch with no DBOS enqueue. Use independent valid before/intended/actual/history ledgers and real complete-carrier, assessment, shared Run, window and Journal checks. Verify actual O030 start precedes publication, final readback and actual Run/result observations, including caught publication/restoration faults and truthful Journal I/O failure without a receipt gate, recording retry/recovery or effect replay. Negative form and evidence cases refuse before effects; interruption after effects remains truthful pending/unknown, never claimed zero-write. A forged child context, missing host binding, changed generation/source/request, mismatched confirmation or queue/worker serialization cannot admit publication. Assert generic update, preview, direct preparation and every other selected route retain their existing queue/preparation behavior. Do not restore O193/O194, change Release behavior or report isolated fixtures as connected-runtime acceptance. Production connected-Codex form acceptance and independent combined verification remain required before the existing live-publication guard can be relaxed.

### Opt-in staged-preview cases

Exercise `run --stage-preview` with the unchanged closed Subject-only payload, omission/explicit Profiles, successful multi-target batches with distinct stable IDs, LF/CRLF, a non-no-op and a no-op in one batch. Distinct source paths sharing an eligible source basename claim the same stable ID: reject that competing-original case before staging rather than treating numbered output folders as identity admission. Prove default dry-run output/digest and zero-write behavior remain unchanged. Reject generic input, mixed input, `--apply`, unknown payload fields and invalid preflight before staging. The pure planner must still perform no filesystem writes.

Independently compare each staged full UTF-8 file with the original preview bytes/hash, retaining its source filename under the deterministic payload-order directory. Verify illustrative Version/time only, unchanged no-op metadata, and real complete-carrier validation using the ORIGINAL logical source path and applicable Status/placement. Verify the closed manifest's exact original preview hash, per-target source pins/intent hash, actual candidate path/measured hash and validation evidence. Require explicit staging-only/illustrative/sources-unchanged result flags, generated batch/manifest paths and measured manifest hash; the manifest is not an approval token.

Reject symlinked/escaping staging ancestors, destination substitution, reused or occupied batch/file/manifest destinations and any overwrite. Inject partial write, candidate readback/hash/validation failure, source or competing-identity drift, and grammar drift before the final check. Recheck with the SAME illustrative time: mismatched preview/pins/intent refuses success, not a refreshed preview. Failures report actual retained artifacts with no success seal or unsafe cleanup. Prove original bytes/modes, existing history and Journal remain unchanged in all cases, with no promotion or MCP call. Editing a candidate later invalidates its measured hash; no ongoing monitor is implied.

### Acceptance criteria

- Valid same-ID applies match their sealed previews and admitted change classes. Every actual change, including carrier-only, refinement and Status-only, advances Version exactly once and preserves exact prior state; no-op preserves Version/time. Retain identity, Summary, Type, path and filename; the unassigned Draft remains unassigned. Summary/Type changes require replacement.
- default dry runs change nothing; opt-in staging changes only its derived temporary batch. rejected requests change no authoritative source, history **or** Journal, and failed staging discloses any retained partial artifacts. no temporary, mixed, **or** partially updated authoritative state remains **after** a successful apply. an actual no-op is not a fictitious accepted edit **or** semantic Revision.
- successful recovery restores the entire mutable before-state, preserves pre-existing history **and** accepted Journal evidence, **and** reports the failed attempt rather than update success.
- preflight-only rejection does **not** prove recovery. incomplete **or** unverified restoration fails the Evaluation.

### Failure disposition

reject a realization that violates **any** required case. preserve sealed preconditions, authority **and** classification result, exact previews, rejection evidence, prior **and** final Carriers, fault position, **and** actual recovery result.

### Direct MCP Subject preparation acceptance

Verify CA-D-425's closed preview_subjects/stage_subjects contract through production registered MCP with actual source/binding validation. Discovery exposes ATOM_UPDATE as atom_update, not selected update_atom or a broader Workflow under this preparation-only schema. Exercise explicit profile and logical ID/Version/SHA-256, unique ordered targets, scalar/by-current-value and complete-set patches, changed/no-op results. Reject unknown fields, add/remove, indexes, physical selectors, mixed generic edits and publication options before scratch work.

Test the native expected_preview_sha256 check against the preview actually used: mismatch refuses immediately after native preview and before even scratch-base creation. Direct stage must pass the reviewed seal and same illustrative time; an adapter-only earlier check is insufficient. Existing CLI omission remains compatible. Retain final same-time preview equality and test source, grammar, definition and Project-boundary drift.

Compare independent expected preview/intent seals and LF/CRLF bytes. Test cross-owner identity ambiguity, delivered/history/Draft exclusion, selected unsafe/malformed sources and unrelated malformed excluded C/A. The latter must not become global current-schema admission; possible selected-ID claims still refuse. Preview changes no bytes/membership. Stage creates only a fresh scratch batch, validates reopened exact bytes at original source context and writes/readbacks the success manifest last; originals/history/Journal remain unchanged.

Inject write/readback/validation/final-currentness and post-helper provider failures. Preserve actual retained/unverified artifact references without a success seal, false zero-effect report, unsafe cleanup or replay. Neither operation creates Session/Action Run/Journal receipts or claims an Atom update; actual enclosing-Step recording remains caller-owned. Existing publication tests/guards are separate. Source authoring and direct-helper fixtures alone do not prove connected-MCP readiness.

### Existing-Atom edit-draft batch cases

Exercise `stage_subject_batch` with strict limits1..10/default10, rejecting Boolean/out-of-range values, malformed packets, mixed draft pins and unsafe paths. Verify bounded actual progress and complete schema1 packet output, exact temporary `CA-R-draft` or `<canonical-ID>@<proposed-version>-draft`/Status Draft files, unchanged canonical/history bytes and modes, source-preserving body/metadata, and changed-proposal N+1/illustrative time. Accept legacy `<canonical-ID>@draft` only as compatibility input with an explicit proposed Version. True no-ops retain source Version/time. New-Atom Drafts remain ID-free or use the role-draft marker and canonical ID allocation remains deferred until explicit promotion.

### Draft marker promotion cases

Exercise a new ID-free Draft, a `CA-R-draft` Draft, an existing `CA-R-123@4-draft` Draft, and legacy `CA-R-123@draft`. Require filename/carried-marker agreement, explicit target and expected current Version/digest, and refusal on stale or mismatched bindings. Promote the version-qualified case to the same canonical `CA-R-123` at Version 4, archive the exact Version-3 predecessor bytes, restore the source Status and remove only the pinned Draft. For ID-free/role-draft cases, require an explicitly admitted fresh next-unreused ID. Journal absence or append failure must remain diagnostic only; no retained Draft history or lineage record is a promotion gate.

After the instructed draft commit, promote using existing request authorization without another full-candidate validation, content-review or confirmation round. Retain normal exact target/draft/patch/layout, archive, metadata, conditional-write and readback checks. Restore canonical ID and original Status (Active for the current migration), preserve unrelated bytes, and prove exact predecessor/N+1/actual-time outputs. Tampering or drift stops that member; completed earlier members remain and held/remaining sources are unchanged. Verify each draft-backed frontier includes the draft path after current/required archive paths, with exactly `{type: "draftRemoval", path, atom_id, sha256}` bound to the packet, including canonical no-op members. Reject wrong paths/digests/fields. After verified canonical output and any required archive readback, verify conditional deletion of only the exact pinned draft. Inject cleanup I/O failure or changed draft bytes: stop, retain published canonical/archive effects, report actual cleanup state and never roll back completed effects or delete an unverified file. For this batch, local carrier parsing, exact descriptors, explicit old-value patches, selected grammar, safe layout, deterministic byte materialization and conditional-write/readback are the normal checks; do not repeatedly revalidate unchanged body content or build a global reference inventory for every member. The existing final graph operation remains separate. Do not fabricate Draft lineage or confirmation receipts, or automatically replay/roll back the batch.
