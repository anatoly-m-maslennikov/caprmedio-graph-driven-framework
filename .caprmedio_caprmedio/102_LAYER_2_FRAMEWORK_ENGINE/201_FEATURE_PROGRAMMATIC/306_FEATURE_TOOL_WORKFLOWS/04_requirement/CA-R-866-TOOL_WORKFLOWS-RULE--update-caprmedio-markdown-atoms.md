---
atom_id: CA-R-866
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Updated At
version: 46
updated_at: 2026-10-27 20:00:11 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Update CAPRMEDIO Markdown Atoms

## Scope

Same-identity updates of exact selected Markdown Atom Carriers by the ATOM_UPDATE Tool.

## Claim

the ATOM_UPDATE Tool **must** provide same-identity updates of the frontmatter, content, **or** both for exact selected Markdown Atoms:

- preserve the Carrier path, filename, Atom identity, Type **and** Summary. do **not** assign an ID **to** an unassigned Draft merely **to** update its Carrier. every Summary or Type value change requires replacement with a new Atom ID and predecessor archival, **not** a same-ID update.
- resolve the admitted change class against the exact current Revision **and** proposal under CA-R-1432, reusing the current identity assessment under CA-O-067 where applicable. Every actual changed same-ID Atom update, including carrier-only, equivalent refinement and Status-only edits, advances Version by **`=1`** and preserves the exact prior Revision as required by the governing history rules. Change-class assessment does not waive the increment. replacement-required **or** uncertain classification must stop this update rather than silently changing identity **or** assuming permission.
- refresh Updated At **to** the actual accepted edit instant under CA-R-1788 for **every** accepted edit, including formatting-only **and** lossless-serialization edits. an actual no-op creates no fictitious edit, Version, timestamp refresh **or** archive effect; retain its truthful result for the governing Run contract.
- reject duplicate, missing, ambiguous, invalid, **or** stale explicit targets; preflight each one-Atom Action before its effect. Modify does not silently Find or substitute targets.
- modify **`=1`** explicit Atom target per Action with its expected Revision or digest. Preserve that Action's verified mutable before-frontier and storage-effect safeguards on effect or postcondition failure. A several-Atom Workflow stops at its first failed Action, retains completed Actions and leaves remaining targets untouched; do not promise cross-Atom rollback or all-or-nothing success.
- permit reuse of generic metadata **or** Relation-patch mechanics while retaining responsibility for Atom authority validation, admitted change class, Revision, one-Atom storage-effect safeguards, **and** effect semantics.
- default **to** mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.

The Tool **must** also accept the additional closed Subject-only preview root
`{atoms, subject_profile?}`. Every Atom item is exactly
`{selector, expected, subject_patches}`, where
`expected = {atom_id, version, sha256}`. Unknown root or item keys **must**
fail. Each replacement `subject_patches` entry has `field = governs|depends_on`,
exact `old` and explicit `new` values. For `depends_on`, the current value
`old` must identify exactly one existing list entry; a caller-supplied index
is not admitted. An Atom item using `subject_patches` must not also request
complete-frontmatter or body replacement. The selected files must be unique
within the payload.

Logical Property edits additionally support explicit add, replace and remove; list edits support entry add/remove, replacement by unique current value or complete-set replacement under CA-R-1934-TOOL_WORKFLOWS-CORE-REQUIREMENT--edit-atom-properties-by-current-values. Section edits follow CA-R-1933-TOOL_WORKFLOWS-CORE-REQUIREMENT--edit-one-explicit-atom-section. Every Summary value change requires a new Atom ID and predecessor archival through the replacement Workflow, even when the Claim remains unchanged.

Subject-only preview **must** select a complete original Atom Carrier with a stable Atom ID, excluding Draft and archived carriers by both carried Status and placement. Both the pinned source and proposed result **must** pass existing complete-carrier validation, including the applicable Content Role/Type Status model and correct Carrier placement. Preserve the carried Status byte-for-byte; do not activate the source or perform a lifecycle transition. Missing, ambiguous, unsupported, or stale validation authority **must** fail closed.

