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
version: 3
updated_at: "2026-10-11 18:04:47 +0400"
relations:
  relates_to: [CA-R-863, CA-O-046, CA-E-301, CA-D-424]
---
# Summary

Match direct Subject fields in valid Atom carriers

## Scope

The field-aware lookup method for ATOM_SEARCH.

## Claim

ATOM_SEARCH **must** evaluate Subject lookup only after it has selected valid
Atom carriers under the requested subtree and lifecycle. It selects one
`subject_profile`: omitted means `legacy`, `approved` is explicit, and unknown
or malformed supplied profiles fail. It reads the parsed, direct
`subjects.governs` scalar and `subjects.depends_on` scalar list, then applies
the requested field, content-role, owner Scope Unit, and Subject match filters
conjunctively under that same profile.

## Details

Use literal equality for `exact`. For `prefix`, legacy compares the whole value or the value followed by `/` or `:` and treats dots literally; approved also recognizes `.` as a lexical boundary. Legacy rejects every `atom(...)` selector. Approved parses only the exact initial lowercase forms registered by CA-R-1321, preserving `Atom`/`atom` case distinction and rejecting every other selector construction, `@`, escaping, conjunctions, wildcards, evaluation, aliases, and inferred profile detection in a Subject. These are lexical syntax checks only: they do not enumerate selector instances, attest semantic conformance, or infer relation meaning. Emit one ordered occurrence for a matching `governs` value and one
ordered occurrence for each matching `depends_on` index. Attach the carrier's
exact identity and source pin to each occurrence.

Before ordinary matching, validate the request and the selected carrier shape.
Return invalid selected carriers as diagnostics, not as omitted non-matches.
Return the selected `subject_profile` and `subject_profile_evidence` containing
exactly `grammar_pins` and `native_admission: "not_performed"`; every grammar
pin contains `atom_id`, `version`, `path`, and `sha256`; legacy cites the five
exact historical definitions and approved cites the five current definitions.
Do not modify carriers, normalize Subjects, invoke migration helpers, or widen
the request. The historical `@<version>` archive filename convention is
Delivery-owned and does not give `@` a Subject role. This method does not define
a generic Subject grammar.
