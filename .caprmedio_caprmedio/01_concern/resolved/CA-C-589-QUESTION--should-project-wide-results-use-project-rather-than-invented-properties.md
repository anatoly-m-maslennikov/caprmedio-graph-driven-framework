---
atom_id: CA-C-589
content_role: Concern
type: Question
current_scope_unit: caprmedio
status: Resolved
author: Anatoly Maslennikov
tier: 3
version: 3
updated_at: 2026-10-24 14:20:44 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - Subject/Domain/Node/Continuant/Project
relations: {}
---
# Summary

Should project-wide results use Project rather than invented properties?

## Question

For a Requirement about a Project-wide result, is Project the sufficient
governed Subject when no distinct property has been approved?

## Scope

Only CA-R-007, CA-R-035, CA-R-1058, CA-R-1423 and CA-R-827 in the current
Candidate #7 Subject migration.

## Details

The provisional interpretation below is superseded by the Resolution.

Their existing text concerns traceability, necessary information acquisition,
authority for change, improvement from observed outcomes and Operator control.
Those are real requirements about the Project. They do not establish new
Project properties named Traceability, Information Necessity Assessment,
Authority Change, Improvement Support or Control.

Use the existing Project Subject and keep each specific result in the source
text. Remove only a redundant dependency on that same Project Subject. Do not
add new Domain entities or properties, change Summary/Substance, or claim the
five Requirements now mean the same thing. Subject and Content Role remain
independent.

This is the best bounded existing-topic choice under the Operator's instruction
to record small uncertainties and continue. Recheck the granularity during the
separate content review. This Question is not a new approval gate.

Checked against Candidate #7, its application plan, this chat's latest two days
of human input and the active MECE, DRY, necessity and coherence principles.
Existing Draft/Archive and C/A instance migration remain excluded. No
PROGRAMMATIC implementation is included.

## Resolution

The Operator's later clarification supersedes the initial Project answer:
the framework is the result of the project. Requirements for that product,
and most principles about it, concern the framework rather than Project.
The exact Subject is `Subject/Product: CAPRMEDIO Framework`.

Product, Domain, Engineering, UX, Design and Documentation are expandable
Subject branches. Graph remains shared for Relations and Rules. Product is
not another Local Scope Unit or Content Role. The Requirement can still live
at Project scope under its relevant principle; numeric Tier rules stay intact.

Review each source before correcting its Subject. Keep Project for requirements
about the project itself. Do not blanket-replace every Project Subject, invent
Framework.Traceability, or infer `/Framework` or `//` instead of the approved
product classifier. The five source corrections are not claimed applied by
this decision record. Their content and principle links need no guessed edits.