Omitted `subject_profile` selects `legacy`; `approved` is explicit; unknown or malformed supplied profiles **must** fail. Subject patches apply only to direct structured `subjects.governs` and `subjects.depends_on` fields, and the selected profile validates both the source and resulting scalar Subjects. Legacy uses `/` bearer qualification and `:` allowed values with literal dots and rejects every `atom(...)` selector. Approved uses `/` broader-to-narrower, `.` bearer-to-dependent, and `:` Property-to-allowed-value, and accepts only the exact initial lowercase selector forms registered by CA-R-1321. `Atom` and `atom` remain distinct; both profiles reject `@`, escapes, every other selector construction, conjunctions, wildcards, evaluation, aliases, and profile inference in Subject syntax. This is syntax validation only and does not enumerate selector instances, admit a target, or add an apply path.

Subject patches **must** reject a malformed or nested legacy Subjects shape, an
absent or ambiguous current value, a stale pin, an escaped or symlink target, or a
duplicate resulting dependency. The Tool **must** retain complete-carrier
validation and preserve every unrelated byte and line ending. A successful
Subject value change is a semantic revision with Version `N + 1`; a no-op
creates no revision. The preview result **must** return the selected
`subject_profile` and `subject_profile_evidence` containing exactly
`grammar_pins` and `native_admission: "not_performed"`; every grammar pin
contains `atom_id`, `version`, `path`, and `sha256`, and preview seals those
fields in its digest. Legacy cites the five exact historical definitions and
approved cites the five current definitions. Local use remains preview-only; an
illustrative preview timestamp is not an execution receipt. This mode does not
repair, migrate, infer ontology, adopt a Subject grammar, or add a standalone apply path.

The local wrapper **may** provide opt-in `run --stage-preview` for this same closed Subject-only payload, without changing the default dry run. Reject this option with generic update input or `--apply` before creating staged artifacts. Export only the existing illustrative proposed Carriers into a fresh Tool-generated `.caprmedio_tmp/subject-preview/<opaque-id>/` batch under CA-D-425's safe layout. Do not write authoritative originals, history, Journal, or promotion effects. Candidate Version/time remain illustrative; no-op metadata remain unchanged.

Staging **must** independently read back exact candidate bytes and SHA-256, run real complete-carrier validation against each original logical source path and applicable Status, then recheck source/identity/grammar pins using the same illustrative time. Return CA-D-425's separate closed manifest only after the whole batch passes; source drift must refuse success rather than refresh a preview. On failure report retained partial artifacts without a success seal or unsafe cleanup. Staged files are point-in-time review evidence, never effect approval.

CA-M-371 defines the same-profile preview method. The historical
`@<version>` archive filename convention remains a Delivery concern and is not
a Subject operator. CA-O-030 defines the operational Action. CA-E-304 supplies
its automated conformance cases **without** duplicating them **in** this
capability Requirement.

## Details

The logical Workflow owns Subject eligibility, selected profile, proposal, Version, preview and effect admission; its connector receives explicit logical targets, deltas and bound source/schema/permission evidence through the coherent interface. The closed legacy CLI payload and Markdown staging layout below are private existing implementation bindings, not a new universal connector schema. This authority split moves no code and does not establish that the existing implementation admits the new connector contract.

### Identified legacy Concern input

For an explicitly selected, already identified Concern under `01_concern`, a legacy single descriptive first H1 may supply the source Summary value for a same-ID full-content repair. Require exactly one nonempty unfenced H1 and no competing Summary; do not infer or assign an identity. The proposed body must use the canonical literal `# Summary` with that exact value and pass complete Concern validation. Preserve ID, path, Type and intended Status; a changed Summary value still requires replacement. Reuse existing assessment, authorization, exact source checks, Version N+1/actual Updated At, exact predecessor history and result readback. This source-input normalization adds no endpoint, flag or proof/approval mechanism and does not relax Subjects-only source validation.

### Instructed Subjects-only batch

