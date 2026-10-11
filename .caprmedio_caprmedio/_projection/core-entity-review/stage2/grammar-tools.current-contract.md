# Current Subject Tool contract — CA-P-2062

Recorded 2026-10-11 04:26:25 +0400. This derived contract supplements the completed CA-P-2061 review; it does not rewrite captured review evidence.

## Latest Operator decision

"We don't need @ - it's just D atoms."

Compact Entity notation has only `/`, `.` and `:`. There is no fourth carrier/display operator. D atoms define carrier and storage rules. The existing negative rejection of `@` in a Subject does not give it a notation role. Do not remove `@<version>` from historical filenames: that is a separate D-governed carrier convention, not an Entity operator. Frozen candidates, receipts and archived versions remain historical evidence.

## Same-profile ordinary operations

- Profiles are `legacy` and `approved`. Omission means legacy; approved is explicit. Unknown or malformed supplied profiles fail.
- Legacy uses `/` for bearer qualification, `:` for allowed values, and literal dots. Approved uses `/` broader-to-narrower, `.` bearer-to-dependent and `:` Property-to-allowed-value.
- Both reject `@` in Subject syntax. Do not introduce escaping, selectors, conjunctions or inferred profile detection.
- Search has an optional `subject_profile` input (`--subject-profile` at the CLI). Prefix matching uses the selected profile's boundaries; exact stays literal. Results are lexical matches, not semantic-conformance attestations.
- Subject-only preview has the closed root envelope `{atoms, subject_profile?}`. Each item remains `{selector, expected, subject_patches}`; other root/item keys fail. Select one profile for source and result syntax checks. Full-carrier validation, pins, no-follow protection, byte preservation and no-op/apply guards remain required.
- Both results add `subject_profile` (the selected name) and `subject_profile_evidence` with exactly `grammar_pins` and `native_admission: "not_performed"`. Each grammar pin contains `atom_id`, `version`, `path` and `sha256`. Preview seals these fields in its digest. They are reviewed grammar evidence, not a native endpoint registry or an attestation about source semantic conformance.
- Legacy evidence cites the five exact historical definitions adopted before CA-P-2059; approved evidence cites the five current definitions. Generic Atom operations do not hardcode a target Project's Core root.
- The shared syntax module proves syntax/direction only. Approved graph slash produces neither a native IS_BORNE_BY nor NARROWER_THAN edge. Dot gives Dependent IS_BORNE_BY Bearer; colon gives AllowedValue IS_ALLOWED_VALUE_OF Property.
- Graph selection is internal, keyword-only, legacy by default. Existing public generator entry points are unchanged. A current approved Core provider checks current source pins; do not silently switch native admission consumers or frozen Step 1 consumers.
- Repairs, cross-profile conversion and live source migration are separate approved ad-hoc work. No reusable migration framework, unguarded writer or new apply path.

## Ownership and gates

CA-P-2063 owns R863/R866/M370/M371; CA-P-2064 owns E301/E304/D424/D425; CA-P-2065 owns O046/O030. Each author owns only those current Engine Tool sources and exact old-version archives. Preserve identity, Summary, Scope, Subjects and unrelated metadata; change Claim/Details, Version +1 and the actual configured Updated At only. CA-D-038/041 remain unchanged.

Root owns Plans, Journal and Git. Independent CA-P-2066 checks all ten effects and shared contract agreement, then creates fresh grammar-aware packet, acceptance and compiled contract. The frozen twelve-source packet and acceptance remain unchanged. Code implementation starts only after that gate.
