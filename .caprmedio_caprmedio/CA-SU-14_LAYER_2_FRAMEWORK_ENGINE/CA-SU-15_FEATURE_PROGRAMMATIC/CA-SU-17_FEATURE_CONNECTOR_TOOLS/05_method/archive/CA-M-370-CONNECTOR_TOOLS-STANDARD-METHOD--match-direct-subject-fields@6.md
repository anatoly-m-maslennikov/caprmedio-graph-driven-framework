---
atom_id: CA-M-370
content_role: Method
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool/ATOM_SEARCH"
  depends_on: [Atom, Subject, Artifact/Carrier, Scope Unit]
version: 6
updated_at: "2026-10-14 10:04:27 +0400"
relations:
  relates_to: [CA-R-863, CA-O-046, CA-E-301, CA-D-424]
---
# Summary

Match direct Subject fields in valid Atom carriers

## Scope

Direct Subject-field matching by an explicitly requested connector query.

## Claim

**To** match Subject data, the connector **must** first validate the explicitly supplied query, source view, schema/context, projection, budget and any source-state preconditions under CA-R-1936-CONNECTOR_TOOLS-CORE-REQUIREMENT--use-one-coherent-connector-interface. Read only the selected source data and the direct `subjects.governs` scalar and `subjects.depends_on` entries needed for that query. Apply the supplied field, owner Scope Unit, Content Role, Type and lifecycle predicates conjunctively; do not add default selection policy.

Use literal equality for `exact`. For explicitly requested `prefix`, use the supplied profile's lexical boundaries: `/` and `:` for legacy, with `.` additionally recognized for approved. For `suffix`, compare the end of the complete scalar; for `contains`, compare a literal substring. Preserve the `Atom`/`atom` distinction and validate any supplied Subject profile without choosing one, translating profiles, expanding selectors or inferring semantic relations.

Return matching values and attributable current source-state evidence in stable order. A dependency position may be an observed storage detail, but it is not a logical update selector or a required public list-edit index. Report invalid selected data and limited coverage explicitly. No query grants effect permission or performs a mutation.

## Details

### Direct Subject subset

For CA-D-424's direct read-only subset, validate explicit owning Scope Unit, Content Roles, lifecycle, profile, field, one value/mode criterion and optional full Atom IDs before traversal. Do not require the unsupported Type, target Scope Unit or arbitrary projection filters; reject them if supplied and do not claim the broader query contract is fully delivered. Suffix and contains criteria may be nonempty literal fragments rather than complete Subject expressions. Validate complete selected source Subjects under the supplied profile.

Apply owner, role and lifecycle eligibility before full selected-content parsing. Do not require unrelated excluded C/A sources or selected Type-absent R/M/D carriers to adopt another header schema. Retain checks for possible competing selected current Atom IDs across owners and excluded roles; malformed excluded headers cause refusal only when they can claim a selected identity. Bound reads and identity checks, reject symlinks and owner/path disagreement, and recheck source bytes, source inventory, Project boundary and grammar evidence before returning. Never present a partial or uncertain set as complete. No Session, Action Run, Journal or staging artifact is created; actual enclosing Workflow recording remains caller-owned.

The common interface representation belongs to CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface. Workflow default-selection, identity, Version, lifecycle and multi-Atom sequencing policies remain in TOOL_WORKFLOWS. The historical `@<version>` archive filename convention remains a private storage representation. Code adoption and acceptance are separate.