The Operator's explicit instruction authorizes the exact ordered Subjects-only map through the existing request Initiative and Operator authorization. Retain the instruction/request and packet bindings in execution context; do not require a separate form, content-review round, review/pause response or batch-confirmation receipt, and never fabricate one. The map binds each selected Atom's canonical target, exact current Version/SHA-256, Subject profile and explicit ordered patches. It does not authorize unlisted targets, held sources or ordinary content changes.

For the instructed draft-backed flow, commit current state, create the full edit drafts, commit the drafts, archive each exact current predecessor and promote its draft through the existing updater, then rebuild the entity graph through its existing operation only after the batch completes. The caller composes these existing operations and records their actual results; no new Tool family, executor or recovery gate is introduced. A separately instructed map-only batch remains available without draft staging.

Before each independent effect, retain the normal local target/draft/patch/layout, current-source, conditional-write, archive, Version/time and readback checks. Do not add a separate full-candidate validation pass, semantic content review or initial intent-metadata gate. Fresh native intent may be derived internally at the operation; no initial `subject_intent_sha256` is required in the public batch effect frontier. Only declared Subjects plus exactly N+1 and actual Updated At may change; preserve canonical ID, Summary, Type, original Status, placement and every unrelated byte. Restore the original Status from the temporary draft marker; an Active source therefore promotes to Active without changing generic non-Active semantics.

Advance in packet order only after verified applied or truthful no-op results. Stop at the first failed, refused, stale, canceled or uncertain member, retain completed effects and leave remaining and held sources untouched. Keep existing native failed-write restoration/error handling, but introduce no automatic batch rollback, replay, retry or resume. Report actual effects and any logging failure separately; a log is observation, not permission or proof of completion.

### Existing-Atom edit-draft staging and promotion

CA-D-446's explicitly source-pinned edit draft is the full proposed next Revision in the owning role's `draft/` folder. A Draft may omit `atom_id` and use the ID-free empty-number filename. When a Draft carries a marker, use `CA-R-draft` (or `<PREFIX>-<ROLE>-draft`) for a new Atom, or `<canonical-ID>@<proposed-version>-draft` for an edit; legacy `<canonical-ID>@draft` remains compatibility input and requires an explicit proposed Version in the request. A carried marker is Draft-only proposal metadata, never a canonical identity. The filename identity segment must exactly match the carried marker, and a version-qualified marker must equal its carried proposed Version. Leave the canonical source untouched while staging; preserve body and unrelated metadata outside the marker, Status and proposed Version/time fields. A true no-op keeps source Version/time.

For promotion, bind the exact Draft bytes to an explicit target and expected state. An existing marker such as `CA-R-123@4-draft` requires target `CA-R-123`, an exact current predecessor at Version 3, and a proposed Version 4; legacy `CA-R-123@draft` supplies the same binding explicitly in the request. Archive the exact current predecessor bytes, materialize the canonical target at the proposed Version with its original admitted Status, and remove the Draft carrier. An ID-free or `CA-R-draft` Draft uses an explicitly admitted fresh next-unreused canonical ID. Any target, Version, digest, marker, placement or destination drift refuses before effects. No retained Draft history, lineage or Journal append is a gate; Journal records observations after the independent effect.

The existing `atom_update` Tool accepts `{operation: "stage_subject_batch", subject_batch: {path, digest}, limit?}` under CA-D-531. `limit` is a strict integer 1..10, default 10. Each call creates at most that many drafts with normal safe create-only/no-follow file checks and readback, changes no canonical/history files, and returns compact actual progress: `operation`, `state: "staging"|"staged"|"stopped"`, `count`, `completed`, `remaining`, `stage_run_id`, and `reviewed_packet: {path, digest}|null`, plus actual failure evidence. Only completed staging returns the final schema1 packet pinning every draft. Preserve truthful partial artifacts; never report partial work as completed.

