---
atom_id: CA-A-1286
ref_id: CA-A-1286
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
topics:
  main_subject: Model::CAPRMEDIO::Graph Syntax::Format
version: 3
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
---
# Summary

Represent nesting with properties instead of map Format

## Decision

Remove map from the proposed value Formats. Declared child properties describe nested structure; a YAML mapping is its carrier representation, not a separate value Format. The earlier removal of list remains in effect.

```text
subjects{0}
subjects.governs[string]{1}
subjects.depend_on[string]{0+}
```

The grouping property has no direct values. Each child keeps its own value format and cardinality. This changes neither nesting nor the existing YAML subjects.depends_on spelling. Arbitrary-key dictionary semantics are not introduced by this decision.

## State

The main Model proposal and Value Format Definition Draft omit map. Current methodology, configuration, implementation and runtime are unchanged.
