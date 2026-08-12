---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-137
scope_path: layer:gov
subject_scopes:
  - public-interface
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-087
---

# Requirement — Register ca as the specialist skill prefix

GOV registers `caprmadio` as CAPRMADIO's canonical primary routing skill and
`ca-` as its canonical short prefix for action-specific public skill names. An
action-specific CAPRMADIO skill uses `ca-<action>` unless a governed external
host contract requires another spelling.

The prefix is an interface abbreviation only. It does not rename the CAPRMADIO
framework, alter governed artifact IDs, or establish a second project prefix.
Skill descriptions and host metadata still identify CAPRMADIO explicitly so
discovery does not depend on knowing the abbreviation in advance.

`ca-` is reserved exclusively for public skill names. CLI commands, package
and import names, repository identities, directories, settings, schemas,
artifact identities, and other non-skill interfaces use their governed
CAPRMADIO names and must not use `ca-`. The unhyphenated `ca` name is not a
public skill identity.

## Primary claim

CAPRMADIO uses `caprmadio` as its primary routing skill and the canonical `ca-`
prefix for action-specific public skills; no non-skill identity uses that
abbreviation.

## Rationale

The short prefix is visibly derived from CAPRMADIO and keeps frequently invoked
specialist skill names readable. Exclusive ownership prevents it from becoming
a second framework, package, command, or artifact namespace, while the full
primary name keeps the main entrypoint explicit and discoverable.
