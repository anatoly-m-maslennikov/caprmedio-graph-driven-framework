---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-056
scope_path: layer:meta
subject_scope: scope-topology
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-044
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-038
      - CAPRMADIO-REQUIREMENT-META-051
---

# Requirement — Preserve external boundary obligations

An operator-accepted DDL, file schema, API, protocol, host format,
supported-platform interface, CI interface, dependency boundary, or comparable
participant obligation is a relational Definition with explicit participants
and a pinned external source version or digest.

Implementation must conform to the exact committed obligation revision it
consumes and cannot rewrite it. A changed external source creates a new
committed revision under the same artifact ID when the same participant
obligation remains identifiable. A different obligation requires a new
relational Definition with an explicit replacement relation. Existing
implementations remain bound to their consumed revisions until lineage-impact
review determines their disposition.

META defines this boundary meaning without assigning its concrete artifact type
or subtype name. GOV owns the canonical name, carrier, identity, and catalog
registration.

## Rationale

This preserves non-negotiable interfaces while removing concrete GOV taxonomy
from the META layer.
