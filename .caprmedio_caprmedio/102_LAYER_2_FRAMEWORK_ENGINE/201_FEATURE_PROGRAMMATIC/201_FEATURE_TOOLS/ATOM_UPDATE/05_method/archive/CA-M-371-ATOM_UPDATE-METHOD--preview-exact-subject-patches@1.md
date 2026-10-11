---
atom_id: CA-M-371
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_UPDATE"
  depends_on: [Atom, Subject, Artifact/Carrier, Atom/Revision]
version: 1
updated_at: "2026-10-10 23:53:36 +0400"
relations:
  relates_to: [CA-R-866, CA-O-030, CA-E-304, CA-D-425]
---
# Summary

Preview exact Subject patches for valid Atom carriers

## Scope

The Subject-only preview method for ATOM_UPDATE.

## Claim

ATOM_UPDATE **must** prepare a Subject-only preview from explicit, source-pinned
replacements. It validates each exact selector and its Atom ID, Version and
SHA-256 before locating the stated direct Subject occurrence. It replaces only
the stated scalar or dependency-list item, validates the complete resulting
carrier, and returns the exact preview without writing a carrier.

## Details

Accept `subject_patches` only in an existing `atoms` item with its exact
`selector` and `expected = {atom_id, version, sha256}`, and separate it from
complete-frontmatter or body replacement. Reject duplicate selected files. For
each patch, require `field`, `old`, and `new`; require the exact dependency
`index` for `depends_on`. Reject invalid carrier shape, missing or ambiguous old
values, stale pins, path escapes, symlink targets and duplicate resulting
dependencies. Preserve all unrelated bytes and line endings.

Classify an actual Subject value change as a semantic revision with Version
`N + 1`; a no-op creates no revision. The local operation is preview-only.
Existing sealed generic update admission and its standalone-apply guard remain
unchanged. Do not repair legacy carriers, select a migration, infer relations,
or create Journal/history effects from the preview.
