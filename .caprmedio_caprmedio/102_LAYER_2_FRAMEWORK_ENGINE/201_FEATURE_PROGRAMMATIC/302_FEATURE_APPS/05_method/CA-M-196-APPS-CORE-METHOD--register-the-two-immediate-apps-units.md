---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - feature-boundary
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1100
    - CA-R-1101
  derived_from:
    - CA-A-058
---
# Register the two immediate APPS units

## Applicable when

Use this Method when defining the immediate structural decomposition of the APPS Feature.

## Procedure

1. Register GRAPH_APP and AGENT_HOST_PLUGINS as the complete unordered set of immediate child Scope Units owned by APPS.
2. Give each child its stable structural address, scope token, source path, and level directly below APPS.
3. Assign GRAPH_APP ownership of the source indexer, rebuildable database, read-only local server, and web views.
4. Assign AGENT_HOST_PLUGINS ownership of host-specific installation and wiring only; keep provider-neutral behavior outside it.
5. Rebuild the Project Scope Unit Graph from these authority carriers and verify that neither child owns the other.

## Outcome

APPS has exactly two immediate children with non-overlapping GRAPH_APP and host-plugin responsibilities.

## Failure or stop

Stop when either child is missing, duplicated, ordered under its sibling, assigned a conflicting address, or given authority owned by the other boundary.
