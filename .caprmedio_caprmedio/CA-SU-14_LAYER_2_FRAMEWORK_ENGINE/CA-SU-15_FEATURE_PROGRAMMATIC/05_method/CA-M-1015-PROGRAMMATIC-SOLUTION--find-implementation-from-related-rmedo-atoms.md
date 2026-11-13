---
identity:
  atom_id: CA-M-1015
  ref_id: CA-M-1015
context:
  role: method
  form: solution
  container:
    scope_unit: CA-SU-15
  tier: 2
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Traceability
state:
  version: 1
  status: active
  updated_at: '2026-11-13T12:16:36.432687+00:00'
destination:
  file:
    name: CA-M-1015-PROGRAMMATIC-SOLUTION--find-implementation-from-related-rmedo-atoms.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
---
## Summary

Find implementation from related RMEDO Atoms

## Claim scope

Finding code to inspect before implementing a new or changed RMEDO Atom. The pilot indexes WORKBENCH, WORKBENCH_BACKEND and WORKBENCH_FRONTEND, with ancestor Packages included for containment. The synthetic benchmark corpus and Codex extension are outside the pilot.

## Claim

### Prose Claim

Index Package `<folder name>.p.spec_trace.md` and Module `<full module filename with extension>.spec_trace.md` files under the Project’s Implementation root. Resolve each spec reference by its owner kind and path so a same-named Package and Module remain distinct. For the pilot, discover Python, Svelte, TypeScript and JavaScript source and test files as Modules and their containing directories as Packages. Skip generated files and directories. Exclude Assets and individual golden corpus files from the implementation trace inventory. Index a corpus-level Evaluation pin from its owning Package’s spec trace. Expose the Implementation structure and its RMEDO pins through `query_schema` and read-only `query_run`:

- `implementation_objects` lists every Package and Module by Project-relative path and kind, including those with no sidecar or pins. Every Module and every Package below the Project Package has exactly one immediate container, which is a Package. The Project Package is the Implementation root and has no container.
- `implementation_rmedo` lists each sidecar entry by owner path, Project-relative sidecar path, entry kind, Atom ID, and exact Version. The owner path refers to an object in `implementation_objects`. Index every pin in a valid sidecar, including pins to non-Current versions. Pins remain queryable when the referenced Archive bodies are unloaded.

A package lookup follows containment to include pins from its descendant packages and modules. Sidecars identify pins for the owner at their location. The owner’s container comes from the Implementation structure. SQL can find Modules and Packages with zero direct `implements` pins. For a Package, the same lookup can also check whether its entire subtree has zero `implements` pins. `applies` pins do not count as implementation coverage.

Reuse the Atom watcher’s event handling under the Implementation root. Index the existing Packages, Modules and sidecars at startup. Track Package and Module creation, moves, renames and deletion even when there is no sidecar. Track sidecar edits as well as creation, moves, renames and deletion. Refresh only affected object and pin rows during ordinary changes. On a move or rename, remove the old rows and index the new location. On deletion, remove the affected rows. If a sidecar cannot be read or parsed, exclude its rows and report the path and error. A full reread rebuilds the Implementation structure and its pin rows.

Given a target Atom, find code through three independent searches:

- Same Scope Unit. Use implemented Atoms owned directly by that Scope Unit to find its package and modules.
- Same main subject. Use Atoms with the same main subject to find related implementations across the Project.
- Atom dependencies. Follow the target's direct dependency links to the referenced Atoms and find their implementation owners. Resolve the exact Version when the relation specifies it.

Return each matching package or module once and show which search found it. Show applicable Package Engineering Standards separately from implementation owners. A candidate path is a place to inspect. It does not establish that the target is already implemented.

## Details

Spec traces describe the existing implementation and are the authored source for its recorded links. The runtime table and search results are derived. Deriving implementation links for Spec Policies and Solutions is deferred. Report a pin as missing only when its exact version is known to be absent. Unloaded Archive coverage leaves resolution unverified. Report Scope Units with no mapped owners. Use the same current Project selection for Atom and implementation lookups. Use SQL joins over the existing Atom and relation data and the two trace tables for the three searches.