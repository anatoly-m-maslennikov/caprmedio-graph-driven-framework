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
version: 13
updated_at: "2026-10-10 23:57:17 +0400"
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

### Acceptance criteria

the exact selector returns one **and** **only** its Atom; the filtered request returns **every** **and** **only** its two matching Atoms **in** stable repository-relative path order; **every** output view **contains** **only** its requested fields; malformed candidates have separate diagnostics; excluded files never appear; repeated results are identical; **and** **every** recorded digest remains unchanged.

### Failure disposition

reject the realization **and** preserve the fixture, requests, unexpected membership **or** ordering, output-view evidence, diagnostics, **and** **any** detected mutation.

### Capability coverage

automated tests **must** prove that search returns deterministic singular **and** bulk results, respects subtree **and** lifecycle filters, excludes non-Atom Markdown, exposes **only** the requested output view, supports field-aware exact **and** delimiter-boundary prefix Subject lookup with source pins, rejects invalid input without repair, **and** leaves **all** repository bytes unchanged.
