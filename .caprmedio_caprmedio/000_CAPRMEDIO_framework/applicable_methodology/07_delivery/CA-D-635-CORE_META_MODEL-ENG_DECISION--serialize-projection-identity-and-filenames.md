---
atom_id: CA-D-635
ref_id: CA-D-635
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
  dependencies:
  - CAPRMEDIO_MODEL <+ Projection.ID
  - CAPRMEDIO_MODEL <+ Projection.Form
  - CAPRMEDIO_MODEL <+ Projection.Scope Unit
  - CAPRMEDIO_MODEL <+ Projection.Source.Named Selection
  - CAPRMEDIO_MODEL <+ Projection.Source.Atoms
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 4
relations:
  depends_on:
  - CA-R-1943
  - CA-D-310
  - CA-D-550
status: Active
version: 17
updated_at: 2026-11-04 07:51:19 +0400
carrier_destination:
  file:
    name: CA-D-635-CORE_META_MODEL-DECISION--serialize-projection-identity-and-filenames.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-635-CORE_META_MODEL-ENG_DECISION--serialize-projection-identity-and-filenames.md
  source_atom_id: CA-D-635
  source_atom_revision: 17
  source_sha256: bb89db55454c90f77d3120e220bf5593c0bf73d8f3380a8f41bf491afe67be1e
  original_relations_sha256: d43f4bf4aabcc9f4b50a5498062a151d8142ac5fb8e67e0e2cde8894a4b819fd
---
## Summary

Serialize Projection identity and filenames

## Claim

### Prose Claim


Projection Markdown File Carriers.


Use this filename:

`<PROJECT_PREFIX>-PROJ-<ID>-<CURRENT_SCOPE_NAME>--<PROJECTION_FORM>--<NAMED_SELECTION>.md`

Store the full Projection ID as `projection_id` in YAML frontmatter. The filename and frontmatter must identify the same Projection.

## Details

For this Project, the prefix is `CA`. For example:

`CA-PROJ-001-CORE_META_MODEL--Entities-Graph--Current-Atoms.md`

Its full Projection ID is `CA-PROJ-001`; `001` is the ID segment in the filename. Use the current Scope Unit name, not its label.

The YAML frontmatter carries:

- `artifact_form: Projection`
- `projection_id`: the full Projection ID.
- `form`: Projection Form.
- `scope_unit`: the reference to the one Scope Unit of the Projection; for a Project-root Projection in caprmedio, `Project//caprmedio`.
- `source.named_selection`: the named source selection.
- `source.atoms`: contributing Atom references with explicit Versions, such as `CA-R-123@3`, when recorded. Identify contributing non-Atom sources separately; do not invent Atom IDs for them.
- `updated_at`: the latest completed rebuild time under CA-D-310.

Keep the ID under CA-R-1943 when rebuilding or changing only the Scope Unit name or Carrier path. Filename changes, including changes to the Named Selection, do not by themselves create a new Projection. Form and Scope Unit determine identity under CA-R-1943.

Form-specific Delivery rules define the body and any additional source evidence. Store the Carrier under the applicable Projection root under CA-D-550.
