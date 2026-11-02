---
atom_id: CA-M-370
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_SEARCH"
  depends_on: [Atom, Subject, Artifact/Carrier, Scope Unit]
version: 1
updated_at: "2026-10-10 23:53:36 +0400"
relations:
  relates_to: [CA-R-863, CA-O-046, CA-E-301, CA-D-424]
---
# Summary

Match direct Subject fields in valid Atom carriers

## Scope

The field-aware lookup method for ATOM_SEARCH.

## Claim

ATOM_SEARCH **must** evaluate Subject lookup only after it has selected valid
Atom carriers under the requested subtree and lifecycle. It reads the parsed,
direct `subjects.governs` scalar and `subjects.depends_on` scalar list, then
applies the requested field, content-role, owner Scope Unit, and Subject match
filters conjunctively.

## Details

Use literal equality for `exact`. For `prefix`, compare the whole value or the
value followed by `/` or `:`. Treat those characters only as current lexical
boundaries; do not infer relation meaning. Emit one ordered occurrence for a
matching `governs` value and one ordered occurrence for each matching
`depends_on` index. Attach the carrier's exact identity and source pin to each
occurrence.

Before ordinary matching, validate the request and the selected carrier shape.
Return invalid selected carriers as diagnostics, not as omitted non-matches.
Do not modify carriers, normalize Subjects, invoke migration helpers, or widen
the request. This method does not define a generic Subject grammar.
