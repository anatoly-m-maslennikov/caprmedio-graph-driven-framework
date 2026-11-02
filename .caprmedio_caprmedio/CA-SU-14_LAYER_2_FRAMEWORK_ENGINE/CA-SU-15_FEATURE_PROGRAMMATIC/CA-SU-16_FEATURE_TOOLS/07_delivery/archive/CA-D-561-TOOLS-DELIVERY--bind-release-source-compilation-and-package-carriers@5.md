---
atom_id: CA-D-561
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-10 10:17:20 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Source and compilation carriers"
  depends_on: [Tool, Methodology, Projection, Manifest, Project Structure, Framework Settings, Framework Package, Installation, Journal, Source Carrier]
relations:
  delivery_for: [CA-R-1877, CA-R-1878, CA-M-331, CA-M-332, CA-M-362]
---
# Summary

Bind Release Version source, compilation, and package carriers

## Scope

The source-bound Methodology delivery and package-owned Tool-binding projections prepared for a release and installed from that exact admitted package.

## Claim

Release Version **must** bind its Methodology delivery and any package-owned Tool-binding projections to the explicitly admitted source snapshot and canonical compiler; the local root `methodology/` copy, binding projections and installed Applicable Methodology remain derived deliveries that preserve their original source relations, never replacement authoring authority or Action authorization.

## Details

### Candidate preparation

1. Compiler input is the canonical source snapshot named by `candidateSnapshotManifest`. Reuse `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py`; do not implement another conflict policy.
2. Candidate output occupies only `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/_release_materialized/<candidateSnapshotManifest.sha256>/` or the sealed private candidate's declared compiled child. Candidate preparation does not replace the currently installed projection.
3. The manifest binds source references/digests, derived-copy digest, compiler frontier, compiled bytes and exact before/after recursive authoring-source digests. Those authoring digests must match. The former `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources` copy is a derived delivery, not source authority; its delivery role is consolidated into root `methodology/`.
4. A new frozen export **must** retain an ordered `binding_atoms` frontier. Each member has exactly `atom_id`, positive integer `version`, safe Project-relative `source_path` and lowercase raw-source `sha256`. Selection is explicit and source-bound; neither the exporter nor a consumer hardcodes particular Atom IDs, Tool names or cardinality. Its complete eligible set is every current Active Delivery Atom in the exact admitted Project/control snapshot whose one closed `tool_binding.entrypoint` names a regular member of the sealed complete Framework Engine inventory. The frontier may be empty only when that derived eligible set is empty. Every eligible declaration is required exactly once; missing, duplicate, ambiguous, inactive, stale or additionally discovered eligible binding sources refuse before export. Historical frozen schemas remain read-only evidence and cannot silently supply an empty frontier for a new package.
5. Binding source bytes are private compiler input only. Reuse the canonical projection metadata formatter and source-preservation validator to emit one derived Carrier per pin under `methodology/bindings/`. Each projection preserves the exact source Atom ID, Version, raw SHA-256, original source path and original Relations digest, and its inverse after removal of the one canonical metadata insertion **must** equal the pinned raw bytes. The package never copies those active authority Carriers as authority and never obtains Action permission from a projection.

### Package-to-Project delivery

1. Reopen the admitted package inventory and catalog. A source descriptor may identify a directory tree, not only a file. Select only exact source identities admitted for this installation command. Presence or visibility is not activation of an Extension or Project Configuration.
2. Package role `methodology` below `methodology/active/` supplies selected Active Atom bytes; role `methodology-support` below `methodology/support/` supplies declared support; role `binding-projection` below `methodology/bindings/` supplies only the sealed non-authoritative Tool-binding projections. The mandatory Methodology descriptor covers `methodology/active/001_CORE_META_MODEL`; Extension descriptors cover distinct `002_INSTALLED_EXTENSIONS/<id>/<revision>` roots and a Configuration descriptor covers `003_PROJECT_CONFIGURATION`. Do not admit an ancestor `methodology/active` descriptor beside these nested identities. Every material row must have exactly one admitted descriptor; an admitted but unselected optional row is excluded, not treated as unadmitted. Strip only the active/support prefixes for the isolated compiler source view. Binding projections never enter that view. Refuse colliding destinations, missing selected revisions, extra unadmitted rows, symlinks and unsafe paths before publication.
3. Engine `core` descriptors are not compiler Atom input. Methodology, Extension and Configuration descriptors contribute only through explicitly selected admitted paths. Support remains support, not an Atom. Binding projections remain discovery metadata, not Methodology, Configuration, Extension or authoring source. Do not silently add checkout sources, installed settings or unselected private Configuration.
4. Reuse canonical compiler metadata, conflict/selection and projection rendering primitives on that exact view. Unresolved conflicts report actual evidence and stop; installation never invents approval. Reopen source-view, binding-projection and compilation bytes before publication.
5. A projected Methodology Atom retains source Atom ID, revision, source SHA-256 and original Relations digest. Its source-carrier relation resolves to the verified package member; its package-relative original export path preserves provenance. Relocation changes relative presentation, not source identity.

