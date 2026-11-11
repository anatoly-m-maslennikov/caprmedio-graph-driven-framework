---
atom_id: CA-D-653@15-draft
ref_id: CA-D-653@15-draft
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: Entity/Object/Continuant/Projection
  dependencies:
  - Entity/Object/Continuant/Projection.Type
  - Entity/Object/Continuant/Selection
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Header.Identity.ID
  - Entity/Object/Continuant/Governing Objects/Atom.Header.State.Version Number
  - Entity/Carrier
  - Entity
  - Entity/Property
  - Entity/Object/Continuant/Governing Objects/Atom.Content Role
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Plan)'
tier: 3
relations:
  delivery_for:
  - CA-R-2150
  - CA-R-2221
  - CA-R-2222
  - CA-R-2223
  - CA-R-2224
  - CA-R-2225
status: Draft
version: 15
updated_at: 2026-10-30 08:49:46 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
## Summary

Deliver readable Subject Graph views as Markdown

## Claim scope

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

Declare the exact named source selection, including Scope Units, Roles and statuses. Current RMEDO is an available default, not a requirement to expand a narrower requested selection. Draft, Archived, derived Projection material and unselected scopes are excluded. Unresolved, malformed, inaccessible, or conflicting source claims remain visible as explicit limitations; none is silently converted into authority.

The combined Subject Graph Type has four main sections:

1. ## Primary subjects: one literal-tab hierarchy rooted at Entity, showing selected source-backed primary kinds and classification-axis topics in their declared branch context. Follow the governing Entity hierarchy in CA-R-1248 and the Subject Graph definition in CA-R-2150, preserving specialization and structural containment. Exclude named instances, dependent Property occurrences, allowed values and their descendants from this section; the direct `Entity/Property` branch declared by CA-R-1248 is a kind, not one of those bearer-qualified occurrences. A value-qualified narrower Atom kind such as `Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Plan)` remains a kind, not a named Atom instance. Retain selected project-specific namespaces; namespace segments are context, not extra entity kinds. `Entity/Object/Continuant/Governing Objects/Atom.Content Role` is the Atom's directly addressable Property and belongs in section 2 under its bearer. An Entity used as a classification axis retains its source-admitted identity; that use creates no intermediate Entity kind. Named Relation Type declarations belong in section 3, not the primary tree.
2. ## Properties: one property detail section for every displayed primary with direct or inherited properties, following its first appearance in section 1. When Atom's Content Role occurs in the selected source-backed property details, keep `Entity/Object/Continuant/Governing Objects/Atom.Content Role` visible under its bearer Atom with its own Property identity and admitted allowed values. The Property-to-bearer relation does not make Content Role a narrower Atom kind or transfer Atom's other properties to that Property. Keep role-qualified narrower Atom kinds such as `Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Plan)` as separate sections where properties are present; those kinds inherit Atom's applicable features and constraints. Show direct properties and additive source-backed inherited properties and allowed values. Mark inherited display entries as `[inherited]` only. Keep full source origins internally and retain all origins for equal-name entries; report conflicts without silently overriding a source. Preserve actual bearer Atom properties and role-specific descendants. Do not copy inherited properties into source Atoms.
3. ## Instances: show only the selected named Relation Type declarations with their bare defining R IDs and source-backed names. Do not enumerate Workflow instances, actual endpoint tuples or a retired Graph Rule catalogue. Constraints remain in the corresponding model definitions.

4. ## Dependency-only subjects: list each exact canonical Subject path that occurs in subjects.depends_on and never explicitly in subjects.governs within this view's selected source Atoms. Use exact complete-string equality, including namespaces, without propagating ancestors or descendants. Show each path once with its sorted, deduplicated referring Atom IDs, sorting paths alphabetically. Keep the other sections intact; this report does not move or remove their targets or infer a missing-definition violation.

Use spaces, not tabs, for YAML frontmatter indentation and literal tabs for hierarchy depth inside fenced text blocks. Each tree line shows its local label and incoming operator, without a repeated full path or a space after the operator. Property-section headings use concise labels with enough branch context to distinguish equal local names, without repeating full canonical paths as display labels. The display uses `[inherited]` without exposing the full origin path; exact paths and origins remain in internal provenance/manifest. Section 4 retains the exact full paths required for its dependency-only report. Keep /, ., :, and // distinct. Render only the selected source-backed named Relation Type declarations in section 3 under the declared source and branch selection. Preserve source-declared order where present, otherwise sort alphabetically. No Terms Graph, construction tree, instance link graph or other main section is added.

The source Atoms remain authoritative for target and property identity. The view follows source of truth → Workflow → Projection: edit its authoritative sources, then rebuild it through its Workflow. The Markdown Projection is not edited directly. Directly edited Implementation is not classified as Projection merely because it realizes RMED. The Projection does not create a separate Revision entity, infer values from filenames or folders, change source authority, or require any Tool, MCP route, runtime namespace, or code-support gate.


For the combined Subject Graph Type, render its complete four-section form. An explicitly requested bounded excerpt of that combined Type must be labeled `Bounded main-Subject view — not a complete Subject Graph` and must not satisfy a full-graph request. The separately registered focused Types instead use their own specified complete bodies; they are not bounded excerpts of the combined Type.


Show defining Current Requirement Atoms by their bare CA-R IDs beside the Subjects they define. Do not copy definition or Claim text into the view, or add a Definitions table, file citation, hyperlink or inline Atom Version. The YAML sources list retains complete versioned provenance. A source is a defining reference only when it is a Current Requirement of an applicable admitted Definition Type with a defining Claim governing that Subject; do not label every governing Atom as its definition. A Subject without such a direct defining reference remains visible without an invented ID.

### Focused Type delivery

Deliver each focused Type in its own Markdown Carrier and stable Projection identity. Subject Graph Primary Subjects contains its primary hierarchy only. Subject Graph Properties contains a flat sequence of primary Subjects with at least one property and their inherited property details. Subject Graph Instances contains primary hierarchy and selected source-backed named Relation Type declarations. Subject Graph Dependency-only Subjects contains the selection-relative exact dependency-only list. Keep definition references as bare IDs and do not copy source definitions or Claims into any focused Carrier.

Use separate Type values for these four products. Retain the same declared selection across Types when the Operator requests comparable views. Record source Scope Units, the descendant option and Subject branches as query criteria, and retain actual versioned sources in YAML. A changed Type or named selection is resolved under the existing Projection-ID policy, not by repurposing another Type's ID.

### Current source pin and pending adoption

Proposed N+1 successor of `/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-653-CORE_META_MODEL-ENG_DECISION--deliver-readable-subject-graph-views-as-markdown.md`, Atom `CA-D-653`, version `14`, SHA-256 `20e249a2b461932d848d668d0a689836d1533e6e15a7ab5aa17926571196e58a`. This source alignment follows the accepted CA-R-1531@21, CA-R-1248@24, CA-R-1284@24 and CA-R-2150@15 Draft successors; those sources remain pending publication. The existing Current source is unchanged. This temporary preparation performs no publication, native operation, generated-view rebuild or runtime change.
