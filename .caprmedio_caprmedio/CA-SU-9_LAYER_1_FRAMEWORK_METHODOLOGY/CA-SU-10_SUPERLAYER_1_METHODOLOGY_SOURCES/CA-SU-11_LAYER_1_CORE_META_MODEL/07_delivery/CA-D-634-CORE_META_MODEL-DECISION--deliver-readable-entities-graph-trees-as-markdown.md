---
atom_id: CA-D-634
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Projection/(.Form:=Entities Graph)
  passive:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Projection
version: 23
updated_at: 2026-11-02 08:06:47 +0400
relations:
  depends_on:
  - CA-R-1456
  - CA-D-310
  - CA-D-550
  - CA-D-635
tier: 5
role: Delivery
form: Decision
---
## Summary

Deliver readable Entities Graph trees as Markdown

## Claim scope

The Markdown Carriers for readable Entities Graph structural and named declaration views.

## Claim

Deliver the view as a UTF-8 Markdown file under the Project's declared Projection root. Include YAML frontmatter and tab-indented trees inside fenced text blocks.

## Details

Use these frontmatter fields:

- `artifact_form: Projection`
- `projection_id`, `named_selection` and `source_of_truth`: under CA-D-635. Use its filename convention and retain the Projection ID under CA-R-1943.
- `type: Entities Graph`
- `updated_at`: actual latest completed rebuild time in Project time, with an explicit UTC offset, under CA-D-310.
- `sources`: the complete deduplicated list of contributing Atom references in `CA-N-123@M` form, where N is the Content Role letter and M is the numeric Version. Sort the references alphabetically. This is the Projection's source list, not its Atom ID.

Declare the requested source selection and any narrower display selection in the document. When non-Atom sources also contribute, identify their exact source evidence separately; do not invent Atom IDs for them.

Inherency view body order:

1. `## Inherency tree`
   - `### Primary entities`: main tree without dependents.
   - One `### <qualified entity name>` section per primary entity with dependents, in first-appearance order from the main tree.

Use one literal tab per tree depth inside fenced `text` blocks. Use spaces, not tabs, for YAML indentation. Keep readable entity names, not YAML storage-key spellings. Preserve relation distinctions with the admitted compact notation or explicit relation labels; indentation alone must not erase edge meaning.

A source-derived tree remains a Projection, not a new source of truth. This format does not require changing unrelated graph exports.

### Declaration-view delivery

The selected Relation Type declaration view uses the same Entities Graph Type, its own named selection and a stable Projection ID under CA-R-1943. Reuse CA-D-635's filename and YAML fields. Render named Relation Types with defining Atom IDs, their meanings and explicitly declared direction, inverse, derivation or transitivity. The defining Atom has Status; the Relation Type has no Status field. Do not turn actual endpoint tuples into Type declarations.

The model views contain primary entities, then one property section per primary entity with properties, including inherited properties marked `[inherited]`. Keep primary-kind definition references as Atom IDs rather than copied definition text. Source-declared containment and specialization retain their distinct operators; use spaces around the complete containment operator, for example `>{1+} Atom/Content Role: Operations/Type: Step`.

Report missing definitions, unresolved identities, unsupported source syntax and coverage limits explicitly. Do not create a separate Graph Rule instance catalogue or render retired frontmatter `claim.*` grammar. Constraints and simple formal expressions belong to the corresponding Entity Definitions. Keep source selection, complete contributing source versions and actual rebuild timestamp in every Projection.
