---
atom_id: CA-R-1878
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-14 12:27:02 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Authority preservation"
  depends_on: [Tool, Methodology, Projection, Journal, Project Settings, Framework Settings]
relations: {}
---
# Summary

Preserve authoritative sources across release delivery

## Scope

The boundary between canonical release inputs and derived source, runtime, Skill, and image deliveries.

## Claim

Release Version **must** copy, compile, package, install, and verify only derived deliveries while preserving canonical authoring sources, Project Structure, Project and Framework Settings, existing Journal evidence, and unrelated Skills byte-for-byte.

## Details

A changed current source/frontier invalidates further direct delivery and requires fresh input validation and intended tests. The release Tool does not repair authority to make delivery pass. Retain exact actual predecessor and effect evidence on failure or uncertainty; a completed-copy predecessor proof binds the exact actual safe copy path, complete file bytes and modes, source/copy identities and expected/actual digests, and the real executing Workflow/Action Run and canonical Journal references. Unknown, unrecorded, tampered, unsafe, mode-drifted or identity-drifted proof is refused; arbitrary old JSON or file presence alone is neither ownership proof nor permission to reuse, replay or promote that copy; preserve protected authoring sources, Settings, Project Structure and Journal bytes and never replay an unknown effect.

Current O164 records actual validated source, source-copy/product, compilation, package/runtime, Skill and image facts on its shared Run/Action evidence and owned Git transitions. It must not require or fabricate the retired D566/D567/D571 candidate/handoff/child formats or archived D574 checkpoints. Preserve all captured historical records unchanged; historical proof does not authorize a new release or prove unobserved old effects. First installation does not invent a prior installed release. Before any destructive replacement, the exact current replacement is ready and verified, protected configuration and Project state remain, and failure/cleanup blockers are reported truthfully.
