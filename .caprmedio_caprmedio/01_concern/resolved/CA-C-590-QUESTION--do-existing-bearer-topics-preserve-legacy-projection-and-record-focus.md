---
atom_id: CA-C-590
content_role: Concern
type: Question
current_scope_unit: caprmedio
status: Resolved
author: Anatoly Maslennikov
tier: 3
version: 2
updated_at: 2026-10-24 18:16:36 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Engineering/Carrier
relations: {}
---
# Summary

Do existing bearer topics preserve legacy Projection and record focus?

## Question

Are these bounded mappings sufficiently precise without adding more Domain
entities or properties?

## Scope

Only the listed Subjects in the current Candidate #7 alias pass. Their source
text stays unchanged; this is not the later content migration.

## Details

- M149 and R1070 govern generation of both Project Scope Unit Graph and Sources
  Projections. Use existing Projection as their shared topic rather than
  reducing both to only one Projection Type. The two outputs remain explicit
  in the source text.
- E232 checks the governed file-change records in the Journal. Use existing
  Journal.Record; the exact file-change event and test remain in its text.
- R1450's old Atom/Carrier dependency concerns the representation inspected by
  the signature Tool. Use existing Carrier, not an invented Atom.Carrier
  property or the CARRIES relation merely because its name contains Carrier.
- E406's governed Subject Set dependency uses existing Atom.Subjects; its text
  still restricts the selection to GOVERNS. Its graph dependency uses the
  existing Entities Graph Projection Type. GOVERNS and DEPENDS_ON do not merge.

Review each source's exact applicability during the separate content review.
Do not infer a new general entity, rewrite a Claim, or treat this Question as
an approval gate. Candidate #7, the application plan, the latest two days of
human input and active principles were checked. The Operator authorized small
Questions followed by the best bounded choice and continued independent work.

## Resolution

The Operator's broader-governed-thing plus exact Content Scope decision
resolves these bounded choices without adding Domain entities. Current
M149/R1070 govern Projection and retain the distinct outputs in their text;
E232 governs Journal.Record; R1450 retains Carrier; E406 retains Atom.Subjects
and Entities Graph context. The GOVERNS-only restriction remains in its text.
Actual current fields were checked. This closes those alias choices, not
the remaining unrelated aliases, content review or runtime behavior.
