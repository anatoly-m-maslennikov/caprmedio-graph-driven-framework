---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Projection/Type: Subject Graph'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Domain/Continuant/Projection/Type
  - Subject/Graph Node/Domain/Continuant/Projection/Selection
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.ID
  - Subject/Graph Node/Domain/Continuant/Atom.Version Number
  - Subject/Graph Node/Carrier
version: 8
updated_at: 2026-10-27 06:04:45 +0400
relations:
  delivery_for:
  - CA-R-2150
atom_id: CA-D-653@8
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

The Markdown body has exactly four main sections:

1. ## Primary subjects: one literal-tab hierarchy rooted at Subject, with kinds only. Exclude named instances, dependent properties, allowed property values and their descendants. Keep the Graph Node, Graph Relation and Graph Rule structure; named Relation Type declarations belong in section 3, not the primary tree.
2. ## Properties: one ### <full primary Subject Path> section for every primary with at least one direct or inherited property, following its first appearance in section 1. Show direct properties and additive source-backed inherited properties and allowed values. Mark each inherited entry as [inherited from <canonical Subject>]. Keep all origins for equal-name entries; report conflicts without silently overriding a source. Do not copy inherited properties into source Atoms.
3. ## Instances: show the selected named instances separately from their kinds, including Workflow instances, named Relation Type declarations and concrete Graph Rule Atoms. Retain the instance's defining kind, actual name and source-backed detail. Concrete Graph Rules retain their source Atom ID/Version and YAML `claim.*` mapping. This section is the named declaration level, not the actual Atom-to-Atom Relation tuples. Explicitly report unavailable or unsupported declaration details rather than guessing or omitting them.

4. ## Dependency-only subjects: list each exact canonical Subject path that occurs in subjects.depends_on and never explicitly in subjects.governs within this view's selected source Atoms. Use exact complete-string equality without propagating ancestors or descendants. Show each path once with its sorted, deduplicated referring Atom IDs, sorting paths alphabetically. Keep the other sections intact; this report does not move or remove their targets or infer a missing-definition violation.

Use spaces, not tabs, for YAML frontmatter indentation and literal tabs for hierarchy depth inside fenced text blocks. Each tree line shows its local label and incoming operator, without a repeated full path or a space after the operator. Full primary paths remain in property-section headings and inherited-origin marks for context. Keep /, ., :, and // distinct. Render all present source-backed instances in section 3; do not limit it to Workflow instances if other kinds are present. Preserve source-declared order where present, otherwise sort alphabetically. No Terms Graph, construction tree, instance link graph or other main section is added.

The source Atoms remain authoritative for target and property identity. The Projection does not create a separate Revision entity, infer values from filenames or folders, change source authority, or require any Tool, MCP route, runtime namespace, or code-support gate.
