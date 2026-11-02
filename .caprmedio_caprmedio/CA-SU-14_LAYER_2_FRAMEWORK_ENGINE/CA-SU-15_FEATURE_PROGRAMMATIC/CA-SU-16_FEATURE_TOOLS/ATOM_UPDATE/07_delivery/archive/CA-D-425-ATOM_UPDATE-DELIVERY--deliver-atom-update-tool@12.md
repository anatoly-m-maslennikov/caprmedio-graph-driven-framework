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
version: 12
updated_at: "2026-10-12 04:20:25 +0400"
relations: {"delivery_for":["CA-R-866"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Deliver ATOM_UPDATE Tool

## Scope

This Delivery carrier defines the public file-operation contract of the canonical `ATOM_UPDATE` wrapper under owner `TOOLS`. The `ATOM_UPDATE` folder is an artifact collection below `TOOLS`, not an independently registered Scope Unit. It retains the existing generic update input and sealed apply guard and adds one small read-only, Subject-only preview for already-correct Atom files. It does not define Core semantics, grammar adoption, migration decisions, source repair, or a new MCP route. CA-D-531 binds its separately admitted one-target Subject effect to the existing MCP update action.

## Claim

the `ATOM_UPDATE` Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/atom_update.py`; that Carrier realizes `CA-R-866` through the Action `CA-O-030`.

The delivered `ATOM_UPDATE` wrapper **must** accept only the closed Subject-only preview envelope `{atoms, subject_profile?}`. Omission means `legacy`; `approved` is explicit; an unknown or malformed supplied profile fails. Each atom item is exactly an exact repository-relative source-path `selector`, an `expected` object containing exactly `atom_id`, `version`, and `sha256`, and an explicit `subject_patches` list. Each patch has `field` equal to `governs` or `depends_on`, `old`, and `new`; `depends_on` patches additionally have a zero-based integer `index`, while `governs` is scalar and has no list index. The selected profile validates both the pinned source and the proposed result. The old value must match the pinned current bytes exactly, and the new value is explicit: no target, relation move, profile conversion, grammar conversion, or migration mapping is inferred.

Legacy uses `/` as bearer qualification, `:` as Property-to-allowed-value, and literal dots, and rejects every `atom(...)` selector. Approved uses `/` as broader-to-narrower, `.` as bearer-to-dependent, and `:` as Property-to-allowed-value, and accepts only the exact initial lowercase selector forms registered by CA-R-1321; `Atom` and `atom` remain distinct. Both profiles reject `@`, and approved rejects every other selector construction, escaping, conjunction, wildcard, evaluation, and alias; it is neither a fourth operator nor carrier/display notation. The result includes the selected `subject_profile` and `subject_profile_evidence` containing exactly five reviewed grammar pins and `native_admission: not_performed`, sealed in `preview_sha256`. This is lexical syntax/direction checking only: it does not enumerate selector instances, establish target conformance, or admit a native endpoint.

The Subject-only mode is exclusive. A request carrying `subject_patches` must not also carry complete `frontmatter` or `content` replacement fields. The selected source must be a complete, canonical, non-symlink Atom Carrier at the exact path, with the expected identity, Version, and full-file SHA-256. The preview validates the complete resulting Carrier and preserves path, filename, identity, Summary, body, unrelated frontmatter, and line endings; only the declared Subject spans plus required Version and `updated_at` spans may differ.

Subject-only preview **must** select a complete original Atom Carrier with a stable Atom ID, excluding Draft and archived carriers by both carried Status and placement. Both the pinned source and proposed result **must** pass existing complete-carrier validation, including the applicable Content Role/Type Status model and correct Carrier placement. Preserve the carried Status byte-for-byte; do not activate the source or perform a lifecycle transition. Missing, ambiguous, unsupported, or stale validation authority **must** fail closed.

## Details

The local dry-run result **must** expose the exact patch set, before and after SHA-256 values, expected Version `N+1`, an illustrative `updated_at` value, and a canonical `preview_sha256` over the complete deterministic preview. The illustrative time is not an execution receipt. Empty or unchanged patches are reported as a truthful no-op and do not create a revision. Invalid or nested Subject shapes, missing or repeated occurrences, stale identity/version/digest, invalid profile syntax, collisions, overlapping spans, path escapes, symlink targets, and incomplete files stop before any write.

The existing generic updater remains available for its complete-carrier contract; Subject-only input does not mix with it and does not weaken the standalone `--apply` guard. The local preview invokes no MCP and performs no Carrier, history or Journal write. A separately authorized one-target Subject effect uses only the existing MCP `update_atom` route under CA-D-531 and CA-O-030, not this local wrapper or a new transport. This contract does not itself advertise an installed runtime capability, refresh an image/manifest, select a migration batch or grant source-effect approval.

### Deterministic Subject intent

Pure preparation for that one-target route **must** expose `subject_intent` and `subject_intent_sha256`. The intent is exactly one JSON object with `schema_version: 1`, `target`, `subject_profile`, `subject_profile_evidence`, `subject_patches`, `proposal`, `execution_metadata`, `predecessorArchive` and `noop`. `target` is CA-D-531's complete descriptor and binds the before bytes; profile evidence and ordered patches retain their existing closed representations. `proposal` contains exactly `frontmatter_digest`, `content_digest` and `sha256`: lowercase SHA-256 of the exact UTF-8 intended frontmatter, exact UTF-8 body and complete intended Carrier. Only declared Subject spans differ from the before Carrier; old Version/time remain for assessment.

`execution_metadata` is exactly `{version, updated_at}`. For a change, `version` is the integer `N+1` and `updated_at` is the literal `actual_effect_time`; for no-op, `version` is `N` and `updated_at` is the literal `preserve`. `predecessorArchive` is null for no-op; otherwise it contains exactly `atom_id`, `version`, `path`, `sha256` and `lifecycle`, binding the original ID, `N`, the existing role-local Delivery history path, exact before-byte hash and literal `archived`. It describes exact historical bytes classified by placement, not another current source or carried status/time edit.

`subject_intent_sha256` is lowercase SHA-256 of canonical UTF-8 JSON of this whole object, with keys sorted, no extra whitespace, unescaped Unicode and no non-finite values. It is outside the object and excludes separate illustrative preview bytes/time and future actual-effect receipts. Thus unchanged source/patch/profile/history/metadata-rule evidence yields the same intended hash independently of illustrative time. Unknown intent fields or a mismatched freshly derived hash fail.

The admitted result **must** retain the intended hash and actual `materialization = {version, updated_at, after_sha256}`, observed current/history descriptors and the existing shared result/effect/recording evidence. Changed materialization uses actual Project time and verified final Carrier hash; no-op retains old Version/time/hash and has no history effect. No other generated Carrier slot is admitted. CA-R-866 and CA-O-030 govern the effect; CA-M-371 remains pure preparation and CA-D-585 binds assessment proposal pins.
