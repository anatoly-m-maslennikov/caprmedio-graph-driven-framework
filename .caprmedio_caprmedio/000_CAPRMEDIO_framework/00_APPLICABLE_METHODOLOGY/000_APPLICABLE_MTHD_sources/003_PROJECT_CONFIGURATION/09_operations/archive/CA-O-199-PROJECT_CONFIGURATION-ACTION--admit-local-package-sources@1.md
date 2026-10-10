---
atom_id: CA-O-199
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 22:00:55 +0400"
subjects:
  governs: "Admit local package sources"
  depends_on: [Action, Operator, Framework Package, Methodology, Catalog, Digest, Journal]
relations:
  relates_to: [CA-R-1908, CA-D-602, CA-D-596]
---
# Summary

Admit local package sources

## Operation

Admit local package sources **means** the programmatic Action that records the Operator's explicit admission of one exact local Core, selected active Methodology and declared support snapshot for package preparation.

## Scope

One selected Project, physically observed source snapshot and verified Operator command for this Action Run.

## Details

1. Observe the selected source bytes and modes through the sealed candidate and private Methodology export/compilation readers. Compute the source descriptors without requiring an existing catalog.
2. Bind the exact snapshot to the Operator command through the trusted invocation admission boundary. Missing, rejected or differently bound invocation evidence stops before receipt or catalog publication.
3. Retain one content-addressed admission record and its matching catalog. Reopen both and retain their actual output references as evidence for this Action Run. Preserve an existing different catalog; replacement requires an explicitly admitted replacement request.
4. Return the snapshot, receipt and catalog identities and actual outcome to the caller. Failed or uncertain publication retains its evidence and does not silently replay an effect.

This Action runs only on the Operator's command, including an explicit command that selects it together with release preparation. Its completion does not start a release Workflow. The canonical Journal retains its Action Run evidence; the package receipt is a derived proof carrier, not a second event log. Optional extensions remain separately admitted. No Tool Run type is created.
