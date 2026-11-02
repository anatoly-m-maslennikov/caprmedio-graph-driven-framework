---
atom_id: CA-D-561
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-10 05:17:00 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Source and compilation carriers"
  depends_on: [Tool, Methodology, Projection, Manifest, Project Structure, Framework Settings, Framework Package, Installation, Journal]
relations:
  delivery_for: [CA-R-1877, CA-R-1878, CA-M-331, CA-M-332, CA-M-362]
---
# Summary

Bind Release Version source, compilation, and package carriers

## Scope

The source-bound Methodology delivery prepared for a release and installed from that exact admitted package.

## Claim

Release Version **must** bind its Methodology delivery to the explicitly admitted source snapshot and canonical compiler; the local root `methodology/` copy and the installed Applicable Methodology remain derived deliveries that preserve their original source relations, never replacement authoring authority.

## Details

### Candidate preparation

1. Compiler input is the canonical source snapshot named by `candidateSnapshotManifest`. Reuse `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py`; do not implement another conflict policy.
2. Candidate output occupies only `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/_release_materialized/<candidateSnapshotManifest.sha256>/` or the sealed private candidate's declared compiled child. Candidate preparation does not replace the currently installed projection.
3. The manifest binds source references/digests, derived-copy digest, compiler frontier, compiled bytes and exact before/after recursive authoring-source digests. Those authoring digests must match. The former `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources` copy is a derived delivery, not source authority; its delivery role is consolidated into root `methodology/`.

### Package-to-Project delivery

1. Reopen the admitted package inventory and catalog. A source descriptor may identify a directory tree, not only a file. Select only exact source identities admitted for this installation command. Presence or visibility is not activation of an Extension or Project Configuration.
2. Package role `methodology` below `methodology/active/` supplies selected Active Atom bytes; role `methodology-support` below `methodology/support/` supplies declared support. Strip only these fixed prefixes for the isolated compiler source view. Refuse colliding destinations, missing selected revisions, extra unadmitted rows, symlinks and unsafe paths before publication.
3. Engine `core` descriptors are not compiler Atom input. Methodology, Extension and Configuration descriptors contribute only through explicitly selected admitted paths. Support remains support, not an Atom. Do not silently add checkout sources, installed settings or unselected private Configuration.
4. Reuse canonical compiler metadata, conflict/selection and projection rendering primitives on that exact view. Unresolved conflicts report actual evidence and stop; installation never invents approval. Reopen source-view and compilation bytes before publication.
5. A projected Atom retains source Atom ID, revision, source SHA-256 and original Relations digest. Its source-carrier relation resolves to the verified package member; its package-relative original export path preserves provenance. Relocation changes relative presentation, not source identity.

### Gated publication

1. Resolve output from this Project's declared control child and Project Structure. The default exception is `<control_child>/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY`, not `_projection`.
2. After the same-byte Full Gate and explicit installation command, the shared installation lock owns publication of staged compiler role folders and their delivery manifest. Existing role folders are replaceable only when every persistent member proves compiler-projection ownership. Preserve unrelated files, settings, source folders and authoring authority.
3. Never replace the enclosing Framework directory or its `000_APPLICABLE_MTHD_sources` subtree. Require its authoring inventory to remain equal before and after. Delivery does not rewrite Project Structure.
4. Publish only the staged verified compilation with exact package/source/compiler bindings. The runtime selector remains the installer's final activation step, after this delivery and the other required carriers are reopened. Journal evidence records actual publication or an honest partial/failed result.

