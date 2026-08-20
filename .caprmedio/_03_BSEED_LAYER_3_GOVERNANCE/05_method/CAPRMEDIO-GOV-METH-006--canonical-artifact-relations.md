---
subject_scopes:
  - relation-model
tier: core
version: 5
updated_at: 2026-08-20 19:42:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CA-R-806-REQUIREMENT-BSEED_GOVERNANCE--register-complete-relation-kind-metadata
  replacement_of:
    - CAPRMEDIO-GOV-METH-023--typed-artifact-relations
  resolution_of:
    - CAPRMEDIO-SPEC-TOOLS-CONC-056--legacy-relation-sealing
    - CAPRMEDIO-SPEC-TOOLS-CONC-057--atomic-replacement-source
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Compile the canonical relation-kind registry

Compile one relation-kind registry from the active GOV Requirement Atoms that register semantic relations. Each registration Atom owns one direct relation's exclusive meaning and supplies every field required by the complete relation-kind metadata Requirement. The compilation must not invent aliases, merge near-synonyms, or infer inverse names, direction, authority, or endpoint rules from spelling.

For each admitted direct relation, emit exactly one row with these columns in canonical order:

| Column | Meaning |
|---|---|
| `direct_name` | The only name authored by the persisted owner |
| `inverse_name` | The unique name derived for reverse navigation |
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

Store only the direct edge on its registered owner. Derive the inverse view at query time and never write it as a backlink. Reject compilation when a direct or inverse name is duplicated, a required field is absent, endpoint rules conflict, or more than one active registration claims the same meaning. Relation kinds used only by rule registries or Structural configuration remain outside this semantic-relation registry unless a GOV Requirement explicitly admits them.
