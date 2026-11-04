---
atom_id: CA-R-2117
content_role: Requirement
type: Rule
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-11-04 23:19:17 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
relations: {}
tier: 2
---
# Summary

Trace RMED obligations to their implementation owners

## Scope

The assessed PROGRAMMATIC implementation boundary: source modules and, when
identifiable, the functions, classes, or other implementation units that
materially realize active Requirement, Evaluation, Delivery, or Engineering
Decision Atoms. This includes Tools, Apps, MCP components, and workflows. It
does not automatically include vendor code, generated output, frozen fixtures,
or legacy history.

## Claim

Each assessed source module that materially realizes one or more applicable
active Requirement, Evaluation, Delivery, or Engineering Decision Atoms
**must** carry one header comment per Atom before its first code. A narrower set may also appear before an identifiable owning unit when useful. Each comment contains only the current Atom ID
and Version:

```text
# CA-R-2117@13
# CA-M-466@5
# CA-D-674@8
```

Do not add role labels, prose, headings, or an `implementation of` marker. Do
not cite a generic coding Policy merely because it guided implementation, or an
Atom merely called by the source. Many-to-many realization remains valid.

## Details

- A module or unit is an implementation owner only when it materially realizes
  the cited claim. A caller, dependency, test, relation, or projection alone
  does not establish realization.
- The comments are direct trace metadata, not proof of conformance, completion,
  or outcome. The authoritative Atom and observed implementation evidence
  remain required.
- The assessed source boundary applies to current admitted implementation work.
  Out-of-boundary files are reported for explicit disposition rather than
  mass-edited automatically.
- A missing or ambiguous current branch, an unidentifiable owner, or an invalid
  comment is a traceability gap. Preserve the source and report the gap; do not
  invent an Atom ID, parent, policy, or completion claim.
