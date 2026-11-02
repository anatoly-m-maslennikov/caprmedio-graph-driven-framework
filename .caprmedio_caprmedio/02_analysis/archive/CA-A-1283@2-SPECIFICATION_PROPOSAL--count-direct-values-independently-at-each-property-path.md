---
atom_id: CA-A-1283@2
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Graph Syntax.Cardinality Notation
version: 2
relations: {}
tier: 3
updated_at: 2026-10-29 21:51:04 +0400
---
# Summary

Count direct values independently at each property path

## Decision

Cardinality counts only the direct values of the addressed property. It does not count nested keys or include values belonging to child properties. A parent with `{0}` has no direct values; its declared children remain permitted and obey their own independent counts. Use explicit `{0}` for grouping properties rather than inferring it from an omitted annotation.

```text
claim[string]{1}
claim.formal_claim[string]{0..1}
subjects{0}
subjects.governs[ref]{1}
subjects.depend_on[ref]{0+}
```

Claim requires exactly one prose value. Its optional Formal claim is counted separately and cannot satisfy that prose requirement. Formal and prose still address one Type-defined contribution; Semantics remains separate. The formal child remains R-only.

Subjects has no direct value. It groups one governing reference and zero or more dependency references. The logical example uses depend_on; the existing YAML key subjects.depends_on is not renamed by this decision.

## Carrier distinction

A YAML property key occurs once within its mapping. Multiple values are serialized as a sequence under that one key. For `property[string]{2}`:

```yaml
property:
  - string1
  - string2
```

Repeated keys such as two sibling version keys are invalid. A mapping under subjects represents child properties, not an additional direct subjects value. A YAML sequence represents multiple values, not a separate list value Format. Remove list from the proposed Formats. This decision does not settle map as an independent value Format.

## State

The cardinality, Claim, base-property, Definition-Type and R/M/E/D Drafts and main Model proposal are aligned. Formal-only prepared Definitions receive a prose Claim from their already recorded meaning. Existing Current sources and runtime are unchanged; Drafts can still be incomplete before promotion.
