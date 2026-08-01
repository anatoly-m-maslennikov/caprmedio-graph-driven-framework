---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-137
scope_path: layer:gov
subject_scopes:
  - public-interface
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-087
---

# Requirement — Register co as the public skill prefix

GOV registers `co-` as CARMADIO's canonical short prefix for public skill
names. A public CARMADIO skill uses `co-<action>` unless a governed external
host contract requires another spelling.

The prefix is an interface abbreviation only. It does not rename the CARMADIO
framework, alter governed artifact IDs, or establish a second project prefix.
Skill descriptions and host metadata still identify CARMADIO explicitly so
discovery does not depend on knowing the abbreviation in advance.

`co-` is reserved exclusively for public skill names. CLI commands, package
and import names, repository identities, directories, settings, schemas,
artifact identities, and other non-skill interfaces use their governed
CARMADIO names and must not use `co-`. The primary routing skill may use the
unhyphenated name `co`; every action-specific public skill uses `co-<action>`.

## Primary claim

Public CARMADIO skills use `co` or the canonical `co-` prefix, and no
non-skill identity uses that abbreviation.

## Rationale

The short prefix keeps frequently invoked skill names readable while exclusive
ownership prevents it from becoming a second framework, package, command, or
artifact namespace.
