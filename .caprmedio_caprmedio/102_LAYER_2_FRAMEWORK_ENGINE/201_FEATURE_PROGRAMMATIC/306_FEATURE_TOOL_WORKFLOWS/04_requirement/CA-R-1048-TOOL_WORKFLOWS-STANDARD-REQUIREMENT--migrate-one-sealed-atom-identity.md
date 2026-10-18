---
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 15
updated_at: "2026-10-19 02:18:51 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
atom_id: CA-R-1048
status: Active
author: Anatoly Maslennikov
---
# Summary

Migrate one sealed Atom identity

## Scope

One assigned legacy Atom identity normalization and independent composition of these Actions.

## Claim

The existing `update_atom` Workflow normalizes one explicitly selected assigned legacy identity. `legacy_identity_proof` binds the exact identity, path, digest and ancestor Git bytes. A missing identity header may be restored from that proof. An explicit noncanonical identity may be changed only through `legacy_identity_mapping`, which names the exact old identity, approved unused canonical identity and destination. An already canonical assigned identity must not be renumbered by this route.

The canonical Atom ID must agree in the destination filename and YAML `atom_id`. The migration preserves Summary, substantive content, Content Role, Type, Status, owning and target Scope Units, tiers, Subjects, relations and all other fields except explicitly approved repairs needed by the current carrier schema. A Scope Unit move is a separate Action. The exact predecessor bytes are retained; Version advances once and Updated At records the actual update.

Preview changes no source. Apply uses the existing MCP authorization and lifecycle execution boundary. Source or proof mismatch, ambiguous identity, destination or reserved-ID collision, role mismatch and unapproved changes stop that Action. The result reports the actual identity mapping, current carrier, predecessor and effects; the Workflow records the actual outcome. This does not add another approval protocol or a prerequisite for earlier Journal history.

A sequence uses independent one-Atom Actions, stops at the first failed or uncertain Action, preserves earlier completed effects and leaves the remainder untouched. It does not promise a cross-Atom transaction or automatic replay.

## Details
