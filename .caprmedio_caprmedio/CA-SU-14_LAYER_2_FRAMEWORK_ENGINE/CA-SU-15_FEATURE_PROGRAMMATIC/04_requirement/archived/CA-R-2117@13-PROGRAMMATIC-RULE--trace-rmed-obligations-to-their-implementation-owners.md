---
atom_id: CA-R-2117
ref_id: CA-R-2117@13
container:
  scope_unit: CA-SU-15
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
tier: 2
status: Archived
version: 13
updated_at: 2026-11-04 23:19:17 +0400
carrier_destination:
  file:
    name: CA-R-2117@13-PROGRAMMATIC-RULE--trace-rmed-obligations-to-their-implementation-owners.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archived
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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
