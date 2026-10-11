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
version: 2
updated_at: "2026-10-11 04:28:11 +0400"
relations:
  relates_to: [CA-R-866, CA-O-030, CA-E-304, CA-D-425]
---
# Summary

Preview exact Subject patches for valid Atom carriers

## Scope

The Subject-only preview method for ATOM_UPDATE.

## Claim

ATOM_UPDATE **must** prepare a Subject-only preview from explicit, source-pinned
replacements under one selected `subject_profile`: omission selects `legacy`,
`approved` is explicit, and unknown or malformed supplied profiles fail. It
validates each exact selector and its Atom ID, Version and SHA-256 before
locating the stated direct Subject occurrence. It validates source and result
syntax under that same profile, replaces only the stated scalar or
dependency-list item, validates the complete resulting carrier, and returns the
exact preview without writing a carrier.

## Details

Accept only the closed root `{atoms, subject_profile?}` and an item exactly
`{selector, expected, subject_patches}`, with
`expected = {atom_id, version, sha256}`; reject unknown root or item keys.
Separate `subject_patches` from complete-frontmatter or body replacement. Reject
duplicate selected files. For each patch, require `field`, `old`, and `new`;
require the exact dependency `index` for `depends_on`. Legacy uses `/` bearer
qualification and `:` allowed values with literal dots. Approved uses `/`
broader-to-narrower, `.` bearer-to-dependent, and `:`
Property-to-allowed-value. Both reject `@`, escaping, selectors, conjunctions,
and inferred profile detection in Subject syntax. Reject invalid carrier shape,
missing or ambiguous old values, stale pins, path escapes, symlink targets and
duplicate resulting dependencies. Preserve all unrelated bytes and line endings.

Classify an actual Subject value change as a semantic revision with Version
`N + 1`; a no-op creates no revision. The preview result returns the selected
`subject_profile` and `subject_profile_evidence` containing exactly
`grammar_pins` and `native_admission: "not_performed"`; every grammar pin
contains `atom_id`, `version`, `path`, and `sha256`, and the preview seals those
fields in its digest. Legacy cites the five exact historical definitions and
approved cites the five current definitions. The local operation is preview-only.
Existing sealed generic update admission and its standalone-apply guard remain
unchanged. Do not repair legacy carriers, select a migration, infer relations,
create Journal/history effects, or add an apply path from the preview. The
historical `@<version>` archive filename convention is Delivery-owned and does
not give `@` a Subject role.
