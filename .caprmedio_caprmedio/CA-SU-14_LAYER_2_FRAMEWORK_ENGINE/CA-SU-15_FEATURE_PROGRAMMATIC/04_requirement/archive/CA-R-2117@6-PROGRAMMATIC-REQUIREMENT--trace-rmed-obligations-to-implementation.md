---
atom_id: CA-R-2117@6
content_role: Requirement
type: Rule
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 10:48:25 +0400
subjects:
  governs: Subject/Engineering/Source Unit Responsibility
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
relations: {}
tier: 2
---
# Summary

Trace RMED obligations to their implementation owners

## Scope

The assessed PROGRAMMATIC implementation boundary: source modules and, when
identifiable, the functions, classes, or other implementation units that
materially realize active Requirement, Method, Evaluation, or Delivery Atoms.
This includes Tools, Apps, MCP components, workflows, and applicable policy
behavior. It does not automatically include vendor code, generated output,
frozen fixtures, or legacy history.

## Claim

Each assessed source module that materially realizes one or more applicable
active RMED Atoms **must** carry a structured `# implementation of:` block at
its module header. When the owning function, class, or other implementation
unit is identifiable, the same block **must** also appear immediately before
that unit and **must** be narrowed to the obligations it realizes.

The block **must** use only current Atom IDs and these role lines: `# Requirement:`,
`# Method:`, `# Evaluation:`, and `# Delivery:`. Empty roles **must** be omitted.
IDs are comma-separated and contain no version, path, or title. Select the
narrowest applicable direct RMED leaf for each relevant `child_of` or
`parent_of` branch, include applicable policy leaves such as error, retry, or
logging rules, do not repeat an ancestor already covered by that leaf, and cite
independent branches separately within the readable block. A branch-specific
block is optional when the owning unit needs that narrower locality. Many-to-many
realization remains valid.

## Details

- A module or unit is an implementation owner only when it materially realizes
  the cited claim. A caller, dependency, test, relation, or projection alone
  does not establish realization.
- The block is direct trace metadata, not proof of conformance, completion, or
  outcome. The authoritative Atom and observed implementation evidence remain
  required.
- The assessed source boundary applies to current admitted implementation
  work. Out-of-boundary files are reported for explicit disposition rather
  than mass-edited automatically.
- A missing or ambiguous current branch, an unidentifiable owner, or an invalid
  block is a traceability gap. Preserve the source and report the gap; do not
  invent an Atom ID, parent, policy, or completion claim.
