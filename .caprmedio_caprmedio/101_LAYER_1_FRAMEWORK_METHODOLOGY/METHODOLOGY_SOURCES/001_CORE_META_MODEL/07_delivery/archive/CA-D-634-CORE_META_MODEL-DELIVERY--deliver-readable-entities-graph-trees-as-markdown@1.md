---
atom_id: CA-D-634
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Projection/Type: Entities Graph"
  depends_on: [Entity, Relation, Atom, Projection]
version: 1
updated_at: "2026-10-15 18:42:08 +0400"
relations:
  depends_on: [CA-R-1456, CA-D-310, CA-D-550]
---
# Summary

Deliver readable Entities Graph trees as Markdown

## Scope

The readable Entities Graph tree-view Carrier.

## Claim

Deliver the view as a UTF-8 Markdown file under the Project's declared Projection root. Include YAML frontmatter and tab-indented trees inside fenced text blocks.

## Details

Use these frontmatter fields:

- `artifact_form: Projection`
- `type: Entities Graph`
- `updated_at`: actual latest completed rebuild time in Project time, with an explicit UTC offset, under CA-D-310.
- `sources`: the complete deduplicated list of contributing Atom references in `CA-N-123@M` form, where N is the Content Role letter and M is the numeric Version. Sort the references alphabetically. This is the Projection's source list, not its Atom ID.

Declare the requested source selection and any narrower display selection in the document. When non-Atom sources also contribute, identify their exact source evidence separately; do not invent Atom IDs for them.

Body order:

1. `## Inherency tree`
   - `### Primary entities`: main tree without dependents.
   - One `### <qualified entity name>` section per primary entity with dependents, in first-appearance order from the main tree.
2. `## Construction tree`: separate CONTAINS view.

Use one literal tab per tree depth inside fenced `text` blocks. Use spaces, not tabs, for YAML indentation. Keep readable entity names, not YAML storage-key spellings. Preserve relation distinctions with the admitted compact notation or explicit relation labels; indentation alone must not erase edge meaning. Preserve declared cardinality beside the relevant containment edge.

A source-derived tree remains a Projection, not a new source of truth. This format does not require changing unrelated graph exports.
