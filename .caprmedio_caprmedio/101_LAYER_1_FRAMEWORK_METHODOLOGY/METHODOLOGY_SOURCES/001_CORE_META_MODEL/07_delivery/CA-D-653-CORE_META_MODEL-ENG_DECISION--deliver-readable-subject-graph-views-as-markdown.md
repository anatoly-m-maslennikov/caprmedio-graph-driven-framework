---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.ID
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Version Number
  - Subject/CAPRMEDIO/Carrier
version: 11
updated_at: 2026-10-27 23:53:05 +0400
relations:
  delivery_for:
  - CA-R-2150
  - CA-R-2221
  - CA-R-2222
  - CA-R-2223
  - CA-R-2224
  - CA-R-2225
atom_id: CA-D-653
content_role: Delivery
type: Eng Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 3
status: Active
author: Anatoly Maslennikov
---
# Summary

Deliver readable Subject Graph views as Markdown

## Scope

Markdown Carriers for the combined and focused Subject Graph Projection Types, under their declared Current RMEDO selections.

## Claim

Deliver each selected Subject Graph as a UTF-8 Markdown Projection Carrier under the Project's declared Projection root. The Carrier reuses the existing Projection identity, filename, timestamp, and source-list format while rendering the content defined by its exact registered Projection Type. This Delivery is Tier 3 in CORE_META_MODEL and delivers the Tier 1 definition CA-R-2150 in that same Scope Unit.

## Details

The Carrier frontmatter must carry:

- artifact_form: Projection.
- projection_id, named_selection, and source_of_truth under the existing Projection identity and filename policy. A different Projection Type or named source selection requires its own stable Projection ID; an Entities Graph ID is not reused for this Subject Graph.
- type: the exact registered combined or focused Subject Graph Projection Type.
- updated_at as the actual latest completed rebuild time with an explicit offset.
- sources as the complete sorted, deduplicated list of contributing Current RMEDO Atom IDs with Versions in CA-N@M form. This YAML source list is the full provenance; the Markdown body does not repeat it as per-Atom link rows.

The named selection is Current RMEDO: current Requirement, Method, Evaluation, Delivery, and Operations source Atoms after approved missing-Status normalization. Concern, Analysis, Plan, Draft, Archived, and derived Projection material are excluded. Unresolved, malformed, inaccessible, or conflicting source claims remain visible as explicit limitations; none is silently converted into authority.

The combined Subject Graph Type has four main sections:

1. ## Primary subjects: one literal-tab hierarchy rooted at Subject, showing kinds and source-backed classification-axis topics with their namespace and branch context. Exclude named instances, dependent properties, allowed property values and their descendants. A value-qualified narrower kind such as `Atom/Content Role: Plan` remains a kind, not a named Atom instance. Within CAPRMEDIO, keep Graph/Node, Graph/Relation and Graph/Rule as sibling branches beneath Graph; show Node/Project Model and Node/Aspect, and keep Carrier outside Graph. Retain selected project-specific namespaces. Namespace and classification-axis segments are context or topics, not extra entity kinds. Keep the bare `Atom/Content Role` axis visible and distinguish its meaning from role-qualified narrower Atom kinds. Named Relation Type declarations belong in section 3, not the primary tree.
2. ## Properties: one property detail section for every displayed primary with direct or inherited properties, following its first appearance in section 1. Keep source-backed classification-axis detail with that Subject; do not hide the bare `Atom/Content Role` Subject or collapse its identity into Atom. An axis does not acquire bearer Atom properties merely by occupying an intermediate path segment. Keep role-qualified narrower Atom kinds such as `Atom/Content Role: Plan` as separate sections where properties are present; those kinds inherit Atom properties. Show direct properties and additive source-backed inherited properties and allowed values. Mark inherited display entries as `[inherited]` only. Keep full source origins internally and retain all origins for equal-name entries; report conflicts without silently overriding a source. Preserve actual bearer Atom properties and role-specific descendants. Do not copy inherited properties into source Atoms.
3. ## Instances: show the selected named instances separately from their kinds, including Workflow instances, named Relation Type declarations and concrete Graph Rule Atoms. Retain the instance's defining kind, actual name and source-backed detail. Concrete Graph Rule declarations show their source-backed kind/name and bare defining CA-R ID. Their operative Claims remain in the source Atoms; the view does not copy their claim.* YAML, Claim text or file citations. This section is the named declaration level, not the actual Atom-to-Atom Relation tuples. Explicitly report unavailable or unsupported declaration details rather than guessing or omitting them.

4. ## Dependency-only subjects: list each exact canonical Subject path that occurs in subjects.depends_on and never explicitly in subjects.governs within this view's selected source Atoms. Use exact complete-string equality, including namespaces, without propagating ancestors or descendants. Show each path once with its sorted, deduplicated referring Atom IDs, sorting paths alphabetically. Keep the other sections intact; this report does not move or remove their targets or infer a missing-definition violation.

Use spaces, not tabs, for YAML frontmatter indentation and literal tabs for hierarchy depth inside fenced text blocks. Each tree line shows its local label and incoming operator, without a repeated full path or a space after the operator. Property-section headings use concise labels with enough branch context to distinguish equal local names, without repeating full canonical paths as display labels. The display uses `[inherited]` without exposing the full origin path; exact paths and origins remain in internal provenance/manifest. Section 4 retains the exact full paths required for its dependency-only report. Keep /, ., :, and // distinct. Render all present source-backed instances in section 3; do not limit it to Workflow instances if other kinds are present. Preserve source-declared order where present, otherwise sort alphabetically. No Terms Graph, construction tree, instance link graph or other main section is added.

The source Atoms remain authoritative for target and property identity. The view follows source of truth → Workflow → Projection: edit its authoritative sources, then rebuild it through its Workflow. The Markdown Projection is not edited directly. Directly edited Implementation is not classified as Projection merely because it realizes RMED. The Projection does not create a separate Revision entity, infer values from filenames or folders, change source authority, or require any Tool, MCP route, runtime namespace, or code-support gate.


For the combined Subject Graph Type, render its complete four-section form. An explicitly requested bounded excerpt of that combined Type must be labeled `Bounded main-Subject view — not a complete Subject Graph` and must not satisfy a full-graph request. The separately registered focused Types instead use their own specified complete bodies; they are not bounded excerpts of the combined Type.


Show defining Current Requirement Atoms by their bare CA-R IDs beside the Subjects they define. Do not copy definition or Claim text into the view, or add a Definitions table, file citation, hyperlink or inline Atom Version. The YAML sources list retains complete versioned provenance. A source is a defining reference only when it is a Current Requirement of Type Definition governing that Subject; do not label every governing Atom as its definition. A Subject without such a direct defining reference remains visible without an invented ID.

## Focused Type delivery

Deliver each focused Type in its own Markdown Carrier and stable Projection identity. Subject Graph Primary Subjects contains its primary hierarchy only. Subject Graph Properties contains a flat sequence of primary Subjects with at least one property and their inherited property details. Subject Graph Instances contains primary hierarchy and instance declarations. Subject Graph Dependency-only Subjects contains the selection-relative exact dependency-only list. Keep definition references as bare IDs and do not copy source definitions or Claims into any focused Carrier.

Use separate Type values for these four products. Retain the same declared selection across Types when the Operator requests comparable views. Record source Scope Units, the descendant option and Subject branches as query criteria, and retain actual versioned sources in YAML. A changed Type or named selection is resolved under the existing Projection-ID policy, not by repurposing another Type's ID.
