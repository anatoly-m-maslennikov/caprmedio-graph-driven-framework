---
atom_id: CA-O-180
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-09 16:36:54 +0400"
subjects:
  governs: "Initialize first Framework runtime and project-local ca Skill"
  depends_on: [Action, Operator, Framework Package, Runtime, Methodology, Skill, Docker Image, Journal]
relations:
  relates_to: [CA-O-164, CA-R-1525, CA-R-1720, CA-R-1881, CA-M-338, CA-D-575]
---
# Summary

Initialize the first Framework runtime and project-local ca Skill

## Action

Initialize the first Framework runtime and project-local `ca` Skill **means** the explicit Operator-invoked Action that creates one initial runtime selection only from the empty carrier state defined by CA-R-1881.

## Scope

The Action binds one sealed current source frontier, one empty runtime/Skill state, one complete manifest-addressed package, one immutable image digest, explicit target-Project metadata, settings, Project Structure and selected control-root `.caprmedio_<project>/operators_registry.toml` bytes, selected extension/configuration revisions from one admitted pinned catalog, and one canonical Action Run. Bootstrap or adoption **must not** fabricate a Project identity, metadata, settings, structure, registry, selected extension or configuration. An adopt entry admits only those existing Project carriers and **no** already-active Framework runtime; upgrade and idempotent reinstallation are outside this first-initialization Action. Its canonical started-Run input binds `requested_run_id`, package-manifest SHA-256, sealed source-context SHA-256, catalog/configuration identity and immutable image digest as one exact intent. It is a bootstrap Action outside CA-O-164's selected Release Version Workflow.

## Details

The Action invokes the admitted FRAMEWORK_INITIALIZATION Tool boundary once. CA-R-1881, CA-M-338 and CA-D-575 remain their owning Engine/TOOLS authority; this Action only binds to their admitted package and carrier evidence. It reopens the exact source and started-Run evidence before any effect; verifies the complete package, hook-free Skill, and inspected immutable image digest and labels bound to the started intent and actual manifest and source-context digests; publishes the Skill; then publishes the reusable package selector and this Project's `.caprmedio_runtime/installation/current.toml` state/environment binding as final activation points and emits the terminal result through the schema-V5 Work Journal. Tool-call evidence attaches to the Action Run by evidence references and parentage; it does not create a Tool Run. Reusing `requested_run_id` with a changed manifest, source-context, catalog/configuration or image digest permits only existing-Run inspection or recovery; it does not create another started evidence entry or source ledger. It does not create a selected-workflow binding, candidate N+1, Release Version Run, source delivery, canonical Projection, hook, global setting, MCP registration, image removal, automatic retry, or permanent bootstrap configuration. Existing state or an uncertain effect returns its actual blocked or partial evidence. Later changes use CA-O-164's N-to-N+1 Release Version path.
