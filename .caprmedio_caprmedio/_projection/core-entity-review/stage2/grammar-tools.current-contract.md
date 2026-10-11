# Current Subject Tool contract — CA-P-2162

This derived contract supersedes the pre-selector CA-P-2062 contract. It does not rewrite captured review evidence. Exact current Core and Engine pins are in [selector-tools.current-contract.json](selector-tools.current-contract.json). CA-P-2163 implemented and independently verified the code alignment; Root's combined418-test run passed. This is not ordinary Subject migration or native admission.

## Latest Operator decision

"We don't need @ - it's just D atoms."

Compact Entity notation has only `/`, `.` and `:`. There is no fourth carrier/display operator. D atoms define carrier and storage rules. The existing negative rejection of `@` in a Subject does not give it a notation role. Do not remove `@<version>` from historical filenames: that is a separate D-governed carrier convention, not an Entity operator. Frozen candidates, receipts and archived versions remain historical evidence.

## Same-profile ordinary operations

- Profiles are `legacy` and `approved`. Omission means legacy; approved is explicit. Unknown or malformed supplied profiles fail.
- Legacy uses `/` for bearer qualification, `:` for allowed values, and literal dots. Approved uses `/` broader-to-narrower, `.` bearer-to-dependent and `:` Property-to-allowed-value.
- Both reject `@` in Subject syntax. Legacy rejects selectors. Approved accepts only the initial, case-sensitive `atom(...)` forms below. Escaping, conjunctions, wildcards and inferred profile detection remain unsupported.
- Search has an optional `subject_profile` input (`--subject-profile` at the CLI). Prefix matching uses the selected profile's boundaries; exact stays literal. Results are lexical matches, not semantic-conformance attestations.
- Subject-only preview has the closed root envelope `{atoms, subject_profile?}`. Each item remains `{selector, expected, subject_patches}`; other root/item keys fail. Select one profile for source and result syntax checks. Full-carrier validation, pins, no-follow protection, byte preservation and no-op/apply guards remain required.
- Both results add `subject_profile` (the selected name) and `subject_profile_evidence` with exactly `grammar_pins` and `native_admission: "not_performed"`. Each grammar pin contains `atom_id`, `version`, `path` and `sha256`. Preview seals these fields in its digest. They are reviewed grammar evidence, not a native endpoint registry or an attestation about source semantic conformance.
- Legacy evidence cites the five exact historical definitions adopted before CA-P-2059; approved evidence cites the five current definitions. Generic Atom operations do not hardcode a target Project's Core root.
- The shared syntax module proves syntax/direction only. Approved graph slash produces neither a native IS_BORNE_BY nor NARROWER_THAN edge. Dot gives Dependent IS_BORNE_BY Bearer; colon gives AllowedValue IS_ALLOWED_VALUE_OF Property.
- Graph selection is internal, keyword-only, legacy by default. Existing public generator entry points are unchanged. A current approved Core provider checks current source pins; do not silently switch native admission consumers or frozen Step 1 consumers.
- Repairs, cross-profile conversion and live source migration are separate approved ad-hoc work. No reusable migration framework, unguarded writer or new apply path.

## Approved selectors

- `Atom` is the existing Entity type and ordinary Term. `atom(...)` is syntax, not another Term, alias or Entity kind. Do not case-fold or interchange them.
- Only `atom(atom_id="CA-O-135")`, `atom(content_role="Plan")` and `atom(content_role="Plan",type="Plan")` forms are accepted. Values are non-empty double-quoted exact literals. The key order is fixed; `atom_id` is exclusive, and `type` requires preceding `content_role`.
- Presentation whitespace is accepted and preserved literally. No evaluation, expansion, nesting, positional arguments, unknown/duplicate keys or selector after a separator.
- A named selector refers to an Atom definition, not Execution. Role/type selection qualifies an Atom bearer pattern; syntax does not enumerate concrete Atom rows or require exactly one row.
- In `atom(content_role="Plan").Status`, Status belongs to the selected Atom. Plan remains that Atom's Content Role allowed value; it is neither Status's bearer nor its allowed value.
- Graph owner paths retain the complete selector literal. The referenced Entity-type Term is `Atom`; selector text is not a Term node. Native endpoint admission remains separate, and no selection relation is added.
- Literal lookup, sealed preview evidence, stale-source rejection and the existing standalone apply rejection remain unchanged. The patch item's repository-relative source locator is not this Subject selector syntax.

## Ownership and gates

CA-P-2162 aligns four Core grammar definitions and ten Engine Tool RMEDO definitions, preserving their exact predecessors, identity, Summary, Scope, Subjects and unrelated content. CA-R-1931, CA-D-038 and CA-D-041 remain unchanged. Root owns source adoption, Plans, actual Journal observations and Git. Independent verification precedes CA-P-2163 code implementation. Ordinary Subject migration and body alignment are not part of this grammar exception. Frozen packets, accepted mappings and captured snapshots retain their historical pins.
