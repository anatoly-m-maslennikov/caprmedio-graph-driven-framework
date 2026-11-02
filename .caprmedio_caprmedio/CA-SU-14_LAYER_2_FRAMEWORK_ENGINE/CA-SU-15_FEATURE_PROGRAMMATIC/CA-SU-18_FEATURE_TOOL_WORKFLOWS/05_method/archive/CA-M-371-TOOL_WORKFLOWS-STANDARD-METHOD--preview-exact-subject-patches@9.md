---
atom_id: CA-M-371
content_role: Method
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_UPDATE"
  depends_on: [Atom, Subject, Artifact/Carrier, Atom/Revision]
version: 9
updated_at: "2026-10-13 05:22:20 +0400"
relations:
  relates_to: [CA-R-866, CA-O-030, CA-E-304, CA-D-425]
---
# Summary

Preview exact Subject patches for valid Atom carriers

## Scope

The Subject-only preview, opt-in local candidate staging, and pure intended-proposal preparation method for ATOM_UPDATE.

## Claim

ATOM_UPDATE **must** prepare a Subject-only preview from explicit, source-pinned
replacements under one selected `subject_profile`: omission selects `legacy`,
`approved` is explicit, and unknown or malformed supplied profiles fail. It
validates each exact selector and its Atom ID, Version and SHA-256 before
locating the stated direct Subject occurrence. It validates source and result
syntax under that same profile, replaces only the stated scalar or
uniquely current-value-selected dependency-list item, validates the complete resulting carrier, and returns the
exact default preview without writing a Carrier. The pure planner remains free of filesystem writes; an opt-in local wrapper may export derived preview copies under CA-D-425 without updating any authoritative Carrier.

Subject-only preview **must** select a complete original Atom Carrier with a stable Atom ID, excluding Draft and archived carriers by both carried Status and placement. Both the pinned source and proposed result **must** pass existing complete-carrier validation, including the applicable Content Role/Type Status model and correct Carrier placement. Preserve the carried Status byte-for-byte; do not activate the source or perform a lifecycle transition. Missing, ambiguous, unsupported, or stale validation authority **must** fail closed.

## Details

The logical Workflow owns Subject eligibility, selected profile, proposal, Version, preview and effect admission; its connector receives explicit logical targets, deltas and bound source/schema/permission evidence through the coherent interface. The closed legacy CLI payload and Markdown staging layout below are private existing implementation bindings, not a new universal connector schema. This authority split moves no code and does not establish that the existing implementation admits the new connector contract.

Accept only the closed root `{atoms, subject_profile?}` and an item exactly
`{selector, expected, subject_patches}`, with
`expected = {atom_id, version, sha256}`; reject unknown root or item keys.
Separate `subject_patches` from complete-frontmatter or body replacement. Reject
duplicate selected files. For each patch, require `field`, `old`, and `new`;
for `depends_on`, resolve exactly one existing entry by the exact current value `old`; reject a caller-supplied index. Legacy uses `/` bearer qualification and `:` allowed values with literal dots and rejects every `atom(...)` selector. Approved uses `/` broader-to-narrower, `.` bearer-to-dependent, and `:` Property-to-allowed-value, and accepts only the exact initial lowercase selector forms registered by CA-R-1321. Preserve `Atom`/`atom` case distinction; reject `@`, type-only or mixed-key selectors, duplicate or unknown keys, positional, nested, or later-position selectors, escaping, conjunctions, wildcards, evaluation, aliases, and inferred profile detection in Subject syntax. Reject invalid carrier shape, missing or ambiguous old values, stale pins, path escapes, symlink targets and duplicate resulting dependencies. Preserve all unrelated bytes and line endings. Selector syntax validates neither a selected Atom instance nor a relation, native admission, or source effect.

Classify an actual Subject value change as a semantic revision with Version
`N + 1`; a no-op creates no revision. The preview result returns the selected
`subject_profile` and `subject_profile_evidence` containing exactly
`grammar_pins` and `native_admission: "not_performed"`; every grammar pin
contains `atom_id`, `version`, `path`, and `sha256`, and the preview seals those
fields in its digest. Legacy cites the five exact historical definitions and
approved cites the five current definitions. The local operation is preview-only.
Existing sealed generic update admission and its standalone-apply guard remain
unchanged. Do not repair legacy carriers, select a migration, infer relations,
create Journal/history effects, or add an apply path from the preview.

Property add/replace/remove, list entry add/remove and complete-set replacement follow CA-R-1934-TOOL_WORKFLOWS-CORE-REQUIREMENT--edit-atom-properties-by-current-values. The by-current-value contract requires new implementation and validation; historical index-based fixtures are not current acceptance. For the selected Subject publication model under CA-R-866/CA-O-030, prepare source-bound intended change and staged review evidence before the exclusive affected-file window and shared cooperative Engine lock. Candidate timestamps remain illustrative; intended metadata rules remain sealed and actual metadata are still materialized at the effect. This pure preparation neither acquires effect permission nor performs publication or restoration. Live changed-Subject publication remains blocked until the selected access binding and combined checks are independently accepted; preview, staging or this Method cannot remove its guard. The
historical `@<version>` archive filename convention is Delivery-owned and does
not give `@` a Subject role.

For reuse by CA-D-531's one-target Subject update, the same pure planner **must** also derive the complete intended Carrier by replacing only the exact Subject spans, retaining the old Version and Updated At. Return the exact proposal pins and CA-D-425's `subject_intent`/`subject_intent_sha256`, which bind the selected complete target, ordered patches, grammar evidence, effect-time metadata rule and exact predecessor-history destination. The hash excludes the separate illustrative timestamp and is unchanged when only that illustrative time changes. A no-op binds unchanged bytes and no history effect. Rechecking a changed source, grammar pin or intended effect yields a changed intent or refusal, never a silently refreshed approval.

This preparation supplies neither an identity assessment nor effect permission. CA-O-067/CA-O-145 assess the intended proposal under CA-R-1892 and CA-D-585; CA-O-030 owns the separately admitted existing-MCP effect. Reuse this planner without converting its local preview into a source-effect writer or weakening standalone apply rejection.

### Opt-in local candidate staging

For `run --stage-preview`, first obtain the existing complete Subject-only preview without changing its closed payload or digest. Reject generic input and `--apply` before staging. Reuse each exact illustrative `proposed_carrier` as UTF-8 bytes, including unchanged no-op metadata; do not recompute a later illustrative time. Export under CA-D-425's fresh generated batch and deterministic numbered-filename layout using create-only, no-follow operations with no overwrite.

Read back every candidate and compare exact bytes and measured SHA-256 with the original preview. Run the real complete-carrier validator using the original logical source path, identity, placement and applicable Status model, not the temporary candidate's placement. Re-run the same pinned preview with the initial illustrative time and require the same `preview_sha256`, target pins and intent hashes after checking source identity/currentness and grammar. Any mismatch refuses success; do not silently refresh sources or candidates.

Only after all checks produce the separate closed manifest and enclosing staging-only result defined by CA-D-425. Return actual partial artifact references on write/readback/validation/currentness failure, without a success seal, authoritative/history/Journal writes, promotion or unverified cleanup. This is a point-in-time check; later use must recheck candidate hashes rather than treat the manifest as approval.
