---
atom_id: CA-D-586
ref_id: CA-D-586
role: Delivery
current_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-11-02 19:46:47 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/File
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Package
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Module
form: Eng Decision
tier: 3
container:
  scope_unit: CA-SU-16
carrier_destination:
  file:
    name: CA-D-586-TOOLS-ENG_DECISION--package-the-release-tool-private-reader-closure.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/07_delivery
---
# Summary

Package the Release Tool private reader closure

## Scope

The private reader dependency delivery of a content-addressed Tool Package containing the Release suite reference-context reader.

## Claim

A Tool Package containing `TOOLS/RELEASE_VERSION/release_suite_reference_context.py` **must** include its two canonical private MCP reader carriers at the sibling paths `204_MCP/release_source_admission.py` and `204_MCP/selected_routes.py`, with their exact source bytes and modes included in the same verified package inventory.

## Details

- the canonical reader sources are the same two paths under `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/`.
- package identity includes these rows, sorted by delivered path with the Tool rows. Copy and installed-package verification use the declared digest and mode; a missing, symlinked, changed or unverified dependency is a package failure.
- the sibling layout preserves the existing private reader import boundary. Packaging these library carriers does not register an MCP server, execute a Workflow, enable hooks, or grant mutation permission.
- Tool Packages without the Release reference-context reader retain their existing inventory contract.
