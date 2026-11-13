---
identity:
  atom_id: CA-P-3029
  ref_id: CA-P-3029
context:
  role: plan
  form: Plan
  label: Epic
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T16:28:00.030685+00:00'
destination:
  file:
    name: CA-P-3029-EPIC--mcp-query-and-atom-lifecycle-refinement.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan
---
## Summary

MCP query and atom lifecycle refinement

## Objective

Apply the decisions from the 36 Code Synopses reviewed after CA-P-2791. Each Task links its source Synopses and updates RMEDO, reviews and fixes RMEDO, then implements the reviewed RMEDO.

## Decision record

- Public Release gets the existing or draft PR URL before the push. Stop before pushing if a draft cannot be created from the published branch. Put the main PR URL in Version History, order releases newest first, and use New and Fixed in PR material. Push the exact tested commit once, report its SHA and the PR URL, verify the PR head, then mark it ready for CI auto-merge. Keep concurrent checkout edits out of the release.
- Local Release runs the full test suite before building or replacing MCP. Confirm the expected image is healthy, then retain the live image and one previous known-good Project image. Remove only older Project-owned images. Verify successful copy operations and runtime readiness from the single release source. The package is the full tested Project tree outside .caprmedio_<project name>, .caprmedio_runtime, .caprmedio_tmp, and technical temp directories. Bind the selected image digest and source fingerprint, stop on checkout change, and enforce existing build and startup timeouts. Use the existing Project temporary staging policy.
- MCP lists started nonterminal Workflow Runs for the caller session by default and supports an explicit Project-wide list. An Actor can continue or cancel by Run ID across sessions. Retain valid fields after invalid or unknown input and return field-level feedback. Reopening an Epic changes its own status. Archived, Done, and Canceled Plan containers accept no new child Plans. Concurrent edits to the same Atom stop conflicting Runs. Select one eligible carrier through Workbench, read it once, and stop on a stale or invalid file. An independent Draft copy gets a fresh ID at Version 1 and retains all source relations unless explicitly changed.
- Use one Settings read/write adapter. Use the previous ready image for declaration refresh, with the existing first-refresh and existing-assets paths. Save all graph Projections by default and select Atom data through Workbench. CA-P-3022 owns Python model-engine adoption and CFEL retirement.
- Workbench reread restores selected Archive coverage. Ordinary indexing stays incremental. Put Project API operations beneath /caprmedio/{project}/api/{operation} and keep old Workbench routes as aliases. Status reports Archive coverage and audit state. Keep density separate from Workspace identity. Check shows Valid, Invalid, or Not checked according to the current SQL. If browser storage fails, keep edits in memory and warn that reload or close can lose them. Grid Evaluation uses one complete query.
- MCP exposes usage through tools/list. Keep submitted SQL out of public diagnostics. Return Status only for successful single-Atom lifecycle writes and report actual outcomes to health. Use typed error categories and preserve primary and secondary diagnostic failures. Return a saved ID with a configured link when available, or a null URL and a machine-readable reason.

## Definition of Done

All linked Synopses have an implementation or a verified disposition. The two checkout lifecycle fixes are verified on the deployed MCP. Each in-scope Task records its RMEDO review and implementation checks.
