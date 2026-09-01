---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-196
---
# Verify register the two immediate apps units

## Claim checked

CA-M-196 gives APPS exactly two immediate unordered children with distinct GRAPH_APP and AGENT_HOST_PLUGINS responsibilities.

## Applicable when

Apply whenever the APPS structural decomposition or its Project Scope Unit Graph Projection changes.

## Test case

Build the Project Scope Unit Graph from the active APPS authority and inspect immediate children, typed ownership edges, addresses, source paths, levels, and responsibility statements for GRAPH_APP and AGENT_HOST_PLUGINS.

## Acceptance criteria

APPS has exactly those two immediate children; neither is ordered under the other; their addresses and paths are unique; GRAPH_APP owns graph serving and views; AGENT_HOST_PLUGINS owns only host-specific installation and wiring.

## Failure disposition

Reject the decomposition and preserve the source Atoms, derived graph nodes and edges, duplicate or missing children, and responsibility overlap.
