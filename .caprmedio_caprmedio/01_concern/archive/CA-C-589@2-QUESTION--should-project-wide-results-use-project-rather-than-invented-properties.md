---
atom_id: CA-C-589@2
content_role: Concern
type: Question
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
tier: 3
version: 2
updated_at: 2026-10-24 14:12:59 +0400
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

The Operator confirmed on 2026-10-24: "yes, the subject is project, it's R in project, core, under some principle".

Use Project as the Subject for these Project-wide Requirements. Keep the precise
required outcome and applicability boundary in the Atom content. The relevant
principle and existing graph relations provide its governing context; do not
invent a Project.Traceability property to repeat that outcome. "Core" here
does not restore a named Tier property or assign a new numeric Tier.

This resolves the Subject-granularity question. It does not merge the five
Requirements, change their content, assign an unevidenced principle link or
authorize new Domain properties. Later content review may still improve them.

