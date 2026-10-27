---
atom_id: CA-D-561@13
content_role: Delivery
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: Subject/Engineering/Release Version/Source Compilation and Package Carriers
  depends_on:
  - Subject/Engineering/Release Version
  - Subject/Domain/Node/Continuant/Selection//Methodology Sources
  - Subject/Domain/Node/Continuant/Projection
  - Manifest
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Framework Package
  - Installation
  - Subject/Engineering/Carrier/Journal Serialization
  - Subject/Engineering/Carrier/File Carrier
relations:
  delivery_for:
  - CA-R-1878
  - CA-M-332
  - CA-M-362
type: Eng Decision
tier: 3
---
# Summary

Bind Release Version source, compilation, and package carriers

## Scope

The Methodology sources, compilation and package copies used by direct local release, and the shared Methodology export helper.

## Claim

Release Version **must** bind Methodology delivery to its selected source inputs and the canonical compiler. The direct `101_FRAMEWORK_METHODOLOGY/` product, runtime package copies and any shared export remain derived deliveries that preserve their original source relations, never replacement authoring authority or Action authorization.

## Details

### Direct local release

1. Resolve the Project root and source roots through the Project's declared controls. Copy the selected Active sources into `101_FRAMEWORK_METHODOLOGY/sources/`; do not change the authoring sources or silently include unselected Configuration or Extensions.
2. Reuse `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py` and its existing selection, conflict and projection-rendering rules. Compile the copied sources into `101_FRAMEWORK_METHODOLOGY/applicable_methodology/`. An unresolved conflict stops compilation; delivery does not invent an approval.
3. Prepare the runtime package from those sources and compiled bytes under `METHODOLOGY/sources/` and `METHODOLOGY/compiled/`, following CA-D-562. Verify the prepared bytes before copying them to the declared destinations. The full release test suite, including required integration tests, precedes delivery.
4. Preserve the compiler's source Atom ID, Version, source path/digest and original Relations metadata. Relocation may change a relative link, not source identity. Binding projections remain discovery metadata, not Methodology authority or permission.
5. Resolve output paths through the declared Project structure. Refuse unsafe paths and collisions; replace only the intended derived destinations. Preserve settings, unrelated files and authoring sources. Delivery does not rewrite Project Structure.

### Shared Methodology export

The existing `methodology_export.py` and inventory helper remain reusable. Their frozen source/export format is not a required sealed-release package, a standalone installer, a runtime selector or a release admission gate.

1. A Project export receives its exact Project root explicitly. Resolve its control child, Methodology source root and canonical Framework Instance Settings through that Project's declared controls; the resolved source root must equal the requested source root. Never infer the Project by scanning ancestors or copying settings into the source tree.
2. Frozen export schema `caprmedio.methodology_export.frozen.v3` retains `project_binding`, `binding_atoms` and `framework_engine_inventory_sha256`. `project_binding` records the resolved Project root, control/source paths and exact Project Settings, Project Structure and Framework Instance Settings carrier paths/digests, or is `null` for detached Core-only input. Record an absent optional Framework Instance Settings carrier explicitly. These are derived input traces, not another settings authority.
3. Each `binding_atoms` member has exactly `atom_id`, positive integer `version`, safe Project-relative `source_path` and lowercase raw-source `sha256`. The complete eligible set is every current Active Delivery Atom in the selected Project/control snapshot whose one closed `tool_binding.entrypoint` names a regular member of the recorded complete Framework Engine inventory. Include every eligible declaration exactly once; refuse missing, duplicate, ambiguous, inactive, stale or additionally discovered eligible sources. Do not hardcode Atom IDs, Tool names or cardinality.
4. `framework_engine_inventory_sha256` is the lowercase SHA-256 of that complete inventory, or `null` only for detached Core-only input, whose binding frontier is empty. Reopen the Project controls, inventory and selected sources before export publication; refuse changed inputs. A detached input cannot select an Extension or Project Configuration or claim Project-specific applicability.
5. Binding source bytes are private compiler input. Reuse the canonical projection metadata formatter and source-preservation validator to emit a derived Carrier under `methodology/bindings/`. Preserve the exact source Atom ID, Version, raw SHA-256, original source path and original Relations digest. Removing the canonical metadata insertion must recover the exact pinned source bytes.
6. Freeze the selected Atom, support and catalog inputs and retain their inventory with the exported bytes. Support remains support; binding projections never become compiler Atom input. Preserve the authoring-source inventory before and after export. Historical frozen schemas v1/v2 remain read-only evidence and cannot authorize a new export or supply invented binding fields.

### Publication boundary

Direct local release uses its verified prepared product and runtime package. It does not require the retired reusable-package promotion, standalone installer, Full Gate, closed release registry or previous Journal records. Keep file/path checks and source-preservation checks at the copying boundary. Any Journal entry describes the actual publication or partial failure; it neither grants permission nor changes the real operation outcome.
