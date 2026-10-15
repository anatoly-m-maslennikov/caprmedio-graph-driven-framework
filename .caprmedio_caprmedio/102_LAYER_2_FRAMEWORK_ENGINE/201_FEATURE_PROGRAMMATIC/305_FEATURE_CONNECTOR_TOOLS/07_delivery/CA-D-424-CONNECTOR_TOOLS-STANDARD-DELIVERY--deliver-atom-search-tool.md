---
atom_id: CA-D-424
content_role: Delivery
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: delivery
subjects:
  governs: "Tool/ATOM_SEARCH/Carrier"
  depends_on:
    - "Tool/ATOM_SEARCH"
version: 14
updated_at: "2026-10-14 10:04:27 +0400"
relations: {"delivery_for":["CA-R-863"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Deliver ATOM_SEARCH Tool

## Scope

This primitive uses CA-D-625's coherent logical connector interface. The bound caller context supplies the requested scope, source view, permission and applicable validation authority; the connector checks them mechanically. It does not choose Atom identity, Version changes, lifecycle, defaults or a configuration schema.

This Delivery carrier records `CONNECTOR_TOOLS` ownership of the rebuilt flat RMEDO contracts and binds the canonical `ATOM_SEARCH` wrapper. Its rebuilt source authority uses the FEATURE's role folders, not an `ATOM_SEARCH` child folder. The existing executable collection remains at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/`, explicitly bound to `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/atom_search.py`; it is not an independently registered Scope Unit. The new FEATURE Delivery root is future/unmaterialized and does not relocate that collection. It binds the current file adapter and the required logical Find contract; future logical behavior does not establish current implementation readiness. It does not define Core semantics, grammar adoption, migration decisions, source repair, graph publication, or completed live MCP acceptance.

## Claim

the `ATOM_SEARCH` Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/atom_search.py`; that Carrier realizes `CA-R-863` through the Action `CA-O-046`.

The delivered `ATOM_SEARCH` wrapper **must** support the existing `--under PATH` and `--lifecycle VALUE` filters and the following Subject lookup options:

- one `--subject VALUE` criterion per request;
- `--subject-field governs|depends_on|both` to select the flat Subject field;
- `--subject-match exact|prefix` for literal equality or delimiter-aware lexical prefix matching;
- optional `--subject-profile legacy|approved`, where omission means `legacy` and an unknown or malformed supplied profile fails;
- repeatable `--content-role ROLE` values as an OR set within the valid-file filter, and `--scope-unit OWNER` as a conjunctive owner filter.

Subject lookup defaults to Active. Explicit `--lifecycle all` can also return valid non-Active originals, including correctly placed Done or Backlog carriers, with their carried Status and exact source pins preserved. Lookup membership does not grant Subject-preview eligibility or cause a lifecycle transition.

Legacy uses `/` as bearer qualification, `:` as Property-to-allowed-value, and literal dots, and rejects every `atom(...)` selector. Approved uses `/` as broader-to-narrower, `.` as bearer-to-dependent, and `:` as Property-to-allowed-value, and accepts only the exact initial lowercase selector forms registered by CA-R-1321; `Atom` and `atom` remain distinct. Exact matching remains literal; prefix matching uses only the selected profile's declared boundaries. Both profiles reject `@`, and approved rejects every other selector construction, escaping, conjunction, wildcard, evaluation, and alias. It is neither a fourth operator nor carrier/display notation.

Each result **must** identify the source pin and exact occurrence: `atom_id`, `version`, `status`, `owner`, `relative_path`, `sha256`, `updated_at`, `field`, `index`, and `value`. `index` is the list index for `depends_on` and is null for the scalar `governs` field. Results are deterministic and path/field/index ordered. The result also carries the selected `subject_profile` and `subject_profile_evidence` containing exactly the five reviewed grammar pins and `native_admission: not_performed`. Malformed, unreadable, duplicate, or rejected selected files appear in a separate `diagnostics` collection; a valid empty match is returned as an empty result and is not a diagnostic. The lookup is lexical only: it never infers target conformance, ontology relations, a native edge, grammar adoption, or source migration.

## Details

### Required logical Find serialization

The query connector contract under CA-D-625 carries the selected logical kind, scope filters and a Subject criterion with field `governs`, `depends_on` or `both`, exact requested value and match mode `exact`, `prefix`, `suffix` or `contains`. It returns matching logical descriptors with IDs, Versions, exact occurrence values and source-state evidence, not complete Atom content. Read and Modify remain separate calls. The direct Subject subset below requires suffix/contains support; this does not assert that the historical CLI already implements those modes. Unknown fields or modes fail rather than widening a request.


The request resolves the configured Project control root and an optional declared subtree before traversal. Existing path, filename, frontmatter, content, exact-selector, output-view, and lifecycle behavior remains available. Subject lookup reads only valid current Atom files with a canonical flat `subjects` block; invalid source paths, symlink targets, projections, malformed carriers, duplicate fields/values, and owner/path disagreements are rejected or diagnosed without widening selection. Prefix matching ends only at a declared Subject delimiter, so a value such as `Artifact/Atom` does not match `Artifact/Atomology`.

The output carries one source pin per occurrence and no inferred target or native graph edge. The local CLI remains mutation-free: it performs no write, rename, repair, migration, Projection rebuild or history/Journal effect. The direct MCP delivery below is a required realization, not a claim of completed registration or live acceptance. CA-R-863 and CA-O-046 remain the governing Requirement and Action; CA-M-370 supplies the focused authoring method when that Method carrier is delivered.

### Direct read-only Subject MCP delivery

The canonical provider must declare this existing Tool binding and expose strict closed request/result models through the descriptor-driven MCP registry. Root is bound by the registry, never supplied by a caller. Descriptor hints do not replace canonical source validation.

```toml
[tool_binding]
name = "ATOM_SEARCH"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_SEARCH/atom_search.py"
action_ids = ["CA-O-046"]
mcp_name = "atom_search"
```

The public `SubjectLookupRequest` requires exactly `subject`, `subject_field`, `subject_match`, `subject_profile`, `scope_unit`, `content_roles` and `lifecycle`, with optional `atom_ids`. Required fields have no defaults. All models reject unknown fields and coercion. `subject` is nonempty text; fields are governs/depends_on/both, modes exact/prefix/suffix/contains and profiles legacy/approved. Exact/prefix criteria are valid complete expressions under the selected profile; suffix/contains criteria may be nonempty literal fragments. Complete selected source Subjects remain profile-validated.

`scope_unit` is one registered owning Scope Unit name, not a new stable-ID or physical-path scheme. `content_roles` is an explicit nonempty unique array from Concern/Analysis/Plan/Requirement/Method/Evaluation/Delivery/Operations. `lifecycle` explicitly selects active/draft/archived/done/resolved/canceled/all using the existing private lookup inclusion rules; all intentionally includes the wider lifecycle set rather than silently choosing current-only. Optional `atom_ids` contains unique complete logical Atom IDs; omission or an empty array imposes no extra ID restriction. No caller root, under, path, filename, index, body query, context/authorization reference, approval flag, Session ID or preview/execute option is accepted. Unsupported Type, target Scope Unit, arbitrary projection and other generic Find filters fail rather than widen the request.

The public `SubjectLookupResult` has exactly `data`, `current_state`, `effects` and `errors`. On complete success, data is exactly `{matches, complete: true, subject_profile, subject_profile_evidence}`. Each match is exactly `{atom_id, version, status, current_scope_unit, updated_at, field, value}`; field is governs or depends_on, and separate matching fields remain separate rows. Sort by Atom ID, Version, field and exact value. No full Atom content, private path or dependency index is returned.

Current state is an array of unique `{identity, version, source_token, source_view}` records per matched carrier, preserving historical Versions; source_token is the complete-byte SHA-256 and source_view is exactly `{scope_unit, content_roles, lifecycle}`. Profile evidence is exactly `{grammar_pins, native_admission: not_performed}`, with each public pin exactly `{atom_id, version, sha256}`; physical pin paths remain private. Effects are always an empty array. Errors follow D625's exact code/message/field schema. A complete empty match returns empty matches/state/errors. A selected-source diagnostic, ambiguity, stale or incomplete frontier, unsupported input or exceeded read budget returns null data/current_state and nonempty errors; partial results are not successful complete coverage.

Validate current Delivery/Action and applicable Requirement/Method/shared definition pins, the selected grammar pins, Project settings/structure and selected-source evidence. Use bounded no-follow reads, preserve possible selected-current-ID collision checks without full admission of unrelated excluded C/A, and recheck source bytes and inventory before returning. Static reported hashes alone are insufficient. Do not require absent Type on otherwise eligible selected R/M/D sources.

Only this direct read-only Subject realization uses D625's named request-envelope exception. It creates no Session, Action Run, Journal or scratch staging artifact and grants no mutation permission. A real enclosing Workflow remains responsible for applicable Tool-call recording. Existing CLI and Session-based behavior, and all preview/staging/publication admission, remain unchanged. Installed binding/code refresh and actual registered/connected-MCP acceptance are separate from this source declaration.
