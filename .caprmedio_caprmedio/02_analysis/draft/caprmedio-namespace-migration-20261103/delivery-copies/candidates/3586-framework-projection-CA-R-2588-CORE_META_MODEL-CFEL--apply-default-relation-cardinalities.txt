---
atom_id: CA-R-2588
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2588-CORE_META_MODEL-CFEL--apply-default-relation-cardinalities.md
  source_atom_id: CA-R-2588
  source_atom_revision: 2
  source_sha256: 609bdaf494217abf6745897c0b4fb086a5625ed96c6dce8a0d562e5511e02544
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Apply default Relation cardinalities

## Claim

- `Host {:0}((*))` sets the default outgoing Relation cardinality for Host to zero.
- `((*))` selects Relation names. Allowed-value notation such as `{:x}` and literal value bindings keep their existing meanings.
- Resolve the selected MODEL, inheritance and applicable named Relation constraints before applying the default. Match the Host, Relation, Target and model or instance layer. A matching named entry supplies its own outgoing count.
- Apply the default to links outside the matched Host, Relation, Target and layer of a named exception. A local named exception also works with an inherited default.
- Narrowing inheritance preserves each selector's scope. Property dependence is distinct from narrowing.
- Named constraints retain their bounds, including an explicit named zero. An explicit MODEL override replaces the matching effective rule. Check all other applicable named constraints together and report conflicting bounds.
- Conditional constraints retain their conditions. Normalize `>|` and `|<` to their HAS_CLASSIFICATION directions: an assertion or true conditional conclusion supplies the matching entry only for its stated Host, axis, value and condition. A Relation reference used only as a condition or example grants nothing. Do not infer unspecified axes or counts.
- Model-entity and instance selectors have separate effective whitelists. An entry applies only to its stated layer. A direct Relation permission does not automatically permit its inverse view; each direction needs its own named entry. Derived inverse links are not authored a second time.
- Every count concerns the active Subject's outgoing Relations. The counterpart Declaration owns its own outgoing counts.

## Details

Model-entity default:

```CFEL
(Node, Node.**) {:0}((*))
```

Instance default:

```CFEL
(Node//, (Node//).**) {:0}((*))
```

Instance exception:

```CFEL
Journal// {:0+}((CONTAINS)) Event Record//
```
