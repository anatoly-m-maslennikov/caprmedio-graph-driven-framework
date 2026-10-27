---
atom_id: CA-D-634
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Projection/Type: Entities Graph'
  depends_on:
  - Subject/Graph Node
  - Subject/Graph Relation
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Projection
version: 16
updated_at: 2026-10-26 17:20:40 +0400
relations:
  depends_on:
  - CA-R-1456
  - CA-D-310
  - CA-D-550
  - CA-D-635
tier: 5
type: Eng Decision
---
# Summary

Deliver readable Entities Graph trees as Markdown

## Scope

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

The selected Relation Type and Graph Rule declaration view uses the same Entities Graph Type, with its own named selection and stable Projection ID under CA-R-1943. Reuse the filename and YAML identity fields under CA-D-635. Keep Core and Project source selections, coverage and provenance separate. The Inherency body order above applies to the structural tree view; use this order for the declaration view:

1. `## Relation Types`: one record per selected project-shared canonical Type name. Render its source-backed defining Claim and optional Type semantics in a fenced text block with one literal tab per display depth.
2. `## Graph Rules`: one record per concrete source Rule, identified by its source Atom ID/Version. Include its readable Summary, governed Subject and the source's operative frontmatter `claim.*` mapping rendered as source YAML.
3. `## Source limitations`: unresolved identity, missing or conflicting metadata, unsupported schemas and other evidenced coverage gaps. State explicitly when the selected concrete Rule catalogue is empty.

For each Relation Type, render its project-unique canonical name and meaning from the defining R Claim, together with any explicitly relevant direct direction, inverse, derivation, or transitivity semantics. Retain exact defining source ID/Version and Claim/Revision traceability. Show an unavailable or unresolved value as an explicit gap with its source evidence; do not invent a value or infer direction from name spelling. Any selected Graph Rule admission, endpoint graph contexts, endpoint restrictions and cardinality are rendered as separate Graph Rule declarations and are not copied into Type metadata. Relation Type Status is not a Type field; the defining Atom carries Status.

Preserve operative Rule YAML from the source frontmatter `claim.*` mapping under CA-D-637, including opaque values; do not convert it to a new schema, normalize it, evaluate it or fill missing semantics. Render that mapping as source YAML without requiring a fenced Markdown body; readable text trees use literal tabs. Do not serialize actual Atom-to-Atom relations tuples as the requested declarations, or turn illustrative YAML into a live Rule.

Retain the existing actual rebuild timestamp, complete contributing source list and source/display selection requirements. This view is derived evidence, not a second source of truth or a claim that unexamined authority is complete.

Construction/CONTAINS projection is deferred to the adjacent `draft/` RMED. It is not required by this active readable-view specification.
