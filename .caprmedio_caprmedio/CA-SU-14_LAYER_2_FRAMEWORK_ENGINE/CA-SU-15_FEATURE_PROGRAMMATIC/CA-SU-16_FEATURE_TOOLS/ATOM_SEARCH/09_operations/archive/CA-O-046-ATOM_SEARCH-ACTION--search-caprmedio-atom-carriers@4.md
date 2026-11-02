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
version: 4
updated_at: "2026-10-10 23:57:31 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Summary

Search CAPRMEDIO Atom carriers

## Operation

Search Atom Carriers **means** the reusable read-only Action that returns the complete matching set of Atom Carriers for **`=1`** declared search frontier **and** requested output view under CA-R-863. incomplete membership **or** missing attribution is **not** a successful result.

## Details

### Applicable conditions

an Operator **or** another Tool requests deterministic Atom discovery within a declared frontier.

### Steps

1. resolve the configured CAPRMEDIO control root, **`=1`** declared subtree boundary, requested output view, **and** supplied exact-selector, lifecycle, path, filename, frontmatter, **or** body-text filters.
2. reject an invalid root, selector, filter, lifecycle, **or** output-view request **before** traversing the frontier.
3. enumerate **only** Markdown candidates inside that frontier. classify Atom eligibility from current locations **and** filenames; exclude runtime state, Projections, **and** non-Atom files.
4. for a Subject lookup, require a valid flat `subjects` mapping with requested `field` equal to `governs`, `depends_on`, **or** `both`; `governs` has **`=1`** scalar occurrence, and `depends_on` has ordered scalar occurrences with zero-based indexes. reject an invalid, nested, duplicate-dependency, unreadable, or symlink Carrier as a separate diagnostic; do not repair it.
5. match each requested Subject value exactly, **or** by the request's explicit lexical prefix boundary. A prefix boundary only compares literal text followed by the current `/` or `:` delimiter; it does not infer an Entity, Term, relation, **or** pending Subject grammar meaning. apply the exact selector **and** **every** supplied filter conjunctively.
6. read **only** the filename, frontmatter, **and** body fields needed for the requested metadata-only, content-only, **or** combined view. return the empty, singular, **or** bulk result in stable repository-relative path order. every Subject occurrence record includes field, dependency index when applicable, value, relative path, Atom ID, Version, Status, owner Scope Unit, Updated At, **and** SHA-256 source pin.
7. perform no write, rename, move, lifecycle transition, repair, Subject replacement, **or** Projection rebuild.

### Outcome

the result identifies **every** **and** **only** matching Atom Carrier and requested Subject occurrence within the declared frontier. stop **without** mutation when the root or request grammar is invalid; distinguish invalid Carriers from valid non-matches and never infer a match from unreadable content. This Action is a read-only lookup; it does not claim MCP delivery or perform a migration.
