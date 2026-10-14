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
version: 5
updated_at: "2026-10-12 23:58:28 +0400"
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

The common interface representation belongs to CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface. Workflow default-selection, identity, Version, lifecycle and multi-Atom sequencing policies remain in TOOL_WORKFLOWS. The historical `@<version>` archive filename convention remains a private storage representation. Code adoption and acceptance are separate.
