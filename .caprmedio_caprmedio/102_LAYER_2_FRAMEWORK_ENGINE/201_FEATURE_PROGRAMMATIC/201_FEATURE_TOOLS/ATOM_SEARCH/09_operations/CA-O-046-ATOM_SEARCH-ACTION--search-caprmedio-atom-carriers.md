---
atom_id: CA-O-046
content_role: Operations
type: Action
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Search Atom Carriers"
  depends_on:
    - "Action"
    - "Tool/ATOM_SEARCH"
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
version: 5
updated_at: "2026-10-11 04:32:58 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Summary

Search CAPRMEDIO Atom carriers

## Operation

Search Atom Carriers **means** the reusable read-only Action that returns the complete matching set of Atom Carriers for **`=1`** declared search frontier **and** requested output view under CA-R-863. A Subject lookup selects one ordinary Subject profile before lexical matching and returns its grammar evidence; it neither converts Profiles nor attests semantic conformance. incomplete membership **or** missing attribution is **not** a successful result.

## Details

### Applicable conditions

an Operator **or** another Tool requests deterministic Atom discovery within a declared frontier.

### Steps

1. resolve the configured CAPRMEDIO control root, **`=1`** declared subtree boundary, requested output view, **and** supplied exact-selector, lifecycle, path, filename, frontmatter, **or** body-text filters.
2. reject an invalid root, selector, filter, lifecycle, **or** output-view request **before** traversing the frontier.
3. enumerate **only** Markdown candidates inside that frontier. classify Atom eligibility from current locations **and** filenames; exclude runtime state, Projections, **and** non-Atom files.
4. for a Subject lookup, resolve optional `subject_profile` (`--subject-profile` at the CLI): omission selects `legacy`, `approved` is explicit, and an unknown or malformed supplied Profile fails. require a valid flat `subjects` mapping with requested `field` equal to `governs`, `depends_on`, **or** `both`; `governs` has **`=1`** scalar occurrence, and `depends_on` has ordered scalar occurrences with zero-based indexes. reject an invalid, nested, duplicate-dependency, unreadable, or symlink Carrier as a separate diagnostic; do not repair it.
5. validate each requested Subject value with the selected Profile and reject `@` in either Profile; that rejection does not create a carrier or display operator. D governs `@<version>` archive filenames as carrier storage, not as an Entity token. `legacy` uses `/` for bearer qualification, `:` for allowed values, and literal dots. `approved` uses `/` broader-to-narrower, `.` bearer-to-dependent, and `:` Property-to-allowed-value. Match exactly, **or** only at the selected Profile's lexical prefix boundaries: literal `/` and `:` for `legacy`, or literal `/`, `.`, and `:` for `approved`. Do not infer an Entity, Term, relation, semantic conformance, Profile conversion, or pending Subject grammar meaning. apply the exact selector **and** **every** supplied filter conjunctively.
6. read **only** the filename, frontmatter, **and** body fields needed for the requested metadata-only, content-only, **or** combined view. return the empty, singular, **or** bulk result in stable repository-relative path order. every Subject occurrence record includes field, dependency index when applicable, value, relative path, Atom ID, Version, Status, owner Scope Unit, Updated At, **and** SHA-256 source pin. every Subject lookup result also echoes `subject_profile` and `subject_profile_evidence` with exactly `grammar_pins` for `legacy`'s five exact historical definitions adopted before CA-P-2059 or `approved`'s five current definitions, plus `native_admission: "not_performed"`; the evidence is grammar evidence, not a native endpoint registry or an attestation about source semantic conformance.
7. perform no write, rename, move, lifecycle transition, repair, Subject replacement, **or** Projection rebuild.

### Outcome

the result identifies **every** **and** **only** matching Atom Carrier and requested Subject occurrence within the declared frontier. stop **without** mutation when the root, selected Profile, or request grammar is invalid; distinguish invalid Carriers from valid non-matches and never infer a match from unreadable content. This Action is a read-only lookup; it does not claim MCP delivery, native endpoint admission, Profile migration, or a semantic-conformance result.
