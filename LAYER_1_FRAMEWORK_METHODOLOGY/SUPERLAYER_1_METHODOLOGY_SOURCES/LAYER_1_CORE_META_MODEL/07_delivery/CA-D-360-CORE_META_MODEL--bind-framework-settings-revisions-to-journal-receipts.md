---
subjects:
  governs: "Framework Instance Settings/Revision Binding"
  depends_on:
    - "Artifact/Revision"
    - "Work Journal/Record"
version: 15
updated_at: "2026-10-18 07:31:21 +0400"
relations:
  child_of:
    - CA-D-359
atom_id: "CA-D-360"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Bind Framework Settings Revisions to Journal Receipts

## Scope

the current `caprmedio_framework_settings` Revision and SHA-256 Digest.

## Claim

the current caprmedio_framework_settings Revision **and** SHA-256 Digest **must** bind **to** its authoritative TOML Carrier through a canonical completed governed-change Work Journal receipt **or** an explicitly authorized canonical recovered-state Work Journal receipt registering its observed baseline; the receipt **must** match the selected Project, exact Carrier path, logical Artifact Revision, **and** Digest. absence, ambiguity, **or** mismatch **must** leave its currentness unknown.

## Details

- recovered baseline registration **must** use the existing `recovered` event for `governed_project_state`, with the exact positive-integer logical Revision in `result.version` **and** Carrier evidence in `recovery_evidence.carrier`: `path`, `sha256`, `observed_at`, **and** `observer_run_id`. no new Journal event **or** schema is required.
- `observed_at` **must** record the actual observation time; `observer_run_id` **must** identify a real observing Run **or** session supported by evidence. unresolved past Actor, mutation time, intent, **or** history **must** remain explicit uncertainty under CA-R-1644.
- the logical Revision **must** follow the existing Artifact lineage, including Carrier renames **or** movements; a changed path **must not** reset it **or** justify a guessed allocation.
- registration **must not** write the Settings Carrier, fabricate a past Settings change **or** author, **or** rewrite Journal history under CA-D-308. a Carrier changed since observation **must not** be presented as the registered current baseline; its historical observation remains intact.
- baseline registration establishes the observed binding only. under CA-R-1491 it proves neither Settings schema conformance nor correct performance **or** authorization of another operation.
