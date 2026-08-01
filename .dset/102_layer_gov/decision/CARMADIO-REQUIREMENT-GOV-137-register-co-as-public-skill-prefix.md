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

## Primary claim

Public CARMADIO skill names use the canonical `co-` prefix.

## Rationale

The short prefix keeps frequently invoked skill names readable while one
registered expansion prevents each skill from inventing an unrelated
abbreviation or leaving `co` semantically unexplained.
