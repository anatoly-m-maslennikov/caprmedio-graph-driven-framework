---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-102
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-049
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-098
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-070
---

# Separate route catalog and project whitelist

One project-local `artifact_catalog.toml` inside the installed methodology owns
the registered artifact types, optional direct subtypes, identity kinds,
derived routes, allowed carriers, and persistence behavior.

`caprmadio_settings.toml` owns only the project selection:

- enabled artifact types and subtypes;
- enabled Governance loci;
- naming options;
- project-specific extensions admitted by the selected governance profile; and
- other operator-controlled workflow settings.

Writers and validators load the catalog first and then apply the settings
whitelist. An unknown, disabled, multiply mapped, or ambiguous type/subtype
fails closed. Project customization changes the project-local catalog through
the governed methodology-customization flow; it does not create a second
classification table in settings, schemas, skills, or tools.

Catalog entries for persisted artifacts declare `commit_on_create`.
`commit_on_update` appears only for entries whose governed content may change
in place and is absent from every atomic entry.

## Rationale

Separating definitions from selection keeps one semantic mapping while allowing
small projects to enable only the artifact vocabulary they need.
