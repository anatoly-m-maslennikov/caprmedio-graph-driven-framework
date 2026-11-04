---
atom_id: CA-D-635
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
  passive:
  - CAPRMEDIO_MODEL <+ Projection.ID
  - CAPRMEDIO_MODEL <+ Projection.Form
  - CAPRMEDIO_MODEL <+ Projection.Scope Unit
  - CAPRMEDIO_MODEL <+ Projection.Source.Named Selection
  - CAPRMEDIO_MODEL <+ Projection.Source.Atoms
  - CAPRMEDIO_MODEL <+ Scope Unit
version: 17
updated_at: 2026-11-04 07:51:19 +0400
relations:
  depends_on:
  - CA-R-1943
  - CA-D-310
  - CA-D-550
tier: 4
role: Delivery
form: Decision
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