For this batch, local carrier parsing, exact descriptors, explicit old-value patches, selected grammar, safe layout, deterministic byte materialization and conditional-write/readback are the normal checks; do not repeatedly revalidate unchanged body content or build a global reference inventory for every member. The existing final graph operation remains separate.

No separate full-candidate validation, content-review or confirmation round follows staging or the draft commit. Existing request authorization carries the instructed promotion. At each target's operation reopen the exact pinned current/draft bytes, verify the explicit marker/target/Version binding, normalize the marker and Status to the canonical ID and original Status, and apply the normal native Subjects-only patch/layout, archive, metadata and conditional-write/readback checks. A full proposal does not authorize any additional metadata/body delta. Use actual effect time and the existing exact predecessor archive; fail on source/draft/target drift without silently rebinding. Same-MCP-connection staging is unnecessary. Existing first-failure and native failed-write handling remain; no automatic batch rollback or replay is introduced. After verified canonical output and any required predecessor readback, conditionally remove only that member's exact packet-pinned draft bytes. If draft cleanup fails or its bytes have drifted, stop and report the actual cleanup failure, preserving the published canonical Revision and archive; do not roll them back or remove another file.

### Ordinary one-target Subject update

The existing Project-local MCP `update_atom` route **must** also accept the closed Subject-only parameter variant defined by CA-D-531: `{target, subject_patches, subject_intent_sha256, subject_profile?, semantic_assessment_report?}`. It selects exactly one complete current original Carrier and reuses the preview's eligibility, exact scalar-patch, same-profile, complete-carrier and byte-preservation checks. Reject mixed generic replacement fields, unknown fields, projection or delivered copies, owner/path mismatch, competing non-archived originals, and an unsafe or unverifiable claimed competing owner. Bulk preview does not authorize bulk lifecycle execution.

The mutation-free preparation **must** return CA-D-425's deterministic `subject_intent` and `subject_intent_sha256`. For a value change, derive the complete intended proposal by changing only Subjects while retaining the old Version and Updated At for CA-O-067's assessment. Reuse current completed assessment evidence from a shared review package or a Done Analysis Report, and the exact CA-O-145 assessment under CA-R-1892 and CA-D-585; syntax validation and a caller-supplied class are not identity or lineage evidence. An unresolved, replacement-required, stale, or mismatched assessment prevents this effect.

Application **must** consume CA-D-527's exact authorized execute envelope through the existing selected route, actual selected execution session and actual CA-O-030 Action start retained in the selected Run, with the exact completed CA-O-145 assessment. A caller Boolean, adapter envelope, local preview, candidate acceptance, or direct internal call grants no apply authority. Recheck all source, grammar, report, validation, definition, permission and destination evidence before effects.

A changed current Carrier **must** retain ID, Summary, Status, path, filename, every unrelated byte and line ending; set Version exactly to `N+1`; and materialize Updated At once from actual Project time at the effect. Preserve the exact predecessor bytes at Version `N` in the existing Delivery-governed history location, classified as archived history by placement, without a second Version increment or invented status/time edit. Verify actual after bytes and hash and bind them to the intended hash in the shared result. No-op creates no Carrier/history/change event; retain the actual Run observation without inventing a change. A caught publication/postcondition error requires an attempt to restore the verified mutable before-frontier and remove attempt-owned history only; failed or unverified restoration is not success and never permits automatic effect replay. Journal append/read has no prior-history, chain, validation, receipt, deduplication, retry or recovery prerequisite and does not gate or prove source-effect completion; report any actual recording I/O failure truthfully without replaying the effect. Abrupt crash or interruption is not crash-atomic: retain interrupted disposition and inspect actual affected current/history files and Run evidence before any separately admitted continuation. The local `ATOM_UPDATE --apply` guard and generic request behavior remain unchanged.

### Selected Subject publication access model

For ordinary one-target Subject publication outside the reviewed batch branch, stage and review the exact source-bound change before a short exclusive window over the affected current Carrier, predecessor-history destination and governing authority sources. Reuse the existing sealed source/delta/intent, assessment, permission and Run bindings; review is not effect permission. Staged candidate metadata remain illustrative. Actual Version and Updated At are materialized under the existing effect-time rule, not fixed by candidate review.

