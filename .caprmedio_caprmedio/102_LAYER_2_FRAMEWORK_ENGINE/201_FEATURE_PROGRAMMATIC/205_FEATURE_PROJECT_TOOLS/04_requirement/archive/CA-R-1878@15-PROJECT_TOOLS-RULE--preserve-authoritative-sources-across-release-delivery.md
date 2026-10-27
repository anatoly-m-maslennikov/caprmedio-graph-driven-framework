---
atom_id: CA-R-1878@15
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
status: Archived
author: Anatoly Maslennikov
version: 15
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Delivery
  depends_on:
  - Subject/Graph Node/Engineering/Release Version/Authoritative Source Preservation
  - Subject/Graph Node/Domain/Continuant/Selection//Methodology Sources
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
relations: {}
type: Rule
tier: 3
---
# Summary

Preserve authoritative sources across release delivery

## Scope

The boundary between canonical release inputs and derived source, runtime, Skill, and image deliveries.

## Claim

Release Version **must** copy, compile, package, install, and verify only derived deliveries while preserving canonical authoring sources, Project Structure, Project and Framework Settings, existing Journal evidence, and unrelated Skills byte-for-byte.

## Details

A changed current source/frontier invalidates further direct delivery and requires fresh input and file/path safety checks plus the declared test scope—the complete discovered suite by default or the explicitly selected discovered modules when the Operator supplies `--test-module`—not separate Active Atom metadata, placement or relation validation. The release Tool does not repair authority to make delivery pass. Retain exact actual predecessor and effect evidence on failure or uncertainty; a completed-copy predecessor proof binds the exact actual safe copy path, complete file bytes and modes, source/copy identities and expected/actual digests, and the real executing Workflow/Action Run. Unknown, tampered, unsafe, mode-drifted or identity-drifted source-effect evidence is refused; arbitrary old JSON or file presence alone is neither ownership proof nor permission to reuse, replay or promote that copy; preserve protected authoring sources, Settings, Project Structure and Journal bytes and never replay an unknown effect. Plain Journal append/read preserves supplied observations independently of that source-effect evidence; no prior-history, chain, validation, canonical receipt, deduplication, logging retry or recovery prerequisite applies. Report actual logging I/O failure without changing the independently observed source-effect outcome or treating the log as permission or completion proof.

Current O164 records actual validated source, source-copy/product, compilation, package/runtime, Skill and image facts on its shared Run/Action evidence and owned Git transitions. It must not require or fabricate the retired D566/D567/D571 candidate/handoff/child formats or archived D574 checkpoints. Preserve all captured historical records unchanged; historical proof does not authorize a new release or prove unobserved old effects. First installation does not invent a prior installed release. Before any destructive replacement, the exact current replacement is ready and verified, protected configuration and Project state remain, and failure/cleanup blockers are reported truthfully.

Default Local release prepares its canonically named image only after the full suite is green. An explicitly focused Local route prepares it only after its selected scope passes. After installed-runtime verification and successful MCP smoke, retain the exact admitted candidate of the current package Version as the sole release-retention image. Remove other unused, positively classified images only when their inspected Project identity, host Project root and control root all match the selected Project. A different digest is not protected merely by the same source fingerprint, Version or tag. Preserve foreign, unowned, incompletely identified and container-referenced images; report blockers and failures without force, global prune or uncertain retries. A container link alone does not establish image ownership.

An explicit Local `--test-module` selection is a declared validation scope: it must be repeatable, repository-relative, and resolved against discovery; empty, duplicate, malformed, foreign, and symlink paths are refused, and any selected failure or required skip blocks downstream Local delivery. Selected scope may include any discovered source module, including Docker modules, with the existing shared image and launcher handling. Without this option the complete discovered suite remains the Local default. Focused evidence is not a Full Gate and cannot satisfy the Public Full Gate; public release retains its complete public gate.
