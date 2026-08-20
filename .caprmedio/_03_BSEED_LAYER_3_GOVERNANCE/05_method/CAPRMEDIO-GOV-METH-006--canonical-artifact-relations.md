---
subject_scopes:
  - relation-model
tier: core
version: 7
updated_at: 2026-08-21 01:09:53
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CA-R-806-REQUIREMENT-BSEED_GOVERNANCE--register-complete-relation-kind-metadata
    - CA-R-807-REQUIREMENT-BSEED_GOVERNANCE--store-replacement-as-direct-replaced-by
    - CA-R-808-REQUIREMENT-BSEED_GOVERNANCE--limit-active-direct-relations-to-upstream-or-same-tier
    - CA-R-809-REQUIREMENT-BSEED_GOVERNANCE--validate-direct-relation-global-tier-direction
  resolution_of:
    - CAPRMEDIO-SPEC-TOOLS-CONC-056--legacy-relation-sealing
    - CAPRMEDIO-SPEC-TOOLS-CONC-057--atomic-replacement-source
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Compile the canonical relation-kind registry

Compile the active GOV Requirement Atoms that register semantic relations into exactly one machine-readable dictionary at `.caprmedio/200_LAYER_2_FRAMEWORK_ENGINE/TOOLS/caprmedio_relation_types.toml`. Install a content-identical copy with every self-contained Tool runtime release that reads the dictionary. Each registration Atom owns one direct relation's exclusive meaning and supplies every field required by the complete relation-kind metadata Requirement. The compilation must not invent aliases, merge near-synonyms, or infer inverse names, direction, authority, lifecycle, or endpoint rules from spelling.

For each admitted direct relation, emit exactly one row with these columns in canonical order:

| Column | Meaning |
|---|---|
| `direct_name` | The only name authored by the persisted owner |
| `inverse_name` | The unique name derived for reverse navigation |
| `source_lifecycles` | Lifecycle states permitted to author the direct edge |
| `target_lifecycles` | Lifecycle states permitted at direct-edge creation |
| `owner` | The endpoint that persists the direct edge |
| `direct_direction` | Source-to-target endpoint direction |
| `upstream_endpoint` | The endpoint treated as upstream for governed traversal |
| `source_classes` | Allowed source Artifact classes |
| `target_classes` | Allowed target Artifact classes |
| `cardinality` | Allowed endpoint cardinality |
| `authority_effect` | Authority, coverage, precedence, or no-authority effect |
| `transitive` | Whether transitive closure is semantically valid |
| `symmetric` | Whether reversing endpoints preserves meaning |
| `authority_modes` | Modes in which the relation may be authored |
| `status` | Active, deprecated, or sealed lifecycle state |
| `exclusive_meaning` | The bounded fact expressed by the relation |

Sort rows by `direct_name`. Store only the direct edge on its registered owner. Derive the inverse view at query time and never write it as a backlink. For an active source at global tier `N`, enforce an active target with global tier less than or equal to `N` before applying any stricter row-specific rule. Compile replacement only as direct `replaced_by` with derived inverse `replacement_of`. Reject compilation when a direct or inverse name is duplicated, an inverse is also admitted as direct, a required field is absent, endpoint rules conflict, or more than one active registration claims the same meaning. Relation kinds used only by rule registries or Structural configuration remain outside this Atom relation-type dictionary unless a GOV Requirement explicitly admits them.
