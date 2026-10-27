---
atom_id: CA-D-586@5
content_role: Delivery
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: Subject/Engineering/Tool//RELEASE_VERSION.Package
  depends_on:
  - Subject/Engineering/Tool//RELEASE_VERSION.Package
  - Subject/Engineering/Carrier/File Carrier
  - Manifest
  - Release Version
  - Subject/Engineering/MCP
relations: {}
type: Eng Decision
tier: 3
---
# Summary

Package the Release Tool private reader closure

## Scope

The private reader dependency delivery of a content-addressed Tool Package containing the Release suite reference-context reader.

## Claim

A Tool Package containing `TOOLS/RELEASE_VERSION/release_suite_reference_context.py` **must** include its two canonical private MCP reader carriers at the sibling paths `204_MCP/release_source_admission.py` and `204_MCP/selected_routes.py`, with their exact source bytes and modes included in the same verified package inventory.

## Details

- the canonical reader sources are the same two paths under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/`.
- package identity includes these rows, sorted by delivered path with the Tool rows. Copy and installed-package verification use the declared digest and mode; a missing, symlinked, changed or unverified dependency is a package failure.
- the sibling layout preserves the existing private reader import boundary. Packaging these library carriers does not register an MCP server, execute a Workflow, enable hooks, or grant mutation permission.
- Tool Packages without the Release reference-context reader retain their existing inventory contract.
