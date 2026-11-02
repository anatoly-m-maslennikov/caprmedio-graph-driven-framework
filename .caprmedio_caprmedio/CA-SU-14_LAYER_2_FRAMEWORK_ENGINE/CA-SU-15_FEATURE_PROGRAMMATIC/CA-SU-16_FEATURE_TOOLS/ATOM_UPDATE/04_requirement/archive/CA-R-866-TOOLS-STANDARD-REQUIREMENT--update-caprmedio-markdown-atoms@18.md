---
atom_id: CA-R-866
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_UPDATE"
  depends_on: ["Atom", "Atom/Revision", "Atom/Summary", "Artifact/Carrier", "Atom Change Classification", "Atom/Revision/Updated At"]
version: 18
updated_at: "2026-10-12 05:39:01 +0400"
relations:
  relates_to: [CA-O-030, CA-E-304, CA-O-067, CA-R-1432, CA-R-1788, CA-R-1464, CA-R-1415, CA-R-1371]
---
# Summary

Update CAPRMEDIO Markdown Atoms

## Scope

Same-identity updates of exact selected Markdown Atom Carriers by the ATOM_UPDATE Tool.

## Claim

the ATOM_UPDATE Tool **must** provide same-identity updates of the frontmatter, content, **or** both for exact selected Markdown Atoms:

- preserve the Carrier path, filename, Atom identity, **and** Summary. do **not** assign an ID **to** an unassigned Draft merely **to** update its Carrier. a Summary change requires replacement under CA-R-1464, **not** a same-ID update.
- resolve the admitted change class against the exact current Revision **and** proposal under CA-R-1432, reusing the current identity assessment under CA-O-067 where applicable. `carrier_only` **and** equivalent `refinement` retain Version; `semantic_revision` advances **`=1`** Version **and** preserves the exact prior semantic Revision under CA-R-1415 **and** CA-R-1371. replacement-required **or** uncertain classification must stop this update rather than silently changing identity **or** assuming permission.
- refresh Updated At **to** the actual accepted edit instant under CA-R-1788 for **every** accepted edit, including formatting-only **and** lossless-serialization edits. an actual no-op creates no fictitious edit, Version, timestamp refresh **or** archive effect; retain its truthful result for the governing Run contract.
- reject duplicate, missing, ambiguous, invalid, **or** stale targets; preflight the complete operation.
- support **`=1`** exact target **or** a frozen bulk set of **`>=2`** targets with expected Revisions **or** digests. apply the complete validated set atomically **and** restore the mutable transaction frontier on apply **or** postcondition failure.
- permit reuse of generic metadata **or** Relation-patch mechanics while retaining responsibility for Atom authority validation, admitted change class, Revision, transaction, **and** effect semantics.
- default **to** mutation-free dry run. accept `--apply` **only** through authorized Project-local MCP delegation with a sealed Initiative action envelope.

The Tool **must** also accept the additional closed Subject-only preview root
`{atoms, subject_profile?}`. Every Atom item is exactly
`{selector, expected, subject_patches}`, where
`expected = {atom_id, version, sha256}`. Unknown root or item keys **must**
fail. Each `subject_patches` entry has `field = governs|depends_on`, exact
`old` and explicit `new` values, and a zero-based `index` when
`field = depends_on`. An Atom item using `subject_patches` must not also request
complete-frontmatter or body replacement. The selected files must be unique
within the payload.

Subject-only preview **must** select a complete original Atom Carrier with a stable Atom ID, excluding Draft and archived carriers by both carried Status and placement. Both the pinned source and proposed result **must** pass existing complete-carrier validation, including the applicable Content Role/Type Status model and correct Carrier placement. Preserve the carried Status byte-for-byte; do not activate the source or perform a lifecycle transition. Missing, ambiguous, unsupported, or stale validation authority **must** fail closed.

Omitted `subject_profile` selects `legacy`; `approved` is explicit; unknown or malformed supplied profiles **must** fail. Subject patches apply only to direct structured `subjects.governs` and `subjects.depends_on` fields, and the selected profile validates both the source and resulting scalar Subjects. Legacy uses `/` bearer qualification and `:` allowed values with literal dots and rejects every `atom(...)` selector. Approved uses `/` broader-to-narrower, `.` bearer-to-dependent, and `:` Property-to-allowed-value, and accepts only the exact initial lowercase selector forms registered by CA-R-1321. `Atom` and `atom` remain distinct; both profiles reject `@`, escapes, every other selector construction, conjunctions, wildcards, evaluation, aliases, and profile inference in Subject syntax. This is syntax validation only and does not enumerate selector instances, admit a target, or add an apply path.

Subject patches **must** reject a malformed or nested legacy Subjects shape, an
absent or ambiguous occurrence, a stale pin, an escaped or symlink target, or a
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

### Admitted one-target Subject update

The existing Project-local MCP `update_atom` route **must** also accept the closed Subject-only parameter variant defined by CA-D-531: `{target, subject_patches, subject_intent_sha256, subject_profile?, semantic_assessment_report?}`. It selects exactly one complete current original Carrier and reuses the preview's eligibility, exact scalar-patch, same-profile, complete-carrier and byte-preservation checks. Reject mixed generic replacement fields, unknown fields, projection or delivered copies, owner/path mismatch, competing non-archived originals, and an unsafe or unverifiable claimed competing owner. Bulk preview does not authorize bulk lifecycle execution.

The mutation-free preparation **must** return CA-D-425's deterministic `subject_intent` and `subject_intent_sha256`. For a value change, derive the complete intended proposal by changing only Subjects while retaining the old Version and Updated At for CA-O-067's assessment. Reuse the current completed Analysis Report and exact CA-O-145 assessment under CA-R-1892 and CA-D-585; syntax validation and a caller-supplied class are not identity or lineage evidence. An unresolved, replacement-required, stale, or mismatched assessment prevents this effect.

Application **must** consume CA-D-527's exact authorized execute envelope through the existing selected route, actual selected execution session and canonically recorded CA-O-030 Action start, with the exact completed CA-O-145 assessment. A caller Boolean, adapter envelope, local preview, candidate acceptance, or direct internal call grants no apply authority. Recheck all source, grammar, report, validation, definition, permission and destination evidence before effects.

A changed current Carrier **must** retain ID, Summary, Status, path, filename, every unrelated byte and line ending; set Version exactly to `N+1`; and materialize Updated At once from actual Project time at the effect. Preserve the exact predecessor bytes at Version `N` in the existing Delivery-governed history location, classified as archived history by placement, without a second Version increment or invented status/time edit. Verify actual after bytes and hash and bind them to the intended hash in the shared result. No-op creates no Carrier/history/change event; its actual Run still requires recording. Publication/postcondition failure restores the verified mutable before-frontier and attempt-owned history only; uncertain restoration or missing required recording is not success and never permits automatic effect replay. The local `ATOM_UPDATE --apply` guard and generic request behavior remain unchanged.