The existing `authorization_ref` **must** resolve a fresh purpose-specific trusted-host record of the Operator's explicit review of the exact source-bound intended change and confirmation to pause manual editing, maintenance/script writes, Git and synchronization for its affected current/history/authority frontier. A form response from the connected Codex Session is sufficient Operator confirmation when the form shows that exact request, selected Session/Run, intended change and affected files and explicitly confirms both review and the pause; no separate identity proof is required. Tool arguments, client names, model assertions, caller-written JSON or hashes and arbitrary callbacks never count as that response. Bind the record to the exact existing request, source/delta/intent, selected Session/Run and affected files; recheck it before effects. Issue the nonserializable one-use confirmation privately and consume it through the existing selected dispatch in the same process; the public API, route and request fields remain unchanged. Decline, cancel, malformed response, timeout, disconnect, unavailable issuer/resolver, missing or mismatched confirmation and any bound-evidence drift refuse before effects. This accepted trust model authorizes building the connection, not publication or runtime activation.

For this one changed Subject-only execute request, the existing connected Project-local MCP host may perform the admitted selected dispatch in the same process that owns the actual Codex request/session and issues the one-use confirmation, instead of enqueueing DBOS work. It must reuse the same closed request, exact current admission, saved request and selected Run/lifecycle implementation, validation, assessment, permission, restoration and truthful actual Run observations in the plain Project Journal. This exception changes dispatch placement only. Generic updates and every other selected operation retain the existing queue path. An unavailable or unconfirmed Subject exception refuses before effects; it is not permission to serialize confirmation, invent an endpoint or silently dispatch elsewhere.

During that window, no manual editing, maintenance/script write, Git operation or synchronization may change the affected sources, history or authority. Recheck the exact admitted frontier before effects; unavailable window, stale evidence or failed admission stops before effects. Preserve the window through current/history effects, independent readback and any existing Action-local restoration. No project-wide Engine write lock or replacement is required; distinct existing resource-specific locks remain unchanged. Retain all existing identity, complete-carrier, byte-preservation, ownership, restoration and truthful failure requirements.

This access model does not exclude other Engine writers and cannot protect against writers ignoring the exclusive window and does not itself establish crash-atomic multi-Carrier publication or a stronger guarantee. It does not waive an existing safety requirement, add effect permission or introduce retry/recovery policy. Live changed-Subject publication remains blocked until the selected model's actual binding and combined checks are independently accepted; choosing this model or revising sources does not remove the existing guard.

The by-current-value, Property and section contracts state required behavior; previous scalar-index fixtures are historical evidence and do not establish acceptance of this behavior. This source revision is neither implementation nor an execution receipt. Resume and retry policy for independent multi-Atom Actions remains deferred.

### Direct Subject preparation

ATOM_UPDATE also admits CA-D-425's direct MCP preview_subjects and stage_subjects operations. They are preparation Tool calls, not actual Atom-update Action Runs: preview writes nothing; explicit stage writes only fresh derived candidates and their manifest in the fixed Project scratch layout. They create no Session, Action Run, canonical Journal, authoritative Carrier or history effect. Actual enclosing-Step Tool-call recording and the existing Workflow semantic policy owner remain unchanged.

Direct input uses explicit logical Atom ID, Version, SHA-256 and selected profile. Support only implemented scalar/by-current-value replacement and complete dependency-set replacement; reject add/remove, generic edits, indexes and physical selectors. Preserve full selected-source/result validation, eligibility, identity/grammar/currentness and byte-preservation safeguards. Preparation supplies review evidence for later assessment without requiring or claiming completed O067/O145 assessment. Native staging must compare its own preview with the requested reviewed seal before any scratch creation, retaining same-time final revalidation. No supplied hash, candidate or manifest grants source-effect permission. Actual publication's source-effect admission guards remain unchanged; Journal recording is plain observation, not an admission or completion gate.
