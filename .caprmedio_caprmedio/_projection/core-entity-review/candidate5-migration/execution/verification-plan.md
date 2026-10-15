# Candidate #5 Subjects-only migration: independent readback plan

Scope: the approved batch changes only Subjects and revision metadata. Missing-R drafts remain empty. This plan adds no execution gate or source mutation.

## Reuse the existing checks

- `subject_batch.load_subject_batch` checks the closed packet, exact current target bytes, unique targets, and committed prestate.
- `subject_batch_frontier.subject_batch_frontier(packet)` derives the exact archive paths and declared effects.
- `atom_subject_patch.prepare_subject_intent` and `materialize_subject_intent` create the expected Subjects-only carrier by replacing YAML spans; the only other edited values are Version and Updated At.
- `subject_batch_drafts.require_reviewed_draft_candidate` checks a staged proposal against that exact candidate, disregarding only temporary draft ID/Status and actual effect time.
- `atom_subject_apply.subject_update_action` writes the exact old bytes to the archive, reads them back, publishes the candidate, and reads it back.
- `subject_batch_execution.execute_subject_batch` stops on the first non-applied/non-no-op result. Its persisted results are evidence of attempted effects, not a substitute for file readback.

## Minimal independent readback

Use the packet's Git checkpoint and each target path to read the original bytes. Do not use another rebuilt model or fresh inventory as the before state.

For each applied target:

1. `SHA256(before_raw) == target.digest`.
2. Read the archive path from the existing frontier helper, or the native result's `history.prior_revision.path`; require `archive_raw == before_raw`.
3. Read current bytes and require their digest equals native `observed.digest`.
4. Parse before/current YAML with the existing parser. Apply the packet's ordered `subject_patches` to the before Subjects. Require current Subjects equal that result, including only explicitly requested dependency-set deduplication.
5. Require current Version = before Version + 1, and current Updated At = native result Updated At.
6. Remove only `subjects`, `version`, and `updated_at` from parsed before/current metadata and require exact equality. Thus Atom ID, Status, Content Role, Type, ownership, Relations, and every other header field remain unchanged.
7. Split with `atom_subject_patch._raw_frontmatter` and require the entire body strings equal, preserving Summary, Scope, Claim/Substance and Details exactly.
8. For byte-level independence, mask only the YAML value spans of those three permitted top-level keys and compare the remaining frontmatter text. This additionally catches unrelated formatting/comment edits.
9. If staged, require only this packet's pinned edit-draft path was consumed. No absent-to-present or removal effect outside the declared frontier is allowed.

For no-op targets: current bytes, Version, Updated At stay identical; no predecessor archive is created. A successfully consumed edit draft is a distinct expected effect.

Archive formula already used by the native helper:

```text
nearest content-role folder / archive / <original filename stem>@<before Version><original extension>
```

Preserve archived bytes including their old Status and timestamp. Archive placement represents history; rewriting its Status would violate exact preservation.

## Missing-R drafts

Current verified baseline: 54 manifest-listed drafts; no `atom_id`; `status: Draft`; Scope, Claim and Details empty.

- Manifest SHA-256: `db65c02e09a3d0214b037045d2e3b40812bd2bc50b423c8d023fe81adef33dba`
- Ordered draft-record digest: `9d94d237b3836e5cc9bc94d1f6812fe550f97bd0336fa3e82c8e1f1149d69106`

The latter is SHA-256 of UTF-8 compact JSON with sorted object keys of manifest-order records `{"path": repository_relative_path, "sha256": raw_file_sha256}`.

After execution, repeat that calculation and the structural checks. These are model-definition placeholders, not the separately staged versioned edit drafts; never promote or remove them as part of Subject migration.

## Existing focused test evidence

`tests/test_subject_batch_drafts.py::test_promotion_restores_canonical_identity_and_done_status_with_exact_history` already checks metadata equality except the intended patch/version/time, unchanged body, exact archive bytes, preserved file mode, draft removal, and unique current identity.

The adjacent changed-draft/repinned-body tests reject unauthorized body changes before publication. No full-suite run is needed merely to read back this data-only migration.

## Stop conditions

Any mismatched bytes, unexpected field/body change, missing archive, unknown/partial result, or changed missing-R draft stops further work. Report the exact target and persisted result; do not silently replay or reinterpret the operation.

