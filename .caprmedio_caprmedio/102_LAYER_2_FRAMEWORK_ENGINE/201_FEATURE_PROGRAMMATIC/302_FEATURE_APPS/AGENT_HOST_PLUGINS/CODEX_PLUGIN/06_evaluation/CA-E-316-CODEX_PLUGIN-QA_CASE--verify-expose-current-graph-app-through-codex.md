---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - graph-app-access
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-198
---
# Verify expose the current graph_app through codex

## Claim checked

CA-M-198 exposes current GRAPH_APP state through Codex as an attributable read-only view with explicit stale and unavailable states.

## Applicable when

Apply before accepting any Codex plugin release that exposes Project Graph browsing.

## Test case

Connect Codex first to a current GRAPH_APP fixture and inspect one filtered node, then alter its source carrier without rebuilding GRAPH_APP and repeat the same inspection while recording all repository digests.

## Acceptance criteria

The current view returns navigation and node content with exact source path, digest, and provenance; the changed-source view reports stale state rather than old content as current; no repository digest changes.

## Failure disposition

Reject the Codex exposure and preserve GRAPH_APP frontier data, selected node results, stale-state handling, and mutation evidence.
