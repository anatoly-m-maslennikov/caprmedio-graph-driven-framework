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
version: 8
updated_at: "2026-10-10 23:57:23 +0400"
relations: {"delivery_for":["CA-R-866"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Deliver ATOM_UPDATE Tool

## Scope

This Delivery carrier defines the public file-operation contract of the canonical `ATOM_UPDATE` wrapper under owner `TOOLS`. The `ATOM_UPDATE` folder is an artifact collection below `TOOLS`, not an independently registered Scope Unit. It retains the existing generic update input and sealed apply guard and adds one small read-only, Subject-only preview for already-correct Atom files. It does not define Core semantics, grammar adoption, migration decisions, source repair, history/Journal materialization, or a live MCP route.

## Claim

the `ATOM_UPDATE` Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/atom_update.py`; that Carrier realizes `CA-R-866` through the Action `CA-O-030`.

The delivered `ATOM_UPDATE` wrapper **must** accept a Subject-only preview item with an exact repository-relative source-path `selector`, an `expected` object containing exactly `atom_id`, `version`, and `sha256`, and an explicit `subject_patches` list. Each patch has `field` equal to `governs` or `depends_on`, `old`, and `new`; `depends_on` patches additionally have a zero-based integer `index`, while `governs` is scalar and has no list index. The old value must match the pinned current bytes exactly, and the new value is explicit: no target, relation move, grammar conversion, or migration mapping is inferred.

The Subject-only mode is exclusive. A request carrying `subject_patches` must not also carry complete `frontmatter` or `content` replacement fields. The selected source must be a complete, canonical, non-symlink Atom Carrier at the exact path, with the expected identity, Version, and full-file SHA-256. The preview validates the complete resulting Carrier and preserves path, filename, identity, Summary, body, unrelated frontmatter, and line endings; only the declared Subject spans plus required Version and `updated_at` spans may differ.

## Details

The local dry-run result **must** expose the exact patch set, before and after SHA-256 values, expected Version `N+1`, an illustrative `updated_at` value, and a canonical `preview_sha256` over the complete deterministic preview. The illustrative time is not an execution receipt. Empty or unchanged patches are reported as a truthful no-op and do not create a revision. Invalid or nested Subject shapes, missing or repeated occurrences, stale identity/version/digest, collisions, overlapping spans, path escapes, symlink targets, and incomplete files stop before any write.

The existing generic updater remains available for its complete-carrier contract; this mode does not mix with it and does not weaken the standalone `--apply` guard. No MCP support is claimed or invoked. The preview performs no write, history/archive/Journal effect, migration-batch sealing, or source publication. Those effects, if later authorized, belong to a separate ad-hoc packet. CA-R-866 and CA-O-030 remain the governing Requirement and Action; CA-M-371 supplies the focused authoring method when that Method carrier is delivered.
