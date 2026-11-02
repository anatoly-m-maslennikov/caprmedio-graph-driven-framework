---
atom_id: CA-M-331
content_role: Method
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-11 16:46:21 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Candidate construction"
  depends_on: [Tool, Manifest, Digest, Artifact, Revision]
relations:
  method_for: [CA-R-1876, CA-R-1877]
---
# Summary

Construct one sealed Release Version candidate manifest

## Scope

Pure construction of the N/N+1 candidate inventory before release effects.

## Claim

The Tool constructs one canonical `candidateSnapshotManifest` internally by discovering current registered release definitions and their Action-to-Tool bindings, capturing current active Methodology-source Atoms at Run start, and normalizing the captured inventory into ordered repository-relative input/output rows. It binds each row to its captured bytes, digest and destination and derives one candidate manifest SHA-256 without installing, compiling, testing, deleting, or changing product or installed contents.

## Details

Construction rejects duplicate destinations, traversal, missing required Framework Methodology or Engine rows, mismatched versions, and ambiguous current selections. The same consistent snapshot is the input to every later admitted candidate phase; no Operator-supplied revision list or separate manifest refresh is required. The result is an input to later admitted effects, not a Workflow or an execution receipt.
