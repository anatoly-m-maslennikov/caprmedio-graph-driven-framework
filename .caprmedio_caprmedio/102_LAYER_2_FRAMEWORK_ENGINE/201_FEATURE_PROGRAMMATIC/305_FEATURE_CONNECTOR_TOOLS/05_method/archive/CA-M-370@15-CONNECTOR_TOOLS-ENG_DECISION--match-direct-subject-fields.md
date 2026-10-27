---
atom_id: CA-M-370@15
content_role: Method
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Tool//ATOM_SEARCH
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Scope Unit
version: 15
updated_at: 2026-10-24 12:35:51 +0400
relations:
  relates_to:
  - CA-R-863
  - CA-O-046
  - CA-E-301
  - CA-D-424
type: Eng Decision
tier: 3
---
# Summary

Match direct Subject fields in valid Atom carriers

## Scope

Direct Subject-field matching by an explicitly requested connector query.

## Claim

**To** match Subject data, the connector **must** first validate the explicitly supplied query, source view, schema/context, projection, budget and any source-state preconditions under CA-R-1936-CONNECTOR_TOOLS-RULE--use-one-coherent-connector-interface. Read only the selected source data and the direct `subjects.governs` scalar and `subjects.depends_on` entries needed for that query. Apply the supplied field, owner Scope Unit, Content Role, Type and lifecycle predicates conjunctively; do not add default selection policy.

Use literal equality for `exact`. For explicitly requested `prefix`, use the supplied profile's lexical boundaries: `/` and `:` for legacy, with `.` additionally recognized for approved. For `suffix`, compare the end of the complete scalar; for `contains`, compare a literal substring. Preserve the `Atom`/`atom` distinction and validate any supplied Subject profile without choosing one, translating profiles, expanding selectors or inferring semantic relations.

Return matching values and attributable current source-state evidence in stable order. A dependency position may be an observed storage detail, but it is not a logical update selector or a required public list-edit index. Report invalid selected data and limited coverage explicitly. No query grants effect permission or performs a mutation.

For an isolated selected Atom whose schema is invalid but whose source frontier and
safety checks remain usable, emit a technical warning with the repository-relative
path and reason, skip that Atom, continue the bounded scan, and mark the result
`complete: false`. Route that warning through the configured diagnostic logging
abstraction under CA-M-414; do not append it as a business Journal event or repair
the source. I/O, security, duplicate-identity, stale, ambiguous, and other
incomplete-frontier failures remain fatal refusal/error outcomes rather than partial
success.

## Details

### Direct Subject subset

For CA-D-424's direct read-only subset, validate explicit owning Scope Unit, Content Roles, lifecycle, profile, field, one value/mode criterion and optional full Atom IDs before traversal. Do not require the unsupported Type, target Scope Unit or arbitrary projection filters; reject them if supplied and do not claim the broader query contract is fully delivered. Suffix and contains criteria may be nonempty literal fragments rather than complete Subject expressions. Validate complete selected source Subjects under the supplied profile.

Apply owner, role and lifecycle eligibility before full selected-content parsing. Do not require unrelated excluded C/A sources or selected Type-absent R/M/D carriers to adopt another header schema. Retain checks for possible competing selected current Atom IDs across owners and excluded roles; malformed excluded headers cause refusal only when they can claim a selected identity. Bound reads and identity checks, reject symlinks and owner/path disagreement, and recheck source bytes, source inventory, Project boundary and grammar evidence before returning. Never present a partial or uncertain set as complete. No Session, Action Run, Journal or staging artifact is created; actual enclosing Workflow recording remains caller-owned.

The common interface representation belongs to CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface. Workflow default-selection, identity, Version, lifecycle and multi-Atom sequencing policies remain in TOOL_WORKFLOWS. The historical `@<version>` archive filename convention remains a private storage representation. Code adoption and acceptance are separate.
