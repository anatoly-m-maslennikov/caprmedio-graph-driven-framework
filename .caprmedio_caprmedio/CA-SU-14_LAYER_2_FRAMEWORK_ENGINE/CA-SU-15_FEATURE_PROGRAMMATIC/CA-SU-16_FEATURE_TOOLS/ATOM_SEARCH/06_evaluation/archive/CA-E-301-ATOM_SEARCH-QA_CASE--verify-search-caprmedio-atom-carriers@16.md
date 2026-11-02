---
atom_id: CA-E-301
content_role: Evaluation
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool/ATOM_SEARCH"
  depends_on:
    - "Atom"
    - "Artifact/Carrier"
    - "Scope Unit"
    - "Search Atom Carriers"
version: 16
updated_at: "2026-10-12 04:06:57 +0400"
relations: {"evaluation_for":["CA-R-863","CA-O-046"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Verify search caprmedio atom carriers

## Scope

apply **to** **any** realization of CA-O-046 **before** it is relied on for read-only Atom discovery.

## Claim

CA-O-046 returns **every** **and** **only** matching Atom carrier **in** a deterministic requested view **without** changing project truth.

## Details

### Test case

use one fixture with active, draft, archived, malformed, **and** non-Atom Markdown candidates across two Scope Units. within one selected subtree, run an exact Atom selector that yields one result **and** a second conjunction of lifecycle, Content-role, Tier, frontmatter, **and** body-text filters that yields two results; request **every** output view **and** repeat both requests **after** recording **every** fixture digest.

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
