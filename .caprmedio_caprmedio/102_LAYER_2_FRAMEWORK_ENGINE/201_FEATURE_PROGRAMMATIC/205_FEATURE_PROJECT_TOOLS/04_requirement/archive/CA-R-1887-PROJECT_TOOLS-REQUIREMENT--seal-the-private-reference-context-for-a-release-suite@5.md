---
atom_id: CA-R-1887
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-11 16:51:04 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Sealed suite reference context"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Project Structure, Operator, Workflow, Action, Source Carrier, Digest]
relations:
  relates_to: [CA-R-1879, CA-R-1886]
---
# Summary

Seal the private reference context for a Release suite

## Scope

The read-only Project control references required by the declared Release suite in addition to its sealed package rows.

## Claim

Before a Release suite executes, its Suite Owner **must** derive, byte-verify, copy read-only, and bind one closed canonical reference context. The local context contains only the internally generated release-only execution snapshot declared by CA-D-572, Operator registry, Project settings, Project Structure, current CA-D-572 and the exact current Workflow, Step, Action and RMED source pins derived for that captured release, and the two Unit-deadline settings carriers declared by CA-D-580. Unrelated Prompt bindings, fixed selected-source refresh pins and the legacy multi-route selected manifest are not Local release prerequisites. It is private Suite-owner state, never a D566 candidate-inventory member, public request field, MCP route, Workflow, Run, Journal carrier, runtime state, secret, or arbitrary caller file.

## Details

Each context row has exactly `source_path`, lowercase SHA-256 `sha256`, and regular-file `mode`. Every path is Project-relative and allowlisted by the closed construction. Filesystem inputs are regular, non-symlinked through every ancestor, and descriptor-captured before the read-only workspace is mounted. The virtual release snapshot is generated internally from captured bindings and materialized only in the private reader/workspace, never written as a Project control carrier. The closure is rejected if a protected root, captured release definition pin, snapshot byte, digest, mode, or cardinality differs from its admitted evidence.

The Suite Owner also binds the existing trusted internal candidate manifest SHA-256, compiled-candidate root, frozen selected N identity, and N image-context identity to this context. These are derived from existing trusted handoffs and actual selected-N evidence, not accepted as public envelope fields. Immediately before execution and after execution the Suite Owner reopens and verifies the same retained reference closure and context digest, with current checks for protected settings and selected-N state. Later authoring revisions do not replace the captured release definitions or payload. Any absence, mutation, symlink, unreadable byte, changed trusted binding, or post-run mismatch is non-passing and authorizes no candidate staging, runtime installation, Skill publication, selector change, image retirement, or source mutation.

Identical shared release pins are represented once; conflicting pins are rejected. Native Engine source inventory and its gates remain bound separately by the candidate manifest, and the generated execution snapshot binds the actual selected Project root's captured `102_FRAMEWORK_ENGINE` implementation tree. This context does not include arbitrary Project folders or obsolete Plan carriers merely because a historical test mentioned them.

The closure also contains exactly these two source carriers for the private Unit execution budget: the canonical default at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml` and the Framework Instance settings at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml`. They remain ordinary `reference_rows`, deduplicated when already admitted, with no new context field. The Suite Owner resolves `[release_suite].unit_timeout_seconds` from the instance table when present, otherwise from the canonical default; a missing canonical carrier, malformed value, stale byte, mode change, or non-finite, non-positive, boolean, or over-`7200` value is non-passing.
