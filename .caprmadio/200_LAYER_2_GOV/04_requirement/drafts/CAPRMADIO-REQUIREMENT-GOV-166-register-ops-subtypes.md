---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-166
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-143-register-release-record-ops-subtype
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-149-register-caprmadio-atom-type-surface
    - CAPRMADIO-REQUIREMENT-GOV-152-register-caprmadio-type-prefixes
---

# Register Ops subtypes

GOV must register these direct subtypes of the internal `ops` Atom Type:

| Subtype | Governed unit |
|---|---|
| `release_record` | One successful release event with the exact frozen version and released manifest. |
| `deployment_record` | One bounded deployment event and its factual outcome. |
| `environment_state` | One bounded observation of the deployed state of one environment. |
| `health_record` | One bounded observation set describing runtime health. |
| `incident_record` | One bounded production incident and its observed impact. |

All Ops subtypes use the `OPER` Type prefix and the Ops Type numbering sequence. They record enacted facts and do not establish normative specification or planning authority.
