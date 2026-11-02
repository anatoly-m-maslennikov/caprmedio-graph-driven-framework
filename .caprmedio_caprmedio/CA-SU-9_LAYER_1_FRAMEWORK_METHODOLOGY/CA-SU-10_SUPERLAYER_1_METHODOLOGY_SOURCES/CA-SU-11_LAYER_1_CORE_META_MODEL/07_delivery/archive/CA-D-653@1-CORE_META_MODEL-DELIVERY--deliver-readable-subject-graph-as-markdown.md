---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Subject Graph'
  depends_on:
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Projection/Type
  - Subject/Domain/Node/Continuant/Projection/Selection
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.ID
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Subject/Engineering/Carrier
version: 1
updated_at: 2026-10-24 00:07:46 +0400
relations:
  delivery_for:
  - CA-R-2150
atom_id: CA-D-653@1
content_role: Delivery
type: Eng Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 3
status: Archived
author: Anatoly Maslennikov
---
# Summary

Deliver readable Subject Graph views as Markdown

## Scope

The Markdown Projection Carriers for a readable Subject Graph from the named Current RMEDO source selection.

## Claim

Deliver each selected Subject Graph as a UTF-8 Markdown Projection Carrier under the Project's declared Projection root. The Carrier reuses the existing Projection identity, filename, timestamp, and source-list format while rendering only the selected Subject Target hierarchy with per-primary property sections. This Delivery is Tier 3 in CORE_META_MODEL and delivers the Tier 1 definition CA-R-2150 in that same Scope Unit.

## Details

The Carrier frontmatter must carry:

- artifact_form: Projection.
- projection_id, named_selection, and source_of_truth under the existing Projection identity and filename policy. A different Projection Type or named source selection requires its own stable Projection ID; an Entities Graph ID is not reused for this Subject Graph.
- type: Subject Graph.
- updated_at as the actual latest completed rebuild time with an explicit offset.
- sources as the complete sorted, deduplicated list of contributing Current RMEDO Atom IDs with Versions in CA-N@M form. This YAML source list is the full provenance; the Markdown body does not repeat it as per-Atom link rows.

The named selection is Current RMEDO: current Requirement, Method, Evaluation, Delivery, and Operations source Atoms after approved missing-Status normalization. Concern, Analysis, Plan, Draft, Archived, and derived Projection material are excluded. Unresolved, malformed, inaccessible, or conflicting source claims remain visible as explicit limitations; none is silently converted into authority.

The Markdown body has only this layout:

1. ## Subject tree, with ### Primary subjects and one literal-tab hierarchy rooted at Subject. The /, ., :, and // operators remain distinct and are preserved as the programmatic hierarchy boundaries.
2. One ### <primary Subject Path> section per primary target, with a #### Properties subsection containing only selected source-backed property names and values.

Use spaces, not tabs, for YAML indentation and literal tabs for hierarchy depth inside fenced text blocks. Do not add per-Atom link lists, a term-oriented graph, a construction tree, a relation-type catalogue, or any other section beyond the primary tree and property sections. The native Entities Graph remains a separate Projection Type and delivery.

The source Atoms remain authoritative for target and property identity. The Projection does not create a separate Revision entity, infer values from filenames or folders, change source authority, or require any Tool, MCP route, runtime namespace, or code-support gate.