### Project-bound source export

1. A Project export receives its exact Project root explicitly. Resolve its control child, Methodology source root and canonical Framework Instance Settings through that Project's declared controls; the resolved source root must equal the requested source root. Never infer the Project by scanning ancestors or copying settings into the source tree.
2. Frozen export schema `caprmedio.methodology_export.frozen.v3` contains the v2 `project_binding` plus the closed `binding_atoms` frontier above. `project_binding` is either the explicit Project's resolved root, control/source paths and exact Project Settings, Project Structure and Framework Instance Settings carrier paths/digests, or `null` for a detached Core-only export. Record an absent optional Framework Instance Settings carrier explicitly so later creation changes the binding. These are derived input traces, not another settings or binding authority.
3. Freeze and reopen the Project binding, active source frontier and binding frontier together. Detect addition, removal or byte changes in any bound control or selected binding source before publication. The canonical compiler consumes the real external settings carrier without a nested copy or fallback. A detached export cannot select an Extension or Project Configuration or claim Project-specific applicability.
4. Historical frozen schemas v1 and v2 may be read only to validate retained historical ownership/evidence. They do not authorize a new Project-specific export, supply invented Project-binding fields or imply an empty binding frontier. Selected publication continues to copy its exact gated export and binding projections, not regenerate them.

### Target selection and preparation

1. Framework Instance Settings use the single canonical carrier declared by CA-D-359-CORE_META_MODEL--bind-framework-settings-to-its-authoritative-toml-carrier. Reuse the canonical compiler's explicit enabled Extension identity/revision parser. A selected label revision must match exactly one admitted Extension root; its catalog revision and receipt still bind immutable content.
2. The optional `[methodology.configuration]` table has exactly `identity` and `revision`. Both are strings and must match one admitted Configuration catalog descriptor, including its immutable catalog revision. Omission selects no package Project Configuration; it never selects the releasing Project's configuration by presence or catalog default. Binding projections are not selectable through this table. Malformed or unavailable selections refuse before command retention or installation effects. Alternative Configurations with colliding canonical destinations require an explicitly governed package layout, not implicit remapping.
3. Direct CA-O-200 installation privately prepares this target's compilation from only the selected admitted package bytes, before any destructive effect. Bind Framework Instance Settings, catalog, chosen source identities and the exact delivery manifest into the context and release proof. No compiler runs after deletion begins.
4. Selected CA-O-164/CA-O-169 promotion publishes the exact root `methodology/` export, binding projections and compiled output accepted by its Full Gate, without another compilation. Before publication, prove that its target selection equals that sealed candidate's source frontier. A different target selection uses a separately prepared direct installation, not a relabeled same-byte promotion.

### Gated publication

1. Resolve output from this Project's declared control child and Project Structure. The default exception is `<control_child>/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY`, not `_projection`.
2. After the same-byte Full Gate and explicit installation command, the shared installation lock owns publication of staged compiler role folders and their delivery manifest. Existing role folders are replaceable only when every persistent member proves compiler-projection ownership. Preserve unrelated files, settings, source folders and authoring authority.
3. Never replace the enclosing Framework directory or its `000_APPLICABLE_MTHD_sources` subtree. Require its authoring inventory to remain equal before and after. Delivery does not rewrite Project Structure.
4. Publish only the staged verified compilation and binding projections with exact package/source/compiler bindings. The runtime selector remains the installer's final activation step, after this delivery and the other required carriers are reopened. Discovery of a binding projection grants no execution authority; the designated direct Action still requires its own current source, command, Operator authorization, Run and Journal evidence. Journal evidence records actual publication or an honest partial/failed result.
