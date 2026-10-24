---
atom_id: CA-E-301
content_role: Evaluation
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Tool//ATOM_SEARCH
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Scope Unit
version: 26
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-R-863
  - CA-O-046
  - CA-O-201
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
tier: 4
type: Eval Case
---
# Summary

Verify search caprmedio atom carriers

## Scope

This primitive uses CA-D-625's coherent logical connector interface. The bound caller context supplies the requested scope, source view, permission and applicable validation authority; the connector checks them mechanically. It does not choose Atom identity, Version changes, lifecycle, defaults or a configuration schema.

apply **to** **any** realization of CA-O-046 **before** it is relied on for read-only Atom discovery.

## Claim

CA-O-046 returns every and only matching logical Atom descriptor in the requested scope, without invoking Read or Modify or changing project truth.

## Details

### Direct registered Subject lookup acceptance

Independently verify the exact bounded direct request/result in CA-D-424 through the production registered MCP transport, with the actual current Delivery/Action binding and source-pin checks enabled. Discovery exposes ATOM_SEARCH as atom_search with non-null closed input/output schemas. A direct request supplies every required logical criterion without Session, authorization/context reference, root or path; unknown fields and broader unsupported Type/target Scope/projection filters fail before traversal. This subset does not establish conformance of the broader generic Find cases above.

Cover governs, depends_on and both with exact/prefix/suffix/contains; include literal fragments, case distinctions, profile delimiter boundaries, body-only false positives and complete empty/singular/multiple results. Compare independently authored expected field/value matches and exact Atom ID, Version and full-byte SHA-256 evidence. Preserve separate fields and historical Versions without public dependency indexes or physical selectors.

Cover valid selected R/M/D carriers with absent Type; excluded malformed C/A; selected malformed/unreadable data; symlinks and owner/path disagreement; competing selected current IDs across owners and excluded-role headers. Include both an unrelated malformed atom_id YAML/header outside selected identities and its possible-selected-ID counterpart: the former does not trigger full schema admission, the latter refuses ambiguous identity. Read-budget or currentness failure remains refusal. Change source bytes, source membership, settings/structure, grammar or applicable definition pins during observation and require refusal, never a partial complete result.

Record before/after bytes and artifact membership, including scratch and Journal locations. A real registered MCP lookup without Session creates no Session, Run, Journal or staging artifact and invokes no Read/Modify. Retain enclosing-Workflow Tool-call recording responsibility when applicable. Fixture-only direct Python calls or mocked freshness do not prove registered or connected-MCP acceptance. Source authoring alone records no observed pass.

### Logical Find contract

Required future cases use logical Atom filters rather than a mandatory file path. Find returns matches with their IDs, Versions and source-state evidence; reading the complete Atom is a separate request. Verify that one match, several matches and no match do not invoke Read or Modify. Current file views are adapter details, not the logical Find result contract.

Test Subject criteria for governs, depends_on and both with exact, prefix, suffix and contains modes, combined with owning/target Scope Unit, Content Role and lifecycle filters. Exact means literal equality; prefix uses the selected profile's delimiter boundary; suffix and contains use the explicitly requested literal text. Include a body-only occurrence, lexical near-miss, malformed source, empty result and invalid mode. Compare an independent expected match ledger and source pins. This revision specifies required checks and records no observed pass.

### Test case

use one fixture with active, draft, archived, malformed, **and** non-Atom Markdown candidates across two Scope Units. within one selected subtree, run an exact Atom selector that yields one result **and** a second conjunction of lifecycle, Content-role, Tier, frontmatter, **and** body-text filters that yields two results; request **every** output view **and** repeat both requests **after** recording **every** fixture digest.

### Individual schema-invalid scan case

Include valid selected Atoms on both sides of one selected Atom with an invalid
schema. The realization may continue the bounded scan only when the invalid Atom is
isolated and the source frontier and safety checks remain usable: valid matches are
retained, the invalid Atom is omitted, a technical warning identifies its
repository-relative path and reason, and the result is `complete: false`. The
warning is emitted through the configured diagnostic logging path and does not
create or rewrite a business Journal record. I/O, security, duplicate-identity,
stale, ambiguous, or incomplete-frontier conditions still refuse the result rather
than producing partial complete coverage. Record fixture bytes and Journal bytes
before and after; no source repair or mutation is accepted.

### Additional selection cases

