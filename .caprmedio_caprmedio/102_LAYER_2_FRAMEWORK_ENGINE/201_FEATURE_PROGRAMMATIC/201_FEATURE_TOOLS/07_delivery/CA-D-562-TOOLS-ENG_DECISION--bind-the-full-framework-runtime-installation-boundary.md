---
atom_id: CA-D-562
content_role: Delivery
current_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 22
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Delivery
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History/Release.ID
  - Subject/Graph Node/Carrier
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Graph Node/Domain/Continuant/Projection
relations:
  delivery_for:
  - CA-R-1878
  - CA-M-332
type: Eng Decision
tier: 3
---
# Summary

Bind the full Framework runtime-installation boundary

## Scope

The installed Framework, local Engine/runtime package and project-local ca Skill delivered inside CA-O-164's local release and CA-O-169's final installation and Project-MCP refresh phase. These are deliveries of the same local release, not a separate installer operation.

## Claim

Local Release Version **must** prepare and verify the complete local Engine/runtime package, its bound `ca` Skill, the exact compiled `101_FRAMEWORK_METHODOLOGY/` product and the package-bound candidate Project-MCP image **before** destructive replacement of the installed Framework, runtime or project-local `ca` Skill. It then copies that verified product into `.caprmedio_caprmedio/000_CAPRMEDIO_framework/`, installs those same prepared package and Skill bytes at their governed runtime and project-local destinations, and refreshes the Project MCP using that verified image. It **must** preserve protected configuration, authoritative Project sources, existing Journal evidence and unrelated Project data. A failed or uncertain transition **must** stop with its actual observed state and no claim that a partial installation, unavailable MCP or unfinished cleanup completed successfully.

## Details

### Local delivery carriers

After normal source/input/file-safety checks, the full test suite including required integration tests and canonical compilation under CA-O-164, the verified derived product is `101_FRAMEWORK_METHODOLOGY/`; the installed Framework copy is `.caprmedio_caprmedio/000_CAPRMEDIO_framework/`. Prepare and verify the complete replacement package before clearing any installed Framework, runtime or Skill target; a preparation or verification failure leaves those installed targets untouched. Under the existing one Project installation lock required by CA-O-169, clear only replaceable delivery members at the declared destinations and copy the verified product as-is. Reopen the actual installed Framework, runtime and complete Skill deliveries against the prepared paths, bytes and modes before reporting installation success. Neither derived nor installed content becomes authoring authority. Release verification adds no separate Active Atom metadata, placement or relation validation; the full test suite and normal input, permission and file/path safety checks remain. Required Docker integration tests build a disposable image from the current code; an old installed or running image is not a substitute, and test execution does not restart the running Project MCP.

Prepare the direct local package in a component-owned, Run-specific descendant of the configured Project Temporary State root under `.caprmedio_tmp/`, following CA-M-422; staging is not a persistent installation root. It carries the complete `102_FRAMEWORK_ENGINE/`, the product's sources and compilation at `METHODOLOGY/sources/` and `METHODOLOGY/compiled/`, the complete canonical `ca` payload at `SKILLS/ca/`, and `pyproject.toml`, `uv.lock` and `version.toml`. Install those same prepared bytes at the governed persistent Project runtime package destination outside temporary state; install its complete `SKILLS/ca/` payload at `.agents/skills/ca/` and refresh the package-bound Project MCP bootstrap. This Delivery does not introduce a new persistent MCP path. Compilation and source lineage remain governed by CA-D-561; this Delivery adds no export or binding-projection schema.

The prepared runtime supplies the Project-MCP launcher and Docker image inputs. Build or reuse and verify the package-bound candidate image in the same Workflow before any installed target is cleared. Final installation delivers the prepared bytes, then restarts or reuses the Project MCP with that image for CA-O-169's startup/smoke check; it does not defer image preparation until after replacement. A successful build alone does not prove a working Project MCP. This direct flow requires no candidate-snapshot manifest, retained Full Gate, selected-N execution gate, N+1 promotion, native runtime selector, state-generation proof or bootstrap image-restoration prerequisite.

Fresh local-release image builds record exact Project ownership with `org.caprmedio.project` (selected instance ID), `org.caprmedio.control_root` (relative control directory) and `org.caprmedio.host_project_root` (canonical owning repository root), plus canonical Settings `project.name` in `org.caprmedio.project.name` and the full build-time owning-repository Git HEAD commit ID in `org.caprmedio.source.head_commit`. Verify those labels by inspecting the built image; missing or invalid Project name or HEAD refuses fresh preparation before building. Name and HEAD are provenance, not ownership gates or proof of a clean checkout or exact built source tree; the runtime source fingerprint and inspected immutable image ID remain the code-identity checks. Preserve existing cache reuse: an admitted cached image is not rebuilt merely to add labels, and reuse does not add or transfer ownership. Matching inspected exact ownership labels can identify newly labelled orphan images for bounded cleanup; old unlabelled or otherwise unproven images remain retained and reported.

### Preservation and failure boundary

Keep Settings, runtime configuration, Project Structure, Operator registry, authoritative source carriers, existing Journal and retained evidence outside replacement. Preserve the protected configuration members already present in the derived and installed roots; do not overwrite them from the product. Source and destination paths must remain safe Project-contained regular trees, not symlink aliases. Unrelated Project files, Skills, user directories and other Projects are not replacement targets. Existing ignored Finder metadata and environment carriers remain outside the delivered payload and are not removed by cleanup.

Actual failure reports retain the failed phase and observed result for manual inspection before any separately authorized retry; a report or Journal entry does not prove completion or fabricate a Workflow, approval or earlier event. Plain Journal append/read preserves supplied actual observations without baseline, prior-history, chain, validation, receipt, deduplication, retry or recovery prerequisites; logging I/O failure does not change the independently observed source-effect outcome. This Delivery imposes no new Journal row count or recovery protocol and does not authorize replay of an unknown effect.

Cleanup covers accumulated obsolete release-owned containers and images for this Project, not only the immediate predecessor. Before Project-MCP startup, remove only proven obsolete stopped Project-owned containers; after verified installation and successful startup/smoke, repeat that cleanup and remove proven obsolete images no longer retained by any container or protected reference. Preserve all images and containers carrying the verified current code. A prior Project-MCP container may be stopped and removed only through the existing exact Project-ownership replacement checks; accumulated cleanup preserves other running containers. Unknown ownership or code identity, unavailable inspection, protected use or failed removal retains the target and reports cleanup pending, including unproven orphan images. Tags and version age alone are not proof. Never force-delete containers, remove unrelated or other-Project resources or prune globally. Successful installation does not falsely imply completed cleanup.
