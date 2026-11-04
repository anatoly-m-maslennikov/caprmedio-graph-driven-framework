---
atom_id: CA-R-2723
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
version: 1
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2723@1-WORKBENCH-RULE--derive-query-projection-only-from-governed-atom-sources.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
updated_at: 2026-11-03 23:17:14 +0400
---
## Summary

Derive the query Projection only from governed Atom sources

## Claim scope

The query Projection of canonical Atom carriers in the governed source inventory.

## Claim

### Prose Claim

The query Projection **must**:

- derive its data only from the existing bound Project context and its canonical governed Atom inventory; no additional named selection artifact or admission gate is required.
- retain each indexed carrier's source locator, Atom identity, Version, lifecycle group, Header, and Markdown Content.
- include all lifecycle groups in that inventory and keep them distinct. A carrier in one lifecycle group **must not** overwrite a carrier in another group solely because they share a base ID.
- treat an observed Atom identity and Version in a source record as source data, not as a fixed-file pin or proof of a Journal record.
- skip a source-file failure with a stderr diagnostic rather than a result record or automatic retry of that same failed input; other valid sources remain eligible.
- remain derived data that can be rebuilt from its sources.
- never edit, move, archive, promote, or invent a source Atom.

