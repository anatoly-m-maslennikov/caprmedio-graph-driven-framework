---
atom_id: CA-R-2588
ref_id: CA-R-2588@6-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Draft
version: 6
updated_at: 2026-11-05 01:53:49 +0400
carrier_destination:
  file:
    name: CA-R-2588@6-draft-RULE--apply-default-relation-cardinalities.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Apply default Relation cardinalities

## Claim

### Prose Claim

- `Host {::0}((*))` sets the default outgoing Relation cardinality for Host to zero.
- `((*))` selects Relation names. Allowed-value notation such as `{::x}` and literal value bindings keep their existing meanings.
- Resolve the selected MODEL, inheritance and applicable named Relation constraints before applying the default. Match the Host, Relation, Target and model or instance layer. A matching named entry supplies its own outgoing count.
- Apply the default to links outside the matched Host, Relation, Target and layer of a named exception. A local named exception also works with an inherited default.
- Narrowing inheritance preserves each selector's scope. Property dependence is distinct from narrowing.
- Named constraints retain their bounds, including an explicit named zero. An explicit MODEL override replaces the matching effective rule. Check all other applicable named constraints together and report conflicting bounds.
- Conditional constraints retain their conditions. Normalize `>|` and `|<` to their HAS_CLASSIFICATION directions: an assertion or true conditional conclusion supplies the matching entry only for its stated Host, axis, value and condition. A Relation reference used only as a condition or example grants nothing. Do not infer unspecified axes or counts.
- Model-entity and instance selectors have separate effective whitelists. An entry applies only to its stated layer. A direct Relation permission does not automatically permit its inverse view; each direction needs its own named entry. Derived inverse links are not authored a second time.
- Relation counts are attached to their written endpoint slots: `Source {::left}((R)){::right} Target` constrains outgoing matches from the written Source on the left and incoming matches to the written Target on the right. Either slot may be omitted and remains unspecified. Normalize a reverse-written view by swapping canonical endpoints and their written count slots. The wildcard default governs outgoing counts only; it does not reinterpret a right-slot bound as outgoing or infer a missing bound. Each counterpart direction still needs its own applicable named outgoing permission; the direct Declaration owns the shared meaning and counterpart binding.