include a valid request matching no Atom, an invalid root, an unsupported filter, an invalid lifecycle selector, an invalid output view **and** an unreadable candidate. a valid non-match returns an empty result, **not** an error **or** a widened selection. reject invalid requests explicitly **before** traversal; an unreadable candidate produces a separate diagnostic **and** **must not** be silently accepted as a match **or** ordinary non-match. repeat applicable requests **to** check deterministic ordering **and** compare **every** fixture digest **to** prove no mutation.

### Subject lookup cases

Build a separate fixture and expected occurrence ledger without using the search producer or its graph builder. Every selected valid file has complete current Atom frontmatter and flat `subjects.governs` and `subjects.depends_on` values. Include a dependency-only match, a governs-only match, the same value in both fields, a malformed or nested Subjects value, and a body-only occurrence of each search value.

For `field=governs`, `field=depends_on`, and `field=both`, prove direction: a governs request never returns a dependency-only occurrence and a depends_on request never returns a governs-only occurrence. For `match=exact`, distinguish `Artifact/Atom` from other values. For `match=prefix`, test delimiter-boundary descendants using both `/` and `:` (for example, `Artifact/Atom/Status` and `Artifact:Atom:Status`) while excluding `Artifact/Atomology` and `Artifact:Atomology`; treat these as lexical lookup boundaries only, not as adoption of a pending grammar. `field=both` reports each matching field/list index as its own occurrence rather than collapsing distinct fields.

Run the same lookup with conjunctive `--under`, lifecycle, content-role, and owner filters. A value found only in Markdown body text is not a Subject match. Each occurrence records Atom ID, Version, Status, owner, current Scope Unit, repository-relative path, SHA-256, Updated At, field, list index, and exact value; source pins cover the complete carrier bytes and results have stable ordering.

Reject missing or unsupported field, value, match, root, lifecycle, `--under`, role, or owner inputs before traversal. Do not repair or write invalid files. A malformed or unreadable selected file produces a diagnostic. Repeat valid requests against an independently checked ledger, including duplicate list positions and all source pins, and prove every fixture byte remains unchanged.

Include valid Plan Done and Backlog originals in their admitted status folders. Omitted lifecycle keeps the Active default and excludes these originals; explicit `--lifecycle all` returns their expected Subject occurrences with exact carried Status and Atom ID/Version/SHA-256 pins in stable order. Compare the independently authored occurrence ledger and every fixture byte before and after both requests. Lookup membership is not Subject-preview eligibility and performs no activation or lifecycle transition.

### Subject-profile cases

Exercise omission and explicit `legacy`, and explicit `approved`; an unknown or malformed supplied profile fails before traversal. Legacy treats `.` as literal, uses only `/` and `:` as prefix boundaries, and rejects every `atom(...)` selector. Approved uses `/`, `.`, and `:` as boundaries and accepts only `Atom.Status`, `atom(content_role="Plan").Status`, `atom(content_role="Plan",type="Plan").Status`, and `atom(atom_id="CA-O-135").Status` as independently authored literal syntax. Prove exact case preservation and no Atom/atom normalization; reject `@`, type-only, mixed `atom_id`/`content_role`, duplicate or unknown keys, unquoted/escaped/wildcard/evaluated/aliased values, and selectors after a separator.

Use mixed approved `/`, `.`, and `:` paths and legacy dotted names to prove that a request selects only the boundaries of its selected profile. Exclude lexical near-misses such as `Artifact/Atomology`. Results label the selected `subject_profile` and carry `subject_profile_evidence` with exactly `grammar_pins` and `native_admission: not_performed`; every grammar pin contains `atom_id`, `version`, `path`, and `sha256`. Assert that this evidence and the result are lexical syntax only: no selector-instance enumeration, target conformance, native edge, NARROWER_THAN relation, carrier/display notation, source migration, or grammar adoption is inferred.

### Acceptance criteria

the exact selector returns one **and** **only** its Atom; the filtered request returns **every** **and** **only** its two matching Atoms **in** stable repository-relative path order; **every** output view **contains** **only** its requested fields; malformed candidates have separate diagnostics; excluded files never appear; repeated results are identical; **and** **every** recorded digest remains unchanged.

### Failure disposition

reject the realization **and** preserve the fixture, requests, unexpected membership **or** ordering, output-view evidence, diagnostics, **and** **any** detected mutation.

### Capability coverage

automated tests **must** prove that search returns deterministic singular **and** bulk results, respects subtree **and** lifecycle filters, excludes non-Atom Markdown, exposes **only** the requested output view, supports field-aware exact **and** delimiter-boundary prefix Subject lookup with source pins, rejects invalid input without repair, **and** leaves **all** repository bytes unchanged.
