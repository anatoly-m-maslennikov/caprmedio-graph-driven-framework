---
atom_id: CA-D-425
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: delivery
subjects:
  governs: "Tool/ATOM_UPDATE/Carrier"
  depends_on:
    - "Tool/ATOM_UPDATE"
version: 14
updated_at: "2026-10-12 23:13:13 +0400"
relations: {"delivery_for":["CA-R-866"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Deliver ATOM_UPDATE Tool

## Scope

This Delivery carrier defines the public file-operation contract of the canonical `ATOM_UPDATE` wrapper under owner `TOOLS`. The `ATOM_UPDATE` folder is an artifact collection below `TOOLS`, not an independently registered Scope Unit. It retains the existing generic update input and sealed apply guard and specifies authoritative-source-read-only Subject-only preview with opt-in local derived-candidate staging. The revised by-value and add/remove/full-set contracts require future implementation verification; historical index-based fixtures and source pins do not prove readiness. It does not define Core semantics, grammar adoption, migration decisions, source repair, or a new MCP route. CA-D-531 binds its separately admitted one-target Subject effect to the existing MCP update action.

## Claim

the `ATOM_UPDATE` Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/atom_update.py`; that Carrier realizes `CA-R-866` through the Action `CA-O-030`.

The delivered `ATOM_UPDATE` wrapper **must** accept only the closed Subject-only preview envelope `{atoms, subject_profile?}`. Omission means `legacy`; `approved` is explicit; an unknown or malformed supplied profile fails. Each atom item is exactly an exact repository-relative source-path `selector`, an `expected` object containing exactly `atom_id`, `version`, and `sha256`, and an explicit `subject_patches` list. A replacement patch contains exactly `field` equal to `governs` or `depends_on`, `old` and `new`. Select one dependency by its unique exact current `old` value; caller indexes are rejected. Missing, ambiguous or duplicate current values fail before effects. The connector may compute an occurrence location internally after binding the exact source state. The selected profile validates both the pinned source and the proposed result. For replacement, the old value must match the pinned current bytes exactly, and the new value is explicit: no target, relation move, profile conversion, grammar conversion, or migration mapping is inferred.

Legacy uses `/` as bearer qualification, `:` as Property-to-allowed-value, and literal dots, and rejects every `atom(...)` selector. Approved uses `/` as broader-to-narrower, `.` as bearer-to-dependent, and `:` as Property-to-allowed-value, and accepts only the exact initial lowercase selector forms registered by CA-R-1321; `Atom` and `atom` remain distinct. Both profiles reject `@`, and approved rejects every other selector construction, escaping, conjunction, wildcard, evaluation, and alias; it is neither a fourth operator nor carrier/display notation. The result includes the selected `subject_profile` and `subject_profile_evidence` containing exactly five reviewed grammar pins and `native_admission: not_performed`, sealed in `preview_sha256`. This is lexical syntax/direction checking only: it does not enumerate selector instances, establish target conformance, or admit a native endpoint.

The Subject-only mode is exclusive. A request carrying `subject_patches` must not also carry complete `frontmatter` or `content` replacement fields. The selected source must be a complete, canonical, non-symlink Atom Carrier at the exact path, with the expected identity, Version, and full-file SHA-256. The preview validates the complete resulting Carrier and preserves path, filename, identity, Summary, body, unrelated frontmatter, and line endings; only the declared Subject spans plus required Version and `updated_at` spans may differ.

Subject-only preview **must** select a complete original Atom Carrier with a stable Atom ID, excluding Draft and archived carriers by both carried Status and placement. Both the pinned source and proposed result **must** pass existing complete-carrier validation, including the applicable Content Role/Type Status model and correct Carrier placement. Preserve the carried Status byte-for-byte; do not activate the source or perform a lifecycle transition. Missing, ambiguous, unsupported, or stale validation authority **must** fail closed.

## Details

### Required logical list and Property operations

CA-D-623 carries explicit Property add/replace/remove, list entry add/remove, replacement of one uniquely matched current value, and replacement of the complete list set. For Subject-only use, the field must remain `governs` or `depends_on` and the operation must validate the complete resulting Subjects and Atom Carrier. Entry replacement is `{field, old, new}`; list addition is `{field, operation: "add", value}`; removal is `{field, operation: "remove", value}`; complete-set replacement is `{field, operation: "replace_set", old, new}`, with exact current and proposed collections. Scalar `governs` replacement retains `{field, old, new}`. Missing or ambiguous targets, duplicate proposed dependencies, unknown fields and caller indexes fail. No generic content edit may be mixed into Subject-only preview/staging.

These are required future input shapes, not claims about the current executable, stored staging candidates, installed MCP or old passing fixtures. Existing historical manifests/receipts retain their original bytes and pins; none is made current by this source revision.


The local dry-run result **must** expose the exact patch set, before and after SHA-256 values, expected Version `N+1`, an illustrative `updated_at` value, and a canonical `preview_sha256` over the complete deterministic preview. The illustrative time is not an execution receipt. Empty or unchanged patches are reported as a truthful no-op and do not create a revision. Invalid or nested Subject shapes, missing or repeated occurrences, stale identity/version/digest, invalid profile syntax, collisions, overlapping spans, path escapes, symlink targets, and incomplete files stop before staging or any authoritative write.

The existing generic updater remains available for its complete-carrier contract; Subject-only input does not mix with it and does not weaken the standalone `--apply` guard. The default local preview invokes no MCP and performs no filesystem write. Opt-in staging invokes no MCP and writes only derived temporary candidates; it performs no authoritative Carrier, history or Journal write. A separately authorized one-target Subject effect uses only the existing MCP `update_atom` route under CA-D-531 and CA-O-030, not this local wrapper or a new transport. This contract does not itself advertise an installed runtime capability, refresh an image/manifest, select a migration batch or grant source-effect approval.

### Opt-in local staged preview

The existing local `run` command **may** accept `--stage-preview` only for the unchanged closed Subject-only payload `{atoms, subject_profile?}`. Reject this option for generic update input or together with `--apply` before creating artifacts. Default dry run and its result/digest remain unchanged, the pure planner writes no files, and standalone apply remains disabled. The option grants no source effect, promotion, new MCP route, API, runtime or monitoring capability.

After a complete pinned preview passes, create a fresh Tool-generated batch at `.caprmedio_tmp/subject-preview/<opaque-id>/`. The caller does not choose the destination. For the one-based ordinal in payload order, use a directory padded to at least four decimal digits (`0001`, `0002`, ...) and retain the exact source filename beneath it. Thus distinct sources with identical basenames cannot collide; the manifest maps each exact source path. Every created directory/file must remain under the approved Project root through no-follow traversal; use create-only writes, reject symlink/escape/substitution/occupied destinations, and never overwrite a candidate or manifest.

Export the existing preview's complete illustrative `proposed_carrier` as exact UTF-8 bytes. Read back and compare bytes and measured SHA-256 with that preview; independently run existing complete-carrier validation on the actual reopened candidate bytes using the ORIGINAL logical source path, identity, applicable Status and placement, not temporary placement. Candidate Version/time are illustrative; no-op Version/time are unchanged. Finally recheck pinned source bytes/current identity uniqueness and grammar with the SAME illustrative timestamp, requiring the same original `preview_sha256`, per-target pins and intent hashes; any change refuses success rather than silently refreshing the preview.

The separate `manifest.json` is a closed object with exactly `schema_version: 1`, `preview_sha256` and `atoms`. `atoms` follows payload order; each entry contains exactly `source`, `subject_intent_sha256`, `candidate` and `validation`. `source` is exactly `{path, atom_id, version, sha256}` for the pinned original; `candidate` is exactly `{path, sha256}` for the actual safe Project-relative candidate path and measured full-file hash; `validation` is exactly `{state: "passed", logical_source_path}` binding real complete-carrier admission to the source path. The original preview hash already binds the chosen Profile, grammar and illustrative proposal; staging does not replace or recalculate it. Create and independently read back the success manifest only after the complete candidate/readback/validation/final-currentness checks pass.

The enclosing local result must retain the complete original preview unchanged so its `preview_sha256` remains reconstructible, and expose `staging_only: true`, `illustrative: true`, `sources_unchanged: true`, the actual generated stage root, manifest path and measured manifest SHA-256. This is point-in-time candidate evidence, never an approval token; later use must recheck candidate/manifest hashes. On write, readback, validation or currentness failure, report actual retained partial artifact references and diagnostics without returning a success manifest/seal or performing unverified cleanup. Do not write originals, historical revisions or Journal, do not promote candidates, and do not invoke MCP.

### Deterministic Subject intent

Pure preparation for that one-target route **must** expose `subject_intent` and `subject_intent_sha256`. The intent is exactly one JSON object with `schema_version: 1`, `target`, `subject_profile`, `subject_profile_evidence`, `subject_patches`, `proposal`, `execution_metadata`, `predecessorArchive` and `noop`. `target` is CA-D-531's complete descriptor and binds the before bytes; profile evidence and ordered patches retain their existing closed representations. `proposal` contains exactly `frontmatter_digest`, `content_digest` and `sha256`: lowercase SHA-256 of the exact UTF-8 intended frontmatter, exact UTF-8 body and complete intended Carrier. Only declared Subject spans differ from the before Carrier; old Version/time remain for assessment.

`execution_metadata` is exactly `{version, updated_at}`. For a change, `version` is the integer `N+1` and `updated_at` is the literal `actual_effect_time`; for no-op, `version` is `N` and `updated_at` is the literal `preserve`. `predecessorArchive` is null for no-op; otherwise it contains exactly `atom_id`, `version`, `path`, `sha256` and `lifecycle`, binding the original ID, `N`, the existing role-local Delivery history path, exact before-byte hash and literal `archived`. It describes exact historical bytes classified by placement, not another current source or carried status/time edit.

`subject_intent_sha256` is lowercase SHA-256 of canonical UTF-8 JSON of this whole object, with keys sorted, no extra whitespace, unescaped Unicode and no non-finite values. It is outside the object and excludes separate illustrative preview bytes/time and future actual-effect receipts. Thus unchanged source/patch/profile/history/metadata-rule evidence yields the same intended hash independently of illustrative time. Unknown intent fields or a mismatched freshly derived hash fail.

The admitted result **must** retain the intended hash and actual `materialization = {version, updated_at, after_sha256}`, observed current/history descriptors and the existing shared result/effect/recording evidence. Changed materialization uses actual Project time and verified final Carrier hash; no-op retains old Version/time/hash and has no history effect. No other generated Carrier slot is admitted as an effect; local derived staging candidates are not authoritative effect slots. CA-R-866 and CA-O-030 govern the effect; CA-M-371 remains pure preparation and CA-D-585 binds assessment proposal pins.
